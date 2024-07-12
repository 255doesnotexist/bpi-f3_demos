# BananaPI BPI-F3 运行官方示例图像分类、目标检测 DEMO

## 开发板说明

### 开发板简介

开发板介绍文档 (BananaPI Wiki)；https://wiki.banana-pi.org/Banana_Pi_BPI-F3#Application_direction

开发板介绍文档 (BananaPI Docs)；https://docs.banana-pi.org/en/BPI-F3/BananaPi_BPI-F3

开发板应用方向：
- NAS
- 笔记本电脑
- 智能机器人
- 工业控制
- 人工智能边缘计算

### DEMO 简介

* DEMO 说明
  classification_demo：单张图片图像分类 demo，输入单张图片路径，输出图像的类别。
* DEMO 源码链接
  位于完整 SDK 解压后 bianbu-ai-support-demo 目录下。
* SDK 及链接
  https://archive.spacemit.com/spacemit-ai/spacemit-ai-sdk/spacemit-ai-sdk.v1.1.0.x86_64.tar.gz
* DEMO 运行所需的 SDK：spacemit-ai-sdk.v1.1.0

### DEMO 运行

执行环境：
- 开发板：BananaPI BPI-F3 (4G RAM 版本)
- 操作系统：Bianbu 1.0

通过 screen /dev/ttyUSB0 115200 串口连接上开发板。

输入默认用户名密码 root、bianbu 登入板子。

首先通过 wget 在板上拉取并解压 SDK（虽然有 x86 后缀，但 demo/bin 是 rv64 架构的，可以直接运行 DEMO）。

```sh
root@k1:~# wget https://archive.spacemit.com/spacemit-ai/spacemit-ai-sdk/spacemit-ai-sdk.v1.1.0.x86_64.tar.gz --no-check-certificate
root@k1:~# tar xzf spacemit-ai-sdk.v1.1.0.tar.gz
```

就地解压完成后，你的 home 目录下应当多出一个 spacemit-ai-sdk.v1.1.0 的 SDK 目录。 （注意文件占地空间较大，需提前清理出可用空间。）

执行以下命令进入到目标 ai-support 目录：

```sh
root@k1:~# cd ~/spacemit-ai-sdk.v1.1.0/bianbu-ai-support
```

板上执行图像分类 DEMO（squeezenet 模型板上自带，无需下载。）：

```sh
root@k1:~/spacemit-ai-sdk.v1.1.0/bianbu-ai-support# bin/classification_demo /usr/share/ai-support/models/squeezenet1.1-7.onnx /usr/share/ai-support/models/synset.txt /usr/share/ai-support/imgs/dog.jpg
Enable spacemit ep now
Classify result: n02113023 Pembroke, Pembroke Welsh corgi
```

下载目标检测 DEMO 必要模型：

```sh
wget https://bj.bcebos.com/paddlehub/fastdeploy/nanodet-plus-m_320.onnx -O share/ai-support/models/nanodet-plus-m_320.onnx
--2024-07-13 03:08:20--  https://bj.bcebos.com/paddlehub/fastdeploy/nanodet-plus-m_320.onnxstdeploy/nanodet-plus-m_320.onnx -O share/ai-support/models/nanodet-plus-m_320.onnx
正在解析主机 bj.bcebos.com (bj.bcebos.com)... 2409:8c04:1001:1203:0:ff:b0bb:4f27, 103.211.222.98
正在连接 bj.bcebos.com (bj.bcebos.com)|2409:8c04:1001:1203:0:ff:b0bb:4f27|:443... 已连接。
已发出 HTTP 请求，正在等待回应... 200 OK
长度：4786922 (4.6M) [application/octet-stream]
正在保存至: “share/ai-support/models/nanodet-plus-m_320.onnx”

share/ai-support/mo 100%[===================>]   4.56M  2.39MB/s  用时 1.9s    

2024-07-13 03:08:22 (2.39 MB/s) - 已保存 “share/ai-support/models/nanodet-plus-m_320.onnx” [4786922/4786922])

板上执行目标检测 DEMO：

```sh
root@k1:~/spacemit-ai-sdk.v1.1.0/bianbu-ai-support# bin/detection_demo share/ai-support/models/nanodet-plus-m_320.onnx share/ai-support/models/coco.txt share/ai-support/imgs/person.jpg result0.jpg
Enable spacemit ep now
bbox[ 0] x1y1x2y2: (1346, 404,1525, 777), score: 0.727, label_text: person
bbox[ 1] x1y1x2y2: (1476, 412,1598, 766), score: 0.605, label_text: person
bbox[ 2] x1y1x2y2: ( 581, 447, 666, 706), score: 0.602, label_text: person
bbox[ 3] x1y1x2y2: (1840, 430,1919, 654), score: 0.470, label_text: person
bbox[ 4] x1y1x2y2: ( 459, 447, 551, 707), score: 0.462, label_text: person
bbox[ 5] x1y1x2y2: ( 689, 468, 745, 601), score: 0.430, label_text: person
bbox[ 6] x1y1x2y2: ( 660, 460, 722, 641), score: 0.401, label_text: person
```

板上生成带 bounding box 的检测框图：

```sh
root@k1:~/spacemit-ai-sdk.v1.1.0/bianbu-ai-support# file result0.jpg 
result0.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1920x1080, components 3
```

理论可用 ```bash demo/build.sh --test``` 执行自动化 DEMO 测试。但在板上执行时出现 dirname 需要更多参数的提示，无法继续执行。猜测是 ```DEMO_DIR=$(dirname $(readlink -f ${BASH_SOURCE[0]}))``` 一句中 readlink 未返回字符串，脚本没有很好处理空字符串的缘故。

理论还可将目标检测模型应用于视频流（detection_video_demo）、检测后进行带框视频推流（detection_stream_demo）。但目前没有与板子的图形化通信手段，仅通过串口无法观察实际 DEMO 效果，暂时搁置。

### DEMO 运行总结

#### SDK 集成说明

该 SDK 仍在活跃更新中。笔者昨晚测试时 SDK 下载链接还是 https://archive.spacemit.com/spacemit-ai/spacemit-ai-sdk/spacemit-ai-sdk.v1.1.0.tar.gz，大约 3 小时后链接即失效（文件名更改为 spacemit-ai-sdk.v1.1.0.x86_64.tar.gz）。如需加入 RuyiSDK 中，需要持续监控、跟进 SDK 链接。

该 SDK 耦合度较高、需要执行 source ./.spine.rc 后方可应用 SDK 工具链，可能临时性破坏用户原有 Shell 环境。如需调用其中工具链，建议采取隔离措施。

该 SDK 提供了 C++、Python 两类接口，主要使用 onnxruntime 推理对应 AI 模型。使用方法与公版 onnxruntime 包大差不差，但需要从其[私有源](https://archive.spacemit.com/spacemit-ai/onnxruntime/)下载 python 包。

其中 Python 包调用时需要增加 providers，示例：```ort.InferenceSession(net_param_path, providers=["SpaceMITExecutionProvider"])```。而 C++ 库的链接方法可以参考 demo 目录下的 build.sh 脚本。

#### 问题及状态

暂无。