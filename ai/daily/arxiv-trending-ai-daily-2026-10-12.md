# arXiv AI: Monday 12 October 2026 — 10 notable papers

The batch leans toward dependable tool-using agents, recursive improvement, and embodied deployment; evaluation and efficient inference are also active. Today’s brief: agent reliability and safety, then robot learning and inference efficiency. This is an inferred relevance ranking, not an official arXiv trending chart; the latest batch is too new for strong citation evidence, so “hottest” cannot be measured as popularity.

## Top papers (ranked)

### 1. [RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](https://arxiv.org/abs/2610.13889)
- **Abstract:** RATED combines semantic tool retrieval with a contextual bandit that re-ranks tools using execution feedback, and introduces a benchmark of 5,172 tools and more than 210,000 query-tool pairs.
- **Authors:** Weiliang Chen; Song Liao
- **arXiv:** `2610.13889v1` (published 2026-10-09 17:38:11 UTC; categories: `cs.AI`, `cs.IR`)
- **Evidence for ranking:** The paper is accepted at CIKM 2026 and has a DOI; its EcoAgent benchmark covers thousands of real-world tools, and the authors report lower fault selection under outages. These are checkable research/validation signals, not attention counts.
- **Claimed contribution:** The authors report a 52.2% relative MRR improvement over ToolLLM’s API retriever and a reduction in fault selection from 86.2% to 2.9% in a 30%-failure scenario, with under 1 ms added latency.
- **Caveat:** The reported outage results are benchmark experiments; they do not establish reliability across every live tool ecosystem or failure distribution.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 2. [X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](https://arxiv.org/abs/2610.13886)
- **Abstract:** X-AgentRed uses a dependency graph and execution feedback to generate and refine harmful multi-tool workflows for testing personal agents.
- **Authors:** Yeonsung Jung; Zhiyuan Wang; Zifan Wang; Vítor Albiero; Benjamin Newman; et al.
- **arXiv:** `2610.13886v1` (published 2026-10-09 17:34:44 UTC; categories: `cs.AI`)
- **Evidence for ranking:** The authors evaluate four frontier agents in a simulated ecosystem of 30 services and 914 tools, reporting 1.77× the harmful-path rate and 2.99× tool coverage versus the compared baselines. The scale and comparative evaluation make it a notable safety result, not evidence of readership.
- **Claimed contribution:** The authors’ feedback-driven HarmFlow graph is designed to discover cross-service harmful paths that prompt-only red teaming may miss.
- **Caveat:** The authors note that updating the dependency graph as services and tools change adds computational cost; the evaluation uses a fixed simulated ecosystem.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 3. [RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://arxiv.org/abs/2610.13912)
- **Abstract:** RSI-Anything uses predictive world models to select actions and learning data, improve policies or workflows from feedback, and retain compatible updates across iterations.
- **Authors:** Taoyong Cui; Pinxian Zeng; Wanghan Xu; Hao Xiao; Shuhan Xue; et al.
- **arXiv:** `2610.13912v1` (published 2026-10-09 17:50:30 UTC; categories: `cs.CL`)
- **Evidence for ranking:** The paper reports experiments across code repair, GUI tasks, laboratory planning, reaction optimization, and an immune-science workflow; its code is linked from the abstract. Breadth across distinct task settings is the ranking signal.
- **Claimed contribution:** The authors report code-repair success rising from 26.3% with a static verifier to 31.2% after predictive selection and world-model adaptation, and laboratory-planning scores increasing across five policy versions.
- **Caveat:** Results are specific to the paper’s selected tasks and evaluation setups; they do not establish general recursive self-improvement across arbitrary environments.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Agents & reasoning; Training & adaptation

### 4. [Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945)
- **Abstract:** Splat2Act builds simulation-ready scene replicas from phone scans and uses generated demonstrations to personalize a vision-language-action policy to a user’s environment and objects.
- **Authors:** Xiaomeng Ye; Krishna Jaganathan; Gyubeum Lim; Gunjan Chhablani; Muhammad Zubair Irshad; Zsolt Kira
- **arXiv:** `2610.13945v1` (published 2026-10-09 17:59:06 UTC; categories: `cs.RO`, `cs.CV`)
- **Evidence for ranking:** The study spans 101 scanned campus environments, generates more than 68,000 pickup demonstrations, and includes a real Stretch 3 deployment. The authors report 63.9% success on a 12-task real-robot subset.
- **Claimed contribution:** The authors present an automated real-to-sim-to-real pipeline for scene-specific VLA adaptation using scene and object capture rather than user-collected demonstrations.
- **Caveat:** Real-robot evaluation is limited to a 12-task subset on one platform; the reported 62.5% aggregate target-scene success is from the personalized policy’s broader evaluation, not a universal deployment rate.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

### 5. [BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation](https://arxiv.org/abs/2610.13862)
- **Abstract:** BT-Agent combines LLM task decisions with behavior-tree skills, structured failure feedback, and an evaluation suite that compares text tasks with simulated robot execution.
- **Authors:** Fabio Hübel; Adam Lilja; Yue Yin; Siming He; Claire Tomlin; et al.
- **arXiv:** `2610.13862v1` (published 2026-10-09 17:08:45 UTC; categories: `cs.RO`)
- **Evidence for ranking:** It reports onboard operation with a 9B model on a quadruped, a 161-task benchmark, and simulated evaluation in Habitat; ablations identify structured tool calls and failure feedback as useful components.
- **Claimed contribution:** The authors report success gains over the strongest Act/ReAct baseline of about 10 percentage points at 4B and 5 points at 9B, and use the benchmark’s text mode for 10.9× higher evaluation throughput.
- **Caveat:** The 161-task text evaluation is not equivalent to physical execution; Habitat covers 39 tasks, and the reported onboard demonstration is on a quadruped.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Robotics & control; Agents & reasoning; Evaluation & benchmarks

### 6. [Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy](https://arxiv.org/abs/2610.13708)
- **Abstract:** Adaptive DHiSparse combines speculative decoding with a hierarchical KV cache whose GPU residency changes with serving load, aiming to sustain long-context throughput under memory pressure.
- **Authors:** Naji Alazhar; Wassel Alazhar
- **arXiv:** `2610.13708v1` (published 2026-10-09 15:02:35 UTC; categories: `cs.AI`, `cs.CL`, `cs.DC`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed in four core AI categories and reports workload-specific throughput and concurrency comparisons at 100K- and 500K-token contexts; these systems measurements support technical relevance.
- **Claimed contribution:** The authors report up to 4× concurrency versus HiSparse at matched latency bounds and 1.85× output versus resident serving in a stated 500K-context configuration.
- **Caveat:** The speedups are tied to specific models, context lengths, concurrency levels, and latency bounds; broader hardware and workload behavior remains to be established.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Efficient inference & systems

### 7. [A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning](https://arxiv.org/abs/2610.13744)
- **Abstract:** The paper argues that score-only privileged teachers fail to localize and correct reasoning errors, then conditions the teacher on generated critiques to create a more corrective distillation signal.
- **Authors:** Mayug Maniparambil; Ayush Rai; Ekansh Verma; Noel E. O'Connor; Fergal Reid
- **arXiv:** `2610.13744v1` (published 2026-10-09 15:36:47 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed across three core AI categories and reports analyses of error localization plus experiments in test-time recovery and cold-start GRPO; the arXiv comment says it was accepted as a NeurIPS 2026 FLLMPT workshop oral.
- **Claimed contribution:** The authors report that critique-conditioned scoring localizes errors and shifts probability toward tokens associated with backtracking, unlike the tested score-only signals.
- **Caveat:** Workshop acceptance and the paper’s reported experiments are preliminary evidence; the abstract does not establish robust gains across models, reasoning domains, or training regimes.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Training & adaptation; Agents & reasoning

### 8. [LapMerge: Differentiable Exact-Budget Token Merging in Linear Time](https://arxiv.org/abs/2610.13858)
- **Abstract:** LapMerge groups ordered tokens into an exact output budget using a learned mass distribution and linear-time scans, retaining differentiability while reducing sequence length.
- **Authors:** Magdalena Trędowicz; Aleksandra Nowak; Tomasz Steifer; Łukasz Struski; Szymon Płotka; Jacek Tabor
- **arXiv:** `2610.13858v1` (published 2026-10-09 17:07:17 UTC; categories: `cs.CV`)
- **Evidence for ranking:** The paper reports vision and vision-language evaluations, comparisons with token reducers, and speedups up to two orders of magnitude at large sequence lengths; this measurable efficiency claim is the ranking signal.
- **Claimed contribution:** The authors propose an exact-budget, differentiable reducer with forward and backward complexity O(M+N), and say it is most effective when token order reflects spatial or temporal locality.
- **Caveat:** The authors identify sequence locality as important; performance may not transfer to inputs whose token order lacks spatial or temporal structure.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Efficient inference & systems; Multimodal & vision-language

### 9. [Can Language Models Play the Wikipedia Game?](https://arxiv.org/abs/2610.13948)
- **Abstract:** The authors use link-navigation games across five Wikipedia languages and academic-paper citation graphs to compare model retrieval/navigation with human and TF-IDF baselines.
- **Authors:** Alexander Hickey; Joanna Knight; James Bishop
- **arXiv:** `2610.13948v1` (published 2026-10-09 17:59:56 UTC; categories: `cs.AI`, `cs.IR`)
- **Evidence for ranking:** It spans five languages and five academic-literature datasets, supplies code for large local graphs, and includes human and TF-IDF baselines; breadth and comparative design make it notable.
- **Claimed contribution:** The authors report that the best tested models achieved human-comparable success but did not significantly outperform humans, with rankings varying across languages and topics.
- **Caveat:** Link navigation is an analogue of information retrieval, not a complete test of open-domain retrieval; the authors report model rankings vary by language and topic.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Retrieval & knowledge; Evaluation & benchmarks

### 10. [Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection](https://arxiv.org/abs/2610.13821)
- **Abstract:** On factual question answering, the study compares training the model and a separate answer selector to improve the decision to answer or abstain.
- **Authors:** Juan Terven; Diana-Margarita Córdova-Esparza; Ruben Gomez; Carlos Miranda Rocha; Julio-Alejandro Romero-González; Edgar Chavez-Urbiola
- **arXiv:** `2610.13821v1` (published 2026-10-09 16:33:27 UTC; categories: `cs.CL`)
- **Evidence for ranking:** It reports three training seeds, two held-out confidence thresholds, and a partial human-reviewed audit on TriviaQA; its comparison across TriviaQA and NQ-Open tests where answer selection does and does not transfer.
- **Claimed contribution:** The authors report improved threshold-averaged utility over a calibrated confidence filter on both datasets, while TriviaQA coverage rises from 20.2% to 30.9% and scored-answer error falls from 23.0% to 14.5% under exact match.
- **Caveat:** The authors report that reinforcement-learning changes did not produce consistent gains and that on NQ-Open the selector remained worse than always abstaining.
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Safety & alignment; Evaluation & benchmarks

## Trending Research Themes

- **Agents are shifting from fluent action to dependable operation.** RATED uses runtime reliability feedback to rank tools; BT-Agent constrains robot behavior with executable skills and failure feedback; X-AgentRed explores compositions of tool actions that can create harm.
- **Learning from interaction is being made recursive.** RSI-Anything couples world-model prediction, observed feedback, and retention checks; critique-conditioned distillation treats error localization as an explicit search problem rather than assuming a score is corrective.
- **Embodied models are being tested against execution, not only language prompts.** Splat2Act personalizes a VLA from scene scans and generated demonstrations; BT-Agent compares faster text screening with simulation and onboard robot operation.
- **Efficiency work targets concrete bottlenecks.** Adaptive DHiSparse focuses on KV memory and long-context serving; LapMerge reduces token sequences with an exact budget and linear-time aggregation.
- **Evaluation quality remains a research topic in its own right.** The Wikipedia Game compares model navigation with humans across languages and domains; the abstention study shows that utility improvements can be dataset-dependent.

## Open Problems and Research Directions

- **Can agent safety evaluation keep up with changing tools?** X-AgentRed identifies the graph-maintenance cost as services evolve. A useful follow-up is to test incremental graph refresh and measure whether coverage and harmful-path discovery remain stable as tools, permissions, and service state change.
- **When do self-improvement loops remain reliable as models change?** RSI-Anything uses compatibility and retention checks, but its results are task-specific. Test held-out environments and longer update chains, tracking both capability gains and regressions under a fixed interaction budget.
- **How much simulation evidence predicts real robot success?** Splat2Act’s physical evaluation covers a limited 12-task subset, while BT-Agent’s text benchmark is much faster than its simulation. Expand matched task suites across more homes, objects, robots, and failure conditions, and quantify how often simulation ranking predicts real execution.
- **Which reliability or efficiency gains generalize beyond the tested operating point?** RATED, Adaptive DHiSparse, and LapMerge report bounded benchmark settings. Replicate across tool-failure distributions, serving hardware/load profiles, and sequence structures, publishing latency/quality trade-offs as well as peak gains.
- **Can answer-selection improvements transfer without suppressing useful answers?** The abstention study’s NQ-Open result shows a boundary. Evaluate calibrated answer selection across domains and scoring rules, including selective coverage, error costs, and human review.

## Takeaway

The most coherent pattern in this batch is operational reliability: papers make agents observe tool failures, explicitly inspect mistakes, or test actions in physical/simulated environments. The work is technically varied rather than one unified breakthrough, and evidence is mostly author-reported preprint evaluation; whether these gains generalize outside their testbeds remains open.

## Method and sources

- **Window:** the latest arXiv announcement batch, Monday 2026-10-12. At the snapshot, the current UTC calendar day (2026-10-13) had no newer batch, so this report uses the prior announcement batch. Exact daily window: 2026-10-12 batch only.
- **Snapshot:** 2026-10-13 00:10:11 UTC.
- **Scope/query:** `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`; category recent pages were checked for the batch date, and arXiv metadata/abstract pages were checked for each selected paper.
- **Inference:** arXiv publishes no official trending ranking. Ordering is an inferred “notable recent” list, prioritizing checkable conference/DOI status, cross-category relevance, evaluation breadth, and reported empirical evidence. No downloads, views, or social attention are claimed. Citation evidence for this newly announced batch was limited; Semantic Scholar citation metadata was unavailable at the snapshot.
- **Sources:** [cs.AI recent](https://arxiv.org/list/cs.AI/recent), [cs.LG recent](https://arxiv.org/list/cs.LG/recent), [stat.ML recent](https://arxiv.org/list/stat.ML/recent), [cs.CL recent](https://arxiv.org/list/cs.CL/recent), [cs.CV recent](https://arxiv.org/list/cs.CV/recent), [cs.RO recent](https://arxiv.org/list/cs.RO/recent), [cs.NE recent](https://arxiv.org/list/cs.NE/recent), [cs.MA recent](https://arxiv.org/list/cs.MA/recent). Paper abstracts are linked in each title; the RATED paper lists DOI `10.1145/3799682.3839887` and CIKM 2026 proceedings.
