# AI papers this week: agent learning, evaluation, and efficient scaling

For the 2026-09-25–2026-10-02 window (UTC), this shortlist has six papers, led by work on learning from agent failures and building stronger, more realistic agent evaluations; next are scaling and alignment benchmarks. I’ll cover the most concrete contributions, their evidence, and what remains uncertain. arXiv has no official trending chart: this ordering is inferred, not a popularity ranking, and very recent papers have little citation evidence (all six currently show zero Semantic Scholar citations).

## Top papers (ranked)

### 1. [Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training](https://arxiv.org/abs/2609.40111)
- **Abstract:** The paper releases 50,228 diagnosis/correction pairs from failed text-agent runs and reports improved replay success and diagnosis-label agreement after training on those signals.
- **Authors:** Kunlun Zhu, Xuyan Ye, Yibo Li, Cheng Qian, Beibin Li, Heng Ji
- **arXiv:** `2609.40111v2` (published 2026-10-01 04:54:01 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** A third-party technical write-up appeared alongside the arXiv listing; the paper is cross-listed in AI and language, and reports matched-replay results over 3,062 pairs. Semantic Scholar listed 0 citations at the snapshot.
- **Claimed contribution:** The authors' Agentic Error-to-Training pipeline links diagnoses and proposed repairs to recorded traces and, where possible, controlled replay; their abstract reports verifier pass rates rising from 18.4% to 51.1% for proposed repairs.
- **Caveat:** The reported experiments use distinct cohorts and protocols; the actor-training comparison is single-seed, and the corpus covers text-based agents.
- **Announcement type:** revision, 2026-10-01
- **Themes:** Agents & reasoning; Data & synthetic data; Training & adaptation

### 2. [PhantomEnvironments: Training LLM Agents in Fictional Worlds](https://arxiv.org/abs/2609.40221)
- **Abstract:** The authors train search agents in rule-generated fictional corpora and report transfer to real-world multi-hop search benchmarks, including newer benchmarks where fictional-world training sometimes outperforms real-world training data.
- **Authors:** Anmol Kabra, Swathi Saravana Selvam, Albert Gong, Chao Wan, Christian Belardi, et al.
- **arXiv:** `2609.40221v1` (published 2026-09-30 17:26:57 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The paper was picked up by multiple recent AI-paper roundups and commentary, and is cross-listed across machine learning, AI, and language. Semantic Scholar listed 0 citations at the snapshot.
- **Claimed contribution:** The authors claim that cheaply generated, rule-based fictional environments can provide verifiable RL practice for multi-hop search without LLM-generated training worlds.
- **Caveat:** The abstract's transfer evidence is for search tasks and particular benchmark suites; it does not establish broad transfer to other agent skills or domains.
- **Announcement type:** new submission, 2026-09-30
- **Themes:** Agents & reasoning; Training & adaptation; Data & synthetic data

### 3. [cua-speedrun: Standardized Benchmarking of the Speed of Computer-Use Agents](https://arxiv.org/abs/2609.40284)
- **Abstract:** The paper introduces a common virtual-machine setup and task interface for measuring computer-use agent performance, speed, and cost across four benchmarks, and reports that no model family leads on all three.
- **Authors:** Pranjal Aggarwal, Lawrence Keunho Jang, Sean Welleck, Daniel Fried, Ruslan Salakhutdinov, Jing Yu Koh
- **arXiv:** `2609.40284v1` (published 2026-09-30 17:48:06 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The paper has cross-category reach and was discussed in a public post by a coauthor, with catalog listings also surfacing it. Semantic Scholar listed 0 citations at the snapshot; the post is not independent confirmation.
- **Claimed contribution:** The authors provide standardized infrastructure for comparing speed and cost and report that reducing task sets can preserve statistical power on most of the evaluated benchmarks.
- **Caveat:** The findings concern the paper's four benchmark suites and standardized virtual-machine setup; they do not by themselves establish deployment speed or cost in every real-world environment.
- **Announcement type:** new submission, 2026-09-30
- **Themes:** Evaluation & benchmarks; Efficient inference & systems; Agents & reasoning

### 4. [Scaling Laws for Looped Mixture of Experts](https://arxiv.org/abs/2609.40316)
- **Abstract:** The authors propose scaling laws that jointly model recurrence and MoE sparsity, reporting improved held-out-loss prediction and parameter-efficiency results, including a trillion-token-scale comparison.
- **Authors:** Yanbei Chen, Anirudh Goyal, Raghuraman Krishnamoorthi
- **arXiv:** `2609.40316v1` (published 2026-09-30 17:53:47 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Cross-listed in machine learning, AI, and language; the paper combines a new scaling-law formulation with downstream evaluations and a reported trillion-token-scale experiment. Semantic Scholar listed 0 citations at the snapshot.
- **Claimed contribution:** The authors' bounded, sparsity-conditional recurrence mapping unifies recurrence, sparsity, model size, and data in a single scaling-law framework.
- **Caveat:** The efficiency and extrapolation claims are results from the authors' evaluated model and benchmark settings; broader scaling behavior remains to be independently tested.
- **Announcement type:** new submission, 2026-09-30
- **Themes:** Training & adaptation; Efficient inference & systems

### 5. [OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software](https://arxiv.org/abs/2609.39903)
- **Abstract:** This benchmark pairs 146 scientific-software tasks with artifact-based evaluators and an agent harness, and evaluates 12 vision-language models across scientific workflows.
- **Authors:** Dingyuan Dai, Heli Qi, Lei Liu, Yinxi Li, Baiding Chen, et al.
- **arXiv:** `2609.39903v1` (published 2026-09-30 15:03:05 UTC; categories: `cs.AI`)
- **Evidence for ranking:** A new benchmark with public project materials and concrete task counts; its artifact-based evaluation broadens the agent-evaluation theme in this week's papers. Semantic Scholar listed 0 citations at the snapshot.
- **Claimed contribution:** The authors connect expert-proposed scientific goals to execution-based checks of generated artifacts, while analyzing model and harness behavior.
- **Caveat:** Results cover the benchmark's 146 tasks, selected software, and 12 models; they should not be generalized to all scientific work or computer-use agents.
- **Announcement type:** new submission, 2026-09-30
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language; Agents & reasoning

### 6. [FIGS: Evaluating Multi-Turn Sycophancy Without Penalizing Empathy](https://arxiv.org/abs/2609.39863)
- **Abstract:** FIGS evaluates whether models maintain factual integrity during adaptive ten-turn conversations while separately measuring empathetic validation, using 500 scenarios and an automated judge.
- **Authors:** Sidharth Pulipaka, Ruta Binkyte, Ivaxi Sheth, Sahar Abdelnabi
- **arXiv:** `2609.39863v1` (published 2026-09-30 14:46:13 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The authors provide a released benchmark and evaluation environment, and the paper is cross-listed in AI and language; it targets a distinct reliability gap within the week's evaluation cluster. Semantic Scholar listed 0 citations at the snapshot.
- **Claimed contribution:** The authors separate unwarranted agreement from calibrated emotional validation in a multi-turn sycophancy evaluation.
- **Caveat:** The benchmark's scenarios and automated-judge setup are a proxy for real conversations; its scores do not alone establish how models behave across all users or settings.
- **Announcement type:** new submission, 2026-09-30
- **Themes:** Safety & alignment; Evaluation & benchmarks

## Trending Research Themes

- **Agent learning is shifting toward the failure trace, not just final reward.** Agent Error Dataset turns failed decisions into diagnosis and repair signals; PhantomEnvironments tests whether scalable synthetic interaction worlds can train search behavior.
- **Agent evaluation is becoming more operational and artifact-grounded.** cua-speedrun isolates speed and cost under standardized conditions; OSWorld-Science checks scientific outputs in the applications that produce them. Both underscore that the harness and environment affect measured performance.
- **Scaling and reliability are being made more explicit.** Scaling Laws for Looped MoE tries to jointly model recurrence and sparsity; FIGS treats honesty and empathetic support as separate axes over sustained dialogue. These are complementary directions, not evidence of a single breakthrough.

## Open Problems and Research Directions

- **Does diagnosis-driven repair generalize?** Agent Error Dataset reports strong matched-replay and diagnosis results, but its text-agent corpus and differing experimental cohorts leave transfer to unseen harnesses and modalities open. Follow-up: hold out entire environments and harness families, then test repair on fresh tasks with preregistered replay controls.
- **What is the scope of fictional-world transfer?** PhantomEnvironments reports transfer for multi-hop search. Follow-up: test on held-out domains and tasks requiring different skills, and compare synthetic curricula against matched-cost real data.
- **Can benchmark gains survive changed infrastructure?** cua-speedrun and OSWorld-Science both show that evaluation setup matters. Follow-up: replicate across independent machines, model versions, and task sets, reporting uncertainty and artifact-level success alongside latency and cost.
- **Are joint recurrence–sparsity laws robust beyond the tested scale?** The Looped MoE paper reports encouraging scaling experiments. Follow-up: validate its fitted law on independently trained architectures and larger held-out compute budgets before treating it as a general design rule.
- **Can a sycophancy metric retain empathy across populations?** FIGS separates validation from agreement using simulated multi-turn scenarios. Follow-up: audit human-rated conversations across cultures and user groups, and measure judge reliability and false positives for appropriate empathy.

## Takeaway

This week's clearest pattern is better measurement and reuse of agent interaction: researchers are building training data from failures and benchmarks that inspect real actions, artifacts, cost, and multi-turn behavior. The technical claims are promising but very fresh; citation counts are not yet informative, and the main evidence still needs independent replication.

## Method and sources

Window: 2026-09-25 through 2026-10-02 UTC (rolling seven calendar days); snapshot: 2026-10-02 01:10:10 UTC. Core category feeds reviewed: [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), and [cs.MA](https://arxiv.org/list/cs.MA/recent). This is a selective shortlist, not a complete census of the many thousands of recent category entries. Each selected paper's arXiv abstract page was checked; full text was reviewed for the top three. Semantic Scholar Graph metadata was checked for current citation totals; counts were zero for all six at retrieval. Third-party discussion checked includes [CCTest's AED overview](https://cctest.ai/en/articles/learning-from-failure-aed-scales-agent-error-diagnosis-to-50-000-pairs), recent [PhantomEnvironments coverage](https://monologg.kr/nlp-arxiv-daily/archive/2026-09/llm-agent/), and the [cua-speedrun coauthor's public post](https://x.com/wellecks/status/2105744715970716069). The latter is author commentary, not independent validation. Ranking is therefore inferred from available discussion, cross-listing, released resources, and concrete evaluation evidence—not downloads, views, or an official arXiv trend statistic. A broad arXiv API request was rate-limited; category recent pages and abstract pages were used instead.