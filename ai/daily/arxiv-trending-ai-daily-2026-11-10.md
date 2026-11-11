# arXiv AI papers — Tuesday, 10 November 2026

Six notable papers from the latest announcement batch. The clearest common thread is grounding AI systems in observations and measurable work: tactile manipulation, visual tool use, scientific discovery, and multi-agent workflows. Spoken agenda: touch and vision first, then scientific and team-level agents, and finally a training-efficiency result. arXiv publishes no official trending chart; this ordering is inferred from observable community attention and independent discussion, while citation evidence is limited for papers announced today.

## Top papers (ranked)

### 1. [Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://arxiv.org/abs/2611.12806)
- **Abstract:** The authors present LingBot-Touch, a tactile foundation model that maps piezoresistive, magnetic, and visuotactile sensor data into transferable tokens and report improved dexterous manipulation in simulation and real-robot deployments.
- **Authors:** Bing Han, Yichuan Peng, Haoyu Dong, Yuanmeng Hu, Yongyi Jia, et al.
- **arXiv:** `2611.12806v1` (published 2026-11-09 18:12:00 UTC; categories: `cs.RO`)
- **Evidence for ranking:** 92 upvotes on the 10 Nov Hugging Face Daily Papers page, the largest checkable attention signal among the selected current-batch papers.
- **Claimed contribution:** The authors claim a unified, extensible tactile representation that can be plugged into diffusion policies and VLA policies; their abstract reports simulation and real-robot results across multiple hardware platforms.
- **Caveat:** The reported sensor coverage is the three named sensor families; transfer to other tactile sensor types is not established by the abstract.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Multimodal & vision-language; Robotics & control; Training & adaptation

### 2. [Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery](https://arxiv.org/abs/2611.12762)
- **Abstract:** Sage-Taiyi tracks evidence, assumptions, and unresolved questions to choose research targets and methods; the paper reports results on an ideation benchmark and five expert-guided scientific collaborations.
- **Authors:** Weida Wang, Benteng Chen, Yigeng Jiang, Shuchen Pu, Weiping Shen, et al.
- **arXiv:** `2611.12762v1` (published 2026-11-09 17:38:05 UTC; categories: `cs.AI`)
- **Evidence for ranking:** 52 upvotes on the 10 Nov Hugging Face Daily Papers page, the second-highest selected current-batch signal.
- **Claimed contribution:** The authors report first place on all eight Taiyi-Bench metrics (265 tasks drawn from 50 papers across ten disciplines), alongside two external ideation benchmarks and five expert-guided collaborations.
- **Caveat:** The authors say future work must refine the reasoning repertoire through accumulated research experience and test its reuse across domains; the applied evidence currently includes five collaborations.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 3. [Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](https://arxiv.org/abs/2611.12886)
- **Abstract:** Reframe combines evidence-aware policy optimization with observation-gated multi-teacher distillation so visual agents learn to use tool-returned observations and recover from deficient tool actions.
- **Authors:** Haozhi Yuan, Handong Li, Yifan Zhang, Qianshan Wei
- **arXiv:** `2611.12886v1` (published 2026-11-09 18:59:54 UTC; categories: `cs.CV`)
- **Evidence for ranking:** 37 upvotes on the 10 Nov Hugging Face Daily Papers page; its attention signal is below the first two papers but substantially above the other listed papers with page counts.
- **Claimed contribution:** The authors report gains over Mix-RL and vanilla MOPD across 14 image and video benchmarks, and ablations showing increased observation dependence and tool gain.
- **Caveat:** The reported comparison is benchmark-based and against the named methods; the abstract does not establish performance in live deployments or outside the evaluated visual tasks.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Agents & reasoning; Multimodal & vision-language; Training & adaptation

### 4. [WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.12856)
- **Abstract:** WorkflowArena evaluates model-authored delegation and executable workflow organization, alongside final deliverable quality, on 145 long-horizon tasks across eight professional domains.
- **Authors:** Zheng Jiang, Fang Niu, Bo Peng, Houde Qian, Wenyi Li, et al.
- **arXiv:** `2611.12856v1` (published 2026-11-09 18:45:28 UTC; categories: `cs.CL`, `cs.SE`)
- **Evidence for ranking:** The paper received several independent technical write-ups, including AICoder, ExplainX, and AILog coverage; its cross-list spans language and software engineering. No comparable public vote count was found for this paper.
- **Claimed contribution:** The authors formalize workflow orchestration as a measurable capability and report that no tested configuration leads across every domain; their controlled subset also suggests workflow choice can affect weaker executors.
- **Caveat:** The evidence is bounded to the benchmark's 145 tasks, eight domains, and nine tested model configurations; the abstract does not establish how the rankings transfer to other workflows or future model versions.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 5. [How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time](https://arxiv.org/abs/2611.12324)
- **Abstract:** The authors introduce MechEval and a 35M-parameter world model, WARC, to measure how quickly an agent learns game mechanics from interaction; tests use 69 mechanics across 20 ARC-AGI-3 games.
- **Authors:** Ku Onoda, Haruto Kawano, Shota Takashiro, Kohei Hayashi
- **arXiv:** `2611.12324v1` (published 2026-11-09 12:45:40 UTC; categories: `cs.LG`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** 4 upvotes on the 10 Nov Hugging Face Daily Papers page and cross-listing across three core AI categories.
- **Claimed contribution:** The authors report that WARC reaches at least 80% accuracy on changed cells for four in five held-out mechanics; the WARC-Agent raises the public-game explorer score from 0.15 to 0.46, while the hidden-game leaderboard score is 0.20.
- **Caveat:** Evaluation is specific to ARC-AGI-3's 20 games and 69 labeled mechanics; the reported hidden-game score is lower than the public-game result, so broader world-model generalization remains open.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Training & adaptation

### 6. [What the Loss Curve Misses: FP4 Pretraining Slows the Acquisition of Rare Facts](https://arxiv.org/abs/2611.12832)
- **Abstract:** Controlled experiments find that emulated NVFP4 pretraining can match BF16 validation loss while requiring more exposures to learn rare facts, with the authors' primary readout estimating an approximately 1.2× exposure cost.
- **Authors:** Chang Lu, Mengjiao Zhang
- **arXiv:** `2611.12832v1` (published 2026-11-09 18:30:41 UTC; categories: `cs.LG`)
- **Evidence for ranking:** The specific rare-fact result received independent technical discussion in ExplainX; the paper also addresses a practical gap in judging low-precision training by loss alone. No public vote or citation count is used for its placement.
- **Claimed contribution:** The authors argue that validation loss alone can hide slower acquisition of rare facts and propose measuring rare-fact recall when comparing low-precision training recipes.
- **Caveat:** The study uses transformers trained from scratch, emulated 4-bit matrix multiplications, and controlled biographies mixed with web text; production-scale training outcomes are not established.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Training & adaptation; Evaluation & benchmarks; Efficient inference & systems

## Trending Research Themes

- **Grounding action in observations:** LingBot-Touch connects heterogeneous tactile sensors to manipulation policies, while Reframe trains visual agents to use tool-returned evidence. WARC adds an interaction-based test of how agents learn unseen mechanics. These are related signals toward grounding behavior in sensed state, not evidence of one unified method.
- **Agents measured by the work they organize:** Sage-Taiyi explicitly monitors evidence and open questions to guide research; WorkflowArena evaluates delegation and workflow construction in addition to the final deliverable. The common methodological move is to assess intermediate process, not only final answers.
- **Evaluation beyond one aggregate score:** FP4 pretraining highlights rare-fact recall that validation loss can miss; Sage-Taiyi reports multiple ideation metrics; WorkflowArena uses hidden deliverable verifiers; WARC measures prediction of changed game cells and reports public and hidden-game performance separately.
- **Cross-domain embodiment and agent evaluation:** Tactile manipulation, visual tool use, and game-mechanics learning span robotics, vision, and machine learning. This is a category-spanning cluster in this batch, not evidence that the methods have already transferred between those fields.

## Open Problems and Research Directions

- **Open problem — tactile transfer:** The LingBot-Touch abstract covers three sensor families. **Research direction:** test held-out sensor physics and hardware, then report calibration effort and manipulation success under sensor shift. [2611.12806]
- **Open problem — scientific-ideation transfer:** Sage-Taiyi's authors explicitly identify reuse across domains and repertoire refinement as future work, while reporting five expert-guided collaborations. **Research direction:** run preregistered, resource-matched studies across more disciplines and labs, with blinded expert assessment and reproducible experimental follow-through. [2611.12762]
- **Open problem — tool and workflow robustness:** Reframe's gains are reported on 14 visual benchmarks; WorkflowArena's results are bounded to its task suite and tested model configurations. **Research direction:** evaluate on held-out tasks and changing tool interfaces, and separately measure successful recovery, cost, and quality of integrated outputs. [2611.12886; 2611.12856]
- **Open problem — benchmark-to-world-model generalization:** WARC is tested on ARC-AGI-3 mechanics and records a 0.20 score on hidden games. **Research direction:** vary game families and interaction budgets, and compare mechanic acquisition with and without test-time parameter updates. [2611.12324]
- **Open problem — low-precision training quality:** The FP4 study's controlled setup shows rare-fact acquisition can lag despite near-matched validation loss. **Research direction:** replicate the recall gap at larger scales and on independently sampled factual data, reporting both training cost and downstream retention. [2611.12832]

## Takeaway

Today's best-supported attention signals favor tactile and visual grounding, with scientific-reasoning and multi-agent workflow papers also attracting discussion. The methodological thread is to evaluate how an AI system uses observations and organizes intermediate work, not just its final output; how well those results survive larger, held-out, real-world tests is still uncertain.

## Method and sources

- **Window:** daily announcement batch for Tuesday, 2026-11-10; the snapshot was taken early on Wednesday, 2026-11-11, so this is the latest available prior batch. All six canonical arXiv abstract pages were reachable and matched their API titles. The selected papers' API first-submission timestamps are on 2026-11-09; none is a revision.
- **Snapshot:** 2026-11-11 01:10:06 UTC.
- **Scope/query:** core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; one broad arXiv API query sorted by submitted date. The latest submission date in the collected pool contained 430 unique records. Per-category counts including cross-lists: cs.LG 175, cs.AI 158, cs.CV 104, cs.RO 73, cs.CL 68, stat.ML 26, cs.MA 10, cs.NE 5.
- **Inference:** arXiv supplies no trending or readership ranking. Hugging Face Daily Papers counts are point-in-time upvotes, not arXiv-wide readership; independent technical write-ups were used where available. Recency was not treated as popularity. Semantic Scholar citation fields could not be retrieved in this snapshot, so no citation counts or citation-velocity claims were used. The two top-paper texts available in arXiv HTML (Sage-Taiyi and Reframe) were checked beyond their abstracts; for the other entries, the report stays within the arXiv abstract and metadata.
- **Sources:** [arXiv recent listings](https://arxiv.org/list/cs.AI/recent), [Hugging Face Daily Papers — 2026-11-10](https://huggingface.co/papers/date/2026-11-10), [AICoder on WorkflowArena](https://aicoder.com/news/news-20261110-einsia-workflowarena-multi-agent-workflow-orchestration-benchmark-145-tasks-claude-code-codex-opus-5-5-36-95), [ExplainX on WorkflowArena](https://www.explainx.ai/blog/workflowarena-multi-agent-orchestration-benchmark-einsia-2026), [AILog on WorkflowArena](https://www.aimodeling.com/en/news/slug/workflowarena-multi-agent-orchestration), and [ExplainX on FP4 pretraining](https://www.explainx.ai/blog/fp4-pretraining-rare-facts-nvfp4-loss-curve-2026). Each paper's canonical arXiv abstract is linked in its title.
