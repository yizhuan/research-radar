# arXiv Trending AI — Daily

AI across the core arXiv categories — Thu, 19 Nov 2026 batch — 5 papers. The clearest pattern is a move toward interactive visual agents built around controllable environments, reusable experience, and explicit evaluation; I’ll cover gameplay agents, fast image generation, configurable worlds, controllable video, and editing benchmarks. arXiv has no official trending chart, so this is an inferred ordering from checkable community attention signals; citation evidence for papers this recent is limited.

## Top papers (ranked)

### 1. [Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development](https://arxiv.org/abs/2611.24154)
- **Abstract:** Game2Player co-develops verifiable web-game environments and player agents to produce gameplay training data, reporting improved visual-agent progress on its held-out PlayerBench and the external GameWorld benchmark.
- **Authors:** Xirui Jiang, Yuxi Chen, Rui Yang, Feng Luo, Pengcheng Wang, et al.
- **arXiv:** `2611.24154v1` (published 2026-11-18T09:58:53Z; categories: `cs.CV`)
- **Evidence for ranking:** 19 Hugging Face Daily Papers votes in the 2026-11-19 archive snapshot, the highest vote count among the selected papers; it is a new paper in the current arXiv batch.
- **Claimed contribution:** The authors describe a Builder/Coding Player/VLM Player loop that creates and repairs game tasks, collecting 15.7K trajectories across 568 games and 3,436 tasks; their reported 9B agent raises PlayerBench progress from 14.3% to 31.2% and GameWorld progress from 30.0% to 53.1%.
- **Caveat:** The authors state that generated environments are not guaranteed correct, the pipeline covers offline single-player browser games, the VLM player pauses the game at each decision, and several builder/player models are proprietary.
- **Announcement type:** new submission, Thu 19 Nov 2026 batch
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Data & synthetic data

### 2. [Jeveration: System One Models Now Generate](https://arxiv.org/abs/2611.24738)
- **Abstract:** Jeveration repurposes a frozen vision-language model and a shared random state for single-pass image generation, image-to-image generation, and dense prediction, reporting 512×512 generation in 78 ms with competitive quality and dense-prediction performance.
- **Authors:** Yuhe Liu, Qi Li, Shihua Zhang, Xinchao Wang
- **arXiv:** `2611.24738v1` (published 2026-11-18T16:56:59Z; categories: `cs.CV`)
- **Evidence for ranking:** 14 Hugging Face Daily Papers votes in the 2026-11-19 archive snapshot; second-highest among the selected new submissions.
- **Claimed contribution:** The authors say that conditioning parallel predictions on a shared random state and first learning a distribution over discrete image codes helps maintain global coherence in one-forward-pass generation.
- **Caveat:** The reported generation-speed claim is for 512×512 images; the abstract does not establish performance at higher resolutions or in broader deployment settings.
- **Announcement type:** new submission, Thu 19 Nov 2026 batch
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Training & adaptation

### 3. [WorldRuler: Interactive World Modeling under Configurable Rules](https://arxiv.org/abs/2611.24869)
- **Abstract:** WorldRuler represents user-defined rules and object state in an executable 3D rule graph and connects rule execution, video generation, and perceptual feedback to preserve and visually realize those rules.
- **Authors:** Mingliang Zhai, Chuanhao Li, Jiaming Tan, Zhen Li, Yuwei Wu, et al.
- **arXiv:** `2611.24869v1` (published 2026-11-18T18:20:39Z; categories: `cs.AI`)
- **Evidence for ranking:** 11 Hugging Face Daily Papers votes in the 2026-11-19 archive snapshot; it is also one of the current batch’s directly listed cs.AI submissions.
- **Claimed contribution:** The authors introduce RuleVerse, built from GTA-V and Habitat interactions, and report experiments on saving/restoring rule-state consistency and realizing rule effects on designated objects and attributes.
- **Caveat:** The reported evidence is tied to the authors’ RuleVerse data and GTA-V/Habitat pipeline; the abstract does not establish generalization to arbitrary simulators or rule families.
- **Announcement type:** new submission, Thu 19 Nov 2026 batch
- **Themes:** Multimodal & vision-language; Robotics & control; Evaluation & benchmarks

### 4. [Code World Model 2.0: Towards Infinite Controllable Video Generation](https://arxiv.org/abs/2611.22925)
- **Abstract:** Invoker-Render pairs bidirectional video creation with a causal four-step streaming renderer conditioned on structural proxies, appearance references, and language, using Progressive Forcing to reduce rollout drift and support long interactive generations.
- **Authors:** Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu, et al.
- **arXiv:** `2611.22925v2` (published 2026-11-18T05:27:57Z; categories: `cs.CV`)
- **Evidence for ranking:** 7 Hugging Face Daily Papers votes in the 2026-11-19 archive snapshot; its v2 revision falls in the current batch, and it reports tests across 140 streaming rollouts.
- **Claimed contribution:** The authors report that their four-step renderer outperforms recent streaming baselines on visual quality, structural adherence, and reference preservation, with stable scene and subject appearance in 30-minute racing rollouts.
- **Caveat:** The authors identify fixed proxy granularity within rollout windows as a current constraint; dynamic mid-stream level-of-detail changes and closed-loop coupling to interactive state engines remain future work.
- **Announcement type:** revision, Thu 19 Nov 2026 batch
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Training & adaptation

### 5. [RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models](https://arxiv.org/abs/2611.24098)
- **Abstract:** RoughCut-Bench evaluates visual- and speech-driven video rough-cut workflows with annotated source material and reports that current large vision-language models remain limited at producing expert-aligned cut plans.
- **Authors:** Ruisi Zhao, You Li, Sihan Chen, Aosong Cheng, Chixiang Ma, et al.
- **arXiv:** `2611.24098v1` (published 2026-11-18T09:21:18Z; categories: `cs.CV`)
- **Evidence for ranking:** 6 Hugging Face Daily Papers votes in the 2026-11-19 archive snapshot; the paper is a new cs.CV submission in the current batch and reports a benchmark spanning visual and speech-driven editing.
- **Claimed contribution:** The authors contribute 101 visually driven cases with 831 raw videos and 1,476 highlight annotations, plus 84 transcript-driven cases, along with agentic workflows and evaluation protocols.
- **Caveat:** Its evidence is bounded by the benchmark’s 22 films and defined visual/speech-driven cases; the reported model comparisons are not a broad trial of production editing workflows.
- **Announcement type:** new submission, Thu 19 Nov 2026 batch
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language; Agents & reasoning

## Trending Research Themes

- **Interactive visual worlds are a shared focus in this small sample.** Game2Player builds and repairs game environments to collect agent experience, while WorldRuler and Code World Model 2.0 focus on controllable world state and video generation. This is a recurring topic in these selected papers, not evidence of a field-wide breakthrough.
- **Control and feedback are becoming part of the generation/evaluation loop.** WorldRuler connects rules, rendering, and perception; Code World Model 2.0 uses proxies and self-generated histories; Game2Player uses agent reports to repair its task environments.
- **Evaluation and data construction are explicit contributions, not just add-ons.** Game2Player releases game tasks and trajectories, and RoughCut-Bench formalizes an editing benchmark; both expose where agent performance is hard to measure or train reliably.
- **The selected batch is category-concentrated:** four of the five papers are primary `cs.CV`; WorldRuler is primary `cs.AI`. These are representative picks based on attention, not a census of the full batch.

## Open Problems and Research Directions

- **Author-stated open problem — environment reliability and realism:** Game2Player says accepted environments are not guaranteed correct and its VLM player pauses the game at every decision. Follow-up work could add larger-scale independent human audits and evaluate action timing under real-time play, then measure whether training gains transfer to online or multiplayer games. [Game2Player](https://arxiv.org/abs/2611.24154)
- **Author-stated open problem — interactive video control:** Code World Model 2.0 identifies fixed proxy granularity within rollout windows and the absence of closed-loop coupling to an interactive state engine as current boundaries. A direct next experiment is to switch proxy detail mid-stream and measure state, identity, and appearance consistency while actions feed back into the renderer. [Code World Model 2.0](https://arxiv.org/abs/2611.22925)
- **Evidence-tied synthesis — generality of rule-conditioned worlds:** WorldRuler’s abstract reports GTA-V/Habitat-derived RuleVerse experiments. Testing held-out rule families and a separate simulator would clarify whether its graph/state approach transfers beyond its construction pipeline. [WorldRuler](https://arxiv.org/abs/2611.24869)
- **Author-reported gap — editing quality:** RoughCut-Bench reports that current LVLMs remain limited on expert-aligned cut plans. Further work could test whether structured planning, stronger temporal grounding, and human-in-the-loop revisions improve quality on new films and independently authored production briefs. [RoughCut-Bench](https://arxiv.org/abs/2611.24098)

## Takeaway

The most visible signal in this batch is practical infrastructure for interactive visual agents: controllable environments, scalable gameplay experience, and evaluation protocols are being built alongside the models. Community votes provide a useful short-term attention cue, but they do not establish research quality or durable impact; independent replication and broader settings remain important tests.

## Method and sources

- **Window:** daily, 2026-11-19 through 2026-11-19; selected the latest category-page batch labeled Thu, 19 Nov 2026. The selected new submissions were submitted on Nov 18 UTC and announced in that batch; Code World Model 2.0 is a v2 revision dated Nov 18 UTC.
- **Snapshot:** 2026-11-19T17:09:09Z. Hugging Face vote counts come from the dated third-party archive recorded at 2026-11-19 07:03 UTC; the archive says its paper list is drawn from Hugging Face Daily Papers.
- **Scope/query:** core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. Machine-readable query attempted: `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`, sorted by submitted date descending. The arXiv API request returned HTTP 429, so category recent pages and verified arXiv abstract pages were used instead. Recent pages: [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent).
- **Inference:** arXiv has no official trending ranking. The ordering uses recorded Hugging Face Daily Papers votes as its primary independent attention signal, then recency and paper-specific technical evidence. This is a notable-paper shortlist, not a claim of comprehensive field coverage. Semantic Scholar Graph API batch metadata for all five showed current citationCount and influentialCitationCount of 0 at retrieval; these are current totals, not period gains, and are too sparse to discriminate among same-day papers.
- **Corroborating sources:** [Hugging Face Daily Papers, Nov 19](https://huggingface.co/papers/date/2026-11-19); [dated vote archive, Nov 19](https://trendingai.today/2026-11-19/); [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch); and the five linked arXiv abstract pages above. arXiv abstract/HTML pages were used for metadata, claims, and caveats; full-text HTML was unavailable for some selected papers, so their caveats are bounded to abstract-level evidence.
