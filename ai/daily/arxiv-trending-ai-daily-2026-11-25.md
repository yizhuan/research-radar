# AI on arXiv — 2026-11-25 announcement batch — 5 notable papers

The strongest recurring pattern in this shortlist is better evaluation of agent and multimodal behavior: papers audit shortcuts and calibration, then test training or memory methods against measurable outcomes. Listen for evaluation quality, verifiable agent training, and compact agent state. This is an inferred ranking, not an official arXiv trending chart; direct attention and citation evidence are sparse for this very recent batch.

## Top papers (ranked)

### 1. [LUCID: Statistically Grounded Self-Correction for LLM Reasoning Evaluation](https://arxiv.org/abs/2611.31595)
- **Abstract:** LUCID combines prompt-based self-correction with design-based supervised learning to calibrate LLM ratings of reasoning steps, reporting improved calibration and downstream selection on several reasoning domains.
- **Authors:** Satiyabooshan Murugaboopathy, Adel Daoud, Connor T. Jerzak
- **arXiv:** `2611.31595v1` (published 2026-11-23 21:40:54 UTC; categories: `cs.CL` (primary), `cs.LG`, `stat.ME`)
- **Evidence for ranking:** Collector score 2.579, the highest in the supplied candidate list; Hugging Face Papers marked it featured on 2026-11-24 (1 upvote, 2 comments), and it has 2 cross-list categories. It is the only candidate with a recorded direct-attention signal in the collector; this is a small signal, not evidence of broad popularity. [Hugging Face Papers](https://huggingface.co/papers/2611.31595)
- **Claimed contribution:** The paper introduces LUCID and Design-based Supervised Learning (DSL); its abstract reports that LUCID narrows GPT-5-mini's calibration gap on PRM800K from 7.8 to 0.9 percentage points in one pass.
- **Caveat:** The authors state that prompt feedback shifts rating thresholds without improving class-balanced sound/unsound discrimination, leaving residual false alarms; supervised fine-tuning can outperform it when open weights are available and discrimination is the priority.
- **Announcement type:** new submission, announcement-batch date 2026-11-25
- **Themes:** Evaluation & benchmarks; Training & adaptation

### 2. [ASTERISM: Do Multimodal LLMs Actually Look at All the Images?](https://arxiv.org/abs/2611.32316)
- **Abstract:** An audit of 19 multi-image benchmarks finds many items solvable from one image, and ASTERISM filters these shortcuts while proposing cross-image credit assignment for multimodal model training.
- **Authors:** Chanseul Cho, Dongwoo Kim, Noori Bae, Seungjae Moon, Seongsu Lee, Youngmin Ro
- **arXiv:** `2611.32316v1` (published 2026-11-24 10:12:44 UTC; categories: `cs.CV` (primary), `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Collector score 0.75, entirely from 3 cross-list categories; it has no recorded Hugging Face or Hacker News attention signal. Its core-AI cross-listing and recent placement support inclusion, not a popularity claim.
- **Claimed contribution:** The paper presents ASTERISM, an 18.7K-item audited multi-image benchmark, and cross-image credit assignment (CICA); the authors report 2.6–6.0 point gains over the base models on three open-source MLLMs.
- **Caveat:** The authors say the benchmark's domains and task mix inherit the 19 source datasets; CICA's main comparison uses three backbones, with larger multimodal models left for future work.
- **Announcement type:** new submission, announcement-batch date 2026-11-25
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Training & adaptation

### 3. [Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models](https://arxiv.org/abs/2611.31821)
- **Abstract:** The paper studies supervised fine-tuning and reinforcement learning with verifiable rewards on three social games, reporting stronger Qwen3 play on trained games and transfer to three held-out games.
- **Authors:** Keyu He, Michael Li, Jiarui Liu, Mingqian Zheng, Koichi Onoue et al.
- **arXiv:** `2611.31821v1` (published 2026-11-24 02:15:30 UTC; categories: `cs.CL` (primary), `cs.AI`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Collector score 0.75 from 3 cross-list categories, including `cs.AI`, `cs.LG`, and `cs.MA`; no paper-specific Hugging Face or Hacker News attention was recorded. It is included as a core-AI agent-training study among equally scored cross-listed candidates.
- **Claimed contribution:** The authors use rule-decided social-game outcomes as a training reward; their abstract reports Qwen3-4B's win rate rising from 33% to 81% on trained games and from 39% to 54% on three held-out games against Gemma-3-27B.
- **Caveat:** The authors limit training to three hidden-role games, one opponent, and the Qwen3 family; they also report no human evaluation and note that transfer varies across game types and opponents.
- **Announcement type:** new submission, announcement-batch date 2026-11-25
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 4. [Learning Compact State Abstractions for LLM Agents](https://arxiv.org/abs/2611.31800)
- **Abstract:** The authors search for inspectable recursive programs that compress interaction histories while preserving an agent's task performance, reporting substantially shorter inputs on ALFWorld and ScienceWorld.
- **Authors:** Yaswanth Chittepu, Raghavendra Addanki, Anup Rao, Branislav Kveton, Scott Niekum
- **arXiv:** `2611.31800v1` (published 2026-11-24 01:52:56 UTC; categories: `cs.LG` (primary), `cs.AI`, `cs.CL`, `cs.NE`)
- **Evidence for ranking:** Collector score 0.75 from 3 cross-list categories, including `cs.AI`, `cs.CL`, and `cs.NE`; no paper-specific direct-attention signal was recorded. Included among the equally scored cross-listed candidates for its concrete agent-memory and input-efficiency result.
- **Claimed contribution:** The paper defines state sufficiency by task performance and uses an LLM-guided genetic algorithm to discover deterministic recursive state programs; its abstract reports input reductions of up to 71% on ALFWorld and 57% on ScienceWorld while preserving near-reference success.
- **Caveat:** The abstract's reported evidence is confined to ALFWorld and ScienceWorld, so performance and robustness in other tasks or deployment settings remain unestablished here.
- **Announcement type:** new submission, announcement-batch date 2026-11-25
- **Themes:** Agents & reasoning; Efficient inference & systems

### 5. [GoldiBench: Right Tools, Wrong Amount -- Benchmarking Agents on Effect Judgement in Professional Editing](https://arxiv.org/abs/2611.31590)
- **Abstract:** GoldiBench tests whether agents can infer the right magnitude of edits from visual goals across five professional applications, finding a sharp gap between executing known settings and choosing settings from the desired effect.
- **Authors:** Wang Yang, Xinpeng Li, Yanyan Zhang, Chaoda Song, Shouren Wang et al.
- **arXiv:** `2611.31590v1` (published 2026-11-23 21:37:22 UTC; categories: `cs.CV` (primary), `cs.AI`, `cs.CL`, `cs.SE`)
- **Evidence for ranking:** Collector score 0.75 from 3 cross-list categories, including `cs.AI` and `cs.CL`; no paper-specific Hugging Face or Hacker News attention was recorded. It is included from the equal-score group for its direct, target-image-based measurement of an agent capability gap.
- **Claimed contribution:** The paper introduces 500 target-rendered editing tasks across darktable, RawTherapee, GIMP, Inkscape, and Blender; its abstract reports that the best model passes 19% of program-based tasks when given tools but not their magnitudes.
- **Caveat:** The measured scope is 500 tasks in five applications, and the reported results do not establish whether the same effect-judgment gap holds across other tools or real-world workflows.
- **Announcement type:** new submission, announcement-batch date 2026-11-25
- **Themes:** Agents & reasoning; Evaluation & benchmarks

## Trending Research Themes

- **Evaluation is becoming diagnostic rather than just aggregate.** LUCID isolates rater calibration from discrimination; ASTERISM tests whether multi-image benchmarks truly require multiple images; GoldiBench separates tool execution from estimating effect magnitude. Together, these papers make task validity and failure mode measurement central, but three examples do not establish a field-wide methodological shift.
- **Verifiable rewards are being tested on richer agent behavior.** The social-games study uses game outcomes to train coordination and hidden-role play; ASTERISM's CICA instead reallocates reward toward image-dependent tokens. The shared idea is reward design tied to the behavior a task is meant to measure, while the settings and evidence differ.
- **Agent capability is being paired with resource and interaction constraints.** Compact state abstractions target input growth, while GoldiBench reveals that tool knowledge does not guarantee calibrated action magnitude. A useful intersection is evaluating whether compressed-memory agents also inspect, compare, and revise tool effects; that intersection is a proposed synthesis, not a result reported by either paper.
- **Category coverage is broad in the source query, but the serialized candidate list is concentrated.** Among its 150 stored candidates, `cs.CV` and `cs.LG` are the most frequent primary categories (39 and 33 entries respectively). The five-paper shortlist deliberately includes language and agent work, so it should not be read as a proportional sample of arXiv activity.

## Open Problems and Research Directions

- **Author-stated — calibration versus discrimination:** LUCID's prompt feedback changes thresholds without sharpening class-balanced separation and can leave false alarms. Test when a calibration pass helps versus when supervised adaptation is needed, and evaluate the choice using balanced-class measures as well as aggregate accuracy. ([LUCID](https://arxiv.org/abs/2611.31595))
- **Author-stated — benchmark coverage and training scale:** ASTERISM inherits domains from 19 source benchmarks and leaves larger MLLMs for future work. Extend the audited item pool to new domains, then repeat CICA comparisons across larger backbones and multiple training seeds. ([ASTERISM](https://arxiv.org/abs/2611.32316))
- **Author-stated — transfer and deception in social play:** The social-games paper uses three hidden-role games, one opponent, and no human evaluation; the authors warn that outcome-based training can change deceptive behavior. Broaden game categories and opponent pools, add independently selected validation games and human evaluation, and track behavior outside game incentives. ([Social-games study](https://arxiv.org/abs/2611.31821))
- **Evidence boundary — state abstraction:** The compact-state result is reported on ALFWorld and ScienceWorld. Test whether the abstractions remain sufficient under longer horizons, new task families, changed tools, and different reference agents, while measuring the cost of learning and maintaining the recursive programs. ([Compact state abstractions](https://arxiv.org/abs/2611.31800))
- **Evidence boundary — effect judgment:** GoldiBench shows low success when agents must infer editing magnitudes. Follow-up experiments could vary the number and type of visual feedback iterations, test whether forced comparison generalizes across the five applications, and add workflows outside the benchmark. ([GoldiBench](https://arxiv.org/abs/2611.31590))

## Takeaway

Today's strongest directly recorded attention signal is attached to LUCID, while the other selected papers have cross-list breadth but no recorded external-attention signal in the supplied candidate data. The substantive commonality is careful measurement: these works expose where language, vision, or tool agents appear capable but fail under more discriminating evaluation; replication and wider task coverage remain necessary.

## Method and sources

- **Window:** daily arXiv announcement batch from 2026-11-23 19:00:00 UTC through 2026-11-24 19:00:00 UTC; announced 2026-11-25 01:00:00 UTC. This is today's batch, not a prior-batch fallback. Snapshot: 2026-11-25 03:05:17 UTC.
- **Category query:** `cs.AI OR cs.LG OR stat.ML OR cs.CL OR cs.CV OR cs.RO OR cs.NE OR cs.MA`. The supplied signal file reports 427 arXiv records and the stored candidate array contains 150 entries; the ranking uses those stored candidates, which include papers spanning all eight configured categories. Among those 150, primary-category counts are led by `cs.CV` (39) and `cs.LG` (33).
- **Inference:** arXiv supplies no official trending chart. The supplied collector's 150-candidate list records one item with direct attention (`LUCID`: HF Papers 1 upvote, 2 comments, featured 2026-11-24), while the other selected candidates score 0.75 solely through 3 cross-list categories. A zero or absent external signal is not evidence of unimportance. No selected paper had a recorded Hacker News points/comments signal. Semantic Scholar citation data was unavailable, so no citation momentum is used; recent-work citation evidence is limited. Equal-score candidates are selected for clear core-AI relevance and concrete reported evidence, not author or institution prestige.
- **Source availability:** the collector reports arXiv, Hugging Face, and Hacker News collection as available; Semantic Scholar was unavailable in the signal run. The `web_extract` backend was not configured, so selected arXiv abstract pages were verified by direct retrieval; PDFs for the first three papers were downloaded and their introductions/results/limitations inspected where extractable. The stored report and structured sidecar are the dated outputs for this batch.
- **Primary sources:** [LUCID](https://arxiv.org/abs/2611.31595), [ASTERISM](https://arxiv.org/abs/2611.32316), [social-games study](https://arxiv.org/abs/2611.31821), [compact state abstractions](https://arxiv.org/abs/2611.31800), and [GoldiBench](https://arxiv.org/abs/2611.31590). Attention cross-check: [Hugging Face Papers: LUCID](https://huggingface.co/papers/2611.31595). Signal file: `/home/yizhuan/.research/ai/daily/arxiv-trending-ai-daily-2026-11-25.signals.json`.
