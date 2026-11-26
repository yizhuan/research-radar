# arXiv Trending Mathematics — Daily, 2026-11-26

## Headline

For the 26 November 2026 mathematics announcement batch, this report ranks 11 notable new submissions from the math archive and cross-listed mathematical work. The strongest recurring pattern is mathematical structure translated into explicit criteria, computable representations, or quantitative bounds; the quick tour moves from knot geometry and equivariant K-theory to stochastic transitions and algorithms. arXiv publishes no official trending chart, so this is an inferred ordering—not a readership ranking—and very recent papers have little citation evidence; here the collected attention signals were especially sparse.

## Top papers (ranked)

### 1. [Colored Jones polynomial of figure eight knot and non-perturbative topological recursion](https://arxiv.org/abs/2611.34110)
- **Abstract:** The authors prove that the all-order asymptotic expansion of the figure-eight knot's colored Jones polynomial is related to non-perturbative topological recursion on its elliptic spectral curve.
- **Authors:** Alexander Hock, Sergey Shadrin
- **arXiv:** `2611.34110v1` (published 2026-11-25T10:13:46Z; categories: `math-ph`, `hep-th`, `math.AG`, `math.GT`, `nlin.SI`)
- **Evidence for ranking:** Signal score 1.00, entirely from four cross-lists; the paper spans algebraic geometry and geometric topology as well as mathematical physics. Its knot-invariant/topological-recursion bridge places it first among the tied highest-score candidates.
- **Claimed result:** In the introduction's Theorem 1.1, the authors identify logarithmic differentials of the colored-Jones asymptotic wave function, the recursion wave function, and the matched non-perturbative recursion wave function to all stable orders.
- **Assumptions and setting:** The result is for the figure-eight knot and the specified elliptic spectral curve; the comparison matches the initial disk and amplitude terms of the wave functions.
- **Caveat:** The theorem compares formal/asymptotic objects with different domains of definition, whose analytic behavior requires careful treatment; the result is not stated for general knots.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Geometry & topology; Mathematical physics

### 2. [Noise-induced Extinction in Hierarchical Food Webs](https://arxiv.org/abs/2611.33569)
- **Abstract:** For hierarchical food webs with omnivory, the authors develop a large-deviation account of demographic-noise-driven extinction networks and derive recursive mean-extinction-time formulas.
- **Authors:** Varun Nevash, Eric Forgoston, M. Ani Hsieh
- **arXiv:** `2611.33569v1` (published 2026-11-25T00:32:11Z; categories: `q-bio.PE`, `cond-mat.stat-mech`, `math.DS`, `math.PR`, `nlin.AO`)
- **Evidence for ranking:** Signal score 1.00 from four cross-lists, including both dynamical systems and probability. The authors' general-N extinction-network result and a worked three-species case give it the second position in the top score tier.
- **Claimed result:** Under the stated model, the authors classify feasible communities and their stability, obtain closed-form fluctuational fixed points, and derive an exact recursion for mean extinction times over a network with `3^(N-1)` transitions; for three species they compute route actions numerically and compare predictions with stochastic simulations.
- **Assumptions and setting:** The hierarchical model has a basal reproducing species, consumers may prey on every lower species, trophic conversion efficiency is one, and self-limitation acts only on the basal species.
- **Caveat:** The general classification depends on these interaction and efficiency assumptions; the three-species instanton actions are numerical rather than closed-form results.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 3. [Equivariant K-homology of affine Grassmannians of orthogonal groups](https://arxiv.org/abs/2611.34174)
- **Abstract:** The authors construct symmetric-function models for torus-equivariant K-homology of affine Grassmannians in types B and D, representing both Schubert structure-sheaf and boundary ideal-sheaf classes.
- **Authors:** Koushik Brahma, Takeshi Ikeda, Mark Shimozono
- **arXiv:** `2611.34174v1` (published 2026-11-25T11:03:51Z; categories: `math.AG`, `math.CO`, `math.KT`, `math.RT`)
- **Evidence for ranking:** Signal score 0.75 from three cross-lists across algebraic geometry, combinatorics, K-theory, and representation theory; the explicit type-B/D realization and stated algebra isomorphism rank it highest in this score tier.
- **Claimed result:** Theorem 5.2 identifies the torus-equivariant K-homology algebra for types B and D with an algebra of constructed symmetric functions, matching Schubert structure sheaves and boundary ideal sheaves with explicit basis elements.
- **Assumptions and setting:** The construction concerns affine Grassmannians of orthogonal types B and D and their torus-equivariant K-homology, with equivariant parameters retained.
- **Caveat:** Equivariant parameters are essential in type D: specializing them to zero can identify distinct Schubert classes, so the result does not simply give an equally faithful nonequivariant model.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Geometry & topology; Algebra & number theory

### 4. [Time-consistency of cash-subadditive risk measures: The infimal cocycle property](https://arxiv.org/abs/2611.34192)
- **Abstract:** The authors characterize time consistency of convex cash-subadditive dynamic risk measures using an attained infimal cocycle condition on their minimal penalties.
- **Authors:** Matteo Ferrari, Roger J. A. Laeven, Emanuela Rosazza Gianin, Marco Zullino
- **arXiv:** `2611.34192v1` (published 2026-11-25T11:20:23Z; categories: `q-fin.MF`, `math.OC`, `math.PR`, `q-fin.RM`)
- **Evidence for ranking:** Signal score 0.75 from three cross-lists, including probability and optimization/control; the paper gives an equivalence theorem and connects it to dynamic programming for BSDE-induced risks.
- **Claimed result:** The authors show that time consistency is equivalent to an infimal cocycle property of the minimal penalty, with the infimum attained; in the cash-additive case this reduces to the classical cocycle property.
- **Assumptions and setting:** On `L∞`, continuity from below is assumed; on `L^p` for finite `p`, the abstract states no continuity assumption. The dual variables are conditional sub-probability densities.
- **Caveat:** The equivalence is stated for the specified convex, cash-subadditive framework and depends on the function-space hypotheses; it should not be read as a characterization of arbitrary dynamic risk measures.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Probability & statistics; Optimization & control

### 5. [Fast Algorithms for Permanents of Permutationally-Dominant Matrices](https://arxiv.org/abs/2611.33485)
- **Abstract:** The authors give a fully polynomial randomized approximation scheme for permanents of permutationally-dominant matrices, using a polymer representation and importance sampling.
- **Authors:** Ryan L. Mann
- **arXiv:** `2611.33485v1` (published 2026-11-24T22:02:54Z; categories: `cs.DS`, `cs.CC`, `cs.DM`, `math.CO`)
- **Evidence for ranking:** Signal score 0.75 from three cross-lists, including combinatorics; the explicit approximation guarantee and runtime make it a strong algorithmic result within this tier.
- **Claimed result:** The abstract claims an FPRAS with runtime quadratic in both matrix dimension and inverse approximation error, based on a polymer-model representation and sampling the logarithm of its partition function.
- **Assumptions and setting:** The guarantee applies to the paper's class of permutationally-dominant matrices, not to arbitrary matrices.
- **Caveat:** The approximation result is restricted to that matrix class; the abstract does not claim a general-purpose permanent algorithm with this runtime.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Numerical analysis & computation

### 6. [Reflection subgroups and the Lookup Conjecture](https://arxiv.org/abs/2611.33572)
- **Abstract:** The authors prove the Lookup Conjecture and its affine type-`A` extension, relating Bruhat-graph criteria to rational smoothness of Schubert varieties, and establish a parabolic version for the type-A affine Grassmannian.
- **Authors:** Christian Gaetz, Yibo Gao
- **arXiv:** `2611.33572v1` (published 2026-11-25T00:36:04Z; categories: `math.CO`, `math.AG`, `math.RT`)
- **Evidence for ranking:** Signal score 0.50 from two cross-lists in algebraic geometry and representation theory; a named conjecture resolution and a parabolic extension give it priority within this score tier.
- **Claimed result:** The authors prove the original Boe–Graham conjecture, its `A~_n` extension, and a parabolic version for the type-A affine Grassmannian, with a stronger Bruhat-graph degree monotonicity property in the latter setting.
- **Assumptions and setting:** The original criterion concerns Schubert varieties in a complex reductive group's flag variety; the extension concerns affine Kac–Moody type `A~_n` and the type-A affine Grassmannian.
- **Caveat:** The authors say extension to other Kac–Moody groups would require checking the rank-three reflection subgroups of the corresponding Weyl group.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Geometry & topology; Combinatorics & discrete mathematics

### 7. [Sharp decay and regularity thresholds for Minkowski stability in spherical symmetry](https://arxiv.org/abs/2611.34283)
- **Abstract:** For the spherically symmetric Einstein–scalar field system, the authors prove borderline small-data stability thresholds and construct trapped spheres below either threshold.
- **Authors:** Dawei Shen, Jingbo Wan
- **arXiv:** `2611.34283v1` (published 2026-11-25T12:37:40Z; categories: `gr-qc`, `math-ph`, `math.AP`)
- **Evidence for ranking:** Signal score 0.50 from two cross-lists, including analysis of PDEs; the paired stability and sharpness claims provide a concrete mathematical result within this score tier.
- **Claimed result:** The authors prove global closeness to Minkowski spacetime and future causal geodesic completeness for small smooth characteristic data at borderline decay and half-derivative regularity, and show both thresholds are sharp by constructing initially untrapped data that form trapped spheres below them.
- **Assumptions and setting:** The theorem is for spherical symmetry and small smooth characteristic data measured in weighted derivative seminorms in the Einstein–scalar field system.
- **Caveat:** The result is confined to spherical symmetry; it does not settle corresponding threshold questions without that symmetry restriction.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Analysis & PDE; Mathematical physics

### 8. [Prophet Inequalities for Mixtures of I.I.D. Random Variables](https://arxiv.org/abs/2611.34264)
- **Abstract:** In a sequential selection problem with an unknown latent component governing conditionally i.i.d. nonnegative observations, the authors determine the best worst-case prophet-inequality factor as `1/e + 1/k^(2/3+o(1))`.
- **Authors:** Felix Fischer, Kevin Schewior
- **arXiv:** `2611.34264v1` (published 2026-11-25T12:26:10Z; categories: `math.ST`, `cs.DS`, `math.OC`)
- **Evidence for ranking:** Signal score 0.50 from two cross-lists spanning statistics, algorithms, and optimization; the matching upper/lower guarantee with an explicit asymptotic factor is the differentiator within this tier.
- **Claimed result:** The authors prove that the largest universally guaranteed fraction of the expected maximum is `1/e + 1/k^(2/3+o(1))`; they give a secretary-rule lower bound and a common-scale-model upper-bound construction.
- **Assumptions and setting:** A latent index `J` is drawn from a known prior over `k` component distributions; conditional on `J`, observations are i.i.d. from a known nonnegative distribution, while `J` is not observed. The expected maximum is finite.
- **Caveat:** The stated correction is asymptotic in the number `k` of mixture components, and the model assumes the prior and all component distributions are known to the selector.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics; Optimization & control

### 9. [Schwinger-Dyson recursion, Gröbner elimination and graph combinatorics](https://arxiv.org/abs/2611.34114)
- **Abstract:** The authors use Gröbner elimination to close zero-dimensional Schwinger–Dyson systems and derive linear-arithmetic-operation recursions for counting labelled 9- and 10-regular graphs.
- **Authors:** Oleg Evnin
- **arXiv:** `2611.34114v1` (published 2026-11-25T10:17:13Z; categories: `math-ph`, `hep-th`, `math.CO`)
- **Evidence for ranking:** Signal score 0.50 from two cross-lists, including combinatorics; the paper bridges algebraic elimination, mathematical physics, and graph enumeration with a concrete complexity claim.
- **Claimed result:** For labelled 9- and 10-regular graphs on `n` vertices, the authors derive a finite-depth, finite-width recursion that computes total graph counts in `O(n)` arithmetic operations.
- **Assumptions and setting:** The method uses zero-dimensional QFT with polynomial actions, interpreted as multivariate Gaussian integrals with polynomial insertions, and applies the stated counting result to degrees 9 and 10.
- **Caveat:** The abstract's linear-operation result is specific to 9- and 10-regular graph counts; it does not state the same complexity for arbitrary degrees or graph-counting problems.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Mathematical physics

### 10. [Generic non-convergence of low-temperature Ising Glauber dynamics on Z²](https://arxiv.org/abs/2611.34193)
- **Abstract:** At sufficiently low positive temperature, a dense `Gδ` set of translation-invariant initial laws for the two-dimensional zero-field Ising heat-bath dynamics has both plus and minus phases as subsequential limits, so distributional convergence is meagre.
- **Authors:** Jonas Köppl, Yannic Steenbeck
- **arXiv:** `2611.34193v1` (published 2026-11-25T11:21:03Z; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** Signal score 0.25 from one cross-list into mathematical physics; the paper also gives a partial answer to a stated open problem about convergence of Ising dynamics.
- **Claimed result:** The authors prove the dense-`Gδ` and meagreness statements for nearest-neighbour, zero-field Ising dynamics on `Z²`; they state the conclusion also applies to all reversible monotone Glauber dynamics for the Ising model.
- **Assumptions and setting:** Initial laws are translation invariant, the temperature is sufficiently low and positive, and genericity is in the weak topology on the space of such laws.
- **Caveat:** “Generic” here is topological, not a probability-one claim; the theorem is limited to a low-temperature regime and the specified dynamics and initial-law space.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 11. [Irreducible trinomials over the binary field: an elliptic-curve criterion and explicit families](https://arxiv.org/abs/2611.34282)
- **Abstract:** The authors give an elliptic-curve and reciprocity criterion for a family of binary trinomials and construct infinite irreducible-trinomial families in fourteen reduced exponent classes.
- **Authors:** Siyuan Fu, Zhiming Li, Huaiqing Zuo
- **arXiv:** `2611.34282v1` (published 2026-11-25T12:37:10Z; categories: `math.NT`, `math.AG`)
- **Evidence for ranking:** Signal score 0.25 from one cross-list between number theory and algebraic geometry; the paper's explicit if-and-only-if criterion makes it a notable cross-field result among the remaining score-tier candidates.
- **Claimed result:** For `k ≥ 2`, the authors prove that `X^((4^k+2)/3)+X+1` is irreducible over `F₂` exactly when `4^k+3` is prime and 2 is a primitive root modulo that prime, and they give explicit infinite families in fourteen reduced exponent classes.
- **Assumptions and setting:** The criterion concerns the displayed trinomial over the binary field and integers `k ≥ 2`; the family construction uses power substitution and linearization.
- **Caveat:** The criterion is for a specific exponent family; the abstract does not claim a complete classification of all irreducible binary trinomials.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Algebra & number theory

## Trending Research Themes

- Several papers turn geometric or algebraic structure into explicit combinatorial data: the figure-eight colored-Jones/topological-recursion comparison (2611.34110), symmetric-function models for orthogonal affine-Grassmannian K-homology (2611.34174), and Bruhat-graph criteria for Schubert rational smoothness (2611.33572). These are separate constructions, not evidence of a shared technique across the archive.
- Probability appears through three different lenses: WKB/large deviations and extinction networks (2611.33569), topological Baire-category non-convergence for Ising dynamics (2611.34193), and worst-case sequential selection guarantees (2611.34264). The common thread is sharp characterization of long-time or sequential behavior, while the proof methods and meanings of “typical” differ.
- Explicit quantitative guarantees also connect combinatorics and computation: the FPRAS for a restricted permanent class (2611.33485), the `O(n)` arithmetic recursion for two regular-graph degrees (2611.34114), and the prophet factor for latent mixtures (2611.34264). The assumptions differ substantially, so these results are adjacent examples rather than a single trend in algorithmic method.
- There are focused mathematical interfaces with applications: cash-subadditive risk measures and stochastic control (2611.34192), and Einstein–scalar PDE stability with geometric completeness and trapped-sphere formation (2611.34283). Each paper's theorem is tied to its own stated hypotheses.

## Open Problems and Research Directions

- **Author-indicated extension:** Gaetz and Gao say their method could extend the Lookup criterion to other Kac–Moody groups after checking rank-three reflection subgroups (2611.33572). A concrete next step is to identify which rank-three configurations suffice in further affine or non-affine types and test whether the criterion survives.
- **Author-stated partial problem:** The Ising paper gives only a partial answer to Liggett's open question about convergence in distribution (2611.34193). Clarifying the boundary between convergence and non-convergence outside the sufficiently-low-temperature regime, or for initial laws outside the translation-invariant space, would probe the scope of the result; these are proposed extensions, not claims made by the authors.
- **Hypothesis boundary and proposed direction:** The Einstein–scalar result establishes sharp thresholds in spherical symmetry and constructs trapped spheres below either threshold (2611.34283). A natural follow-up is to test whether analogous thresholds or counterexamples persist without spherical symmetry and under weaker regularity classes.
- **Author-motivated programme:** The K-homology paper points toward Pieri/Giambelli formulas, positivity of structure constants, and quantum K-theory of orthogonal flag varieties, while stressing that equivariant parameters distinguish classes in type D (2611.34174). Deriving these formulas before and after carefully controlled specialization would test how much structure survives nonequivariantly.
- **Scope extension (synthesis):** The proved recursion/topological-recursion comparison is specific to the figure-eight knot (2611.34110). Applying the same matched-wave-function analysis to other knots with different spectral curves would test which parts are knot-specific and which follow from the general non-perturbative recursion framework.

## Takeaway

This batch contains several precise bridges—between knot invariants and recursion, geometry and symmetric functions, and stochastic models and explicit quantitative guarantees—alongside isolated advances in PDE, number theory, and combinatorics. The ranking is a thin-signal triage of a broad archive window, not a measure of community consensus or mathematical importance.

## Method and sources

- **Window:** daily announcement batch covering first submissions from 2026-11-24 19:00:00 UTC through 2026-11-25 19:00:00 UTC; announced 2026-11-26 at 01:00 UTC. This is the current day's batch, not a prior announcement. Snapshot: 2026-11-26 03:15:11 UTC.
- **Scope:** arXiv Mathematics archive (`math.*`) and mathematical work cross-listed with math categories; selected papers retain their primary and cross-list categories. All 11 are new submissions in the window, not revisions.
- **Candidate signals:** `/home/yizhuan/.research/math/daily/arxiv-trending-math-daily-2026-11-26.signals.json` reports 224 arXiv records, 224 pool-size records, and 150 candidate entries in the saved file. Its note says the pool can be non-exhaustive for very large categories. The 11 papers were selected from those candidates; each selected arXiv abstract page was checked directly, and the introduction/main result material was also inspected for the leading three where the HTML text was available.
- **Inference:** the candidate file reports zero candidates with external attention (`with_attention: 0`); for these selected papers, the listed score components are cross-list counts only, weighted at 0.25 per cross-list (e.g. four cross-lists yield a reported score of 1.00). Scores order the candidates in broad tiers; within tied tiers, the ordering uses the specificity and scope of the stated mathematical result, not author or institution prestige. A zero score is not evidence of low importance. HF and Hacker News collection sources reported `ok`, but no attention signal was attached to these candidates. Semantic Scholar data was unavailable in the collector run, so citation and influential-citation signals were not used. The arXiv abstract listing source returned 224 records, while the saved candidate file contains 150 entries; this report therefore does not claim an exhaustive ranking of every paper in the window.
- **Primary sources:** the selected arXiv abstract pages linked above; arXiv recent Mathematics listing: https://arxiv.org/list/math/recent; candidate-signal file cited above. `web_extract` could not extract pages with the configured search-only backend, so arXiv pages were verified in the browser instead.
