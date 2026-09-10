# arXiv Trending AI — 2026-09-08 announcement batch

## Headline
The strongest signal in this batch is a move from “bigger model” stories toward operational reliability: agents are being given explicit procedural memory and claim-level verification, while robotics and video-generation papers focus on making learned behavior controllable under real-world variation. This is an inferred snapshot, not an official arXiv popularity chart.

## Top papers (ranked)

### 1. [Procedural Graphs: Self-Evolving Execution Structures for LLM Agents](https://arxiv.org/abs/2609.09153)
- **Abstract:** The paper introduces self-evolving procedural graphs that organize what-to-do knowledge and guide an LLM agent’s next action from a localized procedure node, while retaining rejected edits to discourage repeated failures.
- **Authors:** Yuxing Lu, Yicheng Chen, Shanchan Wu, Sercan Ö. Arık
- **arXiv:** `2609.09153v1` (published 2026-09-08 17:59 UTC; categories: `cs.AI`, `cs.CL`, `cs.MA`)
- **Evidence for ranking:** Strongest independent attention found in this batch: an arXiv HTML version, DAIR.AI paper page, Hacker News discussion, and an additional technical explainer appeared in search results within two days. Semantic Scholar was checked and reported 0 citations and 0 influential citations, so the ranking is based on corroborated discussion rather than citation momentum.
- **Claimed contribution:** The authors report consistent gains over memory-based baselines across datasets, task types, and LLMs, with further gains from self-evolution; they also report that graphs can be built from a minimal skeleton or repair a flawed expert prior.
- **Caveat:** The evidence is preprint-level and the abstract does not establish how well the approach transfers beyond the tested tasks and models.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Evaluation & benchmarks

### 2. [ReCite: Agentic Reasoning for Faithful Citation](https://arxiv.org/abs/2609.09156)
- **Abstract:** ReCite replaces similarity-only citation recommendation with claim-level query planning, evidence checking, and reflective correction loops trained on synthesized reasoning trajectories.
- **Authors:** Yuyang Huang, Bobo Li, Jiajia Song, Yuzhe Ding, Chong Teng, et al.
- **arXiv:** `2609.09156v1` (published 2026-09-08 17:59 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Independent arXiv HTML, Academus, arXivTLDR, and agentic-design.ai results were found. The paper is marked “Findings of EMNLP 2026.” Semantic Scholar requests were rate-limited after a successful sparse lookup, so no citation count is claimed.
- **Claimed contribution:** The authors report that the lightweight framework exceeds large generative models on strict citation accuracy by verifying logical claim–evidence consistency rather than semantic overlap.
- **Caveat:** The evidence depends on the paper’s citation benchmarks and synthesized training trajectories; real scholarly workflows and unseen venues remain less tested in the abstract evidence.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Safety & alignment

### 3. [Copying explains the collective behavior of AI agents in the wild](https://arxiv.org/abs/2609.09150)
- **Abstract:** Using a public record of thousands of short-lived agents editing a wiki, the paper finds that simple proportional-copying models reproduce much of the observed collective structure and imply strong sensitivity to early visible conventions.
- **Authors:** Giordano De Marzo, Nicola Alboré, David Garcia
- **arXiv:** `2609.09150v1` (published 2026-09-08 17:59 UTC; categories: `cs.MA`, `cond-mat.stat-mech`, `cs.CL`)
- **Evidence for ranking:** Search results included arXiv, ScholarFeed, papers.cool, SimpleProg, and ScienceAlert coverage; this was the broadest non-specialist attention signal found. No citation count is asserted because Semantic Scholar was rate-limited.
- **Claimed contribution:** The authors show that copying locally visible options can explain page concentration, name construction, and internally consistent subcultures, and that early writers can steer later conventions.
- **Caveat:** The study analyzes one unusual public interaction episode; its generative models may not describe agents with different interfaces, objectives, or memory.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 4. [Proxy Policy Steering](https://arxiv.org/abs/2609.09148)
- **Abstract:** Proxy Policy Steering adapts a frozen generalist robot policy at inference time by adding a calibrated velocity-space residual from reference and task proxy policies.
- **Authors:** Chuanruo Ning, Tianrui Wang, Wei-Chiu Ma, Kuan Fang
- **arXiv:** `2609.09148v1` (published 2026-09-08 17:59 UTC; category: `cs.RO`)
- **Evidence for ranking:** Independent project pages and multiple paper-index results corroborated the method; the project page exposes implementation-oriented detail. Search results also identify a CoRL 2026 submission. Citation counts were unavailable because Semantic Scholar was rate-limited.
- **Claimed contribution:** The authors report a 53 percentage-point average success-rate lift over a pi 0.5 base policy across 8 real-world and 4 simulation tasks, while preserving base behaviors.
- **Caveat:** These are author-reported results from a preprint; the size and diversity of the task suite may not predict deployment robustness.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Robotics & control; Training & adaptation; Efficient inference & systems

### 5. [SignRefine: Adapting Foundational Video Models for Sign Language Generation](https://arxiv.org/abs/2609.08496)
- **Abstract:** SignRefine adapts a pretrained video diffusion transformer with spatially grounded local adapters and a new NVSign dataset to generate more comprehensible signing from 2D keypoints.
- **Authors:** Anton Pelykh, Edward Fish, Ozge Mercanoglu Sincan, Richard Bowden
- **arXiv:** `2609.08496v1` (published 2026-09-08 09:38 UTC; category: `cs.CV`)
- **Evidence for ranking:** arXiv HTML, an ECCV 2026 poster listing, and the senior author’s publication page independently corroborate the paper and venue visibility. No citation count is claimed.
- **Claimed contribution:** The authors report up to 30% improvement in hand-pose precision over the strongest baseline and preference from sign-language users in more than 80% of comparisons.
- **Caveat:** The abstract does not specify the full user-study protocol or how comprehensibility varies across sign languages and signing communities.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Multimodal & vision-language; Data & synthetic data; Evaluation & benchmarks

### 6. [Temporal State Transport in Video Generation: Diagnosing and Correcting Spectral Imbalance](https://arxiv.org/abs/2609.08505)
- **Abstract:** The paper diagnoses fragmented transport and over-mixing in temporal attention using Spectral Tension, then applies a training-free regulator to improve video consistency without fine-tuning.
- **Authors:** Luyao Tang, Bingjun Luo, Dong Yi, Jialin Guo, Haoning Xi, et al.
- **arXiv:** `2609.08505v1` (published 2026-09-08 09:52 UTC; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The arXiv record reports an ICML 2026 F2S Workshop Best Paper award and links public code. Semantic Scholar returned 0 citations and 0 influential citations in the available lookup.
- **Claimed contribution:** The authors report improved temporal consistency and visual quality on pretrained video-generation models through selective, training-free correction.
- **Caveat:** The result is dependent on the chosen pretrained models and temporal diagnostics; broader video domains may expose different failure regimes.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Evaluation & benchmarks

### 7. [Do Reviewers Still Reward Lexical Complexity? A Frozen-Rater Study of Preference Drift in 124K ICLR Reviews](https://arxiv.org/abs/2609.08475)
- **Abstract:** A frozen-rater design separates changes in submissions from changes in human review preferences and finds that human reward for non-domain lexical complexity declined while a fixed LLM rater retained its earlier association.
- **Authors:** Jiabin Zheng
- **arXiv:** `2609.08475v1` (published 2026-09-08 09:19 UTC; categories: `cs.CL`, `cs.DL`, `cs.LG`)
- **Evidence for ranking:** The arXiv HTML exposes machine-readable results and the paper provides code and records; search results independently surfaced the study. Citation counts were unavailable.
- **Claimed contribution:** The authors report results from 32,638 submissions and 124,615 human reviews, with a controlled frozen-rater comparison and placebo tests.
- **Caveat:** The observational corpus is ICLR-specific and the frozen rater was generated in one 2025 window, so the findings should not be generalized to all peer review.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Evaluation & benchmarks; Safety & alignment; Training & adaptation

### 8. [TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](https://arxiv.org/abs/2609.09158)
- **Abstract:** TANGO predicts 29-DoF humanoid actions from language and egocentric RGB, trained entirely in simulation and deployed zero-shot on a Unitree G1 for cluttered-scene traversal.
- **Authors:** Anqi Li, Yuxin Chen, Zhaobo Li, Zhuo Cao, Junli Ren, et al.
- **arXiv:** `2609.09158v1` (published 2026-09-08 17:59 UTC; categories: `cs.RO`, `cs.AI`)
- **Evidence for ranking:** It is among the batch’s newest high-salience embodied-AI papers and reports a real-robot deployment; no independent attention or citation momentum was verified, so it is ranked below papers with stronger corroboration.
- **Claimed contribution:** The authors report state-of-the-art simulation navigation and zero-shot real-world traversal without real-world navigation training data.
- **Caveat:** The abstract does not establish performance across robot embodiments, environments, or long-duration operation.
- **Announcement type:** new submission, 2026-09-08 announcement batch
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

## Trending research themes
- **Agents are gaining explicit operational structure.** Procedural Graphs targets long-horizon action sequencing; ReCite turns retrieval into claim-level verification; the collective-behavior study shows why local context and early conventions matter for multi-agent systems.
- **Embodied models are being adapted without rewriting the base.** Proxy Policy Steering and TANGO both seek generalist behavior that remains usable under new tasks or environments, but via different routes: inference-time residual steering versus simulation-trained whole-body action prediction.
- **Video and vision-language work is shifting toward controllability and usable outputs.** SignRefine focuses on hand/face articulation for a communication task, while Temporal State Transport targets temporal state balance rather than isolated frame quality.
- **Evaluation itself is becoming a research target.** ReCite evaluates citation faithfulness, the frozen-rater study evaluates evaluator drift, and Procedural Graphs tests resilience and self-evolution rather than only one-shot task accuracy.

## Research opportunities

### Potential research areas
- **Authority- and evidence-aware agent memory:** combine procedural graphs with claim/evidence verification, testing whether agents can distinguish “what to do” from “what is authorized” and “what is supported” (Procedural Graphs; ReCite).
- **Multi-agent convention formation and steering:** extend the copying models to controlled interfaces, memory regimes, and adversarial early interventions (Copying explains the collective behavior...).
- **Generalist embodied policies under distribution shift:** compare residual steering, visual calibration, and whole-body language-conditioned control on shared real-robot tasks (Proxy Policy Steering; TANGO; SyncWorld).

### Unsolved problems
- **Out-of-distribution reliability:** the selected papers mainly report benchmark or limited deployment settings; cross-embodiment, cross-venue, and long-horizon reliability remain open (TANGO; Proxy Policy Steering; Procedural Graphs).
- **Faithfulness versus fluent similarity:** ReCite addresses logical support, but robust citation verification under ambiguous claims, conflicting sources, and incomplete literature remains unresolved (ReCite).
- **Evaluator drift:** the frozen-rater result suggests agreement with historical human scores can hide changed preferences; maintaining current, manipulation-resistant evaluators is still open (Do Reviewers Still Reward Lexical Complexity?).

### Potential research directions
- Build a shared agent benchmark with procedural tasks, authority receipts, citation claims, and delayed consequences; report both task success and unsafe/unsupported actions (Procedural Graphs; ReCite).
- Test whether the same inference-time adaptation principle works across robot policies and video generators, with held-out embodiments, environments, and user-centered metrics (Proxy Policy Steering; SignRefine; Temporal State Transport).
- Re-run the frozen-rater design across venues, languages, and model generations, preregistering the feature families and preserving raw review-level data where permitted (Do Reviewers Still Reward Lexical Complexity?).

## Takeaway
Today’s batch is notable less for a single model-scale breakthrough than for methods that make AI behavior inspectable, steerable, and robust to context: procedural memory, evidence checks, local adaptation, and temporal diagnostics. The “hotness” signal is necessarily noisy because these papers are only one to two days old; most have zero observable citations, so the ordering reflects corroborated discussion, venue/code signals, cross-category relevance, and author-reported evidence—not readership.

## Method and sources
- **Window:** daily; latest available arXiv announcement batch was 2026-09-08. No 2026-09-09 batch was returned by the arXiv API at the 2026-09-10 00:10 UTC snapshot, so this report uses the most recent batch rather than returning an empty report.
- **Scope:** `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`, retaining cross-listed AI contributions.
- **Ranking:** inferred from independent search corroboration, public code/project or venue signals, cross-list breadth, real-world evaluation, and sparse Semantic Scholar checks. arXiv has no official trending chart. Semantic Scholar reported zero citations/zero influential citations for `2609.09153` and `2609.08505`; further requests were rate-limited, so missing counts are explicitly not treated as zero.
- **Primary source:** arXiv API query and each linked abstract page. Additional corroboration is linked in search results for Procedural Graphs, ReCite, Proxy Policy Steering, SignRefine, Copying, and the frozen-rater study.
- **Snapshot:** 2026-09-10 00:10 UTC.
