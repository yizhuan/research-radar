# arXiv Trending AI — weekly report

Snapshot: 2026-09-25 16:05 UTC
Window: 2026-09-19 through 2026-09-25 UTC, inclusive

## Headline

This week's strongest signal is a shift from better single-turn answers toward agent systems that can generate their own training data, explore unfamiliar environments, coordinate tools over long horizons, and enforce policy at every action. The evidence is early: all selected papers currently have zero Semantic Scholar citations, so this is an inferred list of notable recent papers—not an official popularity or readership ranking.

## Top papers (ranked)

### 1. [Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents](https://arxiv.org/abs/2609.29892)
- **Abstract:** The paper presents a closed-loop framework that connects agentic data production, model training, and model–harness co-evolution for long-horizon mobile planning.
- **Authors:** Tingyu Qu, Weigao Sun, Yuecheng Liu, Yucheng Zhao, Yi Zhu, et al.
- **arXiv:** `2609.29892v1` (published 2026-09-24 14:38 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Semantic Scholar currently reports 0 citations and 0 influential citations; the paper has 66 references, a dedicated technical-report/project presence surfaced in web search, and a broad systems claim spanning data, training, memory, skills, tools, and sub-agent coordination. These are momentum/relevance signals, not popularity measurements.
- **Claimed contribution:** The authors introduce AI for Data, AI for Training, and execution-evidence-driven model–harness co-evolution, including CARE reward/advantage engineering; they report best overall performance among evaluated systems on MobilePA-Bench and gains on other agentic benchmarks.
- **Caveat:** These performance claims are author-reported in a new preprint; independent replication and details of benchmark comparability are not yet available.
- **Announcement type:** new submission, 2026-09-24
- **Themes:** Agents & reasoning; Training & adaptation; Robotics & control

### 2. [Self-Play Pretraining with Zero Data](https://arxiv.org/abs/2609.30063)
- **Abstract:** The paper proposes jointly training a generator and learner from random initialization, with the generator using reinforcement learning to create computable synthetic sequences at the learner's capability frontier.
- **Authors:** Aditya Cowsik, Kfir Dolev, Michael Y. Li, G. Bruno De Luca, Nourya Cohen, Noah D. Goodman, Yoav Levine
- **arXiv:** `2609.30063v1` (published 2026-09-24 16:23 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations; 52 references; cross-listing into AI and language; and unusually broad conceptual scope—zero-shot transfer from synthetic self-play without natural-data training. Ranking is based on methodological novelty and cross-category relevance, not citation count.
- **Claimed contribution:** The authors report predictable zero-shot-loss scaling with self-play compute on several natural datasets, plus in-context learning and discovery of recognizable mathematical sequences.
- **Caveat:** The authors describe this as an initial proof of concept; the gap between synthetic computable sequences and broad real-world pretraining remains unresolved.
- **Announcement type:** new submission, 2026-09-24
- **Themes:** Training & adaptation; Data & synthetic data; Agents & reasoning

### 3. [ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds](https://arxiv.org/abs/2609.30199)
- **Abstract:** ExplorationBench evaluates whether AI systems can discover and apply genuinely unfamiliar rules using executable “alien worlds” that make answers verifiable and defeat simple recall from pretraining.
- **Authors:** Ming Zhang, Zhenghao Xiang, Peizhong Gao, Yujiong Shen, Yuhui Wang, et al.
- **arXiv:** `2609.30199v1` (published 2026-09-24 17:37 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations; 40 references; two benchmark sandboxes, 140 tasks in total, and evaluation of 10 systems. The benchmark directly targets a widely discussed evaluation gap, and its AI/CL cross-listing supports relevance.
- **Claimed contribution:** The authors introduce AlienCode and AlienLogic, with executable rules, flawed manuals, feedback, and tool schemas; they report that strong systems acquire unfamiliar rules but show substantial trajectory variance and can regress with continued exploration.
- **Caveat:** The environments are deliberately designed sandboxes, so performance may not predict scientific discovery or open-world exploration.
- **Announcement type:** new submission, 2026-09-24
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Retrieval & knowledge

### 4. [SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance](https://arxiv.org/abs/2609.30192)
- **Abstract:** SAGE combines algebraic sparsification and hyperbolic structural guidance to reduce exploration and compounding biases in sparse-reward, long-horizon reasoning.
- **Authors:** Xinyue Zeng, Jiawei Zhang, Yujun Yan, Dawei Zhou
- **arXiv:** `2609.30192v1` (published 2026-09-24 17:33 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations; 41 references; the paper states acceptance at NeurIPS 2026; and it reports results across 12 benchmarks and 7 model families. The acceptance note and breadth of evaluation are stronger quality signals than recency alone.
- **Claimed contribution:** The authors introduce Symbolic Closure Analysis and the SAGE framework; they report gains over baselines across 12 benchmarks, including up to an eight-fold improvement on the Andrews–Curtis problem.
- **Caveat:** The headline improvements are paper-reported, and the transfer of algebraic/hyperbolic structural priors to less formal reasoning tasks needs independent testing.
- **Announcement type:** new submission, 2026-09-24
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 5. [ActGov: Governing LLM Agent Actions via Policy-Constrained Validation](https://arxiv.org/abs/2609.24446)
- **Abstract:** ActGov validates each proposed tool action at runtime against task-scoped authorization and policies learned from specifications, benign tasks, and failure traces.
- **Authors:** Kaiyuan Zhang, Yuke Peng, Ke Jiang, Yinqian Zhang
- **arXiv:** `2609.24446v2` (published 2026-09-22 10:20 UTC; categories: `cs.CR`, `cs.AI`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations; 15 references; a substantive v1-to-v2 revision during the window; cross-listing between security and AI; and evaluation on AgentDojo and AgentDyn. Web search also surfaced the paper among current agent-safety results.
- **Claimed contribution:** The authors introduce ActGov-Policy and ActGov-Runtime, using SMT-based counterexample checking and per-action enforcement; they report reduced indirect prompt-injection success while preserving task utility.
- **Caveat:** The evaluation covers selected benchmarks and attack configurations; deployment against evolving tool ecosystems and adaptive attackers remains open.
- **Announcement type:** revision, announcement 2026-09-22 (v2; first submitted 2026-09-21)
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 6. [BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents](https://arxiv.org/abs/2609.23490)
- **Abstract:** BabelArena extends agent evaluation across 23 languages using structure-preserving translation and multi-layer verification over 16,146 instances derived from 702 tasks.
- **Authors:** Peng Kuang, Yuchun Fan, Jiangnan Li, Minghao Wu, Jialong Tang, Hao-Ran Wei, Weixuan Wang, Jianhong Tu, Baosong Yang, Tong Xiao
- **arXiv:** `2609.23490v1` (published 2026-09-20 09:25 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations; 22 references; a large benchmark with 16,146 instances, 23 languages, 13 domains, and five evaluated frontier models. Its scale and direct relevance to multilingual agent reliability justify inclusion despite sparse external attention.
- **Claimed contribution:** The authors report that no model dominates across benchmark families, low-resource languages show more tool-use/control-flow errors, and token use can be roughly twice that of English without proportional interaction-length gains.
- **Caveat:** Translation and benchmark construction choices can affect cross-language comparisons; the reported disparities require replication with independently authored multilingual tasks.
- **Announcement type:** new submission, 2026-09-20
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Multimodal & vision-language

## Trending Research Themes

- **Long-horizon agents are becoming the organizing problem.** Qwen-Planner-Agent treats data, training, harnesses, memory, skills, and tools as a feedback loop; ActGov addresses safety at each tool action; SAGE targets sparse-reward reasoning; and ExplorationBench tests whether exploration itself is reliable.
- **Evaluation is moving from answer accuracy to process reliability.** ExplorationBench checks rule discovery in executable worlds, BabelArena measures language-dependent tool/control-flow failures, and ActGov evaluates attack success jointly with utility preservation.
- **AI-for-AI and synthetic-data loops are gaining prominence.** Qwen-Planner-Agent builds a human-gated data flywheel, while Self-Play Pretraining explores a more radical generator–learner curriculum with no natural training data.
- **Structural priors and explicit controls are re-entering reasoning systems.** SAGE uses algebraic and hyperbolic structure; ActGov uses authorization semantics and SMT checks. Both replace the hope that the base LLM will reliably infer the needed constraint at runtime.

## Open Problems and Research Directions

- **Open problem — exploration reliability:** ExplorationBench reports large trajectory variation and possible stalled or reversed gains. A useful follow-up is a longitudinal benchmark with repeated seeds, held-out worlds, and explicit measures of exploration efficiency, not just final success.
- **Open problem — synthetic self-play transfer:** Self-Play Pretraining demonstrates transfer in a proof-of-concept setting, but its relation to natural-data coverage is unclear. Test scaling laws across domains, model sizes, and generators while measuring contamination and mode collapse.
- **Open problem — end-to-end agent safety:** ActGov's per-action validation is evaluated on named benchmarks, not the full distribution of compositional, adaptive tool attacks. Stress-test policy synthesis under tool changes, stale state, colluding agents, and utility-preserving adversaries.
- **Open problem — multilingual control flow:** BabelArena finds low-resource tool-use and language-consistency failures. Build native, non-translated tasks and evaluate whether language-specific planners, localized tool schemas, or multilingual training reduce the gap at equal cost.
- **Research direction — closed-loop model–harness co-evolution:** Qwen-Planner-Agent provides an engineering template. Compare its feedback contract against fixed-harness baselines under matched compute, and publish failure-trace datasets so improvements can be independently reproduced.
- **Research direction — structural reasoning beyond formal domains:** SAGE's claimed gains motivate ablations isolating algebraic sparsification, hyperbolic guidance, and their interaction; then test whether the same priors help software, science, and embodied tasks without hand-designed structure.

## Takeaway

The week's clearest pattern is not one new model architecture; it is a systems agenda: agents must learn, explore, remember, act, and be constrained as an integrated loop. The most credible progress signals are better process benchmarks and explicit runtime structure, but external validation is still absent—Semantic Scholar shows zero citations for every selected paper—so treat all reported gains as preliminary.

## Method and sources

- Scope: `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`, with selected cross-listed papers.
- Window: first submissions or revisions from 2026-09-19 through 2026-09-25 UTC; revisions are labeled separately.
- Snapshot: 2026-09-25 16:05 UTC.
- arXiv has no official trending chart. The ordering is inferred from corroborated signals: independent web discoverability, Semantic Scholar citation/influential-citation metadata, cross-list breadth, substantive revisions, benchmark scale, project/technical-report availability, and stated venue acceptance. No paper in this snapshot had nonzero Semantic Scholar citations.
- Primary sources: the linked arXiv abstract pages for each paper; Semantic Scholar Graph API metadata queried by arXiv ID; web search for independent discoverability and project pages.
- This is a curated, evidence-limited snapshot, not a comprehensive popularity ranking or most-read list.
