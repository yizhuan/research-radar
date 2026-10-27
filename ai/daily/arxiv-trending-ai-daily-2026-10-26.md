# arXiv AI trending — Monday, 26 October 2026 (10 papers)

The selected batch points to agent evolution and evaluation as the strongest thread, alongside embodied models and practical efficiency. Spoken agenda: agent frameworks and reliability, embodied planning, then model and software efficiency. Snapshot: 2026-10-27 01:10:09 UTC; this uses the prior announcement batch, Monday 26 October, because no Tuesday batch was available at snapshot time. Global caveat: arXiv publishes no official trending chart, so this ordering is inferred from observable paper-list upvotes and independent curation; citation evidence is limited for these recent papers.

## Top papers (ranked)

### 1. [RSIHub: A Composable Framework for Agent-Evolution Methods](https://arxiv.org/abs/2610.32253)
- **Abstract:** RSIHub is an open framework for composing and comparing agent-evolution methods with shared execution, evaluation, recovery, and lineage services.
- **Authors:** Zimu Wang; Xiaobo Wang; Siyu Ye; Jiaqi Li; Silin Chen; et al.
- **arXiv:** `2610.32253v1` (published 2026-10-23T07:06:07Z; categories: `cs.AI`)
- **Evidence for ranking:** 24 upvotes in the 26 October daily paper list, the highest count among the selected batch papers; it was #3 in that list overall. The ranking uses this observed attention signal, not an arXiv popularity statistic.
- **Claimed contribution:** The paper presents a composable framework that instantiates four agent-evolution methods without changing its core, and reports gains up to 13.5 percentage points while showing that method rankings and held-out transfer vary by setting.
- **Caveat:** The authors state that the evidence depends on trusted framework and host services, valid evaluators, and tested workloads; the experiments cover fixed recipes, not adaptive recipe revision by an outer agent.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 2. [RynnUnify: Towards Unified Embodied Brain](https://arxiv.org/abs/2610.32965)
- **Abstract:** RynnUnify combines embodied understanding, interleaved video-language planning, and robot-action extensions in a 16B model, with evaluations spanning visual planning and simulated and real-robot tasks.
- **Authors:** Minghao Zhu; Bohan Hou; Kun Xiang; Zixuan Wang; Yinzhou Tang; et al.
- **arXiv:** `2610.32965v1` (published 2026-10-23T17:54:07Z; categories: `cs.RO` (primary), `cs.CV` (cross-list))
- **Evidence for ranking:** 17 upvotes in the 26 October daily paper list (#5 overall), plus #5 in ArXiv TLDR's weekly curated list updated 26 October.
- **Claimed contribution:** The authors introduce a unified embodied model and extensions for planning and robot control; they report a 9.75-point improvement over Cosmos 3 Nano on Rynn-VP, gains on Rynn-GEU, and 46.7% average success across three real-robot tasks.
- **Caveat:** The authors report that generated videos can distort fine geometry and call for broader validation of physical execution across tasks and environments; the real-robot result covers three tasks.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Multimodal & vision-language; Robotics & control; Agents & reasoning

### 3. [Every Weight Is a Path of Shared Discrete Decisions](https://arxiv.org/abs/2610.31931)
- **Abstract:** TWIG represents neural-network weights as paths of shared discrete decisions, unifying compression edits and enabling shift-and-add implementations for suitable hardware.
- **Authors:** Ammar Ali; Stamatis Lefkimmiatis
- **arXiv:** `2610.31931v1` (published 2026-10-22T21:21:32Z; categories: `cs.LG`)
- **Evidence for ranking:** 4 upvotes in the 26 October daily paper list (#7 overall); it follows the two selected papers with higher observed counts.
- **Claimed contribution:** The paper proposes TWIG as a shared representation for pruning, quantization, factorization, codebooks, and weight sharing; on LLaMA-3-8B it reports 9–15% fewer adders than GPTQ at equal layer error on typical matrices at 3- and 4-bit settings, with up to 55% fewer on outlier-heavy matrices.
- **Caveat:** The authors describe these as first measurements on selected models and layers; adder counts omit adder width and fixed-point truncation effects, making them a first-order circuit-size proxy rather than measured area. Direct training in TWIG remains future work.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Efficient inference & systems; Training & adaptation

### 4. [DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama Script Generation](https://arxiv.org/abs/2610.32002)
- **Abstract:** DraMaze combines trope-guided evolutionary search with a backward narrative-dependency memory tree and a bilingual benchmark for long microdrama scripts.
- **Authors:** Siyang He; Qiqi Wang; Fan Liu; Yuncheng Huang; Pengfei Xu; et al.
- **arXiv:** `2610.32002v1` (published 2026-10-22T23:54:48Z; categories: `cs.CL`)
- **Evidence for ranking:** 3 upvotes in the 26 October daily paper list (#8 overall); the count ties several other selected papers, so the source's list order is retained as the tie-breaker.
- **Claimed contribution:** The authors report that DraMaze reduces causal-pattern repetition by 32.1% and reaches a Logic score of 82.5 on 60-episode scripts, outperforming the best baseline by 8.5 points across their tested setup.
- **Caveat:** The evidence concerns bilingual microdrama generation and three backbone LLMs; it does not establish improvement in other long-form writing domains or human audience outcomes.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Data & synthetic data

### 5. [Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction](https://arxiv.org/abs/2610.32250)
- **Abstract:** Easy-3Dfy separates object generation from scene-layout estimation and aligns generated object meshes with partial scene point maps to construct 3D scenes from one image.
- **Authors:** Ziang Zhang; Wenyou Yi; Zehan Wang; Jiachen Xu; Xintong Han; et al.
- **arXiv:** `2610.32250v1` (published 2026-10-23T07:04:32Z; categories: `cs.CV` (primary), `cs.AI` (cross-list))
- **Evidence for ranking:** 3 upvotes in the 26 October daily paper list (#10 overall); it shares the 3-vote tier, with the source's ordering used as the tie-breaker.
- **Claimed contribution:** The paper proposes a modular geometric-composition workflow and reports better results than SAM-3Dfy across multiple geometric metrics on Scene-Maker and 3D-FUTURE200.
- **Caveat:** The reported evaluation is on those two benchmarks and relies on specialized object generators; the abstract does not establish transfer to other scene distributions or capture conditions.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Multimodal & vision-language; Training & adaptation

### 6. [DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model](https://arxiv.org/abs/2610.31734)
- **Abstract:** DirCast uses one streaming video-language model to select among player-camera feeds and generate commentary for live esports broadcasts from past frames.
- **Authors:** Zixian Gao; Lixin Xiu; Penghao Luo; Xiangcheng Cao; Ziqi Cai; et al.
- **arXiv:** `2610.31734v1` (published 2026-10-22T16:09:57Z; categories: `cs.CV`)
- **Evidence for ranking:** 3 upvotes in the 26 October daily paper list (#13 overall); the position follows the source's ordering within the tied 3-vote tier.
- **Claimed contribution:** The authors build a 27-match Dota 2 multi-camera dataset and report better directing than rule-based and zero-shot baselines, with commentary preferred in 29.2% of comparisons against GPT-4o under Proact-VL.
- **Caveat:** Evaluation is specific to 27 professional Dota 2 matches and the reported comparison protocol; cross-game or real broadcast deployment is not established.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Multimodal & vision-language; Efficient inference & systems

### 7. [Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance](https://arxiv.org/abs/2610.32555)
- **Abstract:** MCP-Injector tests tool-calling agents under failures calibrated from public MCP ecosystem incidents and finds severe task degradation under its fault profile, with no measured resilience gain from the larger of two tested backbones.
- **Authors:** Antonio Ken Iannillo; Joshua Segun Owotogbe; Roberto Natella; Francesco Avallone; Kristina Kudryavtseva; et al.
- **arXiv:** `2610.32555v1` (published 2026-10-23T12:35:51Z; categories: `cs.SE` (primary), `cs.AI` (cross-list))
- **Evidence for ranking:** ArXiv TLDR selected it as #1 in its weekly AI-paper list updated 26 October, citing the operational fault-tolerance result; this is a curator signal, not a readership metric.
- **Claimed contribution:** The authors introduce protocol-aware MCP fault injection calibrated from 57,240 issue and pull-request threads and report a 60% task-completion-score drop in a 1,350-cell evaluation.
- **Caveat:** The reported scale comparison is between two GPT-OSS backbones (20B and 120B), three agent stacks, and a permanent-heavy stress profile; it does not quantify failure rates for every deployed MCP system.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Safety & alignment

### 8. [The Butterfly Defects: Tracing Cooperation in LLM Agent Networks](https://arxiv.org/abs/2610.32726)
- **Abstract:** Experiments using the Iterated Prisoner's Dilemma show that cooperation among open-weight LLM agents changes with network composition, position, and small linguistic framing changes.
- **Authors:** Maria Sampani; Maria Lymperaiou; Angeliki Dimitriou; Giorgos Filandrianos; Chrysoula Zerva; et al.
- **arXiv:** `2610.32726v1` (published 2026-10-23T14:46:57Z; categories: `physics.soc-ph` (primary), `cs.CL` (cross-list))
- **Evidence for ranking:** ArXiv TLDR selected it as #2 in its weekly AI-paper list updated 26 October, highlighting its results on instability in multi-agent cooperation.
- **Claimed contribution:** The paper reports that cooperation is not stable across homogeneous and mixed populations, and that changing action-label order or adding uncertainty cues can alter behavior and affect agents several network hops away.
- **Caveat:** The evidence comes from Iterated Prisoner's Dilemma interactions with open-weight models; it should not be read as a general measurement of cooperation in deployed multi-agent systems.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 9. [Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations](https://arxiv.org/abs/2610.32891)
- **Abstract:** The study measures both inference energy and execution energy for LLM-generated code optimizations, finding that faster code is often more energy-intensive than human reference code in its benchmark setting.
- **Authors:** Sadra Emami; Benjamin Weigell; Mohammad Reza Mousavi; Gunel Jahangirova; Hugo Araujo; et al.
- **arXiv:** `2610.32891v1` (published 2026-10-23T16:58:01Z; categories: `cs.SE` (primary), `cs.AI` (cross-list))
- **Evidence for ranking:** ArXiv TLDR selected it as #4 in its weekly AI-paper list updated 26 October, calling out the energy/performance mismatch.
- **Claimed contribution:** Across 11 open-source models and 1,000 EffiBench problems, the paper reports that 42 of 44 tested configurations used more execution energy per problem than canonical human solutions; it also identifies output-token limits and model architecture as energy levers.
- **Caveat:** These measurements concern the evaluated open models, configurations, benchmark, and hardware setup; they do not imply the same energy trade-off for all code-generation workloads or deployment systems.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Efficient inference & systems; Evaluation & benchmarks

### 10. [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](https://arxiv.org/abs/2610.32971)
- **Abstract:** RobustRLlib unifies 17 robust online, offline, and safe reinforcement-learning algorithms and evaluates them across diverse shift and perturbation settings.
- **Authors:** Xi Chen; Fengqi Hu; Zeyu Shen; Jiaying Xu; Shangding Gu; et al.
- **arXiv:** `2610.32971v1` (published 2026-10-23T17:57:22Z; categories: `cs.LG` (primary), `cs.AI`, `cs.RO` (cross-lists))
- **Evidence for ranking:** ArXiv TLDR selected it as #10 in its weekly AI-paper list updated 26 October, citing the breadth of its unified evaluation platform.
- **Claimed contribution:** The authors provide a common library and benchmark covering 17 algorithms and 273 perturbation configurations, with the aim of exposing where existing robust-RL methods work and where they fail.
- **Caveat:** The empirical capability map is bounded by the selected algorithms, tasks, and perturbations; performance in the suite does not guarantee robustness in an untested real deployment.
- **Announcement type:** new submission, Monday 26 October 2026 batch
- **Themes:** Robotics & control; Evaluation & benchmarks; Safety & alignment

## Trending Research Themes

- **Agent systems need explicit evaluation and operational safeguards.** RSIHub makes candidate history, evaluation boundaries, and recovery reusable; MCP-Injector tests operational tool failures; RobustRLlib maps performance under shifts. Together these papers emphasize reproducible failure testing, not just capability demonstrations.
- **Embodied and streaming models are being judged on sustained action, not a single answer.** RynnUnify links visual prediction to planning and robot action, while DirCast makes repeated camera-selection and commentary decisions from a live stream. These are distinct applications, but both depend on maintaining useful context over time.
- **Efficiency is being measured beyond parameter count or latency.** TWIG explores discrete weight representations and shift/add computation, while Green Code measures the energy cost of both model-side optimization and generated code execution. The methods differ; the shared methodological shift is measuring resource costs directly.
- **A narrower creative-generation signal appears in DraMaze.** Its future-aware narrative memory targets repetition in long scripts, but one selected paper is not enough to claim a broad change in language-model generation research.
- **Selection-only category mix:** the ten papers span `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`, and `cs.RO` (with some cross-lists); the observed sample leans toward agent evaluation and embodied systems. This is not a category-share estimate for the full announcement batch.

## Open Problems and Research Directions

- **Author-stated — trust boundaries for agent evolution:** RSIHub's guarantees rely on trusted framework, host, filesystem, Git/digest, and evaluator services, and its reported runs use fixed recipes. A follow-up could test adaptive outer-agent changes under independent attestation, stronger isolation, and rollback checks (RSIHub).
- **Author-stated — prediction quality versus physical success:** RynnUnify notes fine-geometry distortions in generated video and calls for broader physical validation. Test geometry-sensitive uncertainty measures and whether visual-planning scores predict closed-loop robot outcomes across more tasks and environments (RynnUnify).
- **Author-stated / synthesis — from a weight representation to deployed efficiency:** TWIG's reported comparison covers five weight matrices, while direct training in the representation remains open. Evaluate full models at matched quality on real accelerators, reporting latency, memory traffic, energy, and robustness to outlier-heavy layers (Every Weight Is a Path of Shared Discrete Decisions).
- **Synthesis — operational reliability under varied faults:** MCP-Injector's results use a calibrated, permanent-heavy profile and two model sizes. Extend tests to broader fault distributions and model/framework combinations, and report whether recovery behavior transfers from controlled injection to live tool traces (Tool-Calling LLM Agents Under Realistic MCP Faults).

## Takeaway

The clearest signal in this batch is a push toward agents that can be measured under changing environments, tool failures, and long-horizon tasks—not simply prompted to perform well once. Embodied planning and resource-aware model design are also visible, but the evidence is still preprint- and benchmark-specific; broader physical and deployment validation remains open.

## Method and sources

- **Window:** Daily; announcement-batch date 2026-10-26 (Monday). Exact batch window: 2026-10-26 to 2026-10-26. Snapshot: 2026-10-27T01:10:09Z. This is the latest prior batch because no Tuesday 27 October batch was available at snapshot time.
- **Category query:** `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`.
- **Collection and verification:** Scanned the 26 October group on official arXiv recent pages for all eight configured categories, then retained papers supported by observable attention/curation signals. Each selected ID, version, abstract, publication timestamp, and category was checked against arXiv metadata and its abstract page; the first three ranked papers were also read in full text (HTML/PDF) for results and limitations. All ten selected items are v1 new submissions in the 26 October announcement group.
- **Inference:** Ordering is inferred, not supplied by arXiv. The first six entries follow observed upvote counts from the 26 October paper list (24, 17, 4, 3, 3, 3; source-list position breaks ties); later entries follow an independent weekly curator's order (#1, #2, #4, #10). Votes are a current attention signal, not downloads or citations. No citation totals are reported.
- **Citation evidence:** Semantic Scholar Graph citation fields were checked but not available in this snapshot after the endpoint rate-limited requests; recent papers were therefore ranked using the independent attention signals above. No failure or zero count is imputed to any paper.
- **Sources:** [Official arXiv recent pages](https://arxiv.org/list/cs.AI/recent), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch), [Hugging Face daily papers for 26 October](https://huggingface.co/papers/date/2026-10-26), [Trending AI Today, week 44 (daily upvote list)](https://trendingai.today/week/2026-44/), and [ArXiv TLDR weekly selections](https://arxivtldr.org/weekly). Canonical arXiv abstract URLs are linked per paper.
- **Retrieval note:** The configured `web_extract` backend was search-only; arXiv abstracts and full texts were instead verified through direct arXiv pages, the arXiv export API, and full-text HTML/PDF retrieval where practical.
