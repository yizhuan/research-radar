# Mathematics — Friday, 6 November 2026 arXiv announcement batch — 8 notable recent papers

The strongest pattern is sharp asymptotic bounds and classifications, led by two papers on Tusnády’s discrepancy problem; the agenda moves from combinatorics to high-dimensional percolation, stochastic PDE, arithmetic geometry, and conformal bootstrap. This is an inferred ordering of notable recent work, not an official arXiv trending chart; citation evidence is limited for papers this recent.

## Top papers (ranked)

### 1. [Resolving Tusnády's Problem](https://arxiv.org/abs/2611.06998)
- **Abstract:** For each fixed dimension $d\ge3$, the authors prove an anchored-box discrepancy lower bound of order $(\log N)^{d-1/2}$, which together with known upper and planar lower bounds yields the sharp order for all fixed $d\ge2$.
- **Authors:** Nicola Wengiel
- **arXiv:** `2611.06998v1` (published 2026-11-04 18:58:56 UTC; categories: `math.CA` (primary), `cs.CG`, `cs.DS`, `math.CO`)
- **Evidence for ranking:** A concrete lower bound closes the dimension-at-least-three gap in a longstanding discrepancy problem; the result connects classical analysis, combinatorics, and computational geometry, and its conclusion is explicitly combined with Nikolov’s upper bound and Wei’s planar result.
- **Claimed result:** The author proves $\Omega_d((\log N)^{d-1/2})$ for anchored boxes when fixed $d\ge3$; with the cited matching upper bound and planar lower bound, this gives $\Theta_d((\log N)^{d-1/2})$ for axis-parallel boxes in every fixed $d\ge2$ (arXiv abstract and Theorem 1.1).
- **Assumptions and setting:** Worst-case combinatorial discrepancy of finite $N$-point sets in fixed-dimensional Euclidean space; constants may depend on dimension.
- **Caveat:** The new lower-bound proof is for $d\ge3$; the two-dimensional lower bound and the matching upper bound are prior results used to complete the stated conclusion.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Combinatorics & discrete mathematics

### 2. [Tusnády's problem and online two-sample thinning](https://arxiv.org/abs/2611.08455)
- **Abstract:** The author obtains the sharp fixed-dimensional order for Tusnády discrepancy, a robust deletion lower bound, and minimax bounds for online thinning of two samples, including a sharp one-dimensional separation between prefix and terminal objectives.
- **Authors:** Yuhao Lei
- **arXiv:** `2611.08455v1` (published 2026-11-05 18:47:43 UTC; categories: `math.CO` (primary), `cs.DS`, `math.PR`)
- **Evidence for ranking:** It combines the sharp discrepancy order with a high-probability robustness statement and a separate online sampling application; the cross-listing spans combinatorics, algorithms, and probability.
- **Claimed result:** The author proves the $\Theta_d((\log N)^{d-1/2})$ discrepancy order for fixed $d\ge2$, and for online thinning with fixed $k$ and expected deletion budget $\rho n$, $0<\rho<2$, obtains minimax expected prefix discrepancy $\Theta_{k,\rho}((\log n)^{k+1/2})$; for $k=1$, terminal discrepancy is $\Theta_\rho((\log\log n)^{3/2})$ (arXiv abstract).
- **Assumptions and setting:** Two independent size-$n$ samples from an unknown common distribution; observations must be kept or deleted on arrival, with fixed dimension and stated expected deletion budget. The discrepancy result is for fixed dimension and axis-parallel boxes.
- **Caveat:** For online terminal discrepancy in dimensions $k\ge2$, the paper reports bounds still differing by a factor of $\log n$.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 3. [On the critical value of void percolation in high dimensions](https://arxiv.org/abs/2611.07196)
- **Abstract:** For the random Lorentz gas, the authors prove that the void-percolation threshold grows linearly with dimension, with explicit sufficiently-large-dimension bounds between $d/2$ and $5d$.
- **Authors:** Patrick Charbonneau, Marcus Michelen
- **arXiv:** `2611.07196v1` (published 2026-11-04 22:37:38 UTC; categories: `cond-mat.dis-nn` (primary), `cond-mat.stat-mech`, `math.PR`)
- **Evidence for ranking:** The theorem determines the scaling where prior bounds left even the order unresolved; probability and disordered-systems cross-listing reflects the mathematical-physics setting.
- **Claimed result:** The authors prove $\Phi_{\rm p}(d)=\Theta(d)$ and, for all sufficiently large $d$, $\tfrac12 d\le\Phi_{\rm p}(d)\le5d$ (arXiv abstract; introduction and main results).
- **Assumptions and setting:** A point tracer moves among spherical obstacles centered on a Poisson point process in $\mathbb{R}^d$; the threshold concerns loss of percolation of the vacant region as obstacle density increases.
- **Caveat:** The constants are not sharp and the bounds apply only for sufficiently large $d$; the exact leading coefficient is not determined.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Probability & statistics; Mathematical physics

### 4. [Pointless K3 surfaces over finite fields](https://arxiv.org/abs/2611.08356)
- **Abstract:** The authors prove that a K3 surface with no rational point over $\mathbb{F}_q$ exists exactly when the finite-field size satisfies $q\le11$, using lattice bounds and the Artin–Tate formula.
- **Authors:** Asher Auel, Philip Engel, Kiran S. Kedlaya, Sair Shaikh
- **arXiv:** `2611.08356v1` (published 2026-11-05 17:36:46 UTC; categories: `math.NT` (primary), `math.AG`)
- **Evidence for ranking:** A sharp if-and-only-if classification with a concrete boundary at $q=11$; the argument bridges arithmetic geometry and lattice optimization, and the authors note another proof of the same classification.
- **Claimed result:** The authors prove that pointless K3 surfaces over $\mathbb{F}_q$ exist if and only if $q\le11$ (arXiv abstract and Theorem 1).
- **Assumptions and setting:** Smooth K3 surfaces over finite fields, with $q$ a prime power; “pointless” means having no $\mathbb{F}_q$-rational points.
- **Caveat:** This classifies rational-point existence for K3 surfaces, not for arbitrary varieties; the paper notes that the relationship between its lattice argument and the other proof remains unexplored.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Algebra & number theory; Geometry & topology

### 5. [Weak uniqueness for the stochastic heat equation with nondegenerate diffusion: the full Hölder regime](https://arxiv.org/abs/2611.07310)
- **Abstract:** For the scalar stochastic heat equation on the one-dimensional torus, the author proves weak well-posedness for uniformly nondegenerate diffusion coefficients of every positive Hölder order and gives extensions with measurable drift.
- **Authors:** Yi Han
- **arXiv:** `2611.07310v1` (published 2026-11-05 01:55:58 UTC; categories: `math.PR` (primary))
- **Evidence for ranking:** It resolves the stated weak-uniqueness question across the full positive Hölder range and includes an associated Lean formalization; it is a substantial probability result with an explicit stochastic-PDE setting.
- **Claimed result:** For bounded uniformly nondegenerate Hölder diffusion, the author proves existence and uniqueness in law for the scalar equation at every positive Hölder exponent; a second theorem treats measurable drifts of linear growth under additional alternatives (arXiv abstract and Theorems 1.1–1.2).
- **Assumptions and setting:** One-dimensional torus, scalar equation driven by space-time white noise, deterministic initial data in $L^2$ for the bounded-diffusion theorem, and diffusion bounded above and away from zero with positive Hölder regularity.
- **Caveat:** The theorem is weak uniqueness in this scalar model, not pathwise uniqueness; the unbounded-diffusion extension uses bounded initial data, a restriction the author identifies as a possible future relaxation.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Probability & statistics; Analysis & PDE

### 6. [Exotic smooth structures on complex projective spaces](https://arxiv.org/abs/2611.08406)
- **Abstract:** The authors show that dimensions admitting exotic smooth structures on $\mathbb{CP}^n$ have natural density one and identify 266 residue classes modulo 288, covering over 92% of dimensions, where such structures exist for $n>3$.
- **Authors:** Yueshi Hou, Hana Jia Kong, Zhouli Xu
- **arXiv:** `2611.08406v1` (published 2026-11-05 18:13:47 UTC; categories: `math.AT` (primary))
- **Evidence for ranking:** It gives both an asymptotic density theorem and an explicit modular classification, and links smoothing theory to stable cohomotopy and chromatic homotopy theory.
- **Claimed result:** The authors prove density one of dimensions admitting an exotic smoothing and exhibit 266 congruence classes modulo 288, covering $266/288>92\%$, for which $\mathbb{CP}^n$ has an exotic smooth structure when $n>3$ (arXiv abstract and Theorems B–C).
- **Assumptions and setting:** Smooth manifolds homeomorphic but not diffeomorphic to complex projective space; the explicit residue-class result concerns complex dimensions $n\ge4$.
- **Caveat:** The conjecture that every $n\ge4$ works remains open; density one and more than 92% residue coverage do not settle the remaining dimensions.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Geometry & topology

### 7. [Conformal Bootstrap Unblocked](https://arxiv.org/abs/2611.07004)
- **Abstract:** The authors formulate a conformal-bootstrap hierarchy using reflection-positive Gram matrices, conformal symmetry, and crossing, without taking the operator product expansion or conformal blocks as inputs, and demonstrate bounds in one to three dimensions.
- **Authors:** Li-Yuan Chiang, David Poland
- **arXiv:** `2611.07004v1` (published 2026-11-04 19:00:01 UTC; categories: `hep-th` (primary), `cond-mat.stat-mech`, `hep-lat`, `math-ph`)
- **Evidence for ranking:** It proposes a distinct mathematical-physics method and reports recovery of generalized-free-field behavior and characteristic two- and three-dimensional Ising kinks; the mathematical-physics cross-list makes the archive inclusion explicit.
- **Claimed result:** The authors construct a hierarchy of semidefinite programs from Gram-matrix positivity and show that it yields correlator and spectral bounds, including the stated Ising features, without explicitly using conformal blocks (arXiv abstract and Sections 2–5).
- **Assumptions and setting:** Conformal field theory constraints from conformal symmetry, reflection positivity, crossing, and any added spectral assumptions; demonstrations cover dimensions one through three.
- **Caveat:** The authors report rapidly growing Gram-matrix sizes and leave open whether the hierarchy becomes equivalent to the conventional conformal-block bootstrap at infinite truncation.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Mathematical physics

### 8. [Gradient higher integrability for a general class of degenerate parabolic double phase systems](https://arxiv.org/abs/2611.08291)
- **Abstract:** The authors prove local higher-integrability estimates for weak solutions of generalized double-phase parabolic systems, under structural conditions on the growth functions and the continuity modulus of the phase coefficient.
- **Authors:** Bogi Kim, Jehan Oh, Abhrojyoti Sen
- **arXiv:** `2611.08291v1` (published 2026-11-05 16:54:36 UTC; categories: `math.AP` (primary))
- **Evidence for ranking:** The result extends power-growth gap conditions to general Young-function growth and continuity moduli, with a 54-page argument combining intrinsic stopping times and reverse-Hölder estimates.
- **Claimed result:** For solutions in $L^\infty(0,T;L^s)$, $2\le s<\infty$, the authors establish $\Psi(\cdot,|Du|)\in L^{1+\varepsilon}_{\rm loc}$ for some $\varepsilon>0$ under their stated modulus-to-growth condition (arXiv abstract).
- **Assumptions and setting:** Degenerate parabolic systems with $\Psi(z,\kappa)=G(\kappa)+a(z)H(\kappa)$, Young functions $G,H$ satisfying structural assumptions, nonnegative $a$ with concave parabolic modulus $\omega$, and the explicit limsup condition given in the abstract.
- **Caveat:** The higher-integrability conclusion is conditional on the growth and modulus hypotheses; it is not a general estimate for all degenerate parabolic systems.
- **Announcement type:** new submission, announcement-batch Friday 6 November 2026
- **Themes:** Analysis & PDE

## Trending Research Themes

- **Discrepancy meets online sampling:** The two Tusnády papers (2611.06998, 2611.08455) share the sharp fixed-dimensional order $\Theta_d((\log N)^{d-1/2})$. The first supplies the new $d\ge3$ lower bound used with prior results; the second adds robustness to deleting a small fraction of a sample and online thinning guarantees.
- **Sharp quantitative thresholds across different models:** Void percolation (2611.07196) pins down linear-in-$d$ scaling after the order itself was unknown, while the K3 classification (2611.08356) turns a rational-point question into an exact finite-field cutoff. These are separate techniques, but both replace broad prior uncertainty with explicit boundaries.
- **Geometry translated into algebraic invariants:** The K3 result (2611.08356) uses zeta-function and lattice constraints; exotic smoothings of $\mathbb{CP}^n$ (2611.08406) use stable cohomotopy and chromatic homotopy. Both connect geometric existence questions to computable algebraic structures, without implying a shared proof method.
- **A direct-positivity route for conformal bootstrap:** Chiang and Poland (2611.07004) build semidefinite constraints from Gram positivity and crossing rather than starting from conformal blocks. This is an isolated methodological signal in this batch, not evidence of a field-wide shift.
- **Regularity and uniqueness remain hypothesis-sensitive:** The stochastic heat result (2611.07310) and double-phase estimates (2611.08291) establish progress under carefully stated coefficient and growth assumptions; their settings and proof techniques differ, so the common pattern is conditional sharpness rather than a common method.

## Open Problems and Research Directions

- **Author-stated — Tusnády online terminal bounds:** For dimensions $k\ge2$, the terminal-discrepancy bounds in 2611.08455 still differ by $\log n$. Closing this factor, or finding an example showing it is necessary, directly tests the remaining gap.
- **Synthesis — dimension dependence in discrepancy:** The results in 2611.06998 and 2611.08455 are for fixed dimension with dimension-dependent constants. Tracking those constants as $d$ grows could clarify whether any useful uniform regime is available.
- **Synthesis — void-percolation constant:** The bounds in 2611.07196 leave a wide interval between $d/2$ and $5d$. Sharpening it or establishing whether $\Phi_{\rm p}(d)/d$ converges would test the paper’s numerical comparison; the reported numerical value is not a proof of a limit.
- **Author-stated — K3 proof comparison:** The authors of 2611.08356 note that the relationship between their Artin–Tate/lattice approach and another proof based on Frobenius actions has not been worked out. Comparing the two may simplify the remaining lattice constraints.
- **Author-stated — exotic projective spaces:** The conjecture in 2611.08406 that every $\mathbb{CP}^n$ for $n\ge4$ admits an exotic smoothing remains open. The unclassified residue dimensions are a concrete target for extending the stable-homotopy calculations.
- **Author-stated — conformal bootstrap hierarchy:** Chiang and Poland (2611.07004) identify both numerical efficiency and equivalence with the conventional conformal-block bootstrap in the infinite-truncation limit as unresolved. Testing sparsity-aware Gram matrices and more effective probe states is a direct follow-up.
- **Author-stated — unbounded diffusion at lower initial regularity:** The discussion in 2611.07310 suggests that a finer near-zero-time argument might replace the $L^\infty$ initial-data condition in its unbounded-diffusion theorem with $L^2$ data.

## Takeaway

This batch’s clearest headline is mathematical sharpening: a long-standing discrepancy order is settled in higher dimensions, and a high-dimensional percolation threshold is shown to be linear. Alongside those are exact arithmetic-geometric classifications and method advances in stochastic PDE and conformal bootstrap; because attention metrics are sparse for such recent submissions, this ordering should be read as evidence-informed notability, not measured popularity.

## Method and sources

- **Window:** daily announcement batch, 2026-11-06 through 2026-11-06 UTC. Sunday 2026-11-08 had no newer batch in the listing, so Friday 6 November is the selected prior batch.
- **Snapshot:** 2026-11-08 01:25:21 UTC.
- **Coverage:** the full Mathematics recent listing for Friday 6 November showed 409 of 409 entries. Titles and subject categories were traversed across the complete batch; the eight retained abstracts and metadata were checked against their arXiv abstract pages and API records. For the top three, the arXiv HTML paper text was inspected for introductions and main-result statements; no proof was independently verified.
- **Ranking:** inferred from concrete mathematical claims, cross-listing, explicitly described prior gaps, and identifiable connections or extensions. The ordering is not an arXiv popularity ranking. Independent discussion signals were sparse; searches mostly returned primary records and related prior work.
- **Attention data:** citation and influential-citation evidence could not be obtained from Semantic Scholar in this run. The papers are only a few days old, so this report uses “notable recent papers” rather than implying measured popularity.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent?skip=0&show=500); the linked arXiv abstract pages in each entry; top-three full texts at [2611.06998](https://arxiv.org/html/2611.06998v1), [2611.07196](https://arxiv.org/html/2611.07196v1), and [2611.07004](https://arxiv.org/html/2611.07004v1); and targeted web searches for independent discussion and contextual checks.
