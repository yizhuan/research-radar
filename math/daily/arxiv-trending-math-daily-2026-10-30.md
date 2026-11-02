# arXiv Mathematics — Friday, 30 October 2026 announcement batch

Latest available daily batch at the 2026-11-02 snapshot: Friday 30 October 2026 (the prior announcement batch; no 2 November batch was yet listed). Five notable recent papers; the strongest pattern is sharp, quantitative statements—an asymptotic resolving a counting question, a uniqueness threshold, and explicit bounds. Spoken agenda: tropical combinatorics, Euler dynamics, self-avoiding walks, then divisor correlations and kinetic equations. arXiv has no official trending chart, and this inferred ordering has little citation evidence for papers only days old; read it as a shortlist of notable new work, not measured popularity.

## Top papers (ranked)

### 1. [The Number of Tropical Order Types and Coherent Matching Fields](https://arxiv.org/abs/2610.40622)
- **Abstract:** The authors count tropical matching fields and hyperplane-sequence types, deriving the same first-order asymptotic for regular triangulations of products of simplices and comparing real and tropical order types.
- **Authors:** Xavier Allamigeon, Yiyuan Chen, Stéphane Gaubert, Xavier Goaoc
- **arXiv:** `2610.40622v1` (published 2026-10-29T17:56:09Z; categories: `math.CO`, `math.AG`, `math.OC`)
- **Evidence for ranking:** The introduction identifies the regular-triangulation estimate as answering a question of Santos; the paper also bridges combinatorics, tropical/algebraic geometry, and optimization. Semantic Scholar recorded 0 citations at the snapshot, so this placement reflects the explicit result and cross-field scope, not observed uptake.
- **Claimed result:** For each fixed integer `r`, the authors show the number of regular triangulations of `Δ^{n−1}×Δ^{r−1}` is `n^{(r−1)^2 n+o(n)}` as `n→∞`; the paper also establishes first-order counting comparisons for associated tropical order types.
- **Assumptions and setting:** The stated asymptotics hold with `r` fixed as `n` tends to infinity; the objects include coherent matching fields, tropical hyperplane-sequence types, and regular triangulations.
- **Caveat:** The fixed-`r` asymptotic is not a uniform two-parameter estimate when `r` grows with `n`; it does not by itself settle algorithmic complexity questions for linear programs or games.
- **Announcement type:** new submission, Friday 30 October 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology; Optimization & control

### 2. [A Sharp Uniqueness-Nonuniqueness Dichotomy for Neutral Vortex Arrays in 2D Euler Equations](https://arxiv.org/abs/2610.40552)
- **Abstract:** For stationary arrays of disjoint neutral vortices, the authors give a sharp integral criterion, based on an envelope of vorticity `L^p` norms, separating unique from nonunique Euler evolution.
- **Authors:** Thomas Y. Hou, Xiang Qin, Peicong Song, Wenhan Zhang
- **arXiv:** `2610.40552v1` (published 2026-10-29T17:39:18Z; categories: `math.AP`)
- **Evidence for ranking:** The authors state both directions of a sharp criterion for every finite nondecreasing envelope, rather than only an example or a one-sided sufficient condition. Semantic Scholar recorded 0 citations at the snapshot, and the searches checked did not surface independent expert discussion; the placement is based on the theorem's precise scope and content.
- **Claimed result:** Writing `I_Θ=∫_{p₀}^{∞} Θ(p)⁻¹ dp`, the authors prove uniqueness for every array in their class when `I_Θ` diverges, even among bounded energy-admissible weak velocity solutions; when it converges, they construct an array with two distinct unforced Lagrangian evolutions from the same data.
- **Assumptions and setting:** The dichotomy concerns a specified class of stationary arrays of disjoint, compactly supported neutral vortices and a finite nondecreasing envelope `Θ` controlling vorticity `L^p` norms.
- **Caveat:** The authors explicitly note that this does not settle sharpness of the classical Yudovich criterion for general unbounded vorticities; the result is limited to the stated neutral-array class.
- **Announcement type:** new submission, Friday 30 October 2026 announcement batch
- **Themes:** Analysis & PDE

### 3. [Quantitative sub-ballisticity of self-avoiding walk on `ℤ^d`](https://arxiv.org/abs/2610.40520)
- **Abstract:** For `d≥2`, the authors give an explicit exponential upper bound on the probability that an `n`-step self-avoiding walk reaches distance at least `vn`, yielding a high-probability displacement bound of order `n/exp(c log* n)`.
- **Authors:** Ekin Arikök, Christoforos Panagiotis, Nicholas Pischke, Thomas Powell
- **arXiv:** `2610.40520v1` (published 2026-10-29T17:28:11Z; categories: `math.PR`, `math.LO`)
- **Evidence for ranking:** It makes a previously qualitative sub-ballisticity result quantitative, derives a bridge-partition estimate, and is cross-listed between probability and logic because of its proof-theoretic analysis. Semantic Scholar recorded 0 citations at the snapshot; no independent expert discussion was found in the searches checked.
- **Claimed result:** The authors bound the probability of linear displacement by `exp(−n/T(v))` for an explicit function `T` and sufficiently large `n`; they derive displacement at most `n/exp(c log* n)` with very high probability.
- **Assumptions and setting:** The uniform law on length-`n` self-avoiding walks starting at the origin in the hypercubic lattice `ℤ^d`, for each fixed `d≥2`.
- **Caveat:** The resulting displacement scale is a quantitative improvement, not a sharp asymptotic; the paper says a stronger bound would follow if the normalized bridge partition function had the expected polynomial decay, which is not proved here.
- **Announcement type:** new submission, Friday 30 October 2026 announcement batch
- **Themes:** Probability & statistics; Logic & foundations

### 4. [Global Well-Posedness of Landau Equation in Bounded Domains](https://arxiv.org/abs/2610.40517)
- **Abstract:** The authors prove global well-posedness near a Maxwellian for the Landau equation in bounded `C^3` domains with in-flow or diffuse-reflection boundary conditions, covering `−3≤γ≤1` including Coulomb interactions.
- **Authors:** Zhimeng Ouyang, Lei Wu
- **arXiv:** `2610.40517v1` (published 2026-10-29T17:26:36Z; categories: `math.AP`)
- **Evidence for ranking:** The claimed global strong-solution result spans the full stated interaction range, including Coulomb, and treats two boundary laws in bounded domains. Semantic Scholar recorded 0 citations at the snapshot, with no independent expert discussion surfaced by the searches checked; ranking rests on the theorem's scope, not measured attention.
- **Claimed result:** The authors show that small compatible Gaussian perturbations generate global strong solutions, with uniqueness and continuous dependence among weak solutions.
- **Assumptions and setting:** Perturbations are small and compatible with a Maxwellian; the spatial domain is bounded with `C^3` boundary, and the boundary condition is either in-flow or diffuse reflection.
- **Caveat:** This is a near-equilibrium theorem under compatibility and boundary-regularity assumptions, not a large-data global result.
- **Announcement type:** new submission, Friday 30 October 2026 announcement batch
- **Themes:** Analysis & PDE; Mathematical physics

### 5. [Shifted convolutions of divisor functions](https://arxiv.org/abs/2610.40439)
- **Abstract:** For fixed positive integers `k,l` and a nonzero fixed shift `h`, the author proves a power-saving asymptotic for a smooth weighted correlation of the `k`- and `l`-fold divisor functions at `n` and `n+h`.
- **Authors:** Miguel N. Walsh
- **arXiv:** `2610.40439v1` (published 2026-10-29T16:56:28Z; categories: `math.NT`)
- **Evidence for ranking:** The introduction says the all-`k,l` theorem supplies cases with `k,l≥3` not previously known, extending a classical shifted-correlation problem. Semantic Scholar recorded 0 citations at the snapshot; a general number-theory paper-list post surfaced, but not independent mathematical analysis, so attention evidence remains slight.
- **Claimed result:** The author establishes a main term with singular series `𝔖_{k,l}(h)(k−1)!(l−1)! x(log x)^{k+l−2}∫Φ`, with a power-saving error, for the weighted sum specified in Theorem 1.1.
- **Assumptions and setting:** Fixed integers `k,l≥1`, fixed nonzero `h`, a smooth compactly supported weight `Φ` on `(0,∞)`, and the asymptotic as `x→∞`.
- **Caveat:** The stated theorem does not assert uniformity as `h`, `k`, or `l` vary with `x`; the result is a preprint claim and its proof has not been independently checked here.
- **Announcement type:** new submission, Friday 30 October 2026 announcement batch
- **Themes:** Algebra & number theory

## Trending Research Themes

- **Sharper quantitative conclusions.** The tropical-counting paper and the divisor-correlation paper both give explicit asymptotics for large combinatorial/arithmetic families; the self-avoiding-walk paper turns a qualitative displacement conclusion into an explicit rate. These are parallel signals in this batch, not a shared technique or evidence of a field-wide shift.
- **Uniqueness and global behavior for nonlinear equations.** The Euler paper gives a sharp uniqueness/nonuniqueness boundary within a structured vorticity class, while the Landau paper proves global well-posedness near equilibrium under specified boundary conditions. Both are analysis/PDE contributions, but their equations, solution classes, and methods differ.
- **A probability–logic bridge.** The self-avoiding-walk work uses proof-theoretic ideas to quantify an existing probabilistic argument. This is a cross-field connection in one selected paper, not a repeated method across the batch.
- **Tropical geometry as a bridge to optimization.** The tropical order-type paper links combinatorial counting to regular triangulations and comparisons between linear programs and mean-payoff games; this is a distinct intersection rather than a trend corroborated by multiple papers.

## Open Problems and Research Directions

- **Author-stated limitation:** The Euler authors say their criterion does not settle sharpness of the classical Yudovich condition for general unbounded vorticities. A follow-up could test whether related thresholds persist beyond stationary neutral arrays, or identify which parts fail for broader data classes; see [the Euler dichotomy](https://arxiv.org/abs/2610.40552).
- **Author-stated expectation:** The self-avoiding-walk paper says polynomial decay of normalized bridge counts is expected; it is not established there. Proving a decay rate and tracing its effect through their argument could test whether a stronger displacement scale follows; see [the self-avoiding-walk paper](https://arxiv.org/abs/2610.40520).
- **Scope-derived direction:** The tropical counting theorem fixes `r` while `n` grows. Investigating regimes where `r` also grows would test how far the asymptotic and the comparison among regular triangulations, order types, and game/LP structures extend; see [the tropical order-type paper](https://arxiv.org/abs/2610.40622).
- **Author-identified extension:** The divisor-correlation introduction says its methods may extend to other shifted convolution problems. Testing which related arithmetic functions or shift ranges retain a power-saving error is a concrete extension, not a claim made by the theorem; see [the divisor-functions paper](https://arxiv.org/abs/2610.40439).
- **Scope-derived direction:** The Landau result is perturbative around a Maxwellian in `C^3` bounded domains. Larger perturbations, weaker boundary regularity, or other boundary laws are possible test settings, without assuming the current proof extends; see [the Landau paper](https://arxiv.org/abs/2610.40517).

## Takeaway

This batch offers several clean theorem-level advances: a fixed-dimension asymptotic answering a triangulation-count question, a two-sided Euler uniqueness criterion, a new quantitative self-avoiding-walk bound, and broad but perturbative PDE results. Since these preprints are only days old and external attention evidence is sparse, the ordering is best treated as an informed shortlist, not a popularity ranking or a substitute for expert review.

## Method and sources

- **Window:** Daily announcement batch, 2026-10-30 through 2026-10-30; the latest available batch at the snapshot, so this is the prior batch relative to 2026-11-02. The batch listing's selected entries show first-submission timestamps on 2026-10-29 UTC; all five are v1 new submissions, not revisions. Snapshot time: 2026-11-02T01:22:41Z.
- **Coverage:** Reviewed the full arXiv Mathematics recent-listing segment for Friday 30 October (874 entries) and selected candidates from that batch; verified all five abstracts on their arXiv abstract pages and checked the arXiv API metadata for IDs, versions, dates, authors, categories, and abstracts. Read the introductions/main-result statements of the selected papers in arXiv HTML; no proof was independently verified. The configured `web_extract` backend could not extract pages, so the arXiv browser pages and API were used instead.
- **Ranking method:** arXiv provides no official trend or popularity ranking. This inferred ordering prioritizes concrete claimed results, scope, and cross-listing, then recency; it is not a readership estimate. Semantic Scholar Graph API current citation and influential-citation totals were 0 for each of these five papers as of the snapshot. These are current totals, not gains during the window, and the age of the papers makes citation evidence uninformative.
- **Attention checks:** Searches for independent expert or seminar discussion did not surface such coverage for these five papers. A general number-theory paper-list post surfaced for the divisor-correlation paper; it is a weak discoverability signal, not an endorsement.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); the five linked arXiv abstract pages and their HTML versions; arXiv Atom API records; Semantic Scholar Graph API metadata; [general number-theory listing post](https://x.com/PQBW/status/2116398997996736836).
