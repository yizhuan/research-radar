# arXiv Trending AI — latest available daily batch

The latest available arXiv announcement batch is dated 2026-09-17; 2026-09-19 is a Saturday with no newer daily batch in the queried feed. arXiv has no official trending chart, so this is an inferred ranking rather than a most-read or most-downloaded list. The strongest supported pattern is a shift from raw capability demos toward evaluation, reliability, and deployable control: papers probe whether agents are safe, whether model confidence and group consensus are trustworthy, and whether robotics and generation systems retain useful structure under real constraints.

## Top papers (ranked)

### 1. [Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation](https://arxiv.org/abs/2609.20822)
- **Abstract:** The paper evaluates coding agents that write robot controllers under obstacle-avoidance constraints and introduces SafeHarness, combining obstacle-aware route planning with obstacle-aware contact execution.
- **Authors:** Bingxin Xu; Yuzhang Shang; Zhen Dong; Emilio Ferrara
- **arXiv:** `2609.20822v1` (published 2026-09-17 17:59 UTC; categories: `cs.RO`, `cs.AI`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** Four-way cross-list breadth; unusually concrete safety failure analysis; reported gains to 71.9% task success and 87.5% collision avoidance; independent search results included two same-day research-digest entries and a technical discussion. Semantic Scholar citation fields were unavailable because its API returned HTTP 429, so no citation momentum is claimed.
- **Claimed contribution:** The authors report that SafeHarness raises task success by 6.5 percentage points and collision avoidance by 27.0 points over prior state of the art, while diagnosing route prioritization and contact execution as distinct failure points.
- **Caveat:** This is a new preprint, and the abstract does not establish how performance transfers beyond the tested manipulation tasks or obstacle configurations.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Safety & alignment; Robotics & control; Agents & reasoning

### 2. [Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision](https://arxiv.org/abs/2609.20820)
- **Abstract:** Workspace Models distill train-time VLM judgments about task-relevant history into a lightweight workspace token that replaces expensive VLM reasoning at deployment.
- **Authors:** Nitish Dashora; Douglas Chen; Idan Shenfeld; John Marangola; Pulkit Agrawal; Max Simchowitz
- **arXiv:** `2609.20820v1` (published 2026-09-17 17:59 UTC; categories: `cs.RO`, `cs.AI`)
- **Evidence for ranking:** Cross-listing into robotics and AI; hardware plus simulation evaluation; same-day search visibility with an arXiv result and digest coverage. Semantic Scholar citation fields were unavailable because its API returned HTTP 429; no citation momentum is claimed.
- **Claimed contribution:** The authors report that workspace tokens solve memory-intensive tasks without VLM reasoning in the loop and can improve policy performance while reducing deployment cost.
- **Caveat:** The abstract does not quantify the hardware-task range or memory failure modes, so the generality of the reported improvement remains uncertain.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Robotics & control; Efficient inference & systems; Multimodal & vision-language

### 3. [Can 4D Foundation Models Remember?](https://arxiv.org/abs/2609.20819)
- **Abstract:** PersistBench uses omniscient 360-degree video ground truth to measure object permanence, motion continuity, and appearance preservation in 4D foundation models.
- **Authors:** Guangzhao He; Hadar Averbuch-Elor; Wei-Chiu Ma
- **arXiv:** `2609.20819v1` (published 2026-09-17 17:59 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Introduces a reusable benchmark addressing a stated blind spot in current 4D evaluation; the paper is among the first entries in the latest batch and is directly relevant to visual-memory claims. Semantic Scholar citation fields were unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors report that current models maintain only short-term consistency and degrade markedly after objects leave the field of view.
- **Caveat:** The abstract reports evaluations across diverse categories but does not specify model coverage or whether PersistBench predicts downstream navigation performance.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language

### 4. [Paint-Anything: Unified Any-Color Control for Image Generation and Editing](https://arxiv.org/abs/2609.20816)
- **Abstract:** Paint-Anything trains a shared hex-prompt interface for object-level 24-bit color control in text-to-image generation and editing, with Paint-500K and the ACBench benchmark.
- **Authors:** Ji Xie; Dewei Zhou; Xinyu Huang; Zhennan Chen; Xun Wang
- **arXiv:** `2609.20816v1` (published 2026-09-17 17:59 UTC; categories: `cs.CV`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Three-way cross-listing; a new dataset and benchmark; reported 85.3% and 28.3% relative gains on ACBench-T2I and ACBench-Edit; multiple independent search results and reviews appeared for the title. Semantic Scholar citation fields were unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors attribute improved hex-color fidelity to object-level supervision plus high-noise pure-color anchors, while retaining natural-image training at low noise.
- **Caveat:** The headline improvements are reported on the authors' benchmark and a FLUX.2-4B base; external replication and perceptual quality trade-offs are not established by the abstract.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Multimodal & vision-language; Data & synthetic data; Training & adaptation

### 5. [An Analysis of Training-Free Self-Reported Confidence in Language Models](https://arxiv.org/abs/2609.20541)
- **Abstract:** On 100 TriviaQA questions and two model families, the study compares verbalized confidence, post-hoc P(True), and three-sample agreement as training-free correctness signals.
- **Authors:** Lukas Meyer; Sofia Rossi; Wei Chen; Thomas Laurent; Yiming Li
- **arXiv:** `2609.20541v1` (published 2026-09-17 15:10 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Directly tests a widely used reliability heuristic; reports AUROC 0.956 and 0.937 for verbalized confidence, plus same-day search results and an HTML version surfaced independently. Semantic Scholar citation fields were unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors report that verbalized confidence outperforms the tested alternatives in this setup, while self-consistency can amplify shared misconceptions and confidence is prompt-sensitive.
- **Caveat:** The sample is only 100 TriviaQA questions plus an exploratory 100-claim biography audit, so the estimates should not be treated as general calibration guarantees.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Evaluation & benchmarks; Safety & alignment

### 6. [Language-model groups overstate consensus when replaying human deliberation on a reasoning task](https://arxiv.org/abs/2609.20543)
- **Abstract:** Replaying 100 held-out human Wason groups with matched LLM groups, the study finds that model groups appear substantially more consensual and that consensus does not track collective accuracy.
- **Authors:** Tengfei Shao
- **arXiv:** `2609.20543v1` (published 2026-09-17 15:11 UTC; categories: `cs.AI`, `cs.CL`, `cs.CY`, `cs.MA`)
- **Evidence for ranking:** Four-way cross-listing; explicit matched human/agent comparison; same-day search results and independent research-digest coverage. Semantic Scholar citation fields were unavailable because its API returned HTTP 429.
- **Claimed contribution:** The paper reports 34.0–44.4 percentage-point consensus gaps under participation and submission controls, with near-unanimous but often incorrect reasoning-mode agreement.
- **Caveat:** The evidence comes from one reasoning task and replay design; it does not establish that all simulated groups overstate consensus.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Safety & alignment

### 7. [UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.20089)
- **Abstract:** UnifiedPlayers jointly trains planning, execution, and evaluation players so tool-using agents can generate trajectories and adaptive executable verifiers under GRPO.
- **Authors:** Wenjie Liao; Liangjie Zhao; Zehong Cao
- **arXiv:** `2609.20089v1` (published 2026-09-17 11:49 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Addresses the coupled data-feedback problem in self-evolving agents; reports results on two backbones and twelve reasoning benchmarks, including 84.2% adversarial detection accuracy. Semantic Scholar citation fields were unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors report gains of at least 3.5% on mathematical reasoning and 3.9% on general reasoning over the strongest prior baseline.
- **Caveat:** The abstract does not identify all baselines or disclose how verifier quality changes under distribution shift beyond the reported benchmarks.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Training & adaptation

### 8. [OmniMimic: Dynamics-completed Motion Augmentation for Multi-style Omnidirectional Quadruped Locomotion](https://arxiv.org/abs/2609.20566)
- **Abstract:** OmniMimic expands directionally limited animal demonstrations into multi-gait quadruped policies using dynamics completion, temporal reversal, reflection, progressive command expansion, and gait-specialized residual experts.
- **Authors:** Sheng Wu; Guoqiang Zhao; Zhe Yang; Fei Teng; Zhikun Zhou; Yanlin Yang; Zheng Fang; Hong Zheng; Yaonan Wang; Kailun Yang
- **arXiv:** `2609.20566v1` (published 2026-09-17 15:28 UTC; categories: `cs.RO`, `cs.CV`, `eess.IV`)
- **Evidence for ranking:** Cross-listing across robotics and vision; reports large reductions in foot-position and velocity-tracking error against a matched baseline; project page is supplied in the abstract. Semantic Scholar citation fields were unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors report 12.9% lower mean foot-position RMSE at forward/backward reference velocities and 63.1% lower velocity-tracking RMSE on a uniform Cartesian command grid.
- **Caveat:** The reported comparisons are simulation-based in the abstract; real-robot transfer and robustness to demonstration mismatch remain open.
- **Announcement type:** new submission, 2026-09-17 announcement batch
- **Themes:** Robotics & control; Data & synthetic data; Training & adaptation

## Trending Research Themes

- **Reliability is becoming an object of measurement, not just a prompt property.** Confidence elicitation, simulated-group consensus, and claim-safe evaluation all show that reproducibility or agreement can coexist with wrong conclusions (2609.20541, 2609.20543, 2609.20538).
- **Agent safety is moving into the execution harness.** SafeHarness makes route verification, replanning, and contact constraints explicit rather than assuming a language model's reasoning trace will prioritize them (2609.20822).
- **Long-horizon memory is being compressed into task-specific representations and benchmarks.** Workspace tokens target cheap deployment memory, while PersistBench tests whether visual memory survives occlusion and time (2609.20820, 2609.20819).
- **Data and evaluation interfaces are active research contributions.** Paint-500K/ACBench and PersistBench turn underspecified capabilities—color fidelity and 4D memory—into measurable tasks (2609.20816, 2609.20819).
- **Theory is catching up with efficient generation.** The diffusion-language-model paper gives provable parallelism comparisons, while UnifiedPlayers explores adaptive evaluation for practical tool-integrated reasoning (2609.20539, 2609.20089).

## Open Problems and Research Directions

- **Open problem — safety constraints still need reliable grounding at every execution phase.** SafeHarness identifies route and contact failures separately (2609.20822). A useful next experiment is a held-out manipulation suite with moving obstacles, perception noise, recovery after collision-risk detection, and independently audited safety metrics.
- **Open problem — memory benchmarks and deployment memory are not yet linked.** PersistBench measures object permanence while Workspace Models optimize lightweight policy memory (2609.20819, 2609.20820). A follow-up should test whether PersistBench scores predict task success under long-horizon manipulation and navigation, rather than only reconstruction consistency.
- **Open problem — model agreement and confidence can be systematically misleading.** Shared misconceptions appear in both self-consistency and simulated consensus studies (2609.20541, 2609.20543). Research should evaluate confidence and group protocols on adversarial, out-of-distribution, and expert-verified datasets with abstention costs.
- **Open problem — claim validity depends on reference support and drift handling.** Refuse, Decompose, Refresh argues that a detector must abstain when its reference stream is unsupported or stale (2609.20538). A concrete direction is preregistered cross-domain replication with frozen references, drift-triggered refresh, and separate reporting of execution, false admission, and structural hypotheses.
- **Open problem — benchmark gains may be interface-specific.** Paint-Anything's gains are measured with ACBench and OmniMimic's with a command-grid protocol (2609.20816, 2609.20566). Cross-benchmark evaluations and human or hardware evaluations would test whether the gains survive changes in color distributions, model families, terrain, and command policies.

## Takeaway

The batch's clearest signal is methodological: AI papers are increasingly testing whether systems remain trustworthy when the environment, evaluator, memory state, or user constraint changes. The most promising work pairs a capability with an explicit harness or benchmark, but the evidence is still preprint-level, often narrow in task coverage, and too new for citation-based popularity claims.

## Method and sources

- **Window:** daily; latest available announcement batch, 2026-09-17 through 2026-09-17 UTC. Snapshot: 2026-09-19 15:10 UTC.
- **Corpus:** arXiv categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`, queried through the arXiv export API and deduplicated by versionless ID.
- **Ranking:** inferred from recency, cross-list breadth, benchmark or hardware evidence, concrete reported results, and corroborating independent search visibility. Semantic Scholar was queried but returned HTTP 429, so citation and influential-citation counts are explicitly unavailable rather than estimated.
- **Primary sources:** each linked arXiv abstract page above; arXiv API query updated 2026-09-19 15:10 UTC.
- **Corroborating sources:** search results for SafeHarness, Paint-Anything, the confidence paper, and the consensus paper included independent digest/review pages; these were used only as attention signals, not as substitutes for the arXiv abstracts.
- **Limitations:** arXiv supplies no official trending ranking; this report is not comprehensive and should be read as a notable-papers snapshot, not a readership ranking.
