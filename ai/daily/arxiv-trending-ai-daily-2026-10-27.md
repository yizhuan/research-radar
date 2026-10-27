# arXiv AI papers — Tuesday, 27 October 2026 batch

The latest announced AI-category batch for 27 October has 11 selected papers. The strongest pattern is interactive agents evaluated under changing context and long-horizon work, alongside video, spatial-audio, and image-generation systems. Spoken agenda: tool-use and proactive agents, human-facing and embodied worlds, then generative and adaptation methods. arXiv has no official trending chart; this ordering is inferred from dated third-party upvotes, filtered to papers in this batch, and citation evidence for these recent preprints is limited.

## Top papers (ranked)

### 1. [Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents](https://arxiv.org/abs/2610.33568)
- **Abstract:** Trajectory2Gym constructs tool-use training interactions that cover underrepresented dependencies and only supervises decisions supported by the agent-visible history.
- **Authors:** Yihao Hu, Zhihao Wen, Yitong Lin, Siyuan Lu, Pan Wang, et al.
- **arXiv:** `2610.33568v1` (published 2026-10-24T09:38:02Z; categories: `cs.CL`)
- **Evidence for ranking:** 121 upvotes in the Tuesday 27 October Hugging Face Daily Papers list, the highest count on that dated list; the paper reports consistent gains across five Qwen3 scales. This is a third-party attention signal, not an arXiv popularity statistic.
- **Claimed contribution:** The authors report that Trajectory2Gym improves the equal-weight mean across Tau1, Tau2, and BFCL by 16.9–29.8 percentage points over their baselines across tested scales, with the strongest gains on stateful and multi-turn interactions.
- **Caveat:** The reported results are on three tool-use benchmarks and Qwen3 scales; transfer to other agent families and live tool environments is not established.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Agents & reasoning; Training & adaptation; Data & synthetic data

### 2. [StreamVibe: Proactive Video Agents for Evolving User Intent](https://arxiv.org/abs/2610.34662)
- **Abstract:** StreamVibe combines a benchmark, streaming vision-language model, and persistent-state harness to infer implicit user intent and adapt responses as that intent changes.
- **Authors:** Chengzhi Liu, Yuxiang Lai, Yuzhe Yang, Yanqing Liu, Jiheng Hou, et al.
- **arXiv:** `2610.34662v1` (published 2026-10-26T00:48:27Z; categories: `cs.CV`)
- **Evidence for ranking:** 98 upvotes in the Tuesday daily list, second-highest; the paper reports a 4.1K-sample benchmark and sustained-interaction experiments.
- **Claimed contribution:** The authors report a 10.7% improvement in response timing and answer quality over baselines and a further 12.3% gain in proactive interaction from the StreamVibe harness.
- **Caveat:** The authors note that the benchmark does not yet capture richer co-evolution of user intent and environment over longer horizons.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Multimodal & vision-language; Agents & reasoning; Evaluation & benchmarks

### 3. [InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants](https://arxiv.org/abs/2610.33966)
- **Abstract:** InteractiveWorld simulates closed-loop assistance in which an MLLM instructs a human actor who acts in a changing scene, and provides a 120-task benchmark with state-based rewards.
- **Authors:** Qinsi Wang, Wei Wen, Chong Zhou, Saksham Suri, Zechun Liu, et al.
- **arXiv:** `2610.33966v1` (published 2026-10-25T00:44:29Z; categories: `cs.HC`, `cs.CV`)
- **Evidence for ranking:** 71 upvotes in the Tuesday daily list, third among listed papers; the benchmark evaluates 12 frontier MLLMs on multi-turn tasks and includes a human-agent study.
- **Claimed contribution:** The authors report that even their strongest tested model reaches at most 20% on long-horizon Guidance and 25% on Planning tasks, showing substantial gaps in the evaluated assistant setting.
- **Caveat:** The authors identify human-agent realism and additional real environments as future work; benchmark outcomes are not yet a substitute for deployment with diverse real users.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language; Agents & reasoning

### 4. [WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control](https://arxiv.org/abs/2610.33135)
- **Abstract:** WorldCast combines explicit 3D geometric guidance with geometry-aligned memory attention to preserve character appearance and identity during large-angle camera motion in generated video.
- **Authors:** Lei Cao, Yu Liu, Wenhua Liao, Peng Zhang, Fei Wang, et al.
- **arXiv:** `2610.33135v1` (published 2026-10-23T14:15:01Z; categories: `cs.CV`)
- **Evidence for ranking:** 40 upvotes in the Tuesday daily list, fourth-highest; the authors introduce a dedicated large-angle camera-trajectory dataset and report evaluations across trajectories.
- **Claimed contribution:** The authors report accurate camera-trajectory following while preserving character geometry, appearance, and identity on the CLACT benchmark.
- **Caveat:** The evaluation is focused on character-centric video and the proposed large-angle camera benchmark; results do not establish generalization to other video-generation domains.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Multimodal & vision-language; Training & adaptation

### 5. [Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion](https://arxiv.org/abs/2610.34415)
- **Abstract:** AMBIT uses executable scene plans and a shared Transfusion model for first-order ambisonics audio generation and editing, with on-policy self-distillation for both planning and rendering.
- **Authors:** Kam Man Wu, Yu Zhang, Pengjun Fang, Mingfei Chen, Weijia Chen, et al.
- **arXiv:** `2610.34415v1` (published 2026-10-25T16:13:07Z; categories: `cs.SD`, `cs.AI`)
- **Evidence for ranking:** 28 upvotes in the Tuesday daily list, tied for fifth; the paper reports tests across speech, music, and sound and is cross-listed in a core AI category.
- **Claimed contribution:** The authors report improvements in generation content and spatial quality, instruction-guided editing fidelity, and preservation of unedited sources over their compared baselines.
- **Caveat:** The work targets first-order ambisonics and its reported speech/music/sound evaluation; broader spatial formats and downstream listening use cases are not established by the abstract.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Multimodal & vision-language; Training & adaptation; Efficient inference & systems

### 6. [DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://arxiv.org/abs/2610.34467)
- **Abstract:** DynaFlow trains a main agent to synthesize executable workflows that coordinate fixed sub-agents through sequential or parallel calls, structured information exchange, and verification.
- **Authors:** Ruhao Liu, Qi Li, Shizun Wang, Xinchao Wang
- **arXiv:** `2610.34467v1` (published 2026-10-25T17:38:55Z; categories: `cs.MA`)
- **Evidence for ranking:** 28 upvotes in the Tuesday daily list, tied with AMBIT; it reports results on six benchmarks and a same-backbone comparison.
- **Claimed contribution:** The authors report 88.08% overall accuracy in Forced mode with Qwen3.5-27B, 10.90 percentage points above their strongest evaluated baseline.
- **Caveat:** The method keeps all sub-agents fixed and improves the orchestrator; it does not establish gains when executor capabilities also change.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 7. [Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845)
- **Abstract:** This work presents a systems-level framework for understanding digital work agents through persistence, openness, capability families, and joint model/harness optimization.
- **Authors:** Zishan Xu, Enjun Du, Mingqi Gao, Cheng Yang, Junhao Shen, et al.
- **arXiv:** `2610.35845v1` (published 2026-10-26T17:56:21Z; categories: `cs.LG`)
- **Evidence for ranking:** 22 upvotes in the Tuesday daily list; the paper organizes work-agent capabilities and evaluation around verifiable work outcomes and links code.
- **Claimed contribution:** The authors propose a work-centric taxonomy covering persistence, openness, five task forms, five capability families, and approaches to model and harness optimization.
- **Caveat:** This is primarily a systems perspective and synthesis of existing methods rather than a single controlled benchmark result; its framework needs validation across deployed work settings.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 8. [Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based RL](https://arxiv.org/abs/2610.33512)
- **Abstract:** FORK augments rubric-based reinforcement learning with a precision objective that penalizes unnecessary or factually incorrect response units alongside rubric coverage.
- **Authors:** Hyun Ryu, Jong-Heon Kim, Yiqing Xie, Seungone Kim, Carolyn Rose, Eunho Yang
- **arXiv:** `2610.33512v1` (published 2026-10-24T07:43:06Z; categories: `cs.CL`)
- **Evidence for ranking:** 19 upvotes in the Tuesday daily list; the authors report benchmark results comparing precision and coverage and provide a code link.
- **Claimed contribution:** The authors report similar rubric coverage with improved precision and response length, with win rates increasing from 10.6% to 68.0% on RubricHub-Medical and 22.1% to 74.1% on HealthBench versus the original recall-based reward.
- **Caveat:** The reported win-rate evidence is from medical response benchmarks and relies on rubric necessity and factual-correctness judgments; transfer to other domains and grader reliability remain open.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Safety & alignment; Training & adaptation; Evaluation & benchmarks

### 9. [World-in-Context: Interactive Video World Modeling with In-Context Conditioning](https://arxiv.org/abs/2610.33169)
- **Abstract:** World-in-Context represents view, action, and camera controls as explicit tokens in a shared attention space and uses accumulated control transitions to model interactive video rollouts.
- **Authors:** Harold Haodong Chen, Rui Peng, Rongjin Guo, Lingteng Qiu, Kejie Qiu, et al.
- **arXiv:** `2610.33169v1` (published 2026-10-23T18:05:48Z; categories: `cs.CV`)
- **Evidence for ranking:** 17 upvotes in the Tuesday daily list; the paper reports navigation and perspective-switching measures on WBench.
- **Claimed contribution:** The authors report that the 5B model matches 22B EchoWM on navigation (81.5 vs. 81.6) and reaches 93.8% perspective-switching success, compared with 18.8% for existing 5B baselines.
- **Caveat:** The reported comparisons are tied to WBench and the tested model sizes; transfer to physical control or broader interactive environments is not established.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Robotics & control

### 10. [Δτ-Bench: Pushing Agents Toward a Moving Capability](https://arxiv.org/abs/2610.34238)
- **Abstract:** Δτ-Bench tests whether agents can adapt procedural knowledge as tool ecosystems change, and introduces Steward to maintain skills and provision tools during execution.
- **Authors:** Shuofei Qiao, Xuanguang Pan, Yijun Chen, Wendi Feng, Bin Wu, et al.
- **arXiv:** `2610.34238v1` (published 2026-10-25T12:10:52Z; categories: `cs.CL`, `cs.AI`, `cs.CV`, `cs.IR`, `cs.LG`, `cs.SE`)
- **Evidence for ranking:** 15 upvotes in the Tuesday daily list; it is cross-listed in four core AI categories and evaluates 1,588 validated multi-turn tasks across 42 domains and six ecosystem states.
- **Claimed contribution:** The authors report that the strongest tested model or harness achieves 42.3% task success, and that Steward sustains higher success across ecosystem changes with lower skill-maintenance overhead.
- **Caveat:** The benchmark uses capability-preserving transformations to create successive ecosystem states; behavior under live, uncontrolled tool changes remains to be established.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Efficient inference & systems

### 11. [Qwen-Image-PE: Learning Visual Design for Text-to-Image Prompt Enhancement](https://arxiv.org/abs/2610.33472)
- **Abstract:** Qwen-Image-PE trains prompt enhancers to improve visual design dimensions through caption-based supervised learning and groupwise image-reward reinforcement learning.
- **Authors:** Zekai Zhang, Yanran Zhang, Shengming Yin, Yan Shu, Zhening Liu, et al.
- **arXiv:** `2610.33472v1` (published 2026-10-24T05:50:40Z; categories: `cs.CV`)
- **Evidence for ranking:** 15 upvotes in the Tuesday daily list, tied with Δτ-Bench; the source-list order breaks the tie. The paper reports cross-backbone evaluations and releases a 9B model.
- **Claimed contribution:** The authors report a 7.81-point improvement on Qwen-Image-Bench for Qwen-Image-PE-397B and say the 9B variant outperforms evaluated prompt-enhancement baselines, with gains transferring to four additional text-to-image backbones.
- **Caveat:** The reported improvements concern prompt enhancement and visual-design benchmarks; the abstract does not establish gains for arbitrary image-generation workflows or user populations.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Multimodal & vision-language; Training & adaptation; Evaluation & benchmarks

## Trending Research Themes

- **Agents are being evaluated through full interactions and changing conditions.** Trajectory2Gym constructs stateful tool-use supervision; StreamVibe responds to evolving intent; InteractiveWorld measures multi-turn human-assistant guidance; and Δτ-Bench tests adaptation as tools change. These papers share an evaluation focus, not a single method.
- **Agent harnesses and orchestration are becoming explicit research objects.** DynaFlow learns workflow structure, Work Agents organizes capability and runtime concerns, and Trajectory2Gym focuses on the quality of interaction data. This is a recurring agent-systems theme in this batch.
- **World models increasingly expose control structure.** WorldCast adds camera geometry for consistent character video, while World-in-Context tokenizes view, action, and camera controls. Their methods address different problems; shared use of explicit structure is the narrower methodological link.
- **Generative models are being steered with richer constraints.** AMBIT uses executable spatial-audio plans, and Qwen-Image-PE trains for visual-design criteria. These are isolated signals across audio and image generation, not evidence of one converged approach.
- **Reward design remains a reliability lever.** Eat Your Precision adds response precision to rubric coverage; Trajectory2Gym restricts supervision to decisions supported by visible context. Both make the quality of training signals more explicit.

## Open Problems and Research Directions

- **Open problem (reported boundary):** Trajectory2Gym's results cover three tool-use benchmarks and five Qwen3 scales. **Research direction (synthesis):** replicate the supervision recipe on other agent families and live software/web tools, measuring whether gains survive distribution shifts in available actions and observations. [Trajectory2Gym](https://arxiv.org/abs/2610.33568)
- **Open problem (author-stated):** StreamVibe's current setting does not capture the full co-evolution of user intent and environment over long horizons. **Research direction (synthesis):** build longer interaction streams with user-driven goal changes and environment feedback, then compare response quality, timing, and task completion under the same protocol. [StreamVibe](https://arxiv.org/abs/2610.34662)
- **Open problem (author-stated):** InteractiveWorld identifies human-agent realism and real-environment breadth as future work. **Research direction (synthesis):** validate state-based simulation scores against studies with diverse real users and scanned physical environments. [InteractiveWorld](https://arxiv.org/abs/2610.33966)
- **Open problem (reported boundary):** Δτ-Bench creates evolving tools through controlled transformations. **Research direction (synthesis):** test whether Steward's skill maintenance transfers to real tool updates, missing services, and conflicting documentation, with recovery and stale-skill metrics. [Δτ-Bench](https://arxiv.org/abs/2610.34238)
- **Open problem (reported boundary):** WorldCast and World-in-Context report results on video-world benchmarks, not physical control. **Research direction (synthesis):** measure whether their control representations improve long-horizon closed-loop behavior under occlusion, camera shifts, and unseen actions. [WorldCast](https://arxiv.org/abs/2610.33135); [World-in-Context](https://arxiv.org/abs/2610.33169)
- **Open problem (reported boundary):** FORK's results rely on rubric and factuality graders in medical-response settings. **Research direction (synthesis):** audit grader agreement and reward hacking across additional domains and with blinded human preference evaluation. [Eat Your Precision](https://arxiv.org/abs/2610.33512)

## Takeaway

The most visible signal in this batch is a shift toward measuring agents in extended, changing interactions: tool use, proactive assistance, human guidance, and evolving tool ecosystems. The papers offer concrete benchmarks and training mechanisms, but their reported gains remain tied to specific simulators, backbones, and task families; broad transfer is still uncertain.

## Method and sources

- **Window:** Daily announcement batch dated 2026-10-27; exact announcement-date window 2026-10-27 through 2026-10-27. Snapshot: 2026-10-27T17:05:10Z. The selected papers' first-submission timestamps range from 2026-10-23 through 2026-10-26 and appear in the Tuesday 27 October new-listing batch.
- **Category query:** Screened the official `/new` pages for `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; retained cross-listed papers and other-primary-category papers with an unambiguous AI contribution. Every selected record is a v1 new submission verified on its arXiv abstract page.
- **Attention and ranking:** Ranked eligible selected papers by the 27 October Hugging Face Daily Papers upvotes recorded at 2026-10-27 07:06 UTC: 121, 98, 71, 40, 28, 28, 22, 19, 17, 15, 15. The tied counts use source-list order. These are dated third-party attention counts, not arXiv readership or citation totals. Papers outside the current official new-listing batch were excluded even if they had more votes in the daily list.
- **Citation evidence:** Semantic Scholar citation totals and velocity were not usable at this snapshot; no citation counts were imputed or used to rank entries.
- **Verification:** Each selected abstract page was opened to check version, date, categories, authors, and abstract. The introduction, results, and limitations of the top three papers were checked in full-text HTML/PDF.
- **Sources:** Official arXiv new listings: [cs.AI](https://arxiv.org/list/cs.AI/new), [cs.LG](https://arxiv.org/list/cs.LG/new), [stat.ML](https://arxiv.org/list/stat.ML/new), [cs.CL](https://arxiv.org/list/cs.CL/new), [cs.CV](https://arxiv.org/list/cs.CV/new), [cs.RO](https://arxiv.org/list/cs.RO/new), [cs.NE](https://arxiv.org/list/cs.NE/new), [cs.MA](https://arxiv.org/list/cs.MA/new); [Tuesday 27 October daily attention record](https://trendingai.today/2026-10-27/); [week 44 archive](https://trendingai.today/week/2026-44/). Canonical arXiv abstract URLs are linked per paper.
