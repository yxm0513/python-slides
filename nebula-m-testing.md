title: 浅谈Nebula-M 测试实践
speaker: yangxinming
transition: cards
prismTheme: dark
css:
    - css/base.css
js:
    - js/zoom.js
    - js/base.js
plugins:
    - echarts
    - mermaid
    - katex


<slide class="bg-black-blue aligncenter zoomIn" image="https://source.unsplash.com/C1HhAQrbykQ/">

# 浅谈Nebula-M 测试实践 {.text-landing.text-shadow}

By ![](https://avatars3.githubusercontent.com/u/73510?s=60&u=200063d372fefbd51de767b8e258de0024d45e52&v=4){.avatar-40} YangXinMing \[SCG-NP-IDEA\] {.text-intro} 


---

:::div
<img src="/img/nodeppt_md.png" width="200" class="bounceInLeft slow" onclick="myfunction(this)"> 
:::
Powered by nodeppt 2.0 {.text-subtitle.bounceInLeft.slow}



<slide class="grid vertical-align content-center fullscreen">
## Agenda {.zoomIn}
---
:::div {.mydiv}
 * 关于Nebula-M {.bounceInRight}
 * 关于我们的测试实践{.bounceInRight}
 * Q&A {.bounceInRight}
{.build}
:::

<slide class="grid vertical-align fullscreen slideInLeft" image="https://source.unsplash.com/n9WPPWiPPJw/">
:::column {.white}
!![](/img/waiguan.png .fadeInUp.delay-400)

---
:::div 
#### Releases
<br>
*From 2019.05.30 To 2020.03.26 More Than 16 Releases* {.bounceInLeft.tobuild}
 * 硬件 {.bounceInLeft.tobuild}
   * 一代TX2平台, 二代3559A平台 {.bounceInLeft.tobuild}
   * 研扬，宝德，天地 {.bounceInLeft.tobuild}
 * 软件  {.bounceInLeft.tobuild}
   * 标准版\: v1.0.0 v1.2.0 v1.3.0 v2.0.0 v2.0.x {.bounceInLeft.tobuild}
   * MQTT版\: v1.0.0 v1.2.0 v2.0.0 {.bounceInLeft.tobuild}
   * 国际版，社区版，测温版，蓝光版 \.etc {.bounceInLeft.tobuild}
{.description}
:::

<slide class="grid vertical-align fullscreen slideInLeft">
<div class="aligncenter content-center">
<h4> Timeline </h4>
<ul class="timeline">
	<li>
		<div class="direction-r">
			<div class="flag-wrapper">
				<span class="flag">标准版 V1.0.0 </span>
				<span class="time-wrapper"><span class="time">2019.05.30</span></span>
			</div>
			<div class="desc">仅仅对接深广需求，简单网络配置,基本功能实现 (研扬&宝德)</div>
		</div>
	</li>
	<li>
		<div class="direction-l">
			<div class="flag-wrapper">
				<span class="flag">标准版 V1.1.0</span>
				<span class="time-wrapper"><span class="time">2019.07.22</span></span>
			</div>
			<div class="desc">
定制版-对接SF&SU
定制版-mqtt对接深广用户
标准版，临时给出支持案场项目
定制版-mqtt对接深广用户
定制版-mqtt对接深广用户
</div>
		</div>
	</li>
	<li>
		<div class="direction-r">
			<div class="flag-wrapper">
				<span class="flag">标准版 V1.1.2</span>
				<span class="time-wrapper"><span class="time">2019.09.02</span></span>
			</div>
			<div class="desc">1.【新功能】抓拍策略与通道绑定
2.【新功能】批量入库支持属性提取
3.【新功能】支持最小人脸像素设置
4.【新功能】视频流接入支持GB28181协议
5. 【新增】针对纯抓拍模式，ROI默认为全尺寸
</div>
		</div>
	</li>
    <li>
        <div class="direction-l">
            <div class="flag-wrapper">
                <span class="flag">标准版 V1.1.3</span>
                <span class="time-wrapper"><span class="time">2019.09.07</span></span>
            </div>
            <div class="desc">
相机接入，ONVIF
</div>
        </div>
    </li>
    <li>
        <div class="direction-r">
            <div class="flag-wrapper">
                <span class="flag">MQTT V1.1.1</span>
                <span class="time-wrapper"><span class="time">2019.09.29</span></span>
            </div>
            <div class="desc">MQTT 推送修改，问题修复</div>
        </div>
    </li>
    <li>
        <div class="direction-l">
            <div class="flag-wrapper">
                <span class="flag">标准版 V1.2</span>
                <span class="time-wrapper"><span class="time">2019.11.29</span></span>
            </div>
            <div class="desc">
人脸属性
人体属性
</div>
        </div>
    </li>
    <li>
        <div class="direction-r">
            <div class="flag-wrapper">
                <span class="flag">MQTT V1.2,Telecom V1.2</span>
                <span class="time-wrapper"><span class="time">2019.12.17</span></span>
            </div>
            <div class="desc">MQTT 版本随主线升级, Telecom 需求支持</div>
        </div>
    </li>
    <li>
        <div class="direction-l">
            <div class="flag-wrapper">
                <span class="flag">标准版 V2.0.1</span>
                <span class="time-wrapper"><span class="time">2020.01.21</span></span>
            </div>
            <div class="desc">
新硬件适配，接入协议
抓拍机接入
支持GB28181
鉴权
视频图片流混合接入
人体特征
人脸信息
网络继电器状态
</div>
        </div>
    </li>
    <li>
        <div class="direction-r">
            <div class="flag-wrapper">
                <span class="flag">测温版 V1.0</span>
                <span class="time-wrapper"><span class="time">2020.02.13</span></span>
            </div>
            <div class="desc">
支持智能测温检测告警
支持未佩戴口罩检测告警
支持热成像相机视频流接入预览， 
支持SDK接入测温告警事件
V1.0版本最大支持2路热成像相机接入处理
支持热成像相机可见光视频预览
支持热成像相机热成像视频预览
支持测温疑似发热弹窗预警，并列表展示
支持测温预警复核确认功能，复核确认疑似发热人员正常/发热状态并录入系统显示
支持未佩戴口罩告警弹窗提示，并列表展示
V1.0版本仅支持100条发热预警缓存，满覆盖方式，首页预警列表展示，不在历史记录查询
V1.0版本暂不支持测温历史记录检索功能
</div>
        </div>
    </li>
    <li>
        <div class="direction-l">
            <div class="flag-wrapper">
                <span class="flag">测温版 V1.1</span>
                <span class="time-wrapper"><span class="time">2020.02.19</span></span>
            </div>
            <div class="desc">
新增支持戴口罩人脸识别
优化最大支持4路热成像相机接入处理
新增支持戴口罩人脸比对告警弹窗提示，并首页列表展示
支持测温疑似发热记录存储和分类（复核确认、正常、发热三类状态）
支持未佩戴口罩告警记录存储
支持戴口罩人脸识别告警记录存储
支持测温历史记录按时间、通道、状态查询检索
支持未佩戴口罩、识别告警记录按时间、通道查询检索
各类告警类型统计报表功能
新增所有功能API接口开放
</div>
        </div>
    </li>
</ul>
</div>

<slide class="grid vertical-align fullscreen slideInRight">
:::column
!![](/img/thermo.png .fadeInUp.delay-400)

---
:::div {.alignright}
#### 测温版{.bounceInLeft}
 * 测温相机接入 {.tobuild.bounceInLeft}
 * 测温告警 {.tobuild.bounceInLeft}
 * 佩戴口罩对比 {.tobuild.bounceInLeft}
 * 未佩戴口罩告警 {.tobuild.bounceInLeft}
{.description}
:::

<slide class="grid vertical-align fullscreen slideInLeft">
:::card {.card-70 .bg-blue .fadeInUp}

## Nebula-M 是什么？
 * 商汤星云M系列智能边缘节点基于深度学习技术，是软硬件一体的嵌入式产品系列。 {.animated.zoomIn}
 * SenseNebula-M 为摄像机、抓拍机等多种采集设备提供接入能力，支持人脸识别、人体分析等多算法融合，具有信号联动控制、数据 汇聚、云边协同等功能，为行业解决方案提供商、集成商、代理商提供适配多种场景的智能化产品和解决方案。{.animated.zoomIn.delay-400} 
---
![](/img/nebula-m.png)

:::

<slide class="fullscreen slideInRight">
### 说人话 = 提供算力,人脸,人体等分析功能 {.aligncenter.text-landing.zoomIn}
<img src="/img/deploy.png" class="aligncenter fadeInUp delay-400" onclick="myfunction(this)">

<slide class="fullscreen">
### 产品功能 {.aligncenter.text-landing.zoomIn} 
---
:::column {.build}
#### 视频接入 
 * 支持网络摄像机 ONVIF、RTSP、GB28181 标准协议
 * 支持视频编码格式 H.264
 * 支持最大视频分辨率 1080P
 * 支持人脸检测感兴趣区域设置
 * 支持最小、最大人脸像素设置

#### 图片接入
 * 支持 SenseDLC AA 系列、11 系列、D 系列、T 系列抓拍机接入
 * 支持其他主流厂家抓拍机等抓拍设备 SDK 二次开发接入

#### 人像库
 * 支持黑/白名单库新增、编辑、删除，人像库图片导入、导出、编辑、删除

---
#### 人脸功能
 * 人脸检测、跟踪、抓拍，抓拍及告警记录查看、条件检索、导出
 * 支持人脸 1:1、1:N 比对，返回相似度等信息
 * 人脸小图、场景大图、人脸质量分数、人脸属性推送
 * 人脸属性包括年龄、性别、胡子、口罩、眼镜、帽子等

#### 人体功能
 * 人体检测、跟踪、抓拍，抓拍记录查看、条件检索、记录导出
 * 人体属性包括朝向、年龄、性别、帽子、头发、上衣、下衣、鞋子、口罩、雨伞、箱包等

#### 信号联动
 * 网络继电器信号联动控制

:::
<slide class="grid vertical-align fullscreen">
:::column
#### 我们是如何测试的{.zoomIn} 
 * 15+ x 摄像头 {.fadeInUp} 
 * 2+ x 继电器 {.fadeInUp}
 * 1 x 台式机 + 1 x 显示器{.fadeInUp}
 * 1 x 服务器{.fadeInUp}
 * Nebula-M 若干{.fadeInUp}
 * 路由器，交换机，智能插座若干{.fadeInUp}
{.description.text-intro.build}
---
<img src="/img/camera.png" class="tobuild fadeInUp delay-800" onclick="myfunction(this)">
:::

<slide class="fullscreen zoomIn">
## 从四个小的实践开始{.text-landing.content-center}
<br>
<br>
:::flexblock 
:::div {.tobuild.zoomIn}
:fa-plug: {.myfa}
## 智能插座
---
:::div {.tobuild.zoomIn}
:fa-lightbulb-o:{.myfa}
## 网络继电器开灯
---
:::div {.tobuild.zoomIn}
:fa-video-camera:{.myfa}
## 视频制作
---
:::div {.tobuild.zoomIn}
:fa-play:{.myfa}
## videowall
---
:::

<slide class="grid vertical-align fullscreen slideInLeft">
:::column 
## 智能插座
 * <span style="font-size:2rem; color:olive"> **BEFORE** </span> \: 手动盒子测试断电，每次最多测几十次 {.fadeInUp}
 * <span style="font-size:2rem; color:lawngreen"> **AFTER** </span> \: 通过自动化之后，可以反复断电1晚 {.fadeInUp}
 * [:fa-file-pdf-o: 插座文档](/plug.pdf) {.fadeInUp}
{.description.build}

!![](/img/plug.png .aligncenter.fadeInUp.delay-400.size-80.tobuild)

---
:::div {.fadeInUp.tobuild.content-center}
<video height="600" width="340" controls autoplay loop onclick="myfunction(this)">
    <source src="/img/plug.mp4" type="video/mp4">
</video>
:::
:::
<slide class="grid vertical-align fullscreen slideInRight">
:::column
## 网络继电器开灯 
 * <span style="font-size:2rem; color:olive"> **BEFORE** </span> \: 只能通过听继电器的滴答声来确定触发 {.fadeInUp}
 * <span style="font-size:2rem; color:lawngreen"> **AFTER** </span> \: 现在观察灯的闪烁就可以了解触发情况 {.fadeInUp}
{.description.build}
---
:::div {.fadeInUp.tobuild}
<video height="600" width="340" controls autoplay loop onclick="myfunction(this)">
    <source src="/img/light.mp4" type="video/mp4">
</video>
:::
:::
<slide class="content-center fullscreen slideInLeft">
## 视频制作
<br/>
:::div {.fadeInUp}
<br> 
<video width="700" controls autoplay loop onclick="myfunction(this)">
    <source src="/img/tmp720p.mp4" type="video/mp4">
</video>
:::

<slide class="content-center fullscreen slideInRight">
## videowall
<br/>
:::div {.fadeInUp}
<br/>
<video width="700" controls autoplay loop onclick="myfunction(this)">
    <source src="/img/videowall.mov" type="video/mp4">
</video>
:::

<slide class="fullscreen slideInLeft">
## 我们测试的目标{.text-landing .aligncenter} 
<br>
:::flexblock {.metrics}

:::div {.tobuild.animated.zoomIn.delay-400}

:fa-clock-o:

有限时间

----
:::div {.tobuild.animated.zoomIn.delay-800}
:fa-users:

有限人力

----
:::div {.tobuild.animated.zoomIn.delay-1200}
:fa-tasks:

保证覆盖

:::
<br>
## 保证产品质量，做到心里有数 {.tobuild .text-landing .content-center .zoomIn.delay-2000}

<slide class="fullscreen slideInRight">
### 我们测试的覆盖 {.aligncenter.text-landing.zoomIn}
<img src="/img/cover.png" class="aligncenter fadeInUp delay-800" onclick="myfunction(this)">
</script>

<slide :class="fullscreen slideInLeft">
## 我们测试的输出 {.aligncenter.text-landing.zoomIn}
<br>
<br>
:::gallery-overlay {.build}
<img src="/img/acc.png" onclick="myfunction(this)">
## 准确率测试

---
<br>
<br>
<br>
<br>
<img src="/img/codecoverage.png" onclick="myfunction(this)">
## 代码覆盖率 [结果](http://10.151.3.74:3500/gcov/CoverageTest4/resultInfo.html)

---
<img src="/img/delay.png" style="background: white" onclick="myfunction(this)">
## 延时测试 

:::

<slide class="fullscreen slideInRight">
### 我们的做法 {.aligncenter.text-landing.fadeInUp}
:::column
#### 自动化{.content-left.tobuild}
 * :覆盖\::{.text-label}
{.description.build}
   * 通过API覆盖超过<span style="font-size:3rem; color:lawngreen" class="fadeInUp"> **80%** </span> 以上的测试 
   * 功能，兼容性，准确率，稳定性，覆盖率 .etc
 * :优点\::{.text-label.build}
   * 有效的测试的覆盖, 回归
   * 测试的稳定性
   * 完成一些手动不可能完成的事情
 * :缺点\::{.text-label.build}
   * 需要开发的时间
----
 * :需要做到\::{.text-label}
{.description.tobuild}
   * 稳定性
   * 可维护性
   * 易用性
   * 可扩展性

<slide class="fullscreen slideInLeft">
### 我们的做法 {.aligncenter.text-landing.fadeInUp}
:::column
#### 手动{.content-left.tobuild}
  * 延时
  * 网络 [:fa-file-pdf-o:](/net.pdf)
  * Web(做了部分的自动化)
  * 对接
{.description.tobuild}

---
#### 其他{.content-left.tobuild}
  * 主动的推动流程的规范化，需求，开发自测，打包，提测，release流程
  * 在项目相对空挡，或者pending的时候，提前做一下技术上的准备，比如完成框架的优化。
{.description.tobuild}
:::
<slide class="fullscreen zoomIn">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
<img src="/img/py_start.png" class="aligncenter fadeInUp delay-400 size-60" onclick="myfunction(this)">

<slide class="fullscreen zoomIn">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
<img src="/img/perl_start.png" class="aligncenter fadeInUp delay-400 size-80" onclick="myfunction(this)">

<slide class="fullscreen zoomIn">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
<img src="/img/run_help.png" class="aligncenter fadeInUp delay-400" onclick="myfunction(this)">

<slide class="fullscreen slideInLeft">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
:::gallery {.build}
<img src="/img/log1.png" class="aligncenter fadeInUp delay-400" onclick="myfunction(this)">

----
<img src="/img/136.png" class="aligncenter fadeInUp delay-400 bg-white size-60" onclick="myfunction(this)">
:::

<slide class="fullscreen slideInRight">
:::column {.zoomIn}
<br>
#### 我们是如何自动化开发的
<br>
 * 高效协作
 * 共识：风格一致
 * 解耦：框架,用例
{.build.zoomIn}
---
<img src="/img/script.png" width=300 style="margin-left: 100px" onclick="myfunction(this)">
:::

<slide class="fullscreen">
### 我们是如何自动化开发的 {.aligncenter.text-landing.zoomIn}
:::span {.aligncenter.text-subtitle.zoomIn}
[![](/img/gitlab-icon-rgb.png){.avatar-40}](http://gitlab.sz.sensetime.com/yangxinming/nebula-m-1.2)
:::
<img src="/img/testcase.png" class="aligncenter fadeInUp delay-400 size-80" onclick="myfunction(this)">

<slide class="fullscreen zoomIn">
### 我们之前的计划 {.content-center}
<br>
:::column {.sm .aligncenter .fadeInUp .build}
> [:fa-file-pdf-o: Deprecated Plan](/test.pdf) 
<br>
<br>
<img src="/img/plan_arch.png" width=600 onclick="myfunction(this)">

---
<video width="850" controls autoplay loop onclick="myfunction(this)">
    <source src="/img/nebula-m_testserver.mov" type="video/mp4">
</video>
:::

<slide class="slideInLeft" image="https://source.unsplash.com/PGnqT0rXWLs/800x600 .right">
:::column
### 未来合作计划 
<br>
 * Viper-Lite SEP
 * SenseNebula-M Lite 迁移 ： 功能上一致，考虑使用现有框架
 * 现有测试框架SEP 集成
{.build.description}
:::

<slide class="slideInRight fullscreen aligncenter" video="https://webslides.tv/static/videos/working.mp4 poster='https://webslides.tv/static/images/working.jpg' .dark">
# Thanks! {.aligncenter.text-landing.zoomIn} 
[![](/img/gitlab-icon-rgb.png){.avatar-80}](http://gitlab.sz.sensetime.com/yangxinming/testing-slides)

