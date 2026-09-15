# arXiv Trending AI — 2026-09-15

## Headline

Today's latest arXiv AI announcement batch is dominated by agentic systems that search, execute, critique, and retain state over long horizons. The strongest cross-cutting signal is not a single model architecture, but infrastructure for making autonomous work more adaptive, auditable, and safe.

arXiv publishes no official trending chart. This is an inferred shortlist of notable papers from the 15 September 2026 announcement batch, using cross-list breadth, concrete evaluation claims, conference/journal signals, and apparent research relevance. Very recent papers generally have sparse citation evidence.

## Top papers (ranked)

### 1. [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](https://arxiv.org/abs/2609.15983)
- **Abstract:** Stellar Colosseum is a model-agnostic multi-agent harness that allocates inference across research strategies, decomposes proof plans, routes verifier feedback, and aggregates candidate arguments for long-horizon mathematics and theoretical computer science.
- **Authors:** Honghao Lin, David P. Woodruff, Yuan Deng, Jieming Mao, Song Zuo, Vahab Mirrokni
- **arXiv:** `2609.15983v1` (published 2026-09-14 17:58 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Cross-listed across three core AI categories; reports 71.0% on TCS-Bench and 218/222 Codeforces problems with the stated Gemini configurations; no independently verified citation count was available at this snapshot.
- **Claimed contribution:** The authors propose a staged workflow with strategy exploration, readiness gating, section-level proof subproblems, targeted falsification, and tree aggregation, and report new research results and benchmark performance.
- **Caveat:** The evidence is tied to specific Gemini versions and benchmark settings; open-ended research claims are preliminary preprint results.
- **Announcement type:** new submission, announcement-batch 2026-09-15
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Training & adaptation

### 2. [OpenAI4S: Code as Action, Science as Sessions](https://arxiv.org/abs/2609.15096)
- **Abstract:** OpenAI4S is an open-source scientific research agent combining persistent Python/R execution, session management, provenance ledgers, versioned artifacts, checkpoints, and sandboxing for reproducible computational research.
- **Authors:** Gongbo Zhang, Hao Li, Yu Wang, Mujie Lin, Liuzhenghao Lv, Yicheng Mao, Yimi Wang, Jun Zhu, Minhan Tang, Zhengxiang Jiang, Yusong Wang, Jiayu Yao, Kunpeng Ning, Dawei Pang, Yonghong Tian, OpenAI4S Community, Yuyang Liu, Li Yuan
- **arXiv:** `2609.15096v1` (published 2026-09-14 06:16 UTC; categories: `cs.AI`, `cs.CL`, `cs.SE`)
- **Evidence for ranking:** Cross-listed across AI, language, and software engineering; evaluates 36 scientific scenarios and reports 7.83 versus 5.7–6.4 for the comparison coding harness; MIT-licensed system and artifacts are stated as available; citation evidence is sparse.
- **Claimed contribution:** The paper introduces persistent execution and session-level provenance as first-class design principles for long-running AI-assisted science workflows.
- **Caveat:** The authors explicitly report that environment specification and full rerunnability remain weak for every evaluated system, including theirs.
- **Announcement type:** new submission, announcement-batch 2026-09-15
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 3. [HazardAuditor: From Executable Threats to Safer Computer-Use Agents](https://arxiv.org/abs/2609.15134)
- **Abstract:** HazardAuditor runs heterogeneous computer-use agents in controlled environments, normalizes their runtime events, and trains execution-grounded safety guards with a sequence-level optimization objective.
- **Authors:** Yunhao Feng, Ruixiao Lin, Ming Wen, Yanming Guo, Xingjun Ma, Yutao Wu, Xinhao Deng, Shouling Ji
- **arXiv:** `2609.15134v1` (published 2026-09-14 07:09 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Directly addresses a high-impact failure mode for deployed agents; evaluates multiple heterogeneous systems and reports up to 16.5 percentage points over the strongest prior guard; code, models, and artifacts are stated as forthcoming; citation evidence is sparse.
- **Claimed contribution:** The authors introduce a canonical event representation and Guard Policy Optimization, which makes safety outcomes rather than rationale length the effective optimization unit.
- **Caveat:** The reported gain is benchmark- and system-dependent, and the release of artifacts is stated in future tense.
- **Announcement type:** new submission, announcement-batch 2026-09-15
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 4. [AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery](https://arxiv.org/abs/2609.15820)
- **Abstract:** AlgoEvo turns automated algorithm discovery into an interactive, knowledge-accumulating process in which an agent inspects, diagnoses, and edits code using runtime feedback and reusable cross-task skills.
- **Authors:** Junhao Qiu, Qinglong Hu, Xialiang Tong, Mingxuan Yuan, Liyong Lin, Qingfu Zhang
- **arXiv:** `2609.15820v1` (published 2026-09-14 16:24 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Reports results across six representative benchmark tasks, including fewer evaluations and lower token consumption than specialized methods; the design explicitly tests intra-task accumulation and cross-task transfer; no verified citation count was available.
- **Claimed contribution:** The authors present a unified agentic framework with a design-skill hub and hierarchical experience memory for adaptive algorithm search.
- **Caveat:** The abstract does not provide task-by-task effect sizes, and all performance claims remain author-reported preprint results.
- **Announcement type:** new submission, announcement-batch 2026-09-15
- **Themes:** Agents & reasoning; Training & adaptation; Efficient inference & systems

### 5. [NoteVQA: Benchmarking VLMs on Real-Life Questions from Human Communities](https://arxiv.org/abs/2609.15695)
- **Abstract:** NoteVQA introduces 252 real-life visual questions from a Chinese image-sharing community, seven user intents, expert-grounded references, and metrics for both concise answers and visually interleaved explanations.
- **Authors:** Haonan Jiang, Guojian Zhan, Jiancong Xie, Shijun Wan, Dongiia Zhao, Cheng Chen, Yahui Liu, Yao Hu, Chuan Mu
- **arXiv:** `2609.15695v1` (published 2026-09-14 15:01 UTC; categories: `cs.AI`)
- **Evidence for ranking:** A 30-page benchmark paper evaluates 10 frontier VLMs and exposes a concrete deployment-relevant gap: the best short-answer accuracy is 52.8%; benchmark and rubric contributions provide stronger evidence than recency alone; citation evidence is sparse.
- **Claimed contribution:** The authors contribute NoteVQA, the AgenticInterleave evaluation setup, and the 12-dimensional IVR-12 rubric for content, presentation, and image quality.
- **Caveat:** The dataset contains only 252 items and is drawn from one platform and cultural context; agentic search improves the reported accuracy by only 2.0% for the tested Qwen model.
- **Announcement type:** new submission, announcement-batch 2026-09-15
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Retrieval & knowledge

### 6. [LongAgent: History-Guided Agentic Search for Longitudinal Outcome Prediction](https://arxiv.org/abs/2609.15859)
- **Abstract:** LongAgent searches over variable sets, temporal windows, and longitudinal aggregation functions for medical prediction, using history memory and numerical evidence to guide subsequent exploration.
- **Authors:** Siyao Wang, Florian Guitton, Shuojie Fu, Guanyu Tao, Kai Sun, Wenjia Bai
- **arXiv:** `2609.15859v1` (published 2026-09-14 16:51 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Accepted to the MICCAI 2026 Agentic AI for Medicine Workshop; reports a statistically significant but small synthetic-data improvement over the strongest non-agent baseline and comparable real-clinical performance; citation evidence is sparse.
- **Claimed contribution:** The authors apply history-guided agentic search to heterogeneous longitudinal medical data and report RMSE results on synthetic and real clinical datasets.
- **Caveat:** On the real clinical dataset the method is only comparable to the best baseline, so general clinical superiority is not established.
- **Announcement type:** new submission, announcement-batch 2026-09-15
- **Themes:** Agents & reasoning; Retrieval & knowledge; Evaluation & benchmarks

## Trending Research Themes

- **Long-horizon agent infrastructure:** Stellar Colosseum, AlgoEvo, OpenAI4S, and LongAgent all treat memory, decomposition, feedback, or persistent state as core capabilities rather than optional prompting tricks.
- **Execution-grounded evaluation and safety:** HazardAuditor evaluates runtime behavior, while OpenAI4S records provenance and NoteVQA tests the quality of grounded multimodal answers. The common shift is from judging text alone to judging actions and artifacts.
- **Benchmarks that expose deployment gaps:** NoteVQA shows large gaps on everyday visual questions; OpenAI4S reports weak full rerunnability; LongAgent finds only parity on real clinical data. These are more informative than headline benchmark gains alone.
- **Adaptive search over fixed pipelines:** AlgoEvo and LongAgent use history or feedback to change what is tried next, suggesting a move toward agents that learn search policy during a task.

## Open Problems and Research Directions

- **Reproducibility of scientific agents (OpenAI4S):** Persistent state and ledgers help, but full environment capture and rerunnability remain weak. A useful next experiment is independent replay by separate teams from frozen session records.
- **Reliability of long-horizon reasoning (Stellar Colosseum):** The reported benchmark results do not settle whether multi-agent decomposition generalizes beyond the tested models and tasks. Stress-test with adversarial proof gaps, hidden false lemmas, and held-out research domains.
- **Safety under heterogeneous tool use (HazardAuditor):** Canonical event representations may lose framework-specific context. Compare guards under unseen tools, permission regimes, and multi-step attacks, with calibrated false-positive costs.
- **Generalization of adaptive search (AlgoEvo, LongAgent):** Both papers report promising task-specific or synthetic results, while real-world transfer is less decisive. Evaluate across unseen datasets and measure compute, token, and human-review budgets alongside accuracy.
- **Cultural and compositional coverage in VLM evaluation (NoteVQA):** The benchmark is small and platform-specific. Expand to multilingual communities, accessibility needs, ambiguous images, and longitudinal user interactions while preserving expert-audited visual evidence.

## Takeaway

The clearest pattern in this batch is a research shift toward agents that manage processes: persistent sessions, adaptive search, verification, and runtime safety. The papers provide credible early evidence, but most are single-batch preprints with sparse external validation; the central question is whether these mechanisms transfer across models, tools, domains, and independently reproduced workflows.

## Method and sources

- **Window:** latest daily arXiv announcement batch, 2026-09-15; papers shown in the batch were submitted 2026-09-14 UTC. Snapshot: 2026-09-15 15:10 UTC.
- **Corpus:** arXiv recent listings for `cs.AI` and related core categories `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`.
- **Ranking:** inferred, not an official arXiv ranking; based on cross-list breadth, concrete evaluation evidence, conference/journal or artifact signals, deployment relevance, and recency. Citation counts were not yet reliably available for these same-day submissions.
- **Primary sources:** [cs.AI recent submissions](https://arxiv.org/list/cs.AI/recent); [Stellar Colosseum](https://arxiv.org/abs/2609.15983); [OpenAI4S](https://arxiv.org/abs/2609.15096); [HazardAuditor](https://arxiv.org/abs/2609.15134); [AlgoEvo](https://arxiv.org/abs/2609.15820); [NoteVQA](https://arxiv.org/abs/2609.15695); [LongAgent](https://arxiv.org/abs/2609.15859).
