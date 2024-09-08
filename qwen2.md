# BananaPI BPI-F3 运行 Qwen2 0.5B Q5_K_M 量化版

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

* Demo 说明
  
  本 Demo 能利用 BPI-F3 的 rvv 1.0 特性加速推理端侧大语言模型。
* Demo 源码链接

  https://github.com/255doesnotexist/bpi-f3_demos

  以及 llama.cpp 官方仓库。
* SDK 及链接
  
  本 Demo 运行不需要厂商 SDK。
  
  在开发板上启用 RISCV=1 FLAG 全量编译 llama.cpp 并指定模型即可。

### Demo运行

#### 克隆 llama.cpp 仓库代码

```
git clone git@github.com:ggerganov/llama.cpp.git
cd llama.cpp
```

#### 附加 RISCV=1 FLAG 并编译

```shell
make RISCV=1
```

#### 下载 Q5_K_M 量化的 Qwen2 模型

```shell
wget -O qwen2-0_5b-instruct-q5_k_m.gguf "https://huggingface.co/Qwen/Qwen2-0.5B-Instruct-GGUF/resolve/main/qwen2-0_5b-instruct-q5_k_m.gguf?download=true"
```

#### 启动 OpenAI-like API 为各类 chatbot 提供服务

```shell
./llama-server -m qwen2-0_5b-instruct-q5_k_m.gguf -fa
```

#### 或以交互模式启动直接与 Qwen2 对话

```shell
./llama-cli -m qwen2-0_5b-instruct-q5_k_m.gguf \
  -n 512 -co -i -if -f prompts/chat-with-qwen.txt \
  --in-prefix "<|im_start|>user\n" \
  --in-suffix "<|im_end|>\n<|im_start|>assistant\n" \
  -fa
```

### 实际运行记录

```shell
root@k1:~/llama.cpp# ./llama-cli -m qwen2-0_5b-instruct-q5_k_m.gguf   -n 512 -co -i -if -f prompts/chat-with-qwen.txt   --in-prefix "<|im_start|>user\n"   --in-suffix "<|im_end|>\n<|im_start|>assistant\n"   -fa
Log start
main: build = 3673 (8ebe8dde)
main: built with cc (Ubuntu 13.2.0-4ubuntu3-bb2) 13.2.0 for riscv64-linux-gnu
main: seed  = 1725819530
llama_model_loader: loaded meta data with 26 key-value pairs and 290 tensors from qwen2-0_5b-instruct-q5_k_m.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen2
llama_model_loader: - kv   1:                               general.name str              = qwen2-0_5b-instruct
llama_model_loader: - kv   2:                          qwen2.block_count u32              = 24
llama_model_loader: - kv   3:                       qwen2.context_length u32              = 32768
llama_model_loader: - kv   4:                     qwen2.embedding_length u32              = 896
llama_model_loader: - kv   5:                  qwen2.feed_forward_length u32              = 4864
llama_model_loader: - kv   6:                 qwen2.attention.head_count u32              = 14
llama_model_loader: - kv   7:              qwen2.attention.head_count_kv u32              = 2
llama_model_loader: - kv   8:                       qwen2.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv   9:     qwen2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                          general.file_type u32              = 17
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  12:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,151936]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,151936]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 151643
llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 151643
llama_model_loader: - kv  19:                    tokenizer.chat_template str              = {% for message in messages %}{% if lo...
llama_model_loader: - kv  20:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - kv  22:                      quantize.imatrix.file str              = ../Qwen2/gguf/qwen2-0_5b-imatrix/imat...
llama_model_loader: - kv  23:                   quantize.imatrix.dataset str              = ../sft_2406.txt
llama_model_loader: - kv  24:             quantize.imatrix.entries_count i32              = 168
llama_model_loader: - kv  25:              quantize.imatrix.chunks_count i32              = 1937
llama_model_loader: - type  f32:  121 tensors
llama_model_loader: - type q5_1:  132 tensors
llama_model_loader: - type q8_0:   13 tensors
llama_model_loader: - type q5_K:   12 tensors
llama_model_loader: - type q6_K:   12 tensors
llm_load_vocab: special tokens cache size = 293
llm_load_vocab: token to piece cache size = 0.9338 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = qwen2
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 151936
llm_load_print_meta: n_merges         = 151387
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 32768
llm_load_print_meta: n_embd           = 896
llm_load_print_meta: n_layer          = 24
llm_load_print_meta: n_head           = 14
llm_load_print_meta: n_head_kv        = 2
llm_load_print_meta: n_rot            = 64
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 64
llm_load_print_meta: n_embd_head_v    = 64
llm_load_print_meta: n_gqa            = 7
llm_load_print_meta: n_embd_k_gqa     = 128
llm_load_print_meta: n_embd_v_gqa     = 128
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-06
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 4864
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 2
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 1000000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 32768
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: ssm_dt_b_c_rms   = 0
llm_load_print_meta: model type       = 1B
llm_load_print_meta: model ftype      = Q5_K - Medium
llm_load_print_meta: model params     = 494.03 M
llm_load_print_meta: model size       = 394.95 MiB (6.71 BPW) 
llm_load_print_meta: general.name     = qwen2-0_5b-instruct
llm_load_print_meta: BOS token        = 151643 '<|endoftext|>'
llm_load_print_meta: EOS token        = 151645 '<|im_end|>'
llm_load_print_meta: PAD token        = 151643 '<|endoftext|>'
llm_load_print_meta: LF token         = 148848 'ÄĬ'
llm_load_print_meta: EOT token        = 151645 '<|im_end|>'
llm_load_print_meta: max token length = 256
llm_load_tensors: ggml ctx size =    0.13 MiB
llm_load_tensors:        CPU buffer size =   394.95 MiB
...................................................
llama_new_context_with_model: n_ctx      = 32768
llama_new_context_with_model: n_batch    = 2048
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 1
llama_new_context_with_model: freq_base  = 1000000.0
llama_new_context_with_model: freq_scale = 1
llama_kv_cache_init:        CPU KV buffer size =   384.00 MiB
llama_new_context_with_model: KV self size  =  384.00 MiB, K (f16):  192.00 MiB, V (f16):  192.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.58 MiB
llama_new_context_with_model:        CPU compute buffer size =   298.50 MiB
llama_new_context_with_model: graph nodes  = 751
llama_new_context_with_model: graph splits = 1

system_info: n_threads = 8 (n_threads_batch = 8) / 8 | AVX = 0 | AVX_VNNI = 0 | AVX2 = 0 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | AVX512_BF16 = 0 | FMA = 0 | NEON = 0 | SVE = 0 | ARM_FMA = 0 | F16C = 0 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 0 | SSSE3 = 0 | VSX = 0 | MATMUL_INT8 = 0 | LLAMAFILE = 1 | 
main: interactive mode on.
Input prefix: '<|im_start|>user
'
Input suffix: '<|im_end|>
<|im_start|>assistant
'
sampling: 
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        top_k = 40, tfs_z = 1.000, top_p = 0.950, min_p = 0.050, typical_p = 1.000, temp = 0.800
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampling order: 
CFG -> Penalties -> top_k -> tfs_z -> typical_p -> top_p -> min_p -> temperature 
generate: n_ctx = 32768, n_batch = 2048, n_predict = 512, n_keep = 0


== Running in interactive mode. ==
 - Press Ctrl+C to interject at any time.
 - Press Return to return control to the AI.
 - To return control without starting a new line, end your input with '/'.
 - If you want to submit another line, end your input with '\'.

You are a helpful assistant.<|im_start|>user
我今天早上喝了一瓶1元钱的牛奶，并吃了1块钱的大肉包。请以 JSON 形式记录我早上吃了什么。并在其中为每样食物给出判断：与一般物价比，是贵了还是便宜了？
<|im_end|>
<|im_start|>assistant
 ```json
{
  "food": {
    "milk": "贵",
    "meat": "便宜"
  },
  "price": {
    "milk": 1,
    "meat": 1
  }
}```
<|im_start|>user


llama_print_timings:        load time =    1014.83 ms
llama_print_timings:      sample time =      62.43 ms /    55 runs   (    1.14 ms per token,   881.00 tokens per second)
llama_print_timings: prompt eval time =  102769.03 ms /    66 tokens ( 1557.11 ms per token,     0.64 tokens per second)
llama_print_timings:        eval time =   11765.31 ms /    54 runs   (  217.88 ms per token,     4.59 tokens per second)
llama_print_timings:       total time =  117412.80 ms /   120 tokens
```

### Demo 运行总结

#### 集成说明

目前执行方式仍需要即时克隆 llama.cpp 仓库并在本地编译。

可以依照机型考虑提供预编译的二进制，节省用户体验前等待耗时。

如果机型不匹配再回落到编译模式。

另，从 huggingface 拉取 Qwen2 模型的部分可能在部分地区存在网络问题。可以考虑 modelscope 作为替代。

#### 问题及状态

暂无