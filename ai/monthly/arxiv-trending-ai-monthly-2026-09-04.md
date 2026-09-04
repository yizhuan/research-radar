## Headline
This month’s arXiv AI submissions cluster around: (1) vision model adaptation without heavy supervision, (2) systems that compile high-level specifications into executable neural components, and (3) more careful evaluation/measurement of LLM behavior. The ordering below is inferred (no official arXiv “trending” chart).

## Top papers (ranked)

### 1. [Temporal Self-Distillation: Learning Visual State Tracking in Videos Without Supervision](https://arxiv.org/abs/2609.04203v1)
- **Abstract:** We introduce S$^3$T (Self-Supervised Self-Distillation over Time), which, to the best of our knowledge, is the first fully self-contained framework for continuous video state tracking.
- **Authors:** Shravan Venkatraman, Wenshuai Zhao, Mohammad Hassan Vali, Arno Solin
- **arXiv:** `2609.04203v1` (published 2026-09-03T17:59:55Z; categories: cs.CV)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** We introduce S$^3$T (Self-Supervised Self-Distillation over Time), which, to the best of our knowledge, is the first fully self-contained framework for continuous video state tracking. Our method treats temporal sampling density as privileged information, based on the hypothesis that a denser view of the same clip recovers the running state more accurately.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Training & adaptation

### 2. [TokenMatch: 3D Mesh Correspondence Transformer with Curvature-Guided Tokenisation](https://arxiv.org/abs/2609.04202v1)
- **Abstract:** While data-driven 3D shape correspondence estimation has recently seen substantial progress, robust matching under partial observations and strong non-isometric deformations remains challenging.
- **Authors:** Adeela Islam, Zorah Lähner, Vittorio Murino, Vladislav Golyanik
- **arXiv:** `2609.04202v1` (published 2026-09-03T17:59:55Z; categories: cs.CV)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** While data-driven 3D shape correspondence estimation has recently seen substantial progress, robust matching under partial observations and strong non-isometric deformations remains challenging. Existing learning-based approaches often rely on hand-crafted descriptors or template-based representations, whereas recent generative models over functional maps suffer from high inference cost, limited interpretability, and poor generalisation to partial shapes.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Training & adaptation

### 3. [Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction](https://arxiv.org/abs/2609.04201v1)
- **Abstract:** Online 3D reconstruction models perform poorly on long videos.
- **Authors:** Chin-Yang Lin, Yang-Che Sun, Cheng Sun, Fu-En Yang, Min-Hung Chen, et al.
- **arXiv:** `2609.04201v1` (published 2026-09-03T17:59:53Z; categories: cs.CV)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** Online 3D reconstruction models perform poorly on long videos. This happens because regressing poses relative to a fixed first-frame anchor forces extrapolation far beyond the training distribution.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Efficient inference & systems

### 4. [Compile by Training: Turning Natural-Language Specifications into Local Neural Functions](https://arxiv.org/abs/2609.04199v1)
- **Abstract:** Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a provider.
- **Authors:** Yuntian Deng, Pengyu Nie, Stuart Shieber
- **arXiv:** `2609.04199v1` (published 2026-09-03T17:59:49Z; categories: cs.CL, cs.AI, cs.LG)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a provider. We present compile by training, which turns a natural-language specification into a reusable neural function.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Efficient inference & systems

### 5. [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](https://arxiv.org/abs/2609.04198v1)
- **Abstract:** Language-model judges now gate training data, score generations, and drive leaderboards.
- **Authors:** Haoyaun Zhu, Jie Zhang
- **arXiv:** `2609.04198v1` (published 2026-09-03T17:59:43Z; categories: cs.AI, cs.LG)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** Language-model judges now gate training data, score generations, and drive leaderboards. The judge is then a measurement instrument, resting on one rarely stated assumption: the same request, sent to the same model name, reads the same tomorrow.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Evaluation & benchmarks

### 6. [ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize](https://arxiv.org/abs/2609.04197v1)
- **Abstract:** Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer yet no more accurate.
- **Authors:** Lihao Liu, Peng Tang, Kunwar Yashraj Singh, Shabnam Ghadar
- **arXiv:** `2609.04197v1` (published 2026-09-03T17:59:37Z; categories: cs.CL, cs.AI)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer yet no more accurate. We trace this to three deficiencies - incomplete error observation, limited search diversity, and unreliable selection - and propose ESPO (Error-Structured Prompt Optimization), which decomposes prompt optimization into three phases: Diagnose clusters all training errors into structural patterns in one round; Propose generates candidates via four complementary strategies with independent biases; Select applies bootstrap stability selection.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Agents & reasoning

### 7. [Robust PAC Learning of Concurrent Stochastic Games](https://arxiv.org/abs/2609.04189v1)
- **Abstract:** We introduce the first Probably Approximately Correct (PAC) learning framework for general-sum concurrent stochastic games (CSGs) with transition uncertainty, while addressing the challenge of Nash equilibrium (NE) existence.
- **Authors:** Angel Y. He, David Parker
- **arXiv:** `2609.04189v1` (published 2026-09-03T17:58:57Z; categories: cs.LG, cs.GT, cs.LO, cs.MA)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** We introduce the first Probably Approximately Correct (PAC) learning framework for general-sum concurrent stochastic games (CSGs) with transition uncertainty, while addressing the challenge of Nash equilibrium (NE) existence. Our algorithm maintains data-driven $L^1$ confidence sets over transition kernels and solves a robust CSG to compute a social-welfare optimal $\varepsilon$-NE, using a robust MDP-based exploration mechanism to drive joint state-action coverage.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Agents & reasoning

### 8. [Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR](https://arxiv.org/abs/2609.04108v1)
- **Abstract:** Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs.
- **Authors:** Boyan Li, Bingsen Chen, Chenghao Yang, Ping Nie, Chen Zhao, Xi Ye
- **arXiv:** `2609.04108v1` (published 2026-09-03T17:14:27Z; categories: cs.CL, cs.AI, cs.LG)
- **Evidence for ranking:** Semantic Scholar citation signals unavailable from the sources checked (API rate-limited / missing values). Ranking is therefore inferred from arXiv recency within the monthly window and thematic coverage.
- **Claimed contribution:** Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs. Prior work uses OPD's dense token-level supervision to complement the sparse RL reward, fusing the two signals within a single step: either as a \emph{weighted-additive combination} or a \emph{teacher-modulated rescaling} of the RL advantage.
- **Caveat:** Caveat: The abstract text reviewed does not include a clear limitations section; full paper should be checked for constraints/failure modes.
- **Announcement type:** new submission
- **Themes:** Agents & reasoning

## Trending research themes
- **Vision learning (self-/distillation-style) for video state tracking and 3D perception:** [Temporal Self-Distillation](https://arxiv.org/abs/2609.04203v1), [TokenMatch](https://arxiv.org/abs/2609.04202v1), [Scal3R](https://arxiv.org/abs/2609.04201v1)
- **Spec-to-model compilation and executable neural components:** [Compile by Training](https://arxiv.org/abs/2609.04199v1)
- **LLM evaluation robustness and prompt optimization/decision-making:** [Clean Engineering, Unstable Measurement](https://arxiv.org/abs/2609.04198v1), [ESPO](https://arxiv.org/abs/2609.04197v1), [Sequential Beats Joint](https://arxiv.org/abs/2609.04108v1)
- **Game-theoretic learning guarantees tied to reasoning/agents:** [Robust PAC Learning of Concurrent Stochastic Games](https://arxiv.org/abs/2609.04189v1)

## Research opportunities
- **Better, checkable limitation reporting for very-recent arXiv submissions:** abstracts are often insufficient to determine failure modes; extracting limitations from the full PDFs would strengthen claims. (e.g., [Temporal Self-Distillation](https://arxiv.org/abs/2609.04203v1), [Clean Engineering, Unstable Measurement](https://arxiv.org/abs/2609.04198v1))
- **Controlled evaluation protocols for prompt/optimization methods:** extend reliability-focused experimental design ideas into optimization/policy-distillation pipelines to test whether improvements hold under consistent measurement. (e.g., [Clean Engineering, Unstable Measurement](https://arxiv.org/abs/2609.04198v1), [ESPO](https://arxiv.org/abs/2609.04197v1))
- **System-level integration of spec-to-function models:** test compilation approaches under real deployment constraints (latency/accuracy and integration with downstream tooling). (e.g., [Compile by Training](https://arxiv.org/abs/2609.04199v1))

## Notable shifts
Not available from sources checked: this run only inspects the current monthly window (no prior-window comparison performed).

## Takeaway
Across the last 30 days, the dominant themes are vision-model adaptation (tracking/reconstruction), compilation/specification-to-execution for neural components, and evaluation rigor for LLM systems. Citation-based “attention” signals could not be reliably retrieved here, so the ranking is inferred rather than popularity-ranked.

## Method and sources
- **Window:** 2026-08-05 to 2026-09-04 (inclusive), mapped from “this month” = last 30 calendar days
- **Snapshot time:** 2026-09-04T15:21:19Z UTC
- **arXiv category query:** cat:cs.AI+OR+cat:cs.LG+OR+cat:stat.ML+OR+cat:cs.CL+OR+cat:cs.CV+OR+cat:cs.RO+OR+cat:cs.NE+OR+cat:cs.MA
- **Candidate pool:** arXiv API feed (max_results=200) sorted by submittedDate, then filtered by arXiv published/updated timestamps within the window
- **Semantic Scholar corroboration:** attempted, but citation signals were rate-limited / missing for these IDs during this run; treated as unavailable
- **Paper sources (verified):** arXiv abstract pages for the papers linked above