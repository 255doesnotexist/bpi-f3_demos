# BananaPI BPI-F3 运行 ChatGLM2 Q4 量化版

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

### Demo简介

参考官方演示视频：https://www.youtube.com/watch?v=Kn7GYiOxato


* demo说明

  > 这个demo大致是干什么的
  >
* demo源码链接

  > demo完整源码链接；该信息将用于包管理器集成/打包集成的信息输入
  >
* sdk 及链接
* Demo 运行所需的 SDK；用于 ruyisdk 集成 sdk；

### Demo运行

- WIP (现役开发板没有 16GB RAM，无法运行，暂时搁置)

> * 另起文档单独描述Demo运行起来的详细步骤；
> * 要求0基础入门级别的人能够按照文档操作；
> * 文档目的：
>   * 集成前：该文档后续用于IDE集成参考；
>   * 集成后：尽量能够做到替换到文档中的通过ruyisdk下载解压等操作外，其它内容可以大幅度参考和复用；修改后的文档将作为ruyisdk社区文档/教材/宣发用途；
> * 可选，欢迎出运行视频、玩机视频； 用于更加直观的 IDE集成指导、社区文档/教材/宣发用途；

下载 Q4 量化的 chatglm2 模型

./download.sh

安装 Python 依赖

root@k1:~# pip install --break-system-packages

### Demo运行总结

#### sdk 集成说明

> 给出需要 ruyisdk 集成建议或者总结;

#### 问题及状态

> 问题描述或者问题issue链接；用于跟踪/推动问题解决；