# arXiv Trending Math — Thursday, 5 November 2026

Latest daily mathematics announcement batch: 9 notable papers. The clearest pattern in this selection is structural mathematics sharpening bounds or proving rigidity—especially graph coloring, extremal combinatorics, and geometric energy minimization—with probability and analysis supplying cross-field results. Agenda: the coloring-bound advance, several classification and asymptotic results, then the open ends they leave. arXiv publishes no official trending chart, so this ordering is inferred from mathematical claims and scope rather than measured popularity; citation evidence for papers this recent is limited.

## Top papers (ranked)

### 1. [Polylogarithmic bound for the Gyárfás-Sumner conjecture](https://arxiv.org/abs/2611.06699)
- **Abstract:** For graphs excluding a fixed forest as an induced subgraph and with bounded clique number, the authors improve the known subpolynomial chromatic-number bound to a polylogarithmic one.
- **Authors:** Martin Bierbaumer, Matija Bucić
- **arXiv:** `2611.06699v1` (published 2026-11-04T16:01:51Z; categories: `math.CO`)
- **Evidence for ranking:** The introduction states an explicit improvement over the recent `|G|^{o(1)}` bound, with theorem `χ(G) ≤ C_{T,k}(log |G|)^{14k}`; this is the strongest explicit bound improvement in the selected batch.
- **Claimed result:** Bierbaumer and Bucić prove that for every fixed tree `T` and positive integer `k`, every `T`-induced-free graph `G` with clique number at most `k` and at least two vertices satisfies `χ(G) ≤ C_{T,k}(log |G|)^{14k}` (arXiv introduction, Theorem 1).
- **Assumptions and setting:** `T` and `k` are fixed; the graph is finite, contains no induced copy of `T`, and has clique number at most `k`.
- **Caveat:** This improves the asymptotic bound but does not establish the conjectured bound on chromatic number independent of graph size.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Combinatorics & discrete mathematics

### 2. [Uniqueness of the hexagonal lattice's universal optimality](https://arxiv.org/abs/2611.06278)
- **Abstract:** Building on a recent proof of universal optimality, the authors show that the planar hexagonal lattice is the only periodic point configuration with that property, up to Euclidean motion.
- **Authors:** Markus Faulhuber, Philipp Petersen
- **arXiv:** `2611.06278v1` (published 2026-11-04T10:20:41Z; categories: `math.MG`)
- **Evidence for ranking:** The paper adds a uniqueness theorem to the recent universal-optimality result and treats every periodic configuration at fixed density, not just lattices; its potential extension reaches all completely monotone potentials of squared distance with finite hexagonal-lattice energy.
- **Claimed result:** Faulhuber and Petersen state that for every periodic `C ⊂ R²` of density one, the hexagonal lattice minimizes every Gaussian energy, and equality for even one Gaussian parameter implies congruence to the hexagonal lattice (arXiv HTML, Theorem 1.2).
- **Assumptions and setting:** Periodic configurations in the plane at density one; the uniqueness statement is up to Euclidean motion. The paper also gives a corresponding result for nonzero completely monotone potentials when the reference energy is finite.
- **Caveat:** The uniqueness claim is deliberately restricted to periodic configurations; arbitrary configurations can be made noncongruent by deleting finitely many lattice points without changing density or the limiting energy.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Geometry & topology; Optimization & control

### 3. [Proof of two conjectures on the log-concavity of partition ranks and cranks](https://arxiv.org/abs/2611.06757)
- **Abstract:** The authors prove two conjectures asserting log-concavity of the partition-crank and partition-rank counting sequences over specified ranges of the statistic.
- **Authors:** Jianxi Mao, Wenle Shi, Bao-Xuan Zhu
- **arXiv:** `2611.06757v1` (published 2026-11-04T16:35:58Z; categories: `math.CO`, `math.NT`)
- **Evidence for ranking:** The authors prove two named conjectures and obtain strict log-concavity for both classical partition statistics; the work connects combinatorics with number theory.
- **Claimed result:** Mao, Shi, and Zhu prove `A_k(m,n)^2 > A_k(m−1,n)A_k(m+1,n)` for `k∈{1,2}`, `n≥72`, and `|m|≤n−k−71`, where `A_1=M` is the crank count and `A_2=N` the rank count (arXiv HTML, Theorem 1.3).
- **Assumptions and setting:** The inequalities hold for integer partition size `n` and statistic index `m` in the stated ranges; the rank case starts at `n≥73` because of the range condition.
- **Caveat:** The theorem covers the conjectured ranges, not every boundary value in the full support of each rank or crank sequence.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 4. [On Diameter Graphs Problems: A proof of Brass's Conjecture](https://arxiv.org/abs/2611.05631)
- **Abstract:** For diameter graphs of finite point sets in three-dimensional space, the authors prove Brass's conjecture by showing that removing at most one point suffices to make the remaining graph 3-colorable.
- **Authors:** Gyivan Lopez-Campos
- **arXiv:** `2611.05631v1` (published 2026-11-03T21:19:45Z; categories: `math.CO`, `math.MG`)
- **Evidence for ranking:** The abstract claims a resolution of a named conjecture with the strong explicit bound of one deleted point, and cross-lists the result between combinatorics and metric geometry.
- **Claimed result:** Lopez-Campos proves that in every finite `S ⊂ R³`, deleting at most one vertex from its diameter graph leaves a 3-colorable induced subgraph; the paper also answers a question of Dol'nikov (arXiv abstract).
- **Assumptions and setting:** Finite point sets in `R³`; adjacency means that two points are at distance equal to the diameter of the set.
- **Caveat:** The conjecture proved here is the specific three-dimensional, three-color case; it does not settle the analogous question for arbitrary dimension and color number.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 5. [Certified Collision Exclusion and an Unconditional Upper Bound Λ<0.156821 for the de Bruijn--Newman Constant](https://arxiv.org/abs/2611.06245)
- **Abstract:** The authors describe a computer-assisted collision-exclusion proof yielding the unconditional bound `Λ < 0.156821` in the Polymath normalization.
- **Authors:** Michel Planat, Dale James Raymond
- **arXiv:** `2611.06245v1` (published 2026-11-04T09:51:08Z; categories: `math.NT`)
- **Evidence for ranking:** The preprint states a specific unconditional bound for a constant tied to the zeros of the Riemann xi-function and describes a finite, auditable certificate with 44,182 torus boxes and additional separator data.
- **Claimed result:** Planat and Raymond claim `Λ < 156821/10^6`, combining a finite-height verification with a continuation argument, certified exclusions, and a uniform barrier at infinity (arXiv abstract).
- **Assumptions and setting:** The normalization is that of Polymath; the conclusion concerns the transition parameter beyond which all zeros of the heat-deformed Riemann xi-function are real.
- **Caveat:** This is a computer-assisted preprint claim whose correctness depends on the certificate and its proof-to-computation interface; this report has not independently verified either.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Algebra & number theory; Numerical analysis & computation

### 6. [Gaussian free field limit for the Airy_β line ensemble](https://arxiv.org/abs/2611.05852)
- **Abstract:** For every `β>0`, the authors prove that a rescaled centered height function of the Airy_β line ensemble converges to the Gaussian free field in the half-plane.
- **Authors:** Vadim Gorin, Lingfu Zhang
- **arXiv:** `2611.05852v1` (published 2026-11-04T02:43:23Z; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** The claimed limit holds for every positive `β` and links a family of random line ensembles to a two-dimensional field; the paper is cross-listed in probability and mathematical physics.
- **Claimed result:** Gorin and Zhang claim convergence of the centered Airy_β height function to the half-plane Gaussian free field after rescaling, with spatial coordinate `x ↦ √(-x)` and `β` entering through a `√β` field rescaling (arXiv abstract).
- **Assumptions and setting:** The statement is for each fixed `β>0` under the paper's specified space-time and field rescalings.
- **Caveat:** The abstract does not specify the precise mode of convergence; the theorem's topology and test-function assumptions must be taken from the paper before applying the limit.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Probability & statistics; Mathematical physics

### 7. [Almost All 3-uniform Hypergraphs are Class 1](https://arxiv.org/abs/2611.05622)
- **Abstract:** For a stated range of edge probabilities, the authors prove that a random 3-uniform binomial hypergraph has chromatic index equal to its maximum degree with high probability, and they contrast this with higher uniformities.
- **Authors:** Arnab Chaterjee, Asaf Ferber, Marcelo Sales, Mason Shurman
- **arXiv:** `2611.05622v1` (published 2026-11-03T21:07:43Z; categories: `math.CO`, `cs.DM`)
- **Evidence for ranking:** This extends the familiar almost-everywhere Class 1 result from ordinary random graphs to 3-uniform random hypergraphs, while also identifying a contrasting obstruction for higher uniformities; it is cross-listed with discrete mathematics.
- **Claimed result:** Chaterjee, Ferber, Sales, and Shurman claim that `H ~ H^{(3)}_{n,p}` is Class 1 with high probability when `n^{-2/3-1/200} ≤ p ≤ 0.99`; they also state non-Class-1 results for a broad range when uniformity `k≥4` and `k` does not divide `n` (arXiv abstract).
- **Assumptions and setting:** The random model is the binomial `k`-uniform hypergraph; the 3-uniform assertion has the explicit probability interval above, and the higher-uniformity contrast is restricted as stated by the authors.
- **Caveat:** The result is asymptotic and probabilistic; it does not assert that every 3-uniform hypergraph in the range is Class 1.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 8. [Matching Random Point Sets with Minimum Distortion](https://arxiv.org/abs/2611.06845)
- **Abstract:** For two independent uniform samples of `n` points from `[0,1]`, the authors show that the typical minimum distortion of a bijection between the samples is `n^{2/3}` up to polylogarithmic factors.
- **Authors:** Itai Benjamini, Mark Braverman, Elad Tzalik, Georgii Zakharov
- **arXiv:** `2611.06845v1` (published 2026-11-04T18:02:57Z; categories: `math.PR`, `math.CO`, `math.MG`)
- **Evidence for ranking:** The work gives matching upper- and lower-bound mechanisms for a nontrivial distortion exponent and spans probability, combinatorics, and metric geometry.
- **Claimed result:** Benjamini, Braverman, Tzalik, and Zakharov claim that the two independent samples from the uniform interval have distortion `n^{2/3}` up to polylogarithmic factors with high probability, using a multiscale construction for the upper bound (arXiv abstract).
- **Assumptions and setting:** Two independent `n`-point samples from `[0,1]` equipped with uniform measure; distortion is measured for a bijection between the induced finite metric spaces.
- **Caveat:** The stated exponent is established for this one-dimensional uniform model, not for arbitrary metric-measure spaces.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics; Geometry & topology

### 9. [Uniqueness of Ricci flows from singular initial data](https://arxiv.org/abs/2611.06814)
- **Abstract:** The authors establish uniqueness for Ricci flows with nonnegative sectional curvature and scaling-invariant curvature bounds when their induced distances converge, up to isometry, to the same initial distance function.
- **Authors:** Laura Flower, Man-Chun Lee, Felix Schulze
- **arXiv:** `2611.06814v1` (published 2026-11-04T17:26:38Z; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** The result addresses uniqueness from singular initial data and is cross-listed between differential geometry and analysis of PDEs; its hypotheses make a precise claim in an active geometric-flow setting.
- **Claimed result:** Flower, Lee, and Schulze claim uniqueness under nonnegative sectional curvature and scaling-invariant curvature bounds when the induced distance functions converge to the same initial metric up to isometry; a compact-case variant is also stated (arXiv abstract).
- **Assumptions and setting:** The main statement assumes nonnegative sectional curvature, scaling-invariant curvature bounds, and convergence of distance functions to a common initial distance function up to isometry.
- **Caveat:** The compact-case extension is described only as requiring a restricted singular-set size and suitable weaker conditions in the abstract; those precise conditions need to be read from the paper.
- **Announcement type:** new submission, announcement-batch date 2026-11-05
- **Themes:** Geometry & topology; Analysis & PDE

## Trending Research Themes

- **Sharper structural bounds in combinatorics.** The Gyárfás-Sumner paper improves a chromatic-number bound, the partition paper proves two log-concavity conjectures, and the diameter-graph and random-hypergraph papers prove coloring or extremal statements in specific settings (papers 1, 3, 4, and 7). These are distinct arguments, not evidence of one shared technique or a field-wide shift.
- **Rigidity and uniqueness in geometric settings.** The hexagonal-lattice paper turns energy minimality into a uniqueness statement for periodic configurations; the Ricci-flow paper proves uniqueness under curvature and metric-convergence hypotheses, while the random-point matching paper quantifies the distortion needed between two samples (papers 2, 8, and 9). The common feature is a focus on structural constraints, not a shared method.
- **Probability connecting discrete models to analytic limits.** The Airy_β result identifies a Gaussian free field scaling limit, the hypergraph paper gives high-probability edge-coloring behavior, and random-point matching gives a high-probability distortion scale (papers 6–8). This is a recurring topic among this selection, not evidence of a broader archive-wide change.

## Open Problems and Research Directions

- **Open problem — author-stated:** The full Gyárfás-Sumner conjecture still predicts a chromatic bound independent of graph size for every fixed forest and clique bound; the new polylogarithmic estimate stops short of that conclusion (paper 1). **Research direction — synthesis:** Test whether the exponent or constants can be reduced for special tree families before seeking the full constant bound.
- **Open problem — paper limitation:** The hexagonal-lattice uniqueness result is for periodic configurations; the authors note that unrestricted uniqueness fails after deleting finitely many points (paper 2). **Research direction — synthesis:** Study uniqueness modulo finite defects or within explicitly broader classes where density and energy are defined compatibly.
- **Open problem — paper range:** The proven rank/crank inequalities cover the stated ranges of `m` and `n`, not the full support boundary (paper 3). **Research direction — synthesis:** Analyze the remaining edge terms and determine whether strict log-concavity persists or changes form there.
- **Open problem — verification gap:** The de Bruijn-Newman bound depends on a large computer certificate and an interface from the certificate to the analytic proof (paper 5). **Research direction — synthesis:** Independently reproduce the certificate and test the stability of the claimed endpoint under alternative interval or precision choices.
- **Research direction — synthesis:** Extend the `n^{2/3}` distortion analysis from uniform samples on `[0,1]` to other one-dimensional densities and then to higher-dimensional or non-Euclidean metric-measure spaces (paper 8).
- **Open problem — paper hypotheses:** The Ricci-flow abstract leaves the exact compact-case weaker conditions and singular-set restriction to the paper (paper 9). **Research direction — synthesis:** Map which singular-set sizes and curvature assumptions are essential by comparing borderline cases against the main uniqueness theorem.

## Takeaway

This batch's clearest theorem-scale advances are the polylogarithmic Gyárfás-Sumner bound, hexagonal-lattice uniqueness, and partition log-concavity. The de Bruijn-Newman bound is especially delicate because it depends on a substantial computer certificate that still needs independent verification.

## Method and sources

- **Window:** Daily; latest mathematics announcement batch listed by arXiv as Thursday, 5 November 2026. Window start and end: 2026-11-05 through 2026-11-05. The listing contains no 6 November batch, so this report uses the prior/latest 5 November batch. The selected papers' original submission timestamps range from 2026-11-03 to 2026-11-04 UTC; the announcement-batch date follows the arXiv recent listing.
- **Snapshot:** 2026-11-06 01:32:58 UTC.
- **Coverage:** Traversed the full 364-entry batch on `https://arxiv.org/list/math/recent`; the mathematics archive was the core, retaining neighboring classes only for papers cross-listed in mathematics. Nine papers were selected for concrete mathematical results and cross-subfield reach. Selected abstract pages were checked directly on arXiv; introductions and main-result statements were inspected for papers 1–3. No proof was independently verified.
- **Inference:** Recent-paper citation and independent-attention signals were too sparse to support popularity-based ordering; selection emphasizes concrete claimed results and scope, with cross-listing as corroboration and recency only as a tie-breaker. Citation counts are not represented as gains during the window.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); selected arXiv abstracts: [2611.06699](https://arxiv.org/abs/2611.06699), [2611.06278](https://arxiv.org/abs/2611.06278), [2611.06757](https://arxiv.org/abs/2611.06757), [2611.05631](https://arxiv.org/abs/2611.05631), [2611.06245](https://arxiv.org/abs/2611.06245), [2611.05852](https://arxiv.org/abs/2611.05852), [2611.05622](https://arxiv.org/abs/2611.05622), [2611.06845](https://arxiv.org/abs/2611.06845), and [2611.06814](https://arxiv.org/abs/2611.06814). The configured `web_extract` backend was unavailable, so abstract and HTML pages were verified using live arXiv pages instead. Semantic Scholar citation metadata was not available for this snapshot and was not used to rank.
