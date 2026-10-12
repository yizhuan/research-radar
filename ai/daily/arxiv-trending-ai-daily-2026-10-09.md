# arXiv AI papers — Friday, 9 October 2026

Eight notable papers from the latest AI-category announcement batch: the strongest shared thread is making agent behavior more measurable and governable, alongside progress in robot world models and inference efficiency. Quick agenda: agent monitoring and safety first, then benchmark validity, robotics, and KV-cache compression. This is an inferred editorial selection, not an official arXiv trending chart: arXiv publishes no popularity ranking, and the papers are too new for meaningful citation evidence (Semantic Scholar showed zero citations and zero influential citations for all eight at the 12 October snapshot).

Today is Monday, 12 October 2026; the latest announcement batch visible across the eight configured AI categories is Friday, 9 October. The arXiv API’s `published` timestamps for these new v1 papers fall on 8 October UTC, before the Friday announcement batch.

## Top papers (ranked)

### 1. [Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception](https://arxiv.org/abs/2610.12445)
- **Abstract:** The authors train activation probes on a large falsehood dataset and report strong detection results for agentic sabotage and hidden-goal deception, including up to 98.8% AUC on SHADE-Arena and up to 99.7% in one introspective evaluation.
- **Authors:** Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba, Adam Gleave, Chris Cundy
- **arXiv:** `2610.12445v1` (published 2026-10-08T17:58:13Z; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** Selected first for its direct relevance to monitoring capable agents and its reported evaluations across ordinary and hidden-goal deception settings; the authors also release the FIBS dataset. No checked popularity signal distinguishes it from the other new papers.
- **Claimed contribution:** The paper claims that probes aggregating signals across model layers and tokens can scale to frontier-monitoring settings and detect some deception not evident from the transcript alone.
- **Caveat:** The authors say FIBS contains little reasoning (5.5% of rows), is mostly off-policy, and is largely artificial; the reported results do not establish reliable deployment performance on naturally occurring deception.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Safety & alignment; Interpretability; Evaluation & benchmarks

### 2. [OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport](https://arxiv.org/abs/2610.12375)
- **Abstract:** OnTrack compares an agent’s evolving, dependency-aware execution graph with successful reference runs, aiming to flag or stop failures online; on SWE-bench trajectories, the authors report improved early ranking of failing runs and compute savings from an abort policy.
- **Authors:** Babak Barazandeh, Connor Swanson, Chinmay Kulkarni, Nikhil Mungel
- **arXiv:** `2610.12375v1` (published 2026-10-08T17:32:08Z; categories: `cs.AI`, `cs.CL`, `cs.CY`, `cs.LG`)
- **Evidence for ranking:** Ranked near the top for an operational agent-safety method with an explicit low-latency claim and measured early-warning results; its cross-listing spans AI, language, and machine learning. No independent attention metric was verified.
- **Claimed contribution:** The authors present a streaming optimal-transport monitor that can operate with different levels of prior information, from successful reference traces down to event logs alone.
- **Caveat:** The headline outcome results are on SWE-bench trajectories; performance in other agent domains and live deployments is not established by that evaluation.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 3. [Searching for “Harmful Refusal”: A Psychometric Audit of an AI Safety Benchmark](https://arxiv.org/abs/2610.12409)
- **Abstract:** The authors test whether HELM Safety’s harmful-refusal scores measure one coherent attribute; their analyses find saturation in three candidate datasets and evidence that HarmBench scores do not isolate a single attribute.
- **Authors:** Christopher M. Stewart, Preston Botter, Natalie Sarabosing, Muye Zhang, Rachel Phinnemore, et al.
- **arXiv:** `2610.12409v1` (published 2026-10-08T17:46:43Z; categories: `cs.AI`)
- **Evidence for ranking:** Included for a concrete measurement-science challenge to how safety results are aggregated, complementing the two monitoring papers above. It is a new single-category submission; no verified attention signal supports a popularity claim.
- **Claimed contribution:** The paper argues that a safety score should demonstrate construct validity before being interpreted as a measurement of one attribute or used to compare models.
- **Caveat:** The audit focuses on four HELM Safety datasets and the HarmBench analysis; its findings do not by themselves establish how every safety benchmark behaves.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Safety & alignment; Evaluation & benchmarks

### 4. [On the estimation and validity of AI time horizons—a statistical look at the METR plot](https://arxiv.org/abs/2610.12466)
- **Abstract:** Using 228 software tasks and 26 AI systems, the authors refit METR time horizons with spline and item-response models, finding a nonlinear mapping between human task time and estimated AI difficulty and proposing diagnostic plots for interpreting the metric.
- **Authors:** Drew T. Nguyen, William Fithian
- **arXiv:** `2610.12466v1` (published 2026-10-08T17:59:50Z; categories: `cs.AI`)
- **Evidence for ranking:** Included for its direct examination of a widely discussed capability metric, with a defined dataset and cross-validated scoring-rule comparisons described in the paper. No verified popularity signal separates it from its batch peers.
- **Claimed contribution:** The authors provide alternative time-horizon estimates and construct-validity diagnostics, and caution that equal multiplicative jumps in “human time” need not represent equal difficulty changes.
- **Caveat:** The analysis is anchored to METR’s software-engineering task set; the authors specifically recommend interpreting time horizons together with diagnostics, especially when extending the benchmark.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Evaluation & benchmarks

### 5. [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](https://arxiv.org/abs/2610.12468)
- **Abstract:** DreamTrue combines geometric action conditioning, counterfactual trajectory post-training, and a learned video reward model to improve robot-world-model predictions; the authors report first place in the AgiBot World Challenge 2026 world-model track and a lower human-assessed interaction-defect rate.
- **Authors:** Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, et al.
- **arXiv:** `2610.12468v1` (published 2026-10-08T17:59:51Z; categories: `cs.RO`, `cs.CV`)
- **Evidence for ranking:** Selected for its combination of action-conditioned prediction and evaluation against interaction defects, plus the paper’s stated challenge result; it brings robotics into a batch otherwise heavy on agent evaluation. The contest placement is the authors’ report, not independent validation.
- **Claimed contribution:** The authors claim counterfactual post-training broadens the model’s action/contact coverage and improves physical plausibility without paired ground-truth futures.
- **Caveat:** The abstract’s quantitative evaluation and challenge result are tied to AgiBot; transfer to other robot platforms and broader task distributions remains to be demonstrated.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

### 6. [BrickBench: Evaluating Agentic Brick Design](https://arxiv.org/abs/2610.12452)
- **Abstract:** BrickBench evaluates text-conditioned agents that must design LEGO assemblies satisfying semantic, design, and physical-build constraints, with scores for validity, alignment, and design across three settings.
- **Authors:** Peter Kulits, Yiqing Xu, R. Kenny Jones, Cordelia Schmid, Jiajun Wu
- **arXiv:** `2610.12452v1` (published 2026-10-08T17:58:56Z; categories: `cs.AI`, `cs.CV`, `cs.GR`)
- **Evidence for ranking:** Included as a concrete benchmark and open environment for embodied, constraint-heavy agent design; its three-category cross-listing broadens the sample beyond language-agent tasks. Search discovery is not treated as evidence of readership.
- **Claimed contribution:** The authors introduce BrickBench and BrickAgent, and report that current leading agents meet many verifiable requirements but remain below human designs.
- **Caveat:** The evaluation is specific to LEGO-part selection and assembly; success on this benchmark alone would not establish general physical-design competence.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Multimodal & vision-language

### 7. [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration](https://arxiv.org/abs/2610.12470)
- **Abstract:** Dex-One2Many turns one human video into scene-graph constraints for reinforcement learning, then transfers a simulation-trained dexterous manipulation policy zero-shot to a real multi-fingered hand; the authors evaluate five tasks and report a larger advantage in unseen configurations.
- **Authors:** Jusuk Lee, Sungha Kim, Yeonsoo Park, Jonguk Cheon, Yoonkyo Jung, et al.
- **arXiv:** `2610.12470v1` (published 2026-10-08T17:59:58Z; categories: `cs.RO`, `cs.CV`)
- **Evidence for ranking:** Selected for an explicit real-robot transfer test and for addressing generalization beyond the demonstrated object poses and grasps; cross-listed in robotics and vision. No independent attention metric was verified.
- **Claimed contribution:** The authors claim scene-graph constraints improve guided RL exploration while supporting generalization to unseen poses and grasps from a single human video.
- **Caveat:** The reported results cover five tasks and one real multi-fingered-hand transfer setting; broader hardware and task coverage is still needed.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Robotics & control; Training & adaptation

### 8. [VFold: Symmetry-Aware Cross-Layer Value Cache Compression](https://arxiv.org/abs/2610.12338)
- **Abstract:** VFold merges similar value-cache states across transformer layers using symmetry-aware reparameterization, with the stated aim of reducing long-context KV-cache memory without architectural changes or major decoding overhead.
- **Authors:** Neha Verma, Sungwon Kim, Kenton Murray, Kevin Duh
- **arXiv:** `2610.12338v1` (published 2026-10-08T17:14:28Z; categories: `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Included as the batch’s systems-oriented entry: the method targets a concrete long-context memory bottleneck and is described as composable with cache quantization and key pruning. No verified popularity measure supports its ordering.
- **Claimed contribution:** The authors propose cross-layer value-cache merging and claim it can combine with existing compression methods to reach higher compression ratios at minimal additional cost.
- **Caveat:** The abstract does not give a concrete compression ratio or workload-level savings figure, so the practical magnitude cannot be judged from the abstract alone.
- **Announcement type:** new submission, Friday 9 October 2026
- **Themes:** Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Agent monitoring is moving toward intervention, not just scoring.** OnTrack proposes online alerts and blocking; Caught in the Act probes internal activations for deception signals. Both are preprints, and their claims need broader, realistic deployment tests.
- **Evaluation validity is itself a research problem.** The METR time-horizon analysis questions the shape of the human-time scale; the harmful-refusal audit questions whether aggregate safety scores measure a single trait; BrickBench builds a more executable agent benchmark.
- **Robotics combines learned world models with structured interaction priors.** DreamTrue uses action-conditioned counterfactuals, while Dex-One2Many uses scene graphs to guide exploration and transfer from a human video.
- **Long-context efficiency still depends on reducing cache footprint.** VFold targets cross-layer redundancy in value states, but the abstract-level evidence does not yet quantify the practical savings.

## Open Problems and Research Directions

- **Probe robustness outside curated deception settings (author-stated limitation):** Caught in the Act notes that FIBS has little reasoning data and is largely artificial/off-policy. A useful next test is prospective evaluation on naturally occurring, on-policy agent failures, with independent labels and distribution-shift analysis.
- **Online-monitor generalization:** OnTrack’s reported outcome results use SWE-bench traces. Test false-positive and missed-failure rates across distinct agent workloads and under the monitor’s lower-information regimes, especially where no successful reference run exists.
- **Measurement validity beyond one benchmark family:** The METR and harmful-refusal papers both show why a summary score can conceal nonlinear task difficulty or multiple underlying attributes. Future studies could predefine the construct, test it on independent datasets, and report diagnostic plots and subgroup/item-level behavior before publishing a single aggregate.
- **Robot transfer under varied failures:** DreamTrue and Dex-One2Many report promising robot-task results, but their abstracts describe bounded platform/task evaluations. Evaluate under new embodiments, contact conditions, and unsuccessful interactions, and test whether gains survive real-world distribution shifts.

## Takeaway

This batch has a practical through-line: better ways to observe, evaluate, and constrain AI systems—especially agents—rather than a single new model architecture dominating the set. The most consequential claims are also the ones that most need out-of-distribution replication: deception probes on natural behavior, agent monitors beyond SWE-bench, and robot policies beyond their reported platforms and tasks.

## Method and sources

- **Window:** Daily; latest arXiv announcement batch visible on category recent pages, Friday 9 October 2026. Monday 12 October had no newer batch at the snapshot. The selected eight are new v1 submissions in that batch; arXiv API `published` timestamps are 8 October UTC.
- **Snapshot:** 2026-10-12 00:10 UTC.
- **Scope/query:** Core AI categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; broad arXiv API query across those categories, cross-list deduplication by arXiv ID, and category-recent pages to establish the announcement date. The featured eight are a selected sample, not an exhaustive list.
- **Ranking:** Inferred selection by specific research relevance, reported evaluation detail, and breadth across the configured corpus. Semantic Scholar batch lookup returned 0 citations and 0 influential citations for each of the eight; no valid popularity ranking can be derived from that snapshot. No downloads, reads, votes, or bookmarks were used.
- **Primary sources:** [arXiv cs.AI recent](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent); paper abstracts linked above. Citation cross-check: [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch).
