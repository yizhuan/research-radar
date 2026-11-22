# AI on arXiv — week ending 2026-11-19: 10 papers

The strongest attention pattern this week is agentic systems: self-editing models, long-horizon interactive agents, and benchmarks that test whether agents finish verifiable work. Also on the agenda: one-pass image generation and AI infrastructure. This is an inferred ranking, not an official arXiv trending chart; citation evidence for these recent papers is limited.

Window: 2026-11-12 19:00 UTC to 2026-11-19 19:00 UTC. The weekly pool corresponds to the 2026-11-19 announcement batch (announced 2026-11-20 01:00 UTC). Snapshot: 2026-11-22 02:11:04 UTC.

## Top papers (ranked)

### 1. [Language Models Can Rewrite Their Own Weights](https://arxiv.org/abs/2611.21885)
- **Abstract:** The authors report that a 27B model can use its own reasoning to edit its weights without gradients or retraining, improving held-out accuracy and repairing a damaged copy.
- **Authors:** Jiajun Fan; Neil He; Changyi Yang; Andy Mao; Xi Zhu; et al.
- **arXiv:** `2611.21885v2` (published 2026-11-16T20:55:08Z; categories: `cs.AI`)
- **Evidence for ranking:** Collector score 21.128; Hacker News 480 points/141 comments (score components 9.264/4.956) and Hugging Face Papers 9 upvotes (component 6.908). These are the highest combined attention signals in this pool; Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors describe “self-rewriting”: a model edits its own weights using forward-pass access and tests, reporting a 6.6-point held-out gain for a 27B model.
- **Caveat:** In the reported model family, the 2B model made no edit and the 4B and 9B models damaged themselves; the positive results are concentrated at 27B, not evidence of general self-improvement across models.
- **Announcement type:** new submission (v2; updated 2026-11-18), announcement-batch 2026-11-19
- **Themes:** Training & adaptation; Agents & reasoning

### 2. [Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://arxiv.org/abs/2611.18397)
- **Abstract:** Gamer combines perception, memory, reasoning, long-horizon reinforcement learning, and low-latency serving to act across 2D interfaces and 3D game environments.
- **Authors:** Run Luo; Kuan Zhang; Qi Deng; Yukun Chen; Zhihao Yang; et al.
- **arXiv:** `2611.18397v3` (published 2026-11-13T16:39:30Z; categories: `cs.CL`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Collector score 19.032; Hugging Face Papers 147 upvotes (component 14.992), GitHub 1,188 stars (component 3.540), and two cross-lists (component 0.500). Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors combine interaction-trajectory pretraining, sparse-thinking tuning, multi-turn RL, and cloud-edge inference; they report generalization across selected 3D games and conventional 2D benchmarks.
- **Caveat:** The authors say evaluation covers selected environments and tasks, serving was tested on evaluated GPU platforms, and deeper reasoning may remain a bottleneck.
- **Announcement type:** new submission (v3; updated 2026-11-18), announcement-batch 2026-11-19
- **Themes:** Agents & reasoning; Multimodal & vision-language; Efficient inference & systems

### 3. [Jeveration: System One Models Now Generate](https://arxiv.org/abs/2611.24738)
- **Abstract:** Jeveration uses parallel typed decisions from a frozen vision-language model to generate images, image-conditioned outputs, and dense predictions in one forward pass.
- **Authors:** Yuhe Liu; Qi Li; Shihua Zhang; Xinchao Wang
- **arXiv:** `2611.24738v1` (published 2026-11-18T16:56:59Z; categories: `cs.CV`)
- **Evidence for ranking:** Collector score 17.299; Hugging Face Papers 148 upvotes (component 15.012) and GitHub 96 stars (component 2.287). Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors coordinate parallel image-code predictions with a shared random state and report 512×512 generation in 78 ms, up to 122× faster than the unified models they compare against, with competitive image quality.
- **Caveat:** The reported latency is for 512×512 generation on one H200; “competitive” quality is limited to the paper’s reported comparisons and tasks.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Multimodal & vision-language; Efficient inference & systems

### 4. [InclusionMed: Benchmarking AI for Inclusive Healthcare](https://arxiv.org/abs/2611.21218)
- **Abstract:** InclusionMed organizes medical-AI evaluation by healthcare role and capability and reports that model rankings and costs vary across those dimensions.
- **Authors:** The InclusionMed Collaboration
- **arXiv:** `2611.21218v1` (published 2026-11-16T15:08:25Z; categories: `cs.AI`)
- **Evidence for ranking:** Collector score 16.114; Hugging Face Papers 104 upvotes (component 13.962) and GitHub 73 stars (component 2.152). Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors audited 388 candidate benchmarks, selected four public benchmarks and added a private diagnostic benchmark, then evaluated frontier models using an aggregate index.
- **Caveat:** The first release covers only three of nine role-capability cells, and its diagnostic benchmark is private, limiting coverage and direct reproducibility.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Evaluation & benchmarks

### 5. [AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs](https://arxiv.org/abs/2611.17621)
- **Abstract:** AscendGYM benchmarks model- and harness-driven optimization of existing Ascend NPU kernels using 48 kernels with workload-derived tensor shapes and data types.
- **Authors:** AI Training Platform Team; Bingwei Zhang; Jing Li; Amir Abdullin; Sihang Chen; et al.
- **arXiv:** `2611.17621v1` (published 2026-11-13T00:45:36Z; categories: `cs.AI`, `cs.DC`, `cs.LG`)
- **Evidence for ranking:** Collector score 15.940; Hugging Face Papers 94 upvotes (component 13.662), GitHub 34 stars (component 1.778), and two cross-lists (component 0.500). Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors provide an execution environment and a Speedup-Token Score that weighs speed gains against token cost for kernel-optimization agents.
- **Caveat:** This is an initial 48-kernel suite for Ascend NPUs; results do not by themselves establish transfer to other accelerator families or workloads.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Evaluation & benchmarks; Efficient inference & systems; Agents & reasoning

### 6. [Sage S2.1 Flash Technical Report](https://arxiv.org/abs/2611.21072)
- **Abstract:** Sage S2.1 Flash is a 320B-parameter mixture-of-experts model with scientific-data encoders and tool-using agents, evaluated across 33 benchmarks in seven domains.
- **Authors:** Kun Cai; Haodong Chen; Guangran Cheng; Qingxiu Cheng; Xu Dai; et al.
- **arXiv:** `2611.21072v2` (published 2026-11-16T13:23:49Z; categories: `cs.AI`)
- **Evidence for ranking:** Collector score 15.590; Hugging Face Papers 98 upvotes (component 13.785) and GitHub 36 stars (component 1.805). Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors report multimodal scientific perception and verifiable tool-use workflows, with leading results on several named benchmarks in comparisons against five baselines.
- **Caveat:** The performance claims are bounded to the report’s 33 benchmarks, seven domains, and stated five-baseline comparison; they are not an independent replication.
- **Announcement type:** new submission (v2; updated 2026-11-17), announcement-batch 2026-11-19
- **Themes:** Agents & reasoning; Multimodal & vision-language; Evaluation & benchmarks

### 7. [Envisioning Agentic Robotics: A New Era of Robotic Systems](https://arxiv.org/abs/2611.18359)
- **Abstract:** This perspective frames agentic robotics as foundation models operating through a closed-loop embodied harness and proposes an evaluation framework and research roadmap.
- **Authors:** Grid Robotics; Qingfeng Lan; Duo Li; Siyao Li; Yiheng Lyu; et al.
- **arXiv:** `2611.18359v1` (published 2026-11-13T16:07:26Z; categories: `cs.RO`, `cs.AI`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** Collector score 15.510; Hugging Face Papers 136 upvotes (component 14.760) and three cross-lists (component 0.750). Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors define “Embodied System 2” as a foundation model plus embodied harness and outline measures for model capability and closed-loop system performance.
- **Caveat:** This is a vision and framework proposal; the authors themselves note that the field lacks a shared definition and reliable evaluation framework, rather than validating a deployed robotic system.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Robotics & control; Agents & reasoning; Evaluation & benchmarks

### 8. [Self-Improvement Memory Enables Continual Recursive Self-Improvement](https://arxiv.org/abs/2611.18856)
- **Abstract:** Self-Improvement Memory records the rationale, outcomes, and context of harness edits so an optimizer can continue improving across compatible models or benchmarks.
- **Authors:** Xin Yu; Fei Xia; Jiaqi Pan; Youbao Tang; Chengzhi Liu; et al.
- **arXiv:** `2611.18856v1` (published 2026-11-13T19:08:56Z; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** Collector score 15.388; Hugging Face Papers 38 upvotes (component 10.991), Hacker News 9 points/1 comment (components 3.454/0.693), and one cross-list (component 0.250). Semantic Scholar listed 0 citations.
- **Claimed contribution:** Across four domains, the authors report better final scores than harness-only and root-cause-only continuation; ten coding source runs show a 2.36-point average gain over harness-only continuation.
- **Caveat:** The reported evidence is from compatible cross-dataset/model settings and a small ten-run coding comparison; the abstract does not establish broad gains for arbitrary tasks or optimizers.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Agents & reasoning; Training & adaptation

### 9. [TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks](https://arxiv.org/abs/2611.22115)
- **Abstract:** The report describes Xing 4 model architecture, training infrastructure, and agent post-training on Ascend chips, including a 285B-parameter model trained on 8,192 Ascend 910C cards.
- **Authors:** Xingchen AGI Lab; Baotian Hu; Bingkai Yang; Boyang Wang; Changzai Pan; et al.
- **arXiv:** `2611.22115v1` (published 2026-11-17T02:58:31Z; categories: `cs.AI`)
- **Evidence for ranking:** Collector score 15.372; Hugging Face Papers 167 upvotes (the entire score component). Semantic Scholar listed 0 citations.
- **Claimed contribution:** The authors describe architecture and training-stack choices for the Xing 4 series and introduce TeleGym, an execution and evaluation platform for agentic post-training.
- **Caveat:** The report’s systems results are specific to its Ascend/MindSpore setup; the cited 285B run demonstrates that stack, not accelerator-agnostic performance.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Efficient inference & systems; Training & adaptation; Agents & reasoning

### 10. [SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations](https://arxiv.org/abs/2611.20218)
- **Abstract:** SWE-CoWork tests coding agents on repository assignments where requirements are distributed across simulated colleagues and workplace records, with private executable tests for delivery.
- **Authors:** Xinping Lei; Minghao Liu; Ruijie Zhu; Xiaohui Hu; Xingqiao Li; et al.
- **arXiv:** `2611.20218v1` (published 2026-11-15T19:39:01Z; categories: `cs.SE`, `cs.AI`)
- **Evidence for ranking:** Collector score 15.251; Hugging Face Papers 53 upvotes (component 11.967), Hacker News 2 points/0 comments (components 1.648/0), GitHub 15 stars (component 1.386), and one cross-list (component 0.250). Semantic Scholar listed 0 citations.
- **Claimed contribution:** On 101 assignments across 101 repositories, the authors find a large gap between partial implementation and complete task delivery; the two leading models pass about 63% of fail-to-pass tests but complete fewer than 8% of assignments.
- **Caveat:** Results use a simulated organization with 26 colleagues and benchmark-specific assignments/tests; performance in live organizations is not measured directly.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Evaluation & benchmarks; Agents & reasoning

## Trending Research Themes

- **Agents are being tested as systems, not only as chat models.** Gamer couples long-horizon perception, memory, RL, and serving; Sage S2.1 Flash uses verifiable tool workflows; SWE-CoWork measures end-to-end completion. The recurring pattern is environment interaction and execution checks, not just answer quality.
- **Self-improvement is appearing at two different layers.** Language Models Can Rewrite Their Own Weights edits model parameters, while Self-Improvement Memory persists lessons for a harness optimizer. Both report iterative improvement, but the former is a single-family 27B result and the latter is benchmark-scoped; neither establishes open-ended recursive improvement.
- **Efficiency is shifting toward fewer sequential steps and specialized systems.** Jeveration reports single-pass image outputs, while AscendGYM and the Xing4 report emphasize workload-aware kernel optimization and accelerator-specific training infrastructure. These are distinct approaches, not evidence of one broadly validated efficiency breakthrough.
- **Evaluation coverage is itself a research object.** InclusionMed exposes missing role-capability coverage in medical AI, AscendGYM builds a practical kernel-optimization testbed, and SWE-CoWork reveals the difference between partial coding progress and completed organizational work.
- **Category mix:** The ten highest-scoring candidates include five primary `cs.AI` papers and one each from `cs.CL`, `cs.CV`, `cs.RO`, `cs.LG`, and `cs.SE`; the `cs.SE` paper is cross-listed into `cs.AI`, and several others are cross-listed. This is the shortlist’s distribution, not a claim about the full arXiv corpus.

## Open Problems and Research Directions

- **Can self-editing generalize safely beyond one model family and task?** The self-rewriting paper reports failure at 2B–9B and success at 27B. Follow-up work could test multiple architectures and tasks with preregistered held-out suites, edit rollback, and robustness checks (Language Models Can Rewrite Their Own Weights).
- **How should real-time agents trade reactive speed against deeper planning and coverage?** Gamer explicitly identifies reasoning bottlenecks and selected-environment evaluation. Test hierarchical fast/slow policies across broader game and embodied tasks, including lower-cost hardware and task shifts (Gamer; Envisioning Agentic Robotics).
- **Which healthcare role-capability cells are missing, and can they be evaluated reproducibly?** InclusionMed’s first Atlas release covers three of nine cells and includes a private diagnostic benchmark. Expand public coverage and report role-specific accuracy, cost, and subgroup reliability (InclusionMed).
- **Do agent and kernel gains transfer across hardware and workload distributions?** AscendGYM’s initial suite is 48 Ascend kernels, while Xing4 reports an Ascend-specific training stack. Cross-device replications and held-out real workload suites would test portability rather than within-stack optimization (AscendGYM; TeleChat to Xing4).
- **What prevents partial coding progress from becoming verified delivery?** SWE-CoWork reports fewer than 8% complete assignments despite roughly 63% fail-to-pass test success for leading models. Trace requirement acquisition, implementation, verification, and handoff separately in live-team pilots as well as controlled benchmarks (SWE-CoWork).

## Takeaway

This week’s attention clusters around agents that act, persist, and verify, plus infrastructure and benchmarks intended to make those abilities measurable. The strongest signals are attention and code interest rather than citations; reported gains remain bounded by small numbers of model families, selected environments, and benchmark-specific evaluations.

## Method and sources

- **Window:** weekly, 2026-11-12 19:00 UTC through 2026-11-19 19:00 UTC; selected announcement-batch date 2026-11-19 (announced 2026-11-20 01:00 UTC). Snapshot time: 2026-11-22 02:11:04 UTC.
- **Categories queried:** `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`. The signal pool contains 3,311 candidates; 247 had external attention. Top ten are ranked by the collector’s log1p-damped weighted signal score, not arXiv API ordering. The score combines available Hugging Face Papers upvotes, Hacker News points/comments, Semantic Scholar citations/influential citations, GitHub stars, and arXiv cross-list breadth; entry-level evidence above names the specific values and score components used.
- **Primary ranking data:** `/home/yizhuan/.research/ai/weekly/arxiv-trending-ai-weekly-2026-11-19.signals.json`. Its arXiv, Hugging Face, Hacker News, arXiv lookup, and Semantic Scholar source statuses were all `ok`; no collection source was unavailable. A paper with no per-paper Hacker News entry had no indexed story in this pool, not a reported service error. Semantic Scholar returned zero citations for the ten selected papers, so citation momentum did not distinguish this shortlist. A zero attention score elsewhere in the pool would not mean a paper is unimportant.
- **Verification:** Each selected abstract and author list was checked on its canonical arXiv abstract page linked above. The introductions/results and limitations/future-work sections of the top three were also checked in arXiv HTML. Their current versions and first-submission timestamps, categories, and attention values were cross-checked against the signal file. All selected papers were first submitted within the weekly window; versions v2/v3 also have an in-window revision date, identified in their entries.
- **Corroborating attention pages:** [Hugging Face Papers for Language Models Can Rewrite Their Own Weights](https://huggingface.co/papers/2611.21885); [Hacker News discussion](https://news.ycombinator.com/item?id=50577265); [Hugging Face Papers for Gamer](https://huggingface.co/papers/2611.18397); [Hugging Face Papers for Jeveration](https://huggingface.co/papers/2611.24738). Additional per-paper Hugging Face and Hacker News links are available in the signal file.
