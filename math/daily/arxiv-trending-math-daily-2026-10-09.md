# Mathematics on arXiv — latest batch, Friday 9 October 2026

Seven notable papers from the latest daily Mathematics announcement batch, spanning undecidability, sharp sampling theory, lattice minimization, hypergraph extremal problems, planar statistical mechanics, geometric inequalities, and Ramsey constructions. This is a result-led selection, not a measured popularity ranking: arXiv has no official trending chart, the batch is only two days old at the snapshot, and citation/attention evidence is too sparse to rank papers by momentum. For a quick tour, start with the stability undecidability result, the Boolean-cube sampling threshold, and the claimed completion of the Mueller–Ho conjecture.

## Top papers (ranked)

### 1. [Global asymptotic stability of homogeneous polynomial vector fields is undecidable](https://arxiv.org/abs/2610.12434)
- **Abstract:** Studies whether the origin of rational homogeneous polynomial ODEs is globally asymptotically stable and reduces this decision problem across odd degrees to the cubic case.
- **Authors:** Ivan O. Shevchenko, Jun Liu, Xinzhi Liu
- **arXiv:** `2610.12434v1` (published 2026-10-08 17:57:15 UTC; categories: `math.DS`, `math.CA`, `math.LO`)
- **Evidence for ranking:** A concrete computability result with many-one completeness and a reduction to fixed-dimension cubic systems; cross-listed across dynamical systems, analysis, and logic. Its breadth and precise undecidability claim place it first in this result-led selection, not on popularity evidence.
- **Claimed result:** The authors prove that deciding global asymptotic stability is many-one complete for every odd degree at least three in every sufficiently large dimension, and in particular is undecidable for cubic vector fields in a fixed dimension.
- **Assumptions and setting:** Homogeneous polynomial vector fields with rational coefficients; the fixed-dimension cubic conclusion is for a dimension whose existence is established by the paper.
- **Caveat:** The reduction is highly indirect and technical (the 50-page preprint uses polynomial encodings and theta-series machinery); the abstract does not give an explicit smallest dimension for the cubic undecidability result.
- **Announcement type:** new submission, announcement batch 2026-10-09
- **Themes:** Logic & foundations; Optimization & control

### 2. [Subspace Uncertainty and Sharp Sampling Thresholds on the Boolean Cube](https://arxiv.org/abs/2610.12358)
- **Abstract:** Derives worst-case noisy-regression sample thresholds for known subspaces of low-degree Boolean-cube functions by quantifying how their energy can concentrate on rarely sampled inputs.
- **Authors:** Thomas Weinberger
- **arXiv:** `2610.12358v1` (published 2026-10-08 17:23:25 UTC; categories: `math.PR`, `cs.IT`, `cs.LG`, `math.CO`)
- **Evidence for ranking:** Gives matching-order sampling and uncertainty bounds, including a lower-order remainder shown sharp by an Airy-kernel construction; its probability, information-theory, learning, and combinatorics cross-lists mark a substantial bridge.
- **Claimed result:** For fixed `q₀<1/2` and degree `1≤k≤q₀d`, the worst-subspace sample threshold for the stated minimax parametric error is `(m+t) exp(E_{d,k}+O(k^{1/3}))`; the authors also show that noisy estimation can cost exponentially more samples than noiseless identification.
- **Assumptions and setting:** Gaussian regression with squared population `L₂` loss, uniform random inputs on the `d`-dimensional Boolean cube, a known `m`-dimensional subspace of degree-at-most-`k` functions, and the confidence and fixed-constant conditions stated in the abstract.
- **Caveat:** The matching lower bound is established under the additional condition `m≤binom(d,⌊k^{1/3}⌋)` or `t≥m`; it is not claimed there for every feasible subspace dimension and confidence regime.
- **Announcement type:** new submission, announcement batch 2026-10-09
- **Themes:** Probability & statistics; Machine learning theory; Combinatorics & discrete mathematics

### 3. [A Complete Proof of Mueller--Ho Conjecture](https://arxiv.org/abs/2610.12203)
- **Abstract:** Classifies the minimizing lattice shapes and relative shifts for a two-component Bose-gas energy built from a theta function and a shifted theta function as the interaction parameter varies.
- **Authors:** Senping Luo, Juncheng Wei
- **arXiv:** `2610.12203v1` (published 2026-10-08 15:56:49 UTC; categories: `math.AP`, `math-ph`, `math.NT`)
- **Evidence for ranking:** Claims a complete parameter-regime classification for a named 2002 conjecture, connecting lattice optimization, analysis, and mathematical physics; this is a specific resolution claim rather than a popularity signal.
- **Claimed result:** The authors prove that minimizers, up to modular equivalence, pass through specified triangular, intermediate, square, and rectangular lattice configurations with relative shifts across three interaction thresholds, thereby claiming to prove the Mueller–Ho conjecture.
- **Assumptions and setting:** Minimize `θ(1;z)+αJ(z;a,b)` over `z` in the upper half-plane and shifts `(a,b)∈R²`, for `α∈[0,1]`; the variables model lattice shape and relative displacement in a two-component Bose gas.
- **Caveat:** The abstract states that three ordered thresholds exist but does not provide their explicit values; the classification is for this particular theta-energy model and is an author-claimed preprint result, not a peer-reviewed verdict.
- **Announcement type:** new submission, announcement batch 2026-10-09
- **Themes:** Mathematical physics; Analysis & PDE; Algebra & number theory

### 4. [A counterexample to the Erdős--Sós bipartite-link conjecture](https://arxiv.org/abs/2610.11642)
- **Abstract:** Constructs 3-uniform hypergraphs whose link graphs are all bipartite yet whose edge density asymptotically exceeds the conjectured one-quarter threshold.
- **Authors:** Tianchi Yang
- **arXiv:** `2610.11642v1` (published 2026-10-08 10:19:33 UTC; categories: `math.CO`)
- **Evidence for ranking:** A direct counterexample to a named extremal-combinatorics conjecture, with an explicit density exceeding its proposed asymptotic bound.
- **Claimed result:** The author claims examples with edge density at least `0.250000356 > 1/4` for all sufficiently large `n`, disproving the stated `(1/4+o(1)) binom(n,3)` upper-bound conjecture.
- **Assumptions and setting:** `n`-vertex 3-uniform hypergraphs subject to every link graph being bipartite; the construction is asserted for all sufficiently large `n`.
- **Caveat:** The improvement over `1/4` is numerically small, and the abstract does not specify the finite size at which the construction applies; the asymptotic counterexample does not by itself determine the optimal density.
- **Announcement type:** new submission, announcement batch 2026-10-09
- **Themes:** Combinatorics & discrete mathematics

### 5. [Strong RSW estimates for the FK-Ising model on s-embeddings](https://arxiv.org/abs/2610.11990)
- **Abstract:** Establishes strong Russo–Seymour–Welsh crossing estimates for the FK-Ising model on s-embeddings under a uniformly bounded geometry condition.
- **Authors:** Dmitry Chelkak, Yanqing Wei
- **arXiv:** `2610.11990v1` (published 2026-10-08 13:59:10 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** Proves a reusable crossing estimate and points to consequences for arm-event quasi-multiplicativity and cluster geometry; it extends a central planar-percolation technique to a broader embedding setup.
- **Claimed result:** Under the stated geometry condition, the authors prove crossings of rough topological quadrilaterals even with unfavorable boundary conditions, then obtain standard consequences including quasi-multiplicativity of arm events and fractal cluster properties.
- **Assumptions and setting:** FK-Ising on s-embeddings whose relevant tangential quadrilaterals have uniformly comparable edge lengths and angles bounded below; the paper also discusses near-critical regular-grid applications below the correlation-length scale.
- **Caveat:** The theorem depends on the uniformly bounded geometry hypothesis; its abstract does not assert the same strong estimates for arbitrary highly irregular embeddings.
- **Announcement type:** new submission, announcement batch 2026-10-09
- **Themes:** Probability & statistics; Mathematical physics

### 6. [The sharp $L^2$-Michael--Simon inequality](https://arxiv.org/abs/2610.12309)
- **Abstract:** Proves a sharp Sobolev-type inequality coupling the gradient and mean curvature of an immersed manifold, and characterizes equality cases.
- **Authors:** Jeffrey S. Case, Dawit Mengesha
- **arXiv:** `2610.12309v1` (published 2026-10-08 16:58:54 UTC; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** Supplies an explicit sharp constant and equality characterization, and reports extensions to spherical, hyperbolic, and other conformally developable ambient spaces; the differential-geometry/analysis cross-list supports its reach.
- **Claimed result:** For `n≥3` and an isometric immersion into Euclidean space, the authors prove the stated sharp `L²` Michael–Simon inequality for all `u∈W^{1,2}(Σ)` and derive related mean-curvature/volume inequalities.
- **Assumptions and setting:** An `n`-dimensional Riemannian manifold isometrically immersed in Euclidean space; the inequality includes the mean-curvature potential and the critical Sobolev exponent `2n/(n−2)`.
- **Caveat:** The stated inequality is for dimensions `n≥3` and the specified isometric-immersion setting; equality and extensions beyond the stated conformal ambient settings need the paper's precise hypotheses.
- **Announcement type:** new submission, announcement batch 2026-10-09
- **Themes:** Geometry & topology; Analysis & PDE

### 7. [Lower bounds for Ramsey numbers: $\mathrm{R}(6,8)\ge 135$ and $\mathrm{R}(8,10)\ge 345$](https://arxiv.org/abs/2610.12122)
- **Abstract:** Gives explicit two-colourings establishing improved lower bounds for two diagonal-family Ramsey numbers, checked by two independently written exhaustive clique-verification programs.
- **Authors:** Fritz Cremer
- **arXiv:** `2610.12122v1` (published 2026-10-08 15:16:34 UTC; categories: `math.CO`, `cs.DM`)
- **Evidence for ranking:** The paper provides explicit finite witnesses for two improved bounds and describes independent exhaustive verification, a concrete and checkable computational-combinatorics result.
- **Claimed result:** The author proves `R(6,8)≥135` and `R(8,10)≥345`, improving the cited April 2026 survey bounds of 134 and 343 using colorings of `K₁₃₄` and `K₃₄₄` without the prohibited monochromatic cliques.
- **Assumptions and setting:** Two-colour Ramsey numbers for avoiding a red `K₆` / blue `K₈`, and a red `K₈` / blue `K₁₀`; the proof rests on explicit coloring witnesses and exhaustive checks.
- **Caveat:** The new bounds establish lower bounds only, not exact Ramsey numbers; the witnesses were discovered with local search and need their certificates/checking code to be reproducible for independent computational auditing.
- **Announcement type:** new submission, announcement batch 2026-10-09
- **Themes:** Combinatorics & discrete mathematics; Numerical analysis & computation

## Trending Research Themes

- **Decision boundaries in dynamical systems:** The GAS paper turns a stability question into a computability-theoretic hardness result (2610.12434). This is a standout result in this batch, not evidence by itself of a field-wide shift.
- **Sharpness and worst cases:** Boolean-cube regression quantifies how rare-input concentration delays parametric rates (2610.12358), while the Michael–Simon paper identifies a sharp geometric inequality and equality cases (2610.12309). The shared theme is extremal control, not a common proof technique.
- **Conjecture tests by construction:** The Mueller–Ho preprint claims a complete minimizer classification (2610.12203); the hypergraph paper gives a counterexample (2610.11642); and the Ramsey paper supplies finite witnesses for improved lower bounds (2610.12122). These are different mathematical tasks, all centered on precise claims that can be checked against explicit hypotheses or certificates.
- **Probability on nonstandard structures:** Strong RSW for FK-Ising on s-embeddings broadens a crossing framework under geometric regularity (2610.11990), complementing the rare-region sampling analysis on the Boolean cube (2610.12358); the two settings do not imply a shared method.
- **A motif, not a trend:** Jacobi/theta functions appear in both the stability undecidability reduction (2610.12434) and the Bose-gas lattice energy (2610.12203), but serve different roles in the two papers.

## Open Problems and Research Directions

- **Stated scope gap:** Extend the matching lower bound in the Boolean-cube regression result beyond its stated dimension/confidence regimes, or determine whether different thresholds hold there (2610.12358).
- **Stated geometric hypothesis:** Investigate whether strong RSW estimates survive weaker geometry assumptions than uniformly bounded s-embedding geometry (2610.11990).
- **Follow-up suggested by the result:** Determine the optimal asymptotic edge density for 3-uniform hypergraphs with bipartite links and quantify the gap above `1/4` (2610.11642).
- **Follow-up suggested by the result:** Make the three Mueller–Ho transition thresholds explicit and test how the minimizer classification changes under broader interaction energies (2610.12203).
- **Computational direction:** Publish independently reproducible coloring certificates and extend local-search/certification efforts to tighten the Ramsey bounds (2610.12122).
- **Follow-up suggested by the result:** Determine explicit dimension thresholds and sharpen the reduction-size bounds for cubic GAS undecidability (2610.12434).

## Takeaway

The batch's most striking claims are about limits and sharp thresholds: an algorithm cannot decide a broad stability problem, noisy prediction can incur an exponential sample penalty, and a long-standing lattice-energy conjecture is claimed proved. They are fresh preprints rather than settled community consensus; this selection reflects the specificity and mathematical reach of the stated results, not demonstrated readership or citation momentum.

## Method and sources

- **Window:** Daily, latest available Mathematics announcement batch, Friday 2026-10-09; the preceding list batch is Thursday 2026-10-08. The selected papers were each first submitted on 2026-10-08, as shown by their arXiv records.
- **Snapshot:** 2026-10-11 00:16 UTC.
- **Coverage:** Screened all 504 entries in the Friday Mathematics listing; checked the arXiv abstract pages and metadata for the seven selected papers. For the three leading selections, also inspected the arXiv HTML introduction/main-results material.
- **Selection:** ArXiv supplies no official trending chart. Exact-title searches and available Semantic Scholar metadata provided little mature independent attention evidence for this two-day-old batch, so the list is labeled notable recent papers and ordered by claimed result specificity, cross-field scope, and checkability—not popularity, downloads, or citation gains.
- **Sources:** [arXiv Mathematics recent submissions](https://arxiv.org/list/math/recent); linked arXiv abstract pages and v1 HTML pages; arXiv API submission/update timestamps; Semantic Scholar Graph API metadata; exact-title web searches. All seven are v1 new submissions; no revisions are included.
