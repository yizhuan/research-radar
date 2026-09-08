# arXiv Trending AI — monthly snapshot

Headline: The strongest supported pattern in this 30-day sample is a shift from “can the model solve the task?” toward whether agentic systems can choose experiments, survive realistic software environments, and remain reliable under paraphrase and reduced human oversight. This is an inferred shortlist, not an official arXiv popularity ranking: arXiv publishes no trending chart.

Window: 2026-08-09 through 2026-09-08 UTC; snapshot: 2026-09-08T17:48:08Z. Scope: cs.AI, cs.LG, stat.ML, cs.CL, cs.CV, cs.RO, cs.NE, and cs.MA, including cross-listed papers.

## Top papers (ranked)

### 1. [AI Research Preference Models](https://arxiv.org/abs/2608.13940v2)
- **Abstract:** AI research agents (AIRA) can now carry machine learning experiments from proposal through implementation and evaluation. Yet progress on frontier tasks is throttled by the cost of evaluations that can consume days of GPU time. When an agent can propose far more candidates than it can afford to run, progress depends on its research preference: how it allocates a fixed execution budget across many candidates. We introduce AI Research Preference Models (RPMs) that predict which candidate solution is most promising, without paying the cost of running them all. We build RPMs from frozen pretrained language models in two variants: an inference-only model that reasons over candidate plans, code, and previously executed solutions, and an agentic model that additionally runs small-scale pilot experiments. Integrated into the AIRA-dojo research agent and evaluated on the machine learning research benchmark AIRS-Bench, the two variants increase the average normalized score from 0.684 to 0.711 and 0.729, respectively. Both reach the unguided agent's 24-hour performance in roughly 15 hours, using less than two-thirds of its execution budget, and together yield new state-of-the-art results on two AIRS-Bench tasks.
- **Authors:** Thomas Simon Foster, Bassel Al Omari, Tingchen Fu, Thomas Mann, Carl Domond, et al.
- **arXiv:** `2608.13940v2` (published 2026-08-14T04:20:37Z; categories: `cs.AI`)
- **Evidence for ranking:** Evidence is sparse: Semantic Scholar returned the paper but no citation totals; it had a surfaced Hugging Face Papers result and a substantive v2 revision.
- **Claimed contribution:** The authors report normalized-score gains from 0.684 to 0.711 and 0.729, reaching the unguided agent’s 24-hour performance in about 15 hours.
- **Caveat:** The benchmark is AIRS-Bench and the gains are reported by the authors; generalization beyond that benchmark and budget regime remains open.
- **Announcement type:** revision, arXiv announcement date 2026-08-14
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 2. [SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring](https://arxiv.org/abs/2608.09802v1)
- **Abstract:** As AI coding agents take on increasingly complex, long-horizon software engineering tasks, existing benchmarks are rapidly saturating and their evaluation quality has come under serious scrutiny: a recent audit found that nearly 60% of unsolved SWE-bench Verified instances contain flawed tests -- either overly narrow tests that reject correct solutions or overly broad tests that check unstated requirements -- and that frontier models can verbatim reproduce gold patches from training data. Code refactoring, which requires coordinated, behavior-preserving changes across many files, offers a substantially harder and more realistic test of agent capability, yet remains underserved by current benchmarks. We introduce SWE-Bench ProMax, an expert-curated, multilingual code refactoring benchmark of 170 instances drawn from real commits across seven programming languages (Python, Java, TypeScript, Go, C, C++, and Rust). Every instance undergoes rigorous, multi-stage curation that directly addresses the quality problems identified in prior benchmarks: issue descriptions are rewritten from scratch to provide precise, unambiguous specifications, and test suites are manually reviewed to remove overly narrow and overly broad tests. Tasks with insufficient complexity or limited cross-file scope are filtered out, yielding a benchmark of challenging, large-scale refactoring tasks that average 11.4 modified files and 261.6 lines of code per instance, substantially exceeding the scale of existing benchmarks. Experiments with frontier models under two agent scaffolds show that the best model achieves only 41.2% resolve rate, confirming that SWE-Bench ProMax presents a meaningful and unsaturated challenge for current AI coding agents. Our benchmark is available at https://huggingface.co/datasets/swe-bench-promax/SWE-Bench-ProMax.
- **Authors:** Yuling Shi, Jinghan Xu, Kelin Fu, Wenhao Zeng, Shilin He, et al.
- **arXiv:** `2608.09802v1` (published 2026-08-10T16:23:19Z; categories: `cs.CL, cs.SE`)
- **Evidence for ranking:** Semantic Scholar returned no citation totals; independent search surfaced the paper and its public Hugging Face dataset.
- **Claimed contribution:** The paper reports a best resolve rate of 41.2% and tasks averaging 11.4 modified files and 261.6 lines of code.
- **Caveat:** The benchmark is newly introduced, and its difficulty/quality claims still need broader independent replication and contamination audits.
- **Announcement type:** new submission, arXiv announcement date 2026-08-10
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Data & synthetic data

### 3. [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489v1)
- **Abstract:** We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mathrm{SE}(3)$ transformations into attention via \textbf{PRoPE-style geometric encoding}, preserving arm identity and rigid-motion structure. Action control alone does not fully constrain scene geometry or the evolution of small manipulated objects. We therefore add a lightweight \textbf{depth branch} for scene-level geometry and use \textbf{SAM3 masks} with a frozen \textbf{V-JEPA teacher} to maintain object consistency throughout grasping. We further distill the multi-step generator into a few-step student via distribution-matching distillation for efficient deployment. At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge. Our model and code will be publicly available.
- **Authors:**  DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, et al.
- **arXiv:** `2608.13489v1` (published 2026-08-13T17:18:09Z; categories: `cs.CV, cs.RO`)
- **Evidence for ranking:** Semantic Scholar returned no citation totals; Hugging Face Papers surfaced the paper with the WorldArena placement, and the project/code release was independently searchable.
- **Claimed contribution:** The authors report first place on WorldArena 2.0 Track 1 and second place on Track 2.
- **Caveat:** The abstract says the model and code will be public; real-world transfer and the limits of benchmark-based ranking remain to be verified.
- **Announcement type:** new submission, arXiv announcement date 2026-08-13
- **Themes:** Robotics & control; Multimodal & vision-language; Efficient inference & systems

### 4. [Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models](https://arxiv.org/abs/2609.05401v1)
- **Abstract:** Vision-language models are increasingly used as reward functions for robotic learning, but this role requires paraphrase invariance: the same trajectory should receive the same reward under semantically equivalent goal descriptions. We show that current VLM reward models often violate this property. Paraphrasing the instruction alone can substantially change predicted progress scores, and can even flip identical robot behavior between failure and success. To measure this failure mode, we introduce ROBORMBENCH, a benchmark with 2,390 real-robot trajectories, ground-truth progress labels, and 21,673 verified paraphrases spanning lexical, syntactic, and action-goal rewrites. Across proprietary and open-source VLMs, paraphrase-induced instability is widespread and severe, grows under more divergent rewrites, and is not reliably reduced by scale or explicit reasoning. Dedicated reward models trained with trajectory-grounded supervision are substantially more stable. These results show that paraphrase robustness is a core requirement for reliable VLM-based reward modeling in robotics.
- **Authors:** Wonje Jeung, Sangyeon Yoon, Hyesoo Hong, Yoonjun Cho, Dongjae Jeon, et al.
- **arXiv:** `2609.05401v1` (published 2026-09-04T17:47:58Z; categories: `cs.RO, cs.CL`)
- **Evidence for ranking:** Semantic Scholar returned no citation totals; independent search produced multiple technical summaries within days of submission.
- **Claimed contribution:** The benchmark contains 2,390 real-robot trajectories, 21,673 verified paraphrases, and reports widespread instability across proprietary and open models.
- **Caveat:** The paper is a v1 preprint with a new benchmark; the extent to which trajectory-grounded training transfers to unseen robots and tasks is not established.
- **Announcement type:** new submission, arXiv announcement date 2026-09-04
- **Themes:** Robotics & control; Safety & alignment; Evaluation & benchmarks

### 5. [Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence](https://arxiv.org/abs/2608.31075v2)
- **Abstract:** Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience. This paper studies how LRMs can continue to improve as human supervision gradually recedes from the learning loop. We examine two connected dimensions of this problem. The reward axis traces the development from per-instance human judgments to reusable verifiers and rewards that operate even without human feedback. The experience axis examines how learning can progress from human-curated tasks and environments toward self-generated curricula, constructed environments, and autonomous co-evolution. We connect these dimensions through a five-level ladder from L0 to L4 that identifies which parts of the learning process remain under continued human control. Our analysis further highlights the risks introduced by increasingly autonomous rewards and experience generation, including reward hacking, feedback drift, curriculum collapse, and environment errors. Consequently, we also provide the evaluation around three complementary objects: policy capability, feedback fidelity, and experience quality. This analysis provides a structured account of current approaches to scaling LRMs beyond human supervision and the open problems involved in developing self-sustaining learning systems toward superintelligence. Furthermore, we maintain a continuously updated \href{https://github.com/visitworld123/Awesome-Scaling-LRM-Beyond-Human-Supervision}{GitHub repository} to track the latest advances.
- **Authors:** Zhiqin Yang, Jingwen Fu, Yuhan Liu, Hengyu Liu, Yonggang Zhang, et al.
- **arXiv:** `2608.31075v2` (published 2026-08-31T16:48:48Z; categories: `cs.AI`)
- **Evidence for ranking:** Semantic Scholar returned no citation totals; the paper had a surfaced Hugging Face Papers result and a v2 revision with a continuously updated repository.
- **Claimed contribution:** It proposes an L0–L4 ladder and highlights reward hacking, feedback drift, curriculum collapse, and environment errors as risks.
- **Caveat:** It is primarily a synthesis and framework rather than a new controlled capability result; its “path toward superintelligence” is not evidence that such scaling is feasible.
- **Announcement type:** revision, arXiv announcement date 2026-08-31
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 6. [AI Agents Push Humans Out of the Loop](https://arxiv.org/abs/2608.23642v2)
- **Abstract:** AI agents pose significant risks as they are granted increasing autonomy. A commonly proposed solution is human oversight and keeping a ''human in the loop'', but this is not a simple solution: Not only do current approaches to AI agent design impede effective human oversight, but the cognitive capacities required for it are also themselves degraded by extended use of AI systems. This position paper argues that current approaches to the development and deployment of AI agent systems do not support effective human oversight -- they contribute to its degradation. To address this, a top priority in the advancement of AI agents should be supporting the situated goals and cognitive requirements of effective human oversight, treating the human needs of overseers at the same level of importance as AI agent capability. To put this idea into practice, we connect work on automation and human-computer interaction to AI agent processes, outlining design-level affordances and organizational protocols that (1) support overseers in exercising critical judgement and (2) counteract the skill atrophy that arises from extended use of automation. We urge developers and deployers to adopt these or similar approaches. Without explicit support for the cognitive demands of effective human-agent interaction, AI agent systems will continue to passively incentivize the degradation of the very human skills they rely on.
- **Authors:** Margaret Mitchell, Avijit Ghosh, Samir Passi
- **arXiv:** `2608.23642v2` (published 2026-08-24T02:58:02Z; categories: `cs.AI, cs.HC`)
- **Evidence for ranking:** Semantic Scholar returned no citation totals; independent search surfaced the revised v2 paper, which was also among recent agent-related search results.
- **Claimed contribution:** The authors connect automation and HCI research to agent oversight and identify cognitive skill atrophy as a deployment risk.
- **Caveat:** The paper is argumentative and does not establish causal effect sizes for skill degradation across agent deployments.
- **Announcement type:** revision, arXiv announcement date 2026-08-24
- **Themes:** Safety & alignment; Agents & reasoning

## Trending research themes

- Agent systems are becoming research subjects themselves: AI Research Preference Models treats experiment selection as a learned policy, while Scaling Large Reasoning Models frames autonomous reward and experience generation as the next bottleneck.
- Evaluation is moving toward realistic failure modes. SWE-Bench ProMax targets large multilingual refactors; ROBORMBENCH tests paraphrase invariance rather than aggregate task scores.
- Robotics is combining world models with stricter reliability checks: DreamX-Phi targets action-faithful rollouts, while ROBORMBENCH shows that language variation can destabilize rewards.
- Human control is an explicit systems requirement. AI Agents Push Humans Out of the Loop treats oversight capacity and skill retention as design constraints, not deployment afterthoughts.

## Research opportunities

### Potential research areas
- Build agent benchmarks that jointly measure capability, budget allocation, software realism, and oversight quality, combining AI Research Preference Models, SWE-Bench ProMax, and AI Agents Push Humans Out of the Loop.
- Develop paraphrase-robust, trajectory-grounded reward models for embodied agents, extending ROBORMBENCH to unseen robots, languages, and long-horizon tasks.

### Unsolved problems
- How to generate autonomous rewards and curricula without reward hacking, feedback drift, or curriculum collapse remains open (Scaling Large Reasoning Models).
- Whether benchmark gains transfer to real deployments is unresolved for DreamX-Phi, SWE-Bench ProMax, and ROBORMBENCH.
- The size and reversibility of human skill degradation under sustained agent use are argued but not causally quantified (AI Agents Push Humans Out of the Loop).

### Potential research directions
- Create contamination-resistant, multi-repository refactoring evaluations with hidden behavioral tests and longitudinal maintenance tasks (SWE-Bench ProMax).
- Evaluate agent research selectors under distribution shift and fixed GPU/latency budgets, with calibration and failure-cost metrics (AI Research Preference Models).
- Pair world-model rollout metrics with real-robot intervention, object permanence, and paraphrase robustness tests (DreamX-Phi; ROBORMBENCH).

## Takeaway

The month’s clearest signal is methodological: credible progress is being defined by evaluation quality, resource-aware autonomy, and robustness under realistic interaction—not just higher static benchmark scores. The evidence is still preliminary because these are fresh preprints, citation counts are effectively unavailable for this window, and several selected contributions are benchmarks or position papers rather than replicated results.

## Method and sources

I queried arXiv’s API across the configured AI categories, deduplicated by versionless arXiv ID, and retained submissions/revisions in the stated 30-day window. Ranking is inferred from corroborated signals: cross-list/category relevance, substantive revisions, public datasets/code/projects, independent technical search results, and reported benchmark placements. Semantic Scholar’s batch lookup found the selected papers but returned no citation totals in this snapshot; therefore no citation momentum is claimed.

Primary sources: arXiv API, and each linked arXiv abstract page above. Corroborating discovery sources included Hugging Face Papers (DreamX-Phi; AI Research Preference Models; Scaling Large Reasoning Models), Hugging Face Datasets (SWE-Bench ProMax), the WorldSculpt project/code search result, and independent technical summaries for ROBORMBENCH.
