# arXiv AI papers — latest announcement batch, 11 November 2026

The latest batch spans the configured AI corpus (cs.AI, cs.LG/stat.ML, cs.CL, cs.CV, cs.RO, cs.NE, cs.MA). This selection covers 8 notable papers from 387 unique new submissions in the batch. The strongest recurring pattern is evaluation becoming more diagnostic: papers inspect how agents search, fail, or saturate rather than reporting only final task scores. I’ll cover agent evaluation and workflow compilation first, then training-time guidance, embodied AI, and low-latency speech. arXiv has no official trending chart; this ordering is inferred, with little citation evidence available for papers announced today, so this is a notable-paper selection rather than a measured popularity ranking.

## Top papers (ranked)

### 1. [Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](https://arxiv.org/abs/2611.14514)
- **Abstract:** The paper replaces testing a single hypothesis against its negation with mutually exclusive competing explanations, so evidence can identify an alternative as well as reject a claim.
- **Authors:** Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
- **arXiv:** `2611.14514v1` (published 2026-11-10 18:58:43 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Listed on the official ICML 2026 program page and cross-listed across three configured AI categories; its reported six-domain evaluation gives this paper the strongest independently checkable research signal in this very recent batch. No citation totals are used.
- **Claimed contribution:** The authors report that contrast sets resolved 67% more questions than pointwise surprisal under the same experiment budget; a blinded study of 38 experts agreed with the selected explanation on 78% of resolved questions.
- **Caveat:** The experiments use observational tabular data and one GPT-4o-based agent; “resolution” relies on LLM-elicited beliefs, and the authors note that such findings are statistical rather than causal.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Data & synthetic data

### 2. [One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge](https://arxiv.org/abs/2611.14432)
- **Abstract:** The authors describe a single vision-language-action checkpoint for 100 long-horizon household tasks in OmniGibson, report ninth place in the 2026 BEHAVIOR Challenge, and combine the learned policy with a coding agent on a subset of tasks.
- **Authors:** Ilia Larchenko, Gleb Zarin, Atindra Nair, Keerti Manney, Vitaly Kleban et al.
- **arXiv:** `2611.14432v1` (published 2026-11-10 18:06:16 UTC; categories: `cs.RO`, `cs.AI`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The paper reports a 9th-place result in the 2026 BEHAVIOR Challenge, whose public leaderboard provides an external competition context; it is cross-listed in four configured categories. The result is a benchmark signal, not readership evidence.
- **Claimed contribution:** The authors report one VLA checkpoint across 100 simulated household tasks, with Q=0.392 over all tasks; their public submission, which includes part of the coding-agent results on 14 tasks, scores Q=0.446 and 27.3% full-task success.
- **Caveat:** The results are from the OmniGibson simulator; the paper says the public submission included only part of the coding-agent results, so the reported agent and learned-policy figures are not a like-for-like full-task comparison.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Robotics & control; Multimodal & vision-language; Agents & reasoning

### 3. [Earlybird: Predictive Streaming Speech Recognition in 29M Parameters](https://arxiv.org/abs/2611.14421)
- **Abstract:** Earlybird is a 29M-parameter streaming recognizer trained to predict words from partial speech, with the authors reporting a median correct word prediction 90 ms before it ends on LibriSpeech test-clean.
- **Authors:** Sahil Mahendrakar
- **arXiv:** `2611.14421v1` (published 2026-11-10 17:59:28 UTC; categories: `cs.SD`, `cs.CL`, `eess.AS`)
- **Evidence for ranking:** The paper has a public Hugging Face model page and a Product Hunt listing, alongside reported comparisons on six timed test sets and eight English Open ASR Leaderboard sets. These are checkable release/discovery signals, not citation or readership counts.
- **Claimed contribution:** The authors report correct prediction of the median LibriSpeech test-clean word 90 ms before completion, earlier than the compared streaming models, and roughly ties a same-size competitor on English ASR accuracy.
- **Caveat:** Evaluation is English-only in the reported benchmarks; the abstract does not establish performance for other languages or noisy, real-world conversational conditions.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Efficient inference & systems; Multimodal & vision-language; Evaluation & benchmarks

### 4. [ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492)
- **Abstract:** ReTrace converts an SOP and a few logged agent runs into a reusable code-driven workflow that replaces per-step LLM planning, reporting lower latency and cost with some task-success trade-offs.
- **Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta et al.
- **arXiv:** `2611.14492v1` (published 2026-11-10 18:49:47 UTC; categories: `cs.AI`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Cross-listed in three configured categories and supported by evaluations on 79 production procedures, τ²-Bench, and SOP-Bench; several paper-discovery sources surfaced the work. The rank reflects methodological relevance, not a verified citation trend.
- **Claimed contribution:** The authors report 93.8% completion versus 96.8% for the agent on 79 procedures at 24% lower cost, and 75.8% success on τ²-Bench with 1.3-second execution versus 170 seconds for the agent.
- **Caveat:** The authors state that extracted reasoning may not reflect why an agent acted, tests concern new inputs to the same procedures rather than transfer to new procedures, and enterprise completion can be misreported by the platform.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 5. [Agent Benchmarks Stop Ranking Before They Run Out of Tasks](https://arxiv.org/abs/2611.13541)
- **Abstract:** Re-scoring eight agent benchmarks, the paper argues that pass/fail scoring can hide meaningful differences between agents and proposes anchored graded scores with cost tracked separately.
- **Authors:** Zihan Dong, Qishi Zhan, Minxuan Hu
- **arXiv:** `2611.13541v1` (published 2026-11-10 04:03:04 UTC; categories: `cs.AI`)
- **Evidence for ranking:** It analyzes released runs from eight established benchmarks, including SWE-bench Verified and Terminal-Bench, and was independently indexed with its abstract and PDF. Its relevance is strong, but no citation or readership signal was available.
- **Claimed contribution:** The authors report that pass/fail ties can conceal more than tenfold differences in a Terminal-Bench re-run and propose a clipped log-ratio score with dated anchors and a separate cost axis.
- **Caveat:** The authors qualify several results: the sliding-window finding rests on ALE-Bench with partly reconstructed dates, and the aggregate separation in their re-run is borderline across three trials.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 6. [AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](https://arxiv.org/abs/2611.14515)
- **Abstract:** AutoScaffold uses a frozen teacher to diagnose a student model’s RL training experience and adapt temporary strategies or hints, which are removed at evaluation.
- **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt et al.
- **arXiv:** `2611.14515v1` (published 2026-11-10 18:58:46 UTC; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** Cross-listed in two configured categories; the authors report results across four settings—ALFWorld, search-based QA, math reasoning, and GPU kernel generation. The paper was surfaced by independent research-indexing pages, though this is weaker than citation evidence.
- **Claimed contribution:** The authors report improvements over the corresponding RL baselines in all four domains under scaffold-free evaluation, including +7.2 points in ALFWorld success and +4.0 points in average QA exact match.
- **Caveat:** The evidence comes from four task domains and specific student/teacher setups; wider transfer and the cost of repeated teacher interventions remain unestablished here.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Training & adaptation; Agents & reasoning

### 7. [Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game](https://arxiv.org/abs/2611.14487)
- **Abstract:** Re-Search tests research ideation as a Twenty Questions-style game over 200 ICML 2026 papers and finds that most of six tested LLMs make little progress after roughly 30 of 100 questions.
- **Authors:** Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi, Kuan-Hao Huang
- **arXiv:** `2611.14487v1` (published 2026-11-10 18:47:22 UTC; categories: `cs.AI`)
- **Evidence for ranking:** The paper evaluates six models on 200 recent conference papers and its report is surfaced in multiple paper-discovery indexes. It is a focused evaluation contribution; no citation velocity is claimed.
- **Claimed contribution:** The authors’ controlled tests suggest candidate generation, rather than judging, is a bottleneck: weaker models improve when given externally proposed questions or a richer hypothesis space.
- **Caveat:** The testbed is 200 machine-learning papers from ICML 2026; recovery scores and search-tree annotations rely on LLM judges, and the authors say errors and possible self-preference cannot be fully ruled out.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 8. [Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](https://arxiv.org/abs/2611.14493)
- **Abstract:** The authors compare three evaluation frameworks on two analytics agents and report that trace-based judging balances precision and recall better than text-only judging, while functional testing and red-teaming expose different failures.
- **Authors:** Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao
- **arXiv:** `2611.14493v1` (published 2026-11-10 18:50:06 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.SE`)
- **Evidence for ranking:** Cross-listed across three configured AI categories plus software engineering; the study reports stability checks, 72 known-risk cases, and 24 newly discovered failures. This is a relevant evaluation signal, not a popularity signal.
- **Claimed contribution:** In the authors’ controlled setting, trace-based evaluation reaches F1=0.90 on known risks, text-only evaluation produces five times more false alarms, and functional testing and security red-teaming find disjoint novel failures.
- **Caveat:** The study uses frozen traces from only two analytics agents, so it does not establish the same framework ordering for live agents or other task domains.
- **Announcement type:** new submission, 11 November 2026 announcement batch
- **Themes:** Evaluation & benchmarks; Safety & alignment; Agents & reasoning

## Trending Research Themes

- **Evaluation is shifting from scalar scores toward diagnosis.** Agent Benchmarks Stop Ranking Before They Run Out of Tasks challenges binary pass/fail saturation; the enterprise-framework comparison measures stability, false alarms, and failure discovery; Re-Search probes the step-by-step ideation process; Contrastive Discovery measures whether evidence resolves alternatives. These papers share a measurement direction, not a single new benchmark method.
- **Agent workflows are being made more structured.** ReTrace compiles repeated SOP runs into code-selected paths, while AutoScaffold adapts training guidance from observed failures. Both replace some open-ended decision-making with reusable structure, but one changes inference-time execution and the other training-time learning.
- **Scientific and research agents need better candidate generation.** Contrastive Discovery represents competing explanations explicitly, and Re-Search finds that supplying candidate ideas/questions can help models that otherwise struggle to generate them. This is an intersection of hypothesis management and search support, not evidence that autonomous discovery is solved.
- **Embodied and speech systems show isolated deployment-oriented signals.** The BEHAVIOR entry targets one checkpoint across many simulated household tasks; Earlybird targets earlier speech output in a small recognizer. They are noteworthy single-paper results, not enough to claim a corpus-wide robotics or speech shift.
- **Category mix:** Of the 387 unique papers dated in this batch, cs.LG had the largest primary-category count (91), followed by cs.CV (82) and cs.AI (54); the rest span other core and cross-listed areas. This is a batch-level concentration, not a popularity ranking.

## Open Problems and Research Directions

- **Test whether the scientific-discovery gains generalize.** Authors of Contrastive Discovery limit their experiments to observational tabular data and one GPT-4o-based agent; Re-Search uses ICML machine-learning papers and LLM-based scoring. A useful follow-up is to replicate with other agent backbones, domains, and independent belief/judging procedures, including tests where causal claims are required. (Contrastive Discovery; Re-Search)
- **Make agent benchmarks statistically robust and harder to game.** Agent Benchmarks Stop Ranking Before They Run Out of Tasks notes benchmark-specific uncertainty and borderline separation in a three-trial re-run. Replicate with more trials and independently audited objective metrics, then test whether graded scores remain discriminative without creating new reward-gaming incentives. (Agent Benchmarks Stop Ranking Before They Run Out of Tasks)
- **Measure workflow transfer and drift.** ReTrace evaluates new inputs to known procedures, not transfer to unseen procedures, and points out that unreliable reasoning traces and SOP/tool changes can invalidate workflows. Test branch-covering trace selection, audited outcomes, and workflow repair after controlled procedure changes. (ReTrace)
- **Account for evaluation-harness deployment conditions.** The enterprise evaluation study uses frozen traces from two agents. Replicate on more agents, live tool failures, and longer-tail workflows, checking whether trace access improves precision without destabilizing automated gating. (Comparative Analysis of Agent Evaluation Frameworks)
- **Quantify the cost and transfer of adaptive scaffolding.** AutoScaffold reports four task settings but leaves the broader teacher-intervention cost and generality unsettled. Report teacher tokens/compute and compare adaptive scaffolds against equally budgeted fixed, human-written, and no-teacher baselines on new task families. (AutoScaffold)
- **Test real-world robustness beyond simulation and clean English.** The household-task paper is evaluated in OmniGibson, while Earlybird’s reported benchmarks are English. Follow-up work could measure real-robot transfer and multilingual/noisy streaming speech, including latency, calibration, and failure recovery. (One Policy for 100 Household Tasks; Earlybird)

## Takeaway

The clearest common thread is a move toward exposing and improving the process behind agent performance: how ideas are generated, how benchmarks fail to distinguish systems, and when workflow or training structure can reduce unnecessary model decisions. The evidence is preliminary and uneven—some results have independent conference or leaderboard context, but citation counts are not informative at this age and several studies are narrow or simulator-based.

## Method and sources

- **Window:** daily; announcement-date range 2026-11-11 through 2026-11-11 (the latest arXiv announcement batch). The selected records carry arXiv submission timestamps on 10 November 2026 (UTC); this is the latest batch visible on the arXiv recent-category pages at the snapshot. The previous-batch fallback was not needed.
- **Snapshot:** 2026-11-11 17:05:12 UTC.
- **Core category query:** `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA` using the arXiv API sorted by submitted date descending. The latest batch yielded 387 unique records; the eight selected records were individually checked against their arXiv abstract pages. All eight are new v1 submissions, not revisions.
- **Inference:** arXiv provides no official trending ranking. The order uses checkable conference/competition/release context and cross-list breadth first, then the specificity of the evaluation evidence and recency. This is an inferred notable-paper ranking; no downloads, views, or period citation gains are claimed. Semantic Scholar citation metadata could not be obtained for this snapshot, so no citation counts or citation velocity are asserted.
- **arXiv sources:** [2611.14514](https://arxiv.org/abs/2611.14514), [2611.14432](https://arxiv.org/abs/2611.14432), [2611.14421](https://arxiv.org/abs/2611.14421), [2611.14492](https://arxiv.org/abs/2611.14492), [2611.13541](https://arxiv.org/abs/2611.13541), [2611.14515](https://arxiv.org/abs/2611.14515), [2611.14487](https://arxiv.org/abs/2611.14487), [2611.14493](https://arxiv.org/abs/2611.14493).
- **Corroborating sources:** [ICML 2026 page for Contrastive Discovery](https://icml.cc/virtual/2026/67941); [BEHAVIOR 2026 challenge](https://behavior.stanford.edu/challenge/index.html) and [public leaderboard](https://huggingface.co/spaces/behavior-1k/2026-challenge-leaderboard); [Earlybird Hugging Face model page](https://huggingface.co/sahilmahendrakar/Earlybird-29M) and [Product Hunt listing](https://www.producthunt.com/products/earlybird-5).