---
hide:
  - navigation
  - toc
---

<style>
  /* 复用 VPS 推荐页的宽度、表格间距和主题配色，仅作用于本页。 */
  .md-content__inner:has(.isp-recommend-page) { max-width: 1200px !important; margin: 0 auto !important; }
  .isp-recommend-page { min-width: 0; }
  .isp-recommend-page .isp-lead { margin: .8rem 0; color: var(--site-muted); font-size: .75rem; line-height: 1.8; }
  .isp-recommend-page .isp-quick-nav { display: flex; flex-wrap: wrap; gap: .5rem; margin: 1rem 0 1.5rem; }
  .isp-recommend-page .isp-quick-nav a { padding: .35rem .8rem; border: 1px solid var(--site-line); border-radius: 2rem; color: var(--site-ink); font-size: .7rem; line-height: 1.5; }
  .isp-recommend-page .isp-quick-nav a:hover,
  .isp-recommend-page .isp-quick-nav a:focus-visible { border-color: var(--site-teal); color: var(--site-teal); }
  .isp-recommend-page h2[id] { scroll-margin-top: 4.5rem; }
  .isp-recommend-page h2 { margin-top: 1.8rem; font-size: 1rem; text-align: left; }
  .isp-recommend-page .isp-section-note { margin: .5rem 0 .8rem; color: var(--site-muted); font-size: .7rem; line-height: 1.8; }
  .isp-recommend-page .isp-highlight { color: #c53030; font-weight: 700; }
  [data-md-color-scheme="slate"] .isp-recommend-page { --md-typeset-a-color: var(--site-teal); }
  [data-md-color-scheme="slate"] .isp-recommend-page .isp-highlight { color: #ff9797; }
  .isp-recommend-page code { background: var(--site-page); color: var(--site-ink); }
  .isp-recommend-page .isp-highlight code { color: inherit; }
  .isp-recommend-page .md-typeset__table { display: block; width: 100%; }
  .isp-recommend-page table:not([class]) { display: table; width: 100%; min-width: 1060px; table-layout: fixed; border-color: var(--site-line); background: var(--site-paper); color: var(--site-ink); font-size: .67rem; line-height: 1.75; }
  .isp-recommend-page table:not([class]) th,
  .isp-recommend-page table:not([class]) td { min-width: 0; padding: .65rem .55rem; vertical-align: top; overflow-wrap: anywhere; }
  .isp-recommend-page table th { background: var(--site-page); color: var(--site-ink); }
  .isp-recommend-page table th:nth-child(1) { width: 14%; }
  .isp-recommend-page table th:nth-child(2) { width: 21%; }
  .isp-recommend-page table th:nth-child(3) { width: 15%; }
  .isp-recommend-page table th:nth-child(4) { width: 15%; }
  .isp-recommend-page table th:nth-child(5) { width: 12%; }
  .isp-recommend-page table th:nth-child(6) { width: 11%; }
  .isp-recommend-page table th:nth-child(7) { width: 12%; }
  .isp-recommend-page table td:first-child strong { white-space: nowrap; }
  .isp-recommend-page table small { color: var(--site-muted); font-size: .62rem; }
  .isp-recommend-page .isp-video-links a { display: inline-flex !important; align-items: center; gap: .25rem !important; margin: .2rem .4rem .2rem 0 !important; padding: .25rem .6rem !important; border: 1px solid var(--site-line) !important; border-radius: 2rem !important; background: var(--site-paper) !important; color: var(--md-typeset-a-color) !important; font-size: .7rem !important; line-height: 1.5; }
</style>

<div class="isp-recommend-page" markdown="1">

[← 返回推荐资源](../index.md)

# 🌐 住宅 IP 平台与厂商推荐

<p class="isp-lead">先区分成品住宅代理与需要自行部署的住宅 VPS，再比较地区、独享方式、带宽和计费。这里集中整理平台简介、优惠和购买入口，具体操作放在独立图文教程中。</p>

<nav class="isp-quick-nav" aria-label="住宅 IP 推荐快速导航">
  <a href="#isp-platforms">住宅代理平台</a>
  <a href="#isp-vps">住宅 VPS 厂商</a>
  <a href="#isp-videos">视频与配置文档</a>
</nav>

> **选购先看产品类型：** 固定 IP、独享、ISP 归属和物理家宽是不同信息。检测网站的标签可用于参考，仍需结合实际出口、连接质量与使用需求判断；成品代理与住宅 VPS 的接入方式也不同。

## 🏠 住宅代理平台简介 { #isp-platforms }

<p class="isp-section-note">已有截图的平台已整理为独立教程；其余教程栏暂时留空。KiloProxy 信息核对日期：2026 年 11 月 9 日；原有平台介绍沿用本站资料，地区、带宽、价格和优惠请以下单页面为准。</p>

<!-- 维护约定：非具体商品入口统一为“官网／注册入口”；已有教程统一为“购买与首次使用教程”；无截图、未制作的教程留空，不建立占位文章。 -->

| 平台名称 | 产品与简介 | 地区与使用特点 | 带宽与计费 | 优惠码及优惠 | 购买入口 | 购买与首次使用教程 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KiloProxy** | 静态 ISP 分原生、广播线路；官网标注独享固定 IP，支持 HTTP／SOCKS5。另有按流量计费的动态住宅产品。 | 长期固定出口可比较静态 ISP；需自备可用的境外网络环境，地区以购买页为准。 | 静态 ISP <strong class="isp-highlight">6.99美元／条／月起</strong><br><strong class="isp-highlight">不限流量</strong>，带宽依地区、线路与套餐。 | 优惠码：<strong class="isp-highlight"><code>KJXVVIP9</code>（9折）</strong><br><small>适用范围与叠加规则以结算页为准</small> | [官网／注册入口](https://www.kiloproxy.com/?inviteCode=WCDDF3EG) |  |
| **NodeMach**<br>原 VIRCS | 美国 AT&T 住宅接入产品；已有截图可对照成品代理、专线隧道与住宅 VPS 的区别。 | 以美国住宅出口为主；截图中的检测结果仅代表当时样本。 | 代理与隧道套餐的带宽、流量不同；历史配置见教程，现价以官网为准。 | 邀请注册优惠以页面为准 | [官网／注册入口](https://www.nodemach.com/welcome?vcd=9467e966) | [购买与首次使用教程](../../tutorials/posts/Buy-Guide-Nodemach-ISP/index.md) |
| **Webshare** | Static Residential／ISP 代理；按共享级别、IP 数量与流量选择，Private 与 Dedicated 的独享程度不同。 | 本站历史实测以美国、英国为主；其他地区需单独测试，不代表平台仅提供这两个国家。 | 数量、流量额度和付款周期影响总价；截图旧价不作为当前售价。 | 本页未列专属优惠码 | [官网／注册入口](https://www.webshare.io/?referral_code=apnsjeua21if) | [购买与首次使用教程](../../tutorials/posts/Buy-Guide-Webshare/index.md) |
| **MIYAIP** | 静态住宅代理备选；本站已有购买与客户端配置演示。 | 是否可直连、可选国家及接入线路，按具体产品确认。 | 带宽、流量和付款周期以下单页为准。 | 优惠码：`V88D`<br><small>优惠以结算页为准</small> | [官网／注册入口](https://www.miyaip.com/?invitecode=1049297) |  |
| **985 Proxy** | 常规住宅／ISP 代理备选，按目标地区和使用需求比较。 | 下单前确认 IP 类型、地区与共享方式。 | 带宽与流量限制先向客服确认。 | 优惠码：`XIAOV007` | [官网／注册入口](https://l1.985proxy.com/?TN1AZJ) |  |
| **Talor** | 住宅代理备选，注册时填写邀请码。 | 具体产品类型、地区与独享规则以页面说明为准。 | 带宽和计费方式先向客服确认。 | 邀请码：`xiaov001` | [官网／注册入口](https://dashboard.talordata.com/reg?inviter_code=xiaov001) |  |
| **Kookeey** | 静态／动态代理平台，按固定出口或轮换需求选择产品。 | 地区覆盖与线路以当前产品列表为准。 | 静态与动态产品分别核对带宽、流量和计费方式。 | 本页未列专属优惠码 | [官网／注册入口](https://www.kookeey.com/?aff=86916142) |  |

**KiloProxy 选型补充：** 静态 ISP 按 IP 和使用周期购买，不按 GB 扣流量；动态住宅按 GB 计费，可轮换或使用短时粘性会话。官网另售静态数据中心代理，选购时请核对产品类型。<strong class="isp-highlight">不限流量不等于不限带宽。</strong>

<p class="isp-section-note">KiloProxy 资料来源：<a href="https://www.kiloproxy.com/static-isp-proxy">官方静态 ISP 说明</a>、<a href="https://www.kiloproxy.com/dynamic-residential-proxy">官方动态住宅说明</a>。上述产品特征为官方说明，本页未将其标注为本站实测结论。</p>

## 🖥️ 住宅 VPS 厂商简介 { #isp-vps }

住宅 VPS 提供服务器，需要自行部署代理或节点；与购买后直接获取地址、端口、账号、密码的成品代理不同。需中转时，尽量选择同国家或地区的入口服务器，并测试实际连接效果。

| 厂商名称 | 产品与简介 | 地区与使用特点 | 带宽与计费 | 优惠码及优惠 | 购买入口 | 购买与首次使用教程 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **丽萨主机**<br>LisaHost | 住宅／双 ISP 类 VPS，适合希望自行搭建代理的用户。 | 按具体套餐核对机房和 IP 类型。 | CPU、内存、带宽和流量依套餐；需要自行维护服务。 | 本页未列专属优惠码 | [官网／注册入口](https://lisahost.com/aff.php?aff=10639) |  |
| **Panstar** | 住宅／双 ISP 类 VPS，可配合入口 VPS 自建固定出口。 | 原推荐为美国住宅 VPS；其他地区以当前产品列表为准。 | 带宽与流量依套餐；需自行部署代理。 | [官方优惠活动](https://panstar.ai/activities?aff=DCAD1VCH) | [直达此套餐](https://panstar.ai/servers?regionId=6&productId=30&planId=480&cycle=12&aff=DCAD1VCH) |  |

📖 入口服务器可参考 [VPS 推荐表](../1-vps/index.md)。双 ISP VPS 的搭建演示见下方视频与配置文档。

## 🎬 视频与配置文档 { #isp-videos }

**Webshare：选购与链式代理配置** · [查看视频文档](../../blog/posts/2026-08-05-3x-ui/index.md)

<div class="isp-video-links" markdown="1">
--8<-- "includes/videos.md:webshare-2026"
</div>

**住宅 VPS：自建 SOCKS5 与中转配置** · [查看视频文档](../../blog/posts/2026-09-26-Multi-EasyGost/index.md)

<div class="isp-video-links" markdown="1">
--8<-- "includes/videos.md:Multi-EasyGost"
</div>

**MIYAIP：购买与客户端配置演示** · [查看视频文档](../../blog/posts/2026-07-17-MIYAIP/index.md)

<div class="isp-video-links" markdown="1">
--8<-- "includes/videos.md:MIYAIP-20260721"
</div>

</div>
