# arXiv AI daily — 28 October 2026: five notable papers on agent reasoning and evaluation

The latest AI-category announcement batch highlights agents acting in worlds, groups, and evidence-rich tasks; one compact time-series model is a distinct systems result. I’ll cover the papers with the strongest checkable signals, then the recurring themes and open tests. arXiv has no official trending chart: this inferred shortlist is drawn from a 200-record recency sample, all five were less than two days old with zero Semantic Scholar citations at snapshot, and Hugging Face upvotes are a narrow platform-specific attention signal rather than a readership measure.

## Top papers (ranked)

### 1. [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666)
- **Abstract:** ThinkWorld represents actions as discrete Chains-of-Dynamics and uses predicted-versus-observed future states to train vision-language-action reasoning from robot demonstrations and videos without action labels.
- **Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, et al.
- **arXiv:** `2610.37666v1` (published 2026-10-27T17:59:52Z; categories: `cs.RO`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** The Hugging Face Papers page displayed 48 upvotes at the snapshot, the highest among these five checked pages. The paper is cross-listed across robotics, AI, and vision and reports simulation and real-robot evaluations.
- **Claimed contribution:** The authors propose a shared motion-token reasoning space and consequence-grounded reinforcement learning, using future-state prediction to extend action supervision to unlabeled human videos; they report transfer to robots and generalization to unseen tasks and environments.
- **Caveat:** The authors report a single training seed, so episode-level confidence intervals do not measure variation across independently trained checkpoints; latency also depends on the stated hardware and input setup.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

### 2. [Can LLMs Uncover Hidden Physical Laws through Free Exploration?](https://arxiv.org/abs/2610.37649)
- **Abstract:** LongChang tests whether LLM agents can investigate simulated worlds with altered physics and discover the hidden laws without being given research questions; only one of twelve evaluated models achieves a non-zero discovery rate.
- **Authors:** Zhen Yang, Wen Wang, Xander Xu, Ying-Cong Chen
- **arXiv:** `2610.37649v1` (published 2026-10-27T17:57:00Z; categories: `cs.CL`, `cs.AI`, `cs.MA`)
- **Evidence for ranking:** The Hugging Face Papers page displayed 7 upvotes at the snapshot. The paper is cross-listed in language, AI, and multiagent categories, and its project page provides a checkable research artifact.
- **Claimed contribution:** The authors introduce LongChang, an automated altered-physics world and exploration-evaluation loop; their full results separate supported observations from correct law discovery, finding 97.6% evidence support but only 19.0% law correctness for the one model with discoveries.
- **Caveat:** The authors explicitly limit the study to simulated worlds with known altered laws and say extending it to unresolved real-world science requires further research; most evaluated models did not discover a law.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 3. [Timestral](https://arxiv.org/abs/2610.37585)
- **Abstract:** The authors introduce four probabilistic time-series foundation models from 5M to 209M parameters and report top results on GIFT-Eval, TIME, and fev-bench.
- **Authors:** Adrien Petralia, Alexandre Gavaudan, Artjom Joosen, Etienne Goffinet, Richard Kurle, et al.
- **arXiv:** `2610.37585v1` (published 2026-10-27T17:25:43Z; categories: `cs.AI`)
- **Evidence for ranking:** The Hugging Face Papers page displayed 6 upvotes at the snapshot. The paper reports results on three forecasting benchmarks, provides model weights and inference code, and gives a concrete efficiency claim: forecasts up to 1,024 steps are produced in one forward pass.
- **Claimed contribution:** The authors combine Decoupled Horizon Forecasting, role-aware treatment of known-future covariates, and synthetic pretraining followed by mixed real-and-synthetic post-training; they report Timestral-209M ranking first among evaluated competitors on all three named suites.
- **Caveat:** The ranking is based on the paper’s evaluation of three public suites and its selected comparator set; it is not evidence of performance across all forecasting workloads or independent deployments.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Training & adaptation; Efficient inference & systems; Data & synthetic data

### 4. [Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](https://arxiv.org/abs/2610.37624)
- **Abstract:** On a controlled 480-task benchmark, rarity- and relevance-based memory filters fail under different distributions of supporting and decoy facts, while attribution tags can induce social-proof errors in the final decision model.
- **Authors:** Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar
- **arXiv:** `2610.37624v1` (published 2026-10-27T17:49:39Z; categories: `cs.AI`, `cs.CL`, `cs.MA`, `cs.SI`)
- **Evidence for ranking:** The Hugging Face Papers page displayed 5 upvotes at the snapshot. The paper is cross-listed across three core AI categories and introduces a 60-template benchmark that separates fact ownership from fact content.
- **Claimed contribution:** The authors introduce CrossProfile and report that relevance filters can admit on-topic decoys, rarity-first selection is not better than random on average, and removing or randomizing agent-attribution tags can improve accuracy in the classic hidden-profile configuration.
- **Caveat:** The findings are bounded by the controlled hidden-profile benchmark, its four tested model families, and its fixed task construction; they do not establish how the same effects scale to arbitrary group discussions.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 5. [TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571)
- **Abstract:** TeamGym evaluates and trains language-model teams on decisions built from legal, finance, medical, and software corpora, measuring how distributing pivotal evidence affects communication and retrieval.
- **Authors:** Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz, Yubin Kim, Taekyun Lee, et al.
- **arXiv:** `2610.37571v1` (published 2026-10-27T17:15:54Z; categories: `cs.AI`)
- **Evidence for ranking:** The Hugging Face Papers page displayed 1 upvote at the snapshot. Its 8-model, 12-corpus study and controlled separation of communication from retrieval provide strong evidence of research relevance, despite a small observed platform vote count.
- **Claimed contribution:** The authors define pivotal information and a configurable team benchmark; they report average success-rate drops of 22.9 percentage points when pivotal information is distributed across participants and a further 19.9 points when participants must retrieve it from source material, while two policy-training experiments improve coordination and final decisions.
- **Caveat:** Results are benchmark-based across the tested models and source corpora; transfer to live teams and other task distributions is not established.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

## Trending Research Themes

- **Agent capability is being tested in interaction, not only single-turn answers.** ThinkWorld studies action reasoning grounded in predicted consequences; LongChang tests self-directed investigation; CrossProfile and TeamGym examine how groups preserve, retrieve, and combine evidence. These are related evaluation targets, not one shared method or proof of a field-wide breakthrough.
- **Evidence handling is a recurring evaluation lens.** CrossProfile manipulates who holds supporting and decoy facts, while TeamGym separates communication failures from retrieval failures. Both indicate that successful final answers can hide distinct failures in the path to a decision.
- **Synthetic data and training objectives remain active levers.** ThinkWorld uses imagined future states to supervise action reasoning from unlabeled video, while Timestral uses synthetic pretraining plus mixed-data post-training for forecasting. The tasks and approaches differ; the common signal is deliberate training-data/objective design.
- **The shortlist is concentrated in agent-related work:** four of five entries concern agents or group decision-making. This describes this selected shortlist, not the full announcement batch; Timestral is a separate forecasting and inference-efficiency signal.

## Open Problems and Research Directions

- **Open problem (author-stated):** LongChang finds that supported observations do not reliably become correct scientific laws, and its authors limit the current study to simulated worlds with known answers. **Research direction:** test staged discovery benchmarks that score hypothesis formation, discriminating experiment design, and law identification separately, then expand toward real domains with expert-verified outcomes (LongChang).
- **Open problem (reported by the authors):** TeamGym measures communication and retrieval gaps, while CrossProfile shows that memory selection and agent attribution can distort decisions. **Research direction:** evaluate provenance-preserving memory and retrieval interventions across varying team sizes, communication budgets, and held-out corpora, with errors decomposed into retrieval, communication, and decision stages (TeamGym; CrossProfile).
- **Open problem (author-stated):** ThinkWorld’s reported training used a single seed. **Research direction:** repeat training across independent seeds and additional embodiments, then report checkpoint-level uncertainty alongside physical-trial variability (ThinkWorld).
- **Research direction (suggested by the paper):** Timestral identifies larger models and use of context representations for classification or anomaly detection as follow-up possibilities. Evaluate those tasks separately from forecasting and test whether the stated accuracy/size trade-off persists outside the three reported suites (Timestral).

## Takeaway

The clearest shared pattern is agent evaluation under information constraints: papers test how models reason about consequences, discover rules, and preserve evidence across a group. Hugging Face upvotes provide some visible attention evidence, led by ThinkWorld, but the papers are extremely recent and the small sampled set cannot establish a comprehensive arXiv popularity ranking.

## Method and sources

- **Window:** Daily arXiv announcement batch dated 2026-10-28; exact report window 2026-10-28 through 2026-10-28. This is the latest batch, not a fallback to a prior batch. The selected version-1 records carry first-submission timestamps on 2026-10-27. arXiv’s `cs.AI` recent page lists the batch as Wed, 28 Oct 2026.
- **Snapshot:** 2026-10-29T01:16:36.984Z (UTC).
- **Scope and candidate pool:** Core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`, including cross-lists. One broad arXiv API query sorted by submitted date returned 200 recent candidates and included records from all eight core categories; it is a recency sample, not a complete ordering of every paper in the batch. Query: `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`.
- **Inference:** arXiv has no official trending chart. The five-paper ordering follows displayed Hugging Face Papers upvotes at snapshot (48, 7, 6, 5, 1), with category breadth and reported evaluation scope used as corroboration. Semantic Scholar Graph lists 0 citationCount and 0 influentialCitationCount for all five; these are current totals, not citations gained during the window. Vote counts are platform-specific, and the list should be read as an inferred shortlist, not a comprehensive popularity ranking.
- **Primary sources:** [arXiv recent AI list](https://arxiv.org/list/cs.AI/recent); [arXiv API](https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:stat.ML+OR+cat:cs.CL+OR+cat:cs.CV+OR+cat:cs.RO+OR+cat:cs.NE+OR+cat:cs.MA&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); each linked arXiv abstract page; [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.37666?fields=title%2CcitationCount%2CinfluentialCitationCount).
- **Semantic Scholar records:** [ThinkWorld](https://www.semanticscholar.org/paper/63159b00120d1888f81fafe04f18224b85843d95), [LongChang](https://www.semanticscholar.org/paper/23c097ac0301de98b5c1de1378c2ecdbc4709827), [Timestral](https://www.semanticscholar.org/paper/5453b58be7f4c9f26cb85fcfe286d329d080a8c3), [CrossProfile](https://www.semanticscholar.org/paper/efc89ea82ffaadd3a0cedbf5e49ece5c1716a5f7), [TeamGym](https://www.semanticscholar.org/paper/eb58bae977c43b1476d8d91399af1b892af4af07).
- **Attention sources:** [ThinkWorld](https://huggingface.co/papers/2610.37666), [LongChang](https://huggingface.co/papers/2610.37649), [Timestral](https://huggingface.co/papers/2610.37585), [CrossProfile](https://huggingface.co/papers/2610.37624), [TeamGym](https://huggingface.co/papers/2610.37571) Hugging Face Papers pages, with displayed upvotes recorded at the stated snapshot. Authors’ additional resources: [ThinkWorld project page](https://thinkworld-project.github.io/), [LongChang project page](https://zhenyangcs.github.io/LongChang-website/), and [Timestral weights and code](https://mistral.ai/news/timestral).
- **Full-text review:** arXiv HTML introductions/results/limitations were checked for the top three papers. The configured `web_extract` backend was unavailable, so arXiv abstracts were verified through live browser pages and the arXiv Atom feed; the full-text review used arXiv HTML.
