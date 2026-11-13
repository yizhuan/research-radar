# Daily AI papers — arXiv announcement batch 2026-11-11

Seven papers are ranked below from the newest available batch across arXiv’s core AI categories. The strongest recurring pattern is agents being made more reliable or cheaper by checking experience, compiling repeated behavior, or making decisions under explicit constraints; we’ll also look at scientific discovery and multimodal abstention. This is an inferred ranking: arXiv has no official trending chart, and these very recent papers have little citation evidence.

## Top papers (ranked)

### 1. [ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492)
- **Abstract:** ReTrace converts an SOP and a few logged agent runs into reusable executable workflows that choose steps without an LLM planner, reporting near-agent task completion with lower cost and much lower latency in tested settings.
- **Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, et al.
- **arXiv:** `2611.14492v1` (published 2026-11-10 18:49:47 UTC; categories: `cs.AI`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Three independent technical explainers discuss the work ([AI Agents Info](https://www.aiagentsinfo.com/research/retrace-planner-free-agent-workflows), [Ken Ashe](https://kenashe.ai/blog/2026-11-11-retrace-turns-repeatable-agents-into-code-paths/), [LearnAgentic](https://learnagentic.substack.com/p/your-agent-took-170-seconds-its-compiled)); it is also cross-listed in three core AI categories.
- **Claimed contribution:** The authors extract action conditions from agent reasoning and tool traces, merge them into an evidence-linked rule document, then compile platform-specific workflows; their tests report 93.8% completion on 79 production procedures at 24% lower task cost, and 1.3 s versus 170 s per task on τ²-bench.
- **Caveat:** The authors say generated-workflow checks do not establish that recovered conditions are correct; evaluation covers new inputs to the same procedures, not transfer to new procedures, and platform completion flags can misreport failures.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Agents & reasoning; Efficient inference & systems

### 2. [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511)
- **Abstract:** Pyrite introduces a 1,500-pair protein–ligand pose-ranking benchmark and structured molecular features for LLM agents, reporting up to 74% accuracy for an LLM-guided feature-engineering pipeline.
- **Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
- **arXiv:** `2611.14511v1` (published 2026-11-10 18:56:32 UTC; categories: `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** Independent coverage appeared at [Bioscience.com](https://www.bioscience.com.pk/en/subject/biology/pyrite-building-and-benchmarking-protein-ligand-pose-ranking-agents); the arXiv record identifies a NeurIPS 2026 Agentic AI for Biological Discovery workshop paper, and the authors link [code](https://github.com/genesistherapeutics/pyrite) and a [dataset](https://huggingface.co/datasets/genesisml/pyrite).
- **Claimed contribution:** The authors introduce PyriteRep and compare direct LLM pose reasoning with LLM-generated features for logistic regression; the latter reaches 74% on their benchmark, while expert chemists perform near chance on the evaluated pairs.
- **Caveat:** The benchmark poses come from the authors’ proprietary cofolding model; they flag possible pre-/post-AF3 distribution shift and leave transfer to other pose generators and downstream drug-discovery pipelines for future work.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 3. [Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](https://arxiv.org/abs/2611.14514)
- **Abstract:** Contrastive Discovery makes an agent evaluate a scientific question against explicit competing explanations rather than a single claim and its negation, reporting more resolved questions under matched evidence and experiment budgets.
- **Authors:** Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
- **arXiv:** `2611.14514v1` (published 2026-11-10 18:58:43 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** The arXiv record says accepted at NeurIPS 2026; the authors also provide a [project page](https://codiscovery.ai/contrastive-discovery/) explaining the method and evaluation. Three core-category cross-lists add relevance across AI, language, and ML.
- **Claimed contribution:** Across six data-driven domains, authors report 67% more resolved questions than pointwise surprisal under the same experiment budget; a blinded study of 38 experts agreed with the selected explanation on 78% of resolved questions.
- **Caveat:** The study uses observational tabular datasets and one GPT-4o-based agent; the authors note that conclusions are statistical rather than causal and that results remain to be tested in laboratory experiments and longer-horizon interventions.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 4. [When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](https://arxiv.org/abs/2611.14326)
- **Abstract:** FGSE treats a proposed agent-memory update as a hypothesis, probes transfer, falsification, and regression risks in temporary state, and commits, revises, or rejects it using verifier-grounded evidence.
- **Authors:** Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, et al.
- **arXiv:** `2611.14326v1` (published 2026-11-10 16:52:25 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The paper is listed as a NeurIPS 2026 poster ([conference page](https://neurips.cc/virtual/2026/loc/sydney/poster/154558)); the study spans web, app, tool-use, and long-term-memory benchmarks and reports explicit falsification and regression measures.
- **Claimed contribution:** The authors report 39.8 WebArena success, 78.8 AppWorld average completion, and reductions in falsification failures, regression damage, and harmful committed updates using their commit–refine–reject process.
- **Caveat:** The reported evidence is from verifier-rich benchmarks; the authors leave extension to multimodal or collaborative agents and settings where verifiers must be learned or approximated to future work.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Agents & reasoning; Safety & alignment; Retrieval & knowledge

### 5. [Multimodal Abstention That Preserves Acquired Correct Answers](https://arxiv.org/abs/2611.14311)
- **Abstract:** ReFrain adds calibrated abstention to a task-adapted vision-language model while constraining newly lost correct answers, reporting improved refusal of unanswerable image questions with fewer regressions than compared methods.
- **Authors:** Jinyuan Zhang
- **arXiv:** `2611.14311v1` (published 2026-11-10 16:41:49 UTC; categories: `cs.AI`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The author provides [code and reproduction materials](https://github.com/ModeLiberaL/ReFrain), and the paper is cross-listed across AI, vision, and ML. A [paper page](https://www.catalyzex.com/paper/multimodal-abstention-that-preserves-acquired) also summarizes the method and links its materials.
- **Claimed contribution:** The author combines a first-token-logit probe, held-out image-cluster threshold calibration, and a deterministic veto; on Qwen2.5-VL-3B, the paper reports higher correct abstention at a specified calibration budget while retaining more SFT-gained answers than the comparison method.
- **Caveat:** The author reports a single training seed and a 677-record training set; independent confirmation covers AI2D science diagrams, and possible exposure of public AI2D data during model pretraining cannot be excluded.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Safety & alignment; Multimodal & vision-language; Evaluation & benchmarks

### 6. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)
- **Abstract:** WikiTrace links each agent-memory lesson to its source trajectory so an agent can inspect missing details, conflicts, or failed-task evidence before acting; the authors report consistent gains over memory baselines on five agentic benchmarks.
- **Authors:** Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- **arXiv:** `2611.14320v1` (published 2026-11-10 16:46:59 UTC; categories: `cs.AI`, `cs.MA`)
- **Evidence for ranking:** The work received an independent [Daily Paper Cast episode](https://poddtoppen.se/podcast/1777620236/daily-paper-cast/dont-just-trust-your-memory-evidence-linked-memory-reduces-memory-induced-degradation-in-llm-agents) and a [third-party paper analysis](https://paperium.net/article/contact-us/27040/dont-just-trust-your-memory-evidence-linked-memory-reduces-memory-induceddegradation-in-llm-agents); it is also cross-listed in AI and multiagent systems.
- **Claimed contribution:** The authors store concise insights with summaries and links to raw trajectories, then use tools to inspect the linked evidence when a lesson lacks detail, conflicts with another, or derives from a failed task.
- **Caveat:** The authors say trajectory diagnoses may be wrong and links do not themselves verify insights; placing every insight in the initial prompt also makes prompt size grow, leaving retrieval for oversized memories open.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Safety & alignment

### 7. [Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2611.14015)
- **Abstract:** MCPO redistributes sequence-level reinforcement-learning credit toward tokens with a small top-two probability margin, reporting gains over GRPO on two small language models while generating longer answers.
- **Authors:** Chi Liu, Xin Chen, Yuchuan Weng, Srinivasan Manoharan
- **arXiv:** `2611.14015v1` (published 2026-11-10 12:51:43 UTC; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** [Machine Brief](https://www.machinebrief.com/news/margin-guided-token-credit-for-reinforcement-learning-with-v-next) published independent coverage; the paper tests two model families, eight data-seed runs, and six math benchmarks, and is cross-listed in AI and ML.
- **Claimed contribution:** The authors use the trainer’s existing forward pass to read top-two token margins and redistribute advantages; they report a 6.55-point mean macro avg@32 gain over GRPO for MiniCPM5-2B-Base and a positive three-seed Qwen3-4B-Base replication.
- **Caveat:** The authors did not compare against entropy-based credit or a length-matched baseline, so they cannot separate the margin-credit effect from the observed increase in answer length; the comparison uses one short LoRA training recipe.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Training & adaptation; Efficient inference & systems

## Trending Research Themes

- **Agents become procedures, not just planners.** ReTrace compiles repeated SOP execution into code-selected workflows; FGSE and WikiTrace instead control whether past experience enters or guides future state. These are related ways to make agent behavior more auditable, but their mechanisms and evaluations differ.
- **Memory is being treated as evidence that needs review.** FGSE temporarily tests candidate updates before commitment, while WikiTrace keeps lessons linked to their originating trajectories. Both address memory-induced regressions, but one gates writes and the other supports checking at use time.
- **Scientific agents benefit from structured alternatives and representations.** Contrastive Discovery represents explicit competing explanations, while PyriteRep structures molecular interactions and scores for pose-ranking agents. These are two distinct approaches to supplying an agent with a better-defined evidence space, not evidence of a general scientific-agent breakthrough.
- **Constrained decisions matter in multimodal reliability.** ReFrain frames abstention as a tradeoff between correct refusal and lost correct answers; its evidence is task- and checkpoint-specific.
- **Training signals are being localized.** MCPO shifts RLVR credit toward close token decisions; Pyrite also reports GRPO fine-tuning for its open-weight agents. Both use RL, but neither result establishes a universal training recipe.
- **Category mix:** The seven selected papers span cs.AI, cs.LG, cs.CL, cs.CV, cs.MA, and q-bio.QM, with a clear concentration on LLM agents and ML methods; robotics and neural/evolutionary computing are not represented in this selected set. This is a curated shortlist, not a census of category output.

## Open Problems and Research Directions

- **Author-stated — workflow truth and transfer:** ReTrace’s checks do not prove recovered action conditions are correct, and the evaluation does not transfer to new procedures. A useful follow-up is a human-audited study on unseen SOPs with branch-coverage-selected traces and outcome checks beyond platform completion flags. [ReTrace](https://arxiv.org/abs/2611.14492)
- **Author-stated — memory diagnosis:** FGSE identifies verifier-learning/approximation settings as future work; WikiTrace notes that a source link cannot validate a wrong insight. Test both approaches where verifiers are imperfect, and measure whether evidence inspection reduces harmful updates under adversarial or ambiguous traces. [FGSE](https://arxiv.org/abs/2611.14326), [WikiTrace](https://arxiv.org/abs/2611.14320)
- **Author-stated — pose distribution shift:** Pyrite flags possible pre-/post-AF3 shift and calls for evaluation on other pose generators and downstream ranking pipelines. Replicate with public pose-generation sources and test whether pairwise gains improve actual selection among candidate binding poses. [Pyrite](https://arxiv.org/abs/2611.14511)
- **Author-stated — abstention generality:** ReFrain’s independent confirmation is limited to AI2D and its training setup has one seed. Repeat across image domains, models, and retraining seeds while reporting cluster-level uncertainty and calibration-budget trade-offs. [ReFrain](https://arxiv.org/abs/2611.14311)
- **Author-stated — credit attribution:** MCPO lacks entropy, random-credit, and length-matched comparisons. Compare these under matched generated-token budgets and longer training to test whether margin-guided credit itself explains the gains. [MCPO](https://arxiv.org/abs/2611.14015)
- **Author-stated — scientific discovery scope:** Contrastive Discovery uses observational tabular data and one agent backbone; the authors call for tests in laboratory experiments and longer interventions. Evaluate whether explicit alternatives remain useful when evidence is causal, expensive, or produced by non-LLM agents, and audit whether contrast sets omit plausible explanations. [Contrastive Discovery](https://arxiv.org/abs/2611.14514)

## Takeaway

The clearest practical thread is engineering reliability around agents: compile repeated tasks, keep memory falsifiable, and constrain abstention or training updates with explicit checks. The results are promising but largely benchmark-bound; broader transfer, stronger controls, and independent replication remain uncertain.

## Method and sources

- **Window:** daily batch 2026-11-11 (2026-11-11 through 2026-11-11 UTC); it is a prior announcement batch relative to the 2026-11-13 snapshot because the recent pages still showed 2026-11-11 as their newest batch.
- **Snapshot:** 2026-11-13 01:10:10 UTC.
- **Scope/query:** arXiv recent listings for `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; papers outside the core list were retained only when cross-listed or when the AI contribution was explicit. The broad arXiv API request timed out, so category recent pages were checked directly. Every selected paper’s arXiv abstract page was opened and its version, submission timestamp, authors, and categories verified.
- **Ranking:** inferred, not an arXiv ranking. Since all seven selected records had zero Semantic Scholar citations and zero influential citations at snapshot, citation momentum offered no useful separation. Ordering therefore favors checkable independent technical discussion, venue/project/code signals, and the specificity of reported evaluation; it is a notable-recent-papers shortlist rather than a claim of measured popularity. Citation counts are current totals, not gains during this date window.
- **arXiv and corroborating sources:** [ReTrace arXiv](https://arxiv.org/abs/2611.14492), [Pyrite arXiv](https://arxiv.org/abs/2611.14511), [Contrastive Discovery arXiv](https://arxiv.org/abs/2611.14514), [FGSE arXiv](https://arxiv.org/abs/2611.14326), [ReFrain arXiv](https://arxiv.org/abs/2611.14311), [WikiTrace arXiv](https://arxiv.org/abs/2611.14320), [MCPO arXiv](https://arxiv.org/abs/2611.14015); corroboration links appear in the relevant evidence fields. Semantic Scholar Graph API was checked by arXiv ID for the citation and field metadata.
