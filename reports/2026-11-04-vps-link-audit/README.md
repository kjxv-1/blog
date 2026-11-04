# VPS 推荐文档链接检查报告

检查日期：2026年11月4日（北京时间）
检查对象：`docs/recommend/1-vps/index.md`，包含该页插入的 5 个搭建视频链接；并对照公开网站 `https://kjxv.net/recommend/1-vps/`。

## 结论

- 共检查 **67 处链接**：32 处厂商购买／活动入口、5 处视频、30 处站内页面或章节链接。重复网址只请求一次，再按出现位置汇总。
- **32／32 处商业入口均附有对应推广参数，未发现遗漏或与本次比对基准不一致的值。** 公开网站上的 32 处商业入口也全部匹配。
- **站内 30／30 处链接正常**：本地预览与公开网站均返回 HTTP 200，7 个带章节定位的网址也全部找到目标标题。
- **视频 5／5 个确认有效**：通过 YouTube 官方 oEmbed 接口取得视频信息，作者均为“科技小V”。直接联网测试最初超时，改用电脑原有的本地代理后全部通过；没有修改系统代理设置。
- 商业入口去重后共 16 个网址，其中 **14 个 HTTP 返回 200，2 个触发访问验证**。页面返回 200 不等同于当前可下单或推广佣金已归属，例外详见下方。

## 需要留意的项目

1. **搬瓦工 `pid=87`、`pid=44`：商品地址和推广跟踪正常，当前商品页显示 Out of Stock，暂时不能下单。** 这不是地址 404。本次遵照你的文案规则，没有把库存标签重新加回推荐表。
2. **NodeMach：** 邀请入口带有 `vcd=9467e966`；HTTP 跳转到注册页，并观察到 `referral` Cookie，后续页面触发 Cloudflare 验证，无法完成邀请人展示及注册流程核对。
3. **VMiss：** 原始入口带有 `aff=3992`，但返回 Cloudflare 验证页，未能确认落地页面和推广 Cookie。不能仅据此判定链接失效。
4. **Panstar：** 5 个独立网址均带有 `aff=DCAD1VCH`，HTTP 请求返回 200、查询参数保留；浏览器复核触发安全验证，尚未确认每个 `planId` 实际选中的配置及后续邀请归属。
5. **推广码归属边界：** 本次比对的是仓库和既有推广入口中的代码，没有登录你的推广后台。可确认源码参数和可观察的跟踪标记，实际注册／订单佣金归属仍以厂商后台为准。

## 推广参数汇总

| 厂商 | 本页出现次数 | 应有参数 | 核对结果 | 跟踪观察 |
| --- | ---: | --- | --- | --- |
| 搬瓦工 | 6 | `aff=81595` | 源码全部匹配 | 观察到 WHMCSAffiliateID，值匹配；两款商品缺货 |
| NodeMach | 3 | `vcd=9467e966` | 源码全部匹配 | 邀请入口带码，注册页遇验证；存在 referral Cookie |
| JTTI | 5 | `k=T7KBH7` | 源码全部匹配 | 浏览器写入 k Cookie，值匹配 |
| VMiss | 5 | `aff=3992` | 源码全部匹配 | 验证页阻止继续检查 |
| Panstar | 11 | `aff=DCAD1VCH` | 源码全部匹配 | HTTP 查询参数保留，浏览器验证未通过 |
| 华纳云 | 2 | `k=kejixiaov` | 源码全部匹配 | 浏览器写入 k Cookie，值匹配 |

站内教程、页内导航和 YouTube 视频不属于厂商商业入口，不需要附加厂商推广码。优惠码（例如 `10%OFF`）与推广码不是同一项；本次未尝试下单验证优惠折扣。

## 商业入口逐项结果

| 厂商／用途 | 原始链接 | 次数 | HTTP | 结果 |
| --- | --- | ---: | ---: | --- |
| JTTI · 官网／分类入口 | [官网／分类入口](https://www.jtti.cc/?k=T7KBH7) | 1 | 200 | 页面响应正常；推广参数匹配 |
| JTTI · 官网／分类入口 | [官网／分类入口](https://www.jtti.cc/zh/light_cloud.html?k=T7KBH7) | 4 | 200 | 页面响应正常；推广参数匹配 |
| NodeMach · 官网／分类入口 | [官网／分类入口](https://www.nodemach.com/welcome?vcd=9467e966) | 3 | 403 | 访问验证拦截，落地结果未确认 |
| Panstar · 活动页 | [活动页](https://panstar.ai/activities?aff=DCAD1VCH) | 5 | 200 | HTTP 200、参数保留；浏览器验证限制，配置未确认 |
| Panstar · 官网／分类入口 | [官网／分类入口](https://panstar.ai/register?aff=DCAD1VCH) | 1 | 200 | HTTP 200、参数保留；浏览器验证限制，配置未确认 |
| Panstar · 官网／分类入口 | [官网／分类入口](https://panstar.ai/servers?regionId=6&productId=15&planId=393&cycle=1&aff=DCAD1VCH) | 1 | 200 | HTTP 200、参数保留；浏览器验证限制，配置未确认 |
| Panstar · 官网／分类入口 | [官网／分类入口](https://panstar.ai/servers?regionId=7&productId=21&planId=236&cycle=1&aff=DCAD1VCH) | 2 | 200 | HTTP 200、参数保留；浏览器验证限制，配置未确认 |
| Panstar · 官网／分类入口 | [官网／分类入口](https://panstar.ai/servers?regionId=8&nodeId=18&productId=24&planId=272&cycle=1&aff=DCAD1VCH) | 2 | 200 | HTTP 200、参数保留；浏览器验证限制，配置未确认 |
| VMiss · 官网／分类入口 | [官网／分类入口](https://app.vmiss.com/aff.php?aff=3992) | 5 | 403 | 访问验证拦截，落地结果未确认 |
| 华纳云 · 官网／分类入口 | [官网／分类入口](https://www.hncloud.com/light_cloud.html?k=kejixiaov) | 2 | 200 | 页面响应正常；推广参数匹配 |
| 搬瓦工 · 官网／分类入口 | [官网／分类入口](https://bwh81.net/aff.php?aff=81595) | 1 | 200 | 页面响应正常；推广参数匹配 |
| 搬瓦工 · 商品 pid=134 | [商品 pid=134](https://bwh81.net/aff.php?aff=81595&pid=134) | 1 | 200 | 页面响应正常；推广参数匹配 |
| 搬瓦工 · 商品 pid=173 | [商品 pid=173](https://bwh81.net/aff.php?aff=81595&pid=173) | 1 | 200 | 页面响应正常；推广参数匹配 |
| 搬瓦工 · 商品 pid=44 | [商品 pid=44](https://bwh81.net/aff.php?aff=81595&pid=44) | 1 | 200 | 商品地址有效；当前缺货，无法下单 |
| 搬瓦工 · 商品 pid=87 | [商品 pid=87](https://bwh81.net/aff.php?aff=81595&pid=87) | 1 | 200 | 商品地址有效；当前缺货，无法下单 |
| 搬瓦工 · 商品 pid=95 | [商品 pid=95](https://bwh81.net/aff.php?aff=81595&pid=95) | 1 | 200 | 页面响应正常；推广参数匹配 |

搬瓦工 `pid=173`、`pid=134`、`pid=95` 已进入商品配置页面，识别到的地区分别为新加坡、大阪、香港。检测过程中使用独立临时会话，没有提交订单或付款。

## 站内页面与章节

下表按网址去重。公开网站与本地预览均已检查；“—”表示链接未指定章节。

| 公开网址 | 出现次数 | 本地 HTTP | 线上 HTTP | 章节定位 |
| --- | ---: | ---: | ---: | --- |
| [/recommend/](https://kjxv.net/recommend/) | 1 | 200 | 200 | — |
| [/recommend/1-vps/#vps-budgets](https://kjxv.net/recommend/1-vps/#vps-budgets) | 1 | 200 | 200 | 本地和线上均存在 |
| [/recommend/1-vps/#vps-regions](https://kjxv.net/recommend/1-vps/#vps-regions) | 1 | 200 | 200 | 本地和线上均存在 |
| [/recommend/1-vps/#vps-vendors](https://kjxv.net/recommend/1-vps/#vps-vendors) | 1 | 200 | 200 | 本地和线上均存在 |
| [/tutorials/bwg/](https://kjxv.net/tutorials/bwg/) | 6 | 200 | 200 | — |
| [/tutorials/jtti/](https://kjxv.net/tutorials/jtti/) | 1 | 200 | 200 | — |
| [/tutorials/jtti/#jtti-hk](https://kjxv.net/tutorials/jtti/#jtti-hk) | 2 | 200 | 200 | 本地和线上均存在 |
| [/tutorials/jtti/#jtti-jp](https://kjxv.net/tutorials/jtti/#jtti-jp) | 2 | 200 | 200 | 本地和线上均存在 |
| [/tutorials/nodemach/](https://kjxv.net/tutorials/nodemach/) | 3 | 200 | 200 | — |
| [/tutorials/panstar/](https://kjxv.net/tutorials/panstar/) | 3 | 200 | 200 | — |
| [/tutorials/panstar/#panstar-de](https://kjxv.net/tutorials/panstar/#panstar-de) | 2 | 200 | 200 | 本地和线上均存在 |
| [/tutorials/panstar/#panstar-us](https://kjxv.net/tutorials/panstar/#panstar-us) | 1 | 200 | 200 | 本地和线上均存在 |
| [/tutorials/vmiss/](https://kjxv.net/tutorials/vmiss/) | 6 | 200 | 200 | — |

## 视频链接

| 视频 | 链接 | 官方接口 | 作者 |
| --- | --- | --- | --- |
| 🌍【2026】最新VPN搭建教程：小白也能学会的云服务器自建梯子指南丨独享节点+全球住宅IP | [观看视频](https://www.youtube.com/watch?v=15nfkz7M4Hk&t=134s) | HTTP 200，有效 | 科技小V |
| 💻 DMIT、搬瓦工连不上？VPS被墙解决方案｜IPv6节点优先，HY2搭建、换IP与备用VPS | [观看视频](https://youtu.be/rl2b9WKhySk) | HTTP 200，有效 | 科技小V |
| 💥跨境直播网络搭建保姆级教程丨TikTok/独立站通用住宅IP链式代理 + 推特、油管实测数据 | [观看视频](https://www.youtube.com/watch?v=vnPZRPD6AB8) | HTTP 200，有效 | 科技小V |
| 50元以内VPS推荐：低预算也能拥有精品线路（CN2｜9929｜CMIN2）｜VPN搭建｜VPS搭建 | [观看视频](https://youtu.be/dQO0tH9XIgY) | HTTP 200，有效 | 科技小V |
| 2026丨（0基础）小白VPS节点搭建教程，有手就行！丨VPS搭建v2rayn丨VPS推荐 | [观看视频](https://www.youtube.com/watch?v=V7AN_wtpaDQ&t=4s) | HTTP 200，有效 | 科技小V |

## 本次操作与文件

- 未修改推荐文档的文字、商品地址、价格、优惠码或推广参数。
- 未注册账户、登录推广后台、提交订单、付款或发送消息。
- 检查输出保存在本目录，不属于网站的 `docs` 公开页面。
- 明细表：[links.csv](links.csv)。
- 页面原始链接清单：[inventory.json](inventory.json)。
- HTTP 检测记录：[results.json](results.json)。
- 浏览器与视频复核：[browser-results.json](browser-results.json)。
- 公开页面推广参数核对：[deployed-page-check.json](deployed-page-check.json)。

检查完成后按你的要求执行正常关机。关机执行记录见本目录的 `shutdown-status.txt`（后台执行时写入）。
