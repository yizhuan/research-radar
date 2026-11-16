# arXiv AI — Monday, 16 November 2026 — 5 notable recent papers

The batch leans toward agent capability and reliability: agents are being tested in real web workflows, directly editing neural weights, operating robots, and executing policy-constrained tool plans. We’ll cover those agent systems, then a mobile brain-to-text result. arXiv has no official trending chart; this ordering is inferred from checkable attention and quality signals, and citation evidence is limited for very recent papers.

## Top papers (ranked)

### 1. [Training Reasoning Models in Simulation to Natively Use Real Robots](https://arxiv.org/abs/2611.18562)
- **Abstract:** The authors train an open-weight 27B reasoning model with robot-use reinforcement learning entirely in simulation and report transfer to unseen tasks, a new robot, and real hardware, including 60% success across their real dual-arm robot trials.
- **Authors:** Jiaming Tang, Zhuoyang Zhang, Junxian Guo, Fangzhou Zhao, Yilong Zhao, et al.
- **arXiv:** `2611.18562v1` (published 2026-11-13T18:59:02Z; categories: `cs.RO`, `cs.LG`)
- **Evidence for ranking:** Independent paper notes by Lixin Xu and coverage by AREX both discuss the simulation-to-real result; the work also has a public project/code site. These sources, plus its robotics/ML cross-list, make it one of the better-corroborated papers in this batch. [Paper notes](https://davidlxu.github.io/posts/2026/11/robot-use-rl-pear-paper-notes/) · [AREX coverage](https://www.arex-research.com/articles/0df1b2e1-9f19-4802-a422-be7e3904ae5e?locale=en) · [Project](https://mit-han-lab.github.io/pear-blog/)
- **Claimed contribution:** The authors introduce PEAR and robot-use reinforcement learning, reporting that simulation-only training lets the model control real robots without demonstrations or a task-specific harness.
- **Caveat:** The authors say training covered only two simulators and a small task set; long reasoning and prompt dependence remain practical limitations.
- **Announcement type:** new submission, announcement batch 2026-11-16
- **Themes:** Robotics & control; Agents & reasoning; Training & adaptation

### 2. [WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents](https://arxiv.org/abs/2611.17955)
- **Abstract:** The authors introduce a reproducible benchmark of 300 tasks across 20 self-hosted web applications that evaluates agents using text, vision, audio, and video, and report a best task-success rate of 62.3% for the tested systems.
- **Authors:** Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han Lù, Weijian Qi, Alexander Miller, et al.
- **arXiv:** `2611.17955v1` (published 2026-11-13T09:44:48Z; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Accepted to the NeurIPS 2026 Evaluations & Datasets Track and listed on NeurIPS and OpenReview; it spans three core AI categories and provides a public benchmark site. These venue and artifact signals support its placement, not a claim of measured readership. [NeurIPS poster](https://neurips.cc/virtual/2026/poster/139782) · [OpenReview](https://openreview.net/forum?id=eMuJZXwAn1) · [Project](https://webarena-pro.github.io/)
- **Claimed contribution:** The authors present a human-validated, container-isolated benchmark intended to make diverse multimodal web-agent evaluation more reproducible.
- **Caveat:** The authors note that audio/video interaction is limited to prerecorded audio and discrete video frames; model-versus-harness comparisons also do not fully control resource use.
- **Announcement type:** new submission, announcement batch 2026-11-16
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Multimodal & vision-language

### 3. [WeightBench: Evaluating Language Models as Weight-Space Programmers](https://arxiv.org/abs/2611.18553)
- **Abstract:** The authors introduce a 42-task benchmark for testing whether language models can inspect, repair, write, reject impossible edits to, and compress neural-network weights without gradient descent; results show current strengths on small networks and substantial gaps on larger-model editing and compression.
- **Authors:** Aayush Marasini, Barsat Khadka, Nick Rahimi
- **arXiv:** `2611.18553v1` (published 2026-11-13T18:58:08Z; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** Independent coverage appeared at CASRAI and DEV Community; the paper also releases a public task registry, sandbox harness, and leaderboard. Its cross-list into AI and ML adds relevance. [CASRAI coverage](https://casrai.org/news/weightbench-evaluating-language-models-weight-space-programmers-2026) · [DEV coverage](https://dev.to/paragonaimag/weightbench-tests-language-models-as-weight-space-programmers-59d0) · [Benchmark](https://github.com/Aayush-Marasini/WeightBench)
- **Claimed contribution:** The authors define and operationalize Weight-Space Programming as a benchmarked capability across five task tracks, with metered execution and constrained edits.
- **Caveat:** The authors’ results show that reliable patching of language models and data-free compression are not yet demonstrated; GPT-6.1-Sol was also evaluated on 38 rather than all 42 tasks.
- **Announcement type:** new submission, announcement batch 2026-11-16
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 4. [Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents](https://arxiv.org/abs/2611.17880)
- **Abstract:** The authors combine verified hierarchical planning with runtime enforcement so an LLM agent can block policy-violating tool calls while using its verified plan to recover, reporting 1.7× the average task success of the strongest baselines with no specification violations on their benchmarks.
- **Authors:** Mike He, Ankush Desai, Sharad Malik, Aarti Gupta
- **arXiv:** `2611.17880v1` (published 2026-11-13T08:14:04Z; categories: `cs.AI`, `cs.SE`)
- **Evidence for ranking:** The paper is listed as a NeurIPS 2026 Oral and has a Princeton-hosted paper and poster; the venue selection and public technical materials are the principal ranking signals. [NeurIPS Orals](https://neurips.cc/virtual/2026/loc/atlanta/events/oral) · [Princeton paper](https://www.cs.princeton.edu/~dh7120/assets/papers/neurips26-soteria.pdf) · [Poster](https://www.cs.princeton.edu/~dh7120/assets/talks/SoteriaPoster.pdf)
- **Claimed contribution:** The authors propose checking an agent’s structured plan against formal specifications before tool use, then using runtime enforcement and the plan to guide recovery after a blocked action.
- **Caveat:** The authors state that specifications still require manual validation, tool contracts must accurately describe tool behavior, and automated theorem provers may not complete verification in practice.
- **Announcement type:** new submission, announcement batch 2026-11-16
- **Themes:** Safety & alignment; Agents & reasoning

### 5. [FETTUCCINE: Fast and efficient brain-to-text decoding on mobile devices](https://arxiv.org/abs/2611.18561)
- **Abstract:** The authors adapt automatic-speech-recognition models for intracortical brain-to-text decoding, reporting a 4.39% word error rate on publicly available data and mobile-device throughput up to 370× real time.
- **Authors:** Jonathan D. McCart, Pranav I. Deevi, Mehdi Azabou, Nanda H. Krishna, Caleb A. McKinney, et al.
- **arXiv:** `2611.18561v1` (published 2026-11-13T18:59:02Z; categories: `q-bio.NC`, `cs.LG`)
- **Evidence for ranking:** The work is listed as a NeurIPS 2026 paper/poster and has additional research coverage at DeekoyaAI and OpenTrain; its cross-list into machine learning and concrete mobile deployment are supporting signals. [NeurIPS poster](https://neurips.cc/virtual/2026/poster/150728) · [DeekoyaAI coverage](https://deekoyaai.in/research/cmwivjfx400023q7xd7e3225w) · [OpenTrain coverage](https://www.opentrain.ai/papers/fettuccine-fast-and-efficient-brain-to-text-decoding-on-mobile-devices--arxiv-2611.18561/)
- **Claimed contribution:** The authors report an end-to-end portable decoding framework with adaptation to neural non-stationarity and gradient-based saliency maps that align with physiological priors.
- **Caveat:** The reported evaluation uses publicly available data from one intracortical speech-neuroprosthesis user, so performance across users and longer-term deployments remains unestablished here.
- **Announcement type:** new submission, announcement batch 2026-11-16
- **Themes:** Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Agents are being evaluated on consequential actions, not only answers.** WebArena-Pro tests heterogeneous browser workflows, WeightBench tests direct edits to network parameters, and Soteria tests policy-constrained tool use. This batch suggests a shift in evaluation targets, not proof that any one method is broadly reliable.
- **Simulation-trained reasoning agents are moving toward physical control.** PEAR reports transfer from two simulated training environments to a real dual-arm robot; its own limited task coverage and slow reasoning make generalization and latency central follow-ups.
- **Efficiency is a deployment constraint across modalities.** FETTUCCINE targets mobile neural decoding, while PEAR reports lengthy per-action reasoning. The approaches are different, but together underscore that useful capability depends on end-to-end latency, not only task success.
- **Evaluation breadth is increasing, while attribution remains difficult.** WebArena-Pro widens application and modality coverage; WeightBench decomposes weight-editing capabilities into tracks. Both reveal substantial gaps, but each benchmark’s scores depend on its task design and execution setup.

## Open Problems and Research Directions

- **Author-stated — PEAR:** Training covered two simulators and a small task set, and long reasoning can make actions slow. Test broader simulator/task diversity and additional real robots; measure whether shorter reasoning can preserve success.
- **Author-stated — WebArena-Pro and Soteria:** WebArena-Pro does not yet test live audio/video interaction, while Soteria depends on manually validated specifications and faithful tool contracts. Evaluate live temporal workflows, automatic specification formalization, and recovery when tool contracts are violated.
- **Observed boundary — WeightBench and FETTUCCINE:** WeightBench reports unresolved large-model editing/compression tasks, while FETTUCCINE’s evaluation is based on one user. Run complete matched benchmark suites across models and multi-user, longitudinal neuroprosthesis evaluations with accuracy, latency, and adaptation measured together.
- **Synthesis — all five:** Compare capability gains under matched compute, repeated trials, and realistic failure recovery. This would help separate better underlying models from added samples, stronger harnesses, or more permissive task conditions.

## Takeaway

The clearest common signal is a move toward testing AI systems as operators: using tools, changing model parameters, and controlling robots under explicit constraints. These papers offer concrete benchmarks and early demonstrations, but their strongest results remain bounded by small or controlled evaluations, uneven resource comparisons, or limited deployment populations.

## Method and sources

- **Window:** daily arXiv announcement batch for Monday, 2026-11-16 (start and end date: 2026-11-16). Snapshot: 2026-11-16 17:09 UTC. The latest-listing pages showed Monday, 16 November 2026; the five selected papers’ arXiv version pages record first submissions on 2026-11-13.
- **Scope/query:** `cs.AI OR cs.LG OR stat.ML OR cs.CL OR cs.CV OR cs.RO OR cs.NE OR cs.MA`. The eight `new` category listings were checked and cross-list duplicates removed (402 unique non-replacement IDs in those listings). An arXiv API query over the same categories, sorted by submitted date and filtered to 2026-11-13, returned 324 metadata records; the selected papers were individually verified on their arXiv abstract pages. The three highest-ranked papers were also read in arXiv HTML for results and limitations.
- **Inference:** ranked by a disclosed mix of independent technical discussion, conference/track selection, cross-category relevance, and public reproducibility artifacts; recency was not treated as popularity. The list is labeled “notable recent papers” because independent attention and citation evidence are sparse. A batched Semantic Scholar Graph query was rate-limited and returned no usable citation records, so no citation counts were used.
- **arXiv listings:** [cs.AI](https://arxiv.org/list/cs.AI/new), [cs.LG](https://arxiv.org/list/cs.LG/new), [stat.ML](https://arxiv.org/list/stat.ML/new), [cs.CL](https://arxiv.org/list/cs.CL/new), [cs.CV](https://arxiv.org/list/cs.CV/new), [cs.RO](https://arxiv.org/list/cs.RO/new), [cs.NE](https://arxiv.org/list/cs.NE/new), [cs.MA](https://arxiv.org/list/cs.MA/new).
- **Paper and corroborating sources:** each paper entry links to its canonical arXiv abstract and the specific external sources used for its placement. Independent discussion and venue records indicate attention or selection, not readership statistics.
