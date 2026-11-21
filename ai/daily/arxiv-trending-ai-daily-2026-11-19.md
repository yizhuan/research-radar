# arXiv AI daily — Thursday, 19 November 2026

Five notable new papers from the latest available core-AI announcement batch. A recurring pattern is agents tested against feedback grounded in real environments—from digital laboratory twins and post-training trajectories to physical robot actions and fabricated hardware. This briefing covers scientific-agent evaluation, behavior shaping, and embodied control. Caveat: arXiv has no official trending chart, and this is an inferred, relevance-weighted shortlist rather than a popularity ranking; independent attention and citation evidence are limited for such recent papers.

## Top papers (ranked)

### 1. [TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs](https://arxiv.org/abs/2611.26248)
- **Abstract:** TwinLab-Bench tests agents designing their own experiments across 52 real-laboratory-derived tasks, using lab-record-grounded digital twins and reports to score results; the strongest tested model averaged 45.0/100.
- **Authors:** Yang Wan, Linchao Zhu
- **arXiv:** `2611.26248v1` (published 2026-11-19 15:25:34 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** The strongest checkable outside-discussion signal found in this batch: independent coverage at [Emergent](https://emergent.sh/news/claude-fable-5-2-scores-45-100-twinlab-bench) and [AGI Hunt](https://agihunt.info/en/p/1a1f840d338862038e032d41170), plus a public [GitHub benchmark](https://github.com/ZJUSCL/TwinLab-Bench) and Hugging Face paper discussion. Its three-way cross-list within the core AI corpus also gives it unusually broad category relevance.
- **Claimed contribution:** The authors introduce task-specific “TwinLab agents” that return recorded or calculated experimental readings, and report that the best of 13 tested agents scores 45.0/100; the paper also analyzes common experiment-design failures.
- **Caveat:** The benchmark tests agents in constructed digital twins, not by conducting new physical experiments; its readings and scoring are grounded in the records and calculators assembled for 52 tasks.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Data & synthetic data

### 2. [PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity](https://arxiv.org/abs/2611.26565)
- **Abstract:** PhyDEX evaluates whether robot policies can infer object mass, center of mass, and friction to throw objects to targets, reporting sub-3% success for three tested VLA policies.
- **Authors:** Hao Vo, Taisei Hanyu, Yuki Ikebe, Pham Tri Quang, Sreevenkata Anjani Tishita Godavarthi, et al.
- **arXiv:** `2611.26565v1` (published 2026-11-19 18:33:43 UTC; categories: `cs.RO`)
- **Evidence for ranking:** The benchmark drew independent discussion from [Data Phoenix](https://dataphoenix.info/news/phydex-vla-physical-reasoning-benchmark) and a technical critique at [Pith](https://pith.science/paper/2611.26565); the arXiv abstract and full text make its evaluation setup and limits checkable. Attention indicators remain qualitative, not a readership measure.
- **Claimed contribution:** The authors provide 35,357 simulated trajectories across nine throwing tasks and 100 scenes, with humanoid and real-world tests; they report that providing ground-truth physical properties roughly doubles policy success.
- **Caveat:** The authors explicitly limit the benchmark to throwing, three randomized physical properties, and three VLA policies; they call for richer physics, more skills, and broader model coverage.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Robotics & control; Evaluation & benchmarks; Multimodal & vision-language

### 3. [AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher](https://arxiv.org/abs/2611.26510)
- **Abstract:** AutoMaster uses natural-language skills, trajectory analysis, and data selection to shape teacher demonstrations before fine-tuning a target model, reporting gains over vanilla supervised fine-tuning across six settings.
- **Authors:** Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao
- **arXiv:** `2611.26510v1` (published 2026-11-19 17:57:59 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Public release artifacts make the work directly inspectable: the authors provide a [project page](https://aweai-team.github.io/AutoMaster/), [code](https://github.com/RUCAIBox/AutoMaster), and models. A Hugging Face paper page and a multi-benchmark result provide further checkable signals; these indicate dissemination and technical relevance, not verified popularity.
- **Claimed contribution:** The authors report that Skill-FT improves mean performance over vanilla SFT by 1.42–8.99 percentage points on Terminal, Search, and software-engineering tasks, holding teacher, task pool, training-set size, and SFT recipe fixed.
- **Caveat:** The reported experiments use Qwen3.5 4B/9B target models and six settings across three task families; transfer to other model families, teachers, or tasks remains to be demonstrated.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Training & adaptation; Agents & reasoning; Evaluation & benchmarks

### 4. [AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](https://arxiv.org/abs/2611.26613)
- **Abstract:** AgentRoboCritic pairs each robot action with the agent’s stated local intent so a critic can label its outcome and failure mode, analyzing frontier agents across 12 manipulation benchmarks.
- **Authors:** Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, et al.
- **arXiv:** `2611.26613v1` (published 2026-11-19 18:57:25 UTC; categories: `cs.RO`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** Its cross-list spans three core AI categories, and the authors released a [12,844-action dataset and critic project](https://adu2021.github.io/blog/AgentRoboCritic/) with a human-annotated evaluation set. This is a concrete research artifact, but outside-attention evidence is sparse, so the placement is relevance-led.
- **Claimed contribution:** The authors report that fine-tuning Muse-Glimmer-30B raises failure-mode accuracy from 32.58% to 74.24% on their 400-action human-annotated benchmark, enabling lower-cost action-level analysis.
- **Caveat:** Critic validation is based on 400 human-annotated actions; generalization to other robots, action distributions, and independently annotated evaluation sets remains open.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Robotics & control; Evaluation & benchmarks; Agents & reasoning

### 5. [JARVIS: An Agent That Designs, Builds, and Tests Circuit Boards on Its Own](https://arxiv.org/abs/2611.26503)
- **Abstract:** JARVIS uses an embodied agent and executable digital twin to design, fabricate, measure, and revise circuit boards, demonstrating a 60 Hz notch filter built and tested without human intervention.
- **Authors:** Shibo Zhou, Tianqi Hong, Zheng Yan, He Yang
- **arXiv:** `2611.26503v1` (published 2026-11-19 17:53:30 UTC; categories: `cs.RO`, `eess.SY`)
- **Evidence for ranking:** The paper is indexed with paper/code information by [CatalyzeX](https://www.catalyzex.com/paper/jarvis-an-agent-that-designs-builds-and-tests) and [ArXivSignals](https://arxivsignals.io/papers/2611.26503). These are modest discovery signals rather than independent popularity measures; the lower placement reflects limited external attention and a single demonstrated circuit task.
- **Claimed contribution:** The authors report an end-to-end design–build–test–learn loop using unmodified desktop equipment, with a robot arm, PCB printer, pick-and-place machine, digital-twin rehearsal, and hardware-in-the-loop circuit tests.
- **Caveat:** The reported physical result is one first-run 60 Hz notch-filter experiment; it does not establish repeatability across board types, component failures, or longer production runs.
- **Announcement type:** new submission, announcement-batch 2026-11-19
- **Themes:** Robotics & control; Agents & reasoning; Evaluation & benchmarks

## Trending Research Themes

- **Agents judged by grounded feedback:** TwinLab-Bench compares proposed experiments with real-lab records; AutoMaster uses student evaluation and trajectories to revise demonstrations; AgentRoboCritic judges actions against stated intent; JARVIS rehearses a physical build in an executable twin. These papers share feedback loops, but do not establish a single converged agent architecture.
- **Evaluation is moving beyond task completion:** TwinLab-Bench scores experimental design, AgentRoboCritic labels action-level failures, and PhyDEX probes physical-property reasoning. This is a recurring methodological emphasis in the selected set, not evidence that benchmarks alone solve the underlying capability gaps.
- **Embodied AI remains a concentrated strand:** PhyDEX, AgentRoboCritic, and JARVIS are all primarily `cs.RO`, covering physical reasoning, action diagnosis, and fabrication. The daily candidate pool itself is broader: its 546 records include 157 primary `cs.CV`, 94 `cs.AI`, 91 `cs.LG`, 66 `cs.RO`, and 48 `cs.CL` papers; 470 have a configured core-AI category as primary, with the remaining 76 included through a core-AI cross-list.

## Open Problems and Research Directions

- **Digital twins versus physical science (author-stated boundary):** TwinLab-Bench tests design in record-grounded twins rather than new physical experiments. Compare agent-designed experiments with later physical replications in more laboratories, and measure how errors in each twin affect conclusions. [TwinLab-Bench](https://arxiv.org/abs/2611.26248)
- **Physical reasoning beyond throwing (author-stated limitation):** PhyDEX is limited to throwing and three randomized properties. Extend evaluation to pushing, sliding, pouring, deformable objects, and richer physics, then test whether policies can actively probe hidden properties rather than receive them. [PhyDEX](https://arxiv.org/abs/2611.26565)
- **Action-critic reliability (evidence-tied synthesis):** AgentRoboCritic validates labels on 400 human-annotated actions. Replicate the action-level evaluation with more annotators, robots, and unseen action distributions; separate critic error from policy recovery effects. [AgentRoboCritic](https://arxiv.org/abs/2611.26613)
- **Post-training transfer (evidence-tied synthesis):** AutoMaster’s gains cover one target-model family and three task families. Test other teachers and model families, and independently reproduce the benefit of retaining skill context in demonstrations. [AutoMaster](https://arxiv.org/abs/2611.26510)
- **Robust autonomous fabrication (evidence-tied synthesis):** JARVIS demonstrates one board experiment. Repeat across circuit classes and perturbations, log failures and recovery rates, and compare digital-twin predictions with repeated physical measurements. [JARVIS](https://arxiv.org/abs/2611.26503)

## Takeaway

The most visible pattern in this batch is not simply “more capable agents,” but more explicit evaluation of how agents use feedback in scientific and physical settings. The best-supported attention signal here is for TwinLab-Bench; the other entries are notable for their artifacts and concrete tests, while their popularity and generality remain uncertain.

## Method and sources

- **Window:** Latest available arXiv announcement batch, Thursday 2026-11-19; exact daily window 2026-11-19 through 2026-11-19. This is a prior batch relative to the snapshot at 2026-11-20 17:05:06 UTC. The broad submitted-date query returned papers through 2026-11-19, with the latest timestamp at 18:59:57 UTC.
- **Core corpus query:** `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`, constrained to `submittedDate:[202611190000 TO 202611200000]`, sorted by submitted date descending. It returned 546 records and represented all configured categories. Primary-category counts included `cs.CV` 157, `cs.AI` 94, `cs.LG` 91, `cs.RO` 66, `cs.CL` 48, `stat.ML` 9, `cs.MA` 3, and `cs.NE` 2. The rest were cross-listed from other primary categories.
- **Ranking method:** Evidence hierarchy was external coverage/discussion, cross-list breadth and publicly checkable research artifacts, then relevance of the reported evaluation. No numeric trend score was constructed. Papers are new submissions, not revisions. arXiv recent listings and every selected abstract page were checked; full-text pages were read for the leading three papers.
- **Citation and attention data:** Semantic Scholar fields were attempted but did not return usable records for this snapshot; citation totals were therefore not used. Attention claims above are tied to the cited checkable sources and are qualitative, not downloads, views, or votes.
- **Batch sources:** [arXiv cs.AI recent listings](https://arxiv.org/list/cs.AI/recent), [arXiv cs.RO recent listings](https://arxiv.org/list/cs.RO/recent), and the [arXiv API](https://export.arxiv.org/api/query?search_query=%28cat%3Acs.AI%20OR%20cat%3Acs.LG%20OR%20cat%3Astat.ML%20OR%20cat%3Acs.CL%20OR%20cat%3Acs.CV%20OR%20cat%3Acs.RO%20OR%20cat%3Acs.NE%20OR%20cat%3Acs.MA%29%20AND%20submittedDate%3A%5B202611190000%20TO%20202611200000%5D&sortBy=submittedDate&sortOrder=descending&start=0&max_results=2000).
- **Selected arXiv pages:** [2611.26248](https://arxiv.org/abs/2611.26248), [2611.26565](https://arxiv.org/abs/2611.26565), [2611.26510](https://arxiv.org/abs/2611.26510), [2611.26613](https://arxiv.org/abs/2611.26613), [2611.26503](https://arxiv.org/abs/2611.26503).
- **Corroborating sources:** [Emergent on TwinLab-Bench](https://emergent.sh/news/claude-fable-5-2-scores-45-100-twinlab-bench), [AGI Hunt on TwinLab-Bench](https://agihunt.info/en/p/1a1f840d338862038e032d41170), [TwinLab-Bench GitHub](https://github.com/ZJUSCL/TwinLab-Bench), [Data Phoenix on PhyDEX](https://dataphoenix.info/news/phydex-vla-physical-reasoning-benchmark), [Pith analysis of PhyDEX](https://pith.science/paper/2611.26565), [AutoMaster project](https://aweai-team.github.io/AutoMaster/), [AutoMaster GitHub](https://github.com/RUCAIBox/AutoMaster), [AgentRoboCritic project](https://adu2021.github.io/blog/AgentRoboCritic/), and [JARVIS CatalyzeX listing](https://www.catalyzex.com/paper/jarvis-an-agent-that-designs-builds-and-tests).