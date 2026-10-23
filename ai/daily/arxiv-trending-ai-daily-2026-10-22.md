# arXiv AI papers — 22 October 2026 announcement batch (5 papers)

The strongest recurring pattern is a shift from impressive generated outputs toward sustained interaction: following changing requests, preserving state, and transferring behavior beyond the training setting. This report covers interactive video evaluation, agent-serving efficiency, and embodied control/generalization. arXiv has no official trending chart, so this is an inferred ordering based on Hugging Face Daily Papers community votes; citation evidence is limited for these very recent papers, and no citation totals were verified.

## Top papers (ranked)

### 1. [StreamEval: Evaluating Interactive Streaming Video Generation Models](https://arxiv.org/abs/2610.28402)
- **Abstract:** StreamEval benchmarks five kinds of interactive video generation with 300 scripted cases and reports that strong visual quality does not ensure reliable request following or state consistency.
- **Authors:** StreamEval Team
- **arXiv:** `2610.28402v1` (published 2026-10-20 15:47:43 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Hugging Face Daily Papers for 2026-10-22 placed it #1 with 347 upvotes at the 2026-10-23 00:12 UTC snapshot; this is the main placement signal.
- **Claimed contribution:** The authors introduce a benchmark spanning avatar dialogue/performance, world generation, and two editing tasks, with metrics for execution, state consistency, visual fidelity, and audiovisual coordination.
- **Caveat:** Its 300 cases are scripted; the authors identify human pairwise judgments and agreement with the rubric as a next step.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language

### 2. [DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997)
- **Abstract:** DONIC combines a multi-view bimanual interaction dataset with a shared reinforcement-learning and behavior-cloning tracker that reports strong reference-tracking results on unseen trajectories and held-out objects.
- **Authors:** Mingze Sun, Ziang Cao, Yuan Fei, Qiankuan Tao, Zihan Wang et al.
- **arXiv:** `2610.29997v1` (published 2026-10-21 16:36:02 UTC; categories: `cs.RO`, `cs.CV`)
- **Evidence for ranking:** Hugging Face Daily Papers for 2026-10-22 placed it #3 with 124 upvotes at the 2026-10-23 00:12 UTC snapshot; this is the main placement signal.
- **Claimed contribution:** The authors contribute DONIC and the 1,575-sequence, 229-object BiHOI dataset; a single checkpoint reports 86.79% success on unseen trajectories of training objects and 57.32% on held-out objects.
- **Caveat:** The authors limit their quantitative evaluation to simulated, reference-conditioned single-rigid-object tracking; physical-robot transfer and longer-horizon/multi-object tasks remain future work.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Robotics & control; Training & adaptation

### 3. [Cache Engineering for Agents](https://arxiv.org/abs/2610.28577)
- **Abstract:** The paper lets LLM agents manage active key-value cache directly, and reports lower inference cost with improved throughput and latency compared with history trimming/summarization baselines.
- **Authors:** Tianyu Fu, Ruoxi Wang, Zihan Min, Zhongqi Ren, Zhihao Li et al.
- **arXiv:** `2610.28577v1` (published 2026-10-20 17:32:24 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Hugging Face Daily Papers for 2026-10-22 placed it #4 with 112 upvotes at the 2026-10-23 00:12 UTC snapshot; independent technical coverage also discussed its cache-control/serving design.
- **Claimed contribution:** The authors propose cache-side `drop` and position-adjustment `repos` operations and the AKV serving engine; their reported tool-response rolling-drop policy improves average benchmark score by 1.7 points and lowers average cost by 27.7% against threshold-triggered summarization.
- **Caveat:** The authors leave broader cache policies, training agents under this scheme, and serving support for linear-attention models to future work.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Efficient inference & systems; Agents & reasoning

### 4. [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989)
- **Abstract:** Future Chunk Prediction adds an auxiliary training objective that predicts temporally distant video chunks, improving physical-plausibility scores over teacher-forced training without changing autoregressive inference.
- **Authors:** Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu et al.
- **arXiv:** `2610.29989v1` (published 2026-10-21 16:28:46 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Hugging Face Daily Papers for 2026-10-22 placed it #5 with 111 upvotes at the 2026-10-23 00:12 UTC snapshot; this is the main placement signal.
- **Claimed contribution:** The authors report that, under matched settings, FCP raises Physics-IQ from 30.4 to 33.8 for Wan2.2-5B image-to-video and from 40.6 to 44.4 for video-to-video, while leaving inference unchanged.
- **Caveat:** The authors did not test larger-scale or from-scratch training or longer video horizons; complementary VLM-judged benchmarks may miss subtle timing and magnitude differences, and some training footage is not released.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Training & adaptation; Multimodal & vision-language

### 5. [Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698)
- **Abstract:** Across 120 continued-pretraining configurations, the study finds that data, world diversity, and model size affect in-domain and cross-world game performance differently, with persistent gaps on distant worlds.
- **Authors:** Kuan Zhang, Yukun Chen, Zhihao Yang, Yue Su, Xiangnan Wu et al.
- **arXiv:** `2610.28698v1` (published 2026-10-20 11:09:09 UTC; categories: `cs.AI`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Hugging Face Daily Papers for 2026-10-22 placed it #10 with 47 upvotes at the 2026-10-23 00:12 UTC snapshot; this is the main placement signal.
- **Claimed contribution:** The authors systematically vary four model sizes, six data budgets, and five game mixtures, reporting an early interface-learning phase with broader benefits followed by more world-specific gains.
- **Caveat:** The authors report limited transfer to distant worlds and conclude that continued pretraining/imitation alone is insufficient for generalist embodied agents; their results come from a fixed game set and 120-condition study.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Training & adaptation

## Trending Research Themes

- Interaction quality is being measured as execution over time, not just a plausible frame or a successful isolated answer: StreamEval separates request execution from visual fidelity and state consistency, while Cache Engineering for Agents treats cache management as part of an agent's long-horizon operating loop.
- Embodied generalization is still conditional on the evaluation distribution. DONIC reports held-out-object reference tracking in simulation, while Scaling in Games finds that broader game mixtures help related worlds more reliably than distant ones; neither result establishes unrestricted real-world transfer.
- Training objectives and data mixtures are being tested as levers for temporal prediction and transfer. Looking Ahead adds parallel future-chunk supervision to autoregressive video training; Scaling in Games varies model size, data volume, and world diversity and finds that these axes do not yield uniform out-of-domain gains.
- The five-paper sample spans primary categories `cs.CV` (2), `cs.RO` (1), `cs.CL` (1), and `cs.AI` (1); computer-vision/video work is prominent, but the ranking is attention-signal-driven rather than a balanced category survey.

## Open Problems and Research Directions

- **Author-stated open problem — interactive evaluation:** StreamEval finds low request-following/edit-success scores and proposes human pairwise judgments against its task rubric. A useful next experiment would extend sessions and request schedules, then test whether rubric scores agree with human judgments under conflicting or revised instructions. [StreamEval]
- **Author-stated open problem — cache generality:** Cache Engineering for Agents leaves broader cache strategies, training agents with cache operations, and linear-attention serving for future work. Compare cache policies across attention architectures and longer tasks, measuring both task outcomes and cache/serving costs. [Cache Engineering for Agents]
- **Author-stated open problem — robot transfer:** DONIC's evidence is simulated reference tracking for single rigid objects. Test the shared tracker on physical bimanual hardware, longer tasks, articulated/multiple objects, and held-out operation categories. [DONIC]
- **Author-stated open problem — temporal-model scale and reproducibility:** Looking Ahead leaves larger models, longer horizons, and from-scratch pretraining untested. Replicate its matched comparisons with released data/checkpoints where possible and evaluate whether gains persist on longer rollouts and non-physics temporal changes. [Looking Ahead]
- **Evidence-tied research direction:** Scaling in Games finds persistent distant-world gaps and identifies limits of imitation. Test training stages that add outcome feedback or online adaptation, with separate reporting for familiar, related, and distant worlds and both paused and real-time interaction. [Scaling in Games]

## Takeaway

The most visible papers in this batch treat interactivity and transfer as first-class problems: video systems must follow changing requests, agents must manage long-context costs, and embodied policies must generalize beyond the most familiar setting. The vote-based ordering captures current community attention, not scientific validation; the clearest open tests are human-aligned interactive evaluation, cross-domain transfer, and physical deployment.

## Method and sources

- **Window:** latest arXiv announcement batch dated 2026-10-22; selected first submissions were published 2026-10-20 through 2026-10-21 UTC. Snapshot: 2026-10-23 00:12:15 UTC.
- **Scope:** core arXiv AI categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; the selected-paper query also retained cross-lists.
- **Candidate collection:** one broad arXiv API query sorted by submission date, followed by targeted metadata retrieval and direct checks of each selected arXiv abstract page; full HTML text was checked for the top three papers where available.
- **Ranking:** inferred primarily from each paper's placement and upvote count on the [Hugging Face Daily Papers page for 2026-10-22](https://huggingface.co/papers/date/2026-10-22), read at snapshot time. Votes are current totals at that snapshot, not citations or votes gained during the day. No numeric composite trend score was created.
- **Citation evidence:** Semantic Scholar citation metadata was not verified during this run, so citation counts and citation velocity were not used.
- **Sources:** [arXiv recent list](https://arxiv.org/list/cs/recent); [StreamEval](https://arxiv.org/abs/2610.28402) and [Hugging Face paper page](https://huggingface.co/papers/2610.28402); [DONIC](https://arxiv.org/abs/2610.29997) and [Hugging Face paper page](https://huggingface.co/papers/2610.29997); [Cache Engineering for Agents](https://arxiv.org/abs/2610.28577), [Hugging Face paper page](https://huggingface.co/papers/2610.28577), and [independent technical coverage](https://aicassindra.com/research/2026/10/22/research-radar-more-memory-worse-agents-decision-model-controller-cost-akv-cache-engineering.html); [Looking Ahead](https://arxiv.org/abs/2610.29989) and [Hugging Face paper page](https://huggingface.co/papers/2610.29989); [Scaling in Games](https://arxiv.org/abs/2610.28698) and [Hugging Face paper page](https://huggingface.co/papers/2610.28698).
