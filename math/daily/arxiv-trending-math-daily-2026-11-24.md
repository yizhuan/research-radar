# arXiv Mathematics — 24 November 2026 batch: 8 notable new papers

Today’s set ranges from a Möbius-band analogue of fusion algebra and a new bridge between differential operators and Calogero–Moser geometry to constructive results in coding theory, integer optimization, and geometric combinatorics. This guide moves through those algebraic and combinatorial results, then closes with numerical algorithms and open questions. This is an inferred ranking, not an official arXiv trending chart; direct citation evidence is limited for papers this new, so the list is best read as notable recent work rather than measured popularity.

## Top papers (ranked)

### 1. [Möbius Fusion Algebra](https://arxiv.org/abs/2611.29234)
- **Abstract:** For a pseudo-unitary modular tensor category with an anti-monoidal involution, the authors define a generally noncommutative Möbius fusion algebra and give a formula for dimensions of its simple modules.
- **Authors:** Ippo Orii, Yuji Tachikawa
- **arXiv:** `2611.29234v1` (published 2026-11-22 05:12:11 UTC; categories: `math.QA` (primary), `hep-th`, `math-ph`, `math.GT`)
- **Evidence for ranking:** Signals score 0.75, entirely from three cross-lists (0.25 each); this is tied for the highest score in the candidate set. Its arXiv comment also links animated versions of two proposition proofs, a checkable research artifact, but no direct attention score was recorded.
- **Claimed result:** The authors prove the algebra is semisimple and identify its simple-module dimensions using the modular S-matrix and data from the involution; they interpret this as a non-orientable analogue of the Verlinde formula.
- **Assumptions and setting:** The input is a pseudo-unitary modular tensor category together with an anti-monoidal involution; the motivation is Reshetikhin–Turaev-type TQFT on non-orientable manifolds.
- **Caveat:** The authors explicitly do not construct the proposed non-orientable TQFT in full generality; the formula’s TQFT role remains an expected interpretation.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Geometry & topology; Mathematical physics; Algebra & number theory

### 2. [Strong holonomicity of functions on curves](https://arxiv.org/abs/2611.29063)
- **Abstract:** For a smooth affine irreducible complex curve, the authors show that a local solution-counting index of a differential operator equals the Calogero–Moser index of its Weyl closure, then apply it to annihilators of locally holomorphic functions.
- **Authors:** Yuri Berest, Isaac Goldberg
- **arXiv:** `2611.29063v1` (published 2026-11-21 22:04:37 UTC; categories: `math.AG` (primary), `math.QA`, `math.RA`, `math.RT`)
- **Evidence for ranking:** Signals score 0.75 from three cross-lists (0.25 each), tied for the highest score. Its claimed equality connects a local differential-equation invariant to a geometric classification of operator ideals, giving it a strong cross-field result among the tied candidates.
- **Claimed result:** The authors prove that the holonomicity index computed by counting solutions in truncated local rings at singular points equals the Calogero–Moser index of the Weyl closure; they use this to compute indices for selected function annihilators.
- **Assumptions and setting:** The main theorem concerns nonzero differential operators on a smooth affine irreducible curve over C and the corresponding global differential-operator ring.
- **Caveat:** The paper computes the invariant in selected examples rather than giving a universal closed formula for every holonomic function; its proposed colored-Jones extension is conjectural, not proved here.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Algebra & number theory; Analysis & PDE

### 3. [Neural Schrödinger Bridge via Yasue Action with Applications to Generative Modeling](https://arxiv.org/abs/2611.28623)
- **Abstract:** The authors propose a neural Schrödinger-bridge solver that learns a deterministic velocity field from endpoint samples through a saddle-point formulation using the Yasue action.
- **Authors:** Yan-Han Chen, Abhishek Halder, Hailiang Liu
- **arXiv:** `2611.28623v1` (published 2026-11-21 07:17:00 UTC; categories: `math.OC` (primary), `cs.LG`, `stat.CO`, `stat.ML`)
- **Evidence for ranking:** Signals score 0.75 from three cross-lists (0.25 each), tied for the highest score. It is placed after the two algebraic results at the same score because its abstract’s evidence is a solver plus numerical demonstrations rather than a structural theorem about the mathematical object.
- **Claimed result:** The authors derive a saddle-point formulation and report consistency for it, then demonstrate the method on synthetic and real data in low and high dimensions; the learned ODE velocity replaces the usual learned SDE drift.
- **Assumptions and setting:** It uses samples from source and target distributions rather than known density functions; the stated Schrödinger-bridge existence setting assumes finite second moments.
- **Caveat:** The abstract supports effectiveness through numerical experiments, not a broad independent benchmark or a general performance guarantee over all generative tasks.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Optimization & control; Numerical analysis & computation

### 4. [Deterministic regularisation of the nonsymmetric eigenproblem](https://arxiv.org/abs/2611.28614)
- **Abstract:** The author gives a deterministic exact-arithmetic algorithm that perturbs a complex contraction to a simple-spectrum matrix with controlled eigenbasis conditioning and computes the resulting eigensystem.
- **Authors:** Matthew J. Colbrook
- **arXiv:** `2611.28614v1` (published 2026-11-21 06:57:56 UTC; categories: `math.NA` (primary), `cs.CC`, `math.SP`)
- **Evidence for ranking:** Signals score 0.50 from two cross-lists (0.25 each). Among that score tier, the claimed resolution of an open complexity problem and explicit perturbation and operation bounds support its placement near the top.
- **Claimed result:** For a complex contraction A of order n≥2 and 0<δ<1/2, the author claims a deterministic algorithm finding ||E||<δ such that A+E has simple spectrum, with the condition-number/minimum-gap ratio bounded by C(n/δ)^(20/3), using O(n^3 log^d(n/δ)) real-field operations and comparisons.
- **Assumptions and setting:** The guarantee is for complex contractions in exact arithmetic, with absolute constants C and d; the algorithm also computes an exact eigensystem of the perturbed matrix.
- **Caveat:** These bounds are stated for the contraction-and-perturbation setting, not as a uniform guarantee for every unmodified nonsymmetric eigenproblem.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Numerical analysis & computation

### 5. [A Proof of Blackburn's Conjecture on Non-Overlapping Codes](https://arxiv.org/abs/2611.28776)
- **Abstract:** For non-overlapping codes of fixed length over large alphabets, the author proves Blackburn’s conjecture about optimal codes and characterizes the codes attaining Levenshtein’s bound.
- **Authors:** Yeow Meng Chee
- **arXiv:** `2611.28776v1` (published 2026-11-21 12:39:26 UTC; categories: `cs.IT` (primary), `cs.DM`, `math.CO`)
- **Evidence for ranking:** Signals score 0.50 from two cross-lists (0.25 each). The explicit proof of a named conjecture and the equality characterization make this one of the stronger concrete results in the same cross-list score tier.
- **Claimed result:** The author proves Blackburn’s conjecture: for every code length n and all sufficiently large alphabet sizes q, the best non-overlapping codes are maximum ones; the abstract also identifies the equality cases for Levenshtein’s bound.
- **Assumptions and setting:** Codewords have fixed length n over an alphabet of size q; “non-overlapping” means no nonempty proper prefix of a codeword is a suffix of a codeword.
- **Caveat:** The abstract states an eventual-in-q result but does not give the threshold for “sufficiently large” q.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 6. [The Gerards-Schrijver conjecture on the Edmonds-Johnson property is false](https://arxiv.org/abs/2611.28580)
- **Abstract:** The author disproves a proposed forbidden-minor characterization by constructing a minimal 5×6 totally half-modular matrix that violates the Edmonds–Johnson property but contains neither of the two conjectured minors.
- **Authors:** Alberto Del Pia
- **arXiv:** `2611.28580v1` (published 2026-11-21 05:23:50 UTC; categories: `math.CO` (primary), `cs.DM`, `math.OC`)
- **Evidence for ranking:** Signals score 0.50 from two cross-lists (0.25 each). The explicit minimal counterexample and proof that every proper minor has the property provide a concrete, independently checkable form of progress on the conjecture.
- **Claimed result:** The author gives a 5×6 counterexample with no minor equal to either of the two specified matrices, and proves it is minimal by reducing every proper minor to known classes with the property.
- **Assumptions and setting:** The statement concerns totally half-modular integral matrices and the equality of the first Chvátal closure with the integer hull for the specified bounded systems.
- **Caveat:** This refutes the proposed characterization; it does not supply a replacement classification of all matrices with the Edmonds–Johnson property.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Optimization & control

### 7. [Reduction types of curves in tame extensions](https://arxiv.org/abs/2611.28255)
- **Abstract:** For curves over discretely valued fields, the author gives sufficient conditions under which a tame base extension determines the curve’s reduction type, along with an algorithm for the possible types using harmonic graph covers.
- **Authors:** Júlia Martínez-Marín
- **arXiv:** `2611.28255v1` (published 2026-11-20 19:42:19 UTC; categories: `math.NT` (primary), `math.AG`, `math.CO`)
- **Evidence for ranking:** Signals score 0.50 from two cross-lists (0.25 each). The work connects arithmetic geometry with graph combinatorics and provides both a reduction-type algorithm and a characterization of potentially good reduction.
- **Claimed result:** Under sufficient conditions on the original reduction type R and a tame extension degree n, the new reduction type is uniquely determined; the author also gives an algorithm for possible types and a characterization of tame curves with potentially good reduction.
- **Assumptions and setting:** C/K has genus at least one over a discretely valued field with algebraically closed residue field; the extension L/K is finite and tame. The abstract highlights zero abelian and toric ranks as a case satisfying the sufficient conditions.
- **Caveat:** Outside the stated sufficient conditions, the result is an algorithm for possibilities rather than a uniqueness theorem for every reduction type.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology; Combinatorics & discrete mathematics

### 8. [Improved Lower Bound on the Hadwiger-Debrunner Numbers](https://arxiv.org/abs/2611.29166)
- **Abstract:** The author improves asymptotic lower bounds for the Hadwiger–Debrunner piercing numbers using parallelotopes and the hypergraph container method.
- **Authors:** Chaya Keller
- **arXiv:** `2611.29166v1` (published 2026-11-22 02:52:46 UTC; categories: `math.CO` (primary), `cs.CG`)
- **Evidence for ranking:** Signals score 0.25 from one cross-list (0.25). This is a weaker attention proxy than the higher-ranked entries, but the paper addresses a longstanding extremal-geometric problem with explicit asymptotic exponents.
- **Claimed result:** For d≥2 the author proves HD_d(p,d+1)≥p^(d−o(1)), and more generally HD_d(p,q)≥p^((q−1)/(q−d)−o(1)); the bound is tight up to polylogarithmic factors among families with bounded VC dimension.
- **Assumptions and setting:** The setting is the (p,q)-theorem for families of convex sets in R^d, with p≥q≥d+1; the stated tightness comparison is restricted to bounded-VC-dimension families.
- **Caveat:** The bound is asymptotic and does not determine the exact Hadwiger–Debrunner numbers; the bounded-VC tightness statement is not a claim of tightness for all convex-set families.
- **Announcement type:** new submission, 2026-11-24 announcement batch
- **Themes:** Combinatorics & discrete mathematics

## Trending Research Themes

- **Combinatorial structure, counterexamples, and extremal bounds:** The selected work ranges from an eventual optimality theorem for non-overlapping codes (Chee, arXiv:2611.28776), through a minimal obstruction to a matrix-minor conjecture (Del Pia, arXiv:2611.28580), to new asymptotic piercing-number lower bounds (Keller, arXiv:2611.29166). These are distinct problems, but all make progress through explicit structural constructions rather than a single shared technique.
- **Geometric and graph-based encodings of algebraic data:** The Möbius fusion algebra uses ribbon graphs and modular-category data (Orii–Tachikawa, arXiv:2611.29234); strong holonomicity relates local solution counts to Calogero–Moser strata (Berest–Goldberg, arXiv:2611.29063); and tame reduction types are studied through harmonic covers of graphs (Martínez-Marín, arXiv:2611.28255). The common signal is translation between geometric objects and algebraic invariants, not evidence of a field-wide surge.
- **Computation with mathematical guarantees:** Colbrook’s deterministic perturbation algorithm gives explicit conditioning and complexity bounds (arXiv:2611.28614), while Chen–Halder–Liu derive a sample-based Schrödinger-bridge solver and report numerical experiments (arXiv:2611.28623). The results differ in kind—an exact algorithmic guarantee versus an empirical neural method—so they should not be read as one emerging method.
- **Generative modeling via optimal transport and stochastic control:** The Schrödinger-bridge paper is an isolated selected signal at this scale; its endpoint-sample formulation links stochastic control, optimal transport ideas, and learned deterministic flows, but one paper is not enough to infer a broader shift.

## Open Problems and Research Directions

- **Author-stated open problem — non-orientable TQFT:** Orii and Tachikawa say their algebraic construction does not fully construct the anticipated non-orientable TQFT. A concrete follow-up is to identify additional categorical coherence data or hypotheses under which the algebra’s module dimensions can be realized as state-space dimensions of a full theory (arXiv:2611.29234).
- **Author-stated conjecture — colored Jones functions:** Berest and Goldberg report the conjecture that colored Jones functions are strongly holonomic, with index at least two, in a quantum-torus analogue. Testing knot families and relating their annihilator ideals to the differential-operator index developed here would probe the conjecture, but the present paper does not prove it (arXiv:2611.29063).
- **Author-raised example — hypergeometric functions:** The introduction asks how to compute the Calogero–Moser index of the annihilator of a Gauss $_2F_1$ function. Applying the local-index method to parameter regimes and singularity types of this example could help clarify when strong holonomicity occurs (arXiv:2611.29063).
- **Author-stated longstanding problem plus synthesis — piercing numbers:** The Hadwiger–Debrunner numbers remain to be determined more sharply. One direction is to test whether constructions beyond parallelotopes, or methods extending the hypergraph-container argument, improve the exponents or close the gap between general convex families and bounded-VC families (arXiv:2611.29166). This is a proposed direction, not a claim of novelty or tractability.

## Takeaway

The clearest mathematical signals today are structural: a new non-orientable fusion-algebra construction, a local-to-global index theorem for differential operators on curves, and several concrete advances in coding and extremal combinatorics. The ordering is only a transparent proxy based largely on cross-listing, with no measured attention or usable citation counts for this batch; treat it as a reading shortlist, not a popularity leaderboard.

## Method and sources

- **Window:** daily announcement batch dated 2026-11-24; arXiv window 2026-11-20 19:00:00 UTC through 2026-11-23 19:00:00 UTC; announced 2026-11-24 01:00:00 UTC. Snapshot time: 2026-11-24 03:12:41 UTC. This uses the latest announcement batch, not a prior batch.
- **Coverage:** the core corpus is arXiv Mathematics (`math.*`); neighboring categories are included only for selected papers cross-listed in a `math.*` category. The supplied signal file reports 247 arXiv records in its collection source and a pool size of 247, while its candidate array contains 150 records; rankings here begin with those candidate records, and this discrepancy means the report does not claim a fully audited archive-wide candidate enumeration.
- **Inference:** no official arXiv trending chart exists. The supplied signals give 0.25 weight per cross-list, with additional weights available for Hugging Face upvotes, Hacker News points/comments, citations, influential citations, and code stars. All eight chosen entries score only from cross-listing: scores are 0.75 for three cross-lists (ranks 1–3), 0.50 for two (ranks 4–7), and 0.25 for one (rank 8). The collector reports `with_attention: 0`; Hugging Face and Hacker News collection succeeded, but no candidate in the signal set had a positive external-attention component. Zero score means no measured signal in this collection, not lack of importance. Semantic Scholar data was unavailable in the signal run, so citation momentum and influential-citation corroboration could not be used. Ties were ordered by the specificity and potential mathematical significance of the authors’ stated results, not author reputation.
- **Verification:** all eight arXiv abstract pages were checked for title, authors, version/date, abstract, and categories. The introductions and main-result framing of the first three papers were inspected in arXiv HTML where available; no proof was independently checked. The claims above are attributed preprint claims.
- **Sources:** supplied signal file `/home/yizhuan/.research/math/daily/arxiv-trending-math-daily-2026-11-24.signals.json`; primary arXiv pages linked in each entry; full-text HTML for `2611.29234`, `2611.29063`, and `2611.28623` at `https://arxiv.org/html/<id>`.
