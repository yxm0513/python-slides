title: 浅谈Nebula-M 测试实践
speaker: yangxinming
transition: cards
prismTheme: dark
css:
    - /css/base.css
js:
    - /js/base.js
plugins:
    - echarts
    - mermaid
    - katex


<slide class="bg-black-blue aligncenter" image="https://source.unsplash.com/C1HhAQrbykQ/ .bg-primary">

# 浅谈Nebula-M 测试实践 {.text-landing.text-shadow}
---
By YangXinMing {.text-intro}  

:::footer {.text-subtitle.alignright.green} 
Powered by nodeppt 
:::

<slide class="grid vertical-align fullscreen" image="https://source.unsplash.com/n9WPPWiPPJw/">
:::column {.white}
!![](/img/waiguan.png .fadeInUp.delay-400)

---
:::div {.fadeInUp.build}

标准版\: v1.0.0 v1.2.0 v2.0.0 

MQTT版\: 

社区办，测温版，蓝光版 \.etc 
:::
:::

<slide>

:::card

#### 测温版

 * 测温告警
 * 佩戴口罩对比
 * 未佩戴口罩告警
{.build.description}
---
![](/img/thermo.png)

<slide class="fullscreen">
:::card {.card-70}

## Nebula-M 是什么？
 * 商汤星云M系列智能边缘节点基于深度学习技术，是软硬件一体的嵌入式产品系列。 {.animated.zoomIn}
 * SenseNebula-M 为摄像机、抓拍机等多种采集设备提供接入能力，支持人脸识别、人体分析等多算法融合，具有信号联动控制、数据 汇聚、云边协同等功能，为行业解决方案提供商、集成商、代理商提供适配多种场景的智能化产品和解决方案。{.animated.zoomIn.delay-400} 
---
![](/img/nebula-m.png)

:::

<slide class="bg-white fullscreen">
### 说人话 = 提供算力,人脸,人体等分析功能 {.aligncenter.text-landing.zoomIn}
!![](/img/deploy.png .aligncenter.fadeInUp.delay-400) 


<slide class="fullscreen">
### 产品功能 {.aligncenter.text-landing.zoomIn} 
---
:::column  {.build.zoomIn}
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
 * 15 x 摄像头
 * 2 x 继电器
 * 1 x 台式机 + 1 x 显示器
 * 1 x 服务器
 * Nebula-M 若干
 * 路由器，交换机，智能插座若干
{.description.text-intro.build}
---
!![](/img/camera.png .fadeInUp.delay-800.tobuild)
:::

<slide class="fullscreen">
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

<slide class="grid vertical-align fullscreen">
:::column 
## 智能插座
 * [:fa-file-pdf-o: 插座文档](/plug.pdf) 
 * 之前手动盒子测试断电，每次最多测几十次
 * 通过自动化之后，可以反复断电1晚
{.description.build}

---
:::div {.fadeInUp.tobuild}
<video height="600" width="340" controls autoplay loop>
    <source src="/img/plug.mp4" type="video/mp4">
</video>
:::
:::
<slide class="grid vertical-align fullscreen">
:::column
## 网络继电器开灯 
 * 之前只能通过听继电器的滴答声来确定触发
 * 现在观察灯的闪烁就可以了解触发情况
{.description.build}
---
:::div {.fadeInUp.tobuild}
<video height="600" width="340" controls autoplay loop>
    <source src="/img/light.mp4" type="video/mp4">
</video>
:::
:::
<slide class="content-center fullscreen">
## 视频制作
<br/>
:::div {.fadeInUp.tobuild}
<br> 
<video width="700" controls autoplay loop>
    <source src="/img/tmp720p.mp4" type="video/mp4">
</video>
:::

<slide class="content-center fullscreen">
## videowall
<br/>
:::div {.fadeInUp.tobuild}
<br/>
<video width="700" controls autoplay loop>
    <source src="/img/videowall.mov" type="video/mp4">
</video>
:::

<slide class="fullscreen">
## 我们测试的目标{.text-landing .aligncenter} 
<br>
:::flexblock {.metrics}

:::div {.animated.zoomIn}

:fa-clock-o:

有限时间

----
:::div {.animated.zoomIn.delay-400}
:fa-users:

有限人力

----
:::div {.animated.zoomIn.delay-800}
:fa-tasks:

保证覆盖

:::
<br>
## 保证产品质量，做到心里有数 {.tobuild .text-landing .content-center .zoomIn.delay-2000}

<slide class="fullscreen">
### 我们测试的覆盖 {.aligncenter.text-landing.zoomIn}
!![](/img/cover.png .aligncenter.fadeInUp.delay-400)
</script>

<slide :class="fullscreen">
## 我们测试的输出 {.aligncenter.text-landing.zoomIn}
<br>
<br>
:::gallery-overlay {.build}
![](/img/acc.png)
## 准确率测试

---
<br>
<br>
<br>
<br>
![](/img/codecoverage.png)
## 代码覆盖率 [结果](http://10.151.3.74:3500/gcov/CoverageTest4/resultInfo.html)

---
![](/img/delay.png)
## 延时测试

:::

<slide class="fullscreen">
:::div{.fadeInUp.content-center.zoomIn}
### 我们的做法 {.aligncenter.text-landing}
:::column {.build}
#### 自动化{.content-left}
 * :覆盖\::{.text-label} --> 通过API覆盖超过80%以上的测试 
   * 功能，兼容性，准确率，稳定性，覆盖率
 * :优点\::{.text-label}
   * 有效的测试的覆盖, 回归
   * 测试的稳定性
   * 完成一些手动不可能完成的事情
 * :缺点\::{.text-label}
   * 需要开发的时间
 * :需要做到\::{.text-label}
   * 稳定性
   * 可维护性
   * 易用性
   * 可扩展性
---
#### 手动{.content-left}
  * 延时
  * 网络 [:fa-file-pdf-o:](/net.pdf)
  * Web(做了部分的自动化)
  * 对接

#### 其他{.content-left}
  * 主动的推动流程的规范化，需求，开发自测，打包，提测，release流程
  * 在项目相对空挡，或者pending的时候，提前做一下技术上的准备，比如完成框架的优化。
:::
:::
<slide class="fullscreen">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
!![](/img/py_start.png .aligncenter.fadeInUp.delay-400.size-60)

<slide class="fullscreen">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
!![](/img/perl_start.png .aligncenter.fadeInUp.delay-400.size-80)

<slide class="fullscreen">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
!![](/img/run_help.png .aligncenter.fadeInUp.delay-400)

<slide class="fullscreen">
### 我们是如何自动化的 {.aligncenter.text-landing.zoomIn}
:::gallery {.build}
!![](/img/log1.png .aligncenter.fadeInUp)

----

!![](/img/136.png .aligncenter.fadeInUp)
:::

<slide class="fullscreen" image="/img/script.png .right.right-10.fadeInUp.delay-400.size-60">
### 我们是如何自动化开发的 {.content-left.zoomIn}

<slide class="fullscreen">
### 我们是如何自动化开发的 {.aligncenter.text-landing.zoomIn}
:::span {.aligncenter.text-subtitle.zoomIn}
[Source Code](http://gitlab.sz.sensetime.com/yangxinming/nebula-m-1.2)
:::
!![](/img/testcase.png .aligncenter.fadeInUp.delay-400.size-80)

<slide class="fullscreen">
### 我们之前的计划 {.content-center}
<br>
:::column {.sm .aligncenter .fadeInUp .build}
> [:fa-file-pdf-o: Deprecated Plan](/test.pdf) 
<br>
<br>
!![](/img/plan_arch.png .alignright)
---
<video width="900" controls autoplay loop>
    <source src="/img/nebula-m_testserver.mov" type="video/mp4">
</video>
:::

<slide class="" image="https://source.unsplash.com/PGnqT0rXWLs/800x600 .right">
:::div 
### 未来合作计划 
<br>
{.text-intro}

 * Viper-Lite SEP
 * SenseNebula-M Lite 迁移 ： 功能上一致，考虑使用现有框架
 * 现有测试框架SEP 集成
{.build.description}
:::

<slide class="fullscreen bg-black-blue aligncenter" video="https://webslides.tv/static/videos/working.mp4 poster='https://webslides.tv/static/images/working.jpg' .dark">
# Thanks!{.aligncenter.text-landing.zoomIn}

