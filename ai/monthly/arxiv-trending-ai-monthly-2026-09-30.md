# September 2026 arXiv AI papers: inferred attention leaders

Snapshot: 2026-09-30 02:10 UTC | Window: 2026-09-01 through 2026-09-30

The attention leaders in this sample point in two directions: agent systems are being made more self-improving and knowledge-rich, while model work is extending into structured data, interactive video, and latent concepts. This ordering is inferred from Hugging Face Papers votes, not an official arXiv ranking; vote counts are platform attention, not readership or research quality.[1][2][5]

## Top papers (ranked)

### 1. [LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence](https://arxiv.org/abs/2609.17488)
- **Abstract:** LimiX-2 trains a contextual mechanism network on synthetic structural-causal data and reports leading results on tabular prediction and causal-skeleton recovery benchmarks.[1]
- **Authors:** Xingxuan Zhang, Gang Ren, Hao Yuan, Hao Zou, Hongze Tan, et al.[1]
- **arXiv:** `2609.17488v1` (published 2026-09-15 17:30:02 UTC; categories: `cs.AI`)[1]
- **Evidence for ranking:** 809 Hugging Face Papers upvotes in the September feed snapshot, the highest among the selected eligible papers; arXiv is the source for submission metadata. Semantic Scholar citation counts were unavailable (API rate-limited), so they do not contribute to this rank.[2]
- **Claimed contribution:** The authors introduce Contextual Mechanism Networks and Context-Conditional Masked Modeling, reporting strong results on TabArena, TALENT, and BCCO and causal-skeleton recovery from feature attention.[1]
- **Caveat:** The full-text evaluation is benchmark-based; its results should not be read as establishing general causal discovery in real deployments. I found no explicit limitations section in the HTML text checked.[1]
- **Announcement type:** new submission, 15 Sep 2026 (latest version checked: v1).[1]
- **Themes:** Training & adaptation; Evaluation & benchmarks[1]

### 2. [Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation](https://arxiv.org/abs/2609.11638)
- **Abstract:** Vidu S2 combines real-time interactive avatar generation and video editing, and explores extending both to spatial video.[3]
- **Authors:** Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, Deyuan Liu, et al.[3]
- **arXiv:** `2609.11638v1` (published 2026-09-10 14:46:07 UTC; categories: `cs.CV`, `cs.LG`)[3]
- **Evidence for ranking:** 701 Hugging Face Papers upvotes in the September feed snapshot, second-highest among selected eligible papers; Semantic Scholar citation counts were unavailable (API rate-limited).[4]
- **Claimed contribution:** The authors report real-time 720p avatar generation with changing references, stream editing, and results above their tested baselines.[3]
- **Caveat:** The authors identify high resolution and low end-to-end latency for spatial video as unresolved deployment challenges; they also point to panoramic spatial generation as future work.[3]
- **Announcement type:** new submission, 10 Sep 2026 (latest version checked: v1).[3]
- **Themes:** Multimodal & vision-language; Efficient inference & systems[3]

### 3. [Scaling Automatic Research Agents via World Models](https://arxiv.org/abs/2608.12564)
- **Abstract:** World Model RL (WMRL) substitutes learned world-model feedback for expensive environment execution in research-agent RL, correcting reward bias and noise with online debiasing and inverse-variance denoising.[5]
- **Authors:** Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li, et al.[5]
- **arXiv:** `2608.12564v3` (first submitted 2026-08-12 20:11:25 UTC; revised 2026-09-10 06:55:02 UTC; category: `cs.LG`)[5]
- **Evidence for ranking:** 482 Hugging Face Papers upvotes in the September feed snapshot. This is a September revision of an August preprint, included because the revision falls inside the window; Semantic Scholar citation counts were unavailable (API rate-limited).[6]
- **Claimed contribution:** The authors report 3–4× lower training compute on their tasks, competitive or improved results over standard RL, and transfer to embodied VLA post-training.[5]
- **Caveat:** WMRL still relies on some ground-truth environment executions to anchor the learned reward; its benefit depends on world-model predictions being useful enough to calibrate.[5]
- **Announcement type:** revision, 10 Sep 2026 (original submission: 12 Aug 2026).[5]
- **Themes:** Agents & reasoning; Efficient inference & systems[5]

### 4. [StudentSim: Training LLM-based Student Simulators](https://arxiv.org/abs/2609.01591)
- **Abstract:** StudentSim specializes simulators to sparse individual-learner data and evaluates behavioral fidelity and response to tutor guidance across chess, English writing, and mathematics.[7]
- **Authors:** Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, et al.[7]
- **arXiv:** `2609.01591v1` (published 2026-09-01 17:55:10 UTC; category: `cs.CL`)[7]
- **Evidence for ranking:** 477 Hugging Face Papers upvotes in the September feed snapshot, fourth among selected eligible papers; Semantic Scholar citation counts were unavailable (API rate-limited).[8]
- **Claimed contribution:** The authors report that StudentSim exceeds GPT-5.4 on both simulator metrics across three domains and show a chess-tutor reinforcement-learning proof of concept.[7]
- **Caveat:** The evaluated cohort is 60 students across three domains; the authors say modeling longer-term acquisition, retention, and forgetting across repeated interactions remains a deeper next step.[7]
- **Announcement type:** new submission, 1 Sep 2026 (latest version checked: v1).[7]
- **Themes:** Evaluation & benchmarks; Agents & reasoning[7]

### 5. [Atria Dawn: The Dawn of Agentic Superintelligence](https://arxiv.org/abs/2609.15818)
- **Abstract:** Atria Dawn Preview is an agentic model for research and engineering, trained with externally verified tool-use experiences and accompanied by a study of human–AI work practices.[9]
- **Authors:** Honglin Guo, Tao Gui, Kun Cai, Haodong Chen, Yicheng Chen, et al.[9]
- **arXiv:** `2609.15818v2` (first submitted 2026-09-14 16:22:30 UTC; revised 2026-09-17 17:33:02 UTC; category: `cs.AI`)[9]
- **Evidence for ranking:** 430 Hugging Face Papers upvotes in the September feed snapshot; this is a revision within the window. Semantic Scholar citation counts were unavailable (API rate-limited).[10]
- **Claimed contribution:** The authors report competitiveness with frontier agents on 16 benchmarks, top scores on five, and analyze 769 task records from 56 participants.[9]
- **Caveat:** The human–AI findings are a case study of one development process, not a controlled estimate of productivity gains across organizations; the paper emphasizes preserving human oversight.[9]
- **Announcement type:** revision, 17 Sep 2026 (original submission: 14 Sep 2026).[9]
- **Themes:** Agents & reasoning; Evaluation & benchmarks[9]

### 6. [Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills](https://arxiv.org/abs/2609.02749)
- **Abstract:** DisCo distills repository know-how into reusable, verified skills and uses those skills in a research-agent harness.[11]
- **Authors:** Jianlyu Chen, Yuyang Hu, Hongjin Qian, Jiawei Liu, Wenqing Wei, et al.[11]
- **arXiv:** `2609.02749v1` (published 2026-09-02 15:49:41 UTC; categories: `cs.AI`, `cs.CL`)[11]
- **Evidence for ranking:** 393 Hugging Face Papers upvotes in the September feed snapshot; Semantic Scholar citation counts were unavailable (API rate-limited).[12]
- **Claimed contribution:** With the same GPT-5.5 backbone, harness, and execution budget, the authors report gains over an agent without distilled skills on MLE-bench, PaperBench, FrontierCS, and PassNet.[11]
- **Caveat:** These gains are tied to the paper’s chosen backbone, harness, budgets, and benchmark suite; the abstract does not establish that the reported lift transfers to other agent stacks or tasks.
- **Announcement type:** new submission, 2 Sep 2026 (latest version checked: v1).[11]
- **Themes:** Agents & reasoning; Data & synthetic data[11]

### 7. [Continual Learning Mechanisms Compose for Long-Horizon Memorization](https://arxiv.org/abs/2609.06986)
- **Abstract:** The paper tests combinations of continual-learning mechanisms for retaining information across 100 sequential fine-tuning tasks and reports a best final-retention rate of 34.9%, versus 1.2% for naive sequential tuning.[13]
- **Authors:** Zheyuan Zhang, Alvin Zhang, Daniel Khashabi, Tianmin Shu[13]
- **arXiv:** `2609.06986v1` (published 2026-09-07 03:21:23 UTC; category: `cs.LG`)[13]
- **Evidence for ranking:** 375 Hugging Face Papers upvotes in the September feed snapshot; Semantic Scholar citation counts were unavailable (API rate-limited).[14]
- **Claimed contribution:** The authors find that combining data, function, and weight anchors with merged LoRA improves retention across three constructed 100-task datasets.[13]
- **Caveat:** Even the best reported method retains only about one-third of the evaluated information at this horizon, and the evidence is limited to the paper’s three constructed datasets.[13]
- **Announcement type:** new submission, 7 Sep 2026 (latest version checked: v1).[13]
- **Themes:** Training & adaptation; Evaluation & benchmarks[13]

### 8. [Compile by Training: Turning Natural-Language Specifications into Local Neural Functions](https://arxiv.org/abs/2609.04199)
- **Abstract:** Compile by training uses teacher-generated examples to train a compact adapter, turning a natural-language specification into a reusable local neural function.[15]
- **Authors:** Yuntian Deng, Pengyu Nie, Stuart Shieber[15]
- **arXiv:** `2609.04199v1` (published 2026-09-03 17:59:49 UTC; categories: `cs.CL`, `cs.AI`, `cs.LG`)[15]
- **Evidence for ranking:** 331 Hugging Face Papers upvotes in the September feed snapshot; Semantic Scholar citation counts were unavailable (API rate-limited).[16]
- **Claimed contribution:** On FuzzyBench-Hard the authors report 83.6% semantic accuracy, while noting compilation takes about a minute rather than seconds for the fast compiler.[15]
- **Caveat:** The quality improvement comes with higher compile-time cost, and the reported figure is on a selected benchmark subset.[15]
- **Announcement type:** new submission, 3 Sep 2026 (latest version checked: v1).[15]
- **Themes:** Efficient inference & systems; Training & adaptation[15]

### 9. [NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction](https://arxiv.org/abs/2609.10715)
- **Abstract:** NCP-ArchPreview adds a multi-token concept-prediction objective to next-token prediction, feeding predicted latent concepts back into autoregressive generation.[17]
- **Authors:** The Intern-NCP Team, Jiaqi Cao, Chiyu Chen, Shuang Cheng, Xu Cheng, et al.[17]
- **arXiv:** `2609.10715v1` (published 2026-09-09 18:12:43 UTC; category: `cs.CL`)[17]
- **Evidence for ranking:** 328 Hugging Face Papers upvotes in the September feed snapshot; Semantic Scholar citation counts were unavailable (API rate-limited).[18]
- **Claimed contribution:** At 8.9B parameters, the authors report matching OLMo-3-7B’s final pretraining loss with 51.3% of the training tokens and improving its downstream macro-average by 2.45 points after full pretraining.[17]
- **Caveat:** These are technical-report claims centered on comparisons with OLMo-3-7B; broader independent replication and comparisons across more model families remain unestablished here.
- **Announcement type:** new submission, 9 Sep 2026 (latest version checked: v1).[17]
- **Themes:** Training & adaptation; Efficient inference & systems[17]

### 10. [NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness](https://arxiv.org/abs/2609.08183)
- **Abstract:** NeoHorse-1 uses routed, verified agent interactions to create post-training examples and feeds evaluation signals back into training-data allocation.[19]
- **Authors:** NeoHorse Team, Guoliang Cao, Guohao Dai, Tianyu Guo, Kai Han, et al.[19]
- **arXiv:** `2609.08183v1` (published 2026-09-08 03:14:54 UTC; category: `cs.CL`)[19]
- **Evidence for ranking:** 326 Hugging Face Papers upvotes in the September feed snapshot; Semantic Scholar citation counts were unavailable (API rate-limited).[20]
- **Claimed contribution:** The authors report improved macro-average benchmark scores after post-training for 4B and 9B models across eleven agent, tool-use, coding, and instruction-following benchmarks.[19]
- **Caveat:** The paper describes an initial prototype; benchmark improvements after post-training do not by themselves demonstrate reliable recursive gains over repeated self-improvement cycles.[19]
- **Announcement type:** new submission, 8 Sep 2026 (latest version checked: v1).[19]
- **Themes:** Agents & reasoning; Training & adaptation[19]

## Trending Research Themes

- **Agent systems are being engineered as learning loops, not just prompt wrappers.** WMRL uses learned environment feedback for cheaper agent RL, while Atria Dawn studies tool-mediated outcomes and human collaboration.[5][9]
- **Knowledge packaging and routed feedback are emerging system components.** Repo-To-Skill supplies operational knowledge, while NeoHorse routes and recycles interaction data.[11][19]
- **Specialized representations are widening the model interface.** LimiX-2 learns joint structure for tabular data, NCP-ArchPreview predicts multi-token concepts, and Vidu S2 moves generation toward interactive and spatial video.[1][3][17]
- **Evaluation and feedback design remain central.** StudentSim separates simulator fidelity from responsiveness to guidance, while continual-learning work measures what survives a long update sequence; both make hidden failure modes measurable rather than relying on broad capability claims.[7][13]
- **A recurring practical constraint is the cost and reliability of learning signals.** WMRL trades real execution for learned feedback plus anchors, Compile by Training trades compile time for local inference, and the continual-learning study shows composition helps but does not eliminate forgetting.[5][13][15]

## Open Problems and Research Directions

- **Can simulated feedback be trusted as agents scale?** WMRL explicitly models bias and noise and retains a stream of real outcomes.[5] A useful next study would vary anchor frequency and world-model error under distribution shift, then report both task quality and cost.
- **What does learner modeling need beyond one-step response?** StudentSim’s authors identify longer-term learning, retention, and forgetting as open needs.[7] Follow-up work could test multi-session forecasts against longitudinal learner data and check whether tutor gains persist outside chess.
- **How can spatial generation meet real-time quality constraints?** Vidu S2’s discussion calls out the tension between latency and resolution and proposes panoramic generation as future work.[3] Measure end-to-end latency, spatial consistency, and user comfort jointly on interactive panoramic tasks.
- **How much continual retention is enough, and at what cost?** The best reported result reaches 34.9% final retention, leaving substantial forgetting even on the study’s constructed datasets.[13] Test the method under real chronological data streams, changing task distributions, and resource-matched replay or retrieval baselines.
- **Do reported agent improvements survive independent replication?** Several high-attention papers report large benchmark gains but use different harnesses and task suites.[9][11][19] Shared, blinded evaluations with frozen budgets, artifacts, and multi-run uncertainty estimates would help separate robust method gains from setup-specific advantages.

## Takeaway

September’s most visible work in this sample treats agents as systems that learn from experience, external tools, and stored operational knowledge—not merely as larger base models. The most actionable research questions are about whether those feedback loops remain reliable under longer horizons and real-world distribution shifts; Hugging Face votes measure attention, not validated impact, and the Semantic Scholar citation signal was unavailable for this snapshot.

## Method and sources

Window: 2026-09-01 to 2026-09-30 UTC; snapshot: 2026-09-30 02:10 UTC. The core arXiv scope was `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. The arXiv API reported 13,792 matches for the category/date query; the query was not exhaustively paginated. Candidate attention signals came from 642 entries in Hugging Face Papers’ daily listings for September, deduplicated by arXiv ID; ranking uses their observed cumulative upvotes and retains first submissions or revisions within the window. This is a platform-attention sample, not a complete or official arXiv trend chart. Semantic Scholar returned HTTP 429, so current citation and influential-citation totals could not be verified. I checked the arXiv HTML full text for the first three papers for results and caveats; the remaining paper summaries and caveats are based on their arXiv abstracts and the stated boundaries of those abstracts.

## Sources

[1] https://arxiv.org/abs/2609.17488
[2] https://huggingface.co/papers/2609.17488
[3] https://arxiv.org/abs/2609.11638
[4] https://huggingface.co/papers/2609.11638
[5] https://arxiv.org/abs/2608.12564
[6] https://huggingface.co/papers/2608.12564
[7] https://arxiv.org/abs/2609.01591
[8] https://huggingface.co/papers/2609.01591
[9] https://arxiv.org/abs/2609.15818
[10] https://huggingface.co/papers/2609.15818
[11] https://arxiv.org/abs/2609.02749
[12] https://huggingface.co/papers/2609.02749
[13] https://arxiv.org/abs/2609.06986
[14] https://huggingface.co/papers/2609.06986
[15] https://arxiv.org/abs/2609.04199
[16] https://huggingface.co/papers/2609.04199
[17] https://arxiv.org/abs/2609.10715
[18] https://huggingface.co/papers/2609.10715
[19] https://arxiv.org/abs/2609.08183
[20] https://huggingface.co/papers/2609.08183
