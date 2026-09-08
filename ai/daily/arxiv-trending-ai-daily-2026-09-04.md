# arXiv Trending AI — daily report

## Headline

The strongest cluster in the latest arXiv AI batch is the operationalization of agents: persistent memory and skills, hybrid GUI/CLI execution, and security-correct forgetting. A second cluster targets evaluation realism—especially whether rewards, explanations, and health reasoning remain reliable under paraphrase, longitudinal data, and human use. arXiv publishes no official trending chart; this is an inferred list of notable papers, not a most-read ranking.

## Scope and snapshot

- **Window:** latest arXiv announcement batch available at the snapshot, 2026-09-04 00:00–23:59 UTC; no 2026-09-08 batch was available at the 2026-09-08T00:10:09Z snapshot.
- **Corpus:** recent submissions cross-listed in cs.AI, cs.LG, stat.ML, cs.CL, cs.CV, cs.RO, cs.NE, or cs.MA.
- **Ranking basis:** corroborated Semantic Scholar metadata plus cross-list breadth, concrete evaluation, benchmark/code availability, and topical relevance. Semantic Scholar showed zero citations and zero influential citations for all selected papers, so citation momentum is unavailable and the ordering is necessarily tentative.

## Top papers (ranked)

### 1. [Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents](https://arxiv.org/abs/2609.04875)
- **Abstract:** The paper formalizes forgetting in stateful agents as behavior equivalent to never having observed revoked information, then proposes provenance-guided selective replay across prompts, compressed memory, and KV cache.
- **Authors:** Chao Yao; Yangbo Wei; Zhen Huang; Junhong Qian; Chenle Chen; et al.
- **arXiv:** `2609.04875v1` (published 2026-09-04 08:31 UTC; categories: `cs.CR`, `cs.AI`)
- **Evidence for ranking:** Semantic Scholar: 0 citations, 0 influential citations, 23 references. Ranked first for a formal guarantee, cross-layer systems treatment, and concrete behavioral audit; popularity signals are sparse.
- **Claimed contribution:** The authors prove a lower bound on recomputation and report that selective replay matches a full reset while using up to 9x fewer recomputed tokens.
- **Caveat:** The abstract describes deterministic-transition assumptions and evaluation on three agent suites; generality to nondeterministic, distributed, or externally stateful agents is not established here.
- **Announcement type:** new submission, announcement batch 2026-09-04
- **Themes:** Safety & alignment; Agents & reasoning; Efficient inference & systems

### 2. [CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents](https://arxiv.org/abs/2609.05374)
- **Abstract:** CUA-Universe provides reproducible desktop environments, controllable hybrid tasks, and rollout steering for training agents to coordinate GUI and command-line operations over shared application state.
- **Authors:** Haoting Shi; Wenhao Wang; Weicheng Fang; Yaozhong Liang; Tian Jin; et al.
- **arXiv:** `2609.05374v1` (published 2026-09-04 17:26 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Semantic Scholar: 0 citations, 0 influential citations, 41 references. Ranked highly for a 16-application environment/data pipeline, released benchmark direction, and reported gains on CUA-Verse, OSWorld, and OSWorld-MCP; no independent attention signal was found.
- **Claimed contribution:** The authors report a 9B model improvement of 39.3 score points with 37% fewer steps and 60% fewer tokens on CUA-Verse, alongside gains on OSWorld variants.
- **Caveat:** The abstract does not establish performance outside the supported desktop applications or against broader real-world workflows.
- **Announcement type:** new submission, announcement batch 2026-09-04
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Efficient inference & systems

### 3. [Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models](https://arxiv.org/abs/2609.05401)
- **Abstract:** ROBORMBENCH tests whether vision-language reward models assign consistent rewards to identical robot trajectories when goal descriptions are paraphrased.
- **Authors:** Wonje Jeung; Sangyeon Yoon; Hyesoo Hong; Yoonjun Cho; Dongjae Jeon; et al.
- **arXiv:** `2609.05401v1` (published 2026-09-04 17:47 UTC; categories: `cs.RO`, `cs.CL`)
- **Evidence for ranking:** Semantic Scholar: 0 citations, 0 influential citations, 56 references. Ranked for a focused reliability failure, 2,390 real-robot trajectories, and 21,673 verified paraphrases; citations are too recent to help.
- **Claimed contribution:** The authors find widespread paraphrase-induced reward instability and report that trajectory-grounded reward models are substantially more stable.
- **Caveat:** The abstract does not provide the full model-by-model effect sizes or evidence that stability transfers to new robots, tasks, or languages.
- **Announcement type:** new submission, announcement batch 2026-09-04
- **Themes:** Robotics & control; Evaluation & benchmarks; Safety & alignment

### 4. [WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data](https://arxiv.org/abs/2609.05405)
- **Abstract:** WearableQA contains 4,084 questions over longitudinal wearable, biomarker, and demographic data from 200 users, separating data reasoning from health reasoning and single-signal from cross-signal reasoning.
- **Authors:** Ji Soo Lee; Xilun Chen; Pierce Chuang; Ashish Shenoy; Jason Wei; et al.
- **arXiv:** `2609.05405v1` (published 2026-09-04 17:52 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Semantic Scholar: 0 citations, 0 influential citations, 21 references. Ranked for realistic longitudinal data, a diagnostic 16-type benchmark, and evaluation of 14 models; no established attention statistic is available.
- **Claimed contribution:** The authors report model accuracy from 19.6% to 72.9% against a 10% chance baseline, with most models below 60%.
- **Caveat:** The benchmark uses 200 users and multiple-choice questions; clinical validity, population coverage, and performance on open-ended decisions remain unresolved.
- **Announcement type:** new submission, announcement batch 2026-09-04
- **Themes:** Evaluation & benchmarks; Retrieval & knowledge; Safety & alignment

### 5. [From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents](https://arxiv.org/abs/2609.04869)
- **Abstract:** This work turns computer-use trajectories and evaluator feedback into a versioned skill library that evolves across iterations without changing model parameters.
- **Authors:** Longtao Hu; Xiao Liang; Linchao Zhu
- **arXiv:** `2609.04869v1` (published 2026-09-04 08:29 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Semantic Scholar: 0 citations, 0 influential citations, 23 references. Ranked for a controlled empty-library comparison across four OSWorld domains and released code; citation signals are unavailable.
- **Claimed contribution:** The authors report post-warm-up gains of 5.7–18.6 percentage points and analyze cross-task retrieval and revision churn.
- **Caveat:** Benefits are domain-dependent, and the paper explicitly reports that repeated revision does not guarantee recovery of the originating task.
- **Announcement type:** new submission, announcement batch 2026-09-04
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 6. [From Interpretability Methods to Interpretable Models](https://arxiv.org/abs/2609.05399)
- **Abstract:** This review argues that vision XAI should shift from producing and comparing explanation methods toward measuring what models represent and whether independent human evaluators can actually understand them.
- **Authors:** Julien Colin; Nuria Oliver; Thomas Serre
- **arXiv:** `2609.05399v1` (published 2026-09-04 17:46 UTC; categories: `cs.CV`, `cs.HC`)
- **Evidence for ranking:** Semantic Scholar: 0 citations, 0 influential citations, 174 references; classified as a review. Ranked for synthesis value and a clearly articulated measurement agenda rather than attention, which is not yet measurable.
- **Claimed contribution:** The authors organize a model-centric interpretability agenda around comparative model characterization and human-centered understandability.
- **Caveat:** This is a perspective/review article; it motivates an agenda but does not itself validate a new interpretability metric or intervention.
- **Announcement type:** new submission, announcement batch 2026-09-04
- **Themes:** Interpretability; Evaluation & benchmarks; Safety & alignment

## Trending research themes

- **Agent state is becoming a first-class object.** Execution-state unlearning and evolving skill libraries treat memory, provenance, replay, and procedural knowledge as system components rather than prompt text alone (Yao et al.; Hu et al.).
- **Agent evaluation is moving toward realistic interaction.** CUA-Universe combines GUI and CLI state; ROBORMBENCH uses real-robot trajectories; WearableQA uses noisy, longitudinal human data. These papers collectively challenge single-score, static benchmark assumptions.
- **Reliability failures are semantic and behavioral, not only capability failures.** ROBORMBENCH exposes paraphrase fragility, while the interpretability review distinguishes producing explanations from being understandable to independent evaluators.
- **Efficiency is tied to correctness.** Selective replay reduces recomputation while preserving counterfactual behavior, and CUA-Universe reports fewer steps and tokens—not merely higher task success.

## Research opportunities

### Potential research areas

- **Provenance-aware agent runtimes:** combine execution-state unlearning with versioned skill libraries so every memory, tool plan, and learned procedure has revocable lineage (Yao et al.; Hu et al.).
- **Cross-modal, cross-interface agent benchmarks:** extend CUA-Universe-style tasks with paraphrase perturbations and explicit permission/security tests (Shi et al.; Jeung et al.).
- **Human-centered reliability evaluation:** connect behavioral correctness, reward invariance, and independent human understandability in one evaluation protocol (Jeung et al.; Colin et al.).

### Unsolved problems

- **Exact forgetting under nondeterminism and external side effects** remains open beyond the deterministic transition model and evaluated suites (Yao et al.).
- **Skill-library stability and negative transfer** remain unresolved: gains vary by domain, and revision churn can fail to recover useful procedures (Hu et al.).
- **Real-world health reasoning is far from solved:** most WearableQA models remain below 60%, and the benchmark's multiple-choice setup does not establish clinical decision safety (Lee et al.).
- **Reward-model invariance under language variation** is not reliably obtained through scale or explicit reasoning alone (Jeung et al.).

### Potential research directions

- Build a benchmark that measures forgetting leakage after model upgrades, skill retrieval, cache reuse, and tool-side effects, with provenance-based certificates (Yao et al.; Hu et al.).
- Evaluate hybrid GUI+CLI agents under adversarial paraphrases, changing application versions, permission boundaries, and recovery from partial failure (Shi et al.; Jeung et al.).
- Replace aggregate agent scores with behavioral suites that separately test task success, semantic invariance, calibration, human comprehension, and safe recovery (Jeung et al.; Colin et al.).

## Takeaway

The most credible signal in this batch is not a single new model architecture but a shift toward agents that must retain, revise, forget, and justify state while operating in messy environments. The papers provide promising benchmarks and systems, but their attention evidence is immature: every selected paper currently has zero Semantic Scholar citations and no official arXiv popularity statistic. Treat the reported improvements as preliminary until independently reproduced across applications, users, languages, and physical settings.

## Method and sources

The snapshot was taken at **2026-09-08T00:10:09Z**. The latest available arXiv announcement batch was **2026-09-04**; arXiv's API returned 200 core-corpus entries for that batch query, and the report selected six after deduplication by versionless ID. Abstract and metadata sources are the canonical arXiv pages linked above. Corroborating metadata came from the Semantic Scholar Graph API batch lookup for each selected arXiv ID. No independent web-attention signal was counted where it could not be verified. The ordering is therefore an evidence-weighted, qualitative inference—not an official trending, readership, download, or citation-gain ranking.
