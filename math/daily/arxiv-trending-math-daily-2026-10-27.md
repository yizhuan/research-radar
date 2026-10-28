# arXiv mathematics — 27 October 2026: 9 notable papers on conjecture resolutions, sharp bounds, and cross-field methods

Today’s readout starts with claimed solutions to long-standing conjectures and problems, then moves to bounds and bridges across number theory, dynamics, statistics, and random matrices; it closes with concrete follow-up questions. arXiv publishes no official trending chart, so this is an inferred ordering of notable papers—not measured popularity—and citation evidence is limited for this very recent batch.

## Top papers (ranked)

### 1. [The Golomb--Welch conjecture for arbitrary centre sets](https://arxiv.org/abs/2610.34291)
- **Abstract:** The authors claim that no Lee ball of radius r≥2 tiles ℤⁿ by translations when n≥3, resolving the Golomb--Welch conjecture for arbitrary centre sets.
- **Authors:** Bocong Chen, Jing Huang, Gaojun Luo
- **arXiv:** `2610.34291v1` (published 2026-10-25 13:45:59 UTC; categories: `math.CO`)
- **Evidence for ranking:** The introduction states the unrestricted-centre theorem and its scope explicitly; the result is also surfaced in [MathWorld’s Golomb–Welch entry](https://mathworld.wolfram.com/Golomb-WelchConjecture.html), providing an independent secondary pointer to the claimed resolution.
- **Claimed result:** The authors state that for every n≥3 and r≥2, ℤⁿ cannot be tiled by translates of the Lee ball Bₙ(r), without assuming the set of centres is linear, periodic, or has a density.
- **Assumptions and setting:** Integer lattice ℤⁿ with Lee distance; the theorem concerns translational tilings by one fixed Lee ball and all centre sets, for n≥3 and r≥2.
- **Caveat:** The authors note that the existence classification does not classify the individual perfect Lee codes in the remaining admissible cases (n≤2 or r=1).
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 2. [A solution to Haagerup's problem: Normality of weights is commutatively determined](https://arxiv.org/abs/2610.35774)
- **Abstract:** The authors prove that lower semi-continuity of a C*-algebra weight and normality of a von Neumann algebra weight can each be detected on the corresponding commutative subalgebras.
- **Authors:** David P. Blecher, Ikhan Choi
- **arXiv:** `2610.35774v1` (published 2026-10-26 17:14:22 UTC; categories: `math.OA` (primary), `math.FA`)
- **Evidence for ranking:** The paper states an affirmative answer to Haagerup’s 1975 Problem 1.11 and provides explicit equivalences in two operator-algebra settings; the result was also independently indexed by [Wolfram MathWorld](https://mathworld.wolfram.com/OperatorAlgebraWeight.html).
- **Claimed result:** The authors show that a weight is lower semi-continuous if its restrictions to commutative C*-subalgebras are lower semi-continuous, and derive the von Neumann algebra counterpart: normality follows from normality on commutative von Neumann subalgebras.
- **Assumptions and setting:** Weights on C*-algebras and von Neumann algebras; the commutative tests involve the relevant positive sums, and normality is understood as preserving directed suprema.
- **Caveat:** The authors disclose that the proofs were substantially obtained with GPT-6.0 and then checked and rewritten by the authors; this report has not independently verified the proofs.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Functional analysis & operator algebras (added theme; no controlled theme precisely fits)

### 3. [The C_p conjecture of Muckenhoupt](https://arxiv.org/abs/2610.34099)
- **Abstract:** For 1<p<∞, the authors claim that the C_p weight condition is necessary and sufficient for weighted inequalities relating the Hilbert transform to the Hardy–Littlewood maximal operator and for the weighted Fefferman–Stein inequality.
- **Authors:** Andrei K. Lerner, Sheldy Ombrosi
- **arXiv:** `2610.34099v1` (published 2026-10-25 06:54:18 UTC; categories: `math.CA` (primary), `math.FA`)
- **Evidence for ranking:** The introduction identifies this as the resolution of Muckenhoupt’s long-standing sufficiency conjecture and gives a concrete sparse-operator estimate from which the weighted theorem follows.
- **Claimed result:** The authors prove the sparse estimate needed to establish sufficiency of C_p, completing the asserted necessary-and-sufficient characterization for both inequalities.
- **Assumptions and setting:** Weights w on ℝ satisfying the stated C_p condition with parameters r>1 and K<∞; the result is stated for 1<p<∞, with the authors saying the argument extends to ℝⁿ.
- **Caveat:** The abstract’s p-range excludes the endpoints p=1 and p=∞; the paper’s main exposition is one-dimensional and points to a remark for the higher-dimensional extension.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Analysis & PDE

### 4. [A proof of Wang's planar D-coloring conjecture](https://arxiv.org/abs/2610.33322)
- **Abstract:** The author proves the remaining sharp D-edge-coloring bounds for planar graphs with maximum degree Δ≥6, completing the conjectured bound after earlier work handled Δ≤5 and Δ≥33.
- **Authors:** Harshit Verma
- **arXiv:** `2610.33322v1` (published 2026-10-23 21:49:55 UTC; categories: `math.CO` (primary), `cs.DM`)
- **Evidence for ranking:** This closes the parameter gap left by the earlier Δ≤5 and Δ≥33 cases; the arXiv record says the Δ=6 case comes with ancillary certificates and verification scripts, making the computational part checkable.
- **Claimed result:** The author proves a D-coloring with 2Δ−1 colors for every planar graph of maximum degree Δ≥6; Δ=6 is computer-assisted.
- **Assumptions and setting:** A D-coloring is a proper edge coloring in which every K₄ minus an edge subgraph is rainbow; Wang’s conjectured counts for Δ=4 and 5 were established earlier, while this paper settles Δ≥6.
- **Caveat:** The Δ=6 case depends on computer-assisted certificates; reproducing and independently checking the ancillary verification is an important review step.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 5. [Counting Admissible Sets of Integers: A Proof of the Erdős--Nicolas--Sárközy Conjecture](https://arxiv.org/abs/2610.34372)
- **Abstract:** For admissible subsets of {1,…,N}, the authors prove that their count grows as exp(Θ(√N)), as conjectured by Erdős, Nicolas, and Sárközy.
- **Authors:** Guoqing Wang, Wenkai Yang
- **arXiv:** `2610.34372v1` (published 2026-10-25 15:26:02 UTC; categories: `math.CO`)
- **Evidence for ranking:** The preprint gives matching exponential-order upper and lower bounds and a concrete additive-combinatorial ingredient for the upper bound; the result also appears in [MathDB’s conjecture listing](https://mathdb.com/p/414124/erdos-nicolas-sarkozy-conjecture-on-admissible-subsets).
- **Claimed result:** The authors prove exp(c√N)≤a(N)≤exp(C√N) for absolute c,C>0 and every N≥4, with the same order for admissible sets whose maximum is N.
- **Assumptions and setting:** A finite set is admissible when any two of its subsets with equal sum have equal cardinality; a(N) counts nonempty admissible subsets of {1,…,N}.
- **Caveat:** The result fixes the order of growth but not a leading constant or finer asymptotic for log a(N); the upper bound uses a proportional-size subset with controlled doubling.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 6. [Dynamical Chowla conjecture for polynomials of several variables](https://arxiv.org/abs/2610.34912)
- **Abstract:** The authors extend a dynamical form of the prime number theorem to multivariate polynomials of sufficiently large Birch rank and establish analogous averages over integer points on algebraic varieties.
- **Authors:** Biao Wang, Daodao Yang
- **arXiv:** `2610.34912v1` (published 2026-10-26 06:36:49 UTC; categories: `math.NT` (primary), `math.AG`, `math.DS`)
- **Evidence for ranking:** The work bridges number theory, algebraic geometry, and dynamics, extending the prior Bergelson–Richter result to a genuinely multivariate regime; the exact rank condition makes the scope checkable in the abstract.
- **Claimed result:** The authors establish the stated dynamical Chowla-type conclusions for multivariate polynomials whose Birch rank is sufficiently large relative to degree, plus analogous results for averages over integer points on algebraic varieties.
- **Assumptions and setting:** Multivariate polynomials subject to a degree-dependent lower bound on Birch rank; the abstract does not state the numerical threshold.
- **Caveat:** The result does not cover all multivariate polynomials: low Birch-rank cases are outside the stated hypothesis.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

### 7. [Operator limits of random matrices: Edge universality and sharp approximations](https://arxiv.org/abs/2610.35808)
- **Abstract:** The author proves spectral-edge convergence of suitably rescaled Lanczos tridiagonalizations of general Wigner matrices to the stochastic Airy operator and gives sharp couplings for several classical ensembles.
- **Authors:** Hyung-Gil Kwak
- **arXiv:** `2610.35808v1` (published 2026-10-26 17:40:39 UTC; categories: `math.PR` (primary), `math-ph`, `math.NA`)
- **Evidence for ranking:** The paper links random-matrix edge statistics to operator limits, with additional joint eigenvalue, eigenfunction, and spectral-measure convergence; it also reports quantitative coupling errors for Airy, Bessel, and Sine operators.
- **Claimed result:** The author establishes convergence to the stochastic Airy operator with Dirichlet boundary condition for the Wigner setting and sharp couplings for Gaussian, Laguerre, and circular β-ensembles, respectively.
- **Assumptions and setting:** Suitably rescaled Lanczos tridiagonalizations formed from deterministic initial vectors; the abstract describes general Wigner matrices, while the exact entry-distribution and moment hypotheses are specified in the paper.
- **Caveat:** “General Wigner” is not assumption-free; the abstract alone does not give the precise entry and moment conditions needed to apply the theorem.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Probability & statistics; Mathematical physics; Numerical analysis & computation

### 8. [Improved lattice-packing bounds in small dimensions](https://arxiv.org/abs/2610.35830)
- **Abstract:** The author modifies the Cohn–Elkies linear program using constraints on short lattice vectors to improve lattice-packing upper bounds in specified dimension ranges.
- **Authors:** Nina Zubrilina
- **arXiv:** `2610.35830v1` (published 2026-10-26 17:50:37 UTC; categories: `math.NT` (primary), `math.CO`)
- **Evidence for ranking:** The paper reports improvement over the three-point bound for dimensions 11–16 and below published numerical Cohn–Elkies values across several further ranges; it supplies exact rational certificates and verification code.
- **Claimed result:** The author proves a certified upper bound based on a modified linear program that exploits restrictions on how short vectors can co-occur in classes modulo 2.
- **Assumptions and setting:** Full-rank Euclidean lattices normalized to have shortest nonzero vector of length 1; the result bounds lattice packing density, not arbitrary sphere packings.
- **Caveat:** The paper reports upper-bound improvements, not new dense lattice constructions; the margin over the comparison bounds diminishes in some higher dimensions.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 9. [Optimal tradeoffs between variance and sensitivity, via Hellinger-Kantorovich geometry](https://arxiv.org/abs/2610.35858)
- **Abstract:** The authors characterize Pareto-optimal variance–sensitivity tradeoffs for unbiased estimators via Hellinger–Kantorovich geometry and give a Z-estimation method that attains such pairs asymptotically.
- **Authors:** Adam Quinn Jaffe, Congwei Yang, Nicolás García Trillos, Bodhisattva Sen
- **arXiv:** `2610.35858v1` (published 2026-10-26 17:58:42 UTC; categories: `math.ST` (primary), `math.AP`, `math.OC`, `stat.ME`)
- **Evidence for ranking:** A four-category bridge connects statistical decision tradeoffs to a geometry interpolating Hellinger and Wasserstein structures; the abstract gives both an asymptotic construction and a concrete maximum-likelihood consequence.
- **Claimed result:** The authors state that the model’s Hellinger–Kantorovich geometry determines the full Pareto front and that their Z-estimation procedure asymptotically achieves optimal pairs; in the stated asymptotic sense, maximum likelihood has the least sensitivity among estimators with optimal variance.
- **Assumptions and setting:** Unbiased estimators in a given statistical model; the Pareto characterization is asymptotic where relevant, and applied construction requires solving a continuum of PDEs.
- **Caveat:** The authors execute the full PDE-based program only for selected nontrivial parametric examples, so practical construction in general models remains unresolved.
- **Announcement type:** new submission, 27 October 2026 announcement batch
- **Themes:** Probability & statistics; Optimization & control; Analysis & PDE

## Trending Research Themes

- **Classical conjectures and problems revisited:** the selected claims span perfect Lee codes and translational tilings ([Chen, Huang & Luo](https://arxiv.org/abs/2610.34291)), normal weights in operator algebras ([Blecher & Choi](https://arxiv.org/abs/2610.35774)), weighted harmonic-analysis inequalities ([Lerner & Ombrosi](https://arxiv.org/abs/2610.34099)), planar edge coloring ([Verma](https://arxiv.org/abs/2610.33322)), and admissible-set counting ([Wang & Yang](https://arxiv.org/abs/2610.34372)). These are distinct conjectures, not evidence of a shared technique or field-wide shift.
- **Sharper bounds built from structure:** the short-vector constraints behind [Zubrilina’s lattice-packing bounds](https://arxiv.org/abs/2610.35830) and the sparse-operator/telescoping argument in [Lerner–Ombrosi](https://arxiv.org/abs/2610.34099) use different tools, but both turn structural restrictions into improved quantitative control.
- **Bridges between discrete objects and analytic limits:** [Kwak’s random-matrix operator limit](https://arxiv.org/abs/2610.35808) connects finite-dimensional spectra to stochastic differential operators; [Wang–Yang’s dynamical Chowla result](https://arxiv.org/abs/2610.34912) carries number-theoretic averages into dynamics and algebraic varieties. These are isolated cross-field signals in this batch.
- **Geometry as a language for statistical tradeoffs:** [Jaffe et al.](https://arxiv.org/abs/2610.35858) use Hellinger–Kantorovich geometry to interpolate the geometries associated with variance and sensitivity minimization, linking optimal transport ideas to estimator theory.

## Open Problems and Research Directions

- **Author-stated scope gap — Lee codes:** [Chen, Huang & Luo](https://arxiv.org/abs/2610.34291) classify which parameter pairs admit perfect Lee codes, but explicitly do not classify the individual codes in the admissible cases. A follow-up could describe code structure for n≤2 or r=1, or make the theorem’s finite local obstructions and density-gap constants more explicit.
- **Hypothesis boundary — dynamical Chowla:** [Wang & Yang](https://arxiv.org/abs/2610.34912) require Birch rank sufficiently large relative to degree. Mapping the threshold precisely, then testing what survives at lower rank or on broader classes of varieties, would probe the boundary of the stated theorem; this is a proposed extension, not an author-claimed resolution.
- **Computer-assisted verification — planar D-coloring:** [Verma](https://arxiv.org/abs/2610.33322) identifies Δ=6 as computer-assisted and provides certificates/scripts. Independent reproduction or formal verification of that finite case is a concrete validation step before relying on the full conjecture resolution.
- **Refining density bounds — lattice packing:** [Zubrilina](https://arxiv.org/abs/2610.35830) notes that constraints involving classes modulo higher powers of 2 could yield further, likely small improvements. Constructing exact certificates for those constraints and comparing them with known lattice constructions would test whether the remaining upper/lower-bound gap can be reduced.
- **Extending the geometric estimator construction:** [Jaffe et al.](https://arxiv.org/abs/2610.35858) say the Pareto front is characterized geometrically, but implementing the associated continuum of PDEs has been completed only in selected parametric examples. Working out additional model families and stable numerical methods would test how broadly the theoretical tradeoffs can be realized.
- **Endpoint and higher-dimensional analysis:** [Lerner & Ombrosi](https://arxiv.org/abs/2610.34099) state the result for 1<p<∞ and explain the ℝⁿ extension in a remark. Endpoint analogues and the precise range of related operators are natural proposed extensions, not claims made by this paper.

## Takeaway

The strongest apparent signals are several explicit, author-claimed resolutions of established conjectures or named problems, alongside papers that sharpen packing and harmonic-analysis bounds and connect fields through geometry or operator limits. These are very recent preprints: the mathematical claims and supporting artifacts deserve expert scrutiny, and the available attention evidence is too thin to interpret the ordering as a popularity measure.

## Method and sources

- **Window:** daily arXiv announcement batch dated 2026-10-27; exact window 2026-10-27 through 2026-10-27. At the snapshot time no 2026-10-28 batch was visible, so this uses the latest prior batch.
- **Coverage:** the complete arXiv Mathematics recent listing for the batch was traversed (835 entries); the nine selected abstract pages were individually checked. Mathematical primary and cross-list categories are retained. This is a selected report, not comprehensive coverage of the archive.
- **Snapshot:** 2026-10-28 01:22:16 UTC.
- **Inference:** arXiv supplies no official trending ranking. Ordering is inferred from the specificity and scope of claimed results, cross-subfield relevance, available secondary indexing, and checkable proof artifacts; no numeric trend score is used. Recency is only a tie-breaker. Semantic Scholar Graph records were queried for the selected arXiv IDs, but the returned records did not expose citation-count or influential-citation fields, so citation momentum could not be measured. No citation totals are represented as period gains.
- **Reading and sources:** arXiv recent listing and all selected arXiv abstract pages are the primary metadata and abstract sources. The introductions/main-result statements were inspected for the top three papers: [Golomb–Welch](https://arxiv.org/html/2610.34291v1), [Haagerup](https://arxiv.org/html/2610.35774v1), and [C_p](https://arxiv.org/html/2610.34099v1). Targeted web searches checked secondary indexing for selected claims, including [MathWorld’s Golomb–Welch](https://mathworld.wolfram.com/Golomb-WelchConjecture.html) and [operator-algebra weight](https://mathworld.wolfram.com/OperatorAlgebraWeight.html) entries and [MathDB’s Erdős–Nicolas–Sárközy entry](https://mathdb.com/p/414124/erdos-nicolas-sarkozy-conjecture-on-admissible-subsets). Semantic Scholar was consulted for attention metadata; its returned records were insufficient to calculate citation momentum.