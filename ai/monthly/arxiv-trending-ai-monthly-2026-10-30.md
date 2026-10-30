# arXiv Trending AI — October 2026

October 2026 arXiv AI, 8 ranked papers first submitted or revised Oct 6–27: agent memory and interactive multimodal environments are the strongest recurring pattern. Agenda: memory-native models, visual agents and world models, then serving and evaluation. arXiv has no official trending chart; this ordering is inferred from platform engagement and corroborating signals, and citation evidence remains sparse for recent papers.

Window: 2026-10-01 through 2026-10-30 inclusive. Snapshot: 2026-10-30 03:19:03 UTC.

## Top papers (ranked)

### 1. [Jeva: System One Models from First Principles](https://arxiv.org/abs/2610.18773)
- **Abstract:** Jeva treats structured decision-making as a native model task, separating reusable request/option representations from set-dependent choice while supporting null answers, permutation consistency, variable-size candidate sets, and caching.
- **Authors:** Qi Li, Xinchao Wang
- **arXiv:** `2610.18773v2` (published 2026-10-13T17:31:09Z; categories: `cs.AI`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 404 upvotes at the snapshot; Semantic Scholar reported 4 citations (0 influential) and 24 references. The paper also reports tests across open-source decision models and thousands of candidates; the latter are author-reported evaluation scope, not an independent popularity measure.
- **Claimed contribution:** The authors introduce a decision-native architecture with a separate coverage gate for null decisions and cached option-side computation, reporting near-perfect null detection and no decision flips under tested permutations.
- **Caveat:** The reported invariance and null-detection results are bounded by the evaluated models and tested permutations; the abstract does not establish robustness across arbitrary decision tasks.
- **Announcement type:** revision, 18 Oct 2026 (v2; first submitted 13 Oct 2026)
- **Themes:** Evaluation & benchmarks; Efficient inference & systems; Training & adaptation

### 2. [WeVisOne-VL: Unified Visual Perception from Objects to Pixels](https://arxiv.org/abs/2610.31329)
- **Abstract:** WeVisOne-VL unifies object-level and pixel-level vision-language tasks through structured outputs and a lightweight pixel decoder, and reports evaluations on more than 30 benchmarks.
- **Authors:** Tianming Liang, Junyi Pan, Yuxi Li, Canmiao Fu, Zhipeng Huang, et al.
- **arXiv:** `2610.31329v2` (published 2026-10-22T14:19:50Z; categories: `cs.CV`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 258 upvotes at the snapshot. Semantic Scholar reported 0 citations and 127 references; the paper reports evaluation across 30+ benchmarks and releases code and model weights. The platform engagement is the main ranking signal.
- **Claimed contribution:** The authors connect structured object predictions to instance-level masks and mattes through an `<OBJ>` token and pixel decoder, followed by supervised curriculum training and mixed-task reinforcement learning.
- **Caveat:** The authors state that the current model is single-turn, omits chain-of-thought reasoning, and may trade off general capability; clear benchmark prompts may understate difficulty with vague real-world instructions.
- **Announcement type:** revision, 24 Oct 2026 (v2; first submitted 22 Oct 2026)
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Training & adaptation

### 3. [VideoJev: System One Model for Video Understanding and Interaction](https://arxiv.org/abs/2610.18615)
- **Abstract:** VideoJev scores temporal intervals and textual options directly against video evidence, reusing visual computation for follow-up queries; the authors report improved temporal-grounding scores and large inference speedups on video QA.
- **Authors:** Yuhan Zhu, Xiangyu Zeng, Qingyi Si, Chenxu Yang, Yifei Li, et al.
- **arXiv:** `2610.18615v1` (published 2026-10-13T16:00:41Z; categories: `cs.CV`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 241 upvotes at the snapshot; Semantic Scholar reported 1 citation (0 influential) and 58 references. The paper’s public project page and reported results across three grounding and four video-QA benchmarks provide corroboration beyond the vote count.
- **Claimed contribution:** The authors report that cached and joint inference reuse visual computation, improving mean mIoU by 6.7 and 10.8 points for the 4B and 35B-A3B models over their backbones, with 2.8–3.1× grounding speedups and over 100× video-QA speedups in the stated setup.
- **Caveat:** The measured speedups and quality claims are tied to the selected temporal-grounding and video-QA benchmarks and the paper’s repeated-query inference setup; they do not establish the same gains for arbitrary video-agent workflows.
- **Announcement type:** new submission, 13 Oct 2026
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Evaluation & benchmarks

### 4. [MemT-1.0: Towards Memory-Native Evolution](https://arxiv.org/abs/2610.26825)
- **Abstract:** MemT-1.0 adds persistent, model-internal memory with token-level updates and Mixture-of-Storage capacity scaling, reporting results on memory and general-capability benchmarks and agentic coding tasks.
- **Authors:** Zhiyu Li, Zeyu Zhang, Linyun Liu, Yiwei Bu, Chenyang Xi, et al.
- **arXiv:** `2610.26825v2` (published 2026-10-19T17:54:35Z; categories: `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 183 upvotes at the snapshot. Semantic Scholar reported 2 citations, including 1 influential citation; the paper is cross-listed in two core AI categories and reports evaluation on 11 memory benchmarks. Citation totals are current counts, not October gains.
- **Claimed contribution:** The authors introduce stable Gated DeltaNet-2 memory updates and Mixture-of-Storage; they report that MemT-1.0-Nano at 128K history is 1.86× faster end-to-end and uses 66× less persistent storage than a full-context KV cache.
- **Caveat:** The authors identify a fixed-size memory-state trade-off: constant storage limits detailed historical fidelity as interactions accumulate, and how local memory should consolidate into trainable hyper memory remains open.
- **Announcement type:** revision, 20 Oct 2026 (v2; first submitted 19 Oct 2026)
- **Themes:** Agents & reasoning; Efficient inference & systems; Training & adaptation

### 5. [AgentGarten: Code Worlds for Evolving Agents](https://arxiv.org/abs/2610.12374)
- **Abstract:** AgentGarten couples stateful simulators with a shared neural renderer so agents can learn from visual interaction and pass playbooks from one round of experience to later agents.
- **Authors:** Jiawei Chi, Shangchen Miao, Zhiyuan Shi, Kailu Wu, Hanyang Wang, et al.
- **arXiv:** `2610.12374v2` (published 2026-10-08T17:32:00Z; categories: `cs.CV`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 180 upvotes at the snapshot and labels it “#1 Paper of the day”; Semantic Scholar reported 1 citation (0 influential) and 77 references. The reported ranking is supported principally by the platform engagement, not by citation totals.
- **Claimed contribution:** The authors combine code-defined environments, a real-time neural renderer and inherited experience playbooks; their study reports learning behaviors after four rounds in a hide-and-seek environment, compared with millions of rounds for a conventional RL counterpart.
- **Caveat:** The reported efficiency comparison is within the authors’ simulator-based tasks and baseline setup; it does not establish transfer to arbitrary or physical environments.
- **Announcement type:** revision, 10 Oct 2026 (v2; first submitted 8 Oct 2026)
- **Themes:** Agents & reasoning; Robotics & control; Multimodal & vision-language

### 6. [TokenRouter: Efficient Serving System for Token-Level LLM Routing](https://arxiv.org/abs/2610.12242)
- **Abstract:** TokenRouter serves token-level LLM routing with request-centric programming, asynchronous model execution and delayed batching, reporting 2.01–64.15× higher decoding throughput than the compared systems.
- **Authors:** Tianyu Fu, Tengxuan Liu, Ruoxi Wang, Yixin Dong, Yi Ge, et al.
- **arXiv:** `2610.12242v1` (published 2026-10-08T16:21:50Z; categories: `cs.CL`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 144 upvotes at the snapshot. The arXiv record says the work was accepted by NeurIPS 2026 and links code; Semantic Scholar reported 0 citations and 36 references. The acceptance and engagement are independent corroborating signals.
- **Claimed contribution:** The authors separate routing logic from serving execution and report higher decoding throughput across routing algorithms, workloads and model pairs.
- **Caveat:** The throughput model assumes a geometric distribution for tokens between consecutive sends; the authors leave corner cases that violate this assumption for future work.
- **Announcement type:** new submission, 8 Oct 2026
- **Themes:** Efficient inference & systems; Agents & reasoning

### 7. [Hy-Nomas: Towards Free-form Interactive World Generation](https://arxiv.org/abs/2610.36729)
- **Abstract:** Hy-Nomas is an 8B diffusion world model for multi-turn text and camera control that carries history across generated video segments using action-aware causal attention and structured captions.
- **Authors:** Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng, Tiankai Hang, Ji Hou, et al.
- **arXiv:** `2610.36729v1` (published 2026-10-27T06:48:59Z; categories: `cs.CV`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 126 upvotes at the snapshot, despite only 2.9 days since first submission; Semantic Scholar reported 0 citations and 120 references. The authors release weights, code and benchmarks, while the recent submission age makes citation totals a weak discriminator.
- **Claimed contribution:** The authors combine action-aware causal attention, a vision-language Prompt Enhancer and progressive training; on their 280-case Hy-Nomas-Bench they report human-evaluation advantages over selected interactive world models.
- **Caveat:** The authors’ benchmark focuses on prompt following, physical plausibility, camera control and spatial memory rather than visual fidelity, aesthetics or audio; they also note that temporal causality alone does not ensure physical causality.
- **Announcement type:** new submission, 27 Oct 2026
- **Themes:** Multimodal & vision-language; Robotics & control; Evaluation & benchmarks

### 8. [Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?](https://arxiv.org/abs/2610.08215)
- **Abstract:** Learn2Play Bench uses text games with novel or counterintuitive rules to test whether agents learn through repeated interaction rather than rely on pretrained knowledge, and compares models, harnesses and human players.
- **Authors:** Yibo Li, Jinhang Qiu, Zhi Zheng, Qianyun Guo, Jiaying Wu, et al.
- **arXiv:** `2610.08215v2` (published 2026-10-06T12:08:45Z; categories: `cs.AI`)
- **Evidence for ranking:** Hugging Face’s paper page displayed 60 upvotes at the snapshot; Semantic Scholar reported 1 citation (0 influential). Its lower engagement places it below the other selected papers, while the benchmark’s explicit human comparison adds a distinct evaluation signal.
- **Claimed contribution:** The authors report that full action-and-feedback histories can help more than distilled rules in their test settings, that the best human players outperform evaluated agents, and that harness changes can improve performance while reducing estimated cost.
- **Caveat:** The benchmark uses text-based games and evaluates learning without model-weight updates; the authors’ results do not establish transfer to open-ended environments or show that current agents match human exploration.
- **Announcement type:** revision, 8 Oct 2026 (v2; first submitted 6 Oct 2026)
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Data & synthetic data

## Trending Research Themes

- Persistent agent memory is shifting from retrieval-only stores toward memory that is updated or learned through experience. MemT-1.0 internalizes memory in model computation, while Learn2Play Bench and AgentGarten test how agents retain and reuse experience across attempts.
- Interactive visual environments connect perception to action and state over time. AgentGarten builds stateful rendered worlds; Hy-Nomas supports repeated text/camera control; VideoJev reuses video features for repeated judgments. These are related agendas, not evidence that a single world-model approach has won.
- Structured, efficient inference appears in both decision models and serving systems. Jeva and VideoJev replace some open-ended generation with direct scoring, while TokenRouter tackles the system-level cost of token-by-token routing. Their mechanisms solve different bottlenecks, so the shared theme is efficiency-oriented specialization rather than a demonstrated common breakthrough.
- Evaluation is increasingly probing conditions hidden by static, familiar tasks: Learn2Play uses novel game rules, Hy-Nomas tests multi-turn control and spatial memory, and WeVisOne-VL includes absent-target rejection. Whether these test-time gains transfer to less curated real-world use remains unresolved.

## Open Problems and Research Directions

- **Open problem (authors’ statement):** MemT-1.0’s bounded memory state can lose historical detail, and the relationship between local experience and trainable hyper memory remains unresolved. **Research direction (synthesis):** Compare adaptive capacity and consolidation strategies on long, contradictory histories, measuring exact recall, update latency and storage together. [MemT-1.0](https://arxiv.org/abs/2610.26825)
- **Open problem (authors’ statement):** WeVisOne-VL is single-turn and may have difficulty with vague or hesitant user instructions; Hy-Nomas notes that temporal causal attention does not by itself guarantee physically correct action outcomes. **Research direction (synthesis):** Evaluate multi-turn, ambiguous instructions and action-conditioned state changes with held-out scenes and task-success measures, not only isolated localization or human preference. [WeVisOne-VL](https://arxiv.org/abs/2610.31329), [Hy-Nomas](https://arxiv.org/abs/2610.36729)
- **Open problem (authors’ statement):** Hy-Nomas’ benchmark omits visual fidelity, aesthetics and audio, while world-model memory must handle changes occurring off-screen. **Research direction (synthesis):** Test longer rollouts with revisited scenes, independently scored visual quality and explicit world-state updates; extend toward robot-action data only where executable action outcomes can be verified. [Hy-Nomas](https://arxiv.org/abs/2610.36729)
- **Open problem (authors’ statement):** Learn2Play’s evaluated human players achieve higher peak scores and explore more varied strategies than the tested agents. **Research direction (synthesis):** Isolate exploration diversity from memory and harness effects, then test whether successful strategies transfer to unseen game instances and non-text environments. [Learn2Play Bench](https://arxiv.org/abs/2610.08215)
- **Open problem (authors’ statement):** TokenRouter’s throughput model assumes geometrically distributed token intervals between sends. **Research direction (synthesis):** Stress-test scheduler behavior under heavy-tailed, bursty and adversarial routing traces and report tail latency alongside throughput. [TokenRouter](https://arxiv.org/abs/2610.12242)

## Takeaway

The month’s strongest attention signal clusters around agents that remember and act in persistent environments, alongside visual systems that make structured judgments more efficiently. The field evidence is still early: platform votes are not a universal popularity measure, citation totals are small, and benchmark gains do not yet settle long-horizon reliability or real-world transfer.

## Method and sources

- **Scope and window:** Monthly report covering 2026-10-01 through 2026-10-30 inclusive; snapshot 2026-10-30 03:19:03 UTC. Core categories: `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`.
- **Candidate query:** arXiv API category OR query across those eight categories, with `submittedDate:[202610010000 TO 202610302359]`; 15,765 unique first-submission records were returned for the window, with the newest dated 2026-10-29 at snapshot time. Category mentions were concentrated in `cs.LG` (6,278) and `cs.AI` (5,999); cross-listed category counts overlap.
- **Ranking method:** Inferred shortlist, not an arXiv ranking. The main attention measure was the cumulative upvote count displayed on each selected Hugging Face Papers page at the snapshot (not downloads or abstract views); Semantic Scholar Graph API citation and influential-citation totals were checked as corroboration, not treated as period gains. Published conference acceptance or released code/model/benchmark artifacts are noted where available. Recent-paper counts and platform engagement are both incomplete signals.
- **Version handling:** Latest arXiv abstract pages were checked for all eight papers. Five entries use v2 revisions dated within the window; three are new submissions. Each entry gives the first-submission timestamp and identifies the latest in-window revision separately.
- **Coverage limitation:** The broad arXiv API candidate retrieval was date-filtered on first submissions. Revision metadata was checked for selected candidates, but older papers first submitted before October and revised during the window were not exhaustively enumerated; accordingly, this is a notable recent shortlist, not comprehensive coverage of every revised paper.
- **Sources:** [arXiv API](https://export.arxiv.org/api/query), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.18773?fields=title%2Cauthors%2Cyear%2CcitationCount%2CinfluentialCitationCount%2CreferenceCount%2CpublicationTypes%2CfieldsOfStudy%2CexternalIds), and Hugging Face Papers pages for [Jeva](https://huggingface.co/papers/2610.18773), [WeVisOne-VL](https://huggingface.co/papers/2610.31329), [VideoJev](https://huggingface.co/papers/2610.18615), [MemT-1.0](https://huggingface.co/papers/2610.26825), [AgentGarten](https://huggingface.co/papers/2610.12374), [TokenRouter](https://huggingface.co/papers/2610.12242), [Hy-Nomas](https://huggingface.co/papers/2610.36729), and [Learn2Play Bench](https://huggingface.co/papers/2610.08215).
