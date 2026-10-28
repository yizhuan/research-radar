# arXiv AI daily — 28 October 2026: six notable papers on agent teams, data scaling, and grounded evaluation

The latest daily batch across arXiv’s core AI categories contains six selected papers here, with recurring work on agent collaboration, synthetic training environments, and evidence-grounded evaluation; I’ll cover those first, then an embodied-learning paper and a pretraining-dynamics study. arXiv has no official trending chart, so this ordering is inferred from checkable signals and research relevance; citation evidence is especially limited for papers announced today.

## Top papers (ranked)

### 1. [TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571)
- **Abstract:** TeamGym evaluates and trains language-model teams on decisions built from legal, finance, medical, and software corpora, and reports substantial communication and retrieval gaps when pivotal evidence is distributed among agents.
- **Authors:** Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz, Yubin Kim, Taekyun Lee, et al.
- **arXiv:** `2610.37571v1` (published 2026-10-27 17:15:54 UTC; categories: `cs.AI`)
- **Evidence for ranking:** The paper’s 8-model, 12-corpus evaluation and controlled separation of communication from retrieval make it directly relevant to multi-agent capability measurement; an OpenReview listing provides a second checkable record. The arXiv batch page also places it among the day’s AI submissions. These are scope and discoverability signals, not readership statistics.
- **Claimed contribution:** The authors introduce pivotal information units and a configurable team benchmark, then report average success-rate drops of 22.9 percentage points from distributing pivotal evidence and another 19.9 points when teams must retrieve it from source material; two policy-training experiments improve final decisions and induce coordination.
- **Caveat:** The authors report one training run for each policy-training demonstration; on held-out MAUD problems, coordination patterns transfer more clearly than final-decision quality. Transfer to live teams and other task distributions is not established here.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 2. [Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648)
- **Abstract:** Across 458,752 synthetic tasks and 849 models of four sizes, the authors vary tool, task, and database diversity and report that scaling environment diversity and complexity can generalize better than simply adding tasks.
- **Authors:** Andrew Szot, Samira Abnar, Omar Attia, Abbas Kazerouni, Michael Kirchhof, et al.
- **arXiv:** `2610.37648v1` (published 2026-10-27 17:56:46 UTC; categories: `cs.LG`)
- **Evidence for ranking:** AITOP published a separate technical write-up of the SynthAPI findings, and the paper reports a large controlled study with four downstream evaluation benchmarks. Its scale and independent technical mention support placing it high for relevance; they do not establish popularity.
- **Claimed contribution:** The authors introduce SynthAPI and an environment-composition scaling law; they report improved generalization when the synthetic-data budget favors broader tools and database states, and benchmark gains over prior synthesis approaches.
- **Caveat:** The authors state that SynthAPI has no user-in-the-loop interactions, underrepresents long-document retrieval, and validates its scaling law on only one data pipeline; they do not claim transfer to other pipelines or training settings.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Agents & reasoning; Data & synthetic data

### 3. [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666)
- **Abstract:** ThinkWorld represents actions as discrete Chains-of-Dynamics and uses predicted-versus-observed future states to train VLA action reasoning from both robot demonstrations and videos without action labels.
- **Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, et al.
- **arXiv:** `2610.37666v1` (published 2026-10-27 17:59:52 UTC; categories: `cs.RO`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** It is cross-listed across robotics, AI, and computer vision, and reports simulation plus real-robot evaluations; the authors also provide a project page. The breadth and concrete embodied-learning evidence make it a strong relevance pick, though not an external popularity signal.
- **Claimed contribution:** The authors propose a shared motion-token reasoning space and consequence-grounded reinforcement learning, using future-state agreement to extend action supervision to unlabeled human videos; they report human-to-robot transfer and generalization to unseen tasks and environments.
- **Caveat:** The authors report training from a single seed, so their episode-level confidence intervals do not measure variation across independently trained checkpoints; inference latency also depends on the stated hardware and input setup.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Robotics & control; Multimodal & vision-language

### 4. [Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](https://arxiv.org/abs/2610.37624)
- **Abstract:** On a controlled 480-task benchmark, rarity- and relevance-based memory filters fail under different distributions of supporting and decoy facts, while attribution tags can induce social-proof errors in the final decision model.
- **Authors:** Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar
- **arXiv:** `2610.37624v1` (published 2026-10-27 17:49:39 UTC; categories: `cs.AI`, `cs.CL`, `cs.MA`, `cs.SI`)
- **Evidence for ranking:** The paper spans three core AI categories and isolates memory selection from evidence ownership using 60 templates and four model families; it is also listed in the Hugging Face Papers index. Those are breadth and discoverability signals, not evidence of readership.
- **Claimed contribution:** The authors introduce CrossProfile, which crosses ownership of supporting, decoy, and irrelevant facts while holding their text fixed; they report that neither rarest-first nor relevance-first selection is reliably better than random, and that removing or randomizing agent-attribution tags can improve accuracy in the classic hidden-profile setup.
- **Caveat:** The benchmark’s controlled discussions and fixed four-agent setup isolate specific failure mechanisms; the authors note that group-size effects are not varied, and the natural-discussion experiment is narrower than the controlled benchmark.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 5. [RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents](https://arxiv.org/abs/2610.36878)
- **Abstract:** RubricAtlas derives reusable analytical requirements from expert financial reports and evaluates deep-research reports through evidence-linked checkpoints, with completeness scored separately from argument validity.
- **Authors:** Delin Wang, Sinuo Wang, Rui Sun, Beidi Luan, Qiming Shi, et al.
- **arXiv:** `2610.36878v1` (published 2026-10-27 09:18:00 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The study covers 3,079 reports, 99 research types, and ten agents; an independent SignalFieldNotes article discusses the work. Cross-category relevance and a checkable secondary discussion support its place among notable new papers, not a popularity claim.
- **Claimed contribution:** The authors build type-level rubrics from multiple expert reports and report checkpoint agreement of κ=0.71 and agent-ranking agreement of Kendall τ=0.87 across two judge pipelines; controlled deletions lower scores on affected analyses.
- **Caveat:** The authors say their first-author audit is not independent expert validation, their source corpus is Chinese financial research, and generic argument-validity rules show limited judge agreement; completeness should not be read as correctness.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 6. [What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models](https://arxiv.org/abs/2610.37631)
- **Abstract:** Using six point-in-time model families and six benchmarks, the authors define a temporal variability score for item likelihoods and report that high-variability items improve faster later in pretraining, leading low-variability items in 34 of 36 final model-benchmark settings.
- **Authors:** Chang Su, Bin Wu, Emine Yilmaz, Yao Lu
- **arXiv:** `2610.37631v1` (published 2026-10-27 17:52:38 UTC; categories: `cs.AI`)
- **Evidence for ranking:** The arXiv record says the paper was accepted to AACL 2026, and its reported comparison spans six benchmarks and six models; it is included for direct relevance to training dynamics, not as a claim of unusual readership.
- **Claimed contribution:** The authors define temporal variability score (TVS) from item-level negative log-likelihood variation across point-in-time models and report a 7.3-point average chance-normalized accuracy advantage for high-TVS items at the end of training, with the effect strongest on knowledge-intensive tasks.
- **Caveat:** The authors limit the evidence to likelihood-ranked multiple-choice benchmarks and a single-size PIT-4B model series covering web crawls from 2017–2024; contamination checks do not cover all evaluated models’ pretraining corpora.
- **Announcement type:** new submission, 2026-10-28 announcement batch
- **Themes:** Training & adaptation; Evaluation & benchmarks

## Trending Research Themes

- **Agent teams as evidence-processing systems:** TeamGym separates the communication gap from the retrieval gap, while Rare, Relevant, and Still Wrong shows that memory selection and attribution can independently distort group decisions. Together, these papers move evaluation beyond whether a single model can answer a question to how teams preserve and combine evidence.
- **More discriminating evaluation, not just more scores:** TeamGym controls who holds pivotal information; CrossProfile independently varies fact ownership and usefulness; RubricAtlas tests whether reports cover recurring analyses; and What Improves During Pretraining tracks item-level learning trajectories. This is a recurring emphasis on diagnosis and measurement, not evidence that any single benchmark is definitive.
- **Training-data composition and knowledge acquisition:** Scaling Laws for Tool-Use Agents studies how synthetic environment diversity changes downstream generalization, while What Improves During Pretraining asks which knowledge items improve later. The shared focus is on the structure and timing of training data; the methods and targets differ substantially.
- **Embodied world-dynamics reasoning — isolated signal:** ThinkWorld is the batch’s clearest example of using predicted consequences to shape VLA action reasoning, including from unlabeled video. One paper is not enough to infer a field-wide shift.
- **Corpus concentration:** The current recent lists show 254 cs.AI and 237 cs.LG entries in the 28 October batch. This report’s six-paper selection also includes robotics and language categories, but it is selective rather than a census of the day’s submissions.

## Open Problems and Research Directions

- **Transfer of synthetic tool-use scaling laws:** The SynthAPI authors explicitly note the absence of user-in-the-loop interactions and limited long-document retrieval, and that the scaling law is validated on one pipeline. A useful next test is to reproduce the composition law on an independently built environment pipeline with clarification turns, long documents, and held-out tools (Scaling Laws for Tool-Use Agents).
- **Separate retrieval, communication, and decision errors in teams:** TeamGym reports distinct retrieval and communication gaps; Rare, Relevant, and Still Wrong finds that evidence can already be lost in natural discussion before compression. Follow-up work could vary team size and communication budget, then compare provenance-aware memory and retrieval interventions on held-out corpora (TeamGym; Rare, Relevant, and Still Wrong).
- **Validate report quality beyond completeness:** RubricAtlas reports that its first-author audit is not independent expert validation and that generic validity rules have limited agreement. Independent expert audits, non-financial and non-Chinese report domains, and stronger tests of argument validity could test how far type-level rubrics generalize (RubricAtlas).
- **Test temporal variability beyond likelihood-ranked multiple choice:** The authors of What Improves During Pretraining limit TVS evidence to a single-size PIT-4B series and multiple-choice benchmarks. Replications across model sizes and corpora, with broader generation or open-response tasks and stronger contamination checks, could determine whether the pattern generalizes (What Improves During Pretraining).
- **Measure robustness of world-imagination training:** ThinkWorld reports a single training seed. Replicated training runs, more embodiments, and broader held-out human-video sources would test whether its reported transfer is stable beyond the current simulation and real-robot evaluations (ThinkWorld).

## Takeaway

This batch’s most concrete common thread is measurement: several papers build controlled ways to expose where agents lose, mis-rank, or fail to integrate evidence, while another studies how synthetic-data composition affects tool use. The results are promising but remain preprints with bounded benchmarks, models, and training setups; the evidence supports a set of notable directions, not a reliable popularity ranking or a settled field-wide shift.

## Method and sources

- **Window:** Daily arXiv announcement batch dated 2026-10-28 (start date 2026-10-28; end date 2026-10-28). The selected version-1 submissions have first-submission timestamps on 2026-10-27. The category recent pages identify the current batch as Wed, 28 Oct 2026.
- **Snapshot:** 2026-10-28 17:07:38 UTC.
- **Scope:** Core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; cross-listed papers were included. Broad arXiv API query: `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`, sorted by last-updated date; the retrieved pool contained 782 records updated 2026-10-27 and represented all eight core categories. The official recent lists checked were [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), and [cs.RO](https://arxiv.org/list/cs.RO/recent).
- **Inference:** arXiv supplies no trending or readership chart. Ranking here is an inferred, relevance-led ordering informed by category breadth, reported evaluation scope, venue/secondary technical records, and independent discussion where found. Semantic Scholar Graph data checked at the snapshot showed 0 citationCount and 0 influentialCitationCount for each selected paper; these are current totals, not citations gained during the batch. Because attention evidence is sparse, the list should be read as notable recent papers rather than a popularity ranking.
- **Paper sources:** Each linked arXiv abstract page is the primary source. The top three papers were also reviewed in arXiv HTML for method, results, and author-stated limitations. Additional checkable sources: [AITOP coverage of SynthAPI](https://aitop.news/item/50529), [TeamGym OpenReview listing](https://openreview.net/forum?id=TRVP5LTMC9), [ThinkWorld project page](https://thinkworld-project.github.io/), [Hugging Face Papers listing for CrossProfile](https://huggingface.co/papers/2610.37624), [SignalFieldNotes discussion of RubricAtlas](https://signalfieldnotes.com/articles/46057), and the arXiv record for What Improves During Pretraining, which notes AACL 2026 acceptance.
