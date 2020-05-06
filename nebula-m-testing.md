title: 浅谈SenseNebula-M 测试实践
speaker: yangxinming
transition: cards
prismTheme: dark
css:
    - css/base.css
js:
    - js/zoom.js
    - js/base.js
    - https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css 
plugins:
    - echarts
    - mermaid
    - katex


<slide class="bg-black-blue aligncenter zoomIn" image="https://source.unsplash.com/C1HhAQrbykQ/">
# 浅谈SenseNebula-M 测试实践 {.text-shadow}

By ![](https://avatars3.githubusercontent.com/u/73510?s=60&u=200063d372fefbd51de767b8e258de0024d45e52&v=4){.avatar-40} YangXinMing \[SCG-NP-IDEA\] {.text-intro} 

---
:::div
<img src="/img/nodeppt_md.png" width="200" class="bounceInLeft slow" onclick="myfunction(this)"> 
:::
Powered by nodeppt 2.0 {.text-subtitle.bounceInLeft.slow}

<slide class="grid vertical-align fullscreen" image="https://source.unsplash.com/n9WPPWiPPJw/">
:::column {.white}
!![](/img/waiguan.png .fadeInUp.delay-400)

---

## Agenda {.zoomIn}
<br>
:::div {.mydiv}
 * 关于SenseNebula-M {.bounceInRight}
 * 我们是如何完成测试的？{.bounceInRight}
 * 之前的设想，以及未来的计划{.bounceInRight}
 * Q&A {.bounceInRight}
{.build.description.text-intro}
:::

<slide class="grid vertical-align fullscreen slideInLeft">
<span class="fa-stack fa-2x" style="color: LIGHTSALMON; position:fixed; top:0; left:0;z-index:100">
    <i class="fa fa-bookmark fa-stack-2x"></i>
    <strong class="fa-stack-1x" style="color: white;">1</strong>
</span>
:::card {.card-70 .bg-blue .fadeInUp}

### SenseNebula-M 是什么？
 * 商汤星云M系列智能边缘节点基于深度学习技术，是软硬件一体的嵌入式产品系列。 {.animated.zoomIn}
 * SenseNebula-M 为摄像机、抓拍机等多种采集设备提供接入能力，支持人脸识别、人体分析等多算法融合，具有信号联动控制、数据 汇聚、云边协同等功能，为行业解决方案提供商、集成商、代理商提供适配多种场景的智能化产品和解决方案。{.animated.zoomIn.delay-400} 
---

![](/img/nebula-m.png)

:::

<slide class="fullscreen slideInRight">
### 说人话 = 提供算力,人脸,人体等分析功能 {.aligncenter.text-landing.zoomIn}
<img src="/img/deploy.png" class="aligncenter fadeInUp delay-400" onclick="myfunction(this)">

<slide class="fullscreen">
### 产品主要功能 {.aligncenter.text-landing.zoomIn} 
---
:::column {.build.mycolmn}
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

<slide class="grid aligncenter fullscreen">
#### Releases
<br>

*From 2019.05.30 To 2020.03.26 ,More Than 16 Releases* {.bounceInLeft.tobuild}
:::div {.mydiv}
 * 硬件 {.bounceInLeft.tobuild}
   * 一代TX2平台, 二代3559A平台 {.bounceInLeft.tobuild}
   * 研扬，宝德，天地 {.bounceInLeft.tobuild}
 * 软件  {.bounceInLeft.tobuild}
   * 标准版\: v1.0.0 v1.2.0 v1.3.0 v2.0.0 v2.0.x {.bounceInLeft.tobuild}
   * MQTT版\: v1.0.0 v1.2.0 v2.0.0 {.bounceInLeft.tobuild}
   * 国际版，社区版，测温版，蓝光版 \.etc {.bounceInLeft.tobuild}
:::

<slide class="grid aligncenter fullscreen">
<div class="">
<h4> Timeline </h4>
<ul class="timeline build">
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
			<div class="desc">1. 定制版-对接SF&SU
2. 定制版-mqtt对接深广用户
3. 标准版，临时给出支持案场项目
4. 定制版-mqtt对接深广用户
5. 定制版-mqtt对接深广用户
</div>
		</div>
	</li>
	<li>
		<div class="direction-r">
			<div class="flag-wrapper">
				<span class="flag">标准版 V1.1.2</span>
				<span class="time-wrapper"><span class="time">2019.09.02</span></span>
			</div>
			<div class="desc">
1.【新功能】抓拍策略与通道绑定
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
                <span class="flag">MQTT/Telecom V1.2</span>
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
            <div class="desc">1. 新硬件适配，接入协议
2. 抓拍机接入
3. 支持GB28181
4. 鉴权
5. 视频图片流混合接入
6. 人体特征
7. 人脸信息
8. 网络继电器状态
</div>
        </div>
    </li>
    <li>
        <div class="direction-r">
            <div class="flag-wrapper">
                <span class="flag">测温版 V1.0</span>
                <span class="time-wrapper"><span class="time">2020.02.13</span></span>
            </div>
            <div class="desc">1. 智能测温检测告警,预警，复核, 未佩戴口罩检测告警, 2. 热成像相机视频流接入预览, 3. 支持SDK接入, 4. 支持未佩戴口罩告警弹窗
</div>
        </div>
    </li>
    <li>
        <div class="direction-l">
            <div class="flag-wrapper">
                <span class="flag">测温版 V1.1</span>
                <span class="time-wrapper"><span class="time">2020.02.19</span></span>
            </div>
            <div class="desc">1. 新增支持戴口罩人脸识别 2. 优化最大支持4路热成像相机接入处理, 记录存储, 查询,分类,检索,统计 3. API接口开放
</div>
        </div>
    </li>
</ul>
</div>
:::
<slide class="grid vertical-align fullscreen slideInRight">
:::column 
<video height="500" controls autoplay loop muted onclick="myfunction(this)">
    <source src="/img/cctv.mp4" type="video/mp4">
</video>

---
:::div {.alignright}
#### 测温版{.bounceInLeft.align-center}
<img src="/img/awards.png" class="fadeInUp tobuild" width=300px onclick="myfunction(this)">
 * 测温相机接入 {.tobuild.bounceInLeft}
 * 测温告警 {.tobuild.bounceInLeft}
 * 佩戴口罩对比 {.tobuild.bounceInLeft}
 * 未佩戴口罩告警 {.tobuild.bounceInLeft}
{.description}
:::

<slide class="grid vertical-align fullscreen">
## DEMO {.text-landing.aligncenter}


<slide class="grid vertical-align fullscreen">
<span class="fa-stack fa-2x" style="color: LIGHTSALMON; position:fixed; top:0; left:0;z-index:100">
    <i class="fa fa-bookmark fa-stack-2x"></i>
    <strong class="fa-stack-1x" style="color: white;">2</strong>
</span>
### 我们是如何完成测试的? {.aligncenter}
:::column {.mycolumn}
#### 嵌入式设备测试的难点 {.zoomIn}
<br>
 * 需特别注重产品稳定性,健壮性,易用性 {.fadeInUp}
 * 需适配场景众多,另需兼容各类设备 {.fadeInUp}
 * 硬件本身资源有限,功能修改容易引入性能问题 {.fadeInUp}
 * 版本较多,回归压力大 {.fadeInUp}
{.description.text-intro.build}
---
<img src="/img/testing.png" class="fadeInUp" width=600px height=420px>
:::

<slide class="grid vertical-align fullscreen">
:::column {.mycolumn}
#### 我们的测试设备{.zoomIn} 
 * 15+ x 摄像头 {.fadeInUp} 
 * 2+ x 继电器 {.fadeInUp}
 * 1 x 台式机 + 1 x 显示器{.fadeInUp}
 * 1 x 服务器{.fadeInUp}
 * SenseNebula-M 若干{.fadeInUp}
 * 路由器，交换机，智能插座若干{.fadeInUp}
{.description.text-intro.build}
---
<img src="/img/camera.png" width=550px class="tobuild fadeInUp delay-800" onclick="myfunction(this)">
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
## 网络继电器开🚪 -> :fa-lightbulb-o:
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
:::column {.mycolumn}
## 智能插座
 * <span style="font-size:2rem; color:olive"> **BEFORE** </span> \: 手动盒子测试断电，每次最多测几十次 {.fadeInUp}
 * <span style="font-size:2rem; color:lawngreen"> **AFTER** </span> \: 通过自动化之后，可以反复断电1晚 {.fadeInUp}
 * [:fa-file-pdf-o: 插座文档](/plug.pdf) {.fadeInUp}
{.description.build}

<img src="/img/plug.png" class="aligncenter fadeInUp delay-400 size-80 tobuild" onclick="myfunction(this)">

---
:::div {.fadeInUp.tobuild.content-center}
<video height="600" width="340" controls autoplay loop muted onclick="myfunction(this)">
    <source src="/img/plug.mp4" type="video/mp4">
</video>
:::
:::
<slide class="grid vertical-align fullscreen slideInRight">
:::column {.mycolumn}
## 网络继电器开🚪  --> :fa-lightbulb-o: 
 * <span style="font-size:2rem; color:olive"> **BEFORE** </span> \: 只能通过听继电器的滴答声来确定触发 {.fadeInUp}
 * <span style="font-size:2rem; color:lawngreen"> **AFTER** </span> \: 现在观察灯的闪烁就可以了解触发情况 {.fadeInUp}
{.description.build}
---
:::div {.fadeInUp.tobuild}
<video height="600" width="340" controls autoplay loop muted onclick="myfunction(this)">
    <source src="/img/light.mp4" type="video/mp4">
</video>
:::
:::
<slide class="content-center fullscreen slideInLeft">
## 视频制作
<br/>
:::div {.fadeInUp}
<br> 
<video width="700" controls autoplay loop muted onclick="myfunction(this)">
    <source src="/img/tmp720p.mp4" type="video/mp4">
</video>
:::

<slide class="content-center fullscreen slideInRight">
## videowall
<br/>
:::div {.fadeInUp}
<br/>
<video width="700" controls autoplay loop muted onclick="myfunction(this)">
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

<slide class="fullscreen slideInRight">
### 我们的做法 Philosophy {.aligncenter.text-landing.fadeInUp}

Test Automation as a Key Enabler for High-performing Teams {.aligncenter.text-intro.fadeInUp}

:::column {.mycolumn}
#### 主要依靠自动化{.content-left.tobuild}
 * 覆盖\:
{.build}
   * 通过API覆盖超过<span style="font-size:3rem; color:lawngreen" class="fadeInUp"> **80%** </span> 以上的测试 
   * 功能，兼容性，准确率，稳定性，覆盖率 .etc
 * 优点\:
   * 有效的测试的覆盖, 回归
   * 测试的稳定性
   * 完成一些手动不可能完成的事情
 * 缺点\:
   * 需要开发的时间
----
 * 自动化开发需要做到\:
{.build}
   * 稳定性
   * 可维护性
   * 易用性
   * 可扩展性

<slide class="fullscreen slideInLeft">
### 我们的做法 Philosophy {.aligncenter.text-landing.fadeInUp}
:::column {.mycolumn}
#### 结合部分手动{.content-left.tobuild}
  * 延时
  * 网络 [:fa-file-pdf-o:](/net.pdf)
  * Web(做了部分的自动化)
  * 对接
{.description.tobuild}

<video width=300 controls autoplay loop muted class="tobuild" onclick="myfunction(this)">
    <source src="/img/delay.mov" type="video/mp4">
</video>

---
#### 另外{.content-left.tobuild}
  * 主动的推动流程的规范化，需求，开发自测，打包，提测，release流程
  * 在项目相对空挡，或者pending的时候，提前做一下技术上的准备，比如完成框架的优化。
{.description.tobuild}
:::
<slide class="fullscreen zoomIn">
### 我们是如何执行自动化 {.aligncenter.text-landing.zoomIn}

<img src="/img/py_start.png" class="aligncenter fadeInUp delay-400 size-60" onclick="myfunction(this)">

<slide class="fullscreen zoomIn">
### 我们是如何执行自动化 {.aligncenter.text-landing.zoomIn}
<img src="/img/perl_start.png" class="aligncenter fadeInUp delay-400 size-80" onclick="myfunction(this)">

<slide class="fullscreen zoomIn">
### 我们是如何执行自动化 {.aligncenter.text-landing.zoomIn}
:::column {.mycolumn}
<img src="/img/run_help.png" class="fadeInUp delay-400" onclick="myfunction(this)">

---

#### Why those options?{.zoomIn.tobuild}
 * ip \: 指向测试的盒子 {.fadeInUp}
 * list \: 哪些case可以执行? {.fadeInUp}
 * select,exclude \: 选择需要的用例{.fadeInUp}
 * tag \: 选择相关的测试用例 {.fadeInUp}
 * repeat,cycle \: 多次运行 {.fadeInUp}
 * random \: 随机执行顺序{.fadeInUp}
 * failed \: 执行上一次出错的用例{.fadeInUp}
 * ignore \: 去除重复的err message 到err.log里{.fadeInUp}
 * common options \: 一些框架执行的配置{.fadeInUp}
{.description.text-intro.build}
:::

<slide class="fullscreen slideInLeft">
### 自动化运行的输出 {.aligncenter.text-landing.zoomIn}
:::column {.build}
<img src="/img/log1.png" class="aligncenter fadeInUp delay-400" onclick="myfunction(this)">

----
##### running logs {.fadeInUp.tobuild}
  * summary \: stdout xxx.log {.fadeInUp}
  * details \: run_xxx.log run_xxx_err.log {.fadeInUp}
  * core \: core files \: core_files_backup, trace \: xxx_core.log {.fadeInUp}
  * faied case \: xxx.err
{.description.build}
##### mock receiving {.fadeInUp.tobuild}
  * http/https  \: posted info {.fadeInUp}
  * ws \: web socket emit{.fadeInUp}
  * tmp_image \: received images{.fadeInUp}
{.description.build}

----
<img src="/img/136.png" class="aligncenter fadeInUp delay-400 bg-white size-60" onclick="myfunction(this)">
:::

<slide class="fullscreen slideInRight">
:::column {.mycolumn.zoomIn}
<br>
#### 我们是如何自动化开发的
* 效率为先{.fadeInUp.text-intro.tobuild}
   * 共识：风格一致(Convention Over Configuration){.fadeInUp}
   * 解耦：框架,用例(DRY, test script reflects test design){.fadeInUp}
   * 反馈：多提交，多执行(Agile, feedback timely){.fadeInUp}
{.build.text-intro}
* 最终实现{.fadeInUp.text-intro.tobuild}
   * built on requests, unittest, paramiko .etc
   * file based tests
   * lightweight, easy to manage, setup and maintain, adaptable, scalable, flexable
   * support all kinds of tests, api, web, tools, performance, accuracy .etc
{.build.text-intro}

---

<img src="/img/script.png" width=350 style="margin-left: 100px" onclick="myfunction(this)">

:::

<slide class="fullscreen">
### 如何写一个用例 {.aligncenter.text-landing.zoomIn}
:::span {.aligncenter.text-subtitle.zoomIn}
[![](/img/gitlab-icon-rgb.png){.avatar-40}](http://gitlab.sz.sensetime.com/yangxinming/nebula-m-1.2)
:::
<img src="/img/testcase.png" class="aligncenter fadeInUp delay-400 size-80" onclick="myfunction(this)">

<slide :class="fullscreen slideInLeft">
## 我们测试的输出 {.aligncenter.text-landing.zoomIn}
<br>
<br>
:::gallery-overlay {.build}
<br>
<img src="/img/report.png" onclick="myfunction(this)">
## 测试报告
---
<img src="/img/acc.png" onclick="myfunction(this)">
## 准确率测试

---
<br>
<br>
<br>
<img src="/img/codecoverage.png" onclick="myfunction(this)">
## 代码覆盖率 [结果](http://10.151.3.74:3500/gcov/CoverageTest4/resultInfo.html)

---
<br>
<br>
<img src="/img/delay.png" style="background: white" onclick="myfunction(this)">
## 延时测试

:::


<slide class="fullscreen zoomIn">
<span class="fa-stack fa-2x" style="z-index:100;color: LIGHTSALMON; position:fixed; top:0; left:0;">
    <i class="fa fa-bookmark fa-stack-2x"></i>
    <strong class="fa-stack-1x" style="color: white;">3</strong>
</span>

### 我们之前的计划 {.content-center}
<br>
:::column {.sm .aligncenter .fadeInUp .build}
<div class="aligncenter">
> [:fa-file-pdf-o: Deprecated Plan](/test.pdf) 
<br>
<img src="/img/plan_arch.png" width=600 onclick="myfunction(this)">
</div>

---
<div class="aligncenter">
<video width=900 controls autoplay loop muted onclick="myfunction(this)">
    <source src="/img/nebula-m_testserver.mov" type="video/mp4">
</video>
</div>
:::

<slide class="slideInLeft" image="https://source.unsplash.com/PGnqT0rXWLs/800x600 .right">
:::column
### 未来合作计划 
<br>
 * Viper-Lite 平台测试 SEP {.tobuild.text-intro.fadeInUp}
 * SenseNebula-M Lite迁移 ：{.tobuild.text-intro.fadeInUp}
   * 旧API功能上不变，考虑使用现有框架{.tobuild.text-intro.fadeInUp}
   * 新API,新功能使用SEP{.tobuild.text-intro.fadeInUp}
 * 现有测试框架SEP 集成 {.tobuild.text-intro.fadeInUp}
---
:::


<slide class="slideInRight fullscreen aligncenter" video="https://webslides.tv/static/videos/working.mp4 poster='https://webslides.tv/static/images/working.jpg' .dark">
<span class="fa-stack fa-2x" style="z-index:100;color: LIGHTSALMON; position:fixed; top:0; left:0;">
    <i class="fa fa-bookmark fa-stack-2x"></i>
    <strong class="fa-stack-1x" style="color: white;">4</strong>
</span>
# Thanks! {.aligncenter.text-landing} 
### <span style="font-size:3rem; color:lawngreen">Any questions? </span> {.aligncenter.fadeInUp.delay-400}

<img src="/img/wechat_qrcode.png" width=130>

