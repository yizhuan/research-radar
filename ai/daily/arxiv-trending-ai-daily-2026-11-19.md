# arXiv AI daily — Thursday, 19 November 2026

Five leading new submissions from the latest core-AI announcement batch, ordered by recorded Hugging Face Daily Papers votes: Game2Player (19), Jeveration (14), WorldRuler (11), then two papers tied at 6. The visible mix is interactive visual worlds, single-pass generation, and practical evaluation/systems work; today’s briefing covers agents, generation, and evaluators. Caveat: arXiv has no official trending chart; this ordering is inferred from one third-party vote snapshot, and citation evidence is too sparse for these new papers to confirm popularity or impact.

## Top papers (ranked)

### 1. [Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development](https://arxiv.org/abs/2611.24154)
- **Abstract:** Game2Player co-develops verifiable web-game environments and player agents to collect gameplay experience, reporting improved visual-agent progress on its held-out PlayerBench and the external GameWorld benchmark.
- **Authors:** Xirui Jiang, Yuxi Chen, Rui Yang, Feng Luo, Pengcheng Wang, et al.
- **arXiv:** `2611.24154v1` (published 2026-11-18 09:58:53 UTC; categories: `cs.CV`)
- **Evidence for ranking:** 19 votes in the archived Hugging Face Daily Papers edition recorded 2026-11-19 07:03 UTC, the highest count among papers in this announcement batch that made the archive’s 15-paper list; it was second in the full archive list, behind an older paper outside this batch.
- **Claimed contribution:** The authors describe a Builder/Coding Player/VLM Player loop that builds and repairs game tasks, collecting 15.7K trajectories across 568 games and 3,436 tasks; they report a 9B agent improves PlayerBench progress from 14.3% to 31.2% and GameWorld progress from 30.0% to 53.1%.
- **Caveat:** The authors state that accepted environments are not guaranteed correct without a full human audit; the pipeline covers offline single-player browser games, the VLM player pauses the game at each decision, and several builder/player models are proprietary.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Multimodal & vision-language; Agents & reasoning; Data & synthetic data

### 2. [Jeveration: System One Models Now Generate](https://arxiv.org/abs/2611.24738)
- **Abstract:** Jeveration repurposes a frozen vision-language model and a shared random state for single-pass image generation, image-to-image generation, and dense prediction, reporting 512×512 generation in 78 ms with competitive image quality.
- **Authors:** Yuhe Liu, Qi Li, Shihua Zhang, Xinchao Wang
- **arXiv:** `2611.24738v1` (published 2026-11-18 16:56:59 UTC; categories: `cs.CV`)
- **Evidence for ranking:** 14 votes in the same archived Hugging Face Daily Papers edition; third in the overall vote list and second among papers from this announcement batch.
- **Claimed contribution:** The authors condition parallel image-code predictions on a shared random state and first learn a distribution over discrete image codes; one checkpoint handles text-to-image, image-to-image, and dense prediction in one forward pass.
- **Caveat:** The reported 78 ms result is for 512-pixel images on a single H200; the paper does not establish the same speed/quality trade-off at larger resolutions or across other hardware.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Training & adaptation

### 3. [WorldRuler: Interactive World Modeling under Configurable Rules](https://arxiv.org/abs/2611.24869)
- **Abstract:** WorldRuler represents user-defined rules and object state in an executable 3D rule graph and connects rule execution, video generation, and perceptual feedback to preserve and visually realize those rules.
- **Authors:** Mingliang Zhai, Chuanhao Li, Jiaming Tan, Zhen Li, Yuwei Wu, et al.
- **arXiv:** `2611.24869v1` (published 2026-11-18 18:20:39 UTC; categories: `cs.AI`)
- **Evidence for ranking:** 11 votes in the archived Hugging Face Daily Papers edition; fifth in the overall vote list and third among batch-eligible papers.
- **Claimed contribution:** The authors introduce an executable rule graph and dynamic object binding for persistent, user-defined world rules, and a GTA-V/Habitat-derived RuleVerse dataset; they report improved rule-state consistency and rule realization in experiments.
- **Caveat:** The reported evidence is tied to the authors’ RuleVerse pipeline and GTA-V/Habitat settings; transfer to unseen simulators or substantially different rule families remains to be established.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Agents & reasoning; Multimodal & vision-language; Robotics & control

### 4. [RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models](https://arxiv.org/abs/2611.24098)
- **Abstract:** RoughCut-Bench evaluates visual- and speech-driven video rough-cut workflows with annotated source material and reports that current large vision-language models remain limited at producing expert-aligned cut plans.
- **Authors:** Ruisi Zhao, You Li, Sihan Chen, Aosong Cheng, Chixiang Ma, et al.
- **arXiv:** `2611.24098v1` (published 2026-11-18 09:21:18 UTC; categories: `cs.CV`)
- **Evidence for ranking:** 6 votes in the archived Hugging Face Daily Papers edition; tied for the fourth-highest count among eligible batch papers in that list. The arXiv record also notes acceptance to KDD 2027.
- **Claimed contribution:** The authors contribute 101 visually driven cases over 831 raw videos with 1,476 highlight annotations, 84 speech-driven transcript cases, and agentic workflows for producing structured cut plans.
- **Caveat:** The reported comparison is bounded by the benchmark’s annotated visual and transcript-driven cases; it does not establish performance in broader production editing workflows.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language; Agents & reasoning

### 5. [Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration](https://arxiv.org/abs/2611.24733)
- **Abstract:** CriticNPU uses an online-calibrated, hardware-mechanistic critic to guide LLM-inference accelerator design search, reporting best-or-tied-best latency in most tested settings with roughly half as many simulator calls as baselines.
- **Authors:** Yicheng He, Yuqi Xue, Tianyang Wu, Jian Huang, Bin Hu
- **arXiv:** `2611.24733v1` (published 2026-11-18 16:48:43 UTC; categories: `cs.AR`)
- **Evidence for ranking:** 6 votes in the archived Hugging Face Daily Papers edition, tied with RoughCut-Bench; the arXiv record notes acceptance to NeurIPS 2026. Included despite its `cs.AR` primary category because its abstract directly studies architecture optimization for LLM inference.
- **Claimed contribution:** The authors’ CriticNPU combines an online-calibrated Roofline-style critic, workload extraction, and an architecture planner; over six LLM workloads and 16 deployment configurations per model, it reaches best-or-tied-best latency in 74% of prefill and 87.5% of decode settings using about half the simulator calls of competitive DSE baselines.
- **Caveat:** Evidence is limited to the reported LLM workloads, model/deployment configurations, and simulator-based design-space exploration; transfer to other hardware, workloads, and measured deployments is not established by the abstract.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Interactive visual worlds and agents:** Game2Player co-develops games and players for scalable experience, while WorldRuler makes user-defined rules persist across generated interactive worlds. They share a control-and-state focus, but use different mechanisms and benchmarks.
- **Speed and controllability in visual generation:** Jeveration targets one-pass generation with a shared latent random state; WorldRuler uses rule graphs and perceptual feedback to constrain generated video. The common emphasis is controllability, not evidence of a single converged architecture.
- **Evaluation becomes a first-class artifact:** RoughCut-Bench packages editing cases and cut-plan measures, while Game2Player releases held-out games and tracks task progress. Both make evaluation environments part of the contribution, though their task domains differ.
- **Efficiency work spans models and hardware:** Jeveration reports single-pass image generation; CriticNPU searches NPU designs for LLM inference. This is an isolated cross-layer pairing in the selected set, not a claim of a field-wide shift.
- **Corpus context:** In the 501-record latest core-category query group, category assignment counts were concentrated in `cs.CV` (188), `cs.AI` (164), `cs.LG` (158), and `cs.RO` (89); assignments include cross-lists and are not disjoint paper counts. Three selected papers are primary `cs.CV`; CriticNPU is the one clearly AI-relevant systems paper admitted from outside the configured categories.

## Open Problems and Research Directions

- **Environment correctness and real-time play (author-stated limits):** Game2Player reports that environments are not guaranteed correct without human audit and that its VLM player pauses at each decision. Expand independent human audits, then test online and multiplayer games under real-time latency and licensing constraints. [Game2Player](https://arxiv.org/abs/2611.24154)
- **Resolution and hardware generalization (evidence-tied synthesis):** Jeveration’s headline latency is at 512×512 on one H200. Test multiple resolutions and accelerators while reporting both wall-clock latency and quality/dense-prediction trade-offs. [Jeveration](https://arxiv.org/abs/2611.24738)
- **World-rule transfer (evidence-tied synthesis):** WorldRuler evaluates GTA-V/Habitat-derived RuleVerse interactions. Test held-out rule families and a separate simulator to determine whether the executable graph and visual state-binding approach generalize beyond the construction pipeline. [WorldRuler](https://arxiv.org/abs/2611.24869)
- **Expert alignment and workflow realism (author-reported gap):** RoughCut-Bench reports current LVLMs remain limited at expert-aligned cut plans. Assess whether temporal grounding and human revision improve results on new source footage and independently authored editing briefs. [RoughCut-Bench](https://arxiv.org/abs/2611.24098)
- **Simulator-to-deployment transfer (evidence-tied synthesis):** CriticNPU’s results use simulator feedback across six LLM workloads. Compare predicted bottlenecks with measured accelerator runs and evaluate whether the critic retains its call savings on unseen workloads and hardware. [CriticNPU](https://arxiv.org/abs/2611.24733)

## Takeaway

The strongest attention signal in the latest batch centers on interactive visual agents and generative systems, with Game2Player and Jeveration leading the archived vote counts. The papers pair ambitious systems with bounded evaluations; follow-up evidence on real-time interaction, broader hardware, and independent task validation will determine how far the reported gains travel.

## Method and sources

- **Window:** latest arXiv announcement batch dated 2026-11-19 (Thursday); it is the prior batch at the 2026-11-20 UTC snapshot. Category pages group the latest submissions under “Thu, 19 Nov 2026,” while the arXiv `published` timestamps on the selected abstracts are 2026-11-18 UTC. Exact daily window: 2026-11-19 through 2026-11-19. Snapshot: 2026-11-20 01:12:57 UTC.
- **Core corpus query:** `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`, sorted by submitted date descending. The broad query returned 501 records in its latest date group, with all configured categories represented. Category assignment counts (including cross-lists): `cs.CV` 188, `cs.AI` 164, `cs.LG` 158, `cs.RO` 89, `cs.CL` 54, `stat.ML` 26, `cs.MA` 11, `cs.NE` 7. CriticNPU, a `cs.AR` paper, was added because its abstract makes the AI contribution—optimizing NPU designs for LLM inference—unambiguous.
- **Ranking evidence:** The Hugging Face Daily Papers list is a community attention proxy, not an arXiv ranking. Vote counts come from the third-party archive’s 2026-11-19 edition recorded at 07:03 UTC; counts are that snapshot, not votes gained during the day. The 15-paper archive list also included older papers outside this batch, which were excluded from this daily batch shortlist. Tied 6-vote papers were ordered by core-corpus category fit, with the `cs.CV` paper before the `cs.AR` systems paper.
- **Citation signal:** Semantic Scholar Graph reports current citationCount and influentialCitationCount of 0 for all five identifiers at this check; these are current totals and provide no useful same-day momentum distinction. No citation counts are presented as period gains.
- **arXiv batch cross-checks:** [cs.AI recent submissions](https://arxiv.org/list/cs.AI/recent) and [cs.CV recent submissions](https://arxiv.org/list/cs.CV/recent). Each selected arXiv abstract page was checked; full-text HTML was reviewed for the leading three papers.
- **Attention source:** [Hugging Face Daily Papers, Nov 19](https://huggingface.co/papers/date/2026-11-19); archived counts at [Trending AI Today, Nov 19](https://trendingai.today/2026-11-19/).
- **Selected arXiv pages:** [2611.24154](https://arxiv.org/abs/2611.24154), [2611.24738](https://arxiv.org/abs/2611.24738), [2611.24869](https://arxiv.org/abs/2611.24869), [2611.24098](https://arxiv.org/abs/2611.24098), [2611.24733](https://arxiv.org/abs/2611.24733).
