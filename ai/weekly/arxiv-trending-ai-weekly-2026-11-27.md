# arXiv Trending AI — Weekly through 2026-11-27

**Headline:** AI (core arXiv categories), weekly window 2026-11-19 through 2026-11-26; 10 ranked papers. The clearest pattern is embodied AI moving from isolated policies toward persistent control, agent harnesses, and better physical-agency evaluation. We’ll cover robotics and world interaction first, then efficient model designs and the remaining evaluation gaps. This is an inferred ordering, not an official arXiv trending chart; citation evidence is limited for these very recent papers.

## Top papers (ranked)

### 1. [Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.29897)
- **Abstract:** The paper combines recurrent Mamba state, local attention, and persistent content memory for long-horizon controllable humanoid motion, reporting 39.52-second rollouts and lower inference latency.
- **Authors:** Yue Huang, Tianshan Zhang, Zeyu Zhang, Jayeon Kang, Akide Liu, et al.
- **arXiv:** `2611.29897v1` (published 2026-11-23 01:51:57 UTC; categories: `cs.RO`, `cs.CV`)
- **Evidence for ranking:** Collector score 18.355, the highest in this window’s candidate ranking; the Hugging Face paper card recorded 224 upvotes and 40 GitHub stars, with one cross-list. [Hugging Face signal](https://huggingface.co/papers/2611.29897); exact score and component values are in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors introduce persistent content memory and an execution path tailored to the Mamba-based diffusion model; the arXiv paper reports a 6.138× median paired speedup on an RTX 4090 while preserving tested outputs and states.
- **Caveat:** The authors state that the framework addresses controllable humanoid motion but not object manipulation; they identify whole-body loco-manipulation as future work.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-23)
- **Themes:** Robotics & control; Efficient inference & systems

### 2. [WorldLeague: Benchmarking Physical Agency](https://arxiv.org/abs/2611.30989)
- **Abstract:** WorldLeague evaluates progress toward physical goals across 60 simulated robot tasks and six capability dimensions, reporting both interactive progress and task success.
- **Authors:** Xinyang Zhou, Qi Li, Xinchao Wang
- **arXiv:** `2611.30989v1` (published 2026-11-23 16:44:19 UTC; categories: `cs.RO`)
- **Evidence for ranking:** Collector score 16.328; the Hugging Face paper card recorded 137 upvotes and 21 GitHub stars. [Hugging Face signal](https://huggingface.co/papers/2611.30989); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors propose a shared Physical Agency Profile that distinguishes physical progress from answering questions about an episode; in their evaluation of 13 systems, 71.8% of episodes with full terminal-QA credit received zero operation credit.
- **Caveat:** The reported comparison covers 60 simulated tasks and 13 representative systems; it does not establish how the profile transfers to physical robot deployments.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-23)
- **Themes:** Evaluation & benchmarks; Robotics & control

### 3. [Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://arxiv.org/abs/2611.31201)
- **Abstract:** Embo-Harness studies prompting, planning, action execution, and tool use in robotic harnesses that use frontier multimodal models directly as closed-loop policies.
- **Authors:** Xiao-Ming Wu, Kang Liao, Yuexiao Ma, Taolin Zhang, Mingqian Zhou, et al.
- **arXiv:** `2611.31201v1` (published 2026-11-23 18:48:54 UTC; categories: `cs.RO`)
- **Evidence for ranking:** Collector score 16.149; the Hugging Face paper card recorded 106 upvotes and 70 GitHub stars. [Hugging Face signal](https://huggingface.co/papers/2611.31201); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors distill six harness-design findings and report an 83.3% RoboLab-120 success rate, 26.2 percentage points above their strongest reported baseline, plus success in 15 of 20 zero-shot real-world trials.
- **Caveat:** The real-world evidence is 20 trials across four manipulation tasks, and the authors note that dexterous manipulation, locomotion, and tactile perception need capabilities beyond those tested.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-23)
- **Themes:** Robotics & control; Agents & reasoning

### 4. [3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013)
- **Abstract:** This work benchmarks rigging and instruction-driven motion across six 3D morphologies, then proposes an agent-written parametric program with deterministic execution for rigging and motion control.
- **Authors:** Bohan Zeng, Kaixin Zhu, Yifan Yang, Dongge Yu, Zihao Wu, et al.
- **arXiv:** `2611.30013v1` (published 2026-11-23 04:16:51 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Collector score 16.059; the Hugging Face paper card recorded 62 upvotes and 1,422 GitHub stars. [Hugging Face signal](https://huggingface.co/papers/2611.30013); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors introduce DivDynBench and an Agentic Motion Framework, arguing that compact parameterized controls paired with deterministic execution improve rigging reliability and motion accuracy.
- **Caveat:** The abstract describes comparative analyses but gives no numerical benchmark results, so the magnitude of the reported improvements cannot be assessed from the abstract alone.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-23)
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 5. [Real2SimLab: A Unified Platform for Real-to-Simulation Transfer](https://arxiv.org/abs/2611.34849)
- **Abstract:** Real2SimLab unifies evaluation of methods that generate simulation programs from real-world observations, running each program through the original benchmark scorer and supporting training-data generation.
- **Authors:** Yongchang Zhang, Jie Huang, Yunhe Ni, Ningyu Zhou, Guangyu Zhao, et al.
- **arXiv:** `2611.34849v1` (published 2026-11-25 18:23:41 UTC; categories: `cs.RO`, `cs.CV`)
- **Evidence for ranking:** Collector score 16.025; the Hugging Face paper card recorded 108 upvotes and 29 GitHub stars, with one cross-list. [Hugging Face signal](https://huggingface.co/papers/2611.34849); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors report support for 47 coding agents, five non-agent methods, and six benchmarks, plus a data-and-reward pipeline that filters benchmark videos to reduce contamination.
- **Caveat:** The reported platform coverage is six benchmarks; its usefulness beyond those scoring pipelines remains to be established by additional benchmark integrations.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-25)
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 6. [Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](https://arxiv.org/abs/2611.32884)
- **Abstract:** Reinforcement Learning with Verifiable Beliefs rewards an agent for gathering evidence while multiple answers remain plausible and committing when the simulator’s posterior is sufficiently concentrated.
- **Authors:** Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang, Soujanya Poria
- **arXiv:** `2611.32884v1` (published 2026-11-24 16:17:51 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Collector score 15.482; the Hugging Face paper card recorded 99 upvotes, 10 comments, and 27 GitHub stars. [Hugging Face signal](https://huggingface.co/papers/2611.32884); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors introduce RLVB and the Pro Worlds visual-puzzle benchmark; across three vision-language models and three benchmarks they report an average 17.1% improvement over the base models.
- **Caveat:** RLVB relies on an exact answer posterior available from its simulator during training; the abstract reports three models and three benchmarks, so broader settings remain untested here.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-24)
- **Themes:** Agents & reasoning; Training & adaptation

### 7. [Sage-Med: Scaling Medical Multimodal Intelligence](https://arxiv.org/abs/2611.34575)
- **Abstract:** Sage-Med-Preview is a 35B-parameter medical multimodal model with 3B active parameters, trained with curated medical data and a staged curriculum; the authors report results across 238 clinical tasks.
- **Authors:** Sage-Med Team, Ming Hu, Cheng Tang, Wei Li, Rongbin Li, et al.
- **arXiv:** `2611.34575v1` (published 2026-11-25 15:39:45 UTC; categories: `cs.CV`, `cs.AI`)
- **Evidence for ranking:** Collector score 15.338; the Hugging Face paper card recorded 89 upvotes and 23 GitHub stars, with one cross-list. [Hugging Face signal](https://huggingface.co/papers/2611.34575); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors present a staged data-and-training recipe and report an average 58.26% on 31 public multimodal benchmarks, alongside comparisons with other open and proprietary models.
- **Caveat:** The authors explicitly note continuing difficulty with complex medical reasoning and multi-step clinical workflows; the evaluation also includes private benchmarks, limiting independent reproduction of that portion.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-25)
- **Themes:** Multimodal & vision-language; Training & adaptation; Evaluation & benchmarks

### 8. [Rewirable Circuits in Transformers with Loom Attention](https://arxiv.org/abs/2611.30634)
- **Abstract:** Loom Attention lets Transformer heads attend both across tokens and over earlier heads, creating a dual-stream architecture that the authors evaluate for language modeling and downstream tasks.
- **Authors:** Da Xiao, Qingye Meng, Shengping Li, Xingyuan Yuan
- **arXiv:** `2611.30634v2` (first submitted 2026-11-23 13:00:54 UTC; v2 revised 2026-11-24 08:46:11 UTC; categories: `cs.LG`)
- **Evidence for ranking:** Collector score 15.152; the Hugging Face paper card recorded 93 upvotes and 20 GitHub stars. This is version 2, revised within the window. [Hugging Face signal](https://huggingface.co/papers/2611.30634); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors introduce LoomFormer’s per-token matrix memory and report that selected models match or surpass larger-compute Transformer and residual-stream baselines under their specified training budgets.
- **Caveat:** The headline comparisons are tied to the reported model sizes, token budgets, and language/downstream task suite; wider architecture families and workloads are not established by this abstract.
- **Announcement type:** revision, announcement-batch date not available (v2 submitted 2026-11-24; originally submitted 2026-11-23)
- **Themes:** Efficient inference & systems; Training & adaptation

### 9. [Mixture-of-Loops Transformer](https://arxiv.org/abs/2611.34923)
- **Abstract:** MoLT reuses key-value memories across Transformer loops, with variants designed for expressivity, efficient decoding, and skipping unused decoder traversals.
- **Authors:** Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai
- **arXiv:** `2611.34923v1` (published 2026-11-25 18:58:53 UTC; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** Collector score 15.119; the Hugging Face paper card recorded 69 upvotes, two comments, and 69 GitHub stars, with one cross-list. [Hugging Face signal](https://huggingface.co/papers/2611.34923); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors report 400B-token pretraining results for U-MoLT, including improved token efficiency at 700M parameters and comparable latency to a non-looped model in their small-model inference test.
- **Caveat:** Results are reported for specific sizes and training regimes (up to a 3B MoE model); the abstract does not establish whether the efficiency gains persist at substantially larger scales.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-25)
- **Themes:** Efficient inference & systems; Training & adaptation

### 10. [Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents](https://arxiv.org/abs/2611.28947)
- **Abstract:** NightWatch pairs a computer-use agent with a lightweight streaming perception model to keep its view of a changing desktop or web interface current while the agent reasons.
- **Authors:** Jiaqi Su, Jie-Jing Shao, Yichen Liu, Long-Kai Huang, Haiyan Yin
- **arXiv:** `2611.28947v1` (published 2026-11-21 17:31:05 UTC; categories: `cs.CL`, `cs.CV`)
- **Evidence for ranking:** Collector score 14.988; the Hugging Face paper card recorded 103 upvotes and four GitHub stars, with one cross-list. [Hugging Face signal](https://huggingface.co/papers/2611.28947); score record in the [weekly signals file](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json).
- **Claimed contribution:** The authors report that NightWatch reduces non-reasoning time by 33% and wasted time by 53% on OSWorld while maintaining task success, and raises success on DynaCU-Bench from 39.5% to 44.2% with a large VLM agent.
- **Caveat:** The reported evaluations cover desktop and dynamic web tasks; performance on mobile interfaces or other real-time environments is not established in the abstract.
- **Announcement type:** new submission, announcement-batch date not available (v1 submitted 2026-11-21)
- **Themes:** Agents & reasoning; Efficient inference & systems

## Trending Research Themes

- **Embodied AI is becoming a systems-and-evaluation problem, not only a policy-model problem.** Motion Mamba 2.0 couples memory and fast execution; Embo-Harness examines the closed-loop interface around a general model; WorldLeague measures physical progress rather than terminal verbal answers; Real2SimLab standardizes benchmark execution. The common shift is toward evaluating and engineering the whole action loop, not a single model score.
- **Agentic generation uses structured tools and iterative checking.** 3AGameFactory-Motion has an agent produce compact rigging/motion programs for deterministic execution, while Embo-Harness and Real2SimLab study how agents plan, act, and produce executable artifacts. These are related engineering choices, not evidence of one universally superior agent design.
- **Efficiency work is changing where computation and memory live.** Loom Attention and Mixture-of-Loops Transformer reuse internal state across heads or loops; Motion Mamba 2.0 uses recurrent state plus persistent content memory; NightWatch moves continuous perception into a small side model. Each paper reports a different trade-off, so the results are not directly comparable.
- **Specialized multimodal capability still depends on training and evaluation design.** Sage-Med reports a staged medical-data curriculum and broad clinical evaluation, while the authors also identify persistent gaps in complex reasoning and multi-step workflows. This is a strong but isolated medical-model signal within this ranked set.
- **Category mix is uneven:** among these ten, primary categories are cs.RO (4), cs.CV (2), cs.LG (2), cs.AI (1), and cs.CL (1). No ranked paper is primarily in cs.NE, stat.ML, or cs.MA; this reflects this attention-weighted shortlist, not the full AI corpus.

## Open Problems and Research Directions

- **Physical success under broader conditions — open problem:** WorldLeague reports a 60-task simulated benchmark, while Embo-Harness reports 20 real-world trials across four tasks and Motion Mamba 2.0 reports humanoid-control experiments without object manipulation. **Research direction:** test physical-agency metrics and control stacks on longer, more varied real-world tasks, including recovery, object interaction, and locomotion-manipulation coupling. (WorldLeague; Embo-Harness; Motion Mamba 2.0)
- **Evidence-based agent decisions outside simulators — open problem:** RLVB’s verifier uses an exact posterior supplied by its simulator. **Research direction:** evaluate whether approximate or learned uncertainty signals can preserve the benefit when exact posteriors are unavailable, and measure premature commitment and calibration on tasks with hidden state. (Lazy Agents Answer Against Their Own Beliefs)
- **Harness generality and interface sensitivity — open problem:** Embo-Harness notes that its conclusions depend on current frontier-model capabilities and that dexterity, locomotion, and tactile tasks require additional capabilities; Real2SimLab currently covers six benchmarks. **Research direction:** compare the same harnesses across new robots, action interfaces, and benchmark families, and report failures by sensing and control constraint. (Embo-Harness; Real2SimLab)
- **Efficiency claims across scale — open problem:** Loom Attention and MoLT show gains in specified sizes, datasets, and compute budgets, but those results do not settle behavior at larger scale or under different inference workloads. **Research direction:** run matched-token and matched-latency evaluations across model families, context lengths, and deployment hardware, including memory and energy costs. (Rewirable Circuits in Transformers with Loom Attention; Mixture-of-Loops Transformer)
- **Multimodal clinical reasoning — author-stated open problem:** Sage-Med reports that complex medical reasoning and multi-step clinical workflows remain challenging. **Research direction:** evaluate longitudinal, multi-step clinical tasks with public, independently reproducible data and explicit error analysis rather than relying only on aggregate benchmark scores. (Sage-Med)

## Notable shifts

The daily rollup covers five editions (2026-11-22 through 2026-11-26) and 36 unique papers. Among the ten papers ranked here, Mixture-of-Loops Transformer was already featured on 2026-11-26 at daily rank 2; it appeared once in the rollup. Six other daily features recurred twice, on 2026-11-22 and 2026-11-23: “Potential emergence in LLM agents: a statistical physics perspective” (best rank 1), “Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI” (rank 2), “SecretAgent: A Multi-Agent Framework for Privacy Protection against Vision Language Models” (rank 3), “Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs” (rank 4), “SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech” (rank 5), and “Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation” (rank 6). These are continuity signals from prior daily selections, not replacements for this week’s attention-based ordering.

## Takeaway

This week’s strongest attention signals cluster around embodied AI, where papers increasingly combine model architecture with memory, interfaces, execution, and benchmarks that measure physical outcomes. The ranking is provisional: several results are evaluated in bounded task suites, and the main unanswered question is how well the methods transfer across real-world settings and model scales.

## Method and sources

- **Window:** weekly; arXiv first submissions or revisions from 2026-11-19 19:00:00 UTC through 2026-11-26 19:00:00 UTC. Signal snapshot generated 2026-11-27 08:04:12 UTC; announcement batch date 2026-11-27.
- **Category query:** `cs.AI OR cs.LG OR stat.ML OR cs.CL OR cs.CV OR cs.RO OR cs.NE OR cs.MA`.
- **Ranking:** started from the supplied deterministic candidate pool (3,270 arXiv listings; 191 with attention; 150 retained candidates). The collector score and its component weights are in the weekly signals JSON; the top ten are ordered by that score. Available signals include Hugging Face paper-card upvotes/comments, GitHub stars, Hacker News activity where present, citation fields when available, and cross-list count. A zero score elsewhere in the pool was not treated as proof of unimportance. The top ten are attention-skewed toward robotics and vision, and are not exhaustive field coverage.
- **Unavailable source:** Semantic Scholar was unavailable in the supplied signal collection (HTTP 429), so citation and influential-citation signals could not corroborate this ranking. No citation-count claims are made.
- **Primary verification:** each selected abstract and version/date/category was checked on its linked arXiv abstract page. The top three papers’ arXiv HTML full texts were also inspected for results and limitations. Abstract and full-text claims are attributed to the authors; these are preprints, not settled findings.
- **Continuity source:** [daily rollup](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-27.rollup.json), covering the daily reports dated 2026-11-22 to 2026-11-26.
- **Signal source:** [weekly deterministic signals](/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-26.signals.json). Per-paper Hugging Face links are given alongside the scores above.
