# Qwen Models — Complete Classification Taxonomy

**Total models classified: 458**

Source: HuggingFace Hub API (`Qwen` organization) — 458 models.

## Executive Summary

### By Model Family / Generation
| Family | Count |
| --- | --- |
| Qwen3 | 183 |
| Qwen2.5 | 102 |
| Qwen2 | 59 |
| Qwen1.5 | 54 |
| Qwen (original) | 28 |
| Qwen3.5 | 21 |
| QwQ | 4 |
| Qwen3.6 | 4 |
| QVQ | 1 |
| Qwen-AgentWorld | 1 |
| Other | 1 |

### By Capability / Pipeline
| Capability | Count |
| --- | --- |
| Text Generation | 305 |
| Quantized | 205 |
| Vision-Language | 86 |
| Code | 44 |
| Interpretability | 14 |
| Reward/Preference | 9 |
| Text Classification | 9 |
| Audio/Speech | 8 |
| Omni/Multimodal | 7 |
| Embeddings | 7 |
| Image Gen/Edit | 6 |
| Audio/Speech (TTS) | 5 |
| Reranking | 5 |
| Agent/Simulation | 4 |
| Other/Unknown | 3 |
| Token Classification | 1 |

### By Architecture Type
| Architecture | Count |
| --- | --- |
| Dense | 368 |
| MoE (A3B) | 41 |
| MoE (A22B) | 18 |
| Specialized (ASR) | 6 |
| Diffusion | 5 |
| Specialized (TTS) | 5 |
| MoE (A14B) | 4 |
| MoE (A17B) | 3 |
| MoE (A10B) | 3 |
| MoE (A2.7B) | 3 |
| MoE (A35B) | 2 |

### By Size Tier
| Size Tier | Count |
| --- | --- |
| Micro (<2B) | 92 |
| Small (2-8B) | 149 |
| Medium (8-35B) | 117 |
| Large (35-100B) | 51 |
| XLarge (>100B) | 31 |
| Unknown | 18 |

### By HuggingFace Pipeline Tag
| Pipeline Tag | Count |
| --- | --- |
| text-generation | 305 |
| image-text-to-text | 86 |
| (none) | 20 |
| text-classification | 9 |
| any-to-any | 7 |
| feature-extraction | 5 |
| automatic-speech-recognition | 5 |
| text-ranking | 5 |
| text-to-speech | 4 |
| image-to-image | 3 |
| text-to-image | 2 |
| audio-text-to-text | 2 |
| sentence-similarity | 2 |
| image-text-to-image | 1 |
| audio-to-audio | 1 |
| token-classification | 1 |

## Size Distribution Chart

| Micro (<2B)          | ██████████████████████████████░░░░░░░░░░░░░░░░░░░░ |  92 |
| Small (2-8B)         | ██████████████████████████████████████████████████ | 149 |
| Medium (8-35B)       | ███████████████████████████████████████░░░░░░░░░░░ | 117 |
| Large (35-100B)      | █████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ |  51 |
| XLarge (>100B)       | ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ |  31 |
| Unknown              | ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ |  18 |

## Detailed Classification by Family

### Other (1 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| WebWorld-8B | 8.0 | Small (2-8B) | Dense | Text Generation, Agent/Simulation | text-generation | 64 |

### QVQ (1 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| QVQ-72B-Preview | 72.0 | Large (35-100B) | Dense | Vision-Language | image-text-to-text | 610 |

### QwQ (4 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| QwQ-32B | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 2937 |
| QwQ-32B-Preview | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 1740 |
| QwQ-32B-GGUF | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 211 |
| QwQ-32B-AWQ | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 134 |

### Qwen (original) (28 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen-Image | - | Unknown | Diffusion | Image Gen/Edit | text-to-image | 2529 |
| Qwen-Image-Edit | - | Unknown | Diffusion | Image Gen/Edit | image-to-image | 2444 |
| Qwen-Image-Edit-2509 | - | Unknown | Diffusion | Image Gen/Edit | image-to-image | 1190 |
| Qwen-Image-Layered | - | Unknown | Dense | Image Gen/Edit | image-text-to-image | 1115 |
| Qwen-Image-Edit-2511 | - | Unknown | Diffusion | Image Gen/Edit | image-to-image | 1099 |
| Qwen-Image-2512 | - | Unknown | Diffusion | Image Gen/Edit | text-to-image | 897 |
| Qwen-7B-Chat | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 789 |
| Qwen-7B | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 399 |
| Qwen-VL-Chat | - | Unknown | Dense | Text Generation | text-generation | 384 |
| Qwen-14B-Chat | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 373 |
| Qwen-72B | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 360 |
| Qwen-VL | - | Unknown | Dense | Text Generation | text-generation | 284 |
| Qwen-14B | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 214 |
| Qwen-72B-Chat | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 156 |
| Qwen-Audio | - | Unknown | Dense | Text Generation | text-generation | 149 |
| Qwen-14B-Chat-Int4 | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 100 |
| Qwen-Audio-Chat | - | Unknown | Dense | Text Generation | text-generation | 96 |
| Qwen-VL-Chat-Int4 | - | Unknown | Dense | Quantized, Text Generation | text-generation | 95 |
| Qwen-7B-Chat-Int4 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 75 |
| Qwen-1_8B | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 73 |
| Qwen-Image-Bench | - | Unknown | Dense | Vision-Language | image-text-to-text | 73 |
| Qwen-72B-Chat-Int4 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 47 |
| Qwen-1_8B-Chat-Int4 | 8.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 36 |
| Qwen-tokenizer | - | Unknown | Dense | Other/Unknown | - | 20 |
| Qwen-72B-Chat-Int8 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 17 |
| Qwen-7B-Chat-Int8 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 9 |
| Qwen-14B-Chat-Int8 | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 7 |
| Qwen-1_8B-Chat-Int8 | 8.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 5 |

### Qwen-AgentWorld (1 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen-AgentWorld-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | Text Generation, Agent/Simulation | text-generation | 530 |

### Qwen1.5 (54 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| CodeQwen1.5-7B-Chat | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 353 |
| Qwen1.5-MoE-A2.7B | 2.7 | Small (2-8B) | MoE (A2.7B) | Text Generation | text-generation | 227 |
| Qwen1.5-72B-Chat | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 217 |
| Qwen1.5-7B-Chat | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 186 |
| Qwen1.5-0.5B | 0.5 | Micro (<2B) | Dense | Text Generation | text-generation | 174 |
| Qwen1.5-MoE-A2.7B-Chat | 2.7 | Small (2-8B) | MoE (A2.7B) | Text Generation | text-generation | 134 |
| Qwen1.5-110B-Chat | 110.0 | XLarge (>100B) | Dense | Text Generation | text-generation | 130 |
| Qwen1.5-14B-Chat | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 112 |
| CodeQwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 111 |
| Qwen1.5-32B-Chat | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 109 |
| CodeQwen1.5-7B | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 104 |
| Qwen1.5-110B | 110.0 | XLarge (>100B) | Dense | Text Generation | text-generation | 104 |
| Qwen1.5-0.5B-Chat | 0.5 | Micro (<2B) | Dense | Text Generation | text-generation | 98 |
| Qwen1.5-32B | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 85 |
| Qwen1.5-1.8B-Chat | 1.8 | Micro (<2B) | Dense | Text Generation | text-generation | 74 |
| Qwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 71 |
| Qwen1.5-14B-Chat-GGUF | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 67 |
| Qwen1.5-72B-Chat-GGUF | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 62 |
| Qwen1.5-1.8B | 1.8 | Micro (<2B) | Dense | Text Generation | text-generation | 59 |
| Qwen1.5-72B | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 59 |
| Qwen1.5-7B | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 56 |
| Qwen1.5-32B-Chat-GGUF | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 52 |
| Qwen1.5-MoE-A2.7B-Chat-GPTQ-Int4 | 2.7 | Small (2-8B) | MoE (A2.7B) | Quantized, Text Generation | text-generation | 50 |
| Qwen1.5-4B-Chat | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 46 |
| Qwen1.5-14B | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 41 |
| Qwen1.5-72B-Chat-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 37 |
| Qwen1.5-4B | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 36 |
| Qwen1.5-0.5B-Chat-GGUF | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 35 |
| Qwen1.5-32B-Chat-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 31 |
| Qwen1.5-72B-Chat-AWQ | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 26 |
| Qwen1.5-7B-Chat-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 26 |
| Qwen1.5-14B-Chat-AWQ | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 23 |
| Qwen1.5-1.8B-Chat-GGUF | 1.8 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 21 |
| Qwen1.5-14B-Chat-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 21 |
| Qwen1.5-7B-Chat-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 18 |
| Qwen1.5-32B-Chat-AWQ | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 18 |
| Qwen1.5-110B-Chat-GPTQ-Int4 | 110.0 | XLarge (>100B) | Dense | Quantized, Text Generation | text-generation | 18 |
| Qwen1.5-4B-Chat-GGUF | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 16 |
| Qwen1.5-0.5B-Chat-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 14 |
| CodeQwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 14 |
| Qwen1.5-110B-Chat-GGUF | 110.0 | XLarge (>100B) | Dense | Quantized, Text Generation | text-generation | 14 |
| Qwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 13 |
| Qwen1.5-14B-Chat-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 11 |
| Qwen1.5-110B-Chat-AWQ | 110.0 | XLarge (>100B) | Dense | Quantized, Text Generation | text-generation | 9 |
| Qwen1.5-0.5B-Chat-AWQ | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 7 |
| Qwen1.5-72B-Chat-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 7 |
| Qwen1.5-1.8B-Chat-GPTQ-Int4 | 1.8 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 7 |
| Qwen1.5-4B-Chat-GPTQ-Int8 | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 6 |
| Qwen1.5-4B-Chat-GPTQ-Int4 | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 6 |
| Qwen1.5-1.8B-Chat-AWQ | 1.8 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 4 |
| Qwen1.5-0.5B-Chat-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 4 |
| Qwen1.5-4B-Chat-AWQ | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 3 |
| Qwen1.5-1.8B-Chat-GPTQ-Int8 | 1.8 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 2 |
| CodeQwen1.5-7B-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 2 |

### Qwen2 (59 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen2-VL-7B-Instruct | 7.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 1281 |
| Qwen2-72B-Instruct | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 718 |
| Qwen2-7B-Instruct | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 686 |
| Qwen2-Audio-7B-Instruct | 7.0 | Small (2-8B) | Dense | Audio/Speech | audio-text-to-text | 544 |
| Qwen2-VL-2B-Instruct | 2.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 512 |
| Qwen2-VL-72B-Instruct | 72.0 | Large (35-100B) | Dense | Vision-Language | image-text-to-text | 310 |
| Qwen2-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | Text Generation | text-generation | 201 |
| Qwen2-72B | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 199 |
| Qwen2-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 179 |
| Qwen2-Audio-7B | 7.0 | Small (2-8B) | Dense | Audio/Speech | audio-text-to-text | 172 |
| Qwen2-7B | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 171 |
| Qwen2-0.5B | 0.5 | Micro (<2B) | Dense | Text Generation | text-generation | 169 |
| Qwen2-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 162 |
| Qwen2-1.5B | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 102 |
| Qwen2-Math-72B-Instruct | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 89 |
| Qwen2-57B-A14B-Instruct | 57.0 | Large (35-100B) | MoE (A14B) | Text Generation | text-generation | 83 |
| WorldPM-72B | 72.0 | Large (35-100B) | Dense | Reward/Preference, Text Classification | text-classification | 82 |
| Qwen2-VL-72B | 72.0 | Large (35-100B) | Dense | Vision-Language | image-text-to-text | 80 |
| Qwen2-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 73 |
| Qwen2-VL-7B | 7.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 67 |
| Qwen2-VL-2B | 2.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 65 |
| Qwen2-57B-A14B | 57.0 | Large (35-100B) | MoE (A14B) | Text Generation | text-generation | 58 |
| Qwen2-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Quantized, Vision-Language | image-text-to-text | 50 |
| Qwen2-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 49 |
| Qwen2-Math-7B-Instruct | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 44 |
| Qwen2-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 41 |
| Qwen2-VL-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 37 |
| Qwen2-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 33 |
| Qwen2-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 31 |
| Qwen2-VL-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 31 |
| Qwen2-Math-72B | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 30 |
| Qwen2-VL-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Quantized, Vision-Language | image-text-to-text | 30 |
| Qwen2-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 29 |
| Qwen2-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 28 |
| Qwen2-VL-2B-Instruct-GPTQ-Int4 | 2.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 28 |
| Qwen2-VL-2B-Instruct-AWQ | 2.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 25 |
| Qwen2-57B-A14B-Instruct-GPTQ-Int4 | 57.0 | Large (35-100B) | MoE (A14B) | Quantized, Text Generation | text-generation | 23 |
| Qwen2-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 23 |
| Qwen2-Math-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 21 |
| Qwen2-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 17 |
| Qwen2-57B-A14B-Instruct-GGUF | 57.0 | Large (35-100B) | MoE (A14B) | Quantized, Text Generation | text-generation | 17 |
| Qwen2-VL-2B-Instruct-GPTQ-Int8 | 2.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 17 |
| Qwen2-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 15 |
| Qwen2-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 15 |
| Qwen2-Math-7B | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 14 |
| Qwen2-Math-1.5B | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 14 |
| Qwen2-VL-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Quantized, Vision-Language | image-text-to-text | 11 |
| WorldPM-72B-HelpSteer2 | 72.0 | Large (35-100B) | Dense | Reward/Preference, Text Classification | text-classification | 11 |
| WorldPM-72B-RLHFLow | 72.0 | Large (35-100B) | Dense | Reward/Preference, Text Classification | text-classification | 11 |
| Qwen2-0.5B-Instruct-MLX | 0.5 | Micro (<2B) | Dense | Text Generation | text-generation | 10 |
| Qwen2-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 9 |
| WorldPM-72B-UltraFeedback | 72.0 | Large (35-100B) | Dense | Reward/Preference, Text Classification | text-classification | 8 |
| Qwen2-Math-RM-72B | 72.0 | Large (35-100B) | Dense | Reward/Preference, Text Classification | text-classification | 7 |
| Qwen2-7B-Instruct-MLX | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 7 |
| Qwen2-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 5 |
| Qwen2-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 5 |
| Qwen2-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 4 |
| Qwen2-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 4 |
| Qwen2-1.5B-Instruct-MLX | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 4 |

### Qwen2.5 (102 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen2.5-Coder-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Code, Text Generation | text-generation | 2062 |
| Qwen2.5-Omni-7B | 7.0 | Small (2-8B) | Dense | Omni/Multimodal | any-to-any | 1913 |
| Qwen2.5-VL-7B-Instruct | 7.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 1605 |
| Qwen2.5-7B-Instruct | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 1397 |
| Qwen2.5-72B-Instruct | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 962 |
| Qwen2.5-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 757 |
| Qwen2.5-Coder-7B-Instruct | 7.0 | Small (2-8B) | Dense | Code, Text Generation | text-generation | 745 |
| Qwen2.5-VL-3B-Instruct | 3.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 670 |
| Qwen2.5-VL-72B-Instruct | 72.0 | Large (35-100B) | Dense | Vision-Language | image-text-to-text | 632 |
| Qwen2.5-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | Text Generation | text-generation | 549 |
| Qwen2.5-3B-Instruct | 3.0 | Small (2-8B) | Dense | Text Generation | text-generation | 521 |
| Qwen2.5-VL-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Vision-Language | image-text-to-text | 494 |
| Qwen2.5-0.5B | 0.5 | Micro (<2B) | Dense | Text Generation | text-generation | 428 |
| Qwen2.5-7B-Instruct-1M | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 371 |
| Qwen2.5-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 354 |
| Qwen2.5-14B-Instruct | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 351 |
| Qwen2.5-14B-Instruct-1M | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 341 |
| Qwen2.5-Omni-3B | 3.0 | Small (2-8B) | Dense | Omni/Multimodal | any-to-any | 337 |
| Qwen2.5-Coder-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 310 |
| Qwen2.5-7B | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 294 |
| Qwen2.5-Coder-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 209 |
| Qwen2.5-3B | 3.0 | Small (2-8B) | Dense | Text Generation | text-generation | 194 |
| Qwen2.5-1.5B | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 192 |
| Qwen2.5-32B | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 179 |
| Qwen2.5-Coder-14B-Instruct | 14.0 | Medium (8-35B) | Dense | Code, Text Generation | text-generation | 171 |
| Qwen2.5-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 164 |
| Qwen2.5-Coder-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 161 |
| Qwen2.5-Coder-32B | 32.0 | Medium (8-35B) | Dense | Code, Text Generation | text-generation | 157 |
| Qwen2.5-Coder-7B | 7.0 | Small (2-8B) | Dense | Code, Text Generation | text-generation | 155 |
| Qwen2.5-14B | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 154 |
| Qwen2.5-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 142 |
| Qwen2.5-Coder-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Code, Text Generation | text-generation | 132 |
| Qwen2.5-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 123 |
| Qwen2.5-Math-7B | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 114 |
| Qwen2.5-Coder-3B-Instruct | 3.0 | Small (2-8B) | Dense | Code, Text Generation | text-generation | 114 |
| Qwen2.5-Math-1.5B | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 110 |
| Qwen2.5-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 110 |
| Qwen2.5-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 106 |
| Qwen2.5-72B | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 101 |
| Qwen2.5-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 101 |
| Qwen2.5-Coder-1.5B | 1.5 | Micro (<2B) | Dense | Code, Text Generation | text-generation | 94 |
| Qwen2.5-Coder-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 93 |
| Qwen2.5-Math-7B-Instruct | 7.0 | Small (2-8B) | Dense | Text Generation | text-generation | 91 |
| Qwen2.5-Math-PRM-7B | 7.0 | Small (2-8B) | Dense | Reward/Preference, Text Classification | text-classification | 90 |
| Qwen2.5-Math-RM-72B | 72.0 | Large (35-100B) | Dense | Reward/Preference, Text Classification | text-classification | 83 |
| Qwen2.5-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 78 |
| Qwen2.5-Coder-14B | 14.0 | Medium (8-35B) | Dense | Code, Text Generation | text-generation | 77 |
| Qwen2.5-Math-PRM-72B | 72.0 | Large (35-100B) | Dense | Reward/Preference, Text Classification | text-classification | 77 |
| Qwen2.5-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Quantized, Vision-Language | image-text-to-text | 73 |
| Qwen2.5-Coder-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | Code, Text Generation | text-generation | 72 |
| Qwen2.5-Coder-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 69 |
| Qwen2.5-VL-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 64 |
| Qwen2.5-VL-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 63 |
| Qwen2.5-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 59 |
| Qwen2.5-Math-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Text Generation | text-generation | 58 |
| Qwen2.5-Coder-0.5B | 0.5 | Micro (<2B) | Dense | Code, Text Generation | text-generation | 57 |
| Qwen2.5-Coder-3B | 3.0 | Small (2-8B) | Dense | Code, Text Generation | text-generation | 53 |
| Qwen2.5-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 47 |
| Qwen2.5-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 45 |
| Qwen2.5-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 44 |
| Qwen2.5-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 44 |
| Qwen2.5-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 40 |
| Qwen2.5-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 37 |
| Qwen2.5-Coder-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 37 |
| Qwen2.5-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 33 |
| Qwen2.5-Math-72B-Instruct | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 31 |
| Qwen2.5-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Quantized, Text Generation | text-generation | 28 |
| Qwen2.5-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 26 |
| Qwen2.5-Coder-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 26 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 24 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 24 |
| Qwen2.5-Coder-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 23 |
| Qwen2.5-Coder-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 21 |
| Qwen2.5-Math-7B-PRM800K | 7.0 | Small (2-8B) | Dense | Reward/Preference, Text Classification | text-classification | 21 |
| Qwen2.5-Math-72B | 72.0 | Large (35-100B) | Dense | Text Generation | text-generation | 18 |
| Qwen2.5-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 18 |
| Qwen2.5-Omni-7B-AWQ | 7.0 | Small (2-8B) | Dense | Quantized, Omni/Multimodal | any-to-any | 18 |
| Qwen2.5-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 16 |
| Qwen2.5-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 14 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 14 |
| Qwen2.5-Omni-7B-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Quantized, Omni/Multimodal | any-to-any | 14 |
| Qwen2.5-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 11 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 10 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 9 |
| Qwen2.5-Coder-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 8 |
| Qwen2.5-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Quantized, Code, Text Generation | text-generation | 7 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 6 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 5 |
| Qwen2.5-Coder-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 4 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 3 |
| Qwen2.5-Coder-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 2 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 1 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Quantized, Code, Text Generation | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | Quantized, Code, Text Generation | text-generation | 1 |

### Qwen3 (183 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | 1.7 | Micro (<2B) | Specialized (TTS) | Audio/Speech (TTS) | text-to-speech | 1669 |
| Qwen3-Coder-Next | - | Unknown | Dense | Code, Text Generation | text-generation | 1505 |
| Qwen3-0.6B | 0.6 | Micro (<2B) | Dense | Text Generation | text-generation | 1383 |
| Qwen3-Coder-480B-A35B-Instruct | 480.0 | XLarge (>100B) | MoE (A35B) | Code, Text Generation | text-generation | 1347 |
| Qwen3-8B | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 1178 |
| Qwen3-Coder-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | Code, Text Generation | text-generation | 1139 |
| Qwen3-235B-A22B | 235.0 | XLarge (>100B) | MoE (A22B) | Text Generation | text-generation | 1100 |
| Qwen3-Embedding-0.6B | 0.6 | Micro (<2B) | Dense | Embeddings | feature-extraction | 1094 |
| Qwen3-Next-80B-A3B-Instruct | 80.0 | Large (35-100B) | MoE (A3B) | Text Generation | text-generation | 1032 |
| Qwen3-VL-8B-Instruct | 8.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 978 |
| Qwen3-Omni-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | Omni/Multimodal | any-to-any | 954 |
| Qwen3-ASR-1.7B | 1.7 | Micro (<2B) | Specialized (ASR) | Audio/Speech | automatic-speech-recognition | 911 |
| Qwen3-30B-A3B | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 905 |
| Qwen3-4B-Instruct-2507 | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 892 |
| Qwen3-30B-A3B-Instruct-2507 | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 819 |
| Qwen3-235B-A22B-Instruct-2507 | 235.0 | XLarge (>100B) | MoE (A22B) | Text Generation | text-generation | 786 |
| Qwen3-Embedding-8B | 8.0 | Small (2-8B) | Dense | Embeddings | feature-extraction | 732 |
| Qwen3-32B | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 709 |
| Qwen3-4B | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 645 |
| Qwen3-4B-Thinking-2507 | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 600 |
| Qwen3-VL-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | Vision-Language | image-text-to-text | 582 |
| Qwen3-Embedding-0.6B-GGUF | 0.6 | Micro (<2B) | Dense | Quantized | - | 539 |
| Qwen3-1.7B | 1.7 | Micro (<2B) | Dense | Text Generation | text-generation | 496 |
| Qwen3-Next-80B-A3B-Thinking | 80.0 | Large (35-100B) | MoE (A3B) | Text Generation | text-generation | 490 |
| Qwen3-VL-Embedding-8B | 8.0 | Small (2-8B) | Dense | Embeddings | sentence-similarity | 451 |
| Qwen3-VL-2B-Instruct | 2.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 436 |
| Qwen3-TTS-12Hz-1.7B-Base | 1.7 | Micro (<2B) | Specialized (TTS) | Other/Unknown | - | 434 |
| Qwen3-VL-Embedding-2B | 2.0 | Small (2-8B) | Dense | Embeddings | sentence-similarity | 427 |
| Qwen3-14B | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 417 |
| Qwen3-235B-A22B-Thinking-2507 | 235.0 | XLarge (>100B) | MoE (A22B) | Text Generation | text-generation | 407 |
| Qwen3-VL-4B-Instruct | 4.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 404 |
| Qwen3-VL-235B-A22B-Instruct | 235.0 | XLarge (>100B) | MoE (A22B) | Vision-Language | image-text-to-text | 400 |
| Qwen3-VL-235B-A22B-Thinking | 235.0 | XLarge (>100B) | MoE (A22B) | Vision-Language | image-text-to-text | 399 |
| Qwen3-30B-A3B-Thinking-2507 | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 377 |
| Qwen3-Reranker-0.6B | 0.6 | Micro (<2B) | Dense | Reranking | text-ranking | 369 |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | 1.7 | Micro (<2B) | Specialized (TTS) | Audio/Speech (TTS) | text-to-speech | 366 |
| Qwen3-ASR-0.6B | 0.6 | Micro (<2B) | Specialized (ASR) | Audio/Speech | automatic-speech-recognition | 310 |
| Qwen3-Omni-30B-A3B-Thinking | 30.0 | Medium (8-35B) | MoE (A3B) | Omni/Multimodal | any-to-any | 309 |
| Qwen3-Embedding-4B | 4.0 | Small (2-8B) | Dense | Embeddings | feature-extraction | 292 |
| Qwen3-Coder-Next-GGUF | - | Unknown | Dense | Quantized, Code, Text Generation | text-generation | 260 |
| Qwen3-TTS-12Hz-0.6B-Base | 0.6 | Micro (<2B) | Specialized (TTS) | Audio/Speech (TTS) | text-to-speech | 259 |
| Qwen3-Reranker-8B | 8.0 | Small (2-8B) | Dense | Reranking | text-ranking | 248 |
| Qwen3-Omni-30B-A3B-Captioner | 30.0 | Medium (8-35B) | MoE (A3B) | Omni/Multimodal | any-to-any | 231 |
| Qwen3-VL-8B-Thinking | 8.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 215 |
| Qwen3-8B-GGUF | 8.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 212 |
| Qwen3-VL-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Vision-Language | image-text-to-text | 210 |
| Qwen3-VL-Reranker-2B | 2.0 | Small (2-8B) | Dense | Reranking | text-ranking | 201 |
| Qwen3-VL-30B-A3B-Thinking | 30.0 | Medium (8-35B) | MoE (A3B) | Vision-Language | image-text-to-text | 199 |
| Qwen3-Coder-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Code, Text Generation | text-generation | 187 |
| Qwen3-0.6B-Base | 0.6 | Micro (<2B) | Dense | Text Generation | text-generation | 174 |
| Qwen3-TTS-12Hz-0.6B-CustomVoice | 0.6 | Micro (<2B) | Specialized (TTS) | Audio/Speech (TTS) | text-to-speech | 164 |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | 480.0 | XLarge (>100B) | MoE (A35B) | Quantized, Code, Text Generation | text-generation | 156 |
| Qwen3-Coder-Next-FP8 | - | Unknown | Dense | Quantized, Code, Text Generation | text-generation | 156 |
| Qwen3-VL-Reranker-8B | 8.0 | Small (2-8B) | Dense | Reranking | text-ranking | 154 |
| Qwen3-235B-A22B-Instruct-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Text Generation | text-generation | 148 |
| Qwen3-Reranker-4B | 4.0 | Small (2-8B) | Dense | Reranking | text-ranking | 146 |
| Qwen3-ForcedAligner-0.6B | 0.6 | Micro (<2B) | Specialized (ASR) | Audio/Speech | automatic-speech-recognition | 145 |
| Qwen3-32B-AWQ | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 136 |
| Qwen3-30B-A3B-Instruct-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Text Generation | text-generation | 130 |
| Qwen3-Embedding-8B-GGUF | 8.0 | Small (2-8B) | Dense | Quantized | - | 129 |
| Qwen3Guard-Gen-8B | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 119 |
| Qwen3-VL-2B-Thinking | 2.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 115 |
| Qwen3-Embedding-4B-GGUF | 4.0 | Small (2-8B) | Dense | Quantized | - | 114 |
| Qwen3-4B-GGUF | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 113 |
| Qwen3-VL-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Vision-Language | image-text-to-text | 113 |
| Qwen3-VL-4B-Thinking | 4.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 113 |
| Qwen3-VL-8B-Instruct-GGUF | 8.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 111 |
| Qwen3-8B-Base | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 110 |
| Qwen3-14B-GGUF | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 109 |
| Qwen3-4B-Base | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 95 |
| Qwen3-235B-A22B-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Text Generation | text-generation | 93 |
| Qwen3-Next-80B-A3B-Instruct-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | Quantized, Text Generation | text-generation | 90 |
| Qwen3-VL-32B-Thinking | 32.0 | Medium (8-35B) | Dense | Vision-Language | image-text-to-text | 87 |
| Qwen3-235B-A22B-Thinking-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Text Generation | text-generation | 86 |
| Qwen3-32B-FP8 | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 84 |
| Qwen3-30B-A3B-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Text Generation | text-generation | 84 |
| Qwen3-4B-Instruct-2507-FP8 | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 78 |
| Qwen3-1.7B-Base | 1.7 | Micro (<2B) | Dense | Text Generation | text-generation | 75 |
| Qwen3Guard-Gen-0.6B | 0.6 | Micro (<2B) | Dense | Text Generation | text-generation | 75 |
| Qwen3-30B-A3B-Base | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 73 |
| Qwen3-VL-8B-Instruct-FP8 | 8.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 73 |
| Qwen3-30B-A3B-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Text Generation | text-generation | 72 |
| Qwen3-14B-AWQ | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 70 |
| Qwen3-TTS-Tokenizer-12Hz | - | Unknown | Dense | Audio/Speech, Audio/Speech (TTS) | audio-to-audio | 70 |
| Qwen3-Coder-Next-Base | - | Unknown | Dense | Code, Text Generation | text-generation | 70 |
| WebWorld-32B | 32.0 | Medium (8-35B) | Dense | Text Generation, Agent/Simulation | text-generation | 70 |
| Qwen3-32B-GGUF | 32.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 69 |
| Qwen3-30B-A3B-Thinking-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Text Generation | text-generation | 67 |
| Qwen3-4B-Thinking-2507-FP8 | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 66 |
| Qwen3-0.6B-GGUF | 0.6 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 63 |
| Qwen3-VL-4B-Instruct-FP8 | 4.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 63 |
| Qwen3-0.6B-FP8 | 0.6 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 62 |
| Qwen3-8B-FP8 | 8.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 62 |
| Qwen3-VL-30B-A3B-Thinking-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Vision-Language | image-text-to-text | 57 |
| Qwen3-14B-Base | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 54 |
| Qwen3-Next-80B-A3B-Thinking-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | Quantized, Text Generation | text-generation | 54 |
| Qwen3-30B-A3B-GPTQ-Int4 | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Text Generation | text-generation | 53 |
| Qwen3Guard-Gen-4B | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 52 |
| Qwen3-8B-AWQ | 8.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 51 |
| Qwen3-VL-2B-Instruct-GGUF | 2.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 50 |
| Qwen3-1.7B-GGUF | 1.7 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 49 |
| Qwen3-VL-4B-Instruct-GGUF | 4.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 49 |
| Qwen3-14B-FP8 | 14.0 | Medium (8-35B) | Dense | Quantized, Text Generation | text-generation | 48 |
| Qwen3-VL-32B-Instruct-FP8 | 32.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 46 |
| Qwen3-4B-SafeRL | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 44 |
| Qwen3-VL-235B-A22B-Instruct-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Vision-Language | image-text-to-text | 44 |
| Qwen3-VL-2B-Instruct-FP8 | 2.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 42 |
| Qwen3-4B-FP8 | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 39 |
| Qwen3Guard-Stream-8B | 8.0 | Small (2-8B) | Dense | Other/Unknown | - | 38 |
| SAE-Res-Qwen3.5-27B-W80K-L0_50 | 27.0 | Medium (8-35B) | Dense | Interpretability | - | 38 |
| Qwen3-1.7B-FP8 | 1.7 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 36 |
| Qwen3Guard-Stream-0.6B | 0.6 | Micro (<2B) | Dense | Embeddings | feature-extraction | 32 |
| Qwen3-VL-8B-Thinking-FP8 | 8.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 32 |
| Qwen3-Next-80B-A3B-Instruct-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | Quantized, Text Generation | text-generation | 32 |
| Qwen3-4B-MLX-4bit | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 31 |
| Qwen3-VL-2B-Thinking-FP8 | 2.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 31 |
| Qwen3-Next-80B-A3B-Thinking-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | Quantized, Text Generation | text-generation | 31 |
| Qwen3-VL-4B-Thinking-FP8 | 4.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 30 |
| Qwen3-4B-AWQ | 4.0 | Small (2-8B) | Dense | Quantized, Text Generation | text-generation | 29 |
| Qwen3-VL-235B-A22B-Thinking-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Vision-Language | image-text-to-text | 29 |
| WebWorld-14B | 14.0 | Medium (8-35B) | Dense | Text Generation, Agent/Simulation | text-generation | 28 |
| Qwen3-ASR-1.7B-hf | 1.7 | Micro (<2B) | Specialized (ASR) | Audio/Speech | automatic-speech-recognition | 28 |
| Qwen3-235B-A22B-GPTQ-Int4 | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Text Generation | text-generation | 27 |
| Qwen3-VL-8B-Thinking-GGUF | 8.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 27 |
| Qwen3-VL-32B-Thinking-FP8 | 32.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 26 |
| Qwen3-0.6B-MLX-4bit | 0.6 | Micro (<2B) | Dense | Text Generation | text-generation | 23 |
| Qwen3Guard-Stream-4B | 4.0 | Small (2-8B) | Dense | Embeddings | feature-extraction | 23 |
| Qwen3-VL-2B-Thinking-GGUF | 2.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 22 |
| Qwen3-VL-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 20 |
| Qwen3-ASR-0.6B-hf | 0.6 | Micro (<2B) | Specialized (ASR) | Audio/Speech | automatic-speech-recognition | 19 |
| Qwen3-VL-4B-Thinking-GGUF | 4.0 | Small (2-8B) | Dense | Quantized, Vision-Language | image-text-to-text | 18 |
| Qwen3-VL-30B-A3B-Instruct-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Vision-Language | image-text-to-text | 17 |
| Qwen3-235B-A22B-MLX-4bit | 235.0 | XLarge (>100B) | MoE (A22B) | Text Generation | text-generation | 16 |
| Qwen3-14B-MLX-4bit | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 14 |
| Qwen3-VL-32B-Thinking-GGUF | 32.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 13 |
| Qwen3-VL-235B-A22B-Instruct-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Vision-Language | image-text-to-text | 13 |
| SAE-Res-Qwen3.5-2B-Base-W32K-L0_50 | 2.0 | Small (2-8B) | Dense | Interpretability | - | 13 |
| SAE-Res-Qwen3.5-27B-W80K-L0_100 | 27.0 | Medium (8-35B) | Dense | Interpretability | - | 13 |
| Qwen3-32B-MLX-8bit | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 11 |
| Qwen3-30B-A3B-MLX-4bit | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 11 |
| Qwen3-VL-30B-A3B-Thinking-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Quantized, Vision-Language | image-text-to-text | 11 |
| Qwen3-ForcedAligner-0.6B-hf | 0.6 | Micro (<2B) | Specialized (ASR) | Token Classification | token-classification | 11 |
| Qwen3-235B-A22B-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Text Generation | text-generation | 10 |
| Qwen3-8B-MLX-4bit | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 10 |
| SAE-Res-Qwen3.5-9B-Base-W64K-L0_50 | 9.0 | Medium (8-35B) | Dense | Interpretability | - | 10 |
| Qwen3-0.6B-GPTQ-Int8 | 0.6 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 9 |
| Qwen3-8B-MLX-bf16 | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 9 |
| Qwen3-32B-MLX-bf16 | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 9 |
| Qwen3-30B-A3B-MLX-8bit | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 9 |
| Qwen3-235B-A22B-MLX-8bit | 235.0 | XLarge (>100B) | MoE (A22B) | Text Generation | text-generation | 9 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W128K-L0_100 | 35.0 | Medium (8-35B) | MoE (A3B) | Interpretability | - | 9 |
| Qwen3-8B-MLX-8bit | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 8 |
| Qwen3-32B-MLX-4bit | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 8 |
| Qwen3-30B-A3B-MLX-bf16 | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 8 |
| Qwen3-1.7B-GPTQ-Int8 | 1.7 | Micro (<2B) | Dense | Quantized, Text Generation | text-generation | 7 |
| Qwen3-1.7B-MLX-bf16 | 1.7 | Micro (<2B) | Dense | Text Generation | text-generation | 7 |
| SAE-Res-Qwen3.5-9B-Base-W64K-L0_100 | 9.0 | Medium (8-35B) | Dense | Interpretability | - | 7 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W32K-L0_50 | 35.0 | Medium (8-35B) | MoE (A3B) | Interpretability | - | 7 |
| Qwen3-0.6B-MLX-6bit | 0.6 | Micro (<2B) | Dense | Text Generation | text-generation | 6 |
| Qwen3-0.6B-MLX-bf16 | 0.6 | Micro (<2B) | Dense | Text Generation | text-generation | 6 |
| Qwen3-8B-MLX-6bit | 8.0 | Small (2-8B) | Dense | Text Generation | text-generation | 6 |
| Qwen3-235B-A22B-MLX-bf16 | 235.0 | XLarge (>100B) | MoE (A22B) | Text Generation | text-generation | 6 |
| Qwen3-14B-MLX-bf16 | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 6 |
| SAE-Res-Qwen3-8B-Base-W64K-L0_50 | 8.0 | Small (2-8B) | Dense | Interpretability | - | 6 |
| SAE-Res-Qwen3-8B-Base-W64K-L0_100 | 8.0 | Small (2-8B) | Dense | Interpretability | - | 6 |
| Qwen3-0.6B-MLX-8bit | 0.6 | Micro (<2B) | Dense | Text Generation | text-generation | 5 |
| Qwen3-4B-MLX-bf16 | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 5 |
| Qwen3-14B-MLX-8bit | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 5 |
| Qwen3-30B-A3B-MLX-6bit | 30.0 | Medium (8-35B) | MoE (A3B) | Text Generation | text-generation | 5 |
| SAE-Res-Qwen3.5-2B-Base-W32K-L0_100 | 2.0 | Small (2-8B) | Dense | Interpretability | - | 5 |
| Qwen3-1.7B-MLX-4bit | 1.7 | Micro (<2B) | Dense | Text Generation | text-generation | 4 |
| Qwen3-14B-MLX-6bit | 14.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 4 |
| Qwen3-4B-MLX-6bit | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 4 |
| Qwen3-32B-MLX-6bit | 32.0 | Medium (8-35B) | Dense | Text Generation | text-generation | 4 |
| Qwen3-235B-A22B-MLX-6bit | 235.0 | XLarge (>100B) | MoE (A22B) | Text Generation | text-generation | 4 |
| SAE-Res-Qwen3-1.7B-Base-W32K-L0_50 | 1.7 | Micro (<2B) | Dense | Interpretability | - | 4 |
| SAE-Res-Qwen3-30B-A3B-Base-W128K-L0_100 | 30.0 | Medium (8-35B) | MoE (A3B) | Interpretability | - | 4 |
| Qwen3-1.7B-MLX-6bit | 1.7 | Micro (<2B) | Dense | Text Generation | text-generation | 3 |
| Qwen3-1.7B-MLX-8bit | 1.7 | Micro (<2B) | Dense | Text Generation | text-generation | 3 |
| Qwen3-4B-MLX-8bit | 4.0 | Small (2-8B) | Dense | Text Generation | text-generation | 3 |
| SAE-Res-Qwen3-1.7B-Base-W32K-L0_100 | 1.7 | Micro (<2B) | Dense | Interpretability | - | 3 |
| SAE-Res-Qwen3-30B-A3B-Base-W32K-L0_50 | 30.0 | Medium (8-35B) | MoE (A3B) | Interpretability | - | 3 |
| Qwen3-VL-235B-A22B-Thinking-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Quantized, Vision-Language | image-text-to-text | 1 |

### Qwen3.5 (21 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3.5-9B | 9.0 | Medium (8-35B) | Dense | Vision-Language | image-text-to-text | 1658 |
| Qwen3.5-397B-A17B | 397.0 | XLarge (>100B) | MoE (A17B) | Vision-Language | image-text-to-text | 1526 |
| Qwen3.5-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | Vision-Language | image-text-to-text | 1455 |
| Qwen3.5-27B | 27.0 | Medium (8-35B) | Dense | Vision-Language | image-text-to-text | 996 |
| Qwen3.5-4B | 4.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 713 |
| Qwen3.5-0.8B | 0.8 | Micro (<2B) | Dense | Vision-Language | image-text-to-text | 605 |
| Qwen3.5-122B-A10B | 122.0 | XLarge (>100B) | MoE (A10B) | Vision-Language | image-text-to-text | 581 |
| Qwen3.5-2B | 2.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 323 |
| Qwen3.5-397B-A17B-FP8 | 397.0 | XLarge (>100B) | MoE (A17B) | Quantized, Vision-Language | image-text-to-text | 181 |
| Qwen3.5-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | Quantized, Vision-Language | image-text-to-text | 152 |
| Qwen3.5-27B-FP8 | 27.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 135 |
| Qwen3.5-35B-A3B-Base | 35.0 | Medium (8-35B) | MoE (A3B) | Vision-Language | image-text-to-text | 134 |
| Qwen3.5-122B-A10B-FP8 | 122.0 | XLarge (>100B) | MoE (A10B) | Quantized, Vision-Language | image-text-to-text | 107 |
| Qwen3.5-35B-A3B-GPTQ-Int4 | 35.0 | Medium (8-35B) | MoE (A3B) | Quantized, Vision-Language | image-text-to-text | 91 |
| Qwen3.5-9B-Base | 9.0 | Medium (8-35B) | Dense | Vision-Language | image-text-to-text | 89 |
| Qwen3.5-0.8B-Base | 0.8 | Micro (<2B) | Dense | Vision-Language | image-text-to-text | 83 |
| Qwen3.5-2B-Base | 2.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 78 |
| Qwen3.5-4B-Base | 4.0 | Small (2-8B) | Dense | Vision-Language | image-text-to-text | 72 |
| Qwen3.5-27B-GPTQ-Int4 | 27.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 57 |
| Qwen3.5-122B-A10B-GPTQ-Int4 | 122.0 | XLarge (>100B) | MoE (A10B) | Quantized, Vision-Language | image-text-to-text | 42 |
| Qwen3.5-397B-A17B-GPTQ-Int4 | 397.0 | XLarge (>100B) | MoE (A17B) | Quantized, Vision-Language | image-text-to-text | 35 |

### Qwen3.6 (4 models)

| Model | Size (B) | Tier | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | Vision-Language | image-text-to-text | 2319 |
| Qwen3.6-27B | 27.0 | Medium (8-35B) | Dense | Vision-Language | image-text-to-text | 1878 |
| Qwen3.6-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | Quantized, Vision-Language | image-text-to-text | 299 |
| Qwen3.6-27B-FP8 | 27.0 | Medium (8-35B) | Dense | Quantized, Vision-Language | image-text-to-text | 298 |

## Detailed Classification by Capability

### Text Generation (305 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| QwQ-32B | 32.0 | Medium (8-35B) | Dense | QwQ | text-generation | 2937 |
| Qwen2.5-Coder-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 2062 |
| QwQ-32B-Preview | 32.0 | Medium (8-35B) | Dense | QwQ | text-generation | 1740 |
| Qwen3-Coder-Next | - | Unknown | Dense | Qwen3 | text-generation | 1505 |
| Qwen2.5-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 1397 |
| Qwen3-0.6B | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 1383 |
| Qwen3-Coder-480B-A35B-Instruct | 480.0 | XLarge (>100B) | MoE (A35B) | Qwen3 | text-generation | 1347 |
| Qwen3-8B | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 1178 |
| Qwen3-Coder-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 1139 |
| Qwen3-235B-A22B | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 1100 |
| Qwen3-Next-80B-A3B-Instruct | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 1032 |
| Qwen2.5-72B-Instruct | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 962 |
| Qwen3-30B-A3B | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 905 |
| Qwen3-4B-Instruct-2507 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 892 |
| Qwen3-30B-A3B-Instruct-2507 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 819 |
| Qwen-7B-Chat | 7.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 789 |
| Qwen3-235B-A22B-Instruct-2507 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 786 |
| Qwen2.5-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 757 |
| Qwen2.5-Coder-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 745 |
| Qwen2-72B-Instruct | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 718 |
| Qwen3-32B | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 709 |
| Qwen2-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 686 |
| Qwen3-4B | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 645 |
| Qwen3-4B-Thinking-2507 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 600 |
| Qwen2.5-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 549 |
| Qwen-AgentWorld-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen-AgentWorld | text-generation | 530 |
| Qwen2.5-3B-Instruct | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 521 |
| Qwen3-1.7B | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 496 |
| Qwen3-Next-80B-A3B-Thinking | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 490 |
| Qwen2.5-0.5B | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 428 |
| Qwen3-14B | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 417 |
| Qwen3-235B-A22B-Thinking-2507 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 407 |
| Qwen-7B | 7.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 399 |
| Qwen-VL-Chat | - | Unknown | Dense | Qwen (original) | text-generation | 384 |
| Qwen3-30B-A3B-Thinking-2507 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 377 |
| Qwen-14B-Chat | 14.0 | Medium (8-35B) | Dense | Qwen (original) | text-generation | 373 |
| Qwen2.5-7B-Instruct-1M | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 371 |
| Qwen-72B | 72.0 | Large (35-100B) | Dense | Qwen (original) | text-generation | 360 |
| Qwen2.5-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 354 |
| CodeQwen1.5-7B-Chat | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 353 |
| Qwen2.5-14B-Instruct | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 351 |
| Qwen2.5-14B-Instruct-1M | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 341 |
| Qwen2.5-Coder-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 310 |
| Qwen2.5-7B | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 294 |
| Qwen-VL | - | Unknown | Dense | Qwen (original) | text-generation | 284 |
| Qwen3-Coder-Next-GGUF | - | Unknown | Dense | Qwen3 | text-generation | 260 |
| Qwen1.5-MoE-A2.7B | 2.7 | Small (2-8B) | MoE (A2.7B) | Qwen1.5 | text-generation | 227 |
| Qwen1.5-72B-Chat | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 217 |
| Qwen-14B | 14.0 | Medium (8-35B) | Dense | Qwen (original) | text-generation | 214 |
| Qwen3-8B-GGUF | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 212 |
| QwQ-32B-GGUF | 32.0 | Medium (8-35B) | Dense | QwQ | text-generation | 211 |
| Qwen2.5-Coder-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 209 |
| Qwen2-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 201 |
| Qwen2-72B | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 199 |
| Qwen2.5-3B | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 194 |
| Qwen2.5-1.5B | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 192 |
| Qwen3-Coder-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 187 |
| Qwen1.5-7B-Chat | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 186 |
| Qwen2-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 179 |
| Qwen2.5-32B | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 179 |
| Qwen1.5-0.5B | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 174 |
| Qwen3-0.6B-Base | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 174 |
| Qwen2-7B | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 171 |
| Qwen2.5-Coder-14B-Instruct | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 171 |
| Qwen2-0.5B | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 169 |
| Qwen2.5-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 164 |
| Qwen2-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 162 |
| Qwen2.5-Coder-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 161 |
| Qwen2.5-Coder-32B | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 157 |
| Qwen-72B-Chat | 72.0 | Large (35-100B) | Dense | Qwen (original) | text-generation | 156 |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | 480.0 | XLarge (>100B) | MoE (A35B) | Qwen3 | text-generation | 156 |
| Qwen3-Coder-Next-FP8 | - | Unknown | Dense | Qwen3 | text-generation | 156 |
| Qwen2.5-Coder-7B | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 155 |
| Qwen2.5-14B | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 154 |
| Qwen-Audio | - | Unknown | Dense | Qwen (original) | text-generation | 149 |
| Qwen3-235B-A22B-Instruct-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 148 |
| Qwen2.5-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 142 |
| Qwen3-32B-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 136 |
| Qwen1.5-MoE-A2.7B-Chat | 2.7 | Small (2-8B) | MoE (A2.7B) | Qwen1.5 | text-generation | 134 |
| QwQ-32B-AWQ | 32.0 | Medium (8-35B) | Dense | QwQ | text-generation | 134 |
| Qwen2.5-Coder-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 132 |
| Qwen1.5-110B-Chat | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 130 |
| Qwen3-30B-A3B-Instruct-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 130 |
| Qwen2.5-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 123 |
| Qwen3Guard-Gen-8B | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 119 |
| Qwen2.5-Math-7B | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 114 |
| Qwen2.5-Coder-3B-Instruct | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 114 |
| Qwen3-4B-GGUF | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 113 |
| Qwen1.5-14B-Chat | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 112 |
| CodeQwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 111 |
| Qwen2.5-Math-1.5B | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 110 |
| Qwen2.5-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 110 |
| Qwen3-8B-Base | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 110 |
| Qwen1.5-32B-Chat | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 109 |
| Qwen3-14B-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 109 |
| CodeQwen1.5-7B | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 104 |
| Qwen1.5-110B | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 104 |
| Qwen2-1.5B | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 102 |
| Qwen2.5-72B | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 101 |
| Qwen2.5-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 101 |
| Qwen-14B-Chat-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen (original) | text-generation | 100 |
| Qwen1.5-0.5B-Chat | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 98 |
| Qwen-Audio-Chat | - | Unknown | Dense | Qwen (original) | text-generation | 96 |
| Qwen-VL-Chat-Int4 | - | Unknown | Dense | Qwen (original) | text-generation | 95 |
| Qwen3-4B-Base | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 95 |
| Qwen2.5-Coder-1.5B | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 94 |
| Qwen2.5-Coder-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 93 |
| Qwen3-235B-A22B-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 93 |
| Qwen2.5-Math-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 91 |
| Qwen3-Next-80B-A3B-Instruct-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 90 |
| Qwen2-Math-72B-Instruct | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 89 |
| Qwen3-235B-A22B-Thinking-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 86 |
| Qwen1.5-32B | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 85 |
| Qwen3-32B-FP8 | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 84 |
| Qwen3-30B-A3B-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 84 |
| Qwen2-57B-A14B-Instruct | 57.0 | Large (35-100B) | MoE (A14B) | Qwen2 | text-generation | 83 |
| Qwen2.5-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 78 |
| Qwen3-4B-Instruct-2507-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 78 |
| Qwen2.5-Coder-14B | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 77 |
| Qwen-7B-Chat-Int4 | 7.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 75 |
| Qwen3-1.7B-Base | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 75 |
| Qwen3Guard-Gen-0.6B | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 75 |
| Qwen1.5-1.8B-Chat | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 74 |
| Qwen-1_8B | 8.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 73 |
| Qwen2-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 73 |
| Qwen3-30B-A3B-Base | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 73 |
| Qwen2.5-Coder-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 72 |
| Qwen3-30B-A3B-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 72 |
| Qwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 71 |
| Qwen3-14B-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 70 |
| Qwen3-Coder-Next-Base | - | Unknown | Dense | Qwen3 | text-generation | 70 |
| WebWorld-32B | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 70 |
| Qwen2.5-Coder-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 69 |
| Qwen3-32B-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 69 |
| Qwen1.5-14B-Chat-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 67 |
| Qwen3-30B-A3B-Thinking-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 67 |
| Qwen3-4B-Thinking-2507-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 66 |
| WebWorld-8B | 8.0 | Small (2-8B) | Dense | Other | text-generation | 64 |
| Qwen3-0.6B-GGUF | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 63 |
| Qwen1.5-72B-Chat-GGUF | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 62 |
| Qwen3-0.6B-FP8 | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 62 |
| Qwen3-8B-FP8 | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 62 |
| Qwen1.5-1.8B | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 59 |
| Qwen1.5-72B | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 59 |
| Qwen2.5-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 59 |
| Qwen2-57B-A14B | 57.0 | Large (35-100B) | MoE (A14B) | Qwen2 | text-generation | 58 |
| Qwen2.5-Math-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 58 |
| Qwen2.5-Coder-0.5B | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 57 |
| Qwen1.5-7B | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 56 |
| Qwen3-14B-Base | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 54 |
| Qwen3-Next-80B-A3B-Thinking-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 54 |
| Qwen2.5-Coder-3B | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 53 |
| Qwen3-30B-A3B-GPTQ-Int4 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 53 |
| Qwen1.5-32B-Chat-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 52 |
| Qwen3Guard-Gen-4B | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 52 |
| Qwen3-8B-AWQ | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 51 |
| Qwen1.5-MoE-A2.7B-Chat-GPTQ-Int4 | 2.7 | Small (2-8B) | MoE (A2.7B) | Qwen1.5 | text-generation | 50 |
| Qwen3-1.7B-GGUF | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 49 |
| Qwen3-14B-FP8 | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 48 |
| Qwen-72B-Chat-Int4 | 72.0 | Large (35-100B) | Dense | Qwen (original) | text-generation | 47 |
| Qwen2.5-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 47 |
| Qwen1.5-4B-Chat | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 46 |
| Qwen2.5-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 45 |
| Qwen2-Math-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 44 |
| Qwen2.5-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 44 |
| Qwen2.5-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 44 |
| Qwen3-4B-SafeRL | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 44 |
| Qwen1.5-14B | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 41 |
| Qwen2-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 41 |
| Qwen2.5-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 40 |
| Qwen3-4B-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 39 |
| Qwen1.5-72B-Chat-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 37 |
| Qwen2.5-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 37 |
| Qwen2.5-Coder-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 37 |
| Qwen-1_8B-Chat-Int4 | 8.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 36 |
| Qwen1.5-4B | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 36 |
| Qwen3-1.7B-FP8 | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 36 |
| Qwen1.5-0.5B-Chat-GGUF | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 35 |
| Qwen2-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 33 |
| Qwen2.5-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 33 |
| Qwen3-Next-80B-A3B-Instruct-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 32 |
| Qwen1.5-32B-Chat-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 31 |
| Qwen2-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 31 |
| Qwen2.5-Math-72B-Instruct | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 31 |
| Qwen3-4B-MLX-4bit | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 31 |
| Qwen3-Next-80B-A3B-Thinking-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 31 |
| Qwen2-Math-72B | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 30 |
| Qwen2-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 29 |
| Qwen3-4B-AWQ | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 29 |
| Qwen2-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 28 |
| Qwen2.5-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 28 |
| WebWorld-14B | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 28 |
| Qwen3-235B-A22B-GPTQ-Int4 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 27 |
| Qwen1.5-72B-Chat-AWQ | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 26 |
| Qwen1.5-7B-Chat-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 26 |
| Qwen2.5-Coder-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 26 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 24 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 24 |
| Qwen1.5-14B-Chat-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 23 |
| Qwen2-57B-A14B-Instruct-GPTQ-Int4 | 57.0 | Large (35-100B) | MoE (A14B) | Qwen2 | text-generation | 23 |
| Qwen2-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 23 |
| Qwen2.5-Coder-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 23 |
| Qwen3-0.6B-MLX-4bit | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 23 |
| Qwen1.5-1.8B-Chat-GGUF | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 21 |
| Qwen1.5-14B-Chat-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 21 |
| Qwen2-Math-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 21 |
| Qwen2.5-Coder-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 21 |
| Qwen1.5-7B-Chat-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 18 |
| Qwen1.5-32B-Chat-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 18 |
| Qwen1.5-110B-Chat-GPTQ-Int4 | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 18 |
| Qwen2.5-Math-72B | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 18 |
| Qwen2.5-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 18 |
| Qwen-72B-Chat-Int8 | 72.0 | Large (35-100B) | Dense | Qwen (original) | text-generation | 17 |
| Qwen2-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 17 |
| Qwen2-57B-A14B-Instruct-GGUF | 57.0 | Large (35-100B) | MoE (A14B) | Qwen2 | text-generation | 17 |
| Qwen1.5-4B-Chat-GGUF | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 16 |
| Qwen2.5-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 16 |
| Qwen3-235B-A22B-MLX-4bit | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 16 |
| Qwen2-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 15 |
| Qwen2-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 15 |
| Qwen1.5-0.5B-Chat-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 14 |
| CodeQwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 14 |
| Qwen1.5-110B-Chat-GGUF | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 14 |
| Qwen2-Math-7B | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 14 |
| Qwen2-Math-1.5B | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 14 |
| Qwen2.5-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 14 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 14 |
| Qwen3-14B-MLX-4bit | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 14 |
| Qwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 13 |
| Qwen1.5-14B-Chat-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 11 |
| Qwen2.5-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 11 |
| Qwen3-32B-MLX-8bit | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 11 |
| Qwen3-30B-A3B-MLX-4bit | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 11 |
| Qwen2-0.5B-Instruct-MLX | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 10 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 10 |
| Qwen3-235B-A22B-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 10 |
| Qwen3-8B-MLX-4bit | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 10 |
| Qwen-7B-Chat-Int8 | 7.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 9 |
| Qwen1.5-110B-Chat-AWQ | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 9 |
| Qwen2-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 9 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 9 |
| Qwen3-0.6B-GPTQ-Int8 | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 9 |
| Qwen3-8B-MLX-bf16 | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 9 |
| Qwen3-32B-MLX-bf16 | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 9 |
| Qwen3-30B-A3B-MLX-8bit | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 9 |
| Qwen3-235B-A22B-MLX-8bit | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 9 |
| Qwen2.5-Coder-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 8 |
| Qwen3-8B-MLX-8bit | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 8 |
| Qwen3-32B-MLX-4bit | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 8 |
| Qwen3-30B-A3B-MLX-bf16 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 8 |
| Qwen-14B-Chat-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen (original) | text-generation | 7 |
| Qwen1.5-0.5B-Chat-AWQ | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 7 |
| Qwen1.5-72B-Chat-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 7 |
| Qwen1.5-1.8B-Chat-GPTQ-Int4 | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 7 |
| Qwen2.5-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen2-7B-Instruct-MLX | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen3-1.7B-GPTQ-Int8 | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 7 |
| Qwen3-1.7B-MLX-bf16 | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 7 |
| Qwen1.5-4B-Chat-GPTQ-Int8 | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 6 |
| Qwen1.5-4B-Chat-GPTQ-Int4 | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 6 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 6 |
| Qwen3-0.6B-MLX-6bit | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 6 |
| Qwen3-0.6B-MLX-bf16 | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 6 |
| Qwen3-8B-MLX-6bit | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 6 |
| Qwen3-235B-A22B-MLX-bf16 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 6 |
| Qwen3-14B-MLX-bf16 | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 6 |
| Qwen-1_8B-Chat-Int8 | 8.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 5 |
| Qwen2-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 5 |
| Qwen2-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 5 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 5 |
| Qwen3-0.6B-MLX-8bit | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 5 |
| Qwen3-4B-MLX-bf16 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 5 |
| Qwen3-14B-MLX-8bit | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 5 |
| Qwen3-30B-A3B-MLX-6bit | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 5 |
| Qwen1.5-1.8B-Chat-AWQ | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 4 |
| Qwen1.5-0.5B-Chat-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 4 |
| Qwen2-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 4 |
| Qwen2-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 4 |
| Qwen2-1.5B-Instruct-MLX | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 4 |
| Qwen2.5-Coder-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 4 |
| Qwen3-1.7B-MLX-4bit | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 4 |
| Qwen3-14B-MLX-6bit | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 4 |
| Qwen3-4B-MLX-6bit | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 4 |
| Qwen3-32B-MLX-6bit | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 4 |
| Qwen3-235B-A22B-MLX-6bit | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 4 |
| Qwen1.5-4B-Chat-AWQ | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 3 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-Coder-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen3-1.7B-MLX-6bit | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 3 |
| Qwen3-1.7B-MLX-8bit | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 3 |
| Qwen3-4B-MLX-8bit | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 3 |
| Qwen1.5-1.8B-Chat-GPTQ-Int8 | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 2 |
| CodeQwen1.5-7B-AWQ | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 2 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 2 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 1 |

### Quantized (205 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-Embedding-0.6B-GGUF | 0.6 | Micro (<2B) | Dense | Qwen3 | - | 539 |
| Qwen2.5-Coder-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 310 |
| Qwen3.6-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.6 | image-text-to-text | 299 |
| Qwen3.6-27B-FP8 | 27.0 | Medium (8-35B) | Dense | Qwen3.6 | image-text-to-text | 298 |
| Qwen3-Coder-Next-GGUF | - | Unknown | Dense | Qwen3 | text-generation | 260 |
| Qwen3-8B-GGUF | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 212 |
| QwQ-32B-GGUF | 32.0 | Medium (8-35B) | Dense | QwQ | text-generation | 211 |
| Qwen2.5-Coder-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 209 |
| Qwen3-Coder-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 187 |
| Qwen3.5-397B-A17B-FP8 | 397.0 | XLarge (>100B) | MoE (A17B) | Qwen3.5 | image-text-to-text | 181 |
| Qwen2-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 179 |
| Qwen2.5-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 164 |
| Qwen2.5-Coder-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 161 |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | 480.0 | XLarge (>100B) | MoE (A35B) | Qwen3 | text-generation | 156 |
| Qwen3-Coder-Next-FP8 | - | Unknown | Dense | Qwen3 | text-generation | 156 |
| Qwen3.5-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.5 | image-text-to-text | 152 |
| Qwen3-235B-A22B-Instruct-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 148 |
| Qwen2.5-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 142 |
| Qwen3-32B-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 136 |
| Qwen3.5-27B-FP8 | 27.0 | Medium (8-35B) | Dense | Qwen3.5 | image-text-to-text | 135 |
| QwQ-32B-AWQ | 32.0 | Medium (8-35B) | Dense | QwQ | text-generation | 134 |
| Qwen3-30B-A3B-Instruct-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 130 |
| Qwen3-Embedding-8B-GGUF | 8.0 | Small (2-8B) | Dense | Qwen3 | - | 129 |
| Qwen2.5-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 123 |
| Qwen3-Embedding-4B-GGUF | 4.0 | Small (2-8B) | Dense | Qwen3 | - | 114 |
| Qwen3-4B-GGUF | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 113 |
| Qwen3-VL-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 113 |
| CodeQwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 111 |
| Qwen3-VL-8B-Instruct-GGUF | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 111 |
| Qwen2.5-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 110 |
| Qwen3-14B-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 109 |
| Qwen3.5-122B-A10B-FP8 | 122.0 | XLarge (>100B) | MoE (A10B) | Qwen3.5 | image-text-to-text | 107 |
| Qwen2.5-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | image-text-to-text | 106 |
| Qwen2.5-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 101 |
| Qwen-14B-Chat-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen (original) | text-generation | 100 |
| Qwen-VL-Chat-Int4 | - | Unknown | Dense | Qwen (original) | text-generation | 95 |
| Qwen2.5-Coder-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 93 |
| Qwen3-235B-A22B-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 93 |
| Qwen3.5-35B-A3B-GPTQ-Int4 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.5 | image-text-to-text | 91 |
| Qwen3-Next-80B-A3B-Instruct-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 90 |
| Qwen3-235B-A22B-Thinking-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 86 |
| Qwen3-32B-FP8 | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 84 |
| Qwen3-30B-A3B-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 84 |
| Qwen2.5-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 78 |
| Qwen3-4B-Instruct-2507-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 78 |
| Qwen-7B-Chat-Int4 | 7.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 75 |
| Qwen2-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 73 |
| Qwen2.5-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2.5 | image-text-to-text | 73 |
| Qwen3-VL-8B-Instruct-FP8 | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 73 |
| Qwen3-30B-A3B-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 72 |
| Qwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 71 |
| Qwen3-14B-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 70 |
| Qwen2.5-Coder-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 69 |
| Qwen3-32B-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 69 |
| Qwen1.5-14B-Chat-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 67 |
| Qwen3-30B-A3B-Thinking-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 67 |
| Qwen3-4B-Thinking-2507-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 66 |
| Qwen2.5-VL-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Qwen2.5 | image-text-to-text | 64 |
| Qwen2.5-VL-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | image-text-to-text | 63 |
| Qwen3-0.6B-GGUF | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 63 |
| Qwen3-VL-4B-Instruct-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 63 |
| Qwen1.5-72B-Chat-GGUF | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 62 |
| Qwen3-0.6B-FP8 | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 62 |
| Qwen3-8B-FP8 | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 62 |
| Qwen2.5-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 59 |
| Qwen3-VL-30B-A3B-Thinking-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 57 |
| Qwen3.5-27B-GPTQ-Int4 | 27.0 | Medium (8-35B) | Dense | Qwen3.5 | image-text-to-text | 57 |
| Qwen3-Next-80B-A3B-Thinking-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 54 |
| Qwen3-30B-A3B-GPTQ-Int4 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 53 |
| Qwen1.5-32B-Chat-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 52 |
| Qwen3-8B-AWQ | 8.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 51 |
| Qwen1.5-MoE-A2.7B-Chat-GPTQ-Int4 | 2.7 | Small (2-8B) | MoE (A2.7B) | Qwen1.5 | text-generation | 50 |
| Qwen2-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 50 |
| Qwen3-VL-2B-Instruct-GGUF | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 50 |
| Qwen2-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 49 |
| Qwen3-1.7B-GGUF | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 49 |
| Qwen3-VL-4B-Instruct-GGUF | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 49 |
| Qwen3-14B-FP8 | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 48 |
| Qwen-72B-Chat-Int4 | 72.0 | Large (35-100B) | Dense | Qwen (original) | text-generation | 47 |
| Qwen2.5-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 47 |
| Qwen3-VL-32B-Instruct-FP8 | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 46 |
| Qwen2.5-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 45 |
| Qwen2.5-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 44 |
| Qwen2.5-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 44 |
| Qwen3-VL-235B-A22B-Instruct-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 44 |
| Qwen3-VL-2B-Instruct-FP8 | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 42 |
| Qwen3.5-122B-A10B-GPTQ-Int4 | 122.0 | XLarge (>100B) | MoE (A10B) | Qwen3.5 | image-text-to-text | 42 |
| Qwen2-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 41 |
| Qwen2.5-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 40 |
| Qwen3-4B-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 39 |
| Qwen1.5-72B-Chat-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 37 |
| Qwen2-VL-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 37 |
| Qwen2.5-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 37 |
| Qwen2.5-Coder-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 37 |
| Qwen-1_8B-Chat-Int4 | 8.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 36 |
| Qwen3-1.7B-FP8 | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 36 |
| Qwen1.5-0.5B-Chat-GGUF | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 35 |
| Qwen3.5-397B-A17B-GPTQ-Int4 | 397.0 | XLarge (>100B) | MoE (A17B) | Qwen3.5 | image-text-to-text | 35 |
| Qwen2-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 33 |
| Qwen2.5-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 33 |
| Qwen3-VL-8B-Thinking-FP8 | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 32 |
| Qwen3-Next-80B-A3B-Instruct-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 32 |
| Qwen1.5-32B-Chat-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 31 |
| Qwen2-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 31 |
| Qwen2-VL-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 31 |
| Qwen3-VL-2B-Thinking-FP8 | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 31 |
| Qwen3-Next-80B-A3B-Thinking-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | Qwen3 | text-generation | 31 |
| Qwen2-VL-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 30 |
| Qwen3-VL-4B-Thinking-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 30 |
| Qwen2-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 29 |
| Qwen3-4B-AWQ | 4.0 | Small (2-8B) | Dense | Qwen3 | text-generation | 29 |
| Qwen3-VL-235B-A22B-Thinking-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 29 |
| Qwen2-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 28 |
| Qwen2-VL-2B-Instruct-GPTQ-Int4 | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 28 |
| Qwen2.5-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-generation | 28 |
| Qwen3-235B-A22B-GPTQ-Int4 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 27 |
| Qwen3-VL-8B-Thinking-GGUF | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 27 |
| Qwen1.5-72B-Chat-AWQ | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 26 |
| Qwen1.5-7B-Chat-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 26 |
| Qwen2.5-Coder-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 26 |
| Qwen3-VL-32B-Thinking-FP8 | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 26 |
| Qwen2-VL-2B-Instruct-AWQ | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 25 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 24 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 24 |
| Qwen1.5-14B-Chat-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 23 |
| Qwen2-57B-A14B-Instruct-GPTQ-Int4 | 57.0 | Large (35-100B) | MoE (A14B) | Qwen2 | text-generation | 23 |
| Qwen2-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 23 |
| Qwen2.5-Coder-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 23 |
| Qwen3-VL-2B-Thinking-GGUF | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 22 |
| Qwen1.5-1.8B-Chat-GGUF | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 21 |
| Qwen1.5-14B-Chat-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 21 |
| Qwen2.5-Coder-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 21 |
| Qwen3-VL-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 20 |
| Qwen1.5-7B-Chat-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 18 |
| Qwen1.5-32B-Chat-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 18 |
| Qwen1.5-110B-Chat-GPTQ-Int4 | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 18 |
| Qwen2.5-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 18 |
| Qwen2.5-Omni-7B-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | any-to-any | 18 |
| Qwen3-VL-4B-Thinking-GGUF | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 18 |
| Qwen-72B-Chat-Int8 | 72.0 | Large (35-100B) | Dense | Qwen (original) | text-generation | 17 |
| Qwen2-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2 | text-generation | 17 |
| Qwen2-57B-A14B-Instruct-GGUF | 57.0 | Large (35-100B) | MoE (A14B) | Qwen2 | text-generation | 17 |
| Qwen2-VL-2B-Instruct-GPTQ-Int8 | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 17 |
| Qwen3-VL-30B-A3B-Instruct-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 17 |
| Qwen1.5-4B-Chat-GGUF | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 16 |
| Qwen2.5-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 16 |
| Qwen2-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen2 | text-generation | 15 |
| Qwen2-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 15 |
| Qwen1.5-0.5B-Chat-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 14 |
| CodeQwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 14 |
| Qwen1.5-110B-Chat-GGUF | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 14 |
| Qwen2.5-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 14 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 14 |
| Qwen2.5-Omni-7B-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | any-to-any | 14 |
| Qwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 13 |
| Qwen3-VL-32B-Thinking-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 13 |
| Qwen3-VL-235B-A22B-Instruct-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 13 |
| Qwen1.5-14B-Chat-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen1.5 | text-generation | 11 |
| Qwen2-VL-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 11 |
| Qwen2.5-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 11 |
| Qwen3-VL-30B-A3B-Thinking-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 11 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 10 |
| Qwen3-235B-A22B-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | text-generation | 10 |
| Qwen-7B-Chat-Int8 | 7.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 9 |
| Qwen1.5-110B-Chat-AWQ | 110.0 | XLarge (>100B) | Dense | Qwen1.5 | text-generation | 9 |
| Qwen2-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 9 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 9 |
| Qwen3-0.6B-GPTQ-Int8 | 0.6 | Micro (<2B) | Dense | Qwen3 | text-generation | 9 |
| Qwen2.5-Coder-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 8 |
| Qwen-14B-Chat-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen (original) | text-generation | 7 |
| Qwen1.5-0.5B-Chat-AWQ | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 7 |
| Qwen1.5-72B-Chat-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen1.5 | text-generation | 7 |
| Qwen1.5-1.8B-Chat-GPTQ-Int4 | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 7 |
| Qwen2.5-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen3-1.7B-GPTQ-Int8 | 1.7 | Micro (<2B) | Dense | Qwen3 | text-generation | 7 |
| Qwen1.5-4B-Chat-GPTQ-Int8 | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 6 |
| Qwen1.5-4B-Chat-GPTQ-Int4 | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 6 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 6 |
| Qwen-1_8B-Chat-Int8 | 8.0 | Small (2-8B) | Dense | Qwen (original) | text-generation | 5 |
| Qwen2-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 5 |
| Qwen2-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 5 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 5 |
| Qwen1.5-1.8B-Chat-AWQ | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 4 |
| Qwen1.5-0.5B-Chat-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 4 |
| Qwen2-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 4 |
| Qwen2-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen2 | text-generation | 4 |
| Qwen2.5-Coder-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 4 |
| Qwen1.5-4B-Chat-AWQ | 4.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 3 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-Coder-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen1.5-1.8B-Chat-GPTQ-Int8 | 1.8 | Micro (<2B) | Dense | Qwen1.5 | text-generation | 2 |
| CodeQwen1.5-7B-AWQ | 7.0 | Small (2-8B) | Dense | Qwen1.5 | text-generation | 2 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 2 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen3-VL-235B-A22B-Thinking-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 1 |

### Vision-Language (86 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.6 | image-text-to-text | 2319 |
| Qwen3.6-27B | 27.0 | Medium (8-35B) | Dense | Qwen3.6 | image-text-to-text | 1878 |
| Qwen3.5-9B | 9.0 | Medium (8-35B) | Dense | Qwen3.5 | image-text-to-text | 1658 |
| Qwen2.5-VL-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2.5 | image-text-to-text | 1605 |
| Qwen3.5-397B-A17B | 397.0 | XLarge (>100B) | MoE (A17B) | Qwen3.5 | image-text-to-text | 1526 |
| Qwen3.5-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.5 | image-text-to-text | 1455 |
| Qwen2-VL-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 1281 |
| Qwen3.5-27B | 27.0 | Medium (8-35B) | Dense | Qwen3.5 | image-text-to-text | 996 |
| Qwen3-VL-8B-Instruct | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 978 |
| Qwen3.5-4B | 4.0 | Small (2-8B) | Dense | Qwen3.5 | image-text-to-text | 713 |
| Qwen2.5-VL-3B-Instruct | 3.0 | Small (2-8B) | Dense | Qwen2.5 | image-text-to-text | 670 |
| Qwen2.5-VL-72B-Instruct | 72.0 | Large (35-100B) | Dense | Qwen2.5 | image-text-to-text | 632 |
| QVQ-72B-Preview | 72.0 | Large (35-100B) | Dense | QVQ | image-text-to-text | 610 |
| Qwen3.5-0.8B | 0.8 | Micro (<2B) | Dense | Qwen3.5 | image-text-to-text | 605 |
| Qwen3-VL-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 582 |
| Qwen3.5-122B-A10B | 122.0 | XLarge (>100B) | MoE (A10B) | Qwen3.5 | image-text-to-text | 581 |
| Qwen2-VL-2B-Instruct | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 512 |
| Qwen2.5-VL-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | image-text-to-text | 494 |
| Qwen3-VL-2B-Instruct | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 436 |
| Qwen3-VL-4B-Instruct | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 404 |
| Qwen3-VL-235B-A22B-Instruct | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 400 |
| Qwen3-VL-235B-A22B-Thinking | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 399 |
| Qwen3.5-2B | 2.0 | Small (2-8B) | Dense | Qwen3.5 | image-text-to-text | 323 |
| Qwen2-VL-72B-Instruct | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 310 |
| Qwen3.6-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.6 | image-text-to-text | 299 |
| Qwen3.6-27B-FP8 | 27.0 | Medium (8-35B) | Dense | Qwen3.6 | image-text-to-text | 298 |
| Qwen3-VL-8B-Thinking | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 215 |
| Qwen3-VL-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 210 |
| Qwen3-VL-30B-A3B-Thinking | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 199 |
| Qwen3.5-397B-A17B-FP8 | 397.0 | XLarge (>100B) | MoE (A17B) | Qwen3.5 | image-text-to-text | 181 |
| Qwen3.5-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.5 | image-text-to-text | 152 |
| Qwen3.5-27B-FP8 | 27.0 | Medium (8-35B) | Dense | Qwen3.5 | image-text-to-text | 135 |
| Qwen3.5-35B-A3B-Base | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.5 | image-text-to-text | 134 |
| Qwen3-VL-2B-Thinking | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 115 |
| Qwen3-VL-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 113 |
| Qwen3-VL-4B-Thinking | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 113 |
| Qwen3-VL-8B-Instruct-GGUF | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 111 |
| Qwen3.5-122B-A10B-FP8 | 122.0 | XLarge (>100B) | MoE (A10B) | Qwen3.5 | image-text-to-text | 107 |
| Qwen2.5-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | image-text-to-text | 106 |
| Qwen3.5-35B-A3B-GPTQ-Int4 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3.5 | image-text-to-text | 91 |
| Qwen3.5-9B-Base | 9.0 | Medium (8-35B) | Dense | Qwen3.5 | image-text-to-text | 89 |
| Qwen3-VL-32B-Thinking | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 87 |
| Qwen3.5-0.8B-Base | 0.8 | Micro (<2B) | Dense | Qwen3.5 | image-text-to-text | 83 |
| Qwen2-VL-72B | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 80 |
| Qwen3.5-2B-Base | 2.0 | Small (2-8B) | Dense | Qwen3.5 | image-text-to-text | 78 |
| Qwen2.5-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2.5 | image-text-to-text | 73 |
| Qwen3-VL-8B-Instruct-FP8 | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 73 |
| Qwen-Image-Bench | - | Unknown | Dense | Qwen (original) | image-text-to-text | 73 |
| Qwen3.5-4B-Base | 4.0 | Small (2-8B) | Dense | Qwen3.5 | image-text-to-text | 72 |
| Qwen2-VL-7B | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 67 |
| Qwen2-VL-2B | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 65 |
| Qwen2.5-VL-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Qwen2.5 | image-text-to-text | 64 |
| Qwen2.5-VL-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | image-text-to-text | 63 |
| Qwen3-VL-4B-Instruct-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 63 |
| Qwen3-VL-30B-A3B-Thinking-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 57 |
| Qwen3.5-27B-GPTQ-Int4 | 27.0 | Medium (8-35B) | Dense | Qwen3.5 | image-text-to-text | 57 |
| Qwen2-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 50 |
| Qwen3-VL-2B-Instruct-GGUF | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 50 |
| Qwen2-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 49 |
| Qwen3-VL-4B-Instruct-GGUF | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 49 |
| Qwen3-VL-32B-Instruct-FP8 | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 46 |
| Qwen3-VL-235B-A22B-Instruct-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 44 |
| Qwen3-VL-2B-Instruct-FP8 | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 42 |
| Qwen3.5-122B-A10B-GPTQ-Int4 | 122.0 | XLarge (>100B) | MoE (A10B) | Qwen3.5 | image-text-to-text | 42 |
| Qwen2-VL-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 37 |
| Qwen3.5-397B-A17B-GPTQ-Int4 | 397.0 | XLarge (>100B) | MoE (A17B) | Qwen3.5 | image-text-to-text | 35 |
| Qwen3-VL-8B-Thinking-FP8 | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 32 |
| Qwen2-VL-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 31 |
| Qwen3-VL-2B-Thinking-FP8 | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 31 |
| Qwen2-VL-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 30 |
| Qwen3-VL-4B-Thinking-FP8 | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 30 |
| Qwen3-VL-235B-A22B-Thinking-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 29 |
| Qwen2-VL-2B-Instruct-GPTQ-Int4 | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 28 |
| Qwen3-VL-8B-Thinking-GGUF | 8.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 27 |
| Qwen3-VL-32B-Thinking-FP8 | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 26 |
| Qwen2-VL-2B-Instruct-AWQ | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 25 |
| Qwen3-VL-2B-Thinking-GGUF | 2.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 22 |
| Qwen3-VL-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 20 |
| Qwen3-VL-4B-Thinking-GGUF | 4.0 | Small (2-8B) | Dense | Qwen3 | image-text-to-text | 18 |
| Qwen2-VL-2B-Instruct-GPTQ-Int8 | 2.0 | Small (2-8B) | Dense | Qwen2 | image-text-to-text | 17 |
| Qwen3-VL-30B-A3B-Instruct-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 17 |
| Qwen3-VL-32B-Thinking-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen3 | image-text-to-text | 13 |
| Qwen3-VL-235B-A22B-Instruct-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 13 |
| Qwen2-VL-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | Qwen2 | image-text-to-text | 11 |
| Qwen3-VL-30B-A3B-Thinking-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | image-text-to-text | 11 |
| Qwen3-VL-235B-A22B-Thinking-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | Qwen3 | image-text-to-text | 1 |

### Code (44 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen2.5-Coder-32B-Instruct | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 2062 |
| Qwen3-Coder-Next | - | Unknown | Dense | Qwen3 | text-generation | 1505 |
| Qwen3-Coder-480B-A35B-Instruct | 480.0 | XLarge (>100B) | MoE (A35B) | Qwen3 | text-generation | 1347 |
| Qwen3-Coder-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 1139 |
| Qwen2.5-Coder-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 745 |
| Qwen2.5-Coder-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 310 |
| Qwen3-Coder-Next-GGUF | - | Unknown | Dense | Qwen3 | text-generation | 260 |
| Qwen2.5-Coder-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 209 |
| Qwen3-Coder-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | text-generation | 187 |
| Qwen2.5-Coder-14B-Instruct | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 171 |
| Qwen2.5-Coder-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 161 |
| Qwen2.5-Coder-32B | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 157 |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | 480.0 | XLarge (>100B) | MoE (A35B) | Qwen3 | text-generation | 156 |
| Qwen3-Coder-Next-FP8 | - | Unknown | Dense | Qwen3 | text-generation | 156 |
| Qwen2.5-Coder-7B | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 155 |
| Qwen2.5-Coder-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 132 |
| Qwen2.5-Coder-3B-Instruct | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 114 |
| Qwen2.5-Coder-1.5B | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 94 |
| Qwen2.5-Coder-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 93 |
| Qwen2.5-Coder-14B | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 77 |
| Qwen2.5-Coder-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 72 |
| Qwen3-Coder-Next-Base | - | Unknown | Dense | Qwen3 | text-generation | 70 |
| Qwen2.5-Coder-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 69 |
| Qwen2.5-Coder-0.5B | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 57 |
| Qwen2.5-Coder-3B | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 53 |
| Qwen2.5-Coder-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 37 |
| Qwen2.5-Coder-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 26 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 24 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 24 |
| Qwen2.5-Coder-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 23 |
| Qwen2.5-Coder-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 21 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 14 |
| Qwen2.5-Coder-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 8 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | Qwen2.5 | text-generation | 7 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 5 |
| Qwen2.5-Coder-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 4 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-Coder-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 2 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | Qwen2.5 | text-generation | 1 |

### Interpretability (14 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| SAE-Res-Qwen3.5-27B-W80K-L0_50 | 27.0 | Medium (8-35B) | Dense | Qwen3 | - | 38 |
| SAE-Res-Qwen3.5-2B-Base-W32K-L0_50 | 2.0 | Small (2-8B) | Dense | Qwen3 | - | 13 |
| SAE-Res-Qwen3.5-27B-W80K-L0_100 | 27.0 | Medium (8-35B) | Dense | Qwen3 | - | 13 |
| SAE-Res-Qwen3.5-9B-Base-W64K-L0_50 | 9.0 | Medium (8-35B) | Dense | Qwen3 | - | 10 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W128K-L0_100 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | - | 9 |
| SAE-Res-Qwen3.5-9B-Base-W64K-L0_100 | 9.0 | Medium (8-35B) | Dense | Qwen3 | - | 7 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W32K-L0_50 | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | - | 7 |
| SAE-Res-Qwen3-8B-Base-W64K-L0_50 | 8.0 | Small (2-8B) | Dense | Qwen3 | - | 6 |
| SAE-Res-Qwen3-8B-Base-W64K-L0_100 | 8.0 | Small (2-8B) | Dense | Qwen3 | - | 6 |
| SAE-Res-Qwen3.5-2B-Base-W32K-L0_100 | 2.0 | Small (2-8B) | Dense | Qwen3 | - | 5 |
| SAE-Res-Qwen3-1.7B-Base-W32K-L0_50 | 1.7 | Micro (<2B) | Dense | Qwen3 | - | 4 |
| SAE-Res-Qwen3-30B-A3B-Base-W128K-L0_100 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | - | 4 |
| SAE-Res-Qwen3-1.7B-Base-W32K-L0_100 | 1.7 | Micro (<2B) | Dense | Qwen3 | - | 3 |
| SAE-Res-Qwen3-30B-A3B-Base-W32K-L0_50 | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | - | 3 |

### Reward/Preference (9 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen2.5-Math-PRM-7B | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-classification | 90 |
| Qwen2.5-Math-RM-72B | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-classification | 83 |
| WorldPM-72B | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 82 |
| Qwen2.5-Math-PRM-72B | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-classification | 77 |
| Qwen2.5-Math-7B-PRM800K | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-classification | 21 |
| WorldPM-72B-HelpSteer2 | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 11 |
| WorldPM-72B-RLHFLow | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 11 |
| WorldPM-72B-UltraFeedback | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 8 |
| Qwen2-Math-RM-72B | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 7 |

### Text Classification (9 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen2.5-Math-PRM-7B | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-classification | 90 |
| Qwen2.5-Math-RM-72B | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-classification | 83 |
| WorldPM-72B | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 82 |
| Qwen2.5-Math-PRM-72B | 72.0 | Large (35-100B) | Dense | Qwen2.5 | text-classification | 77 |
| Qwen2.5-Math-7B-PRM800K | 7.0 | Small (2-8B) | Dense | Qwen2.5 | text-classification | 21 |
| WorldPM-72B-HelpSteer2 | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 11 |
| WorldPM-72B-RLHFLow | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 11 |
| WorldPM-72B-UltraFeedback | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 8 |
| Qwen2-Math-RM-72B | 72.0 | Large (35-100B) | Dense | Qwen2 | text-classification | 7 |

### Audio/Speech (8 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-ASR-1.7B | 1.7 | Micro (<2B) | Specialized (ASR) | Qwen3 | automatic-speech-recognition | 911 |
| Qwen2-Audio-7B-Instruct | 7.0 | Small (2-8B) | Dense | Qwen2 | audio-text-to-text | 544 |
| Qwen3-ASR-0.6B | 0.6 | Micro (<2B) | Specialized (ASR) | Qwen3 | automatic-speech-recognition | 310 |
| Qwen2-Audio-7B | 7.0 | Small (2-8B) | Dense | Qwen2 | audio-text-to-text | 172 |
| Qwen3-ForcedAligner-0.6B | 0.6 | Micro (<2B) | Specialized (ASR) | Qwen3 | automatic-speech-recognition | 145 |
| Qwen3-TTS-Tokenizer-12Hz | - | Unknown | Dense | Qwen3 | audio-to-audio | 70 |
| Qwen3-ASR-1.7B-hf | 1.7 | Micro (<2B) | Specialized (ASR) | Qwen3 | automatic-speech-recognition | 28 |
| Qwen3-ASR-0.6B-hf | 0.6 | Micro (<2B) | Specialized (ASR) | Qwen3 | automatic-speech-recognition | 19 |

### Omni/Multimodal (7 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen2.5-Omni-7B | 7.0 | Small (2-8B) | Dense | Qwen2.5 | any-to-any | 1913 |
| Qwen3-Omni-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | any-to-any | 954 |
| Qwen2.5-Omni-3B | 3.0 | Small (2-8B) | Dense | Qwen2.5 | any-to-any | 337 |
| Qwen3-Omni-30B-A3B-Thinking | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | any-to-any | 309 |
| Qwen3-Omni-30B-A3B-Captioner | 30.0 | Medium (8-35B) | MoE (A3B) | Qwen3 | any-to-any | 231 |
| Qwen2.5-Omni-7B-AWQ | 7.0 | Small (2-8B) | Dense | Qwen2.5 | any-to-any | 18 |
| Qwen2.5-Omni-7B-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | Qwen2.5 | any-to-any | 14 |

### Embeddings (7 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-Embedding-0.6B | 0.6 | Micro (<2B) | Dense | Qwen3 | feature-extraction | 1094 |
| Qwen3-Embedding-8B | 8.0 | Small (2-8B) | Dense | Qwen3 | feature-extraction | 732 |
| Qwen3-VL-Embedding-8B | 8.0 | Small (2-8B) | Dense | Qwen3 | sentence-similarity | 451 |
| Qwen3-VL-Embedding-2B | 2.0 | Small (2-8B) | Dense | Qwen3 | sentence-similarity | 427 |
| Qwen3-Embedding-4B | 4.0 | Small (2-8B) | Dense | Qwen3 | feature-extraction | 292 |
| Qwen3Guard-Stream-0.6B | 0.6 | Micro (<2B) | Dense | Qwen3 | feature-extraction | 32 |
| Qwen3Guard-Stream-4B | 4.0 | Small (2-8B) | Dense | Qwen3 | feature-extraction | 23 |

### Image Gen/Edit (6 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen-Image | - | Unknown | Diffusion | Qwen (original) | text-to-image | 2529 |
| Qwen-Image-Edit | - | Unknown | Diffusion | Qwen (original) | image-to-image | 2444 |
| Qwen-Image-Edit-2509 | - | Unknown | Diffusion | Qwen (original) | image-to-image | 1190 |
| Qwen-Image-Layered | - | Unknown | Dense | Qwen (original) | image-text-to-image | 1115 |
| Qwen-Image-Edit-2511 | - | Unknown | Diffusion | Qwen (original) | image-to-image | 1099 |
| Qwen-Image-2512 | - | Unknown | Diffusion | Qwen (original) | text-to-image | 897 |

### Audio/Speech (TTS) (5 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | 1.7 | Micro (<2B) | Specialized (TTS) | Qwen3 | text-to-speech | 1669 |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | 1.7 | Micro (<2B) | Specialized (TTS) | Qwen3 | text-to-speech | 366 |
| Qwen3-TTS-12Hz-0.6B-Base | 0.6 | Micro (<2B) | Specialized (TTS) | Qwen3 | text-to-speech | 259 |
| Qwen3-TTS-12Hz-0.6B-CustomVoice | 0.6 | Micro (<2B) | Specialized (TTS) | Qwen3 | text-to-speech | 164 |
| Qwen3-TTS-Tokenizer-12Hz | - | Unknown | Dense | Qwen3 | audio-to-audio | 70 |

### Reranking (5 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-Reranker-0.6B | 0.6 | Micro (<2B) | Dense | Qwen3 | text-ranking | 369 |
| Qwen3-Reranker-8B | 8.0 | Small (2-8B) | Dense | Qwen3 | text-ranking | 248 |
| Qwen3-VL-Reranker-2B | 2.0 | Small (2-8B) | Dense | Qwen3 | text-ranking | 201 |
| Qwen3-VL-Reranker-8B | 8.0 | Small (2-8B) | Dense | Qwen3 | text-ranking | 154 |
| Qwen3-Reranker-4B | 4.0 | Small (2-8B) | Dense | Qwen3 | text-ranking | 146 |

### Agent/Simulation (4 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen-AgentWorld-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | Qwen-AgentWorld | text-generation | 530 |
| WebWorld-32B | 32.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 70 |
| WebWorld-8B | 8.0 | Small (2-8B) | Dense | Other | text-generation | 64 |
| WebWorld-14B | 14.0 | Medium (8-35B) | Dense | Qwen3 | text-generation | 28 |

### Other/Unknown (3 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-TTS-12Hz-1.7B-Base | 1.7 | Micro (<2B) | Specialized (TTS) | Qwen3 | - | 434 |
| Qwen3Guard-Stream-8B | 8.0 | Small (2-8B) | Dense | Qwen3 | - | 38 |
| Qwen-tokenizer | - | Unknown | Dense | Qwen (original) | - | 20 |

### Token Classification (1 models)

| Model | Size (B) | Tier | Architecture | Family | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-ForcedAligner-0.6B-hf | 0.6 | Micro (<2B) | Specialized (ASR) | Qwen3 | token-classification | 11 |

## Architecture Deep Dive

### MoE Models — Active Parameter Configurations

| Model | Total Params (B) | Active Params | Architecture Tag | Likes |
| --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B | 35.0 | A3B | qwen3_5_moe | 2319 |
| Qwen3.5-397B-A17B | 397.0 | A17B | qwen3_5_moe | 1526 |
| Qwen3.5-35B-A3B | 35.0 | A3B | qwen3_5_moe | 1455 |
| Qwen3-Coder-480B-A35B-Instruct | 480.0 | A35B | qwen3_moe | 1347 |
| Qwen3-Coder-30B-A3B-Instruct | 30.0 | A3B | qwen3_moe | 1139 |
| Qwen3-235B-A22B | 235.0 | A22B | qwen3_moe | 1100 |
| Qwen3-Next-80B-A3B-Instruct | 80.0 | A3B | - | 1032 |
| Qwen3-Omni-30B-A3B-Instruct | 30.0 | A3B | qwen3_omni_moe | 954 |
| Qwen3-30B-A3B | 30.0 | A3B | - | 905 |
| Qwen3-30B-A3B-Instruct-2507 | 30.0 | A3B | qwen3_moe | 819 |
| Qwen3-235B-A22B-Instruct-2507 | 235.0 | A22B | qwen3_moe | 786 |
| Qwen3-VL-30B-A3B-Instruct | 30.0 | A3B | qwen3_vl_moe | 582 |
| Qwen3.5-122B-A10B | 122.0 | A10B | qwen3_5_moe | 581 |
| Qwen-AgentWorld-35B-A3B | 35.0 | A3B | qwen3_5_moe | 530 |
| Qwen3-Next-80B-A3B-Thinking | 80.0 | A3B | - | 490 |
| Qwen3-235B-A22B-Thinking-2507 | 235.0 | A22B | qwen3_moe | 407 |
| Qwen3-VL-235B-A22B-Instruct | 235.0 | A22B | qwen3_vl_moe | 400 |
| Qwen3-VL-235B-A22B-Thinking | 235.0 | A22B | qwen3_vl_moe | 399 |
| Qwen3-30B-A3B-Thinking-2507 | 30.0 | A3B | qwen3_moe | 377 |
| Qwen3-Omni-30B-A3B-Thinking | 30.0 | A3B | qwen3_omni_moe | 309 |
| Qwen3.6-35B-A3B-FP8 | 35.0 | A3B | qwen3_5_moe | 299 |
| Qwen3-Omni-30B-A3B-Captioner | 30.0 | A3B | qwen3_omni_moe | 231 |
| Qwen1.5-MoE-A2.7B | 2.7 | A2.7B | qwen2_moe | 227 |
| Qwen3-VL-30B-A3B-Thinking | 30.0 | A3B | qwen3_vl_moe | 199 |
| Qwen3-Coder-30B-A3B-Instruct-FP8 | 30.0 | A3B | qwen3_moe | 187 |
| Qwen3.5-397B-A17B-FP8 | 397.0 | A17B | qwen3_5_moe | 181 |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | 480.0 | A35B | qwen3_moe | 156 |
| Qwen3.5-35B-A3B-FP8 | 35.0 | A3B | qwen3_5_moe | 152 |
| Qwen3-235B-A22B-Instruct-2507-FP8 | 235.0 | A22B | qwen3_moe | 148 |
| Qwen1.5-MoE-A2.7B-Chat | 2.7 | A2.7B | qwen2_moe | 134 |
| Qwen3.5-35B-A3B-Base | 35.0 | A3B | qwen3_5_moe | 134 |
| Qwen3-30B-A3B-Instruct-2507-FP8 | 30.0 | A3B | qwen3_moe | 130 |
| Qwen3-VL-30B-A3B-Instruct-FP8 | 30.0 | A3B | qwen3_vl_moe | 113 |
| Qwen3.5-122B-A10B-FP8 | 122.0 | A10B | qwen3_5_moe | 107 |
| Qwen3-235B-A22B-FP8 | 235.0 | A22B | qwen3_moe | 93 |
| Qwen3.5-35B-A3B-GPTQ-Int4 | 35.0 | A3B | qwen3_5_moe | 91 |
| Qwen3-Next-80B-A3B-Instruct-FP8 | 80.0 | A3B | - | 90 |
| Qwen3-235B-A22B-Thinking-2507-FP8 | 235.0 | A22B | qwen3_moe | 86 |
| Qwen3-30B-A3B-FP8 | 30.0 | A3B | - | 84 |
| Qwen2-57B-A14B-Instruct | 57.0 | A14B | qwen2_moe | 83 |
| Qwen3-30B-A3B-Base | 30.0 | A3B | qwen3_moe | 73 |
| Qwen3-30B-A3B-GGUF | 30.0 | A3B | - | 72 |
| Qwen3-30B-A3B-Thinking-2507-FP8 | 30.0 | A3B | qwen3_moe | 67 |
| Qwen2-57B-A14B | 57.0 | A14B | qwen2_moe | 58 |
| Qwen3-VL-30B-A3B-Thinking-FP8 | 30.0 | A3B | qwen3_vl_moe | 57 |
| Qwen3-Next-80B-A3B-Thinking-FP8 | 80.0 | A3B | - | 54 |
| Qwen3-30B-A3B-GPTQ-Int4 | 30.0 | A3B | qwen3_moe | 53 |
| Qwen1.5-MoE-A2.7B-Chat-GPTQ-Int4 | 2.7 | A2.7B | qwen2_moe | 50 |
| Qwen3-VL-235B-A22B-Instruct-FP8 | 235.0 | A22B | qwen3_vl_moe | 44 |
| Qwen3.5-122B-A10B-GPTQ-Int4 | 122.0 | A10B | qwen3_5_moe | 42 |
| Qwen3.5-397B-A17B-GPTQ-Int4 | 397.0 | A17B | qwen3_5_moe | 35 |
| Qwen3-Next-80B-A3B-Instruct-GGUF | 80.0 | A3B | - | 32 |
| Qwen3-Next-80B-A3B-Thinking-GGUF | 80.0 | A3B | - | 31 |
| Qwen3-VL-235B-A22B-Thinking-FP8 | 235.0 | A22B | qwen3_vl_moe | 29 |
| Qwen3-235B-A22B-GPTQ-Int4 | 235.0 | A22B | qwen3_moe | 27 |
| Qwen2-57B-A14B-Instruct-GPTQ-Int4 | 57.0 | A14B | qwen2_moe | 23 |
| Qwen2-57B-A14B-Instruct-GGUF | 57.0 | A14B | - | 17 |
| Qwen3-VL-30B-A3B-Instruct-GGUF | 30.0 | A3B | - | 17 |
| Qwen3-235B-A22B-MLX-4bit | 235.0 | A22B | qwen3_moe | 16 |
| Qwen3-VL-235B-A22B-Instruct-GGUF | 235.0 | A22B | - | 13 |
| Qwen3-30B-A3B-MLX-4bit | 30.0 | A3B | qwen3_moe | 11 |
| Qwen3-VL-30B-A3B-Thinking-GGUF | 30.0 | A3B | - | 11 |
| Qwen3-235B-A22B-GGUF | 235.0 | A22B | - | 10 |
| Qwen3-30B-A3B-MLX-8bit | 30.0 | A3B | qwen3_moe | 9 |
| Qwen3-235B-A22B-MLX-8bit | 235.0 | A22B | qwen3_moe | 9 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W128K-L0_100 | 35.0 | A3B | - | 9 |
| Qwen3-30B-A3B-MLX-bf16 | 30.0 | A3B | qwen3_moe | 8 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W32K-L0_50 | 35.0 | A3B | - | 7 |
| Qwen3-235B-A22B-MLX-bf16 | 235.0 | A22B | qwen3_moe | 6 |
| Qwen3-30B-A3B-MLX-6bit | 30.0 | A3B | qwen3_moe | 5 |
| Qwen3-235B-A22B-MLX-6bit | 235.0 | A22B | qwen3_moe | 4 |
| SAE-Res-Qwen3-30B-A3B-Base-W128K-L0_100 | 30.0 | A3B | - | 4 |
| SAE-Res-Qwen3-30B-A3B-Base-W32K-L0_50 | 30.0 | A3B | - | 3 |
| Qwen3-VL-235B-A22B-Thinking-GGUF | 235.0 | A22B | - | 1 |

### Dense Models by Size (Top 50)

| Model | Size (B) | Family | Capabilities | Likes |
| --- | --- | --- | --- | --- |
| Qwen1.5-110B-Chat | 110.0 | Qwen1.5 | Text Generation | 130 |
| Qwen1.5-110B | 110.0 | Qwen1.5 | Text Generation | 104 |
| Qwen1.5-110B-Chat-GPTQ-Int4 | 110.0 | Qwen1.5 | Quantized, Text Generation | 18 |
| Qwen1.5-110B-Chat-GGUF | 110.0 | Qwen1.5 | Quantized, Text Generation | 14 |
| Qwen1.5-110B-Chat-AWQ | 110.0 | Qwen1.5 | Quantized, Text Generation | 9 |
| Qwen2.5-72B-Instruct | 72.0 | Qwen2.5 | Text Generation | 962 |
| Qwen2-72B-Instruct | 72.0 | Qwen2 | Text Generation | 718 |
| Qwen2.5-VL-72B-Instruct | 72.0 | Qwen2.5 | Vision-Language | 632 |
| QVQ-72B-Preview | 72.0 | QVQ | Vision-Language | 610 |
| Qwen-72B | 72.0 | Qwen (original) | Text Generation | 360 |
| Qwen2-VL-72B-Instruct | 72.0 | Qwen2 | Vision-Language | 310 |
| Qwen1.5-72B-Chat | 72.0 | Qwen1.5 | Text Generation | 217 |
| Qwen2-72B | 72.0 | Qwen2 | Text Generation | 199 |
| Qwen-72B-Chat | 72.0 | Qwen (original) | Text Generation | 156 |
| Qwen2.5-72B | 72.0 | Qwen2.5 | Text Generation | 101 |
| Qwen2-Math-72B-Instruct | 72.0 | Qwen2 | Text Generation | 89 |
| Qwen2.5-Math-RM-72B | 72.0 | Qwen2.5 | Reward/Preference, Text Classification | 83 |
| WorldPM-72B | 72.0 | Qwen2 | Reward/Preference, Text Classification | 82 |
| Qwen2-VL-72B | 72.0 | Qwen2 | Vision-Language | 80 |
| Qwen2.5-72B-Instruct-AWQ | 72.0 | Qwen2.5 | Quantized, Text Generation | 78 |
| Qwen2.5-Math-PRM-72B | 72.0 | Qwen2.5 | Reward/Preference, Text Classification | 77 |
| Qwen2.5-VL-72B-Instruct-AWQ | 72.0 | Qwen2.5 | Quantized, Vision-Language | 73 |
| Qwen1.5-72B-Chat-GGUF | 72.0 | Qwen1.5 | Quantized, Text Generation | 62 |
| Qwen1.5-72B | 72.0 | Qwen1.5 | Text Generation | 59 |
| Qwen2-VL-72B-Instruct-AWQ | 72.0 | Qwen2 | Quantized, Vision-Language | 50 |
| Qwen-72B-Chat-Int4 | 72.0 | Qwen (original) | Quantized, Text Generation | 47 |
| Qwen2.5-72B-Instruct-GPTQ-Int4 | 72.0 | Qwen2.5 | Quantized, Text Generation | 44 |
| Qwen2.5-72B-Instruct-GGUF | 72.0 | Qwen2.5 | Quantized, Text Generation | 44 |
| Qwen2-72B-Instruct-AWQ | 72.0 | Qwen2 | Quantized, Text Generation | 41 |
| Qwen1.5-72B-Chat-GPTQ-Int4 | 72.0 | Qwen1.5 | Quantized, Text Generation | 37 |
| Qwen2-72B-Instruct-GPTQ-Int4 | 72.0 | Qwen2 | Quantized, Text Generation | 33 |
| Qwen2-72B-Instruct-GGUF | 72.0 | Qwen2 | Quantized, Text Generation | 31 |
| Qwen2.5-Math-72B-Instruct | 72.0 | Qwen2.5 | Text Generation | 31 |
| Qwen2-Math-72B | 72.0 | Qwen2 | Text Generation | 30 |
| Qwen2-VL-72B-Instruct-GPTQ-Int4 | 72.0 | Qwen2 | Quantized, Vision-Language | 30 |
| Qwen2.5-72B-Instruct-GPTQ-Int8 | 72.0 | Qwen2.5 | Quantized, Text Generation | 28 |
| Qwen1.5-72B-Chat-AWQ | 72.0 | Qwen1.5 | Quantized, Text Generation | 26 |
| Qwen2.5-Math-72B | 72.0 | Qwen2.5 | Text Generation | 18 |
| Qwen-72B-Chat-Int8 | 72.0 | Qwen (original) | Quantized, Text Generation | 17 |
| Qwen2-72B-Instruct-GPTQ-Int8 | 72.0 | Qwen2 | Quantized, Text Generation | 15 |
| Qwen2-VL-72B-Instruct-GPTQ-Int8 | 72.0 | Qwen2 | Quantized, Vision-Language | 11 |
| WorldPM-72B-HelpSteer2 | 72.0 | Qwen2 | Reward/Preference, Text Classification | 11 |
| WorldPM-72B-RLHFLow | 72.0 | Qwen2 | Reward/Preference, Text Classification | 11 |
| WorldPM-72B-UltraFeedback | 72.0 | Qwen2 | Reward/Preference, Text Classification | 8 |
| Qwen1.5-72B-Chat-GPTQ-Int8 | 72.0 | Qwen1.5 | Quantized, Text Generation | 7 |
| Qwen2-Math-RM-72B | 72.0 | Qwen2 | Reward/Preference, Text Classification | 7 |
| QwQ-32B | 32.0 | QwQ | Text Generation | 2937 |
| Qwen2.5-Coder-32B-Instruct | 32.0 | Qwen2.5 | Code, Text Generation | 2062 |
| QwQ-32B-Preview | 32.0 | QwQ | Text Generation | 1740 |
| Qwen3-32B | 32.0 | Qwen3 | Text Generation | 709 |
*... and 305 more dense models (see family tables above)*

### Specialized Architecture Models

| Model | Architecture | Pipeline | Family | Likes |
| --- | --- | --- | --- | --- |
| Qwen-Image | Diffusion | text-to-image | Qwen (original) | 2529 |
| Qwen-Image-Edit | Diffusion | image-to-image | Qwen (original) | 2444 |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | Specialized (TTS) | text-to-speech | Qwen3 | 1669 |
| Qwen-Image-Edit-2509 | Diffusion | image-to-image | Qwen (original) | 1190 |
| Qwen-Image-Edit-2511 | Diffusion | image-to-image | Qwen (original) | 1099 |
| Qwen3-ASR-1.7B | Specialized (ASR) | automatic-speech-recognition | Qwen3 | 911 |
| Qwen-Image-2512 | Diffusion | text-to-image | Qwen (original) | 897 |
| Qwen3-TTS-12Hz-1.7B-Base | Specialized (TTS) | - | Qwen3 | 434 |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | Specialized (TTS) | text-to-speech | Qwen3 | 366 |
| Qwen3-ASR-0.6B | Specialized (ASR) | automatic-speech-recognition | Qwen3 | 310 |
| Qwen3-TTS-12Hz-0.6B-Base | Specialized (TTS) | text-to-speech | Qwen3 | 259 |
| Qwen3-TTS-12Hz-0.6B-CustomVoice | Specialized (TTS) | text-to-speech | Qwen3 | 164 |
| Qwen3-ForcedAligner-0.6B | Specialized (ASR) | automatic-speech-recognition | Qwen3 | 145 |
| Qwen3-ASR-1.7B-hf | Specialized (ASR) | automatic-speech-recognition | Qwen3 | 28 |
| Qwen3-ASR-0.6B-hf | Specialized (ASR) | automatic-speech-recognition | Qwen3 | 19 |
| Qwen3-ForcedAligner-0.6B-hf | Specialized (ASR) | token-classification | Qwen3 | 11 |

## Quantized Model Variants

### AWQ (40 models)

| Model | Size (B) | Family | Likes |
| --- | --- | --- | --- |
| Qwen3-32B-AWQ | 32.0 | Qwen3 | 136 |
| QwQ-32B-AWQ | 32.0 | QwQ | 134 |
| Qwen2.5-VL-7B-Instruct-AWQ | 7.0 | Qwen2.5 | 106 |
| Qwen2.5-32B-Instruct-AWQ | 32.0 | Qwen2.5 | 101 |
| Qwen2.5-72B-Instruct-AWQ | 72.0 | Qwen2.5 | 78 |
| Qwen2.5-VL-72B-Instruct-AWQ | 72.0 | Qwen2.5 | 73 |
| Qwen3-14B-AWQ | 14.0 | Qwen3 | 70 |
| Qwen2.5-VL-3B-Instruct-AWQ | 3.0 | Qwen2.5 | 64 |
| Qwen2.5-VL-32B-Instruct-AWQ | 32.0 | Qwen2.5 | 63 |
| Qwen3-8B-AWQ | 8.0 | Qwen3 | 51 |
| Qwen2-VL-72B-Instruct-AWQ | 72.0 | Qwen2 | 50 |
| Qwen2-VL-7B-Instruct-AWQ | 7.0 | Qwen2 | 49 |
| Qwen2.5-7B-Instruct-AWQ | 7.0 | Qwen2.5 | 47 |
| Qwen2-72B-Instruct-AWQ | 72.0 | Qwen2 | 41 |
| Qwen2.5-14B-Instruct-AWQ | 14.0 | Qwen2.5 | 37 |
| Qwen2.5-Coder-32B-Instruct-AWQ | 32.0 | Qwen2.5 | 37 |
| Qwen3-4B-AWQ | 4.0 | Qwen3 | 29 |
| Qwen1.5-72B-Chat-AWQ | 72.0 | Qwen1.5 | 26 |
| Qwen2.5-Coder-7B-Instruct-AWQ | 7.0 | Qwen2.5 | 26 |
| Qwen2-VL-2B-Instruct-AWQ | 2.0 | Qwen2 | 25 |
| Qwen1.5-14B-Chat-AWQ | 14.0 | Qwen1.5 | 23 |
| Qwen2-7B-Instruct-AWQ | 7.0 | Qwen2 | 23 |
| Qwen2.5-Coder-14B-Instruct-AWQ | 14.0 | Qwen2.5 | 21 |
| Qwen1.5-32B-Chat-AWQ | 32.0 | Qwen1.5 | 18 |
| Qwen2.5-Omni-7B-AWQ | 7.0 | Qwen2.5 | 18 |
| Qwen2.5-3B-Instruct-AWQ | 3.0 | Qwen2.5 | 16 |
| CodeQwen1.5-7B-Chat-AWQ | 7.0 | Qwen1.5 | 14 |
| Qwen1.5-7B-Chat-AWQ | 7.0 | Qwen1.5 | 13 |
| Qwen2.5-0.5B-Instruct-AWQ | 0.5 | Qwen2.5 | 11 |
| Qwen1.5-110B-Chat-AWQ | 110.0 | Qwen1.5 | 9 |
| Qwen2-1.5B-Instruct-AWQ | 1.5 | Qwen2 | 9 |
| Qwen2.5-Coder-3B-Instruct-AWQ | 3.0 | Qwen2.5 | 8 |
| Qwen1.5-0.5B-Chat-AWQ | 0.5 | Qwen1.5 | 7 |
| Qwen2.5-1.5B-Instruct-AWQ | 1.5 | Qwen2.5 | 7 |
| Qwen2-0.5B-Instruct-AWQ | 0.5 | Qwen2 | 5 |
| Qwen1.5-1.8B-Chat-AWQ | 1.8 | Qwen1.5 | 4 |
| Qwen2.5-Coder-1.5B-Instruct-AWQ | 1.5 | Qwen2.5 | 4 |
| Qwen1.5-4B-Chat-AWQ | 4.0 | Qwen1.5 | 3 |
| Qwen2.5-Coder-0.5B-Instruct-AWQ | 0.5 | Qwen2.5 | 3 |
| CodeQwen1.5-7B-AWQ | 7.0 | Qwen1.5 | 2 |

### FP8 (37 models)

| Model | Size (B) | Family | Likes |
| --- | --- | --- | --- |
| Qwen3.6-35B-A3B-FP8 | 35.0 | Qwen3.6 | 299 |
| Qwen3.6-27B-FP8 | 27.0 | Qwen3.6 | 298 |
| Qwen3-Coder-30B-A3B-Instruct-FP8 | 30.0 | Qwen3 | 187 |
| Qwen3.5-397B-A17B-FP8 | 397.0 | Qwen3.5 | 181 |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | 480.0 | Qwen3 | 156 |
| Qwen3-Coder-Next-FP8 | - | Qwen3 | 156 |
| Qwen3.5-35B-A3B-FP8 | 35.0 | Qwen3.5 | 152 |
| Qwen3-235B-A22B-Instruct-2507-FP8 | 235.0 | Qwen3 | 148 |
| Qwen3.5-27B-FP8 | 27.0 | Qwen3.5 | 135 |
| Qwen3-30B-A3B-Instruct-2507-FP8 | 30.0 | Qwen3 | 130 |
| Qwen3-VL-30B-A3B-Instruct-FP8 | 30.0 | Qwen3 | 113 |
| Qwen3.5-122B-A10B-FP8 | 122.0 | Qwen3.5 | 107 |
| Qwen3-235B-A22B-FP8 | 235.0 | Qwen3 | 93 |
| Qwen3-Next-80B-A3B-Instruct-FP8 | 80.0 | Qwen3 | 90 |
| Qwen3-235B-A22B-Thinking-2507-FP8 | 235.0 | Qwen3 | 86 |
| Qwen3-32B-FP8 | 32.0 | Qwen3 | 84 |
| Qwen3-30B-A3B-FP8 | 30.0 | Qwen3 | 84 |
| Qwen3-4B-Instruct-2507-FP8 | 4.0 | Qwen3 | 78 |
| Qwen3-VL-8B-Instruct-FP8 | 8.0 | Qwen3 | 73 |
| Qwen3-30B-A3B-Thinking-2507-FP8 | 30.0 | Qwen3 | 67 |
| Qwen3-4B-Thinking-2507-FP8 | 4.0 | Qwen3 | 66 |
| Qwen3-VL-4B-Instruct-FP8 | 4.0 | Qwen3 | 63 |
| Qwen3-0.6B-FP8 | 0.6 | Qwen3 | 62 |
| Qwen3-8B-FP8 | 8.0 | Qwen3 | 62 |
| Qwen3-VL-30B-A3B-Thinking-FP8 | 30.0 | Qwen3 | 57 |
| Qwen3-Next-80B-A3B-Thinking-FP8 | 80.0 | Qwen3 | 54 |
| Qwen3-14B-FP8 | 14.0 | Qwen3 | 48 |
| Qwen3-VL-32B-Instruct-FP8 | 32.0 | Qwen3 | 46 |
| Qwen3-VL-235B-A22B-Instruct-FP8 | 235.0 | Qwen3 | 44 |
| Qwen3-VL-2B-Instruct-FP8 | 2.0 | Qwen3 | 42 |
| Qwen3-4B-FP8 | 4.0 | Qwen3 | 39 |
| Qwen3-1.7B-FP8 | 1.7 | Qwen3 | 36 |
| Qwen3-VL-8B-Thinking-FP8 | 8.0 | Qwen3 | 32 |
| Qwen3-VL-2B-Thinking-FP8 | 2.0 | Qwen3 | 31 |
| Qwen3-VL-4B-Thinking-FP8 | 4.0 | Qwen3 | 30 |
| Qwen3-VL-235B-A22B-Thinking-FP8 | 235.0 | Qwen3 | 29 |
| Qwen3-VL-32B-Thinking-FP8 | 32.0 | Qwen3 | 26 |

### GGUF (54 models)

| Model | Size (B) | Family | Likes |
| --- | --- | --- | --- |
| Qwen3-Embedding-0.6B-GGUF | 0.6 | Qwen3 | 539 |
| Qwen2.5-Coder-7B-Instruct-GGUF | 7.0 | Qwen2.5 | 310 |
| Qwen3-Coder-Next-GGUF | - | Qwen3 | 260 |
| Qwen3-8B-GGUF | 8.0 | Qwen3 | 212 |
| QwQ-32B-GGUF | 32.0 | QwQ | 211 |
| Qwen2.5-Coder-32B-Instruct-GGUF | 32.0 | Qwen2.5 | 209 |
| Qwen2-7B-Instruct-GGUF | 7.0 | Qwen2 | 179 |
| Qwen2.5-7B-Instruct-GGUF | 7.0 | Qwen2.5 | 164 |
| Qwen2.5-Coder-14B-Instruct-GGUF | 14.0 | Qwen2.5 | 161 |
| Qwen2.5-3B-Instruct-GGUF | 3.0 | Qwen2.5 | 142 |
| Qwen3-Embedding-8B-GGUF | 8.0 | Qwen3 | 129 |
| Qwen2.5-1.5B-Instruct-GGUF | 1.5 | Qwen2.5 | 123 |
| Qwen3-Embedding-4B-GGUF | 4.0 | Qwen3 | 114 |
| Qwen3-4B-GGUF | 4.0 | Qwen3 | 113 |
| CodeQwen1.5-7B-Chat-GGUF | 7.0 | Qwen1.5 | 111 |
| Qwen3-VL-8B-Instruct-GGUF | 8.0 | Qwen3 | 111 |
| Qwen2.5-0.5B-Instruct-GGUF | 0.5 | Qwen2.5 | 110 |
| Qwen3-14B-GGUF | 14.0 | Qwen3 | 109 |
| Qwen2.5-Coder-3B-Instruct-GGUF | 3.0 | Qwen2.5 | 93 |
| Qwen2-0.5B-Instruct-GGUF | 0.5 | Qwen2 | 73 |
| Qwen3-30B-A3B-GGUF | 30.0 | Qwen3 | 72 |
| Qwen1.5-7B-Chat-GGUF | 7.0 | Qwen1.5 | 71 |
| Qwen2.5-Coder-1.5B-Instruct-GGUF | 1.5 | Qwen2.5 | 69 |
| Qwen3-32B-GGUF | 32.0 | Qwen3 | 69 |
| Qwen1.5-14B-Chat-GGUF | 14.0 | Qwen1.5 | 67 |
| Qwen3-0.6B-GGUF | 0.6 | Qwen3 | 63 |
| Qwen1.5-72B-Chat-GGUF | 72.0 | Qwen1.5 | 62 |
| Qwen2.5-14B-Instruct-GGUF | 14.0 | Qwen2.5 | 59 |
| Qwen1.5-32B-Chat-GGUF | 32.0 | Qwen1.5 | 52 |
| Qwen3-VL-2B-Instruct-GGUF | 2.0 | Qwen3 | 50 |
| Qwen3-1.7B-GGUF | 1.7 | Qwen3 | 49 |
| Qwen3-VL-4B-Instruct-GGUF | 4.0 | Qwen3 | 49 |
| Qwen2.5-32B-Instruct-GGUF | 32.0 | Qwen2.5 | 45 |
| Qwen2.5-72B-Instruct-GGUF | 72.0 | Qwen2.5 | 44 |
| Qwen1.5-0.5B-Chat-GGUF | 0.5 | Qwen1.5 | 35 |
| Qwen3-Next-80B-A3B-Instruct-GGUF | 80.0 | Qwen3 | 32 |
| Qwen2-72B-Instruct-GGUF | 72.0 | Qwen2 | 31 |
| Qwen3-Next-80B-A3B-Thinking-GGUF | 80.0 | Qwen3 | 31 |
| Qwen2-1.5B-Instruct-GGUF | 1.5 | Qwen2 | 29 |
| Qwen3-VL-8B-Thinking-GGUF | 8.0 | Qwen3 | 27 |
| Qwen2.5-Coder-0.5B-Instruct-GGUF | 0.5 | Qwen2.5 | 23 |
| Qwen3-VL-2B-Thinking-GGUF | 2.0 | Qwen3 | 22 |
| Qwen1.5-1.8B-Chat-GGUF | 1.8 | Qwen1.5 | 21 |
| Qwen3-VL-32B-Instruct-GGUF | 32.0 | Qwen3 | 20 |
| Qwen3-VL-4B-Thinking-GGUF | 4.0 | Qwen3 | 18 |
| Qwen2-57B-A14B-Instruct-GGUF | 57.0 | Qwen2 | 17 |
| Qwen3-VL-30B-A3B-Instruct-GGUF | 30.0 | Qwen3 | 17 |
| Qwen1.5-4B-Chat-GGUF | 4.0 | Qwen1.5 | 16 |
| Qwen1.5-110B-Chat-GGUF | 110.0 | Qwen1.5 | 14 |
| Qwen3-VL-32B-Thinking-GGUF | 32.0 | Qwen3 | 13 |
| Qwen3-VL-235B-A22B-Instruct-GGUF | 235.0 | Qwen3 | 13 |
| Qwen3-VL-30B-A3B-Thinking-GGUF | 30.0 | Qwen3 | 11 |
| Qwen3-235B-A22B-GGUF | 235.0 | Qwen3 | 10 |
| Qwen3-VL-235B-A22B-Thinking-GGUF | 235.0 | Qwen3 | 1 |

### GPTQ (74 models)

| Model | Size (B) | Family | Likes |
| --- | --- | --- | --- |
| Qwen-14B-Chat-Int4 | 14.0 | Qwen (original) | 100 |
| Qwen-VL-Chat-Int4 | - | Qwen (original) | 95 |
| Qwen3.5-35B-A3B-GPTQ-Int4 | 35.0 | Qwen3.5 | 91 |
| Qwen-7B-Chat-Int4 | 7.0 | Qwen (original) | 75 |
| Qwen3.5-27B-GPTQ-Int4 | 27.0 | Qwen3.5 | 57 |
| Qwen3-30B-A3B-GPTQ-Int4 | 30.0 | Qwen3 | 53 |
| Qwen1.5-MoE-A2.7B-Chat-GPTQ-Int4 | 2.7 | Qwen1.5 | 50 |
| Qwen-72B-Chat-Int4 | 72.0 | Qwen (original) | 47 |
| Qwen2.5-72B-Instruct-GPTQ-Int4 | 72.0 | Qwen2.5 | 44 |
| Qwen3.5-122B-A10B-GPTQ-Int4 | 122.0 | Qwen3.5 | 42 |
| Qwen2.5-32B-Instruct-GPTQ-Int4 | 32.0 | Qwen2.5 | 40 |
| Qwen1.5-72B-Chat-GPTQ-Int4 | 72.0 | Qwen1.5 | 37 |
| Qwen2-VL-7B-Instruct-GPTQ-Int4 | 7.0 | Qwen2 | 37 |
| Qwen-1_8B-Chat-Int4 | 8.0 | Qwen (original) | 36 |
| Qwen3.5-397B-A17B-GPTQ-Int4 | 397.0 | Qwen3.5 | 35 |
| Qwen2-72B-Instruct-GPTQ-Int4 | 72.0 | Qwen2 | 33 |
| Qwen2.5-7B-Instruct-GPTQ-Int4 | 7.0 | Qwen2.5 | 33 |
| Qwen1.5-32B-Chat-GPTQ-Int4 | 32.0 | Qwen1.5 | 31 |
| Qwen2-VL-7B-Instruct-GPTQ-Int8 | 7.0 | Qwen2 | 31 |
| Qwen2-VL-72B-Instruct-GPTQ-Int4 | 72.0 | Qwen2 | 30 |
| Qwen2-7B-Instruct-GPTQ-Int4 | 7.0 | Qwen2 | 28 |
| Qwen2-VL-2B-Instruct-GPTQ-Int4 | 2.0 | Qwen2 | 28 |
| Qwen2.5-72B-Instruct-GPTQ-Int8 | 72.0 | Qwen2.5 | 28 |
| Qwen3-235B-A22B-GPTQ-Int4 | 235.0 | Qwen3 | 27 |
| Qwen1.5-7B-Chat-GPTQ-Int8 | 7.0 | Qwen1.5 | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int4 | 14.0 | Qwen2.5 | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int8 | 14.0 | Qwen2.5 | 26 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int8 | 32.0 | Qwen2.5 | 24 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 | 32.0 | Qwen2.5 | 24 |
| Qwen2-57B-A14B-Instruct-GPTQ-Int4 | 57.0 | Qwen2 | 23 |
| Qwen1.5-14B-Chat-GPTQ-Int4 | 14.0 | Qwen1.5 | 21 |
| Qwen1.5-7B-Chat-GPTQ-Int4 | 7.0 | Qwen1.5 | 18 |
| Qwen1.5-110B-Chat-GPTQ-Int4 | 110.0 | Qwen1.5 | 18 |
| Qwen2.5-7B-Instruct-GPTQ-Int8 | 7.0 | Qwen2.5 | 18 |
| Qwen-72B-Chat-Int8 | 72.0 | Qwen (original) | 17 |
| Qwen2-7B-Instruct-GPTQ-Int8 | 7.0 | Qwen2 | 17 |
| Qwen2-VL-2B-Instruct-GPTQ-Int8 | 2.0 | Qwen2 | 17 |
| Qwen2-72B-Instruct-GPTQ-Int8 | 72.0 | Qwen2 | 15 |
| Qwen2-0.5B-Instruct-GPTQ-Int4 | 0.5 | Qwen2 | 15 |
| Qwen1.5-0.5B-Chat-GPTQ-Int4 | 0.5 | Qwen1.5 | 14 |
| Qwen2.5-32B-Instruct-GPTQ-Int8 | 32.0 | Qwen2.5 | 14 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int4 | 7.0 | Qwen2.5 | 14 |
| Qwen2.5-Omni-7B-GPTQ-Int4 | 7.0 | Qwen2.5 | 14 |
| Qwen1.5-14B-Chat-GPTQ-Int8 | 14.0 | Qwen1.5 | 11 |
| Qwen2-VL-72B-Instruct-GPTQ-Int8 | 72.0 | Qwen2 | 11 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int8 | 0.5 | Qwen2.5 | 10 |
| Qwen-7B-Chat-Int8 | 7.0 | Qwen (original) | 9 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int4 | 0.5 | Qwen2.5 | 9 |
| Qwen3-0.6B-GPTQ-Int8 | 0.6 | Qwen3 | 9 |
| Qwen-14B-Chat-Int8 | 14.0 | Qwen (original) | 7 |
| Qwen1.5-72B-Chat-GPTQ-Int8 | 72.0 | Qwen1.5 | 7 |
| Qwen1.5-1.8B-Chat-GPTQ-Int4 | 1.8 | Qwen1.5 | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int8 | 14.0 | Qwen2.5 | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int4 | 14.0 | Qwen2.5 | 7 |
| Qwen3-1.7B-GPTQ-Int8 | 1.7 | Qwen3 | 7 |
| Qwen1.5-4B-Chat-GPTQ-Int8 | 4.0 | Qwen1.5 | 6 |
| Qwen1.5-4B-Chat-GPTQ-Int4 | 4.0 | Qwen1.5 | 6 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int8 | 1.5 | Qwen2.5 | 6 |
| Qwen-1_8B-Chat-Int8 | 8.0 | Qwen (original) | 5 |
| Qwen2-1.5B-Instruct-GPTQ-Int4 | 1.5 | Qwen2 | 5 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int8 | 7.0 | Qwen2.5 | 5 |
| Qwen1.5-0.5B-Chat-GPTQ-Int8 | 0.5 | Qwen1.5 | 4 |
| Qwen2-1.5B-Instruct-GPTQ-Int8 | 1.5 | Qwen2 | 4 |
| Qwen2-0.5B-Instruct-GPTQ-Int8 | 0.5 | Qwen2 | 4 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int4 | 1.5 | Qwen2.5 | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int4 | 3.0 | Qwen2.5 | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int8 | 3.0 | Qwen2.5 | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int8 | 1.5 | Qwen2.5 | 3 |
| Qwen1.5-1.8B-Chat-GPTQ-Int8 | 1.8 | Qwen1.5 | 2 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int4 | 1.5 | Qwen2.5 | 2 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int8 | 0.5 | Qwen2.5 | 1 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int4 | 0.5 | Qwen2.5 | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int8 | 3.0 | Qwen2.5 | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int4 | 3.0 | Qwen2.5 | 1 |

## Top 50 Models by Community Engagement (Likes)

| Rank | Model | Size (B) | Family | Architecture | Capabilities | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | QwQ-32B | 32.0 | QwQ | Dense | Text Generation | text-generation | 2937 |
| 2 | Qwen-Image | - | Qwen (original) | Diffusion | Image Gen/Edit | text-to-image | 2529 |
| 3 | Qwen-Image-Edit | - | Qwen (original) | Diffusion | Image Gen/Edit | image-to-image | 2444 |
| 4 | Qwen3.6-35B-A3B | 35.0 | Qwen3.6 | MoE (A3B) | Vision-Language | image-text-to-text | 2319 |
| 5 | Qwen2.5-Coder-32B-Instruct | 32.0 | Qwen2.5 | Dense | Code, Text Generation | text-generation | 2062 |
| 6 | Qwen2.5-Omni-7B | 7.0 | Qwen2.5 | Dense | Omni/Multimodal | any-to-any | 1913 |
| 7 | Qwen3.6-27B | 27.0 | Qwen3.6 | Dense | Vision-Language | image-text-to-text | 1878 |
| 8 | QwQ-32B-Preview | 32.0 | QwQ | Dense | Text Generation | text-generation | 1740 |
| 9 | Qwen3-TTS-12Hz-1.7B-CustomVoice | 1.7 | Qwen3 | Specialized (TTS) | Audio/Speech (TTS) | text-to-speech | 1669 |
| 10 | Qwen3.5-9B | 9.0 | Qwen3.5 | Dense | Vision-Language | image-text-to-text | 1658 |
| 11 | Qwen2.5-VL-7B-Instruct | 7.0 | Qwen2.5 | Dense | Vision-Language | image-text-to-text | 1605 |
| 12 | Qwen3.5-397B-A17B | 397.0 | Qwen3.5 | MoE (A17B) | Vision-Language | image-text-to-text | 1526 |
| 13 | Qwen3-Coder-Next | - | Qwen3 | Dense | Code, Text Generation | text-generation | 1505 |
| 14 | Qwen3.5-35B-A3B | 35.0 | Qwen3.5 | MoE (A3B) | Vision-Language | image-text-to-text | 1455 |
| 15 | Qwen2.5-7B-Instruct | 7.0 | Qwen2.5 | Dense | Text Generation | text-generation | 1397 |
| 16 | Qwen3-0.6B | 0.6 | Qwen3 | Dense | Text Generation | text-generation | 1383 |
| 17 | Qwen3-Coder-480B-A35B-Instruct | 480.0 | Qwen3 | MoE (A35B) | Code, Text Generation | text-generation | 1347 |
| 18 | Qwen2-VL-7B-Instruct | 7.0 | Qwen2 | Dense | Vision-Language | image-text-to-text | 1281 |
| 19 | Qwen-Image-Edit-2509 | - | Qwen (original) | Diffusion | Image Gen/Edit | image-to-image | 1190 |
| 20 | Qwen3-8B | 8.0 | Qwen3 | Dense | Text Generation | text-generation | 1178 |
| 21 | Qwen3-Coder-30B-A3B-Instruct | 30.0 | Qwen3 | MoE (A3B) | Code, Text Generation | text-generation | 1139 |
| 22 | Qwen-Image-Layered | - | Qwen (original) | Dense | Image Gen/Edit | image-text-to-image | 1115 |
| 23 | Qwen3-235B-A22B | 235.0 | Qwen3 | MoE (A22B) | Text Generation | text-generation | 1100 |
| 24 | Qwen-Image-Edit-2511 | - | Qwen (original) | Diffusion | Image Gen/Edit | image-to-image | 1099 |
| 25 | Qwen3-Embedding-0.6B | 0.6 | Qwen3 | Dense | Embeddings | feature-extraction | 1094 |
| 26 | Qwen3-Next-80B-A3B-Instruct | 80.0 | Qwen3 | MoE (A3B) | Text Generation | text-generation | 1032 |
| 27 | Qwen3.5-27B | 27.0 | Qwen3.5 | Dense | Vision-Language | image-text-to-text | 996 |
| 28 | Qwen3-VL-8B-Instruct | 8.0 | Qwen3 | Dense | Vision-Language | image-text-to-text | 978 |
| 29 | Qwen2.5-72B-Instruct | 72.0 | Qwen2.5 | Dense | Text Generation | text-generation | 962 |
| 30 | Qwen3-Omni-30B-A3B-Instruct | 30.0 | Qwen3 | MoE (A3B) | Omni/Multimodal | any-to-any | 954 |
| 31 | Qwen3-ASR-1.7B | 1.7 | Qwen3 | Specialized (ASR) | Audio/Speech | automatic-speech-recognition | 911 |
| 32 | Qwen3-30B-A3B | 30.0 | Qwen3 | MoE (A3B) | Text Generation | text-generation | 905 |
| 33 | Qwen-Image-2512 | - | Qwen (original) | Diffusion | Image Gen/Edit | text-to-image | 897 |
| 34 | Qwen3-4B-Instruct-2507 | 4.0 | Qwen3 | Dense | Text Generation | text-generation | 892 |
| 35 | Qwen3-30B-A3B-Instruct-2507 | 30.0 | Qwen3 | MoE (A3B) | Text Generation | text-generation | 819 |
| 36 | Qwen-7B-Chat | 7.0 | Qwen (original) | Dense | Text Generation | text-generation | 789 |
| 37 | Qwen3-235B-A22B-Instruct-2507 | 235.0 | Qwen3 | MoE (A22B) | Text Generation | text-generation | 786 |
| 38 | Qwen2.5-1.5B-Instruct | 1.5 | Qwen2.5 | Dense | Text Generation | text-generation | 757 |
| 39 | Qwen2.5-Coder-7B-Instruct | 7.0 | Qwen2.5 | Dense | Code, Text Generation | text-generation | 745 |
| 40 | Qwen3-Embedding-8B | 8.0 | Qwen3 | Dense | Embeddings | feature-extraction | 732 |
| 41 | Qwen2-72B-Instruct | 72.0 | Qwen2 | Dense | Text Generation | text-generation | 718 |
| 42 | Qwen3.5-4B | 4.0 | Qwen3.5 | Dense | Vision-Language | image-text-to-text | 713 |
| 43 | Qwen3-32B | 32.0 | Qwen3 | Dense | Text Generation | text-generation | 709 |
| 44 | Qwen2-7B-Instruct | 7.0 | Qwen2 | Dense | Text Generation | text-generation | 686 |
| 45 | Qwen2.5-VL-3B-Instruct | 3.0 | Qwen2.5 | Dense | Vision-Language | image-text-to-text | 670 |
| 46 | Qwen3-4B | 4.0 | Qwen3 | Dense | Text Generation | text-generation | 645 |
| 47 | Qwen2.5-VL-72B-Instruct | 72.0 | Qwen2.5 | Dense | Vision-Language | image-text-to-text | 632 |
| 48 | QVQ-72B-Preview | 72.0 | QVQ | Dense | Vision-Language | image-text-to-text | 610 |
| 49 | Qwen3.5-0.8B | 0.8 | Qwen3.5 | Dense | Vision-Language | image-text-to-text | 605 |
| 50 | Qwen3-4B-Thinking-2507 | 4.0 | Qwen3 | Dense | Text Generation | text-generation | 600 |

## Complete Model Index

All 458 models sorted by family, then by likes descending.

### Other

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| WebWorld-8B | 8.0 | Small (2-8B) | Dense | text-generation | 64 |

### QVQ

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| QVQ-72B-Preview | 72.0 | Large (35-100B) | Dense | image-text-to-text | 610 |

### QwQ

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| QwQ-32B | 32.0 | Medium (8-35B) | Dense | text-generation | 2937 |
| QwQ-32B-Preview | 32.0 | Medium (8-35B) | Dense | text-generation | 1740 |
| QwQ-32B-GGUF | 32.0 | Medium (8-35B) | Dense | text-generation | 211 |
| QwQ-32B-AWQ | 32.0 | Medium (8-35B) | Dense | text-generation | 134 |

### Qwen (original)

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| Qwen-Image | - | Unknown | Diffusion | text-to-image | 2529 |
| Qwen-Image-Edit | - | Unknown | Diffusion | image-to-image | 2444 |
| Qwen-Image-Edit-2509 | - | Unknown | Diffusion | image-to-image | 1190 |
| Qwen-Image-Layered | - | Unknown | Dense | image-text-to-image | 1115 |
| Qwen-Image-Edit-2511 | - | Unknown | Diffusion | image-to-image | 1099 |
| Qwen-Image-2512 | - | Unknown | Diffusion | text-to-image | 897 |
| Qwen-7B-Chat | 7.0 | Small (2-8B) | Dense | text-generation | 789 |
| Qwen-7B | 7.0 | Small (2-8B) | Dense | text-generation | 399 |
| Qwen-VL-Chat | - | Unknown | Dense | text-generation | 384 |
| Qwen-14B-Chat | 14.0 | Medium (8-35B) | Dense | text-generation | 373 |
| Qwen-72B | 72.0 | Large (35-100B) | Dense | text-generation | 360 |
| Qwen-VL | - | Unknown | Dense | text-generation | 284 |
| Qwen-14B | 14.0 | Medium (8-35B) | Dense | text-generation | 214 |
| Qwen-72B-Chat | 72.0 | Large (35-100B) | Dense | text-generation | 156 |
| Qwen-Audio | - | Unknown | Dense | text-generation | 149 |
| Qwen-14B-Chat-Int4 | 14.0 | Medium (8-35B) | Dense | text-generation | 100 |
| Qwen-Audio-Chat | - | Unknown | Dense | text-generation | 96 |
| Qwen-VL-Chat-Int4 | - | Unknown | Dense | text-generation | 95 |
| Qwen-7B-Chat-Int4 | 7.0 | Small (2-8B) | Dense | text-generation | 75 |
| Qwen-1_8B | 8.0 | Small (2-8B) | Dense | text-generation | 73 |
| Qwen-Image-Bench | - | Unknown | Dense | image-text-to-text | 73 |
| Qwen-72B-Chat-Int4 | 72.0 | Large (35-100B) | Dense | text-generation | 47 |
| Qwen-1_8B-Chat-Int4 | 8.0 | Small (2-8B) | Dense | text-generation | 36 |
| Qwen-tokenizer | - | Unknown | Dense | - | 20 |
| Qwen-72B-Chat-Int8 | 72.0 | Large (35-100B) | Dense | text-generation | 17 |
| Qwen-7B-Chat-Int8 | 7.0 | Small (2-8B) | Dense | text-generation | 9 |
| Qwen-14B-Chat-Int8 | 14.0 | Medium (8-35B) | Dense | text-generation | 7 |
| Qwen-1_8B-Chat-Int8 | 8.0 | Small (2-8B) | Dense | text-generation | 5 |

### Qwen-AgentWorld

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| Qwen-AgentWorld-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | text-generation | 530 |

### Qwen1.5

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| CodeQwen1.5-7B-Chat | 7.0 | Small (2-8B) | Dense | text-generation | 353 |
| Qwen1.5-MoE-A2.7B | 2.7 | Small (2-8B) | MoE (A2.7B) | text-generation | 227 |
| Qwen1.5-72B-Chat | 72.0 | Large (35-100B) | Dense | text-generation | 217 |
| Qwen1.5-7B-Chat | 7.0 | Small (2-8B) | Dense | text-generation | 186 |
| Qwen1.5-0.5B | 0.5 | Micro (<2B) | Dense | text-generation | 174 |
| Qwen1.5-MoE-A2.7B-Chat | 2.7 | Small (2-8B) | MoE (A2.7B) | text-generation | 134 |
| Qwen1.5-110B-Chat | 110.0 | XLarge (>100B) | Dense | text-generation | 130 |
| Qwen1.5-14B-Chat | 14.0 | Medium (8-35B) | Dense | text-generation | 112 |
| CodeQwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | text-generation | 111 |
| Qwen1.5-32B-Chat | 32.0 | Medium (8-35B) | Dense | text-generation | 109 |
| CodeQwen1.5-7B | 7.0 | Small (2-8B) | Dense | text-generation | 104 |
| Qwen1.5-110B | 110.0 | XLarge (>100B) | Dense | text-generation | 104 |
| Qwen1.5-0.5B-Chat | 0.5 | Micro (<2B) | Dense | text-generation | 98 |
| Qwen1.5-32B | 32.0 | Medium (8-35B) | Dense | text-generation | 85 |
| Qwen1.5-1.8B-Chat | 1.8 | Micro (<2B) | Dense | text-generation | 74 |
| Qwen1.5-7B-Chat-GGUF | 7.0 | Small (2-8B) | Dense | text-generation | 71 |
| Qwen1.5-14B-Chat-GGUF | 14.0 | Medium (8-35B) | Dense | text-generation | 67 |
| Qwen1.5-72B-Chat-GGUF | 72.0 | Large (35-100B) | Dense | text-generation | 62 |
| Qwen1.5-1.8B | 1.8 | Micro (<2B) | Dense | text-generation | 59 |
| Qwen1.5-72B | 72.0 | Large (35-100B) | Dense | text-generation | 59 |
| Qwen1.5-7B | 7.0 | Small (2-8B) | Dense | text-generation | 56 |
| Qwen1.5-32B-Chat-GGUF | 32.0 | Medium (8-35B) | Dense | text-generation | 52 |
| Qwen1.5-MoE-A2.7B-Chat-GPTQ-Int4 | 2.7 | Small (2-8B) | MoE (A2.7B) | text-generation | 50 |
| Qwen1.5-4B-Chat | 4.0 | Small (2-8B) | Dense | text-generation | 46 |
| Qwen1.5-14B | 14.0 | Medium (8-35B) | Dense | text-generation | 41 |
| Qwen1.5-72B-Chat-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | text-generation | 37 |
| Qwen1.5-4B | 4.0 | Small (2-8B) | Dense | text-generation | 36 |
| Qwen1.5-0.5B-Chat-GGUF | 0.5 | Micro (<2B) | Dense | text-generation | 35 |
| Qwen1.5-32B-Chat-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | text-generation | 31 |
| Qwen1.5-72B-Chat-AWQ | 72.0 | Large (35-100B) | Dense | text-generation | 26 |
| Qwen1.5-7B-Chat-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | text-generation | 26 |
| Qwen1.5-14B-Chat-AWQ | 14.0 | Medium (8-35B) | Dense | text-generation | 23 |
| Qwen1.5-1.8B-Chat-GGUF | 1.8 | Micro (<2B) | Dense | text-generation | 21 |
| Qwen1.5-14B-Chat-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | text-generation | 21 |
| Qwen1.5-7B-Chat-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | text-generation | 18 |
| Qwen1.5-32B-Chat-AWQ | 32.0 | Medium (8-35B) | Dense | text-generation | 18 |
| Qwen1.5-110B-Chat-GPTQ-Int4 | 110.0 | XLarge (>100B) | Dense | text-generation | 18 |
| Qwen1.5-4B-Chat-GGUF | 4.0 | Small (2-8B) | Dense | text-generation | 16 |
| Qwen1.5-0.5B-Chat-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | text-generation | 14 |
| CodeQwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | text-generation | 14 |
| Qwen1.5-110B-Chat-GGUF | 110.0 | XLarge (>100B) | Dense | text-generation | 14 |
| Qwen1.5-7B-Chat-AWQ | 7.0 | Small (2-8B) | Dense | text-generation | 13 |
| Qwen1.5-14B-Chat-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | text-generation | 11 |
| Qwen1.5-110B-Chat-AWQ | 110.0 | XLarge (>100B) | Dense | text-generation | 9 |
| Qwen1.5-0.5B-Chat-AWQ | 0.5 | Micro (<2B) | Dense | text-generation | 7 |
| Qwen1.5-72B-Chat-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | text-generation | 7 |
| Qwen1.5-1.8B-Chat-GPTQ-Int4 | 1.8 | Micro (<2B) | Dense | text-generation | 7 |
| Qwen1.5-4B-Chat-GPTQ-Int8 | 4.0 | Small (2-8B) | Dense | text-generation | 6 |
| Qwen1.5-4B-Chat-GPTQ-Int4 | 4.0 | Small (2-8B) | Dense | text-generation | 6 |
| Qwen1.5-1.8B-Chat-AWQ | 1.8 | Micro (<2B) | Dense | text-generation | 4 |
| Qwen1.5-0.5B-Chat-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | text-generation | 4 |
| Qwen1.5-4B-Chat-AWQ | 4.0 | Small (2-8B) | Dense | text-generation | 3 |
| Qwen1.5-1.8B-Chat-GPTQ-Int8 | 1.8 | Micro (<2B) | Dense | text-generation | 2 |
| CodeQwen1.5-7B-AWQ | 7.0 | Small (2-8B) | Dense | text-generation | 2 |

### Qwen2

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| Qwen2-VL-7B-Instruct | 7.0 | Small (2-8B) | Dense | image-text-to-text | 1281 |
| Qwen2-72B-Instruct | 72.0 | Large (35-100B) | Dense | text-generation | 718 |
| Qwen2-7B-Instruct | 7.0 | Small (2-8B) | Dense | text-generation | 686 |
| Qwen2-Audio-7B-Instruct | 7.0 | Small (2-8B) | Dense | audio-text-to-text | 544 |
| Qwen2-VL-2B-Instruct | 2.0 | Small (2-8B) | Dense | image-text-to-text | 512 |
| Qwen2-VL-72B-Instruct | 72.0 | Large (35-100B) | Dense | image-text-to-text | 310 |
| Qwen2-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | text-generation | 201 |
| Qwen2-72B | 72.0 | Large (35-100B) | Dense | text-generation | 199 |
| Qwen2-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | text-generation | 179 |
| Qwen2-Audio-7B | 7.0 | Small (2-8B) | Dense | audio-text-to-text | 172 |
| Qwen2-7B | 7.0 | Small (2-8B) | Dense | text-generation | 171 |
| Qwen2-0.5B | 0.5 | Micro (<2B) | Dense | text-generation | 169 |
| Qwen2-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | text-generation | 162 |
| Qwen2-1.5B | 1.5 | Micro (<2B) | Dense | text-generation | 102 |
| Qwen2-Math-72B-Instruct | 72.0 | Large (35-100B) | Dense | text-generation | 89 |
| Qwen2-57B-A14B-Instruct | 57.0 | Large (35-100B) | MoE (A14B) | text-generation | 83 |
| WorldPM-72B | 72.0 | Large (35-100B) | Dense | text-classification | 82 |
| Qwen2-VL-72B | 72.0 | Large (35-100B) | Dense | image-text-to-text | 80 |
| Qwen2-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | text-generation | 73 |
| Qwen2-VL-7B | 7.0 | Small (2-8B) | Dense | image-text-to-text | 67 |
| Qwen2-VL-2B | 2.0 | Small (2-8B) | Dense | image-text-to-text | 65 |
| Qwen2-57B-A14B | 57.0 | Large (35-100B) | MoE (A14B) | text-generation | 58 |
| Qwen2-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | image-text-to-text | 50 |
| Qwen2-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | image-text-to-text | 49 |
| Qwen2-Math-7B-Instruct | 7.0 | Small (2-8B) | Dense | text-generation | 44 |
| Qwen2-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | text-generation | 41 |
| Qwen2-VL-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | image-text-to-text | 37 |
| Qwen2-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | text-generation | 33 |
| Qwen2-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | text-generation | 31 |
| Qwen2-VL-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | image-text-to-text | 31 |
| Qwen2-Math-72B | 72.0 | Large (35-100B) | Dense | text-generation | 30 |
| Qwen2-VL-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | image-text-to-text | 30 |
| Qwen2-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | text-generation | 29 |
| Qwen2-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | text-generation | 28 |
| Qwen2-VL-2B-Instruct-GPTQ-Int4 | 2.0 | Small (2-8B) | Dense | image-text-to-text | 28 |
| Qwen2-VL-2B-Instruct-AWQ | 2.0 | Small (2-8B) | Dense | image-text-to-text | 25 |
| Qwen2-57B-A14B-Instruct-GPTQ-Int4 | 57.0 | Large (35-100B) | MoE (A14B) | text-generation | 23 |
| Qwen2-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | text-generation | 23 |
| Qwen2-Math-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | text-generation | 21 |
| Qwen2-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | text-generation | 17 |
| Qwen2-57B-A14B-Instruct-GGUF | 57.0 | Large (35-100B) | MoE (A14B) | text-generation | 17 |
| Qwen2-VL-2B-Instruct-GPTQ-Int8 | 2.0 | Small (2-8B) | Dense | image-text-to-text | 17 |
| Qwen2-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | text-generation | 15 |
| Qwen2-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | text-generation | 15 |
| Qwen2-Math-7B | 7.0 | Small (2-8B) | Dense | text-generation | 14 |
| Qwen2-Math-1.5B | 1.5 | Micro (<2B) | Dense | text-generation | 14 |
| Qwen2-VL-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | image-text-to-text | 11 |
| WorldPM-72B-HelpSteer2 | 72.0 | Large (35-100B) | Dense | text-classification | 11 |
| WorldPM-72B-RLHFLow | 72.0 | Large (35-100B) | Dense | text-classification | 11 |
| Qwen2-0.5B-Instruct-MLX | 0.5 | Micro (<2B) | Dense | text-generation | 10 |
| Qwen2-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | text-generation | 9 |
| WorldPM-72B-UltraFeedback | 72.0 | Large (35-100B) | Dense | text-classification | 8 |
| Qwen2-Math-RM-72B | 72.0 | Large (35-100B) | Dense | text-classification | 7 |
| Qwen2-7B-Instruct-MLX | 7.0 | Small (2-8B) | Dense | text-generation | 7 |
| Qwen2-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | text-generation | 5 |
| Qwen2-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | text-generation | 5 |
| Qwen2-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | text-generation | 4 |
| Qwen2-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | text-generation | 4 |
| Qwen2-1.5B-Instruct-MLX | 1.5 | Micro (<2B) | Dense | text-generation | 4 |

### Qwen2.5

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| Qwen2.5-Coder-32B-Instruct | 32.0 | Medium (8-35B) | Dense | text-generation | 2062 |
| Qwen2.5-Omni-7B | 7.0 | Small (2-8B) | Dense | any-to-any | 1913 |
| Qwen2.5-VL-7B-Instruct | 7.0 | Small (2-8B) | Dense | image-text-to-text | 1605 |
| Qwen2.5-7B-Instruct | 7.0 | Small (2-8B) | Dense | text-generation | 1397 |
| Qwen2.5-72B-Instruct | 72.0 | Large (35-100B) | Dense | text-generation | 962 |
| Qwen2.5-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | text-generation | 757 |
| Qwen2.5-Coder-7B-Instruct | 7.0 | Small (2-8B) | Dense | text-generation | 745 |
| Qwen2.5-VL-3B-Instruct | 3.0 | Small (2-8B) | Dense | image-text-to-text | 670 |
| Qwen2.5-VL-72B-Instruct | 72.0 | Large (35-100B) | Dense | image-text-to-text | 632 |
| Qwen2.5-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | text-generation | 549 |
| Qwen2.5-3B-Instruct | 3.0 | Small (2-8B) | Dense | text-generation | 521 |
| Qwen2.5-VL-32B-Instruct | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 494 |
| Qwen2.5-0.5B | 0.5 | Micro (<2B) | Dense | text-generation | 428 |
| Qwen2.5-7B-Instruct-1M | 7.0 | Small (2-8B) | Dense | text-generation | 371 |
| Qwen2.5-32B-Instruct | 32.0 | Medium (8-35B) | Dense | text-generation | 354 |
| Qwen2.5-14B-Instruct | 14.0 | Medium (8-35B) | Dense | text-generation | 351 |
| Qwen2.5-14B-Instruct-1M | 14.0 | Medium (8-35B) | Dense | text-generation | 341 |
| Qwen2.5-Omni-3B | 3.0 | Small (2-8B) | Dense | any-to-any | 337 |
| Qwen2.5-Coder-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | text-generation | 310 |
| Qwen2.5-7B | 7.0 | Small (2-8B) | Dense | text-generation | 294 |
| Qwen2.5-Coder-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | text-generation | 209 |
| Qwen2.5-3B | 3.0 | Small (2-8B) | Dense | text-generation | 194 |
| Qwen2.5-1.5B | 1.5 | Micro (<2B) | Dense | text-generation | 192 |
| Qwen2.5-32B | 32.0 | Medium (8-35B) | Dense | text-generation | 179 |
| Qwen2.5-Coder-14B-Instruct | 14.0 | Medium (8-35B) | Dense | text-generation | 171 |
| Qwen2.5-7B-Instruct-GGUF | 7.0 | Small (2-8B) | Dense | text-generation | 164 |
| Qwen2.5-Coder-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | text-generation | 161 |
| Qwen2.5-Coder-32B | 32.0 | Medium (8-35B) | Dense | text-generation | 157 |
| Qwen2.5-Coder-7B | 7.0 | Small (2-8B) | Dense | text-generation | 155 |
| Qwen2.5-14B | 14.0 | Medium (8-35B) | Dense | text-generation | 154 |
| Qwen2.5-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | text-generation | 142 |
| Qwen2.5-Coder-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | text-generation | 132 |
| Qwen2.5-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | text-generation | 123 |
| Qwen2.5-Math-7B | 7.0 | Small (2-8B) | Dense | text-generation | 114 |
| Qwen2.5-Coder-3B-Instruct | 3.0 | Small (2-8B) | Dense | text-generation | 114 |
| Qwen2.5-Math-1.5B | 1.5 | Micro (<2B) | Dense | text-generation | 110 |
| Qwen2.5-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | text-generation | 110 |
| Qwen2.5-VL-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | image-text-to-text | 106 |
| Qwen2.5-72B | 72.0 | Large (35-100B) | Dense | text-generation | 101 |
| Qwen2.5-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | text-generation | 101 |
| Qwen2.5-Coder-1.5B | 1.5 | Micro (<2B) | Dense | text-generation | 94 |
| Qwen2.5-Coder-3B-Instruct-GGUF | 3.0 | Small (2-8B) | Dense | text-generation | 93 |
| Qwen2.5-Math-7B-Instruct | 7.0 | Small (2-8B) | Dense | text-generation | 91 |
| Qwen2.5-Math-PRM-7B | 7.0 | Small (2-8B) | Dense | text-classification | 90 |
| Qwen2.5-Math-RM-72B | 72.0 | Large (35-100B) | Dense | text-classification | 83 |
| Qwen2.5-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | text-generation | 78 |
| Qwen2.5-Coder-14B | 14.0 | Medium (8-35B) | Dense | text-generation | 77 |
| Qwen2.5-Math-PRM-72B | 72.0 | Large (35-100B) | Dense | text-classification | 77 |
| Qwen2.5-VL-72B-Instruct-AWQ | 72.0 | Large (35-100B) | Dense | image-text-to-text | 73 |
| Qwen2.5-Coder-0.5B-Instruct | 0.5 | Micro (<2B) | Dense | text-generation | 72 |
| Qwen2.5-Coder-1.5B-Instruct-GGUF | 1.5 | Micro (<2B) | Dense | text-generation | 69 |
| Qwen2.5-VL-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | image-text-to-text | 64 |
| Qwen2.5-VL-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 63 |
| Qwen2.5-14B-Instruct-GGUF | 14.0 | Medium (8-35B) | Dense | text-generation | 59 |
| Qwen2.5-Math-1.5B-Instruct | 1.5 | Micro (<2B) | Dense | text-generation | 58 |
| Qwen2.5-Coder-0.5B | 0.5 | Micro (<2B) | Dense | text-generation | 57 |
| Qwen2.5-Coder-3B | 3.0 | Small (2-8B) | Dense | text-generation | 53 |
| Qwen2.5-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | text-generation | 47 |
| Qwen2.5-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | text-generation | 45 |
| Qwen2.5-72B-Instruct-GPTQ-Int4 | 72.0 | Large (35-100B) | Dense | text-generation | 44 |
| Qwen2.5-72B-Instruct-GGUF | 72.0 | Large (35-100B) | Dense | text-generation | 44 |
| Qwen2.5-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | text-generation | 40 |
| Qwen2.5-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | text-generation | 37 |
| Qwen2.5-Coder-32B-Instruct-AWQ | 32.0 | Medium (8-35B) | Dense | text-generation | 37 |
| Qwen2.5-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | text-generation | 33 |
| Qwen2.5-Math-72B-Instruct | 72.0 | Large (35-100B) | Dense | text-generation | 31 |
| Qwen2.5-72B-Instruct-GPTQ-Int8 | 72.0 | Large (35-100B) | Dense | text-generation | 28 |
| Qwen2.5-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | text-generation | 26 |
| Qwen2.5-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | text-generation | 26 |
| Qwen2.5-Coder-7B-Instruct-AWQ | 7.0 | Small (2-8B) | Dense | text-generation | 26 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | text-generation | 24 |
| Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 | 32.0 | Medium (8-35B) | Dense | text-generation | 24 |
| Qwen2.5-Coder-0.5B-Instruct-GGUF | 0.5 | Micro (<2B) | Dense | text-generation | 23 |
| Qwen2.5-Coder-14B-Instruct-AWQ | 14.0 | Medium (8-35B) | Dense | text-generation | 21 |
| Qwen2.5-Math-7B-PRM800K | 7.0 | Small (2-8B) | Dense | text-classification | 21 |
| Qwen2.5-Math-72B | 72.0 | Large (35-100B) | Dense | text-generation | 18 |
| Qwen2.5-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | text-generation | 18 |
| Qwen2.5-Omni-7B-AWQ | 7.0 | Small (2-8B) | Dense | any-to-any | 18 |
| Qwen2.5-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | text-generation | 16 |
| Qwen2.5-32B-Instruct-GPTQ-Int8 | 32.0 | Medium (8-35B) | Dense | text-generation | 14 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | text-generation | 14 |
| Qwen2.5-Omni-7B-GPTQ-Int4 | 7.0 | Small (2-8B) | Dense | any-to-any | 14 |
| Qwen2.5-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | text-generation | 11 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | text-generation | 10 |
| Qwen2.5-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | text-generation | 9 |
| Qwen2.5-Coder-3B-Instruct-AWQ | 3.0 | Small (2-8B) | Dense | text-generation | 8 |
| Qwen2.5-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int8 | 14.0 | Medium (8-35B) | Dense | text-generation | 7 |
| Qwen2.5-Coder-14B-Instruct-GPTQ-Int4 | 14.0 | Medium (8-35B) | Dense | text-generation | 7 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | text-generation | 6 |
| Qwen2.5-Coder-7B-Instruct-GPTQ-Int8 | 7.0 | Small (2-8B) | Dense | text-generation | 5 |
| Qwen2.5-Coder-1.5B-Instruct-AWQ | 1.5 | Micro (<2B) | Dense | text-generation | 4 |
| Qwen2.5-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | text-generation | 3 |
| Qwen2.5-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | text-generation | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int8 | 1.5 | Micro (<2B) | Dense | text-generation | 3 |
| Qwen2.5-Coder-0.5B-Instruct-AWQ | 0.5 | Micro (<2B) | Dense | text-generation | 3 |
| Qwen2.5-Coder-1.5B-Instruct-GPTQ-Int4 | 1.5 | Micro (<2B) | Dense | text-generation | 2 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int8 | 0.5 | Micro (<2B) | Dense | text-generation | 1 |
| Qwen2.5-Coder-0.5B-Instruct-GPTQ-Int4 | 0.5 | Micro (<2B) | Dense | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int8 | 3.0 | Small (2-8B) | Dense | text-generation | 1 |
| Qwen2.5-Coder-3B-Instruct-GPTQ-Int4 | 3.0 | Small (2-8B) | Dense | text-generation | 1 |

### Qwen3

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | 1.7 | Micro (<2B) | Specialized (TTS) | text-to-speech | 1669 |
| Qwen3-Coder-Next | - | Unknown | Dense | text-generation | 1505 |
| Qwen3-0.6B | 0.6 | Micro (<2B) | Dense | text-generation | 1383 |
| Qwen3-Coder-480B-A35B-Instruct | 480.0 | XLarge (>100B) | MoE (A35B) | text-generation | 1347 |
| Qwen3-8B | 8.0 | Small (2-8B) | Dense | text-generation | 1178 |
| Qwen3-Coder-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 1139 |
| Qwen3-235B-A22B | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 1100 |
| Qwen3-Embedding-0.6B | 0.6 | Micro (<2B) | Dense | feature-extraction | 1094 |
| Qwen3-Next-80B-A3B-Instruct | 80.0 | Large (35-100B) | MoE (A3B) | text-generation | 1032 |
| Qwen3-VL-8B-Instruct | 8.0 | Small (2-8B) | Dense | image-text-to-text | 978 |
| Qwen3-Omni-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | any-to-any | 954 |
| Qwen3-ASR-1.7B | 1.7 | Micro (<2B) | Specialized (ASR) | automatic-speech-recognition | 911 |
| Qwen3-30B-A3B | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 905 |
| Qwen3-4B-Instruct-2507 | 4.0 | Small (2-8B) | Dense | text-generation | 892 |
| Qwen3-30B-A3B-Instruct-2507 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 819 |
| Qwen3-235B-A22B-Instruct-2507 | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 786 |
| Qwen3-Embedding-8B | 8.0 | Small (2-8B) | Dense | feature-extraction | 732 |
| Qwen3-32B | 32.0 | Medium (8-35B) | Dense | text-generation | 709 |
| Qwen3-4B | 4.0 | Small (2-8B) | Dense | text-generation | 645 |
| Qwen3-4B-Thinking-2507 | 4.0 | Small (2-8B) | Dense | text-generation | 600 |
| Qwen3-VL-30B-A3B-Instruct | 30.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 582 |
| Qwen3-Embedding-0.6B-GGUF | 0.6 | Micro (<2B) | Dense | - | 539 |
| Qwen3-1.7B | 1.7 | Micro (<2B) | Dense | text-generation | 496 |
| Qwen3-Next-80B-A3B-Thinking | 80.0 | Large (35-100B) | MoE (A3B) | text-generation | 490 |
| Qwen3-VL-Embedding-8B | 8.0 | Small (2-8B) | Dense | sentence-similarity | 451 |
| Qwen3-VL-2B-Instruct | 2.0 | Small (2-8B) | Dense | image-text-to-text | 436 |
| Qwen3-TTS-12Hz-1.7B-Base | 1.7 | Micro (<2B) | Specialized (TTS) | - | 434 |
| Qwen3-VL-Embedding-2B | 2.0 | Small (2-8B) | Dense | sentence-similarity | 427 |
| Qwen3-14B | 14.0 | Medium (8-35B) | Dense | text-generation | 417 |
| Qwen3-235B-A22B-Thinking-2507 | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 407 |
| Qwen3-VL-4B-Instruct | 4.0 | Small (2-8B) | Dense | image-text-to-text | 404 |
| Qwen3-VL-235B-A22B-Instruct | 235.0 | XLarge (>100B) | MoE (A22B) | image-text-to-text | 400 |
| Qwen3-VL-235B-A22B-Thinking | 235.0 | XLarge (>100B) | MoE (A22B) | image-text-to-text | 399 |
| Qwen3-30B-A3B-Thinking-2507 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 377 |
| Qwen3-Reranker-0.6B | 0.6 | Micro (<2B) | Dense | text-ranking | 369 |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | 1.7 | Micro (<2B) | Specialized (TTS) | text-to-speech | 366 |
| Qwen3-ASR-0.6B | 0.6 | Micro (<2B) | Specialized (ASR) | automatic-speech-recognition | 310 |
| Qwen3-Omni-30B-A3B-Thinking | 30.0 | Medium (8-35B) | MoE (A3B) | any-to-any | 309 |
| Qwen3-Embedding-4B | 4.0 | Small (2-8B) | Dense | feature-extraction | 292 |
| Qwen3-Coder-Next-GGUF | - | Unknown | Dense | text-generation | 260 |
| Qwen3-TTS-12Hz-0.6B-Base | 0.6 | Micro (<2B) | Specialized (TTS) | text-to-speech | 259 |
| Qwen3-Reranker-8B | 8.0 | Small (2-8B) | Dense | text-ranking | 248 |
| Qwen3-Omni-30B-A3B-Captioner | 30.0 | Medium (8-35B) | MoE (A3B) | any-to-any | 231 |
| Qwen3-VL-8B-Thinking | 8.0 | Small (2-8B) | Dense | image-text-to-text | 215 |
| Qwen3-8B-GGUF | 8.0 | Small (2-8B) | Dense | text-generation | 212 |
| Qwen3-VL-32B-Instruct | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 210 |
| Qwen3-VL-Reranker-2B | 2.0 | Small (2-8B) | Dense | text-ranking | 201 |
| Qwen3-VL-30B-A3B-Thinking | 30.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 199 |
| Qwen3-Coder-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 187 |
| Qwen3-0.6B-Base | 0.6 | Micro (<2B) | Dense | text-generation | 174 |
| Qwen3-TTS-12Hz-0.6B-CustomVoice | 0.6 | Micro (<2B) | Specialized (TTS) | text-to-speech | 164 |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | 480.0 | XLarge (>100B) | MoE (A35B) | text-generation | 156 |
| Qwen3-Coder-Next-FP8 | - | Unknown | Dense | text-generation | 156 |
| Qwen3-VL-Reranker-8B | 8.0 | Small (2-8B) | Dense | text-ranking | 154 |
| Qwen3-235B-A22B-Instruct-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 148 |
| Qwen3-Reranker-4B | 4.0 | Small (2-8B) | Dense | text-ranking | 146 |
| Qwen3-ForcedAligner-0.6B | 0.6 | Micro (<2B) | Specialized (ASR) | automatic-speech-recognition | 145 |
| Qwen3-32B-AWQ | 32.0 | Medium (8-35B) | Dense | text-generation | 136 |
| Qwen3-30B-A3B-Instruct-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 130 |
| Qwen3-Embedding-8B-GGUF | 8.0 | Small (2-8B) | Dense | - | 129 |
| Qwen3Guard-Gen-8B | 8.0 | Small (2-8B) | Dense | text-generation | 119 |
| Qwen3-VL-2B-Thinking | 2.0 | Small (2-8B) | Dense | image-text-to-text | 115 |
| Qwen3-Embedding-4B-GGUF | 4.0 | Small (2-8B) | Dense | - | 114 |
| Qwen3-4B-GGUF | 4.0 | Small (2-8B) | Dense | text-generation | 113 |
| Qwen3-VL-30B-A3B-Instruct-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 113 |
| Qwen3-VL-4B-Thinking | 4.0 | Small (2-8B) | Dense | image-text-to-text | 113 |
| Qwen3-VL-8B-Instruct-GGUF | 8.0 | Small (2-8B) | Dense | image-text-to-text | 111 |
| Qwen3-8B-Base | 8.0 | Small (2-8B) | Dense | text-generation | 110 |
| Qwen3-14B-GGUF | 14.0 | Medium (8-35B) | Dense | text-generation | 109 |
| Qwen3-4B-Base | 4.0 | Small (2-8B) | Dense | text-generation | 95 |
| Qwen3-235B-A22B-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 93 |
| Qwen3-Next-80B-A3B-Instruct-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | text-generation | 90 |
| Qwen3-VL-32B-Thinking | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 87 |
| Qwen3-235B-A22B-Thinking-2507-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 86 |
| Qwen3-32B-FP8 | 32.0 | Medium (8-35B) | Dense | text-generation | 84 |
| Qwen3-30B-A3B-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 84 |
| Qwen3-4B-Instruct-2507-FP8 | 4.0 | Small (2-8B) | Dense | text-generation | 78 |
| Qwen3-1.7B-Base | 1.7 | Micro (<2B) | Dense | text-generation | 75 |
| Qwen3Guard-Gen-0.6B | 0.6 | Micro (<2B) | Dense | text-generation | 75 |
| Qwen3-30B-A3B-Base | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 73 |
| Qwen3-VL-8B-Instruct-FP8 | 8.0 | Small (2-8B) | Dense | image-text-to-text | 73 |
| Qwen3-30B-A3B-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 72 |
| Qwen3-14B-AWQ | 14.0 | Medium (8-35B) | Dense | text-generation | 70 |
| Qwen3-TTS-Tokenizer-12Hz | - | Unknown | Dense | audio-to-audio | 70 |
| Qwen3-Coder-Next-Base | - | Unknown | Dense | text-generation | 70 |
| WebWorld-32B | 32.0 | Medium (8-35B) | Dense | text-generation | 70 |
| Qwen3-32B-GGUF | 32.0 | Medium (8-35B) | Dense | text-generation | 69 |
| Qwen3-30B-A3B-Thinking-2507-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 67 |
| Qwen3-4B-Thinking-2507-FP8 | 4.0 | Small (2-8B) | Dense | text-generation | 66 |
| Qwen3-0.6B-GGUF | 0.6 | Micro (<2B) | Dense | text-generation | 63 |
| Qwen3-VL-4B-Instruct-FP8 | 4.0 | Small (2-8B) | Dense | image-text-to-text | 63 |
| Qwen3-0.6B-FP8 | 0.6 | Micro (<2B) | Dense | text-generation | 62 |
| Qwen3-8B-FP8 | 8.0 | Small (2-8B) | Dense | text-generation | 62 |
| Qwen3-VL-30B-A3B-Thinking-FP8 | 30.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 57 |
| Qwen3-14B-Base | 14.0 | Medium (8-35B) | Dense | text-generation | 54 |
| Qwen3-Next-80B-A3B-Thinking-FP8 | 80.0 | Large (35-100B) | MoE (A3B) | text-generation | 54 |
| Qwen3-30B-A3B-GPTQ-Int4 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 53 |
| Qwen3Guard-Gen-4B | 4.0 | Small (2-8B) | Dense | text-generation | 52 |
| Qwen3-8B-AWQ | 8.0 | Small (2-8B) | Dense | text-generation | 51 |
| Qwen3-VL-2B-Instruct-GGUF | 2.0 | Small (2-8B) | Dense | image-text-to-text | 50 |
| Qwen3-1.7B-GGUF | 1.7 | Micro (<2B) | Dense | text-generation | 49 |
| Qwen3-VL-4B-Instruct-GGUF | 4.0 | Small (2-8B) | Dense | image-text-to-text | 49 |
| Qwen3-14B-FP8 | 14.0 | Medium (8-35B) | Dense | text-generation | 48 |
| Qwen3-VL-32B-Instruct-FP8 | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 46 |
| Qwen3-4B-SafeRL | 4.0 | Small (2-8B) | Dense | text-generation | 44 |
| Qwen3-VL-235B-A22B-Instruct-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | image-text-to-text | 44 |
| Qwen3-VL-2B-Instruct-FP8 | 2.0 | Small (2-8B) | Dense | image-text-to-text | 42 |
| Qwen3-4B-FP8 | 4.0 | Small (2-8B) | Dense | text-generation | 39 |
| Qwen3Guard-Stream-8B | 8.0 | Small (2-8B) | Dense | - | 38 |
| SAE-Res-Qwen3.5-27B-W80K-L0_50 | 27.0 | Medium (8-35B) | Dense | - | 38 |
| Qwen3-1.7B-FP8 | 1.7 | Micro (<2B) | Dense | text-generation | 36 |
| Qwen3Guard-Stream-0.6B | 0.6 | Micro (<2B) | Dense | feature-extraction | 32 |
| Qwen3-VL-8B-Thinking-FP8 | 8.0 | Small (2-8B) | Dense | image-text-to-text | 32 |
| Qwen3-Next-80B-A3B-Instruct-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | text-generation | 32 |
| Qwen3-4B-MLX-4bit | 4.0 | Small (2-8B) | Dense | text-generation | 31 |
| Qwen3-VL-2B-Thinking-FP8 | 2.0 | Small (2-8B) | Dense | image-text-to-text | 31 |
| Qwen3-Next-80B-A3B-Thinking-GGUF | 80.0 | Large (35-100B) | MoE (A3B) | text-generation | 31 |
| Qwen3-VL-4B-Thinking-FP8 | 4.0 | Small (2-8B) | Dense | image-text-to-text | 30 |
| Qwen3-4B-AWQ | 4.0 | Small (2-8B) | Dense | text-generation | 29 |
| Qwen3-VL-235B-A22B-Thinking-FP8 | 235.0 | XLarge (>100B) | MoE (A22B) | image-text-to-text | 29 |
| WebWorld-14B | 14.0 | Medium (8-35B) | Dense | text-generation | 28 |
| Qwen3-ASR-1.7B-hf | 1.7 | Micro (<2B) | Specialized (ASR) | automatic-speech-recognition | 28 |
| Qwen3-235B-A22B-GPTQ-Int4 | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 27 |
| Qwen3-VL-8B-Thinking-GGUF | 8.0 | Small (2-8B) | Dense | image-text-to-text | 27 |
| Qwen3-VL-32B-Thinking-FP8 | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 26 |
| Qwen3-0.6B-MLX-4bit | 0.6 | Micro (<2B) | Dense | text-generation | 23 |
| Qwen3Guard-Stream-4B | 4.0 | Small (2-8B) | Dense | feature-extraction | 23 |
| Qwen3-VL-2B-Thinking-GGUF | 2.0 | Small (2-8B) | Dense | image-text-to-text | 22 |
| Qwen3-VL-32B-Instruct-GGUF | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 20 |
| Qwen3-ASR-0.6B-hf | 0.6 | Micro (<2B) | Specialized (ASR) | automatic-speech-recognition | 19 |
| Qwen3-VL-4B-Thinking-GGUF | 4.0 | Small (2-8B) | Dense | image-text-to-text | 18 |
| Qwen3-VL-30B-A3B-Instruct-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 17 |
| Qwen3-235B-A22B-MLX-4bit | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 16 |
| Qwen3-14B-MLX-4bit | 14.0 | Medium (8-35B) | Dense | text-generation | 14 |
| Qwen3-VL-32B-Thinking-GGUF | 32.0 | Medium (8-35B) | Dense | image-text-to-text | 13 |
| Qwen3-VL-235B-A22B-Instruct-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | image-text-to-text | 13 |
| SAE-Res-Qwen3.5-2B-Base-W32K-L0_50 | 2.0 | Small (2-8B) | Dense | - | 13 |
| SAE-Res-Qwen3.5-27B-W80K-L0_100 | 27.0 | Medium (8-35B) | Dense | - | 13 |
| Qwen3-32B-MLX-8bit | 32.0 | Medium (8-35B) | Dense | text-generation | 11 |
| Qwen3-30B-A3B-MLX-4bit | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 11 |
| Qwen3-VL-30B-A3B-Thinking-GGUF | 30.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 11 |
| Qwen3-ForcedAligner-0.6B-hf | 0.6 | Micro (<2B) | Specialized (ASR) | token-classification | 11 |
| Qwen3-235B-A22B-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 10 |
| Qwen3-8B-MLX-4bit | 8.0 | Small (2-8B) | Dense | text-generation | 10 |
| SAE-Res-Qwen3.5-9B-Base-W64K-L0_50 | 9.0 | Medium (8-35B) | Dense | - | 10 |
| Qwen3-0.6B-GPTQ-Int8 | 0.6 | Micro (<2B) | Dense | text-generation | 9 |
| Qwen3-8B-MLX-bf16 | 8.0 | Small (2-8B) | Dense | text-generation | 9 |
| Qwen3-32B-MLX-bf16 | 32.0 | Medium (8-35B) | Dense | text-generation | 9 |
| Qwen3-30B-A3B-MLX-8bit | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 9 |
| Qwen3-235B-A22B-MLX-8bit | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 9 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W128K-L0_100 | 35.0 | Medium (8-35B) | MoE (A3B) | - | 9 |
| Qwen3-8B-MLX-8bit | 8.0 | Small (2-8B) | Dense | text-generation | 8 |
| Qwen3-32B-MLX-4bit | 32.0 | Medium (8-35B) | Dense | text-generation | 8 |
| Qwen3-30B-A3B-MLX-bf16 | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 8 |
| Qwen3-1.7B-GPTQ-Int8 | 1.7 | Micro (<2B) | Dense | text-generation | 7 |
| Qwen3-1.7B-MLX-bf16 | 1.7 | Micro (<2B) | Dense | text-generation | 7 |
| SAE-Res-Qwen3.5-9B-Base-W64K-L0_100 | 9.0 | Medium (8-35B) | Dense | - | 7 |
| SAE-Res-Qwen3.5-35B-A3B-Base-W32K-L0_50 | 35.0 | Medium (8-35B) | MoE (A3B) | - | 7 |
| Qwen3-0.6B-MLX-6bit | 0.6 | Micro (<2B) | Dense | text-generation | 6 |
| Qwen3-0.6B-MLX-bf16 | 0.6 | Micro (<2B) | Dense | text-generation | 6 |
| Qwen3-8B-MLX-6bit | 8.0 | Small (2-8B) | Dense | text-generation | 6 |
| Qwen3-235B-A22B-MLX-bf16 | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 6 |
| Qwen3-14B-MLX-bf16 | 14.0 | Medium (8-35B) | Dense | text-generation | 6 |
| SAE-Res-Qwen3-8B-Base-W64K-L0_50 | 8.0 | Small (2-8B) | Dense | - | 6 |
| SAE-Res-Qwen3-8B-Base-W64K-L0_100 | 8.0 | Small (2-8B) | Dense | - | 6 |
| Qwen3-0.6B-MLX-8bit | 0.6 | Micro (<2B) | Dense | text-generation | 5 |
| Qwen3-4B-MLX-bf16 | 4.0 | Small (2-8B) | Dense | text-generation | 5 |
| Qwen3-14B-MLX-8bit | 14.0 | Medium (8-35B) | Dense | text-generation | 5 |
| Qwen3-30B-A3B-MLX-6bit | 30.0 | Medium (8-35B) | MoE (A3B) | text-generation | 5 |
| SAE-Res-Qwen3.5-2B-Base-W32K-L0_100 | 2.0 | Small (2-8B) | Dense | - | 5 |
| Qwen3-1.7B-MLX-4bit | 1.7 | Micro (<2B) | Dense | text-generation | 4 |
| Qwen3-14B-MLX-6bit | 14.0 | Medium (8-35B) | Dense | text-generation | 4 |
| Qwen3-4B-MLX-6bit | 4.0 | Small (2-8B) | Dense | text-generation | 4 |
| Qwen3-32B-MLX-6bit | 32.0 | Medium (8-35B) | Dense | text-generation | 4 |
| Qwen3-235B-A22B-MLX-6bit | 235.0 | XLarge (>100B) | MoE (A22B) | text-generation | 4 |
| SAE-Res-Qwen3-1.7B-Base-W32K-L0_50 | 1.7 | Micro (<2B) | Dense | - | 4 |
| SAE-Res-Qwen3-30B-A3B-Base-W128K-L0_100 | 30.0 | Medium (8-35B) | MoE (A3B) | - | 4 |
| Qwen3-1.7B-MLX-6bit | 1.7 | Micro (<2B) | Dense | text-generation | 3 |
| Qwen3-1.7B-MLX-8bit | 1.7 | Micro (<2B) | Dense | text-generation | 3 |
| Qwen3-4B-MLX-8bit | 4.0 | Small (2-8B) | Dense | text-generation | 3 |
| SAE-Res-Qwen3-1.7B-Base-W32K-L0_100 | 1.7 | Micro (<2B) | Dense | - | 3 |
| SAE-Res-Qwen3-30B-A3B-Base-W32K-L0_50 | 30.0 | Medium (8-35B) | MoE (A3B) | - | 3 |
| Qwen3-VL-235B-A22B-Thinking-GGUF | 235.0 | XLarge (>100B) | MoE (A22B) | image-text-to-text | 1 |

### Qwen3.5

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| Qwen3.5-9B | 9.0 | Medium (8-35B) | Dense | image-text-to-text | 1658 |
| Qwen3.5-397B-A17B | 397.0 | XLarge (>100B) | MoE (A17B) | image-text-to-text | 1526 |
| Qwen3.5-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 1455 |
| Qwen3.5-27B | 27.0 | Medium (8-35B) | Dense | image-text-to-text | 996 |
| Qwen3.5-4B | 4.0 | Small (2-8B) | Dense | image-text-to-text | 713 |
| Qwen3.5-0.8B | 0.8 | Micro (<2B) | Dense | image-text-to-text | 605 |
| Qwen3.5-122B-A10B | 122.0 | XLarge (>100B) | MoE (A10B) | image-text-to-text | 581 |
| Qwen3.5-2B | 2.0 | Small (2-8B) | Dense | image-text-to-text | 323 |
| Qwen3.5-397B-A17B-FP8 | 397.0 | XLarge (>100B) | MoE (A17B) | image-text-to-text | 181 |
| Qwen3.5-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 152 |
| Qwen3.5-27B-FP8 | 27.0 | Medium (8-35B) | Dense | image-text-to-text | 135 |
| Qwen3.5-35B-A3B-Base | 35.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 134 |
| Qwen3.5-122B-A10B-FP8 | 122.0 | XLarge (>100B) | MoE (A10B) | image-text-to-text | 107 |
| Qwen3.5-35B-A3B-GPTQ-Int4 | 35.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 91 |
| Qwen3.5-9B-Base | 9.0 | Medium (8-35B) | Dense | image-text-to-text | 89 |
| Qwen3.5-0.8B-Base | 0.8 | Micro (<2B) | Dense | image-text-to-text | 83 |
| Qwen3.5-2B-Base | 2.0 | Small (2-8B) | Dense | image-text-to-text | 78 |
| Qwen3.5-4B-Base | 4.0 | Small (2-8B) | Dense | image-text-to-text | 72 |
| Qwen3.5-27B-GPTQ-Int4 | 27.0 | Medium (8-35B) | Dense | image-text-to-text | 57 |
| Qwen3.5-122B-A10B-GPTQ-Int4 | 122.0 | XLarge (>100B) | MoE (A10B) | image-text-to-text | 42 |
| Qwen3.5-397B-A17B-GPTQ-Int4 | 397.0 | XLarge (>100B) | MoE (A17B) | image-text-to-text | 35 |

### Qwen3.6

| Model | Size (B) | Tier | Arch | Pipeline | Likes |
| --- | --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B | 35.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 2319 |
| Qwen3.6-27B | 27.0 | Medium (8-35B) | Dense | image-text-to-text | 1878 |
| Qwen3.6-35B-A3B-FP8 | 35.0 | Medium (8-35B) | MoE (A3B) | image-text-to-text | 299 |
| Qwen3.6-27B-FP8 | 27.0 | Medium (8-35B) | Dense | image-text-to-text | 298 |

---

*Report generated from 458 Qwen models on HuggingFace Hub.*
*Classification is based on model naming conventions, tags, and pipeline metadata.*