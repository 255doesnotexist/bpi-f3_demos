## SpacemiT SDK

参考官方快速上手文档：https://developer.spacemit.com/#/documentation?token=KmlMwkcOIi0fp3kUyDHcyOa8ntf

### 下载及解压 SDK

```sh
wget https://archive.spacemit.com/spacemit-ai/spacemit-ai-sdk/spacemit-ai-sdk.v1.1.0.tar.gz --no-check-certificate
tar xzf spacemit-ai-sdk.v1.1.0.tar.gz
```

（如遇 URL 更新，请前往 https://archive.spacemit.com/spacemit-ai/spacemit-ai-sdk/ 查看最新版本 SDK 下载链接）

### 安装依赖

理论 yum / deb 系发行版全系可用。但 ./install.sh 有硬判断发行版限制。如用 Ubuntu / CentOS 可直接执行 ./install.sh 安装依赖。否则：

Debian 系可尝试安装：

```sh
apt update
# install dependencies for qemu
apt install -y libglib2.0-0
# install dependencies for xquant
apt install -y libgl1 # libgl1-mesa-glx
# install dependencies for support library
apt install -y cmake wget
```

CentOS 系可尝试安装：

```sh
  # install dependencies for xquant
  yum install libGL-devel
  # install dependencies for support library
  yum install -y cmake wget
```

然后在 SDK 根目录下执行：

```sh
source ./.spine.rc # switch to spine environment
spine # first initialization
```

在 spine 初次初始化时。它会自动安装剩余依赖。

### 简单跑跑相关 demo

paddle 相关 demo：

```sh
quick_start paddle
```

示例输出：

```sh
[INFO] 2024-07-12 18:26:57 Running test case: test_convert_paddle ....
[INFO] Convert dataset/paddle/classification/resnet50/inference.pdmodel ...
[Paddle2ONNX] Start to parse PaddlePaddle model...
[Paddle2ONNX] Model file path: ./dataset/paddle/classification/resnet50/inference.pdmodel
[Paddle2ONNX] Paramters file path: ./dataset/paddle/classification/resnet50/inference.pdiparams
[Paddle2ONNX] Start to parsing Paddle model...
[Paddle2ONNX] Use opset_version = 9 for ONNX export.
[Paddle2ONNX] PaddlePaddle model is exported as ONNX format now.
2024-07-12 18:27:00 | xquant.xquant_setting    | INFO     | Not set output_prefix, deatults to inference.q.
2024-07-12 18:27:00 | xquant.xquant_setting    | WARNING  | Specifies that cuda is used but not detected. Turn to cpu.
2024-07-12 18:27:00 | xquant.xquant_pipeline   | INFO     | using api input onnx model dataset/paddle/classification/resnet50/inference.onnx.
2024-07-12 18:27:00 | xquant.xquant_pipeline   | INFO     | using api output path dataset/paddle/classification/resnet50/inference.q.onnx.
2024-07-12 18:27:01 | xquant.xquant_pipeline   | INFO     | simplify onnx model...
2024-07-12 18:27:03 | xquant.onnx_graph_helper | WARNING  | convert ai.onnx version 9 to 13...
Layerwise Equalization: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:38<00:00,  3.85s/it]
Runtime Calibration(BlockWise): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21/21 [02:56<00:00,  8.42s/it]
Analysing Dequantized: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 17/17 [00:01<00:00, 13.12it/s]
Analysing Quantized: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 17/17 [00:01<00:00,  9.91it/s]
2024-07-12 18:30:44 | xquant.analyse.graphwise | INFO     | export quantization statistical results file to /home/xyz/spacemit-ai-sdk.v1.1.0/dataset/paddle/classification/resnet50/inference.q_report.md
2024-07-12 18:30:44 | xquant.xquant_pipeline   | INFO     | quantization eplased time 223.61 s
[INFO] 2024-07-12 18:30:45 Running test case: test_convert_paddle done
```

QEMU 仿真实机板运行模型示例输出：

```sh
[INFO] 2024-07-12 18:30:45 Running test case: test_simulate_paddle_qemu test_data ....
[INFO] Simulation (qemu-)test with dataset/paddle/classification/resnet50/inference.onnx ...
touch: cannot touch '/home/xyz/spacemit-ai-sdk.v1.1.0/.cache': Permission denied
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_0 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_1 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_2 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_3 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_4 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_5 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_6 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_7 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_8 done
[INFO] create random test data under /home/xyz/spacemit-ai-sdk.v1.1.0/test_data/paddle/classification/resnet50/test_data_set_9 done

result: 
        Models: 1
        Total test cases: 10
                Succeeded: 10
                Not implemented: 0
                Failed: 0
        Stats by Operator type:
                Not implemented(0): 
                Failed:
Failed Test Cases:
[INFO] 2024-07-12 18:43:19 Running test case: test_simulate_paddle_qemu test_data done
[INFO] 2024-07-12 18:43:19 Running test case: test_quantize_paddle ....
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple, https://pypi.ngc.nvidia.com
Requirement already satisfied: opencv-python in ./spacengine-xquant/lib/python3.8/site-packages (4.10.0.84)
Requirement already satisfied: numpy>=1.17.0 in ./spacengine-xquant/lib/python3.8/site-packages (from opencv-python) (1.24.4)
[INFO] Eval dataset/paddle/classification/resnet50/inference.onnx:
Prec@1 0.750 = 45 / 60
Prec@5 0.967 = 58 / 60
[INFO] Eval dataset/paddle/classification/resnet50/inference.q.onnx:
Prec@1 0.767 = 46 / 60
Prec@5 0.967 = 58 / 60
[INFO] 2024-07-12 18:43:26 Running test case: test_quantize_paddle done
[INFO] 2024-07-12 18:43:26 Running test case: test_spacemit_ai_demo ....
~/spacemit-ai-sdk.v1.1.0/demo ~/spacemit-ai-sdk.v1.1.0
[ 16%] Built target classification_demo
[ 33%] Built target detection_demo
[ 50%] Built target detection_video_demo
[ 66%] Built target detection_stream_demo
[ 83%] Built target estimation_demo
[100%] Built target tracker_stream_demo
[INFO] Prepare ...
[INFO] Smoke test with image classification task ...
[INFO] Run: build/classification_demo data/models/squeezenet1.1-7.onnx data/models/synset.txt data/imgs/dog.jpg
open tcm device failed(-1)
Enable spacemit ep now
tcm check param err--->fun:tcm_malloc_sync + line:164Classify result: n02113023 Pembroke, Pembroke Welsh corgi
[INFO] Smoke test with object detection task ...
[INFO] Run: build/detection_demo data/models/nanodet-plus-m_320.onnx data/models/coco.txt data/imgs/person.jpg result0.jpg
open tcm device failed(-1)
Enable spacemit ep now
tcm check param err--->fun:tcm_malloc_sync + line:164bbox[ 0] x1y1x2y2: (1346, 404,1525, 777), score: 0.727, label_text: person
bbox[ 1] x1y1x2y2: (1476, 412,1598, 766), score: 0.605, label_text: person
bbox[ 2] x1y1x2y2: ( 581, 447, 666, 706), score: 0.602, label_text: person
bbox[ 3] x1y1x2y2: (1840, 430,1919, 654), score: 0.470, label_text: person
bbox[ 4] x1y1x2y2: ( 459, 447, 551, 707), score: 0.462, label_text: person
bbox[ 5] x1y1x2y2: ( 689, 468, 745, 601), score: 0.430, label_text: person
bbox[ 6] x1y1x2y2: ( 660, 460, 722, 641), score: 0.401, label_text: person
~/spacemit-ai-sdk.v1.1.0
[INFO] 2024-07-12 18:43:45 Running test case: test_spacemit_ai_demo done
```

官方提供的脚本，基本上在 QEMU 中仿真了 BPI-F3 上的 SpacemiT X60 SDK 执行 paddle 模型转换、模型量化、模型推理、图像分类任务、目标检测任务的执行。