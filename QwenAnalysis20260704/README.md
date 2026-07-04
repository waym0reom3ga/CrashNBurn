# Qwen Models Analysis — July 4, 2026

Complete classification and completeness audit of all Qwen models on HuggingFace Hub.

## Files

| File | Size | Description |
|------|------|-------------|
| `qwen_models_classification.md` | 181K | Full taxonomy: 458 models classified by family, capability, architecture, and size tier |
| `qwen_models_audit.md` | 9.6K | Completeness audit: cross-referenced against GitHub repos, papers, READMEs — found 11 missing/expected models |
| `qwen_models_full.json` | 221K | Raw HuggingFace API data (all model metadata) |
| `qwen_models_index.txt` | 87K | Quick-reference index of all 458 models |

## Key Findings

- **458 total models** across the Qwen organization on HuggingFace
- **Qwen3 dominates** with 183 models (40% of catalog)
- **Core families complete**: Qwen1.5 through Qwen2.5-Coder have full Base/Instruct pairs
- **11 missing models identified**: Qwen-VLA, RobotNav, RobotManip, 4x TTS-25Hz variants, and several expected Instruct/Thinking variants for Qwen3.5/Qwen3.6

## Methodology

Data sourced from HuggingFace Hub API (`https://huggingface.co/api/models?author=Qwen`). Cross-referenced against QwenLM GitHub organization repos, official READMEs, arXiv papers, and naming pattern analysis.
