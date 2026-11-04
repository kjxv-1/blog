"""Build the tutorial feed, short permalinks and automatic tag navigation.

Opt in using ``tutorial: true`` in Markdown front matter. Generated pages stay
in memory; a normal MkDocs build is sufficient, including GitHub Pages CI.
"""

from __future__ import annotations

from collections import Counter
from datetime import date, datetime
import hashlib
from html import escape
import json
import math
import posixpath
import re
import unicodedata
from urllib.parse import urljoin

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File, InclusionLevel
from mkdocs.utils import get_relative_url
from mkdocs.utils.meta import get_data


PAGE_SIZE = 10
INDEX = "tutorials/index.md"
# One-time migration compatibility; authors do not need aliases in new articles.
LEGACY_URLS = {
    "bwg": "tools/Buy-Guide-Bwg/",
    "jtti": "tools/Buy-Guide-Jtti/",
    "nodemach": "tools/Buy-Guide-Nodemach/",
    "panstar": "tools/Buy-Guide-Panstar/",
}
_articles = []
_views = {}
_tags = []


def _date(value, field, path):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError as exc:
        raise PluginError(f"图文教程 {path} 的 {field} 应填写 YYYY-MM-DD 日期") from exc


def _slug(tag):
    slug = re.sub(r"[^\w-]+", "-", unicodedata.normalize("NFKC", tag).casefold()).strip("-")
    return slug or hashlib.sha256(tag.encode()).hexdigest()[:10]


def _read_minutes(body):
    text = re.sub(r"<[^>]*>|!\[[^\]]*\]\([^)]*\)", " ", body)
    chinese = len(re.findall(r"[\u3400-\u9fff]", text))
    words = len(re.findall(r"[A-Za-z0-9]+", text))
    return max(1, math.ceil(chinese / 300 + words / 200))


def _permalink(file, meta, config, files):
    original_dest = file.dest_uri
    slug = meta.get("slug")
    if slug is not None:
        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:[-_][a-z0-9]+)*", slug):
            raise PluginError(f"图文教程 {file.src_uri} 的 slug 仅支持小写字母、数字、连字符和下划线")
        if slug in {"tags", "common", "page", "posts", "index"}:
            raise PluginError(f"图文教程 {file.src_uri} 的 slug 与栏目保留路径重名：{slug}")
        dest = f"tutorials/{slug}/index.html" if config.use_directory_urls else f"tutorials/{slug}.html"
        if any(other is not file and other.dest_uri == dest for other in files):
            raise PluginError(f"图文教程 {file.src_uri} 的 slug 与其他页面重名：{slug}")
        file.dest_uri = dest
        for cached in ("url", "abs_dest_path"):
            file.__dict__.pop(cached, None)
    aliases = meta.get("aliases", [])
    if not isinstance(aliases, list):
        raise PluginError(f"图文教程 {file.src_uri} 的 aliases 应填写旧路径列表")
    if slug in LEGACY_URLS:
        aliases = [*aliases, LEGACY_URLS[slug]]
    redirects = [original_dest] if original_dest != file.dest_uri else []
    for alias in aliases:
        if not isinstance(alias, str) or not alias.strip("/"):
            raise PluginError(f"图文教程 {file.src_uri} 的旧路径不能为空")
        alias = alias.strip("/")
        if any(part in {".", "..", ""} for part in alias.split("/")) or re.search(r"[\\:?#%]", alias):
            raise PluginError(f"图文教程 {file.src_uri} 的 aliases 只能填写站内路径")
        redirects.append(alias if alias.endswith(".html") else alias + "/index.html")
    return list(dict.fromkeys(redirects))


def _redirect_file(src, target, config):
    redirect = File.generated(config, src, content="", inclusion=InclusionLevel.NOT_IN_NAV)
    relative = get_relative_url(target.url, redirect.url)
    script_url = json.dumps(relative, ensure_ascii=True).replace("<", "\\u003c")
    canonical = escape(urljoin(config.site_url or "/", target.url), quote=True)
    redirect.content_string = f'''<!doctype html>
<html lang="zh"><head><meta charset="utf-8">
<meta name="robots" content="noindex">
<link rel="canonical" href="{canonical}">
<meta http-equiv="refresh" content="0; url={escape(relative, quote=True)}">
<title>图文教程已迁移</title>
<script>const destination = new URL({script_url}, location.href);
destination.search = location.search; destination.hash = location.hash;
location.replace(destination.href);</script></head>
<body><a href="{escape(relative, quote=True)}">前往图文教程</a></body></html>'''
    return redirect


def on_files(files, config):
    global _articles, _views, _tags
    _articles, _views, _tags = [], {}, []
    redirects = []
    for file in list(files.documentation_pages()):
        body, meta = get_data(file.content_string)
        if meta.get("tutorial") is not True:
            continue
        if meta.get("draft") is True:
            file.inclusion = InclusionLevel.EXCLUDED
            continue
        title = meta.get("title")
        if not isinstance(title, str) or not title.strip():
            raise PluginError(f"图文教程 {file.src_uri} 缺少 title")
        tags = meta.get("tags", [])
        if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
            raise PluginError(f"图文教程 {file.src_uri} 的 tags 应填写非空文字列表")
        published = _date(meta.get("date"), "date", file.src_uri)
        updated = _date(meta["updated"], "updated", file.src_uri) if meta.get("updated") else None
        if updated and updated < published:
            raise PluginError(f"图文教程 {file.src_uri} 的 updated 不能早于 date")
        redirects.extend((src, file) for src in _permalink(file, meta, config, files))
        cover = meta.get("cover")
        if cover is not None and not isinstance(cover, str):
            raise PluginError(f"图文教程 {file.src_uri} 的 cover 应填写图片路径，或留空")
        if cover and not re.match(r"https?://", cover):
            cover = posixpath.normpath(posixpath.join(posixpath.dirname(file.src_uri), cover))
            if files.get_file_from_path(cover) is None:
                raise PluginError(f"图文教程 {file.src_uri} 的封面文件不存在：{cover}")
            cover = files.get_file_from_path(cover).url
        _articles.append({
            "file": file, "title": title.strip(), "description": meta.get("description", ""),
            "date": published, "updated": updated, "tags": list(dict.fromkeys(t.strip() for t in tags)),
            "pin": meta.get("pin") is True, "cover": cover, "read_minutes": _read_minutes(body),
        })
    # Stable tie-breaking keeps same-day articles in a predictable order.
    _articles.sort(key=lambda item: item["file"].src_uri)
    _articles.sort(key=lambda item: (item["pin"], item["date"]), reverse=True)
    counts = Counter(tag for article in _articles for tag in article["tags"])
    used_slugs = set()
    for tag, count in sorted(counts.items(), key=lambda pair: (-pair[1], pair[0].casefold())):
        slug = _slug(tag)
        if slug in used_slugs:
            slug += "-" + hashlib.sha256(tag.encode()).hexdigest()[:8]
        used_slugs.add(slug)
        _tags.append({"name": tag, "count": count, "src": f"tutorials/tags/{slug}/index.md"})

    def add_view(src, title, items, *, tag=None, common=False):
        total_pages = max(1, math.ceil(len(items) / PAGE_SIZE))
        page_files = []
        for number in range(1, total_pages + 1):
            page_src = src if number == 1 else src.removesuffix("index.md") + f"page/{number}/index.md"
            if page_src != INDEX:
                if files.get_file_from_path(page_src) is not None:
                    raise PluginError(f"图文教程自动页面与已有文件重名：{page_src}")
                meta = yaml.safe_dump({"title": title, "search": {"exclude": True}}, allow_unicode=True)
                content = f"---\n{meta}---\n\n# {title}\n"
                files.append(File.generated(config, page_src, content=content, inclusion=InclusionLevel.NOT_IN_NAV))
            page_files.append(files.get_file_from_path(page_src))
        for number, file in enumerate(page_files, start=1):
            _views[file.src_uri] = {
                "title": title, "items": items[(number - 1) * PAGE_SIZE:number * PAGE_SIZE],
                "count": len(items), "number": number, "pages": page_files,
                "tag": tag, "common": common,
            }

    add_view(INDEX, "图文教程", _articles)
    add_view("tutorials/common/index.md", "常用教程", [a for a in _articles if a["pin"]], common=True)
    for tag in _tags:
        add_view(tag["src"], f"标签：{tag['name']}", [a for a in _articles if tag["name"] in a["tags"]], tag=tag["name"])
        tag["url"] = files.get_file_from_path(tag["src"]).url
    for src, target in redirects:
        if src == target.dest_uri:
            continue
        existing = next((file for file in files if file.dest_uri == src), None)
        if existing:
            raise PluginError(f"图文教程旧网址与已有输出文件重名：{src}")
        files.append(_redirect_file(src, target, config))
    for article in _articles:
        article["file"].inclusion = InclusionLevel.NOT_IN_NAV
    for section in config.nav:
        if isinstance(section, dict) and "图文教程" in section:
            section["图文教程"] = [INDEX]
            break
    return files


def on_nav(nav, config, files):
    # Associate each tutorial with the top-level tab without flooding the
    # mobile site's main menu with every article and generated tag page.
    section = next(item for item in nav.items if item.title == "图文教程")
    for src in set(_views) | {a["file"].src_uri for a in _articles}:
        if src != INDEX:
            files.get_file_from_path(src).page.parent = section
    return nav


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri in _views:
        page.meta["template"] = "tutorial-index.html"
    elif any(a["file"].src_uri == page.file.src_uri for a in _articles):
        page.meta["template"] = "tutorial.html"
        page.meta["hide"] = [item for item in page.meta.get("hide", []) if item not in ("navigation", "toc")]
    return markdown


def on_page_context(context, page, config, nav):
    listing = _views.get(page.file.src_uri)
    article = next((a for a in _articles if a["file"].src_uri == page.file.src_uri), None)
    if listing is not None or article is not None:
        def entry_url(item):
            while item.is_section:
                item = item.children[0]
            return item.url

        context.update(
            tutorial_listing=listing, tutorial_article=article, tutorial_tags=_tags,
            tutorial_total=len(_articles), tutorial_common_count=sum(a["pin"] for a in _articles),
            tutorial_global_nav=[{"title": item.title, "url": entry_url(item), "active": item.active} for item in nav.items],
        )
    return context
