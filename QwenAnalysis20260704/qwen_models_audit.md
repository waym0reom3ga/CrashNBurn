# Qwen HuggingFace Catalog Completeness Audit

**Date:** 2026-07-04  
**Source HF listing:** 458 models from `qwen_models_full.json`  
**Cross-referenced against:** GitHub repos (QwenLM org), official READMEs, arXiv papers, qwen.ai blog metadata  

---

## Executive Summary

The Qwen HuggingFace catalog of 458 models is **substantially complete** for the core LLM families (Qwen2, Qwen2.5, Qwen3 dense/MoE), but several announced or documented models are **missing from HF**. The most significant gaps involve newer specialized models (VLA, TTS-25Hz) and quantization format coverage for recent releases.

---

## 1. Confirmed Missing Models (Announced/Documented but Not on HF)

### HIGH CONFIDENCE — Officially announced with GitHub repos/papers

| Model | Source | Status |
|-------|--------|--------|
| **Qwen-VLA** | [GitHub](https://github.com/QwenLM/Qwen-VLA), [arXiv 2605.30280](https://arxiv.org/abs/2605.30280), qwen.ai blog | ❌ Not on HF — has repo, paper, demo video, but no model weights uploaded to Qwen org |
| **Qwen-RobotNav** | [GitHub](https://github.com/QwenLM/Qwen-RobotNav) | ❌ Not on HF — dedicated repo exists |
| **Qwen-RobotManip** | [GitHub](https://github.com/QwenLM/Qwen-RobotManip) | ❌ Not on HF — dedicated repo exists |

### HIGH CONFIDENCE — Documented in official READMEs with benchmark tables

| Model | Source | Status |
|-------|--------|--------|
| **Qwen3-TTS-25Hz-0.6B-Base** | [Qwen3-TTS README](https://github.com/QwenLM/Qwen3-TTS) — benchmark table includes it | ❌ Not on HF — only 12Hz variants exist |
| **Qwen3-TTS-25Hz-1.7B-Base** | Same as above, with explicit benchmark comparisons vs 12Hz | ❌ Not on HF |
| **Qwen3-TTS-25Hz-1.7B-CustomVoice** | README benchmark table (L912) | ❌ Not on HF |
| **Qwen-TTS-Tokenizer-25Hz** | README tokenizer comparison table (L1219, L1228) — two stages mentioned | ❌ Not on HF — only 12Hz tokenizer exists |

### MEDIUM CONFIDENCE — Expected by naming pattern / referenced in docs

| Model | Reasoning | Status |
|-------|-----------|--------|
| **Qwen3-Next-80B-A3B-Base** | Qwen3-Coder README explicitly references `Qwen3-Next-80B-A3B-Base` as the foundation for Qwen3-Coder-Next. Instruct and Thinking variants exist on HF, but Base is absent. | ❌ Likely missing — referenced in official docs |
| **Qwen3.5-*-Instruct / Qwen3.5-*-Thinking** | All prior Qwen generations (Qwen2, Qwen2.5, Qwen3) have Instruct/Thinking variants. Qwen3.5 has 8 model sizes on HF but ZERO Instruct or Thinking versions. README doesn't mention them yet — may be upcoming. | ⚠️ Possibly not yet released |
| **Qwen3.6-*-Instruct / Qwen3.6-*-Thinking** | Same pattern as above. Two models (27B, 35B-A3B) on HF with no Instruct/Thinking variants. README mentions "User Guide, coming soon." | ⚠️ Possibly not yet released |

---

## 2. Naming Pattern Gaps

### Qwen3 Dense Model Sizes
- **Available:** 0.6B, 1.7B, 4B, 8B, 14B, 32B (dense) + 30B-A3B, 235B-A22B (MoE)
- **Pattern analysis:** The progression 0.6 → 1.7 → 4 → 8 → 14 → 32 follows a ~2x scaling pattern. No obvious gaps in the dense lineup.
- **Note:** Qwen3-32B has no `-Base` variant (unlike 0.6B, 1.7B, 4B, 8B, 14B). The `Qwen3-32B` model itself may serve as the base.

### Qwen3 MoE Model Sizes
- **Available:** 30B-A3B (3B active), 235B-A22B (22B active)
- **Pattern analysis:** Two-tier MoE coverage seems intentional (mid-size + flagship). No obvious missing sizes.

### Qwen3.5 Model Sizes
- **Available:** 0.8B, 2B, 4B, 9B (dense) + 27B, 35B-A3B, 122B-A10B, 397B-A17B (MoE/hybrid)
- **Pattern analysis:** Dense sizes follow ~2x scaling. MoE lineup is extensive. No obvious gaps in announced sizes.

### Qwen3-VL Model Sizes
- **Available:** 2B, 4B, 8B, 32B (dense) + 30B-A3B, 235B-A22B (MoE)
- **Pattern analysis:** Mirrors Qwen3 LLM lineup. Complete.

### Qwen2.5 Model Sizes
- **Available:** 0.5B, 1.5B, 3B, 7B, 14B, 32B, 72B
- **Pattern analysis:** Standard progression. Complete.

---

## 3. Base/Instruct Pair Completeness Check

### ✅ Complete Families (all base/instruct pairs present)

| Family | Sizes | Status |
|--------|-------|--------|
| Qwen1.5 | 0.5B, 1.8B, 4B, 7B, 14B, 32B, 72B, 110B | ✓ All Base+Chat pairs |
| Qwen2 | 0.5B, 1.5B, 7B, 57B-A14B, 72B | ✓ All Base+Instruct pairs |
| Qwen2-Math | 1.5B, 7B, 72B | ✓ All Base+Instruct pairs |
| Qwen2.5 | 0.5B, 1.5B, 3B, 7B, 14B, 32B, 72B | ✓ All Base+Instruct pairs |
| Qwen2.5-Math | 1.5B, 7B, 72B | ✓ All Base+Instruct pairs |
| Qwen2.5-Coder | 0.5B, 1.5B, 3B, 7B, 14B, 32B | ✓ All Base+Instruct pairs |
| Qwen2-VL | 2B, 7B, 72B | ✓ All Base+Instruct pairs |
| Qwen2-Audio | 7B | ✓ Base+Instruct pair |
| Qwen3 (dense) | 0.6B, 1.7B, 4B, 8B, 14B | ✓ All have `-Base` variants |
| Qwen3-VL | 2B, 4B, 8B, 32B, 30B-A3B, 235B-A22B | ✓ All Instruct+Thinking pairs |

### ⚠️ Partial/Incomplete Families

| Family | Gap | Details |
|--------|-----|---------|
| Qwen3 MoE | Base model for 235B-A22B | `Qwen3-235B-A22B` exists (likely base), Instruct-2507 and Thinking-2507 present. No explicit `-Base` suffix variant. |
| Qwen3 MoE | Base model for 30B-A3B | Has `-Base`, `Instruct-2507`, `Thinking-2507`. Complete. |
| Qwen3-Next | Missing Base | Instruct and Thinking variants exist; `Qwen3-Next-80B-A3B-Base` referenced in docs but absent from HF. |
| Qwen3.5 | No Instruct/Thinking | All 8 sizes have base models only. May be intentional (API-only instruct) or upcoming releases. |
| Qwen3.6 | No Instruct/Thinking | Both sizes (27B, 35B-A3B) are base-only. README says "User Guide, coming soon." |

---

## 4. Quantization Format Gaps

### Qwen3 Dense Models — Quantization Coverage Matrix

| Size | GGUF | AWQ | GPTQ-Int8 | FP8 | MLX-bf16 |
|------|------|-----|-----------|-----|----------|
| 0.6B | ✓ | ✗ | ✓ | ✓ | ✓ |
| 1.7B | ✓ | ✗ | ✓ | ✓ | ✓ |
| 4B | ✓ | ✓ | ✗ | ✓ | ✓ |
| 8B | ✓ | ✓ | ✗ | ✓ | ✓ |
| 14B | ✓ | ✓ | ✗ | ✓ | ✓ |
| 32B | ✓ | ✓ | ✗ | ✓ | ✓ |

**Pattern:** Small models (0.6B, 1.7B) have GPTQ-Int8 but no AWQ. Larger models have AWQ but no GPTQ-Int8. This appears intentional — different quantization strategies for different size tiers. No clear "missing" formats.

### Qwen3 MoE Models — Quantization Coverage Matrix

| Model | GGUF | AWQ | GPTQ-Int4 | FP8 | MLX-bf16 |
|-------|------|-----|-----------|-----|----------|
| 30B-A3B | ✓ | ✗ | ✓ | ✓ | ✓ |
| 235B-A22B | ✓ | ✗ | ✓ | ✓ | ✓ |

**Gap:** No AWQ for MoE models. May be intentional (MoE quantization complexity).

### Qwen3.5 Models — Quantization Coverage Matrix

| Model | GGUF | FP8 | GPTQ-Int4 | AWQ | MLX |
|-------|------|-----|-----------|-----|-----|
| 0.8B | ✗ | ✗ | ✗ | ✗ | ✗ |
| 2B | ✗ | ✗ | ✗ | ✗ | ✗ |
| 4B | ✗ | ✗ | ✗ | ✗ | ✗ |
| 9B | ✗ | ✗ | ✗ | ✗ | ✗ |
| 27B | ✗ | ✓ | ✓ | ✗ | ✗ |
| 35B-A3B | ✗ | ✓ | ✓ | ✗ | ✗ |
| 122B-A10B | ✗ | ✓ | ✓ | ✗ | ✗ |
| 397B-A17B | ✗ | ✓ | ✓ | ✗ | ✗ |

**Significant gap:** Qwen3.5 models have **zero GGUF support** across all sizes, and the four dense models (0.8B–9B) have no quantization at all. Only FP8 and GPTQ-Int4 for larger MoE/hybrid models. This is a notable coverage gap compared to prior generations.

### Qwen3-VL Models — Quantization Coverage Matrix

| Size | FP8 | GGUF |
|------|-----|------|
| 2B | ✓ | ✓ |
| 4B | ✓ | ✓ |
| 8B | ✓ | ✓ |
| 32B | ✓ | ✓ |
| 30B-A3B | ✓ | ✓ |
| 235B-A22B | ✓ | ✓ |

**Complete:** All VL models have FP8 and GGUF for both Instruct and Thinking variants.

---

## 5. Summary of Findings by Confidence Level

### 🔴 HIGH CONFIDENCE — Missing (7 items)
Models that are documented in official sources but absent from HF:

1. **Qwen-VLA** — Full GitHub repo, arXiv paper, blog post, demo video; no weights on HF
2. **Qwen-RobotNav** — Dedicated GitHub repo; no weights on HF  
3. **Qwen-RobotManip** — Dedicated GitHub repo; no weights on HF
4. **Qwen3-TTS-25Hz-0.6B-Base** — In official benchmark tables
5. **Qwen3-TTS-25Hz-1.7B-Base** — In official benchmark tables with explicit comparisons
6. **Qwen3-TTS-25Hz-1.7B-CustomVoice** — In official benchmark tables
7. **Qwen-TTS-Tokenizer-25Hz** — Referenced in tokenizer comparison table

### 🟡 MEDIUM CONFIDENCE — Likely Missing (4 items)
Models expected by pattern or referenced but not confirmed as released:

8. **Qwen3-Next-80B-A3B-Base** — Explicitly named in Qwen3-Coder README as foundation model
9. **Qwen3.5-*-Instruct** (all 8 sizes) — Pattern suggests these should exist; may be API-only or upcoming
10. **Qwen3.5-*-Thinking** (all 8 sizes) — Same reasoning
11. **Qwen3.6-*-Instruct/Thinking** (2 sizes × 2 variants = 4 models) — README says "User Guide, coming soon"

### 🟢 LOW CONFIDENCE — Possible Gaps (format coverage)
Quantization format gaps that may be intentional:

- Qwen3.5: No GGUF for any size; no quantization for dense models (0.8B–9B)
- Qwen3 MoE: No AWQ variants
- Qwen3 0.6B/1.7B: No AWQ (larger sizes have it)

---

## 6. Methodology Notes

- **HF data source:** `/home/waymore/qwen_models_full.json` — 458 models from the Qwen organization on HuggingFace
- **GitHub repos checked:** All 43+ repos in `github.com/QwenLM` org (via GitHub API)
- **READMEs analyzed:** Qwen3, Qwen3-VL, Qwen3-Coder, Qwen3-Omni, Qwen3-TTS, Qwen3-ASR, Qwen3.6, Qwen-VLA, Qwen3Guard, Qwen-Image
- **arXiv papers referenced:** 2605.30280 (Qwen-VLA), 2601.15621 (Qwen3-TTS), 2509.17765 (Qwen3-Omni)
- **Limitations:** Could not access qwen.ai blog content directly (SPA-rendered). HF API search requires authentication, so direct model existence checks for unlisted models were not possible. Some "missing" models may exist under different naming conventions or on ModelScope only.
