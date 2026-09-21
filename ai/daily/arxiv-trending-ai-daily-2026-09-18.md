# arXiv Trending AI — 2026-09-18 announcement batch

The strongest signal in this batch is a move from better standalone models toward operationally grounded agents: executable training environments, cross-domain visual interaction, persistent procedural memory, and workflow-level evaluation. arXiv publishes no official trending chart; this is an inferred ranking based on recency, cross-list relevance, reported evaluation scale/results, and corroborating discovery signals. Citation counts are too sparse to establish popularity for papers submitted in this batch.

## Top papers (ranked)

### 1. [CodeMidas: Scaling Agentic Coding RL Environments from Code Itself](https://arxiv.org/abs/2609.22068)
- **Abstract:** CodeMidas turns implemented functionality in existing codebases into executable reinforcement-learning environments using source code as the only task-specific input, producing 5,545 tasks from 3,185 codebases across 23 languages and 15 domains.
- **Authors:** Bowen Ye, Lei Li, Shicheng Li, Zihao Yue, Linghao Zhang, et al.
- **arXiv:** `2609.22068v1` (published 2026-09-18 17:55:17 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Submitted in the latest batch; cross-domain agentic-RL relevance; the abstract reports improvements on five coding benchmarks, including +11.7% on DeepSWE, +17% on ProgramBench, and +8.5% on Terminal-Bench v2.1; independently surfaced by Papers with Code and the DailyArXiv issue for the batch. Semantic Scholar metrics were unavailable after a rate-limit response.
- **Claimed contribution:** The authors propose an agentic pipeline that explores code, writes execution-grounded specifications and tests, then validates tasks through repeated solution rollouts.
- **Caveat:** The reported gains depend on the generated task and verifier pipeline; the abstract does not establish how performance transfers beyond the five evaluated benchmarks.
- **Announcement type:** new submission, 2026-09-18 announcement batch
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 2. [MintAct: A Unified Visual Agent for Digital Environments](https://arxiv.org/abs/2609.22083)
- **Abstract:** MintAct is a 2B/4B/8B family of vision-language models that unifies UI grounding, multi-step navigation across mobile, desktop, and web, and visual tool use through scalable environments and asynchronous reinforcement learning.
- **Authors:** Mingfei Gao, Rui Tian, Haiming Gang, Bohan Zhai, Le Zhang, et al.
- **arXiv:** `2609.22083v1` (published 2026-09-18 17:59:34 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Submitted in the latest batch; unusually broad cross-domain agent scope; the abstract reports 48.9 on OSWorld-Verified and specialist-matching performance across several benchmarks; independently listed in the DailyArXiv batch issue. Semantic Scholar metrics were unavailable after a rate-limit response.
- **Claimed contribution:** The authors present a unified visual-agent family and an infrastructure recipe for concurrent environment hosting, trajectory collection, and online RL under noisy feedback and off-policy drift.
- **Caveat:** The abstract gives aggregate benchmark claims but does not expose per-domain trade-offs or robustness under distribution shift.
- **Announcement type:** new submission, 2026-09-18 announcement batch
- **Themes:** Agents & reasoning; Multimodal & vision-language; Training & adaptation

### 3. [TrialAtlas: Multi-Agent Research Organization for Clinical Trial Design and Optimization](https://arxiv.org/abs/2609.21859)
- **Abstract:** TrialAtlas coordinates specialized agents for literature synthesis, competitive-trial intelligence, regulatory precedent analysis, and integrated reasoning, evaluated on a benchmark built from 291 FDA Complete Response Letters.
- **Authors:** Jiacheng Lin, Zifeng Wang, Zheng Chen, Erick Scott, Ziwei Yang, et al.
- **arXiv:** `2609.21859v1` (published 2026-09-18 14:53:34 UTC; categories: `cs.CL`)
- **Evidence for ranking:** Submitted in the latest batch; strong real-world workflow relevance and a domain-specific benchmark; the abstract reports 50.0% F1 for deficiency detection and 85.3% balanced accuracy for technical/regulatory-success prediction; independent technical coverage appeared on Pith and the arXiv HTML page was surfaced in search. Semantic Scholar metrics were unavailable after a rate-limit response.
- **Claimed contribution:** The authors combine a memory-augmented multi-agent organization with historical trial and regulatory outcomes, and introduce TrialAtlasBench.
- **Caveat:** Expert judgments and benchmark results are from a specialized clinical setting; they do not show that the organization generalizes to other regulated decision workflows.
- **Announcement type:** new submission, 2026-09-18 announcement batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Evaluation & benchmarks

### 4. [Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design](https://arxiv.org/abs/2609.22086)
- **Abstract:** Designer-RSI continually grows and revises an external procedural-memory bank for a frozen frontier model operating professional design software through more than 230 tools, using replay-gated experience rather than weight updates or human labels.
- **Authors:** Hongyang Du, Lan Yan, Christian Flores, Asim Kadav
- **arXiv:** `2609.22086v1` (published 2026-09-18 17:59:56 UTC; categories: `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Latest-batch recency, two-category relevance, and unusually large reported evaluation (1,406 briefs and 1,869 trajectories); the abstract reports GenEval2 execution success rising from 72.7% to 99.3% and a 58.5% held-out win rate for combined memory widening/deepening. Semantic Scholar returned 0 citations and 0 influential citations at snapshot time, with 62 references.
- **Claimed contribution:** The authors introduce procedural-memory widening and deepening with a matched replay gate that admits changes only when they repair failures without regressing observed successes.
- **Caveat:** The evidence is concentrated on professional graphic-design tasks and an external memory bank; the abstract does not establish transfer to unrelated software domains.
- **Announcement type:** new submission, 2026-09-18 announcement batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Training & adaptation

### 5. [EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise](https://arxiv.org/abs/2609.21841)
- **Abstract:** EnterpriseVal specifies use cases, metrics, calibrated grading, confidence-aware decision gates, and value/risk models for deciding whether a generative-AI workflow should be rejected, conditionally deployed, or scaled.
- **Authors:** Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid
- **arXiv:** `2609.21841v1` (published 2026-09-18 14:39:26 UTC; categories: `cs.AI`, `stat.ML`)
- **Evidence for ranking:** Latest-batch recency; cross-listing into AI and statistical ML; direct deployment relevance; the abstract reports a three-workflow global-bank pilot including 88% citation precision and 1.6% hallucination for the best credit-memo model, plus a reduction in estimated procedure-transformation effort from 27.4 to 2.9 hours. Semantic Scholar metrics were unavailable after a rate-limit response.
- **Claimed contribution:** The authors propose an executable evaluation-and-gating system that freezes the socio-technical configuration under test and combines expert judgment with calibrated LLM judging.
- **Caveat:** The abstract explicitly separates pilot evidence from proposed components and open hypotheses; a three-workflow pilot is not evidence of general enterprise validity.
- **Announcement type:** new submission, 2026-09-18 announcement batch
- **Themes:** Evaluation & benchmarks; Safety & alignment; Agents & reasoning

## Trending Research Themes

- **Agent systems are becoming infrastructure problems.** CodeMidas focuses on generating reliable RL environments from code; MintAct focuses on scalable heterogeneous environments and asynchronous training; Designer-RSI focuses on external procedural memory rather than parameter updates.
- **Evaluation is moving closer to deployment conditions.** TrialAtlas uses FDA response letters and expert review, while EnterpriseVal evaluates frozen workflows with human oversight, reliability, value, and risk gates rather than model-only benchmark scores.
- **External memory and executable feedback are recurring adaptation mechanisms.** Designer-RSI revises procedural skills from successes and failures; CodeMidas uses executable tests and repeated rollouts as task validation; TrialAtlas uses historical regulatory memory.
- **Multimodal agents are broadening beyond chat.** MintAct covers mobile, desktop, and web interaction, while Designer-RSI targets complex editable artifacts in professional software.

## Open Problems and Research Directions

- **Generalization of generated training environments (CodeMidas):** Test whether source-derived tasks remain reliable when codebases, languages, and verifier styles are held out by project family rather than randomly split.
- **Robustness under feedback and distribution shift (MintAct, Designer-RSI):** Evaluate visual agents and procedural memories on unseen interfaces, tool failures, ambiguous goals, and adversarially changed software states.
- **Memory safety and regression control (Designer-RSI):** Measure long-term memory contamination, skill interference, and replay-gate false acceptance over substantially longer deployment histories.
- **Validity of workflow-level gates (EnterpriseVal, TrialAtlas):** Replicate the proposed decision thresholds across organizations and domains, and compare calibrated LLM judging against blinded expert panels with prospective outcomes.
- **Human oversight and accountability (TrialAtlas, EnterpriseVal):** Quantify when specialized multi-agent decomposition improves decisions rather than merely increasing cost, latency, or apparent explanation detail.

## Takeaway

This batch is less about a single new model architecture than about making agents trainable, adaptable, and auditable in concrete environments. The most consequential ideas are executable feedback loops, external procedural or domain memory, and evaluations tied to real workflows. The evidence is still preliminary: all five are new submissions, citation-based momentum is effectively unavailable, and several headline results are author-reported pilot or benchmark claims.

## Method and sources

- **Window:** 2026-09-18 announcement batch, used for the daily report because it is the most recent batch available at the 2026-09-21 15:10 UTC snapshot.
- **Scope:** arXiv `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; candidates were filtered for clear AI relevance and deduplicated by versionless arXiv ID.
- **Ranking:** inferred, not an official arXiv ranking. Signals were recency, AI cross-list relevance, reported evaluation scale/results, and corroborating discovery coverage. Semantic Scholar was queried for the selected IDs; one paper returned 0 citations/0 influential citations and later requests were rate-limited, so citation evidence is explicitly sparse.
- **Primary sources:** the five linked arXiv abstract pages. Corroboration: [DailyArXiv batch issue](https://github.com/Ponkux/DailyArXiv-cp/issues/570), [Pith coverage of TrialAtlas](https://pith.science/paper/2609.21859), and [Papers with Code entry for CodeMidas](https://paperswithcode.co/paper/2609.22068).
- **Snapshot:** 2026-09-21 15:10 UTC.
