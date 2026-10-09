# arXiv AI weekly | 2–9 October 2026 | 8 notable papers

The clearest pattern this week is a push to make agent systems more efficient and auditable, alongside sharper tests of what their reasoning and memory actually buy. In this brief: agent advisors and programmatic control, model compression, and the evaluation gaps behind claimed gains. This is an inferred shortlist, not an official arXiv trend ranking: arXiv has no trending chart, and papers this recent have little usable citation evidence.

## Top papers (ranked)

### 1. [Training Advisors for LLM Agents from Task Outcomes](https://arxiv.org/abs/2610.09858)
- **Abstract:** Caddie trains a language-model critic with reinforcement learning from final task success, and the authors report that its advice improves several agents and interactive benchmarks without step-level labels or reference critiques.
- **Authors:** Sergei Polezhaev, Barys Liskavets, Ori Press, Alexander Golubev
- **arXiv:** `2610.09858v1` (published 2026-10-07 11:14:26 UTC; categories: `cs.CL`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Cross-listed in three core AI categories; indexed independently by several paper-discovery services; the abstract reports transfer to three base models not used in critic training and gains on out-of-domain interactive tasks.
- **Claimed contribution:** The authors introduce outcome-trained natural-language advice for an agent during execution, updating the critic while keeping the base agent frozen.
- **Caveat:** Reported transfer starts from one Qwen3-4B critic-training setup; performance beyond the tested agents, benchmarks, and critic invocation protocols remains unestablished.
- **Announcement type:** new submission, 2026-10-07
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 2. [CurveTQ: Rotation-Free Trellis Quantization of LLM Weights via Curvature-Weighted Search](https://arxiv.org/abs/2610.09212)
- **Abstract:** CurveTQ uses Hessian-curvature weights in trellis search to quantize model weights without the rotations used by competing two-bit methods; the authors report higher accuracy than QTIP and Proteus on their tested models and faster decoding.
- **Authors:** Guanhua Ding, Zi Wang, Ruichao Li, Jack Liu
- **arXiv:** `2610.09212v1` (published 2026-10-06 23:14:06 UTC; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** Cross-listed in machine learning and AI; provides directly comparable two-bit results across three 4–8B instruction models and one 35B MoE, plus decoding-speed measurements.
- **Claimed contribution:** The authors incorporate diagonal Hessian information into Viterbi branch costs and use a native-basis codec to avoid decoding-time rotations.
- **Caveat:** The reported evidence covers a limited set of model families and bit-widths; the claimed accuracy and speed advantages need replication under broader hardware and workload conditions.
- **Announcement type:** new submission, 2026-10-06
- **Themes:** Efficient inference & systems; Training & adaptation

### 3. [Noise Your Prompt: Noising Conditioning Tokens in Continuous Diffusion Language Models](https://arxiv.org/abs/2610.09145)
- **Abstract:** The paper adds noise to conditioning tokens during training of continuous diffusion language models; the author reports improved results on Sudoku, N-Queens, and Gigaword summarization, but not open-ended dialogue.
- **Authors:** Justin Jung
- **arXiv:** `2610.09145v2` (published 2026-10-06 21:38:52 UTC; revised 2026-10-08 06:22:59 UTC; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** The paper has a TMLR journal reference and a v2 revision during the window; it tests a low-cost training-objective change across reasoning and language-generation tasks.
- **Claimed contribution:** The author reports that noising the prompt improves harder Sudoku solve rates and N-Queens solution coverage, with no default inference-cost increase.
- **Caveat:** The author explicitly reports no gains for open-ended dialogue; positive results are task-dependent and include modest-data summarization settings.
- **Announcement type:** revision, 2026-10-08
- **Themes:** Training & adaptation; Evaluation & benchmarks

### 4. [Agent Behavior as Code: Efficient and Robust LLM Agents with Programmatic Specifications](https://arxiv.org/abs/2610.04824)
- **Abstract:** ABCAgent turns reusable agent behavior into editable programs, which the authors report can improve robustness and reduce cost or latency on selected benchmarks compared with model-matched neural agents.
- **Authors:** Peng Qi, Chunliang Lyu, Gang Li, Fabian Chan, Cheng Chang, et al.
- **arXiv:** `2610.04824v1` (published 2026-10-04 00:14:33 UTC; categories: `cs.AI`, `cs.CL`, `cs.MA`)
- **Evidence for ranking:** Cross-listed in AI, language, and multiagent systems; evaluated on six benchmarks, including two constructed to test task-variant generalization; reports cost and latency comparisons as well as task outcomes.
- **Claimed contribution:** The authors use a symbolic program to specify agent behavior at runtime, with a foundation-model agent editing the program when flexibility is needed.
- **Caveat:** Strong results are benchmark- and task-family-specific; the authors' evaluation does not establish that programmatic specifications generalize to arbitrary open-ended tasks.
- **Announcement type:** new submission, 2026-10-04
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 5. [Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell](https://arxiv.org/abs/2610.07782)
- **Abstract:** In a three-tier agent setup, the authors measure lower peak KV-cache use from decomposing long-context inference, but find no detectable accuracy change from persistent reasoning-trace memory on their single-question benchmarks.
- **Authors:** Hochan Son, Kyungdoe Han, Jaehan Koh, Xiaowu Dai, Wenlu Xu, Guang Cheng
- **arXiv:** `2610.07782v1` (published 2026-10-06 05:17:44 UTC; categories: `cs.AI`, `cs.CL`, `cs.DC`, `cs.LG`)
- **Evidence for ranking:** Broad four-category cross-listing, acceptance as a NeurIPS 2026 Machine Learning for Systems Workshop poster, and independent indexing; the paper reports controlled memory and cache measurements rather than only an accuracy ablation.
- **Claimed contribution:** The authors specify conditions and detection procedures for meaningful agent-memory ablations, and report that their benchmark setup gives stored traces nothing informative to retrieve.
- **Caveat:** The null accuracy result is limited to one three-tier architecture and single-question datasets; it does not show persistent memory is useless for tasks that require accumulated cross-task evidence.
- **Announcement type:** new submission, 2026-10-06
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 6. [How RL Reshapes LLM Reasoning: Transferability, Coverage, and Scaling Laws](https://arxiv.org/abs/2610.04158)
- **Abstract:** Across Qwen and Gemma models, the authors analyze how reinforcement learning changes reasoning strategies, cross-domain transfer, and solution coverage, and develop a two-stage strategy-selection model with scaling-law analyses.
- **Authors:** Ziheng Cheng, Yixiao Huang, Hanlin Zhu, Somayeh Sojoudi
- **arXiv:** `2610.04158v1` (published 2026-10-03 00:01:36 UTC; categories: `cs.LG`, `cs.AI`, `stat.ML`)
- **Evidence for ranking:** Spans three core AI/ML categories and combines experiments across two model families with a formal account of why RL can improve some tasks while reducing coverage on others.
- **Claimed contribution:** The authors argue that RL can reweight existing reasoning strategies—altering performance and coverage without necessarily expanding strategy support—and analyze compute-scaling behavior.
- **Caveat:** The empirical scope is Qwen and Gemma families; the theoretical conclusions depend on the paper's two-stage strategy-selection abstraction.
- **Announcement type:** new submission, 2026-10-03
- **Themes:** Training & adaptation; Evaluation & benchmarks; Agents & reasoning

### 7. [PsyCIDRA: A Dual-Agent Framework for Psychiatric Interviewing and Diagnostic Reasoning](https://arxiv.org/abs/2610.07473)
- **Abstract:** PsyCIDRA separates an interactive psychiatric interviewer from a diagnostic-reasoning agent; the authors report improved agreement over direct prompting on simulated cases and a blinded study with human participants.
- **Authors:** Milad Mohammadi, Fatemeh Akrami Shamsabadi, Zahra Mohseni, Amirhossein Safdarian, Malekfarhad Malek, et al.
- **arXiv:** `2610.07473v1` (published 2026-10-05 22:40:24 UTC; categories: `cs.AI`)
- **Evidence for ranking:** A timely, domain-specific AI-agent study with explicit evaluation of interviewing, diagnostic reasoning, and safety; the abstract reports 53 simulated evaluation cases, 81 held-out simulated cases, and 101 human participants in separate arms.
- **Claimed contribution:** The authors combine tool-supported interviewing, working notes, expert-written skills, and ICD-11 retrieval with a separate evidence-reporting diagnostic agent.
- **Caveat:** Patient profiles are simulated and the human-participant study is not evidence of improved real-world clinical outcomes or readiness for clinical deployment.
- **Announcement type:** new submission, 2026-10-05
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Safety & alignment

### 8. [Shared and structured inputs undermine collective random choice by reasoning AI agents](https://arxiv.org/abs/2610.09667)
- **Abstract:** Behavioral tests across reasoning models find that identifier patterns can make supposedly random agent choices biased or correlated, while explicit instructions to randomize reduce but do not eliminate the effect.
- **Authors:** Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari
- **arXiv:** `2610.09667v1` (published 2026-10-07 08:32:36 UTC; categories: `cs.AI`, `physics.soc-ph`)
- **Evidence for ranking:** A cross-disciplinary test of a concrete agent-oversight failure mode; Semantic Scholar listed 0 citations at the snapshot, so no citation momentum supports its position.
- **Claimed contribution:** The authors show that selection rates alone can miss input-dependent bias, correlation, and predictability in model-based random selection.
- **Caveat:** Results are behavioral tests on a small set of models and specified identifiers; the abstract does not establish prevalence in deployed allocation or audit systems.
- **Announcement type:** new submission, 2026-10-07
- **Themes:** Safety & alignment; Evaluation & benchmarks

## Trending Research Themes

- **Agent design is shifting from one monolithic policy toward explicit components.** Caddie adds a learned advisor, ABCAgent externalizes repeatable behavior into programs, PsyCIDRA separates interviewing from diagnosis, and Persistent Memory measures memory as a distinct system tier. These are different design choices, not evidence of one winning architecture.
- **Efficiency is being treated as an algorithmic objective, not just a hardware problem.** CurveTQ targets weight storage and decode work; Persistent Memory measures peak KV-cache use; ABCAgent reports latency and cost; Noise Your Prompt changes training to improve selected tasks without extra default inference work.
- **Evaluation quality and scope are central to the claims.** Persistent Memory shows how benchmark structure can make memory uninformative; the RL study separates pass-at-one gains from broader solution coverage; PsyCIDRA distinguishes simulated cases from a human-participant comparison; the random-choice study measures bias that aggregate selection rates can conceal.
- **A smaller methodological signal is more robust training through harder or more varied inputs.** Noise Your Prompt corrupts conditioning tokens, while the RL paper studies shifts in strategy selection. The connection is conceptual; the papers do not test a shared method.

## Open Problems and Research Directions

- **Test whether learned advice transfers beyond the critic's training regime.** Caddie reports cross-model and out-of-domain gains; follow-up work could reproduce the results with independently trained critics, broader agent/environment families, and controlled critic-call budgets.
- **Make memory benchmarks require memory.** Persistent Memory argues that isolated single-question items can leave stored traces with nothing useful to retrieve. Build multi-stage tasks where evidence must persist across questions, and report cache cost, accuracy, reset behavior, and confidence intervals together.
- **Stress-test efficiency and generalization across deployment conditions.** CurveTQ's gains are measured on a limited model set, while ABCAgent's cost advantages come from selected task families. Replicate under diverse model sizes, hardware, batch sizes, long-horizon tasks, and held-out task variants.
- **Map when prompt noising helps.** Noise Your Prompt reports no transfer to open-ended dialogue. Test more model scales, data regimes, and generation objectives, with preregistered ablations separating robustness to corrupted context from changes in the learned output distribution.
- **Measure strategy coverage and randomization under realistic use.** The RL paper reports that coverage can move differently from pass-at-one; the random-choice paper finds identifier-dependent selection. Future evaluations should sample larger task and identifier spaces and test whether mitigations hold under distribution shift.
- **Keep clinical-agent evidence distinct from clinical effectiveness.** PsyCIDRA's simulated profiles and participant comparison motivate prospective, clinician-supervised evaluation with realistic cases, calibrated abstention, and explicit harm analysis before any deployment claim.

## Takeaway

This week's most useful thread is not a single new agent recipe, but a stronger emphasis on making agent components measurable: advice, memory, executable behavior, and safety properties all need task-appropriate tests. Several papers report promising gains, but the evidence is early and benchmark-bound; follow-up replication and broader evaluation should matter more than headline percentages.

## Method and sources

- **Window:** 2026-10-02 01:13:10 UTC through 2026-10-09 01:13:10 UTC; weekly scope includes new submissions in that interval and revisions dated within it. Snapshot: 2026-10-09 01:13:10 UTC.
- **Corpus sought:** `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`, plus unambiguous AI cross-lists. Candidate discovery used date-focused web searches and official arXiv abstract pages. The bulk arXiv query did not complete, so this is a selected shortlist rather than a comprehensive scan of every category.
- **Ranking:** Inferred from visible cross-list breadth, independent paper indexing or discussion where found, publication/workshop/revision signals, and the specificity of reported evaluation. No numeric trend score is used. Semantic Scholar returned 0 citations for 2610.09667; requests for most other shortlisted records were rate-limited, so citation counts are not used to rank them.
- **arXiv records:** [2610.09858](https://arxiv.org/abs/2610.09858), [2610.09212](https://arxiv.org/abs/2610.09212), [2610.09145](https://arxiv.org/abs/2610.09145), [2610.04824](https://arxiv.org/abs/2610.04824), [2610.07782](https://arxiv.org/abs/2610.07782), [2610.04158](https://arxiv.org/abs/2610.04158), [2610.07473](https://arxiv.org/abs/2610.07473), [2610.09667](https://arxiv.org/abs/2610.09667).
- **Other checked sources:** [Semantic Scholar record for 2610.09667](https://www.semanticscholar.org/paper/8052eae0bcc6164f97f18f5c7362710662f44b95); independently indexed paper records for Caddie and Persistent Memory surfaced in web search. Paper claims and caveats are attributed to the arXiv abstracts/full text; results are not treated as established facts.
