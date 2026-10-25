# arXiv Trending AI — Friday, 23 October 2026

## Headline

Core AI categories, Friday’s 23 October announcement batch; five notable papers. The clearest selected threads are safer agent evaluation and selective use of test-time compute, with embodied-model evaluation as a related strand. Spoken agenda: first evidence-sensitive agent safety, then reasoning efficiency and adaptive memory, followed by what remains difficult to measure in robotics and video world models. arXiv has no official trending chart; this ordering is inferred from technical relevance and reported evaluation breadth, not popularity, and citation evidence is limited for papers announced only days ago. Since today is Sunday, 25 October, this daily report uses the previous announcement batch, Friday 23 October.

## Top papers (ranked)

### 1. [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650)
- **Abstract:** The authors introduce a benchmark of 300 matched safe/unsafe task pairs across six domains to test whether tool-using agents act safely when critical facts are omitted and whether they retrieve and use those facts appropriately.
- **Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu et al.
- **arXiv:** `2610.31650v1` (published 2026-10-22T17:57:04Z; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The core-AI/ML cross-list, matched-world design, six-domain scope, and ten-model evaluation make this a broad, directly relevant agent-safety benchmark; those are demonstrated-relevance signals, not popularity measures.
- **Claimed contribution:** The paper claims EpiSEM-Bench separates unsafe execution, safety boundaries, and evidence recovery; its ten-model study finds that resistance to omissions does not by itself ensure useful recovery.
- **Caveat:** The authors note that cost-conscious evaluation used fast variants for two model families and that results may not generalize to larger models in those families.
- **Announcement type:** new submission, Friday, 23 October 2026 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks; Agents & reasoning

### 2. [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667)
- **Abstract:** The authors propose selecting partial reasoning traces by directly optimizing the probability that at least one retained trace finishes correctly, balancing quality and diversity to reduce the cost of test-time scaling.
- **Authors:** Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn
- **arXiv:** `2610.31667v1` (published 2026-10-22T17:59:48Z; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Its cross-list across AI and language, explicit pass@$k$ selection objective, and comparisons on eight open-weight reasoning models place it high for methodological and empirical relevance to inference-time reasoning.
- **Claimed contribution:** The authors’ PKTP method models correlated rollout outcomes, approximates pass@$k$ with a submodular objective, and uses greedy selection; they report gains over quality-only and diversity-only pruning baselines.
- **Caveat:** The method estimates joint rollout success from partial-trace representations; the authors identify stronger representations of rollout correctness as a natural next step.
- **Announcement type:** new submission, Friday, 23 October 2026 announcement batch
- **Themes:** Efficient inference & systems; Agents & reasoning; Evaluation & benchmarks

### 3. [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670)
- **Abstract:** The authors propose a training-free metric that measures alignment between sensory representations and physical motion, reporting positive correlations with downstream robot task success across embodied-model families.
- **Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- **arXiv:** `2610.31670v1` (published 2026-10-22T17:59:51Z; categories: `cs.CV`, `cs.LG`, `cs.RO`)
- **Evidence for ranking:** The three-category CV/ML/robotics cross-list and evaluation across VLAs, VLMs, world-action models, and real-robot policies provide unusually broad evidence for a proposed offline capability proxy.
- **Claimed contribution:** The paper claims Sensorimotor Alignment (S²) can help prioritize embodied models before expensive closed-loop evaluation and can explain selected representation-level behaviors.
- **Caveat:** The authors emphasize that the relationship with success is correlational; they also report limited model families, benchmarks, few models per comparison, and one real-robot setting.
- **Announcement type:** new submission, Friday, 23 October 2026 announcement batch
- **Themes:** Robotics & control; Evaluation & benchmarks; Multimodal & vision-language

### 4. [METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](https://arxiv.org/abs/2610.31656)
- **Abstract:** METTA combines causal neural memory for within-episode adaptation with compact episode summaries for longer-range task inference, and the authors report results on held-out Meta-World tasks and sparse-reward PointMaze.
- **Authors:** Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah
- **arXiv:** `2610.31656v1` (published 2026-10-22T17:58:27Z; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** Its AI/ML cross-list, held-out task-family evaluation, and comparison with transformer-based baselines on long-context tasks make it a relevant test-time adaptation result.
- **Claimed contribution:** The authors propose a two-timescale memory and test-time adaptation design intended to retain useful history with linear sequence complexity rather than attending over the full trajectory.
- **Caveat:** The authors frame the experiments around fixed-task trials and identify continual or nonstationary settings, where temporal or recency information may matter, as future work.
- **Announcement type:** new submission, Friday, 23 October 2026 announcement batch
- **Themes:** Training & adaptation; Robotics & control; Efficient inference & systems

### 5. [Reading, Writing, Sharing, and Interacting with the World through Video](https://arxiv.org/abs/2610.31668)
- **Abstract:** This survey organizes video understanding, generation, unified models, and video world models as reading, writing, sharing, and interacting with latent evolving worlds, emphasizing persistent state and interaction-grounded evaluation.
- **Authors:** Shengqiong Wu, Meng Luo, Bobo Li, Ziwei Liu, Shuicheng Yan et al.
- **arXiv:** `2610.31668v1` (published 2026-10-22T17:59:50Z; categories: `cs.CV`)
- **Evidence for ranking:** The 102-page survey synthesizes models, datasets, and benchmarks across four connected video-modeling paradigms; its value here is as a field-mapping reference, not as a new experimental result.
- **Claimed contribution:** The authors propose a world-modeling lens and identify a shift from clip-level recognition and perceptual fidelity toward persistent state, controllability, physical and causal validity, and downstream decisions.
- **Caveat:** This is a literature synthesis rather than an experimental validation of the proposed taxonomy; the paper cautions that strong performance on individual video tasks does not by itself establish general world-model capability.
- **Announcement type:** new submission, Friday, 23 October 2026 announcement batch
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Robotics & control

## Trending Research Themes

- **Agent safety increasingly depends on what the agent knows before acting.** EpiSEM-Bench evaluates matched safe and unsafe worlds when safety-relevant facts disappear, and distinguishes abstention from useful evidence recovery. This is a single selected benchmark signal, not evidence that all agent-safety work has shifted to this framing.
- **Test-time efficiency is being treated as selective allocation of computation and memory.** PKTP decides which partial reasoning traces receive further compute, while METTA divides adaptation between within-episode memory and episode-level summaries. They address different settings, but both make test-time resource allocation part of the method.
- **Capability evaluation is reaching beyond passive perception and one terminal score.** Sensorimotor Alignment relates representations to physical trajectories and downstream robot success; EpiSEM-Bench separates safety, task completion, and recovery. These are distinct evaluation proposals rather than a shared benchmark or validated general solution.
- **Video world modeling foregrounds persistent state and physical validity.** The video survey argues for interaction- and decision-grounded tests alongside visual coherence. This is a survey synthesis, not an independent empirical trend count.
- **The announcement pool is category-imbalanced.** In the 449-record date-bounded query, overlapping category tags were most frequent for `cs.AI` (169) and `cs.LG` (151), followed by `cs.CV` (101) and `cs.CL` (89); these counts overlap and are not exclusive paper totals. The five-paper selection should not be read as a balanced sample of the entire batch.

## Open Problems and Research Directions

- **Open problem (reported by EpiSEM-Bench):** Resistance to missing evidence does not necessarily translate into useful recovery, and agents vary in whether they retrieve facts and then act appropriately. **Research direction (synthesis):** test recovery policies on new tool APIs and longer workflows while jointly measuring prohibited actions, legitimate completion, and recovery cost. [EpiSEM-Bench](https://arxiv.org/abs/2610.31650)
- **Open problem (author-stated by PKTP):** The pruning objective depends on how well partial-trace representations indicate eventual correctness; the authors identify better representations as a future-work need. **Research direction (synthesis):** evaluate representation and joint-success calibration under shifts in task type, verifier, and candidate-pool size. [Direct Pass@$k$](https://arxiv.org/abs/2610.31667)
- **Open problem (author-stated by Sensorimotor Alignment):** Its correlation with task success is not causal, and current evaluation covers few models and a limited number of real-robot settings. **Research direction (synthesis):** run prospective model-selection studies across additional embodiments, then test whether directly optimizing the metric improves closed-loop success. [Sensorimotor Alignment](https://arxiv.org/abs/2610.31670)
- **Open problem (author-stated by METTA):** The current fixed-task trial setup does not establish fast adaptation as task structure or rewards change over time. **Research direction (synthesis):** compare recency-aware memory with the reported episode summaries in nonstationary task streams, measuring adaptation speed and forgetting. [METTA](https://arxiv.org/abs/2610.31656)
- **Open problem (survey synthesis):** Long-horizon state consistency, physical and causal grounding, and standardized evaluation remain unresolved across video world models. **Research direction (synthesis):** benchmark state persistence and action-conditioned counterfactuals separately from visual realism, and report degradation as the rollout horizon grows. [Video world-model survey](https://arxiv.org/abs/2610.31668)

## Takeaway

The selected papers point to a practical agenda: evaluate agents on whether they gather the evidence needed for safe action, and spend inference-time compute or memory where it improves decisions. Embodied and video-model evaluation is also moving toward state, motion, and interaction rather than visual plausibility alone. These are early preprint claims from one announcement batch; neither the ordering nor the small selected sample establishes field-wide popularity or settled capability.

## Method and sources

- **Window:** daily, exact start and end date 2026-10-23; snapshot 2026-10-25T17:09:02Z. The latest batch on Sunday was the previous Friday, 23 October 2026; selected records show arXiv submission timestamps on 22 October UTC, while category recent pages list them in the Friday 23 October announcement batch.
- **Scope/query:** one date-bounded arXiv API query across `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`, using `submittedDate:[20261022 TO 20261024]`; it returned 449 records, all with published dates on 2026-10-22. The overlapping category appearances were: `cs.AI` 169, `cs.LG` 151, `cs.CV` 101, `cs.CL` 89, `cs.RO` 57, `stat.ML` 20, `cs.MA` 15, and `cs.NE` 2.
- **Verification:** each selected arXiv abstract page was checked for title, abstract, version, authors, and categories; full HTML text was read for the five selected papers to support method, evaluation, and caveat claims. The category recent pages confirmed Friday, 23 October as the latest announcement batch across the configured categories.
- **Inference method:** arXiv supplies no official trending chart. Because citation and independent-attention signals were too sparse to support a popularity ordering, this is a “notable recent papers” list ordered by cross-category relevance and the breadth/concreteness of author-reported methods and evaluations. Semantic Scholar citation metadata was not available in this snapshot; no downloads, reads, or view counts are claimed.
- **Primary sources:** [arXiv API query](https://export.arxiv.org/api/query?search_query=%28cat%3Acs.AI+OR+cat%3Acs.LG+OR+cat%3Astat.ML+OR+cat%3Acs.CL+OR+cat%3Acs.CV+OR+cat%3Acs.RO+OR+cat%3Acs.NE+OR+cat%3Acs.MA%29+AND+submittedDate%3A%5B20261022+TO+20261024%5D&sortBy=submittedDate&sortOrder=descending&start=0&max_results=2000); arXiv recent listings for [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), and [cs.MA](https://arxiv.org/list/cs.MA/recent); abstract and full-text pages linked above.