# arXiv mathematics — 30 October 2026 batch: 10 notable papers

The batch's strongest pattern is sharp thresholds and quantitative limits: from Euler-flow uniqueness to tropical enumeration, random models, and stability inequalities. This report ranks ten papers for a short tour of those results and their conditions. The ordering is inferred, not an official arXiv trending chart; arXiv publishes no such chart, and the selected papers are too new for robust citation-based attention evidence.

## Top papers (ranked)

### 1. [The Number of Tropical Order Types and Coherent Matching Fields](https://arxiv.org/abs/2610.40622)
- **Abstract:** The authors bound counts of coherent matching fields, tropical hyperplane sequences, regular triangulations, and labeled order types, comparing the combinatorial expressivity of linear programs and mean-payoff games.
- **Authors:** Xavier Allamigeon, Yiyuan Chen, Stéphane Gaubert, Xavier Goaoc
- **arXiv:** `2610.40622v1` (published 2026-10-29 17:56:09 UTC; categories: `math.CO`, `math.AG`, `math.OC`)
- **Evidence for ranking:** Three-way cross-listing across combinatorics, algebraic geometry, and optimization/control; the paper gives matching first-order asymptotics for several related structures and answers a named counting question of Santos about regular triangulations.
- **Claimed result:** For fixed rank, the number of regular triangulations of the product of simplices Δⁿ⁻¹ × Δʳ⁻¹ is n^((r−1)²n+o(n)); the authors also compare real and signed-tropical labeled order types and show a collapse after double tropicalization. This summarizes Theorems 1.1–1.4 and Corollary 1.2 in the paper.
- **Assumptions and setting:** The asymptotic statements take n to infinity with rank/dimension fixed; the counts concern labeled structures and, for the tropical hyperplane theorem, general-position sequences.
- **Caveat:** These first-order counts do not resolve every finer asymptotic or unlabeled enumeration question; the fixed-rank regime should not be read as uniform in rank.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Combinatorics & discrete mathematics; Optimization & control; Algebra & number theory

### 2. [A Sharp Uniqueness-Nonuniqueness Dichotomy for Neutral Vortex Arrays in 2D Euler Equations](https://arxiv.org/abs/2610.40552)
- **Abstract:** For stationary arrays of disjoint neutral vortices, the authors give an integral test on the growth envelope of vorticity Lᵖ norms that separates uniqueness for every datum in the class from existence of a datum with two distinct evolutions.
- **Authors:** Thomas Y. Hou, Xiang Qin, Peicong Song, Wenhan Zhang
- **arXiv:** `2610.40552v1` (published 2026-10-29 17:39:18 UTC; categories: `math.AP`)
- **Evidence for ranking:** The paper states a sharp two-sided criterion within a precisely defined Euler data class, with both a uniqueness theorem and a matching nonuniqueness construction; a companion submission in this batch treats nonuniqueness for each fixed finite p.
- **Claimed result:** Theorem 1.3 says that for a finite nondecreasing envelope Θ, IΘ = ∫ₚ₀∞ dp/Θ(p) diverging gives uniqueness for every datum in the stationary neutral-array class, while a finite integral yields at least one datum with two distinct unforced Lagrangian Euler evolutions.
- **Assumptions and setting:** Two-dimensional incompressible Euler on ℝ²; compactly supported stationary arrays of disjoint radial neutral vortices, with the prescribed envelope controlling all finite vorticity Lᵖ norms.
- **Caveat:** The authors explicitly leave open whether the classical Yudovich uniqueness threshold is sharp for general unbounded vorticities; their dichotomy depends on the restricted array geometry and exact shielding.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Analysis & PDE

### 3. [JT gravity as a conformal scaling limit of random flat combinatorial disks](https://arxiv.org/abs/2610.40645)
- **Abstract:** A Boltzmann ensemble of rectilinear combinatorial disks converges, after rescaling a distinguished side to large length, to a continuum random surface described by flat Jackiw–Teitelboim gravity.
- **Authors:** Morris Ang
- **arXiv:** `2610.40645v1` (published 2026-10-29 17:59:13 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** The result connects discrete random geometry, probability, and mathematical physics; the paper also supplies a branching-exploration criterion intended to transfer the scaling-limit proof to other discrete disk models.
- **Claimed result:** Theorem 1.1 proves convergence in distribution of the uniformly parametrized conformal factors of Boltzmann rectilinear disks, after subtracting log B, to the flat JT surface as base length B tends to infinity. Theorem 1.3 gives a general criterion based on a Markov exploration, tightness, and convergence of exploration data.
- **Assumptions and setting:** The proved model is the critical Boltzmann ensemble of rectilinear flat disks with a distinguished base; convergence is uniform on compact subsets in the stated conformal coordinates. The general criterion has additional exploration hypotheses.
- **Caveat:** The paper proves the limit for this ensemble, not for every discretization of flat surfaces; extension to triangulations and quadrangulations is presented as a route or expectation, not as an established result here.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Probability & statistics; Mathematical physics; Combinatorics & discrete mathematics

### 4. [On Zeros and Algorithms for Disordered Systems II: The Antiferromagnetic Ising Model up to Kesten-Stigum](https://arxiv.org/abs/2610.40598)
- **Abstract:** The authors give a polynomial-time, arbitrarily accurate partition-function estimator for the antiferromagnetic Ising model on a uniformly random regular graph up to the Kesten–Stigum threshold, using a high-probability zero-free region.
- **Authors:** Ferenc Bencs, Brice Huang, Daniel Z. Lee, Kuikui Liu, Guus Regts
- **arXiv:** `2610.40598v1` (published 2026-10-29 17:50:26 UTC; categories: `cs.DS`, `cond-mat.dis-nn`, `math-ph`, `math.PR`)
- **Evidence for ranking:** Four-category cross-listing and a concrete algorithmic result tied to a zero-free theorem; the abstract identifies the threshold as the full replica-symmetric regime and a conjectured boundary for efficient counting and sampling.
- **Claimed result:** The authors claim the first polynomial-time algorithm achieving arbitrarily high accuracy for the partition function throughout the stated inverse-temperature range, and prove that Fisher zeros are absent from a constant-width strip around that range with high probability over the random graph.
- **Assumptions and setting:** Antiferromagnetic Ising model on a uniformly random d-regular graph; the algorithmic guarantee is for inverse temperatures up to the Kesten–Stigum threshold and the zero-free statement is with high probability over the input graph.
- **Caveat:** The paper does not establish algorithmic tractability beyond the threshold or prove that the threshold is an optimal boundary; optimality is described as conjectured.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Mathematical physics; Probability & statistics; Combinatorics & discrete mathematics

### 5. [A self-normalized law of the iterated logarithm for Rademacher random multiplicative functions](https://arxiv.org/abs/2610.40605)
- **Abstract:** For a squarefree-supported Rademacher random multiplicative function, the authors prove a two-sided law of the iterated logarithm for its partial sums when normalized by the full predictable quadratic variation.
- **Authors:** Dariusz Buraczewski, Alexander Iksanov
- **arXiv:** `2610.40605v1` (published 2026-10-29 17:52:57 UTC; categories: `math.PR`, `math.NT`)
- **Evidence for ranking:** A precise almost-sure limit theorem connects probability and number theory, with an explicit random normalization and cluster set rather than only an order-of-magnitude bound.
- **Claimed result:** For M(x)=∑ₙ≤ₓ f(n) and the full predictable quadratic variation Q(x), the authors prove limsup M(x)/√(2Q(x)log log x)=1 and liminf =−1 almost surely; the normalized cluster set is [−1,1].
- **Assumptions and setting:** f is a Rademacher random multiplicative function supported on squarefree integers; Q(x) is the predictable quadratic variation of the martingale obtained by revealing prime signs.
- **Caveat:** The authors do not determine which alternative holds for the separate limsup normalized by √x(log log x)^(1/4): it may be a finite positive nondegenerate random variable or infinite almost surely.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Probability & statistics; Algebra & number theory

### 6. [Supersaturation: Cliques and Positive Square Energy](https://arxiv.org/abs/2610.40570)
- **Abstract:** The authors show that a sufficiently large sum of squared positive adjacency eigenvalues forces many copies of a larger clique, with an asymptotically best-possible leading coefficient for each fixed clique size.
- **Authors:** Abhay Jayarajan, M. Rajesh Kannan, Shivaramakrishna Pragada
- **arXiv:** `2610.40570v1` (published 2026-10-29 17:44:06 UTC; categories: `math.CO`)
- **Evidence for ranking:** The abstract states a sharp asymptotic supersaturation bound and optimality of its leading coefficient; it links spectral information to extremal clique counts through stability, removal, and cut arguments.
- **Claimed result:** For every fixed r≥2, if √s⁺>(1−1/r)n, then kᵣ₊₁≥(r⁻⁽ʳ⁻¹⁾−oᵣ(1))n^(r−1); the authors say the coefficient is asymptotically best possible. In particular, k₃≥n/2−o(n).
- **Assumptions and setting:** G is a simple graph of order n; r is fixed while n tends to infinity; kᵣ counts unlabeled Kᵣ copies and s⁺ is the sum of squares of positive adjacency eigenvalues.
- **Caveat:** The theorem is asymptotic for fixed r, and its triangle conclusion is a consequence of the stated spectral threshold rather than a claim about every graph.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Combinatorics & discrete mathematics

### 7. [Nonuniqueness of the 2D Euler Evolutions with L¹∩Lᵖ Vorticity](https://arxiv.org/abs/2610.40553)
- **Abstract:** For every prescribed 1<p<∞, the authors construct compactly supported initial vorticity in L¹∩Lᵖ that has two distinct unforced two-dimensional Euler evolutions, both with strong continuity and exact Lagrangian transport.
- **Authors:** Thomas Y. Hou, Xiang Qin, Peicong Song, Wenhan Zhang
- **arXiv:** `2610.40553v1` (published 2026-10-29 17:39:32 UTC; categories: `math.AP`)
- **Evidence for ranking:** A concrete nonuniqueness construction for each finite p, with the mechanism carried through exact Euler patch solutions and a limiting cascade across scales; it complements the same-batch envelope dichotomy paper.
- **Claimed result:** For every 1<p<∞, the paper constructs one compactly supported initial datum in L¹(ℝ²)∩Lᵖ(ℝ²) with two distinct evolutions on [0,1], both strongly continuous in that space and transported by their respective regular Lagrangian flows.
- **Assumptions and setting:** Unforced incompressible 2D Euler on ℝ²; the constructed initial vorticity and construction parameters may depend on p.
- **Caveat:** The construction is tailored to each prescribed finite p and does not, by itself, settle uniqueness or nonuniqueness for all possible unbounded-vorticity classes simultaneously.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Analysis & PDE

### 8. [Multicomplexes in Action: Strong Formality of Compact Hyperkähler Manifolds](https://arxiv.org/abs/2610.40639)
- **Abstract:** The paper proves that compact hyperkähler manifolds are bigraded strongly formal in a pluripotential homotopy-theoretic sense, using algebraic results for multicomplexes and commutative n-differential graded algebras.
- **Authors:** Antonio Pio Contrò
- **arXiv:** `2610.40639v1` (published 2026-10-29 17:58:39 UTC; categories: `math.AT`, `math.AG`, `math.DG`)
- **Evidence for ranking:** Three-way cross-listing across algebraic topology, algebraic geometry, and differential geometry; the paper establishes a broad class-wide formality result via a structural algebraic framework.
- **Claimed result:** The author proves all compact hyperkähler manifolds are bigraded strongly formal in the sense of Milivojević and Stelzig, and develops a generalized ∂∂̄-lemma and algebraic formality theorem for the relevant multicomplex setting.
- **Assumptions and setting:** Compact hyperkähler manifolds, interpreted through pluripotential homotopy theory and the paper's notion of bigraded strong formality.
- **Caveat:** This specialized formality statement should not be conflated with every version of ordinary rational homotopy formality; the paper is a new preprint without a journal reference listed in the checked metadata.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Geometry & topology; Algebra & number theory

### 9. [Sharp L² stability for anisotropic radial Caffarelli-Kohn-Nirenberg inequalities](https://arxiv.org/abs/2610.40360)
- **Abstract:** The authors prove quantitative stability and sharp constants for radial Caffarelli–Kohn–Nirenberg and Heisenberg inequalities using an anisotropic radial derivative and a smooth strictly convex body's Minkowski functional.
- **Authors:** Zhenzhen Wei, Denghui Wu
- **arXiv:** `2610.40360v1` (published 2026-10-29 16:13:10 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract reports sharp constants, equality-case classification, and extensions to weighted Lᵖ stability; the anisotropic nonsymmetric-body setting broadens the usual radial formulation.
- **Claimed result:** For the L² Caffarelli–Kohn–Nirenberg inequality with a≠b+1, the authors obtain the sharp stability constant |b+1−a| and classify equality cases; they also give sharp constants 2 and 4 for the scale-invariant and scale-noninvariant L² Heisenberg inequalities.
- **Assumptions and setting:** Dimension N≥2 and a smooth strictly convex body, not necessarily origin-symmetric; the Lᵖ extensions require 2≤p<∞, a≠b+1, and the stated sign condition.
- **Caveat:** The L² theorem excludes the parameter boundary a=b+1, while the stated Lᵖ results apply only under additional parameter restrictions.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Analysis & PDE; Optimization & control

### 10. [Quantitative propagation of chaos on arbitrary finite time intervals for the three-dimensional repulsive Vlasov-Poisson-Fokker-Planck equation](https://arxiv.org/abs/2610.40422)
- **Abstract:** For singular repulsive Vlasov–Riesz–Fokker–Planck interactions, the authors prove total-variation propagation-of-chaos rates on finite intervals under regularity of the limiting solution, including a three-dimensional Vlasov–Poisson–Fokker–Planck case.
- **Authors:** Ning Jiang, Juntao Wu
- **arXiv:** `2610.40422v1` (published 2026-10-29 16:48:16 UTC; categories: `math.AP`)
- **Evidence for ranking:** The result addresses singular, unregularized interactions and provides a quantitative rate on any finite interval satisfying the solution hypotheses; the proof combines weighted BBGKY estimates with coupling.
- **Claimed result:** The authors prove algebraic-in-particle-number convergence of marginals in total variation for 0<s<d/2 on ℝᵈ or 𝕋ᵈ when the limiting classical solution has the stated regularity; in 3D VPFP they obtain convergence on every finite interval for their specified initial-density assumptions.
- **Assumptions and setting:** Repulsive interactions with singularity |x|⁻ˢ, 0<s<d/2; product initial law; finite time intervals on which the limiting classical solution meets the paper's regularity assumptions. The 3D VPFP specialization assumes weighted Cᵐ data, m≥3, Gaussian velocity decay, and polynomial spatial decay of order M>3.
- **Caveat:** “Arbitrary finite time intervals” is conditional on the required regularity of the limiting classical solution; this is not an unconditional global-in-time theorem for arbitrary initial data.
- **Announcement type:** new submission, 2026-10-30 batch
- **Themes:** Probability & statistics; Analysis & PDE

## Trending Research Themes

- **Sharp uniqueness thresholds in fluid PDEs (two selected papers).** The neutral-vortex-array paper gives a divergence/convergence test for a restricted class, while the companion L¹∩Lᵖ construction gives two evolutions for every fixed finite p. Together they make Euler uniqueness/nonuniqueness the clearest recurring subject in this selection, not evidence by themselves of an archive-wide shift.
- **Exact asymptotics and sharp constants.** Tropical order-type counts, positive-square-energy supersaturation, and anisotropic Caffarelli–Kohn–Nirenberg stability all report sharp or first-order optimal bounds, though for distinct objects and hypotheses.
- **Random structures meet continuum or algorithmic limits.** The JT-disk paper proves a discrete-to-continuum limit using branching exploration; the Ising paper combines zero-free regions and algorithms on random regular graphs; the multiplicative-function paper obtains an almost-sure iterated-logarithm law with random normalization. These are related by probabilistic tools, not a single shared technique.
- **Cross-field structural bridges.** Tropical geometry connects combinatorial types to linear programming and mean-payoff games; hyperkähler formality connects differential geometry to multicomplex algebra; kinetic PDE work connects singular-particle estimates to weighted BBGKY hierarchies.

## Open Problems and Research Directions

- **Author-stated open scope — Euler uniqueness:** The authors of the neutral-array paper say their criterion does not settle sharpness of the classical Yudovich–Osgood condition for general unbounded vorticities. A follow-up suggested by the paper is to test which parts of the reciprocal-envelope criterion survive when exact neutral shielding or stationary-array structure is relaxed. [2610.40552]
- **Author-stated unresolved alternative — random multiplicative functions:** The authors do not decide whether the limsup normalized by √x(log log x)^(1/4) is finite positive with a nondegenerate distribution or infinite almost surely. Resolving which branch occurs, and finding conditions distinguishing it, is a direct next question. [2610.40605]
- **Author-stated conjectural boundary — Ising counting:** The Kesten–Stigum threshold is described as conjecturally optimal for polynomial-time counting and sampling, but the paper's algorithm covers only temperatures up to that threshold. Investigating the boundary behavior and what obstructs or permits algorithms beyond it would test that conjecture. [2610.40598]
- **Author-motivated extension — flat discrete disks:** The JT paper gives a criterion and identifies triangulations or quadrangulations as natural possible models. Verifying its Markov, tightness, and exploration-convergence hypotheses for a specific additional model would test the proposed universality. [2610.40645]

## Takeaway

This batch contains several mathematically precise claims—sharp Euler criteria, a tropical enumeration answer, and discrete-to-continuum convergence—alongside quantitative results in random models and inequalities. The report is a research-oriented shortlist, not evidence that these papers attracted the most readers: the batch is fresh, external attention signals are sparse, and the ranking should be treated as provisional.

## Method and sources

- **Window:** Daily, 2026-10-30 through 2026-10-30; arXiv announcement batch: Friday, 2026-10-30. This uses today's batch, not a prior announcement.
- **Snapshot:** 2026-10-30 17:19:34 UTC.
- **Coverage:** Traversed the complete `math` recent listing for the batch (874 entries; 1,079 math-subject assignments across cross-lists). The selected papers' abstract pages were checked directly, and arXiv API records were used to verify version, authors, UTC submission/update timestamps, and category metadata. For the top three, PDF text from the introduction and main-results statements was inspected; no proof verification is claimed.
- **Ranking method:** Inferred shortlist based on explicit mathematical results, cross-list breadth, reusable methods, and concrete limitations; recency was not used to imply popularity. No official arXiv trending chart exists. Semantic Scholar citation metadata could not be reliably obtained for this batch, and searches did not surface independent expert discussion or journal references for these new submissions, so the ranking is best read as “notable recent papers,” not measured attention.
- **Sources:** [arXiv math recent listing](https://arxiv.org/list/math/recent); each linked arXiv abstract page and its `/pdf/` version; arXiv API records; targeted web searches for the selected paper titles. The configured `web_extract` service could not extract pages in this run, so abstract pages were verified in the browser and metadata was cross-checked against the arXiv API.
