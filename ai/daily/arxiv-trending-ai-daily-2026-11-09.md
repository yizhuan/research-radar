# arXiv AI — Daily | 9 Nov 2026

Latest arXiv AI announcement batch (Mon, 9 Nov 2026): six notable papers, with a strong cluster around agentic systems, test-time scaling, and embodied control. Spoken agenda: parallel agent teams, embodied generalists, then reuse and safer evaluation. Global caveat: arXiv has no official trending chart; this is an inferred ranking from sparse, checkable attention signals, and citation evidence is limited for papers this recent.

## Top papers (ranked)

### 1. [On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)
- **Abstract:** The authors introduce AMP1, a generalist model-in-the-loop robot manipulation harness, and report strong zero-shot benchmark and real-robot results against specialist policies.
- **Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi et al.
- **arXiv:** `2611.09892v1` (published 2026-11-06T18:59:34Z; categories: `cs.RO`, `cs.AI`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Cross-listed across four core AI categories; surfaced in independent coverage by [CryptoBriefing](https://cryptobriefing.com/apple-amp1-ai-models-control-robot-arms/) and [Singularity Radar](https://singularityradar.com/items/generalist-agentic-models-beat-specialist-manipulation-policies/), in addition to its [project page](https://apple-aiml-research.github.io/ml-amp/) and public [code release](https://github.com/apple-aiml-research/ml-amp). The multiple category and discussion signals place it first; reported experiment results are author claims, not independent replications.
- **Claimed contribution:** The paper presents AMP1, a shared harness for direct model control across robot embodiments; the authors report 85.6% zero-shot success on RoboLab-120 and success in 104 of 108 real-world trials.
- **Caveat:** The authors say the approach is slow because the robot waits for model reasoning and cannot revise an executing trajectory; evaluations mainly use quasi-static scenes, so it is not yet suitable for mission-critical deployment.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Robotics & control

### 2. [Test-Time Compute Scales Better with Parallel Agent Teams](https://arxiv.org/abs/2611.09798)
- **Abstract:** The paper proposes sampling many small collaborating agent teams in parallel and keeping the best verifier-scored team's result, reporting gains over independent agents and one large team on long-horizon tasks.
- **Authors:** Junlin Wang, Haozhe Chen, Ang Li, Rahul Chalamala, Zhuang Liu
- **arXiv:** `2611.09798v1` (published 2026-11-06T17:53:07Z; categories: `cs.AI`)
- **Evidence for ranking:** Independent discussion surfaced at [DAIR.AI Academy](https://academy.dair.ai/papers/test-time-compute-scales-better-with-parallel-agent-teams-2611.09798) and [arXivSignals](https://arxivsignals.io/papers/2611.09798), alongside an [OpenReview listing](https://openreview.net/forum?id=ZweFYN4Dy1) and released [code](https://github.com/modal-projects/parallel-agent-teams-scaling). The broad technical discussion and 12-task evaluation support its placement near the top; the paper has only the cs.AI category.
- **Claimed contribution:** The authors report that, with a 27B model and a budget of 100 agents, teams of ten beat parallel individual agents on 10 of 12 tasks and beat a single 100-agent team on all four tasks tested at that size.
- **Caveat:** The paper notes small run pools (10–11 runs per task), only one to five runs for larger-team sizes, and use of one agent harness; without a verifier, selecting the best team becomes an additional problem.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Efficient inference & systems

### 3. [Video-Coder: Reinforcing Agentic Coding for Video Generation](https://arxiv.org/abs/2611.09894)
- **Abstract:** Video-Coder trains an agent to write and execute code for a structured 3D draft video that guides a downstream video generator, using supervised fine-tuning and harness-native reinforcement learning.
- **Authors:** Chaoyang Wang, Sicheng Gao, Junan Hu, Kunyang Li, Dongyang Chen et al.
- **arXiv:** `2611.09894v1` (published 2026-11-06T18:59:57Z; categories: `cs.CV`)
- **Evidence for ranking:** The paper surfaced as [#7 on alphaXiv's trending page](https://www.alphaxiv.org/abs/2611.09894) at the checked snapshot; the team announced its [code, model, and data release on 8 Nov](https://github.com/CYWang735/Video-Coder), and a [Hugging Face paper page](https://huggingface.co/papers/2611.09894) also surfaced. These are external platform/release signals, not arXiv readership statistics.
- **Claimed contribution:** The authors combine two curated datasets, a code-execution/3D-rendering harness, and reinforcement learning with execution and video rewards; they report gains of about 7 points on PhyGenBench and 24 points on VBench-2.0 over Minimax-H3.
- **Caveat:** The reported evidence is on PhyGenBench and VBench-2.0; transfer to other video generators or real-world production use is not established by these evaluations.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Multimodal & vision-language

### 4. [CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse](https://arxiv.org/abs/2611.09891)
- **Abstract:** CPU-ARC converts LLM reasoning traces into reusable CPU-executable caches that apply prior solutions to new, related problem instances with less model inference.
- **Authors:** Peter Belcak, Greg Heinrich, Saurav Muralidharan, Shizhe Diao, Pavlo Molchanov
- **arXiv:** `2611.09891v1` (published 2026-11-06T18:58:50Z; categories: `cs.AI`)
- **Evidence for ranking:** Multiple third-party explainers discussed the proposal, including [AGI Hunt](https://agihunt.info/en/p/1a1c152762577cd97c8ef326acb), [AI Crunch](https://ai-crunch.com/articles/cpu-arc-agentic-reasoning-caching-llm-reasoning-reuse), and [Aivora](https://ai.kitmori.com/en/article/cpu-arc-agentic-reasoning-caching-for-on-cpu-reasoning-reuse). The reported invocation-cost reduction is a concrete systems result, though the paper is single-category and does not have independent experimental replication in the sources checked.
- **Claimed contribution:** The paper introduces reusable semantic-function caches built from reasoning traces; across eight math/science benchmarks, it reports invocation costs 16–291 times lower than the source model, with cache construction costing 12–84 times a source invocation.
- **Caveat:** The authors target repetitive tasks whose reasoning transfers across varied inputs; the up-front construction cost must be amortized, and novel or unmatched requests still need a full-model fallback.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Retrieval & knowledge

### 5. [Knowing When to Intervene: Causal Evaluation of AI Agents](https://arxiv.org/abs/2611.09792)
- **Abstract:** The authors develop a framework using randomized interventions within agent trajectories to estimate how review or steering policies affect final outcomes, with effects varying by action and state in three benchmarks.
- **Authors:** Ayush Sawarni, Wenqian Xing, Tijana Zrnic, Ramesh Johari, Vasilis Syrgkanis
- **arXiv:** `2611.09792v1` (published 2026-11-06T17:46:53Z; categories: `cs.AI`, `cs.LG`, `econ.EM`, `stat.ME`)
- **Evidence for ranking:** Cross-listed in AI, machine learning, econometrics, and methodology; independent discussion appeared at [Cybernoise](https://cybernoise.de/articles/2611.09792v1--when-does-reviewing-an-ai-agent-actually-help/) and [DAIR.AI Academy](https://academy.dair.ai/papers/knowing-when-to-intervene-causal-evaluation-of-ai-agents-2611.09792), with an [arXivSignals page](https://arxivsignals.io/papers/2611.09792). Category breadth and multiple technical summaries support inclusion, though the latter discovery pages are not citation measures.
- **Claimed contribution:** The paper uses sequential randomization, AIPW, and structural nested mean models to estimate intervention effects, and reports heterogeneous effects on tau-bench Retail, ToolSandbox, and ImpossibleBench.
- **Caveat:** The authors state that estimates for some target policies rely on correctly specified structural nested mean models; experiments cover relatively small models and established benchmarks, which may be saturated by frontier systems.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 6. [Computer-Use Agents Are Embodied Generalists](https://arxiv.org/abs/2611.09847)
- **Abstract:** The authors frame embodied tasks as software interaction and report that one computer-use agent design, without task-specific tuning, placed in four ECCV workshop competitions across navigation and visual tasks.
- **Authors:** Pranjal Aggarwal, Sean Welleck
- **arXiv:** `2611.09847v1` (published 2026-11-06T18:31:17Z; categories: `cs.LG`, `cs.RO`)
- **Evidence for ranking:** The paper bridges the cs.LG and cs.RO categories and reports first-, second-, third-, and sixth-place results across four ECCV workshop competitions; its [project page](https://pranjal2041.github.io/cua-embodied/) and [CMU lab page](https://cmu-l3.github.io/cua-week/) provide checkable context. Independent attention evidence was thinner than for the higher-ranked papers, so it is placed lower.
- **Claimed contribution:** The authors argue that computer-use agents can transfer visual grounding and exploration skills to embodied tasks through a shared screen-and-controls interface, and report results across four competition tracks.
- **Caveat:** The authors' text-action experiment covers a two-arm simulated setup; they note higher-degree-of-freedom robots may need more efficient action representations, and real-time control remains a separate challenge.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Robotics & control; Multimodal & vision-language

## Trending Research Themes

- Agentic systems are being optimized through execution structure, not just prompt changes: parallel teams allocate test-time compute across multiple teams, CPU-ARC reuses reasoning as executable cache entries, and AMP1 leaves a generalist model in the robot control loop. These are distinct mechanisms, not evidence for one universal agent architecture.
- Embodied and generative systems are converging on explicit interactive environments: AMP1 uses robot sensing and control tools, Computer-Use Agents expose embodied tasks through screen software, and Video-Coder adds code execution and 3D rendering as a video-generation scaffold. The papers differ in physical grounding and evaluation, so this is a recurring system-design motif rather than a demonstrated shared capability.
- Agent evaluation is becoming more conditional and intervention-aware. Parallel Agent Teams compares compute allocations under verifier-scored tasks, while Knowing When to Intervene estimates the impact of review at different agent states; the former concerns test-time scaling, the latter causal evaluation of deployment interventions.
- The announcement batch is category-heavy in cs.AI and cs.LG: the eight recent pages list 220 cs.AI, 213 cs.LG, 117 cs.CV, 78 cs.CL, 60 cs.RO, 22 stat.ML, 14 cs.MA, and 4 cs.NE entries. These page counts overlap through cross-listing; the six-paper selection spans AI, ML, robotics, and vision rather than reproducing the batch's category proportions.

## Open Problems and Research Directions

- **Author-stated open problem — latency and dynamic control:** AMP1 spends much time waiting for model reasoning and cannot change a motion already underway; its evaluations mainly use quasi-static scenes. **Research direction (synthesis):** measure success jointly with response latency on moving targets and slipping objects, and test asynchronous planning/feedback against real robot timing constraints. [On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)
- **Author-stated open problem — scaling evidence:** Parallel Agent Teams reports small run pools, sparse tests at large team sizes, and one agent harness. **Research direction (synthesis):** replicate across models, harnesses, tasks, and verifier quality with sufficient independent runs to estimate uncertainty and cost. [Test-Time Compute Scales Better with Parallel Agent Teams](https://arxiv.org/abs/2611.09798)
- **Author-stated open problem — cache coverage and amortization:** CPU-ARC relies on reusable reasoning patterns and pays a substantial one-time construction cost. **Research direction (synthesis):** evaluate cache-miss detection, correctness auditing, and break-even usage counts under workload drift and paraphrased or adversarial inputs, while preserving a reliable model fallback. [CPU-ARC](https://arxiv.org/abs/2611.09891)
- **Evidence-tied extension — video-scene fidelity:** Video-Coder reports improvements on PhyGenBench and VBench-2.0, but those benchmark results do not establish generalization across generators or out-of-distribution physical interactions. **Research direction (synthesis):** test held-out generators, longer interactions, and explicit scene-to-video consistency measures with human review. [Video-Coder](https://arxiv.org/abs/2611.09894)
- **Author-stated open problem — intervention estimation and opportunity selection:** Some causal policy estimates depend on parametric effect models; the authors call for harder, frontier-agent tasks and semantically defined intervention opportunities. **Research direction (synthesis):** validate history representations on held-out trajectories and experimentally test semantic intervention detectors before relying on them for review allocation. [Knowing When to Intervene](https://arxiv.org/abs/2611.09792)
- **Author-stated open problem — embodied generalization and action bandwidth:** Computer-Use Agents tests four competition tasks and a limited two-arm action setup; the paper notes that higher-DoF robots may need a more efficient action format. **Research direction (synthesis):** benchmark the same agent across higher-DoF robots and real-time conditions, varying action encoding and simulator fidelity. [Computer-Use Agents Are Embodied Generalists](https://arxiv.org/abs/2611.09847)

## Takeaway

The clearest shared signal is a move toward agent systems that structure their own compute, tools, memory, and environment feedback. The most striking results are still preprints on bounded benchmarks; replication, broader task coverage, and real-time deployment evidence remain the main uncertainties.

## Method and sources

- **Window:** daily, 2026-11-09 through 2026-11-09; the latest arXiv announcement batch shown as Mon, 9 Nov 2026, not a prior-batch fallback. Snapshot time: 2026-11-10T01:14:17Z. Each selected paper is a new v1 submission; the individual arXiv pages show 6 Nov submission timestamps, while the category recent pages place them in the 9 Nov announcement batch.
- **Scope and candidate pool:** configured categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`. All eight [arXiv recent pages](https://arxiv.org/list/cs.AI/recent?show=2000) were checked (the link is representative; the matching `/list/<category>/recent?show=2000` pages were checked for each category). They listed 728 category entries in total, deduplicated to 524 unique candidate IDs; cross-listing causes overlap. The six retained papers were verified on their individual arXiv abstract pages. The machine-readable category query used was `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`.
- **Ranking method:** rank is inferred from independent technical discussion/platform visibility, cross-list breadth, release/venue signals, and paper-specific evaluation evidence; recency was only a tie-breaker. No numeric trend score was constructed, and this report makes no claim about downloads, readership, or period citation gains. Semantic Scholar citation data were not available for this snapshot and were not used.
- **Paper reading:** arXiv abstracts were checked for all six selected papers. For the top three, arXiv HTML full text was read for the introduction and results/discussion or conclusion to ground the contribution and caveat fields.
- **Sources:** [arXiv recent categories](https://arxiv.org/list/cs.AI/recent), [arXiv API category query](https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:stat.ML+OR+cat:cs.CL+OR+cat:cs.CV+OR+cat:cs.RO+OR+cat:cs.NE+OR+cat:cs.MA&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200), [AMP1 project](https://apple-aiml-research.github.io/ml-amp/), [OpenReview — Parallel Agent Teams](https://openreview.net/forum?id=ZweFYN4Dy1), [DAIR.AI Academy — Parallel Agent Teams](https://academy.dair.ai/papers/test-time-compute-scales-better-with-parallel-agent-teams-2611.09798), [alphaXiv — Video-Coder](https://www.alphaxiv.org/abs/2611.09894), [AI Crunch — CPU-ARC](https://ai-crunch.com/articles/cpu-arc-agentic-reasoning-caching-llm-reasoning-reuse), [Cybernoise — Knowing When to Intervene](https://cybernoise.de/articles/2611.09792v1--when-does-reviewing-an-ai-agent-actually-help/), and [CMU lab — Computer-Use Agents](https://cmu-l3.github.io/cua-week/).