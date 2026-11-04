r"""Integration coverage for authoring without manually editing navigation.

Run: .venv\Scripts\python.exe -m unittest discover -s tests -v
"""

from pathlib import Path
import re
import tempfile
import unittest

import yaml
from mkdocs.commands.build import build
from mkdocs.config import load_config
from mkdocs.exceptions import Abort


ROOT = Path(__file__).resolve().parents[1]


class TutorialPublishingTests(unittest.TestCase):
    def test_automatic_discovery_filtering_and_static_pagination(self):
        with tempfile.TemporaryDirectory(prefix="blog-tutorials-test-") as temp:
            root = Path(temp)
            docs = root / "docs"
            docs.mkdir()
            (docs / "index.md").write_text("# 首页\n", encoding="utf-8")
            (docs / "tutorials").mkdir()
            (docs / "tutorials/index.md").write_text("# 图文教程\n", encoding="utf-8")

            def write_article(name, **extra):
                meta = dict(tutorial=True, title=name, date="2026-11-04", tags=["新标签", "申请流程"])
                meta.update(extra)
                path = docs / "tutorials/posts" / name / "index.md"
                path.parent.mkdir(parents=True)
                path.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n\n# " + name + "\n\n## 操作步骤\n\n正文。\n", encoding="utf-8")

            write_article("旧教程置顶", date="2026-10-01", pin=True)
            for number in range(11):
                write_article(f"教程{number:02}", date=f"2026-11-{number + 1:02}")
            write_article("草稿不能发布", draft=True)

            # No per-article or per-tag entries in this configuration.
            data = {
                "site_name": "测试站", "docs_dir": str(docs), "site_dir": str(root / "site"),
                "theme": {"name": "material", "language": "zh", "custom_dir": str(ROOT / "overrides"), "features": ["navigation.tabs", "navigation.indexes"]},
                "hooks": [str(ROOT / "hooks/tutorials.py")], "plugins": ["search"],
                "nav": [{"首页": "index.md"}, {"图文教程": ["tutorials/index.md"]}],
            }
            config_path = root / "mkdocs.yml"
            config_path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
            config = load_config(str(config_path))
            build(config)

            def page(relative):
                return (root / "site" / relative).read_text(encoding="utf-8")

            def cards(html):
                return re.findall(r'<article class="tutorial-card[^"]*">(.*?)</article>', html, re.S)

            first = page("tutorials/index.html")
            entries = cards(first)
            self.assertEqual(len(entries), 10)
            self.assertIn(">旧教程置顶</a></h2>", entries[0])
            self.assertIn(">教程10</a></h2>", entries[1])
            self.assertEqual(len(cards(page("tutorials/page/2/index.html"))), 2)
            tag = page("tutorials/tags/新标签/index.html")
            self.assertIn('data-tutorial-count="12"', tag)
            self.assertEqual(len(cards(page("tutorials/tags/新标签/page/2/index.html"))), 2)
            self.assertEqual(len(cards(page("tutorials/common/index.html"))), 1)
            article = page("tutorials/posts/旧教程置顶/index.html")
            self.assertRegex(article, r'md-tabs__item--active[^>]*>\s*<a[^>]*>\s*图文教程')
            heading_id = re.search(r'<h2 id="([^"]+)">操作步骤', article).group(1)
            self.assertIn(f'href="#{heading_id}"', article)
            self.assertFalse((root / "site/tutorials/posts/草稿不能发布/index.html").exists())
            self.assertNotIn("草稿不能发布", (root / "site/search/search_index.json").read_text(encoding="utf-8"))
            self.assertFalse((docs / "tutorials/tags").exists(), "Generated pages must not be written into source docs")

    def test_short_url_separate_cover_and_three_level_toc(self):
        with tempfile.TemporaryDirectory(prefix="blog-tutorial-permalink-") as temp:
            root = Path(temp)
            docs = root / "docs"
            source = docs / "tutorials/posts/a-long-folder-name"
            images = source / "images"
            images.mkdir(parents=True)
            (docs / "index.md").write_text("# 首页\n", encoding="utf-8")
            (docs / "tutorials/index.md").write_text("# 图文教程\n", encoding="utf-8")
            for name in ("cover.svg", "step.svg"):
                (images / name).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="9"/>', encoding="utf-8")
            meta = dict(tutorial=True, title="独立封面教程", date="2026-11-04", tags=["购买指引"],
                        slug="short-guide", cover="images/cover.svg", aliases=["tools/old-guide/"])
            body = "# 文章标题\n\n## 主要章节\n\n### 详细操作\n\n#### 操作补充\n\n![正文截图](images/step.svg)\n"
            (source / "index.md").write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n\n" + body, encoding="utf-8")
            (docs / "ordinary.md").write_text(body.replace("(images/step.svg)", "(tutorials/posts/a-long-folder-name/images/step.svg)"), encoding="utf-8")
            # Migrated guides keep their legacy URLs without an aliases field.
            (docs / "tutorials/posts/vendor.md").write_text("---\ntutorial: true\ntitle: 厂商教程\ndate: 2026-11-04\nslug: bwg\n---\n\n# 厂商教程\n", encoding="utf-8")
            config_data = {
                "site_name": "测试站", "site_url": "https://example.com/", "docs_dir": str(docs), "site_dir": str(root / "site"),
                "theme": {"name": "material", "language": "zh", "custom_dir": str(ROOT / "overrides"), "features": ["navigation.tabs"]},
                "hooks": [str(ROOT / "hooks/tutorials.py")], "plugins": ["search"],
                "nav": [{"首页": "index.md"}, {"图文教程": ["tutorials/index.md"]}, {"普通文档": "ordinary.md"}],
            }
            config_path = root / "mkdocs.yml"
            config_path.write_text(yaml.safe_dump(config_data, allow_unicode=True), encoding="utf-8")
            build(load_config(str(config_path)))
            output = root / "site"
            listing = (output / "tutorials/index.html").read_text(encoding="utf-8")
            article = (output / "tutorials/short-guide/index.html").read_text(encoding="utf-8")
            self.assertIn('href="short-guide/"', listing)
            self.assertIn('src="posts/a-long-folder-name/images/cover.svg"', listing)
            self.assertNotIn('step.svg', listing, "Body screenshots must not be used as covers")
            self.assertNotIn('cover.svg', article, "List covers must not be inserted into article content")
            self.assertIn('images/step.svg', article)
            for level in (1, 2, 3, 4):
                heading_id = re.search(fr'<h{level} id="([^"]+)"', article).group(1)
                if level <= 3:
                    self.assertIn(f'href="#{heading_id}"', article)
                else:
                    self.assertNotIn(f'href="#{heading_id}"', article)
            ordinary = (output / "ordinary/index.html").read_text(encoding="utf-8")
            third_id = re.search(r'<h3 id="([^"]+)"', ordinary).group(1)
            self.assertIn(f'href="#{third_id}"', ordinary, "Other columns must retain their original TOC levels")
            redirect = (output / "tools/old-guide/index.html").read_text(encoding="utf-8")
            self.assertIn('../../tutorials/short-guide/', redirect)
            self.assertIn('destination.hash = location.hash', redirect)
            self.assertIn('https://example.com/tutorials/short-guide/', redirect)
            legacy = (output / "tools/Buy-Guide-Bwg/index.html").read_text(encoding="utf-8")
            self.assertIn('../../tutorials/bwg/', legacy)
            self.assertTrue((output / "tutorials/posts/a-long-folder-name/index.html").exists())
            # Omitting the cover must not silently reuse the first body image.
            meta.pop("cover")
            (source / "index.md").write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n\n" + body, encoding="utf-8")
            build(load_config(str(config_path)))
            listing = (output / "tutorials/index.html").read_text(encoding="utf-8")
            self.assertIn('tutorial-card__placeholder', listing)
            self.assertNotIn('step.svg', listing)
            # A duplicate slug must fail explicitly instead of overwriting a tutorial.
            duplicate = docs / "tutorials/posts/duplicate.md"
            duplicate.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n\n# Duplicate\n", encoding="utf-8")
            with self.assertLogs("mkdocs.commands.build", level="ERROR") as captured:
                with self.assertRaises(Abort):
                    build(load_config(str(config_path)))
            self.assertIn("slug 与其他页面重名", "\n".join(captured.output))


if __name__ == "__main__":
    unittest.main()
