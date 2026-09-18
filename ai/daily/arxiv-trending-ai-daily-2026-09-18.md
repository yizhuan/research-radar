# arXiv Trending AI — 2026-09-18

## Headline
Today's latest arXiv AI batch is dominated by practical reliability: how agent harnesses manage context and resources, how retrieval systems preserve state, and how evaluations avoid unsupported claims. The ordering below is inferred from concrete signals in the papers—not an official arXiv popularity ranking.

## Top papers (ranked)

### 1. [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/abs/2609.20804)
- **Abstract:** A controlled study varies planning, action space, and context management across 176 settings and four models on SWE-Bench Verified and Terminal-Bench 2.1.
- **Authors:** Run-Ze Fan, Zihao Zhang, Simin Ma, Yebowen Hu, Shouju Wang, Kaiqiang Song, Fei Liu, Hamed Zamani, Xiaoyang Wang
- **arXiv:** `2609.20804v1` (published 2026-09-17 17:58 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.SE`)
- **Evidence for ranking:** Large controlled ablation (176 matched settings), two coding benchmarks, four models, and a 43-page study; Semantic Scholar citation and influential-citation counts were unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors isolate how context management, planning, and action-space design affect accuracy, trajectory length, and cost instead of treating a coding harness as a monolith.
- **Caveat:** The evidence is limited to the evaluated models, benchmarks, and harness components; the abstract does not establish that the findings generalize to every coding-agent workload.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 2. [Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics](https://arxiv.org/abs/2609.19947)
- **Abstract:** Measurements across retrieval, web-search, and coding agents reveal task-dependent CPU, disk-I/O, and memory bottlenecks and motivate resource-aware scheduling.
- **Authors:** Wonmi Choi, Minuk Park, Zhixiong Niu, Yongqiang Xiong, Chuck Yoo, Gyeongsik Yang
- **arXiv:** `2609.19947v1` (published 2026-09-17 09:20 UTC; categories: `cs.AI`, `cs.PF`)
- **Evidence for ranking:** Covers three representative agent workloads and reports concrete system-level gains—about 5.4× on CPU-sensitive tasks and 32% lower average latency; Semantic Scholar counts unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors propose CPU-aware tool admission and task-aware CPU allocation based on measured resource dynamics.
- **Caveat:** The gains are reported for the paper's workloads and deployment configuration; broader hardware and model combinations remain untested in the abstract.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Efficient inference & systems; Agents & reasoning

### 3. [RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents](https://arxiv.org/abs/2609.20754)
- **Abstract:** RAFT represents historical support cases as stateful chains, retrieves matching intermediate states, and returns the parent-case trajectory for troubleshooting.
- **Authors:** Mingxuan Zhang, Xiaowen Wang, Anupma Sharan, Zhengyi Chen, Chenyu Diana Zhang, Shanshan Yang, Chittibabu Pacharu
- **arXiv:** `2609.20754v1` (published 2026-09-17 17:41 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Accepted to the EMNLP 2026 Industry Track, releases an implementation and benchmark, and reports statistically significant improvements over vanilla RAG and GraphRAG at every case-progress stage; Semantic Scholar counts unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors introduce entry-level retrieval over directed case timelines, with an optional graph linking similar cases.
- **Caveat:** Public multi-stage troubleshooting data is scarce, so the main benchmark is synthetic and the real Jira evaluation is described as directional evidence.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Retrieval & knowledge; Agents & reasoning; Evaluation & benchmarks

### 4. [Perception, Layout, and Validation: Calibrated Confidence for Reliable Straight-Through Processing of Financial Documents](https://arxiv.org/abs/2609.20110)
- **Abstract:** A decomposed confidence score plus conformal risk control improves the reliability and usable coverage of automated financial-document extraction.
- **Authors:** Yichao Jin, Yushuo Wang, Yuxuan Han, Kwan Ching Yee Sonia, Weiyang Song, Chiu Jin-Chun Kent, Wong Chong Hwee, Wong Tiong Kiat, Kenneth Zhu Ke, Jingyuan Zhao
- **arXiv:** `2609.20110v1` (published 2026-09-17 12:09 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Evaluated on three public datasets and two VLM families; reports AUROC of 0.90–0.99 and 49–72% auto-approval at a target error below 10%, versus 0.1–7% for native confidence; Semantic Scholar counts unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors combine perception, layout, and validation signals with conformal risk control for calibrated straight-through processing.
- **Caveat:** The reported coverage and error guarantees are empirical results on the selected datasets and models, not a universal guarantee for document extraction.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Safety & alignment

### 5. [Can Data Attribution Filter Out Subliminal Learning? Not Reliably](https://arxiv.org/abs/2609.20027)
- **Abstract:** An evaluation of three gradient-based data-attribution methods finds partial, inconsistent mitigation of subliminal learning across models and settings.
- **Authors:** Moritz Weckbecker, Sweta Jena, Jonas Müller, Ponnurangam Kumaraguru, Sebastian Lapuschkin, Wojciech Samek, Louis Jaburi, Gonçalo Paulo
- **arXiv:** `2609.20027v1` (published 2026-09-17 10:34 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Directly tests three attribution methods across three models against a strong counterfactual-dependent baseline and reports a safety-relevant negative result; Semantic Scholar counts unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors show that EK-FAC can mitigate a significant part of the effect in some settings, while other methods and sample-level filtering often fall short.
- **Caveat:** Success varies across method/model-preference combinations, and the paper does not identify a consistent explanation for the variation.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Safety & alignment; Training & adaptation; Evaluation & benchmarks

### 6. [Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation](https://arxiv.org/abs/2609.20538)
- **Abstract:** A protocol for closed-loop evaluation separates unsupported claims, operational false admission, and distribution-shift alarms through refusal, decomposition, and reference refresh.
- **Authors:** Peiying Zhu, Sidi Chang
- **arXiv:** `2609.20538v1` (published 2026-09-17 15:09 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Preregistered held-out evaluation with 1,440 cases and 21,600 partition rows, plus an executable reproducibility artifact; Semantic Scholar counts unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors connect observable support, statistical calibration, and justified claims in a claim-safe evaluation contract.
- **Caveat:** The results come from an aggregate-only simulator with specified policy components and demand regimes; external validity is not established by the abstract.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Evaluation & benchmarks; Safety & alignment

### 7. [Tailored to you: longitudinal effects of personalising language models](https://arxiv.org/abs/2609.20077)
- **Abstract:** A five-day, 992-participant study compares baseline, memory-based, and survey-based personalization and measures changes in disclosure, advice-seeking, and regret.
- **Authors:** Canfer Akbulut, Justine Breuch, Arianna Manzini, Lujain Ibrahim, Matija Franklin, Roma Patel, Iason Gabriel, Kristian Lum, Laura Weidinger
- **arXiv:** `2609.20077v1` (published 2026-09-17 11:35 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Large human-subject longitudinal study with 992 participants and two personalization conditions; Semantic Scholar counts unavailable because its API returned HTTP 429.
- **Claimed contribution:** The authors report distinct effects of memory-based and survey-based personalization on self-disclosure, perceived creepiness, and regret about sharing information.
- **Caveat:** The intervention lasted five days, so longer-term behavioral and relational effects remain uncertain.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Safety & alignment; Evaluation & benchmarks

### 8. [Language-model groups overstate consensus when replaying human deliberation on a reasoning task](https://arxiv.org/abs/2609.20543)
- **Abstract:** Replaying 100 human Wason groups with matched LLM groups shows that simulated groups are more consensual and that consensus does not reliably track collective accuracy.
- **Authors:** Tengfei Shao
- **arXiv:** `2609.20543v1` (published 2026-09-17 15:11 UTC; categories: `cs.AI`, `cs.CL`, `cs.CY`, `cs.MA`)
- **Evidence for ranking:** Uses matched human/agent groups, preregistration, code and data, and two sensitivity analyses converging on the same direction; Semantic Scholar counts unavailable because its API returned HTTP 429.
- **Claimed contribution:** The paper provides a scoring-explicit test of whether belief-anchored LLM groups can estimate human deliberative outcomes.
- **Caveat:** The task is a Wason reasoning setting and may not represent deliberation more broadly.
- **Announcement type:** new submission, announcement-batch date 2026-09-18
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Safety & alignment

## Trending Research Themes

- **Agent infrastructure is becoming a first-class research object.** The harness ablations in Fan et al. and resource characterization in Choi et al. treat context, tools, scheduling, and cost—not only model weights—as determinants of agent performance.
- **State and trajectory matter for retrieval and evaluation.** RAFT retrieves intermediate troubleshooting states, while Zhu and Chang argue that closed-loop evaluation must preserve reference support and invalidate stale maps under drift.
- **Reliability is moving from confidence scores to calibrated procedures.** Jin et al. combine interpretable VLM signals with conformal control; the result is a deployment-oriented alternative to verbalized confidence.
- **Human- and model-behavior measurement is under scrutiny.** Shao finds simulated consensus can be inflated and inaccurate, while Akbulut et al. show personalization changes disclosure and regret in ways that depend on the personalization mechanism.
- **Safety work is producing negative results, not only mitigation proposals.** Weckbecker et al. find data attribution helps inconsistently against subliminal learning, making robustness and method selection central open issues.

## Open Problems and Research Directions

- **Transferability of harness findings:** Fan et al.'s controlled component analysis should be repeated across more models, coding environments, context budgets, and repositories to test whether the planning/tool conclusions are stable.
- **Joint agent scheduling:** Choi et al. identify CPU, disk, and memory bottlenecks; a next experiment is a benchmark that jointly varies concurrency, model latency, tool mix, and container placement while reporting cost and tail latency.
- **Real stateful support data:** RAFT's synthetic benchmark and directional Jira result leave a data gap. Building privacy-preserving, multi-stage support corpora would test whether state-level retrieval retains its advantage in production distributions.
- **Calibration under drift:** Jin et al. demonstrate empirical risk control on selected document sets, and Zhu and Chang emphasize reference refresh. A useful follow-up is a shared drift benchmark measuring coverage, residual error, and abstention over time.
- **Reliable attribution for subliminal behavior:** Weckbecker et al. report inconsistent method/model interactions. Controlled studies that vary attribution approximation, token-versus-sample filtering, and teacher access could identify when filtering is trustworthy.
- **External validity of simulated groups:** Shao's Wason-task result motivates replication across tasks, cultures, group sizes, and interaction protocols before using LLM groups as proxies for human deliberation.
- **Long-horizon personalization effects:** Akbulut et al. observed five-day effects. Longer randomized studies should test persistence, reversibility, and effects on offline relationships while minimizing unnecessary collection of sensitive personal data.

## Takeaway
The strongest supported pattern is operational: agent quality increasingly depends on state, context, calibration, resource scheduling, and evaluation design around the model. These papers offer unusually concrete measurements and negative findings, but most are fresh preprints with no reliable citation momentum yet; their results need replication beyond the reported benchmarks, simulators, and short study windows.

## Method and sources

Window: latest daily arXiv announcement batch dated 2026-09-18; snapshot 2026-09-18 15:10 UTC. The current `cs.AI` recent page showed the 18 Sep 2026 batch; the selected records were submitted on 17 Sep and appeared in that latest batch. Core scope: `cs.AI`, with cross-listed AI papers where relevant. arXiv has no official trending chart. Papers were ranked by transparent, inferred momentum signals: controlled evaluation scale, benchmark breadth, concrete reported results, released code/data/artifacts, conference acceptance, and cross-list relevance. Semantic Scholar corroboration was attempted for all selected arXiv IDs, but the API returned HTTP 429, so no citation counts are asserted.

Primary sources: the arXiv recent listing at https://arxiv.org/list/cs.AI/recent and each linked arXiv abstract page above. No paper is described as most read or most downloaded.
