---
title: 搬瓦工 VPS 购买与首次使用图文教程
description: 搬瓦工套餐选择、注册结账、付款，以及通过 KiwiVM 安装系统、查看 IP 和 SSH 登录信息的图文指引。
tutorial: true
date: 2026-11-04
updated: 2026-11-04
tags: [VPS购买与首次使用图文教程]
pin: true
---

<style>
  .bwg-purchase-guide h2[id], .bwg-purchase-guide h3[id] { scroll-margin-top: 4.5rem; }
  .bwg-purchase-guide .bwg-guide-nav { display: flex; flex-wrap: wrap; gap: .5rem; margin: 1rem 0 1.4rem; }
  .bwg-purchase-guide .bwg-guide-nav a { padding: .35rem .7rem; border: 1px solid var(--site-line); border-radius: 2rem; color: var(--site-ink); font-size: .7rem; }
  .bwg-purchase-guide .bwg-guide-nav a:hover,
  .bwg-purchase-guide .bwg-guide-nav a:focus-visible { border-color: var(--site-teal); color: var(--site-teal); }
  .bwg-purchase-guide .bwg-highlight { color: #c53030; font-weight: 700; }
  [data-md-color-scheme="slate"] .bwg-purchase-guide .bwg-highlight { color: #ff9797; }
</style>

<div class="bwg-purchase-guide" markdown="1">

[← 返回 VPS 推荐表](../../recommend/1-vps/index.md) · [查看搬瓦工套餐对比](../2026-04-25-VPS-banwagong.md)

# 🖥️ 搬瓦工 VPS 购买与首次使用图文教程

本文按截图顺序，说明如何选择搬瓦工（BandwagonHost）套餐、注册并付款，以及购买后如何进入 **KiwiVM** 控制面板，安装系统并查看连接 VPS 所需的信息。

👉 **[进入搬瓦工官网](https://bwh81.net/aff.php?aff=81595)** · **[先查看本站套餐推荐](../2026-04-25-VPS-banwagong.md)**

<nav class="bwg-guide-nav" aria-label="搬瓦工购买与首次使用快速导航">
  <a href="#bwg-purchase">🛒 购买流程：第1～9步</a>
  <a href="#bwg-first-use">🔧 首次使用：第1～6步</a>
  <a href="#bwg-connect">🔑 直接查看连接信息</a>
</nav>

> 购买部分以截图中的 **40GB 电子商务系列套餐**为例，账单示例为 **89.99美元／季度**；首次使用部分展示的是另一台 **20GB 套餐 VPS**。两组图片用于演示操作路径，配置、价格、机房和库存请以自己的订单及官网实际显示为准。图片可点击放大查看。

## 🛒 搬瓦工购买指引 { #bwg-purchase }

### 第1步：选择 VPS 系列与机房

进入官网的 **「VPS Hosting／VPS 托管」** 页面，先选择需要的系列，再选择地区和数据中心。

截图中的系列入口包括 **「基础VPS」「电子商务VPS」「电子商务+SLA」「Ultra VPS」**。本例选择的是**电子商务 VPS**，不同系列的线路、配置和可选机房可能不同，选购时应对照自己需要的套餐。

![购买第1步：选择 VPS 系列，再选择地区和数据中心](images/purchase-01-series.png)

如果已经从本站推荐表的具体套餐链接进入，可以直接继续核对该产品的配置、付款周期和机房。

### 第2步：选择计费周期和地点

在产品配置页找到 **「计费周期」**，按需要选择季付、年付等页面提供的周期，再在 **「地点」** 中选择目标机房。

截图示例选择的是 **「季度价格89.99美元」**，地点为 **「美国－洛杉矶DC9 CN2GIA（USCA_9）」**。确认无误后点击 **「加入购物车」**。

![购买第2步：选择计费周期和目标机房，确认后加入购物车](images/purchase-02-cycle-location.png)

部分套餐支持后续在后台迁移机房，是否支持以及可迁移的范围，以所购套餐说明和控制面板显示为准。

### 第3步：核对购物车并结账

进入购物车后，检查**产品名称、机房、计费周期、当前应付金额和续费金额**，再点击 **「结账」**。

本教程不预填促销码。没有有效优惠码时，可将促销码一栏留空；如果之后有官方有效优惠，核验成功后再确认结算金额。

![购买第3步：核对订单摘要，促销码按实际情况填写，再点击结账](images/purchase-03-cart.png)

### 第4步：填写账户与联系信息

首次购买时，按页面要求填写账户资料。使用自己**能够正常收信的邮箱**，设置并确认账户登录密码；姓名、地址、国家或地区、电话等联系与账单信息，按实际情况及网站要求填写。

已有账户的用户，可通过页面上的登录入口登录后继续。截图中的资料仅用于展示填写位置，请使用自己的信息。

![购买第4步：填写账户邮箱、登录密码及联系和账单信息](images/purchase-04-account.png)

这里设置的是**搬瓦工网站账户的密码**；VPS 的 SSH 登录密码在后面的系统安装流程中获取。

### 第5步：选择付款方式并提交订单

继续向下查看付款方式，根据页面提供的选项选择。**「公用SSH密钥」** 为选填项：使用密钥登录时填写自己的公钥；本例未填写，首次使用部分按密码登录流程演示。

阅读服务条款，确认接受后勾选同意选项，再点击 **「完整订单」**。此时是提交订单，仍需继续完成后面的付款步骤。

![购买第5步：选择付款方式，阅读服务条款并提交完整订单](images/purchase-05-submit-order.png)

### 第6步：按提示完成联系验证

如果出现 **「Device Authentication／Contact verification」** 页面，查看自己邮箱收到的验证码，填入 **「Verification code」**，再点击 **「Verify and remember this device」**。

![购买第6步：出现联系验证时，填写自己收到的验证码并完成验证](images/purchase-06-verification.png)

未收到验证码时，可先检查垃圾邮件文件夹，再使用页面提供的重新获取或其他验证方式。若没有出现验证页面，继续处理订单即可。

### 第7步：打开未付款账单

在账单页面核对产品、机房、付款周期和应付金额。确认显示的是自己刚提交的订单后，点击 **「付款」**。

![购买第7步：核对未付款账单后点击付款](images/purchase-07-invoice.png)

### 第8步：选择实际支付渠道

在可用支付方式中选择自己准备使用的渠道。截图以**支付宝**为例，点击对应的支付宝付款按钮；也可以选择页面当时提供的其他可用方式。

![购买第8步：在可用支付方式中选择支付宝或其他渠道](images/purchase-08-payment-method.png)

### 第9步：完成支付并等待开通

跳转到支付页面后，核对商户、订单信息和金额，再使用支付宝扫描**自己订单页面生成的二维码**完成支付。本文截图中的二维码仅用于展示操作位置，请不要扫描它来付款。

![购买第9步：在自己订单的支付页面核对金额并扫码完成付款](images/purchase-09-payment.png)

支付完成后返回客户区，查看账单是否更新为已付款，并等待服务开通。若支付结果尚未同步，先核对支付记录和账单状态，再根据页面提示处理。

## 🔧 VPS 首次使用图文教程 { #bwg-first-use }

以下演示从客户区进入 KiwiVM，安装操作系统，再获取 SSH 登录信息。

!!! warning "安装或重装系统会清空数据"
    第3～5步用于需要安装或重装系统的服务器。已有服务或数据时，应先备份再决定是否重装。**如果系统已经可用，只想查看连接信息，可以跳过第3～5步，直接查看第6步，并使用已有登录凭据。**

### 第1步：进入客户区的我的服务

登录搬瓦工账户，点击 **「Client Area／客户区」**，再展开 **「Services／服务」**，选择 **「My Services／我的服务」**。

![首次使用第1步：登录客户区，从服务菜单进入我的服务](images/first-use-01-my-services.png)

### 第2步：打开 KiwiVM 控制面板

在服务列表中找到自己的 VPS，点击右侧管理栏的**齿轮按钮**，选择 **「Open KiwiVM／打开 KiwiVM」**。

![首次使用第2步：点击服务管理齿轮，选择打开 KiwiVM](images/first-use-02-kiwivm.png)

### 第3步：准备装机时先停止服务器

进入 KiwiVM 后，点击左侧 **「Main controls」**，在主控制页面点击 **「Stop」**，等待服务器停止后再进行系统安装。

![首次使用第3步：进入 Main controls，并点击 Stop 停止服务器](images/first-use-03-stop.png)

如果只是查看 IP 和端口，不需要执行这一步。

### 第4步：选择并安装操作系统

点击左侧 **「Install new OS」**，在系统列表中选择所需版本。截图选择的是 **「ubuntu-24.04-x86_64」**；后续搭建教程若有版本要求，以对应教程要求为准。

确认不需要保留服务器上的原有数据后，勾选页面中的**永久清除现有数据确认项**，再点击 **「Reload」**，按提示开始安装。

![首次使用第4步：在 Install new OS 中选择系统，确认清除数据后点击 Reload](images/first-use-04-install-os.png)

### 第5步：保存新密码与 SSH 端口

提交安装后，页面会显示本次安装生成的**临时 root 密码**及 **「SSH Port」**。先复制并妥善保存自己的密码和端口，再点击 **「Go back」**。

![首次使用第5步：复制保存新生成的临时 root 密码和 SSH 端口，再返回](images/first-use-05-password.png)

等待系统安装完成，并留意页面状态及邮件通知；安装期间不要重复提交重装操作。后续连接时使用这次安装生成的密码，旧系统的密码不再适用。

### 第6步：查看连接信息并登录 VPS { #bwg-connect }

回到 **「Main controls」**，查看公网 IP、SSH 端口及服务器运行状态。待服务器处于可用状态后，将以下信息填写到 FinalShell 等 SSH 客户端：

- **主机地址：** 自己面板中的 **「Public IP address」**，按需要使用 IPv4 或 IPv6 地址。
- **SSH 端口：** 自己面板中的 **「SSH Port」**；截图示例为 `22`，实际以面板显示为准。
- **用户名：** 本例 Linux 系统使用 `root`。
- **密码：** 第5步保存的本次安装生成的密码；如果没有重装，则使用自己现有的登录密码或密钥。

![首次使用第6步：在 Main controls 查看公网 IP 和 SSH 端口，配合保存的密码连接 VPS](images/first-use-06-connect.png)

请使用自己服务器的实际连接信息。搬瓦工网站账户、KiwiVM 控制面板和 VPS 的 SSH 登录属于不同入口，**SSH 客户端中应填写 VPS 的登录凭据**。

[← 返回 VPS 推荐表](../../recommend/1-vps/index.md) · [查看搬瓦工套餐对比](../2026-04-25-VPS-banwagong.md)

</div>
