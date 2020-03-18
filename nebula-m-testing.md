title: 浅谈Nebula-M 测试实践
speaker: yangxinming
transition: slide
prismTheme: funky
css:
    - /css/base.css
plugins:
    - echarts
    - mermaid
    - katex


<slide class="bg-black-blue aligncenter" image="https://source.unsplash.com/C1HhAQrbykQ/ .bg-primary">

# 浅谈Nebula-M 测试实践 {.text-landing.text-shadow}
---
By YangXinMing {.text-intro}

<slide class="size-100" image="https://source.unsplash.com/n9WPPWiPPJw/">
!![](/img/waiguan.png .fadeInUp.delay-400)

<slide class="fullscreen">
:::card {.card-70}

## Nebula-m 是什么？
 * 商汤星云M系列智能边缘节点基于深度学习技术，是软硬件一体的嵌入式产品系列。 {.animated.zoomIn}
 * SenseNebula-M 为摄像机、抓拍机等多种采集设备提供接入能力，支持人脸识别、人体分析等多算法融合，具有信号联动控制、数据 汇聚、云边协同等功能，为行业解决方案提供商、集成商、代理商提供适配多种场景的智能化产品和解决方案。{.animated.zoomIn.delay-400} 
---
![](/img/nebula-m.png)

:::

<slide class="fullscreen">
### 说人话 = 提供算力,人脸,人体等分析功能 {.aligncenter.text-landing.zoomIn}
!![](/img/deploy.png .aligncenter.fadeInUp.delay-400) 


<slide class="fullscreen">
### 产品功能 {.aligncenter.text-landing.zoomIn} 
---
:::column {.fadeInUp}
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

<slide class="grid vertical-align">
:::column
# 我们是如何测试的{.zoomIn} 
---
!![](/img/camera.png .fadeInUp.delay-800)
:::

<slide class="slide-top">
# 从四个小实践开始{.text-landing}

:::flexblock 
:::div {.animated.zoomIn}
::fa-plug::
## 智能插座
---
:::div {.animated.zoomIn.delay-400}
::fa-lightbulb-o::
## 网络继电器开灯
---
:::div {.animated.zoomIn.delay-800}
::fa-video-camera::
## 视频制作
---
:::div {.animated.zoomIn.delay-1200}
::fa-play::
## videowall
---
:::

<slide class="grid vertical-align">
:::column
# 智能插座
 * [:fa-file-pdf-o: 插座文档](/plug.pdf) 
---
<video height="600" width="340" controls autoplay loop>
    <source src="/img/plug.mp4" type="video/mp4">
</video>
:::
<slide class="grid vertical-align">
:::column
# 网络继电器开灯 
---
<video height="600" width="340" controls autoplay loop>
    <source src="/img/light.mp4" type="video/mp4">
</video>
:::
<slide class="">
# 视频制作
<br/><br/>
<video width="800" controls autoplay>
    <source src="/img/tmp720p.mp4" type="video/mp4">
</video>
<slide class="">
# videowall
<br/><br/>
<video width="800" controls autoplay>
    <source src="/img/videowall.mov" type="video/mp4">
</video>


<slide>
# 我们测试的目标 {.content-left}
  * 保证产品质量，做到心里有底
    * 有限时间
    * 有限人力
    * 保证覆盖

<slide>
# 我们测试的覆盖
![](/img/cover.png)

<slide :class="">
# 我们测试的覆盖 {.content-center}
:::gallery-overlay
![](/img/acc.png)
## 准确率测试

---
![](/img/codecoverage.png)
## 代码覆盖率测试

---
![](/img/delay.png)
## 延时测试

:::

<slide class="">
# 我们是如何测试的 {.content-left}
:::column
* 自动化 -> API -> 功能，兼容性，准确率，稳定性，覆盖率
    * 好处
        * 测试的覆盖
        * 测试的稳定性
        * 一些手动不可能完成的事情
    * 坏处
        * 需要开发的时间
    * 需要做到
        * 稳定性
        * 可维护性
        * 易用性
        * 可扩展性
---
* 手动
    * 延时，网络，Web(做了部分的自动化)
* 其他
    * 主动的推动流程的规范化，需求，开发自测，打包，提测，release流程
    * 在项目不是空挡，或者pending的时候，提前做一下技术上的准备，比如完成框架的优化。
---
:::

<slide class="slide-top">
# 我们是如何自动化的
![](/img/run_help.png)

<slide class="slide-top">
# 关于执行测试

<slide class="slide-top">
# 关于脚本开发
![](/img/script.png)

<slide :class="size-80">
:::card

## 第一部分
.card-50.bg-white

 [Unsplash](http://Unsplash.com) is a really cool resource. It is a collection of Creative Commons Zero licensed photos that are really great. {.text-intro}

 * :Role\::{.text-label} Frontend
 * :client\::{.text-label} Acme
 * :year\::{.text-label} 2018
 {.description}

---
![](https://source.unsplash.com/rCOWMC8qf8A/)

:::
<slide class="bg-black-blue aligncenter" video="https://webslides.tv/static/videos/working.mp4 poster='https://webslides.tv/static/images/working.jpg' .dark">
# Thanks
