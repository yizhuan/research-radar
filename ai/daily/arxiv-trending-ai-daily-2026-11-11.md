# AI papers — arXiv announcement batch 11 Nov 2026: 8 selected papers

Dominant pattern: agent systems are being made more reliable and economical by changing what they learn from experience—compiling repeated behavior, checking memory against source evidence, and gating updates before commit. A second cluster structures scientific reasoning and connects biological models to experiments. Agenda: agent memory and workflows first, then scientific discovery and biology. This is an inferred ordering: arXiv has no official trending chart, and citation evidence is limited for papers announced within the last day.

Daily window: latest arXiv announcement batch, Wednesday 11 November 2026. The arXiv category “new” pages identify that batch; the selected papers were first submitted on 10 November UTC. Snapshot: 2026-11-12 17:05 UTC.

## Top papers (ranked)

### 1. [ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492)
- **Abstract:** ReTrace turns an SOP and logged agent runs into executable workflows where code selects each next step, reporting modest completion trade-offs alongside lower cost and much shorter latency on its tested procedures.
- **Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta et al.
- **arXiv:** `2611.14492v1` (published 2026-11-10 18:49:47 UTC; categories: `cs.AI`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Multiple independent technical commentaries discuss the latency/cost trade-off and where compilation is unsafe; the paper also reports 79 production procedures and two public benchmarks. This is a stronger attention signal than recency alone.
- **Claimed contribution:** The authors extract rules from agent reasoning and tool-call traces, then compile the rules into planner-free executable workflows; on τ²-Bench they report 1.3 seconds per task versus 170 seconds for the agent.
- **Caveat:** The authors say construction checks do not establish that recovered conditions are correct; results test new inputs to the same procedures, not transfer to new procedures, and changes to SOPs/tools may require rebuilding.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Agents & reasoning; Efficient inference & systems

### 2. [Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](https://arxiv.org/abs/2611.14514)
- **Abstract:** The paper replaces single-hypothesis testing with contrast sets of competing explanations, reporting that the framing resolves more questions from the same evidence and experiment budget across six datasets.
- **Authors:** Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
- **arXiv:** `2611.14514v1` (published 2026-11-10 18:58:43 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Accepted at NeurIPS 2026, cross-listed in three core AI categories, and discussed in independent technical coverage; its six-domain results and blinded expert study are checkable in the paper and project page.
- **Claimed contribution:** The authors report 67% more resolved questions than pointwise surprisal under the same experiment budget and expert agreement on 78% of resolved questions.
- **Caveat:** The authors limit experiments to tabular observational datasets and one GPT-4o-backed agent; conclusions are statistical rather than causal, and generated contrast sets can omit plausible alternatives.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 3. [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504)
- **Abstract:** The authors report that Bonbon, trained on paired protein–ligand sequences, supports zero-shot interaction predictions and prospective compound screening, with a sharp capability increase at the largest of six tested scales.
- **Authors:** Adi Mashiach
- **arXiv:** `2611.14504v1` (published 2026-11-10 18:53:01 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Listed as a NeurIPS 2026 main-track oral and covered independently by Astrobiology; the paper reports prospective wet-lab validation across nine targets. These are checkable venue and external-attention signals.
- **Claimed contribution:** The authors claim one frozen sequence-trained representation supports functional, residue-level, and bond-level interaction predictions, reporting a 61.5% dose-response hit rate for de novo compounds in prospective tests.
- **Caveat:** The authors say the reported capabilities are coarse-grained; explicit 3D-coordinate extraction and properties such as residence time and dissociation kinetics were not studied, and results use frozen representations.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Training & adaptation; Evaluation & benchmarks

### 4. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)
- **Abstract:** WikiTrace links each agent-memory lesson to its source summary and trajectory, letting an agent revisit evidence when a lesson is ambiguous, conflicting, or drawn from a failed task; the authors report gains across five agentic benchmarks.
- **Authors:** Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- **arXiv:** `2611.14320v1` (published 2026-11-10 16:46:59 UTC; categories: `cs.AI`, `cs.MA`)
- **Evidence for ranking:** The method is discussed by independent technical coverage, has a public implementation and project page, and reports results across five benchmarks/eight suites. Its core contribution is independently inspectable beyond an abstract-only claim.
- **Claimed contribution:** The authors report top performance on all evaluated suites, a 3.2-point average improvement over an insights-only baseline, and lower memory-induced regression when source evidence is available.
- **Caveat:** The authors note that source links let agents check but do not verify an insight; including all insights in the initial prompt makes memory grow, and scalable retrieval is left open.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Agents & reasoning; Retrieval & knowledge; Evaluation & benchmarks

### 5. [When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](https://arxiv.org/abs/2611.14326)
- **Abstract:** FGSE temporarily tests proposed memory updates as structured hypotheses on transfer, falsification, and regression probes before committing, refining, or rejecting them; the authors report results across web, app, tool-use, and long-term-memory benchmarks.
- **Authors:** Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng et al.
- **arXiv:** `2611.14326v1` (published 2026-11-10 16:52:25 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Listed as a NeurIPS 2026 poster, cross-listed in AI and machine learning, and reports concrete multi-environment safety and task-performance evaluations.
- **Claimed contribution:** The authors report reduced falsification failures, regression damage, and harmful committed updates while retaining benchmark performance, supporting verifier-gated rather than immediate memory writes.
- **Caveat:** The approach is framed for verifier-rich environments; extending it to settings where verifiers must be learned or approximated, and to multimodal agents, remains future work.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 6. [AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](https://arxiv.org/abs/2611.14515)
- **Abstract:** AutoScaffold uses a frozen teacher to diagnose student-model training experience and adapt task-class strategies and hard-example hints, reporting improved scaffold-free results over corresponding RL baselines in four domains.
- **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt et al.
- **arXiv:** `2611.14515v1` (published 2026-11-10 18:58:46 UTC; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** Cross-listed in machine learning and language, spans four task settings, and has multiple independent technical write-ups; its scaffold-removal evaluation makes the transfer claim checkable.
- **Claimed contribution:** The authors report gains over corresponding RL baselines on ALFWorld, search-based QA, math, and GPU-kernel generation after removing scaffolds at evaluation.
- **Caveat:** The authors identify reducing the cost of teacher interventions as future work; the reported gains are against corresponding baselines in the four evaluated domains, not all methods or settings.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Training & adaptation; Agents & reasoning

### 7. [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511)
- **Abstract:** Pyrite introduces a 1,500-pair protein–ligand pose-ranking benchmark and LLM agents that combine structured molecular representations, tool outputs, and learned features, reporting up to 74% accuracy.
- **Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
- **arXiv:** `2611.14511v1` (published 2026-11-10 18:56:32 UTC; categories: `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** Presented in the NeurIPS 2026 Agentic AI for Biological Discovery Workshop, with a NeurIPS listing, OpenReview record, and public benchmark/code. These provide checkable conference and artifact signals; the topic is narrower than higher-ranked general agent work.
- **Claimed contribution:** The authors report up to 74% pose-pair accuracy from LLM-guided feature discovery, exceeding observed expert performance, and report improvements from GRPO for open-weight models.
- **Caveat:** The authors say an accuracy gap remains; training is limited to pre-AF3 structures, while transfer to other pose generators and full drug-discovery ranking pipelines remains untested.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 8. [Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505)
- **Abstract:** Continual-ARC makes ARC tasks recur with fresh instances in a budgeted stream, comparing memory-based agent harnesses and weight-updating learners on memorization and generalization.
- **Authors:** Daniel Lenton
- **arXiv:** `2611.14505v1` (published 2026-11-10 18:55:01 UTC; categories: `cs.LG`)
- **Evidence for ranking:** A new benchmark protocol with released code and run records received independent technical discussion in multiple write-ups; the direct comparison of persistent harnesses and weight-based learning has broad relevance to agent-continuity claims.
- **Claimed contribution:** The authors report that harness persistence usually does not improve memorization without expert guidance, that tested harnesses did not improve unseen-task performance, and that weight-based learning did.
- **Caveat:** The authors note most runs use relatively small models on the easiest ARC-AGI-1 track; stronger models and ARC-AGI-2/3 remain future work.
- **Announcement type:** new submission, announcement-batch date 2026-11-11
- **Themes:** Evaluation & benchmarks; Training & adaptation

## Trending Research Themes

- **Agent experience is being made safer and more economical.** ReTrace compiles repeated procedures into code rather than replanning every step; WikiTrace preserves source trajectories so agents can check lessons; FGSE tests candidate updates before committing them. These approaches target different failure modes—runtime cost, unsupported memory, and harmful updates—and do not yet establish one general agent-memory solution.
- **Learning-time support is being separated from independent capability.** AutoScaffold adapts temporary hints during RL and evaluates after removing them, while Continual-ARC compares persistent harnesses with weight updates on recurring and unseen tasks. One is a training scaffold; the other is a benchmark of continual learning, so their results are complementary rather than directly comparable.
- **Scientific discovery is being represented more explicitly.** Contrastive Discovery makes competing explanations part of the search and evaluation unit; Pyrite asks LLM agents to interpret conflicting geometry and chemistry signals. Both shift attention from fluent proposals toward evidence handling, but each is evaluated in a bounded data setting.
- **Biological AI is moving toward sharper validation.** Bonbon reports sequence-trained representations and prospective wet-lab screening; Pyrite evaluates agents on pose ranking against crystallographic labels and human judgments. These are distinct evidence levels, and neither establishes broad clinical utility.
- **Category mix:** four of the eight selected papers are `cs.LG`-primary and four are `cs.AI`-primary; several are cross-listed. This reflects the selected shortlist, not field-wide popularity.

## Open Problems and Research Directions

- **Author-stated — ReTrace:** Construction checks do not prove recovered workflow conditions correct, and the evaluation does not test transfer to new procedures. Direction: audit decision rules against held-out branch/outcome traces, test transfer to new procedures, and measure degradation after SOP/tool changes (ReTrace).
- **Author-stated — WikiTrace:** Source links support checking but do not verify insights, and putting all insights in context creates a memory-scaling problem. Direction: compare selective retrieval with all-insights prompts, and measure whether agents can detect unsupported or out-of-scope lessons using source trajectories (WikiTrace).
- **Author-stated — Contrastive Discovery:** Experiments are observational and use one GPT-4o-backed agent; candidate contrast sets may omit alternatives. Direction: test in laboratory or longer-horizon interventions, add an abstention/“other” alternative, and compare LLM-elicited beliefs with independent statistical or expert adjudication (Contrastive Discovery).
- **Author-stated — Bonbon:** The paper leaves finer-grained interaction properties and explicit 3D-coordinate extraction unexplored. Direction: evaluate residence time, dissociation kinetics, and conformational changes on held-out protein families, then validate prospective predictions experimentally (Bonbon).
- **Author-stated — FGSE:** Verifier-rich environments are assumed; learned or approximate verifiers and multimodal settings remain future work. Direction: stress-test verifier errors and false commits as verification becomes noisy or learned (FGSE).
- **Author-stated — AutoScaffold:** Reducing teacher-intervention cost is left for future work. Direction: measure teacher calls/tokens against scaffold-free performance and compare adaptive revisions with fixed schedules at matched budgets (AutoScaffold).
- **Author-stated — Pyrite:** Transfer across pose generators and from pairwise accuracy to end-to-end drug-discovery ranking are untested. Direction: use generator-held-out splits and prospective downstream selection outcomes (Pyrite).
- **Author-stated — Continual-ARC:** Stronger models and harder ARC-AGI-2/3 tracks remain untested. Direction: replicate the same memory-versus-weights protocol on harder tracks while varying stream length and expert guidance (Continual-ARC).

## Takeaway

This batch's clearest pattern is agent lifecycle engineering: converting repeated decisions into faster workflows and making persistent lessons evidence-linked or falsification-gated. The strongest claims remain bounded by the specific procedures, verifiers, datasets, and models studied; replication across domains will determine which designs generalize.

## Method and sources

- Window: daily latest arXiv announcement batch dated 2026-11-11 (start 2026-11-11; end 2026-11-11). The latest category “new” pages identify the Wednesday, 11 November batch. All selected papers are new submissions first submitted on 2026-11-10 UTC, not revisions.
- Snapshot: 2026-11-12 17:05 UTC.
- Core corpus query: `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`, sorted by submitted date descending, first 200 records. The recent pool included entries in all eight configured categories; the shortlist is not an exhaustive field survey.
- Ranking: qualitative and inferred from independent technical discussion where found, checkable venue/workshop listings, category cross-list breadth, public artifacts, and reported evaluation. No numeric trend score was constructed. Semantic Scholar citation totals could not be verified for this snapshot, so citation counts and citation velocity were not used.
- arXiv category announcement pages: [cs.AI new](https://arxiv.org/list/cs.AI/new), [cs.LG new](https://arxiv.org/list/cs.LG/new), [cs.CL new](https://arxiv.org/list/cs.CL/new), [cs.CV new](https://arxiv.org/list/cs.CV/new), [cs.RO new](https://arxiv.org/list/cs.RO/new), [cs.NE new](https://arxiv.org/list/cs.NE/new), [cs.MA new](https://arxiv.org/list/cs.MA/new), [stat.ML new](https://arxiv.org/list/stat.ML/new).
- Selected arXiv abstract pages: [ReTrace](https://arxiv.org/abs/2611.14492), [WikiTrace](https://arxiv.org/abs/2611.14320), [Contrastive Discovery](https://arxiv.org/abs/2611.14514), [Bonbon](https://arxiv.org/abs/2611.14504), [FGSE](https://arxiv.org/abs/2611.14326), [AutoScaffold](https://arxiv.org/abs/2611.14515), [Pyrite](https://arxiv.org/abs/2611.14511), [Continual-ARC](https://arxiv.org/abs/2611.14505). The top three papers' introductions, results, and limitations/conclusions were checked in their PDFs.
- Corroborating sources: [ReTrace commentary](https://learnagentic.substack.com/p/your-agent-took-170-seconds-its-compiled), [ReTrace coverage](https://news.bitwarelabs.com/posts/retrace-distilling-tool-using-agents-planner-free-workflows/), [WikiTrace project page](https://yukyeongleee.github.io/wikitrace/), [WikiTrace coverage](https://www.tokenpost.com/news/technology/54827), [Contrastive Discovery project page](https://codiscovery.ai/contrastive-discovery/), [independent Contrastive Discovery commentary](https://alcybr.com/blog/contrastive-discovery-restructures-how-llm-agents-test-hypotheses), [NeurIPS Bonbon oral](https://neurips.cc/virtual/2026/oral/149425), [Astrobiology coverage of Bonbon](https://astrobiology.com/2026/11/12/emergent-biological-capabilities-in-a-foundation-model-for-molecular-interactions/), [NeurIPS FGSE poster](https://neurips.cc/virtual/2026/poster/154558), [AutoScaffold coverage](https://news.bitwarelabs.com/posts/autoscaffold-ai-guided-scaffolding-reinforcement-learning/), [NeurIPS Pyrite listing](https://neurips.cc/virtual/2026/172672), [Pyrite OpenReview](https://openreview.net/forum?id=1D1zTveOCw), [Continual-ARC technical discussion](https://subagentic.ai/posts/continual-arc-harness-memory/).
