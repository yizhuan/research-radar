# arXiv Mathematics — 25 November 2026

Eight notable papers from the 25 November announcement batch, spanning heat-kernel analysis, Hamiltonian Monte Carlo, operator algebras, nonlinear waves, and number theory. The clearest shared pattern is work turning structural hypotheses into sharper characterizations or quantitative bounds; we’ll look at those bridges, then at several isolated theorem-level advances. This is an inferred ranking, not an official arXiv trending chart: the available attention evidence is sparse, and recent citation data is unavailable, so the ordering should not be read as a popularity measure.

## Top papers (ranked)

### 1. [Spectral characterizations of sub-Gaussian heat kernel bounds](https://arxiv.org/abs/2611.31712)
- **Abstract:** The authors construct a planar counterexample to eigenvalue-only criteria for sub-Gaussian heat-kernel bounds, then give a characterization using first Dirichlet eigenpairs under geometric and analytic hypotheses.
- **Authors:** Phanuel Mariano, Jing Wang
- **arXiv:** `2611.31712v1` (published 2026-11-24T00:03:42Z; categories: `math.PR`, `math.AP`, `math.FA`, `math.MG`)
- **Evidence for ranking:** Collector score 0.75, entirely from three cross-lists; placed first for combining a concrete counterexample with a corrected spectral characterization and a stated resolution of a prior conjecture.
- **Claimed result:** The authors show that the bottom Dirichlet eigenvalue on balls alone does not characterize the heat-kernel upper bound, and prove an equivalence using the first eigenvalue together with a uniform comparison of the first eigenfunction's supremum and its value at the ball center.
- **Assumptions and setting:** The main equivalence is for unbounded proper geodesic Dirichlet spaces with volume doubling, reverse volume doubling, and a scale-\(r^\beta\) Poincaré inequality; an additional exit-time/spectral equivalence is stated under an elliptic Harnack inequality.
- **Caveat:** The planar counterexample warns against dropping exit-time controls; the positive characterization is conditional on the stated space and regularity assumptions.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Probability & statistics; Analysis & PDE; Geometry & topology

### 2. [Spatial switching near a four-loop homoclinic bouquet: a mechanism for multi-bump bound states in coupled nonlinear Schrödinger systems](https://arxiv.org/abs/2611.31846)
- **Abstract:** In a four-dimensional Hamiltonian reduction of a coupled nonlinear Schrödinger system, the authors show that a transverse intersection of invariant manifolds near a four-loop homoclinic bouquet yields infinitely many multi-bump homoclinic orbits.
- **Authors:** Sajjad Bakrani
- **arXiv:** `2611.31846v1` (published 2026-11-24T02:40:27Z; categories: `math.DS`, `math-ph`, `nlin.PS`, `physics.optics`)
- **Evidence for ranking:** Collector score 0.75, entirely from three cross-lists; the placement reflects the explicit conditional multiplicity theorem linking Hamiltonian dynamics to localized wave states.
- **Claimed result:** Given a transverse intersection away from the bouquet (a super-homoclinic orbit), the author proves the existence of infinitely many multi-bump homoclinic orbits, corresponding to multi-bump localized standing waves.
- **Assumptions and setting:** The saddle eigenvalues satisfy 0 < λ₁ < λ₂ < 2λ₁, with further nondegeneracy assumptions; the conclusion is conditional on the transverse intersection of the constructed invariant manifolds.
- **Caveat:** The abstract does not establish that the required transverse intersection occurs for a particular parameter regime of the coupled system.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Mathematical physics; Analysis & PDE

### 3. [Breaking Resonance: Square-root acceleration for Metropolis-adjusted randomized Hamiltonian Monte Carlo](https://arxiv.org/abs/2611.32322)
- **Abstract:** For randomized integration-time laws satisfying a Fourier non-resonance condition, the author proves a warm-start mixing bound for Metropolis-adjusted HMC with velocity Verlet and gives a lower-bound example when Hessian regularity is removed.
- **Authors:** Nawaf Bou-Rabee
- **arXiv:** `2611.32322v1` (published 2026-11-24T10:14:55Z; categories: `math.PR`, `math.NA`, `stat.CO`)
- **Evidence for ranking:** Collector score 0.50, entirely from two cross-lists; ranked highly for a quantified mixing result, a matching cautionary lower bound, and a linked Lean 4 formalization of the main results.
- **Claimed result:** For an m-strongly convex potential with L-Lipschitz gradient and L_H-Lipschitz Hessian, expected gradient evaluations to reach fixed total-variation accuracy are, up to constants and logarithmic factors, of order √(κd) + √(L_H)(d/m)^(3/4), with κ=L/m. The paper also gives a κ^(2/3)-scale obstruction, up to logarithms, when Hessian regularity is absent.
- **Assumptions and setting:** The upper bound assumes a warm start, fixed step-size Verlet integration, the stated strong-convexity/smoothness conditions, and a non-resonant duration law; uniform, exponential, and triangular laws are given as examples.
- **Caveat:** The authors explicitly do not establish optimality of the upper bound's L_H dependence; Hessian regularity matters for fixed-step performance.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Probability & statistics; Numerical analysis & computation

### 4. [Monadicity of noncommutative measurable spaces over C*-algebras](https://arxiv.org/abs/2611.32363)
- **Abstract:** The authors establish a monadic description of σ-C*-algebras over C*-algebras and derive universal descriptions of probabilistic morphisms, local presentability, a tensor product, and a formulation of CP-instruments.
- **Authors:** Fosco Loregian, Antonio Lorenzin
- **arXiv:** `2611.32363v1` (published 2026-11-24T10:33:06Z; categories: `math.OA`, `math.CT`, `math.FA`)
- **Evidence for ranking:** Collector score 0.50, entirely from two cross-lists; ranked for a structural theorem that connects category theory and operator algebras and supports several explicitly stated consequences.
- **Claimed result:** The authors prove that the forgetful functor from σ-C*-algebras with σ-normal *-homomorphisms to C*-algebras is monadic, and use this framework to characterize σ-cpu maps, construct a tensor product, and obtain a correspondence for σ-CP-instruments.
- **Assumptions and setting:** The results concern monotone σ-complete C*-algebras and σ-normal morphisms; the paper builds on the authors' proposed noncommutative analogue of measurable spaces.
- **Caveat:** The paper notes that the resulting symmetric monoidal category is not closed; the framework is a proposed analogue, not an equivalence with ordinary measurable spaces in full generality.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Algebra & number theory; Logic & foundations

### 5. [Blow-up size for the noncommutative rank of linear symbolic matrices with low-rank coefficients](https://arxiv.org/abs/2611.31963)
- **Abstract:** For a linear symbolic matrix whose nonconstant coefficient matrices have rank at most r, the author proves that every blow-up size k ≥ r attains its noncommutative rank and derives algorithmic and polyhedral consequences.
- **Authors:** Yuni Iwamasa
- **arXiv:** `2611.31963v1` (published 2026-11-24T05:12:32Z; categories: `math.CO`, `cs.DM`, `math.RA`)
- **Evidence for ranking:** Collector score 0.50, entirely from two cross-lists; the placement reflects a precise rank-bounded stabilization theorem with computational and polyhedral applications.
- **Claimed result:** The author proves that blow-up size k ≥ r suffices when the nonconstant coefficient matrices have rank at most r, and gives a randomized nc-rank algorithm for fixed r plus stabilization of a related polytope hierarchy at level r.
- **Assumptions and setting:** The matrices may be rectangular over an arbitrary field; the coefficient A₀ is unrestricted, while each other coefficient has rank at most r. The stated arithmetic-operation bound assumes a sufficiently large field and constant r.
- **Caveat:** The algorithmic consequence is restricted to fixed coefficient-rank bound and sufficiently large fields; the theorem does not claim an analogous fixed-size bound without the low-rank hypothesis.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 6. [Gaps between zeros of Epstein zeta-functions of binary quadratic forms on the critical line](https://arxiv.org/abs/2611.32154)
- **Abstract:** For integral binary quadratic forms with nonsquare discriminant up to sign, the authors prove that the associated Epstein zeta-function has a critical-line zero within T^(2/5+ε) of every sufficiently large height T, improving prior exponents in several cases.
- **Authors:** Stephan Baier, Srinivas Kotyada, Usha Keshav Sangale
- **arXiv:** `2611.32154v1` (published 2026-11-24T08:08:30Z; categories: `math.NT`)
- **Evidence for ranking:** Collector score 0.00; selected as a notable result for an explicit improvement below the classical 1/2 exponent for indefinite forms and an especially strong 1/3 exponent in the stated negative-discriminant case.
- **Claimed result:** The authors establish a T^(2/5+ε) proximity bound for all sufficiently large T; for discriminant −4m² with m odd they obtain exponent 1/3. Their method includes an additive-twist Voronoi formula and two-dimensional Weyl differencing.
- **Assumptions and setting:** Q is an integral binary quadratic form whose discriminant, up to sign, is not a perfect square; the bound is for zeros on the critical line and for all sufficiently large T.
- **Caveat:** The exponents retain an arbitrary ε-loss, and the result does not assert a uniform exponent of 1/3 for every eligible discriminant.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Algebra & number theory

### 7. [The optimal exponent in the Babai-Goodman-Pyber theorem](https://arxiv.org/abs/2611.32149)
- **Abstract:** For a finite group X and soluble subgroup H, the author identifies the least exponent bounding [X:Rad(X)] by a power of [X:H], and proves sharpness of the associated coefficient in the nonsoluble case.
- **Authors:** Shaowu Zheng
- **arXiv:** `2611.32149v1` (published 2026-11-24T08:04:51Z; categories: `math.GR`)
- **Evidence for ranking:** Collector score 0.00; selected as a notable result because it determines the exact optimal exponent and gives examples establishing sharpness, rather than for a measured attention signal.
- **Claimed result:** The author proves that the least possible exponent is b₀ = 1 + log₉(168·24^(1/3)) ≈ 3.8141 and that the coefficient 24^(−1/3) in the stronger nonsoluble-group inequality is optimal.
- **Assumptions and setting:** X is finite and H is a soluble subgroup; Rad(X) is the largest soluble normal subgroup. The proof reduces to bounds on soluble subgroups of automorphism groups of finite simple groups.
- **Caveat:** The result is confined to finite groups and soluble subgroups; sharpness is demonstrated by examples based on PSL₂(8), not by a classification of all equality cases.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Algebra & number theory

### 8. [An improved estimate for discrete L^8 restriction on the cubic curve](https://arxiv.org/abs/2611.32210)
- **Abstract:** The authors prove a discrete eighth-moment restriction estimate for the cubic curve (n,n³), saving a factor N^(1/47500) over the N^(1/2+ε) scale.
- **Authors:** Xudong Lai, Hongxu Wu
- **arXiv:** `2611.32210v1` (published 2026-11-24T08:55:38Z; categories: `math.CA`)
- **Evidence for ranking:** Collector score 0.00; included as a concrete harmonic-analysis bound improvement, with its displayed power saving providing a checkable mathematical basis for selection.
- **Claimed result:** For every ε>0, the paper bounds the eighth moment of Σ_{n≤N} b_n exp(2πi(nx+n³y)) over [0,1]² by a constant depending on ε times N^(1/2−1/47500+ε)(Σ|b_n|²)^4.
- **Assumptions and setting:** The estimate is for the stated cubic frequency set, arbitrary coefficients bₙ, and every ε>0; the implied constant may depend on ε.
- **Caveat:** The power saving 1/47500 is small, and the abstract does not claim that the exponent is optimal.
- **Announcement type:** new submission, 2026-11-25 announcement batch
- **Themes:** Analysis & PDE

## Trending Research Themes

- **Spectral criteria for diffusion:** Mariano and Wang combine a planar counterexample with a first-eigenpair characterization of sub-Gaussian heat-kernel bounds. The technical lesson is that eigenvalue scale alone may miss how the diffusion travels; the first eigenfunction and exit-time controls matter under the paper's stated hypotheses.
- **Randomization and quantitative stability:** Bou-Rabee connects a Fourier non-resonance condition on HMC trajectory lengths to mixing, and isolates Hessian regularity as a source of fixed-step stability. This is a specific algorithmic result, not evidence of a field-wide shift.
- **Structural algebraic frameworks:** Loregian and Lorenzin use monadicity to organize noncommutative probability maps and tensor products; Iwamasa instead bounds the matrix blow-up scale needed to attain noncommutative rank. These are separate algebraic bridges, not a shared method.
- **Isolated theorem-level advances:** Bakrani's conditional multi-bump construction, Baier–Kotyada–Sangale's zero-gap exponent, Zheng's optimal finite-group exponent, and Lai–Wu's small discrete-restriction power saving are distinct signals across dynamics, number theory, group theory, and harmonic analysis. Eight selected papers do not support a claim of a broader disciplinary shift.

## Open Problems and Research Directions

- **Author-stated limitation:** Bou-Rabee states that the paper does not settle optimality of the upper bound's dependence on L_H. A follow-up could seek matching lower bounds or improve that dependence while keeping the same warm-start and duration-law framework. [2611.32322]
- **Conditional gap in the wave result:** Bakrani's infinite multi-bump conclusion requires transverse intersection of the invariant manifolds; the abstract does not provide parameter conditions ensuring that intersection. Establishing such conditions in concrete coupled-NLS regimes would turn the mechanism into an existence criterion. [2611.31846]
- **Scope of the heat-kernel characterization:** Mariano and Wang's positive equivalence uses volume doubling, reverse volume doubling, a scale-dependent Poincaré inequality, and first-eigenfunction control. Testing which assumptions can be weakened—without repeating the planar failure of eigenvalue-only criteria—is a natural extension suggested by their counterexample. [2611.31712]
- **Reported structural limitation:** Loregian and Lorenzin note that their symmetric monoidal category is not closed. A follow-up could characterize whether a useful closure property holds under additional restrictions, particularly in settings related to the paper's commutative-object case. [2611.32363]
- **Exponent frontier:** Baier, Kotyada, and Sangale reach 1/3 for discriminants −4m² with m odd and 2/5+ε in the general eligible case. Improving the general exponent or identifying further discriminant families with stronger bounds would test the method's reach. [2611.32154]

## Takeaway

The strongest mathematical thread is sharper characterization: a spectral counterexample forces more precise heat-kernel hypotheses, while randomized HMC and noncommutative rank work derive quantitative guarantees from structural conditions. The batch also contains several strong but largely isolated advances; since the available attention signals did not measure readership or citation momentum, their ordering is a curated inference rather than a popularity claim.

## Method and sources

- **Window:** daily batch, 2026-11-23 19:00:00 UTC through 2026-11-24 19:00:00 UTC; announced 2026-11-25 at 01:00:00 UTC. This is the latest batch, not a prior-batch substitute. Snapshot: 2026-11-25 03:14:20 UTC.
- **Coverage:** arXiv Mathematics archive (`math.*`). The date-window API query returned all 235 matching records; the supplied signal file reports `pool_size: 235` but stores 150 candidate records. Selected papers were chosen from that signal candidate set and individually verified on their arXiv abstract pages. All eight are v1 submissions in this batch.
- **Ranking:** the supplied signal file is primary for attention evidence. Its 150 stored candidates have `with_attention: 0`; HF and Hacker News collection statuses were OK, but no attention was recorded. Scores used here are cross-list-only: 0.75 for three cross-lists; 0.50 for two; 0.00 means no external attention was found, not that a paper is unimportant. Ties and zero-score selections are ordered by the concrete result and its stated mathematical scope, not author prestige or arXiv listing order. No official arXiv trending chart exists.
- **Unavailable source:** Semantic Scholar collection was unavailable in the supplied run, so citation counts and influential-citation signals could not be used. No citation figures are inferred.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); arXiv API date-window query for `cat:math.*` and 2026-11-23 19:00–2026-11-24 19:00 UTC; supplied signal file `/home/yizhuan/.research/math/daily/arxiv-trending-math-daily-2026-11-25.signals.json`; the eight linked arXiv abstract pages above. The introductions and main-result statements of the first three were also inspected via their arXiv HTML versions. No proof verification or independent acceptance status is claimed.
