# AI arXiv daily | Friday, 13 November 2026 batch | 10 notable papers

This batch has a clear agent-reliability thread: energy-based puzzle reasoning, program search for semi-supervised learning, policies trained from partial verification, and benchmarks for evidence provenance and changing environments. I’ll cover those signals, then a robotics result, an engineering-surrogate pair, and agent infrastructure. arXiv has no official trending chart; this is an inferred ranking from checkable discussion, conference/publication signals, citations, and artifacts, with limited citation evidence for papers this recent.

## Top papers (ranked)

### 1. [Classical Energies Learn to Reason 1,000x Faster than Looped Models](https://arxiv.org/abs/2611.17309)
- **Abstract:** The authors introduce CRAM, a learned Hopfield–Tank energy for constraint puzzles, reporting near-perfect Sudoku-Extreme and Maze-Unique accuracy after 42 ms and 132 ms of training, respectively, and at least 282× fewer inference FLOPs than looped baselines on the studied tasks.
- **Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **arXiv:** `2611.17309v1` (published 2026-11-12 18:56:56 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Several checkable signals appeared immediately: Ken Ashe published a technical discussion, World Neural posted a separate paper summary, and the authors released a public implementation. No current Semantic Scholar citations were reported at the snapshot; these are discussion and artifact signals, not readership statistics.
- **Claimed contribution:** The authors train an explicit energy directly from solved puzzles and report data-efficient reasoning on Sudoku, maze, N-Queens, and graph-coloring tasks.
- **Caveat:** The authors caution that the tested puzzles are unusually well matched to the pairwise energy; high scores do not establish scaling to harder tasks such as ARC-AGI, where learning latent quantities remains open.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Agents & reasoning; Efficient inference & systems

### 2. [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323)
- **Abstract:** AgentSSL frames semi-supervised learning as agentic program search and reports that generated pipelines beat tuned human-engineered baselines in 8 of 12 settings, while selection by the agent's feedback metric can reduce performance by as much as 47%.
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **arXiv:** `2611.17323v1` (published 2026-11-12 18:59:06 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The arXiv record lists NeurIPS 2026, with a matching official NeurIPS poster and OpenReview record; the authors also provide a project site and a 16,977-program selection benchmark. These are checkable quality/artifact signals, not popularity counts.
- **Claimed contribution:** The authors formulate semi-supervised learning as search over executable programs and introduce ProgramSelectBench to measure how well agents choose among candidate pipelines.
- **Caveat:** The paper reports that the supervised AgentSL variant matches AgentSSL on both ecology tasks; its search is biased toward SSL, and reliable program selection without labels remains unresolved.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Agents & reasoning; Data & synthetic data; Evaluation & benchmarks

### 3. [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://arxiv.org/abs/2611.17287)
- **Abstract:** NOPO formalizes settings where a verifier can reliably identify failures but cannot certify apparent successes, and updates a policy by suppressing trusted negatives rather than treating unverified positives as rewards.
- **Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- **arXiv:** `2611.17287v1` (published 2026-11-12 18:52:33 UTC; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** The arXiv record identifies acceptance at NeurIPS 2026 as a Spotlight, corroborated by the official NeurIPS poster page. No current Semantic Scholar citations were reported at the snapshot; the conference signal, rather than citation momentum, supports its placement.
- **Claimed contribution:** The authors combine reference-relative suppression of verifier-negative samples with group-level weighting and report pass@k gains across code, logic, and math evaluations using unit-test, constraint, and LLM-based verifiers.
- **Caveat:** The authors state that negative-only learning specifies what to avoid but not where removed probability mass should move; using partial positive evidence without losing robustness remains future work.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Training & adaptation; Safety & alignment; Evaluation & benchmarks

### 4. [Collaborative Task Allocation for Heterogeneous Multi-Robot Systems Through Iterative Clustering](https://arxiv.org/abs/2611.17213)
- **Abstract:** The paper introduces iterative clustering to split multi-robot task allocation into smaller assignments, proves monotonic utility improvement, and reports simulation gains over several heuristic baselines.
- **Authors:** David R. Martin, Brooks A. Butler, Scott Nivison, Magnus Egerstedt, Mohammad Abdullah Al Faruque, Pramod Khargonekar
- **arXiv:** `2611.17213v1` (published 2026-11-12 18:10:27 UTC; categories: `cs.RO`)
- **Evidence for ranking:** Semantic Scholar reports 10 citations and 1 influential citation as current totals; the arXiv record links the paper to IEEE Robotics and Automation Letters and ICRA 2026, and the authors provide code. The journal/conference work predates this arXiv posting, so citation totals are not evidence of citations gained in this batch.
- **Claimed contribution:** The authors propose random and heuristic iterative clustering variants, prove assignment utility rises monotonically, and report scalable simulations up to 1,000 robots and 500 tasks.
- **Caveat:** The reported evaluation is simulation-based; the authors identify decentralized implementations and dynamic or uncertain environments as future work.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Robotics & control

### 5. [Unibuc - NLP at "Voight-Kampff" Generative AI Detection PAN 2025](https://arxiv.org/abs/2611.16612)
- **Abstract:** The team compares LLM-embedding classifiers and fine-tuned models for PAN 2025 AI-text detection, reporting about 99.4% F1 for a classical-model ensemble on the sensitivity task and more modest results on human-AI collaborative text classification.
- **Authors:** Teodor Marchitan, Claudiu Creanga, Liviu P. Dinu
- **arXiv:** `2611.16612v1` (published 2026-11-12 10:49:03 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Semantic Scholar reports 5 citations and 1 influential citation as current totals; a matching PAN at CLEF 2025 proceedings paper is independently available through CEUR-WS. This is an arXiv posting of earlier competition work, so these citations do not establish a new burst in the present batch.
- **Claimed contribution:** The authors report that majority voting over LightGBM, XGBoost, logistic regression, and SVM is comparable to fine-tuning for Subtask 1; their feature-fusion approach for Subtask 2 performs modestly.
- **Caveat:** The paper's error analysis highlights AI-generated fiction as difficult to distinguish; human-AI collaborative text classification also remains weak, with reported macro-F1 and recall around 0.43.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Evaluation & benchmarks; Safety & alignment

### 6. [Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation](https://arxiv.org/abs/2611.17161)
- **Abstract:** By replacing facts in retrieved passages with counterfactual variants, the authors estimate that some cited claims come from parametric memory rather than retrieved context and find that standard natural-language-inference checks do not reliably detect this mismatch.
- **Authors:** Tanzeel Abbas, Tehseen Zia, David Windridge
- **arXiv:** `2611.17161v1` (published 2026-11-12 17:39:14 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Multiple recent third-party write-ups surfaced, including SyncAI News, Bharat Hunt, Agentic Design, and CASRAI. Semantic Scholar reports no current citations at the snapshot; these write-ups are attention signals, not validation of the method.
- **Claimed contribution:** The authors propose counterfactual value substitution for separating retrieved facts from model-supplied parametric facts, compare ten attribution methods, and report that their best detector is not yet accurate enough to act on.
- **Caveat:** The tested model set covers five sizes from one family and one comparator family; the authors say the method measures what a model knew rather than what it actually used, leaving provenance separation open.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Retrieval & knowledge; Evaluation & benchmarks; Interpretability

### 7. [LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](https://arxiv.org/abs/2611.17267)
- **Abstract:** GeoWorld and LiveGeo create an evolving geographic environment and benchmark where agents must gather evidence, check whether it remains valid, and revise plans; the authors report that strong static performance does not ensure dynamic reliability.
- **Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li et al.
- **arXiv:** `2611.17267v1` (published 2026-11-12 18:45:58 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Recent summaries appeared from World Neural, AI Hot, and CASRAI. Semantic Scholar reports no current citations at the snapshot; the outside coverage is a modest attention signal, not evidence that the benchmark is widely adopted.
- **Claimed contribution:** The authors release GeoWorld with verifiable evolving state histories and LiveGeo tasks that test active information gathering, evidence revalidation, and replanning.
- **Caveat:** The evidence is specific to the proposed geographic tasks; the abstract does not establish reliability in other dynamic environments or real-world deployments.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge

### 8. [ISLA: A Coordinate-Free, Measure-Weighted Transformer for Boundary-Driven PDEs](https://arxiv.org/abs/2611.17141)
- **Abstract:** ISLA is a measure-weighted slice-attention transformer for steady boundary-driven PDEs that builds in rigid-motion and unit invariance and reports strong results on aerodynamic surrogate benchmarks.
- **Authors:** Peter Sharpe
- **arXiv:** `2611.17141v1` (published 2026-11-12 17:30:03 UTC; categories: `cs.LG`, `cs.CE`, `math-ph`, `physics.flu-dyn`)
- **Evidence for ranking:** Semantic Scholar reports 1 citation, marked influential, as a current total; the paper is cross-listed across four categories and is explicitly paired with AeroZoo. An experimental NVIDIA PhysicsNeMo implementation page provides an additional checkable artifact signal.
- **Claimed contribution:** The author claims coordinate-free learned operations, measure-weighted boundary aggregation, and read-only interior queries provide rigid-motion/reflection equivariance and mesh-consistent predictions under stated conditions.
- **Caveat:** The paper states that unseen boundary layouts can sharply hurt accuracy, a deterministic equivariant predictor cannot represent symmetry-breaking flow modes, and 3D interior training can require more than 80 GiB per GPU.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Training & adaptation; Evaluation & benchmarks

### 9. [AeroZoo: A Benchmark of Well-Posed Flow Problems for Foundation Models of Aerodynamics](https://arxiv.org/abs/2611.17152)
- **Abstract:** AeroZoo contributes 3,815 time-mean RANS flow problems across seven geometry families and eight enclosures, with 22 frozen evaluation splits intended to test generalization beyond single-family datasets.
- **Authors:** Peter Sharpe, Carmelo Gonzales, Corey Adams, Mehdi Ataei, Sanjay Choudhry
- **arXiv:** `2611.17152v1` (published 2026-11-12 17:36:09 UTC; categories: `cs.LG`, `cs.CE`, `physics.flu-dyn`)
- **Evidence for ranking:** Semantic Scholar reports 1 citation as a current total; the three-category cross-list and explicit companion link to ISLA make this a coherent benchmark/model pairing rather than an isolated architecture claim.
- **Claimed contribution:** The authors provide a benchmark with complete boundary-condition inputs and geometry-disjoint splits; their results report that boundary-condition tokens reduce GeoTransolver error on the random split.
- **Caveat:** The canonical benchmark uses only 2,816 cases with stable time means, and the authors report error increases of 2.4–9.2 times on some held-out enclosure or boundary-layout splits; the abstract says the data and scoring code will be released.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Evaluation & benchmarks; Training & adaptation

### 10. [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](https://arxiv.org/abs/2611.17294)
- **Abstract:** Metal Sandbox combines per-agent filesystem isolation, native command execution, and cross-Mac scheduling, reporting higher command throughput on four Mac mini M4 nodes and reduced waiting in fixed-trace replays.
- **Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang et al.
- **arXiv:** `2611.17294v1` (published 2026-11-12 18:54:42 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.DC`)
- **Evidence for ranking:** Semantic Scholar reports no current citations at the snapshot; the four-category cross-list, open-source Metal Sandbox and Harbor repositories, and concrete multi-node measurements support its relevance, but not a claim of popularity.
- **Claimed contribution:** The authors present a native Apple Silicon execution environment that schedules agent tool commands across Macs and integrates with Harbor for task verification and rollout collection.
- **Caveat:** The authors state that this is not hostile multi-tenant containment or physical GPU exclusivity; replay estimates hold agent behavior and phase durations fixed, and the hardware evaluation uses four Macs.
- **Announcement type:** new submission, 2026-11-13
- **Themes:** Efficient inference & systems; Agents & reasoning

## Trending Research Themes

- **Agent systems are being measured at the decision bottlenecks around generation.** AgentSSL makes program selection a benchmarked problem; NOPO handles partial verification without trusting apparent positives; LiveGeo tests whether evidence stays valid as the environment changes. These are distinct methods, but all expose a failure point beyond fluent generation.
- **Evidence provenance and verification are recurring concerns.** Cited but Unused tests whether a retrieved citation actually supplied a claim; NOPO asks what to do when verifiers only reject failures; LiveGeo asks agents to revalidate evidence over time. The common methodological shift is to evaluate the reliability of evidence signals, not just task answers.
- **Efficiency is pursued at several layers, not by one shared technique.** CRAM reports lower training and inference cost on structured puzzles; NOPO changes the policy update rule; Metal Sandbox schedules tool execution across machines. These results should not be conflated into a single efficiency breakthrough.
- **Evaluation boundaries are increasingly explicit.** CRAM cautions that puzzle scores may not transfer to harder reasoning; AgentSSL separates pipeline discovery from selection; LiveGeo separates static competence from dynamic reliability. The papers collectively foreground what current benchmarks fail to test, without establishing a general solution.
- **Scientific and physical systems form a smaller applied cluster.** ISLA and AeroZoo pair an invariant PDE surrogate with a benchmark that varies geometry and boundary conditions; the multi-robot allocation paper instead focuses on simulation-tested coordination. These are notable applications, not evidence of a batch-wide shift toward physical AI.
- **Batch composition:** the 348 eligible records had primary categories cs.CV 76, cs.LG 67, cs.AI 61, cs.RO 40, cs.CL 38, stat.ML 5, cs.MA 3, and cs.NE 2. The ten-paper shortlist is not proportional to those category counts.

## Open Problems and Research Directions

- **Author-stated open problem — generalizing energy-based reasoning.** CRAM's strong results concern constraint puzzles that fit a pairwise energy; the authors note harder tasks require latent quantities and do not follow from current scores. **Research direction (synthesis):** test on tasks requiring latent-variable discovery and compare against looped models with matched data, compute, and stopping rules. [CRAM](https://arxiv.org/abs/2611.17309)
- **Author-stated open problem — program selection under scarce labels.** AgentSSL reports that unsupervised selection can badly mis-rank candidate programs and that supervised alternatives match it on ecology tasks. **Research direction (synthesis):** compare active label allocation, stronger feedback, and joint selection of supervised versus semi-supervised pipelines across new domains. [AgentSSL](https://arxiv.org/abs/2611.17323)
- **Author-stated open problem — partial positive evidence.** NOPO avoids rewarding verifier positives, but suppressing negatives alone does not specify where policy probability should move. **Research direction (synthesis):** test uncertainty-filtered or pairwise positive signals while tracking reward hacking and robustness across verifier types. [NOPO](https://arxiv.org/abs/2611.17287)
- **Author-stated open problem — identifying what a RAG model actually used.** Cited but Unused finds current provenance signals too inaccurate to act on, and standard NLI checks can fail. **Research direction (synthesis):** test calibrated interventions across model families and retrieval settings, measuring the false-positive cost before using provenance labels in downstream decisions. [Cited but Unused](https://arxiv.org/abs/2611.17161)
- **Author-stated open problem — adapting to changing worlds.** LiveGeo reports that static success is not enough for dynamic geographic decisions. **Research direction (synthesis):** vary update frequency, stale-evidence rates, and replanning cost, then test whether similar failures occur outside geographic tasks. [LiveGeo](https://arxiv.org/abs/2611.17267)
- **Author-stated limitations — aerodynamic out-of-distribution performance and system cost.** ISLA reports poor performance on some unseen boundary layouts and high GPU memory requirements; AeroZoo shows held-out layout/enclosure degradation. **Research direction (synthesis):** evaluate both on shared preregistered splits that hold out geometry-condition combinations and compare against solver sensitivity and mesh-refinement baselines. [ISLA](https://arxiv.org/abs/2611.17141), [AeroZoo](https://arxiv.org/abs/2611.17152)
- **Author-stated boundary — sandbox security and replay assumptions.** Metal Sandbox does not claim hostile multi-tenant containment or GPU exclusivity, and replay holds agent behavior and phase durations fixed. **Research direction (synthesis):** run live trials with diverse workloads, hardware, contention, and audited isolation boundaries. [Metal Sandbox](https://arxiv.org/abs/2611.17294)

## Takeaway

The most visible pattern in this batch is a move from evaluating model outputs to testing the machinery around them: selecting agent-generated programs, learning from incomplete verifiers, tracing evidence provenance, and revising decisions as the world changes. The attention signals favor a handful of agent/reasoning papers, but most candidates are too new for citation totals to mean much, and the strongest claims remain bounded by specific benchmarks and deployment setups.

## Method and sources

- **Window:** daily announcement batch 2026-11-13 through 2026-11-13. The arXiv recent-submissions page identifies Friday, 13 November as the latest batch; this is the prior batch for the Sunday 2026-11-15 run. The selected records have first-submission timestamps on 2026-11-12 UTC. Snapshot: 2026-11-15 17:12:51 UTC.
- **Corpus:** one broad arXiv API query over `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`, filtered to `submittedDate:[202611120000 TO 202611122359]`. It returned 348 unique records and covered all configured categories. The arXiv cs.AI recent page reports 321 entries in the 13 November announcement batch.
- **Ranking:** arXiv publishes no official trending ranking. Ordering prioritizes visible independent discussion or conference/publication signals, then corroborating current citation totals, cross-list breadth, and checkable artifacts; recency is only a tie-breaker. Semantic Scholar citation totals are current counts, not citations gained during this batch. For the RA-L/ICRA and PAN proceedings papers, cited work predates this arXiv posting, so those counts are not interpreted as a batch-period surge. Because the attention signals are sparse, this is better described as notable recent papers than a reliable popularity ranking.
- **Verification:** all ten selected arXiv abstract pages were checked. The PDFs for the top three were read for introduction, evaluation, and limitations; the robotics paper's conclusion and the ISLA paper's limitations were also checked. No prior-window comparison is included.
- **Primary sources:** [arXiv recent submissions](https://arxiv.org/list/cs.AI/recent); [arXiv API](https://export.arxiv.org/api/query); [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch). Selected arXiv pages: [2611.17309](https://arxiv.org/abs/2611.17309), [2611.17323](https://arxiv.org/abs/2611.17323), [2611.17287](https://arxiv.org/abs/2611.17287), [2611.17213](https://arxiv.org/abs/2611.17213), [2611.16612](https://arxiv.org/abs/2611.16612), [2611.17161](https://arxiv.org/abs/2611.17161), [2611.17267](https://arxiv.org/abs/2611.17267), [2611.17141](https://arxiv.org/abs/2611.17141), [2611.17152](https://arxiv.org/abs/2611.17152), [2611.17294](https://arxiv.org/abs/2611.17294).
- **Corroboration:** [Ken Ashe's CRAM discussion](https://kenashe.ai/blog/2026-11-13-cram-makes-sudoku-reasoning-look-too-easy/); [World Neural CRAM report](https://worldneural.com/research/arxiv-2611-17309); [CRAM repository](https://github.com/Prefrontal-AI/CRAM); [NeurIPS AgentSSL poster](https://neurips.cc/virtual/2026/poster/154115); [AgentSSL OpenReview](https://openreview.net/forum?id=yWxcbCZwgn); [NeurIPS NOPO poster](https://neurips.cc/virtual/2026/poster/152610); [RA-L DOI for the robotics paper](https://doi.org/10.1109/LRA.2025.3632086); [PAN 2025 CEUR proceedings paper](https://ceur-ws.org/Vol-4038/paper_308.pdf); [Cited but Unused coverage at SyncAI News](https://syncai.news/article/cited-but-unused-parametric-provenance-in-retrieval-augmented-generation-979e5b) and [Bharat Hunt](https://bharathunt.org/ai/cited-but-unused-parametric-provenance-in-retrieval-augmented); [LiveGeo coverage at AI Hot](https://aihot.tech/story/arxiv-ker5a3-livegeo-benchmarking-geographic-agents-in-continuously-evolving-worlds/) and [World Neural](https://worldneural.com/research/arxiv-2611-17267); [NVIDIA PhysicsNeMo ISLA documentation](https://docs.nvidia.com/physicsnemo/latest/physicsnemo/api/models/isla.html); [Metal Sandbox](https://github.com/WangHaoZhe/metal-sandbox) and [Harbor](https://github.com/WangHaoZhe/harbor).
