# arXiv AI — Monday, 16 November 2026 — 5 papers

Today’s report uses the prior announcement batch: the latest arXiv category pages show Monday, 16 November, not a 17 November batch. The strongest attention signal in this small selected set is for long-horizon agents and multimodal systems; we’ll cover embodied robotics, a game-playing VLA agent, faster vision-language decoding, query memory, and pixel-space video generation. arXiv has no official trending chart, so this ordering is inferred from dated Hugging Face Daily Papers upvotes; citation evidence is limited for these recent papers.

## Top papers (ranked)

### 1. [Envisioning Agentic Robotics: A New Era of Robotic Systems](https://arxiv.org/abs/2611.18359)
- **Abstract:** The authors frame agentic robotics as foundation models coordinating skills and tools in a closed loop, and propose an evaluation framework and roadmap toward sustained physical autonomy.
- **Authors:** Qingfeng Lan, Duo Li, Siyao Li, Yiheng Lyu, Shijian Lu, et al.
- **arXiv:** `2611.18359v1` (published 2026-11-13T16:07:26Z; categories: `cs.RO`, `cs.AI`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** Ranked first among the selected papers: the 2026-11-16 Trending AI Today archive records 42 Hugging Face Daily Papers upvotes at 07:00 UTC, the highest count in that day's list. The paper is cross-listed in four configured AI/robotics categories.
- **Claimed contribution:** The authors propose “Embodied System 2” (a foundation model plus embodied harness) as the decision-making core, with an evaluation framework distinguishing model capability from closed-loop system performance.
- **Caveat:** This is a perspective and synthesis, not a new robot-system experiment; the authors note reviewed benchmark settings differ and some simulations pause while models deliberate, limiting direct comparisons.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Robotics & control; Agents & reasoning; Evaluation & benchmarks

### 2. [Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://arxiv.org/abs/2611.18397)
- **Abstract:** The authors describe an agent combining large-scale keyboard-and-mouse pretraining, sparse-reasoning instruction tuning, multi-turn reinforcement learning, memory, and real-time serving, and report competitive performance across selected 3D and 2D games.
- **Authors:** Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, et al.
- **arXiv:** `2611.18397v1` (published 2026-11-13T16:39:30Z; categories: `cs.CL`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Ranked second among the selected papers: the 2026-11-16 Trending AI Today archive records 36 Hugging Face Daily Papers upvotes at 07:00 UTC; its cross-list spans language, AI, and vision.
- **Claimed contribution:** The authors combine cross-game interaction data and training with a shared perception-memory-reasoning-control pipeline, reporting long-horizon game results and a cloud-edge inference system for real-time play.
- **Caveat:** The authors say evaluation covers selected environments and task structures; transfer depends on training-data coverage, and the paper identifies lower serving cost and deeper deliberation as remaining issues.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Agents & reasoning; Multimodal & vision-language; Training & adaptation

### 3. [MMFlash: Faster Speculative Decoding for Vision-Language Models](https://arxiv.org/abs/2611.18482)
- **Abstract:** The authors measure how visual dependence reduces draft-token acceptance, then propose adaptively upweighting visually dependent tokens and using sparse attention for long videos; they report lossless decoding speedups up to 3.58×.
- **Authors:** Sicheng Feng, Zigeng Chen, Song Wang, Gongfan Fang, Xinchao Wang
- **arXiv:** `2611.18482v1` (published 2026-11-13T17:54:28Z; categories: `cs.CV`)
- **Evidence for ranking:** Ranked third among the selected papers: 20 Hugging Face Daily Papers upvotes in the dated 2026-11-16 archive at 07:00 UTC; the archive also links a code release.
- **Claimed contribution:** The authors’ visually aware diffusion drafter reweights tokens using a visual-dependence measure and adds sparse attention for video; tests cover seven image and three video benchmarks, two VLM sizes, and multiple serving settings.
- **Caveat:** The authors state that long-video drafting remains harder than image drafting; their video approach uses a simple sparse-attention pattern and lightweight fine-tuning rather than a video-specialized drafter.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Efficient inference & systems; Multimodal & vision-language; Training & adaptation

### 4. [MEM-SQL: Memory-Empowered Text-to-SQL](https://arxiv.org/abs/2611.18338)
- **Abstract:** The authors introduce HARE, a 1,600-request benchmark for reusing prior SQL, and MEM-SQL, which stores query templates, SQL blocks, and schema mappings; across six language models they report higher execution accuracy with fewer tokens and lower latency than direct generation.
- **Authors:** Xiaoqi Wang, Wenqi Pei, Shizheng Hou, Yilai Liu, Han Chen, et al.
- **arXiv:** `2611.18338v1` (published 2026-11-13T15:49:41Z; categories: `cs.DB`)
- **Evidence for ranking:** Ranked fourth among the selected papers: the 2026-11-16 Trending AI Today archive records 11 Hugging Face Daily Papers upvotes at 07:00 UTC. Although its primary category is `cs.DB`, the abstract is explicitly about LLM-based text-to-SQL, so it qualifies as an unambiguous AI contribution under this report’s scope.
- **Claimed contribution:** The authors present a history-aware benchmark and a layered memory method with on-demand schema linking; they report mean execution accuracy rising from 37.1% to 50.0%, alongside reduced input tokens and latency.
- **Caveat:** The authors report that accuracy drops from 56.7% to 29.7% when several verified queries must be recombined, particularly when reused pieces need a new query structure or shared join.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Retrieval & knowledge; Evaluation & benchmarks

### 5. [JVT: Just Video Transformer makes pixel-space video diffusion simple](https://arxiv.org/abs/2611.18549)
- **Abstract:** The authors propose a large-patch DiT-style Transformer for pixel-space video diffusion without a pretrained autoencoder or cascaded stages, reporting quality competitive with latent-diffusion baselines and camera-conditioned RGB-disparity generation.
- **Authors:** Jianjun Zhou, Hua Geng, Haoyu Guo
- **arXiv:** `2611.18549v1` (published 2026-11-13T18:55:25Z; categories: `cs.CV`)
- **Evidence for ranking:** Ranked fifth among the selected papers: the 2026-11-16 Trending AI Today archive records 9 Hugging Face Daily Papers upvotes at 07:00 UTC and links a code release.
- **Claimed contribution:** The authors use a simple pixel-space video Transformer and ablate patch embeddings, register tokens, and adaptive layer normalization; the abstract reports class-conditioned and unconditional video results plus a camera-conditioned RGB-disparity demonstration.
- **Caveat:** The abstract’s evaluation is limited to those generation settings and the camera-conditioned demonstration; it does not establish performance across broader video-generation tasks.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Multimodal & vision-language

## Trending Research Themes

- **Long-horizon agents are a shared topic, but not yet a single methodological shift.** Envisioning Agentic Robotics argues for a system-level foundation-model-plus-harness view of physical autonomy; Gamer reports a trained perception, memory, and control stack in selected games. One is a perspective and the other an empirical agent paper, so this pair signals attention to sustained interaction, not established general-purpose autonomy.
- **Multimodal systems work spans both capability and efficiency.** Gamer targets real-time interaction, while MMFlash reduces VLM decoding cost and JVT simplifies pixel-space video diffusion. These are distinct technical problems; the common thread is end-to-end operation over visual or video inputs.
- **Memory is being operationalized for structured reuse.** MEM-SQL’s HARE benchmark tests when historical queries can be reused, a narrower, database-centered signal rather than evidence of a broad agent-memory trend.
- **The five selected papers are category-diverse:** two have primary category `cs.CV`, and one each `cs.RO`, `cs.CL`, and `cs.DB`; only two cross-list to `cs.AI`. This is an attention-selected slice, not a representative distribution of all 404 unique papers in the eight-category batch.

## Open Problems and Research Directions

- **Author-stated — Envisioning Agentic Robotics:** Existing benchmarks cover too little responsibility, space, and time, while simulated rankings have not been established on real robots. A follow-up could evaluate sustained, multi-task workflows on hardware, with live timing, failure recovery, and success-latency-cost reporting.
- **Author-stated — Gamer:** The evaluated environment and task set are selected, data composition affects transfer, and serving cost and deeper deliberation remain constraints. Test broader held-out environments and measure whether cheaper serving or hierarchical fast/slow reasoning preserves long-horizon success.
- **Author-stated — MMFlash:** Long-video drafting remains difficult. Test question-conditioned frame selection or context compression and compare frame-level visual-dependence signals against the current sparse-attention approach.
- **Evidence boundary — MEM-SQL and JVT:** MEM-SQL’s harder multi-query recombination remains a bottleneck; JVT’s abstract reports a limited set of video-generation settings. Follow-up work could stress-test more complex SQL compositions and evaluate JVT across additional conditioning modes and downstream video tasks.

## Takeaway

The strongest attention signal in this batch points to agents that sustain interaction and systems that make multimodal workloads more practical. The evidence is still bounded: one paper is a roadmap, agent results cover selected environments, and the reported decoding and video-generation gains need broader replication.

## Method and sources

- **Window:** daily announcement batch 2026-11-16 only (start date 2026-11-16; end date 2026-11-16). Snapshot time: 2026-11-17 01:10:12 UTC. The latest category pages showed Monday 16 November and no 17 November batch, so this report uses the prior batch. The five first-submission timestamps appear on the individual arXiv pages; all were announced in the Nov 16 batch.
- **Scope/query:** `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`. The full latest batch was checked across all eight category recent pages: 404 unique versionless IDs after deduplicating cross-lists (557 category entries). Four papers have a primary or cross-listed category in the configured corpus; MEM-SQL is included because its LLM-based text-to-SQL contribution is explicit. Each selected paper’s arXiv abstract page and announcement listing were verified.
- **Inference:** Ranking is inferred, not supplied by arXiv. Among eligible papers in the dated batch, the selected order follows the recorded Hugging Face Daily Papers vote counts shown in the 2026-11-16 Trending AI Today archive (snapshot 07:00 UTC): 42, 36, 20, 11, and 9 upvotes. These are attention signals, not citations, downloads, or period gains. No older paper or revision outside the Nov 16 batch was included merely because it appeared higher in the daily vote list.
- **Sources:** [Trending AI Today — Nov 16 archive](https://trendingai.today/2026-11-16/); arXiv category listings: [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent). Each entry links to its verified arXiv abstract page; the top three were also checked in arXiv HTML for results or limitations.
- **Retrieval notes:** The broad arXiv export API and batched Semantic Scholar Graph query did not return usable data during this run. Category recent pages and individual arXiv abstract pages were used to verify the batch and metadata; no citation counts were used in ranking.
