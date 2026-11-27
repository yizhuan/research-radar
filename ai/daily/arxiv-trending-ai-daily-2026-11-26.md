## Headline

AI, arXiv daily announcement batch 2026-11-26: 8 notable papers. The signal-defined batch for 2026-11-27 had no eligible core-AI submissions, so this report falls back to the previous populated batch (2026-11-26). The selected papers emphasize evaluation validity for AI agents, efficient model computation, and methods that connect perception to action. Spoken agenda: monitor tests, reasoning and training, then vision-language and robotics. arXiv has no official trending chart; this inferred relevance ordering is not a popularity ranking, and recent citation evidence is limited because no per-paper attention or citation values were available for the fallback batch.

## Top papers (ranked)

### 1. [Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934)
- **Abstract:** The authors find that an AI monitor's measured miss rate changes substantially with the method and optimization level used to generate attack transcripts that stand in for dangerous behavior.
- **Authors:** Charlie Griffin, Oliver Makins, Asa Cooper Stickland, Alessandro Abate, Yarin Gal, et al.
- **arXiv:** `2611.34934v1` (published 2026-11-25T18:59:28Z; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** The UK AI Safety Institute published a dedicated research page and a follow-up technical blog about this work, providing the clearest independent discussion found in this batch. No per-paper HF/HN/citation score was emitted for the fallback batch, so this is a relevance signal, not a measured popularity rank.
- **Claimed contribution:** The authors report false-negative rates of 0.5–20.8% across reinforcement-learning optimization levels and 6.4–23.0% across methods at their best observed levels, with attacks transferring from proxy monitors to a held-out GPT-5.4 monitor.
- **Caveat:** The authors state that the case study uses limited settings and attack methods, and a Qwen 3.8 27B target agent less capable than the GPT-5.4 monitor; they stress that synthetic attack transcripts need a separate justification as deployment proxies.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Safety & alignment; Evaluation & benchmarks

### 2. [Mixture-of-Loops Transformer](https://arxiv.org/abs/2611.34923)
- **Abstract:** MoLT uses key-value memory across repeated Transformer loops, with a U-shaped variant designed to balance model quality and computation and enable single-traversal decoding.
- **Authors:** Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai
- **arXiv:** `2611.34923v1` (published 2026-11-25T18:58:53Z; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** The work is listed on Hugging Face Papers and has a linked public code repository, both checkable discovery/artifact signals. No verified upvote, repository-star, or citation count was available, so it ranks for demonstrated systems relevance rather than quantified attention.
- **Claimed contribution:** In experiments reported by the authors, U-MoLT matches OLMo3 validation cross-entropy with 1.7× token efficiency at 700M parameters and achieves similar latency to a non-looped OLMo3 on their small-model decoding test.
- **Caveat:** The authors' from-scratch evaluations cover 700M and 1.5B dense models and a 3B MoE model; their continued-pretraining test uses one 0.8B backbone, so behavior at larger scales remains unestablished.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Efficient inference & systems; Training & adaptation

### 3. [Diverse Alternative Reasoning Traces for Hard Math Problems](https://arxiv.org/abs/2611.34928)
- **Abstract:** DART revisits rejected mathematical reasoning traces, targeting uncertain steps for alternative completions, and the authors report improved recovery of hard problems over matched Monte Carlo sampling.
- **Authors:** Lukas Aichberger, Adam Golinski, Arno Blaas, Arwen Bradley, Jacob Springer, et al.
- **arXiv:** `2611.34928v1` (published 2026-11-25T18:59:11Z; categories: `cs.CL`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The arXiv record notes a NeurIPS 2026 workshop connection, and the paper is cross-listed across three core AI categories. These establish scholarly context and breadth, not readership; no per-paper attention or citation score was available for this fallback batch.
- **Claimed contribution:** On greedy-unsolved DeepMath-103K problems, the authors report 37% more problems recovered than matched-count Monte Carlo sampling, and lower cost per accepted trace; post-training Llama-3.1-8B-Instruct gives the best point estimate in five of six reported evaluations.
- **Caveat:** The authors say reference-answer guidance makes DART primarily a post-training trace-mining method, not a test-time reasoning method; the main post-training comparison uses one model and one seed, and exact-string deduplication cannot rule out near-duplicate contamination.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Agents & reasoning; Training & adaptation; Data & synthetic data

### 4. [Tracking Any Point with Agentic Visual Reasoning](https://arxiv.org/abs/2611.34943)
- **Abstract:** AgenTAP lets a vision-language model actively inspect video evidence to localize and verify physical points, including points that disappear and later reappear.
- **Authors:** Xuweiyi Chen, Jin Yao, Linzhan Mou, Lei Gong, Di Liu, et al.
- **arXiv:** `2611.34943v1` (published 2026-11-25T18:59:58Z; categories: `cs.CV`)
- **Evidence for ranking:** The authors provide a project page and introduce the EgoTAP-4D trajectory dataset, which make the result and data contribution directly inspectable. No independent attention counts were found; placement reflects its evaluated agentic method and dataset contribution, not a popularity claim.
- **Claimed contribution:** The authors report that AgenTAP with GPT-6 Astra outperforms tested expert vision models on point localization and visibility prediction, and that training D4RT with EgoTAP-4D improves average 3D tracking performance.
- **Caveat:** The strongest reported comparison is tied to the evaluated backbones and tracking benchmarks; the authors' conclusion about extending visual reasoning to pixel-level tracking should not be read as evidence for all VLMs or video settings.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Agents & reasoning; Multimodal & vision-language; Data & synthetic data

### 5. [Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs](https://arxiv.org/abs/2611.34914)
- **Abstract:** Cairn steers a frozen vision-language-action model around obstacles by sampling object-centric 3D trajectories and feeding waypoint guidance back into the model's action generation.
- **Authors:** Agelos Kratimenos, Kostas Daniilidis, Evangelos Chatzipantazis
- **arXiv:** `2611.34914v1` (published 2026-11-25T18:57:29Z; categories: `cs.RO`, `cs.CV`)
- **Evidence for ranking:** The paper is cross-listed in robotics and computer vision and reports tests on held-out simulation scenes, a third-party benchmark, and a real robot. These are relevance and evaluation-breadth signals; no per-paper external-attention score was available.
- **Claimed contribution:** On 1,941 held-out LIBERO scenes, the authors report raising frozen π0.5 task success from 24.5% to 95.1%; they also report gains on LIBERO-PRO and one real Franka demonstration.
- **Caveat:** Most quantitative evidence is from simulation; the real-robot result is a single described task, so broad physical-world reliability is not established.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Robotics & control; Multimodal & vision-language

### 6. [Can image generation help visual reasoning? An empirical study](https://arxiv.org/abs/2611.34935)
- **Abstract:** Across 13 vision-language model and image-generator pairs, the authors find that adding a generated helper image reduces mean visual-question accuracy, with outcomes varying by task and repeated editing.
- **Authors:** Xueyang Yu, Yifan Jing, Taiming Lu, Linrong Cai, Zhipeng Cai, et al.
- **arXiv:** `2611.34935v1` (published 2026-11-25T18:59:31Z; categories: `cs.LG`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** The paper is cross-listed across language, learning, and vision and provides a counterexample to the assumption that extra generated visual context necessarily helps. No independent discussion or per-paper attention values were found, so it is included for the informative negative result, not inferred popularity.
- **Claimed contribution:** The authors report a mean accuracy decrease of 3.7 percentage points, with decreases on nine of ten tasks; repeated edits help on ERQA but leave ChartQAPro and MathVista below their no-generation baselines.
- **Caveat:** The result is bounded by the 13 tested model-generator pairs and ten tasks; the abstract itself reports task-dependent outcomes rather than a universal effect of generated images.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks

### 7. [$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents](https://arxiv.org/abs/2611.34920)
- **Abstract:** μ-Bench evaluates voice agents on concurrent users' goals, permissions, privacy, and follow-up requests using simulated participants that react to the agent during a session.
- **Authors:** Qihao Lin, Guanxu Chen, Shuhang Zheng, Xiaoya Lu, Jingyi Yang, et al.
- **arXiv:** `2611.34920v1` (published 2026-11-25T18:58:42Z; categories: `cs.CL`, `cs.AI`)
- **Evidence for ranking:** The paper supplies a public benchmark repository and a clearly specified 800-case evaluation suite. No repository popularity or per-paper attention value was checked; its place reflects benchmark relevance to shared-agent authority and coordination.
- **Claimed contribution:** Across 13 voice agents, the authors report that proprietary systems peak at 62.24% tool-free and 65.44% tool-augmented joint success, while tested open-weight models remain below 20%.
- **Caveat:** Participants are simulated rather than live users, so results measure performance in the benchmark's interaction model and do not establish real-world multi-user reliability.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Safety & alignment

### 8. [One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics](https://arxiv.org/abs/2611.34925)
- **Abstract:** OneOcean combines data-grounded ocean conditions with a multi-task, multi-agent marine robotics simulator and standardized evaluation manifests.
- **Authors:** Shuaijun Liu, Qifu Wen, Xingwei Chen, Xinwen Hu, Feiyang You, et al.
- **arXiv:** `2611.34925v1` (published 2026-11-25T18:58:56Z; categories: `cs.RO`, `cs.DB`)
- **Evidence for ranking:** The paper offers a broad task ladder, multi-agent capability for 2–10 vehicles, and a reproducible benchmark; these support its inclusion as a useful robotics evaluation contribution. No independent attention or citation signal was available for this fallback batch.
- **Claimed contribution:** The authors introduce a suite spanning navigation, inspection, and multi-agent coordination under data-driven currents and tides, and compare heuristic, behavior-cloning, and LLM-based planners.
- **Caveat:** The abstract reports simulator experiments, not physical marine-robot trials; the benchmark's real-world transfer remains to be tested.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Robotics & control; Evaluation & benchmarks

## Trending Research Themes

- Agent evaluation is shifting from a single headline score toward scrutinizing the test distribution and interactions. *Attack Policy Selection* shows measured monitor evasion varies with the attack policy, while *μ-Bench* requires joint goal completion without unauthorized actions in reactive multi-user sessions. This is a pattern in this selected batch, not proof of a field-wide methodological shift.
- Training-time and inference-time computation are both being redesigned: *MoLT* reuses key-value memory across loops to improve token efficiency and decoding, while *DART* mines alternative traces from failed reasoning attempts to improve post-training data yield. The common motif is deliberate reuse of prior computation, but the methods target different bottlenecks.
- In multimodal systems, richer internal actions are not automatically better. *AgenTAP* uses active inspection to verify point identity, whereas *Can image generation help visual reasoning?* reports that generated helper images often reduce accuracy. One paper advances visual interaction; the other cautions against assuming an added modality is useful.
- Robotics papers emphasize robustness and reproducible evaluation: *Cairn* steers a frozen VLA around changed layouts, while *One Ocean, Many Tasks* provides a disturbance-aware simulation suite for marine tasks. Both move beyond a single static task, but only Cairn reports a real-robot demonstration and that evidence is limited.
- The fallback batch query is concentrated in computer vision and machine learning as primary categories; the selected set deliberately samples language, safety, and robotics as well. This concentration describes the retrieved corpus, not field-wide research importance.

## Open Problems and Research Directions

- **Author-reported open problem:** *Attack Policy Selection* says results on synthetic transcripts need a defensible argument that the proxy distribution represents dangerous deployment behavior. **Research direction (synthesis):** evaluate attack policies in more realistic settings, include stronger target agents and properties that preserve plausible deployment behavior, and report proxy-validity arguments alongside miss rates.
- **Author-reported boundary:** *DART* is designed primarily for post-training because alternative generation uses reference answers; its study also notes one-seed post-training and possible near-duplicate contamination. **Research direction (synthesis):** test multi-seed results across model scales and domains, audit semantic duplicates, and compare variants with and without reference guidance under matched budgets.
- **Author-reported boundary:** *AgenTAP* and *Cairn* report promising visual/robotic results, but their evaluations do not establish broad physical-world generalization. **Research direction (synthesis):** test point tracking and object-trajectory steering across new sensors, object categories, environments, and longer-horizon physical tasks with consistent failure reporting.
- **Author-reported boundary:** *μ-Bench* uses simulated users, and *One Ocean, Many Tasks* evaluates in simulation. **Research direction (synthesis):** validate benchmark outcomes with human participants and physical marine platforms, then measure how well simulated task rankings predict real deployment behavior.
- **Author-reported result:** generated helper images reduced average accuracy in the tested settings, but some task outcomes improved after repeated edits. **Research direction (synthesis):** characterize which task, generator, and edit-selection conditions make generated visual aids useful, using preregistered held-out tests and calibrated measures of both benefit and harm. (*Can image generation help visual reasoning?*)

## Takeaway

The most consequential theme in this selection is evaluation quality: monitor scores depend on how attacks are generated, and agent benchmarks increasingly include authority, privacy, or interaction constraints. There are promising efficiency and robotics ideas too, but this is a notable-paper fallback rather than a defensible popularity chart; per-paper attention evidence for this older batch could not be recovered from the supplied signal file.

## Method and sources

- **Window:** The current signal-defined daily window was 2026-11-25 19:00:00–2026-11-26 19:00:00 UTC, announced 2026-11-27 01:00:00 UTC; its core AI arXiv query returned 0 entries. Following the daily fallback rule, this report uses the immediately preceding populated batch: 2026-11-24 19:00:00–2026-11-25 19:00:00 UTC, announced 2026-11-26 01:00:00 UTC. Snapshot: 2026-11-27T03:05:14Z.
- **Scope/query:** `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; arXiv API query: `(cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA) AND submittedDate:[202611241900 TO 202611251900]`. The prior-batch query returned 690 records, collected across four pages; the selected eight are new v1 submissions, not revisions.
- **Inference and signal status:** arXiv has no official trending chart. The supplied current-window signal file has `pool_size: 0`, `with_attention: 0`, and no candidates; its source counts are arXiv 0, Hugging Face 124, Hacker News 16, Semantic Scholar 0, and arXiv lookup 139, all reported with status `ok`. Those aggregates cannot be attributed to the fallback-batch papers. Per-paper scores, upvotes, points, comments, and citation counts for the selected fallback papers were therefore unavailable, not assumed to be zero. The ordering is an inferred notable-paper ranking: independent technical discussion when found, then visible scholarly/artifact context and reported evaluation relevance; recency only breaks ties. A zero or missing attention value is not evidence of unimportance.
- **Primary-page verification:** All eight selected arXiv abstract pages were checked for title, version, authors, submission timestamp, categories, and abstract. The top three papers' experimental HTML full texts were also reviewed for methods/results and stated limitations. The `web_extract` backend was unavailable in this environment, so pages were verified by direct arXiv retrieval and browser access.
- **Sources:** [Attack Policy Selection arXiv](https://arxiv.org/abs/2611.34934); [UK AI Safety Institute research page](https://www.aisi.gov.uk/research/attack-policy-selection-can-mislead-monitor-evaluators); [AISI technical blog](https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading); [MoLT arXiv](https://arxiv.org/abs/2611.34923); [Hugging Face Papers: MoLT](https://huggingface.co/papers/2611.34923); [MoLT code](https://github.com/hustvl/MoLT); [DART arXiv](https://arxiv.org/abs/2611.34928); [NeurIPS workshop listing](https://neurips.cc/virtual/2026/164465); [AgenTAP arXiv](https://arxiv.org/abs/2611.34943); [AgenTAP project](https://agentap.cs.virginia.edu); [Cairn arXiv](https://arxiv.org/abs/2611.34914); [generated-image reasoning study](https://arxiv.org/abs/2611.34935); [μ-Bench arXiv](https://arxiv.org/abs/2611.34920); [μ-Bench code](https://github.com/lqh1106/mu-bench); [OneOcean arXiv](https://arxiv.org/abs/2611.34925).
