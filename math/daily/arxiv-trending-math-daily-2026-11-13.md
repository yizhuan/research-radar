# arXiv Mathematics — 13 November 2026: 9 notable papers

The latest announcement batch has nine selected papers, with especially strong signals in probability and scaling limits, alongside conjecture-level results in geometry, spectral theory, and analysis. Spoken agenda: surface fluctuations and percolation limits, then extremal geometry and arithmetic, followed by random Fourier analysis and PDE obstructions. This is an inferred ranking, not an official arXiv trending chart; independent-attention and citation evidence is sparse for papers this recent, so the list is best read as notable new mathematics rather than measured popularity.

## Top papers (ranked)

### 1. [GFF for 3D Ising interfaces in three moves of Tetris](https://arxiv.org/abs/2611.16943)
- **Abstract:** The authors establish a Gaussian free field scaling limit for tilted interfaces in the three-dimensional Ising model at sufficiently low temperature, through reductions to SOS, half-monotone SOS, and dimer models.
- **Authors:** Benoît Laslier, Eyal Lubetzky
- **arXiv:** `2611.16943v1` (published 2026-11-12 15:23:54 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** A concrete scaling-limit claim covers the full 3D Ising interface and related surface models; it is cross-listed in probability and mathematical physics and reports a broader dimer renormalization theorem. No measurable citation momentum is established for this fresh submission.
- **Claimed result:** The abstract and Theorem 1 claim local gradient convergence and, after rescaling, convergence modulo constants to an anisotropic Gaussian free field for positive slopes and sufficiently large inverse temperature; analogous limits are claimed for SOS and half-monotone SOS.
- **Assumptions and setting:** 3D Ising model on tilted tori, both limiting slopes strictly positive, and inverse temperature above a threshold; the limiting amplitude and anisotropy depend on temperature and slope.
- **Caveat:** The result is restricted to the low-temperature, positive-slope regime; the fluctuation amplitude and linear anisotropy map are not explicit.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 2. [The loop-ensemble scaling limits of near-critical percolation in the plane](https://arxiv.org/abs/2611.15209)
- **Abstract:** For near-critical site percolation on the triangular lattice at fixed nonzero parameter, the author proves a unique scaling limit for all cluster-boundary loops and convergence of exploration paths to continuous paths.
- **Authors:** Chang-Long Yao
- **arXiv:** `2611.15209v1` (published 2026-11-11 09:04:28 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** The paper says it answers a problem proposed by Camia, Fontes, and Newman and establishes uniqueness of a full loop-ensemble scaling limit, not just subsequential convergence; the claimed result is cross-listed in probability and mathematical physics.
- **Claimed result:** Theorem 1.2 claims convergence in law of the near-critical loop ensemble in loop-ensemble space for each fixed `λ ≠ 0`; the introduction also states convergence in distribution of near-critical exploration paths to continuous paths.
- **Assumptions and setting:** Site percolation on the triangular lattice, near-critical parameter fixed and nonzero, with mesh tending to zero; the paper builds on established quad-crossing scaling limits.
- **Caveat:** The result is for the specified triangular-lattice near-critical coupling; it does not assert the same limit theorem for arbitrary planar percolation models.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 3. [A complete solution to the Naor isomorphic reverse isoperimetry conjecture](https://arxiv.org/abs/2611.16898)
- **Abstract:** For every origin-symmetric convex body, the authors claim a volume-preserving linear transformation and a nearby symmetric convex body with isoperimetric quotient at most `40 ε⁻¹√n`, resolving Naor's conjecture.
- **Authors:** Su Mengwei, Sun Qiang, Xiong Ge
- **arXiv:** `2611.16898v1` (published 2026-11-12 14:54:50 UTC; categories: `math.MG`)
- **Evidence for ranking:** The paper states an explicit resolution of a named conjecture for every origin-symmetric convex body; the arXiv HTML introduction and Theorem 1.1 give the quantitative bound and hypotheses.
- **Claimed result:** Theorem 1.1 claims that for each origin-symmetric convex body `K ⊂ Rⁿ`, there is `T ∈ SLₙ(R)` such that for every `0 < ε < 1` one can find symmetric `L` with `(1−ε)TK ⊆ L ⊆ TK` and `iq(L) ≤ 40 ε⁻¹√n`.
- **Assumptions and setting:** Finite-dimensional real space; `K` is an origin-symmetric convex body and `T` preserves volume.
- **Caveat:** The bound concerns a nearby body `L` inside a transformed `K`, not the quotient of `TK` itself; this is a new preprint claim, not an independently checked proof.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Geometry & topology

### 4. [The Pólya–Szegő buckling conjecture in dimensions two through forty-seven](https://arxiv.org/abs/2611.15243)
- **Abstract:** The authors prove the Pólya–Szegő conjecture for dimensions 2 through 47: among open sets of fixed finite volume, a ball minimizes the first clamped buckling eigenvalue, with a sharp comparison to the first Dirichlet eigenvalue.
- **Authors:** Guowei Dai, Yingxin Sun, Yong Zhang
- **arXiv:** `2611.15243v1` (published 2026-11-11 09:32:22 UTC; categories: `math.SP`)
- **Evidence for ranking:** The paper claims a dimension-explicit resolution of a classical spectral-geometric conjecture over a wide finite range and identifies a sharp equality case; the arXiv HTML introduction states the precise variational setting.
- **Claimed result:** For `2 ≤ n ≤ 47`, the abstract claims `Λ₁(Ω) ≥ (j_{n/2,1}/j_{n/2−1,1})² λ₁ᴰ(Ω)` and that balls are the volume-constrained minimizers; equality is characterized up to sets of zero `H²` capacity.
- **Assumptions and setting:** Open sets of prescribed finite volume; `Λ₁` is the first clamped buckling eigenvalue and `λ₁ᴰ` the first Dirichlet eigenvalue.
- **Caveat:** The theorem covers dimensions 2–47 only. The authors show their calibration fails for `n ≥ 48`, which is a limitation of this method and not a disproof of the conjecture there.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Analysis & PDE

### 5. [Forbidden subset sums in a linear range: an inverse theorem and the Erdős-Graham irregularity problem](https://arxiv.org/abs/2611.17205)
- **Abstract:** The paper gives an inverse theorem for dense sets with forbidden subset sums and derives an exact formula for `c ≥ 1` and non-convergence and subsequential limits for the Erdős–Graham extremal function when `0 < c < 1`.
- **Authors:** Mateo Matijasevick
- **arXiv:** `2611.17205v1` (published 2026-11-12 18:05:45 UTC; categories: `math.CO`, `math.NT`)
- **Evidence for ranking:** The abstract states a resolution of the irregularity question in broad parameter ranges, a separate inverse theorem, and partial Lean 4 verification; the paper bridges combinatorics and number theory. Its introduction and stated theorems were checked in arXiv HTML.
- **Claimed result:** The paper claims `f_c(n)=⌊cn⌋−⌈n/2⌉` for `c≥1`; for `0<c<1` it proves non-convergence and a limsup of `c/2`, with further subsequential limits under least-non-divisor conditions. The inverse theorem applies when `2^(q−2)E ≤ sT`; selected results are Lean-verified.
- **Assumptions and setting:** `f_c(n)` is the maximum size of a subset of `{1,…,⌊cn⌋}` avoiding `n` as a sum of distinct elements; the inverse theorem has additional size and least-non-divisor hypotheses.
- **Caveat:** The full limit-point set is identified in the abstract only for `c=1/2`; the stated subsequential formula has extra conditions, and Lean verification covers only specified portions.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 6. [The Fourier dimension conjecture for complex Gaussian multiplicative chaos on the circle](https://arxiv.org/abs/2611.15733)
- **Abstract:** The author proves the Bonnefont–Rajamäki–Vargas Fourier-dimension conjecture throughout its stated parameter range for complex Gaussian multiplicative chaos on the circle, with additional boundary decay and Sobolev results.
- **Authors:** Feng Guo
- **arXiv:** `2611.15733v1` (published 2026-11-11 17:09:57 UTC; categories: `math.PR`)
- **Evidence for ranking:** The abstract claims a conjecture resolution with explicit parameter regions and almost-sure Fourier decay statements; it connects random measures, harmonic analysis, and Sobolev regularity.
- **Claimed result:** For the canonical holomorphic family the claimed dimension identity holds almost surely on the stated open parameter regions; on the specified sloping boundary, Fourier coefficients decay logarithmically and the Fourier dimension is zero.
- **Assumptions and setting:** Complex Gaussian multiplicative chaos built from a single real Gaussian field on the circle, with parameters `γ=α+iβ` in the paper's stated regions.
- **Caveat:** The identity is asserted on the conjecture's stated parameter range, not all complex parameters; boundary behavior is separately described and can differ from the interior formula.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Probability & statistics; Analysis & PDE

### 7. [Existence of a fluid phase for the two-dimensional one-component plasma](https://arxiv.org/abs/2611.17174)
- **Abstract:** For inverse temperature `β ≤ 2`, the authors claim exponential correlation decay and uniqueness within a stated controlled-fluctuation class, yielding an infinite-volume plasma process and first-order Debye–Hückel asymptotics.
- **Authors:** Jeanne Boursier, Thomas Leblé
- **arXiv:** `2611.17174v1` (published 2026-11-12 17:45:58 UTC; categories: `math-ph`, `math.PR`)
- **Evidence for ranking:** The paper turns the predicted fluid regime into specific correlation-decay and uniqueness claims and gives infinite-volume and Debye–Hückel consequences; it is cross-listed in probability and mathematical physics.
- **Claimed result:** The abstract claims exponential decay of correlations and uniqueness of the Gibbs state for `β ≤ 2` among point processes whose fluctuations are controlled; it constructs `Gin_β` and identifies the truncated two-point function to first order in `β` at the Debye-length scale.
- **Assumptions and setting:** Two-dimensional logarithmically repelling point charges in a uniform neutralizing background; inverse temperature at most 2 and the stated fluctuation-control condition for uniqueness.
- **Caveat:** The stated temperature range ends at `β=2`; the abstract does not establish the fluid phase or uniqueness beyond it.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 8. [The coercivity conjecture for nonlocal energies](https://arxiv.org/abs/2611.16682)
- **Abstract:** The authors disprove the implication from uniform ellipticity to fractional Sobolev coercivity for symmetric nonlocal kernels when `n>2s`, prove it for `n=1, s>1/2`, and give criteria for important kernel classes.
- **Authors:** Linus Behn, Roberto Colombo, Xavier Fernández-Real, Florian Grube, Harsh Prasad, Xavier Ros-Oton
- **arXiv:** `2611.16682v1` (published 2026-11-12 11:56:48 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract pairs a counterexample to a broad coercivity conjecture with positive results for selected kernels, an application to the Gressman–Strain estimate, and Hölder estimates under added cancellation assumptions.
- **Claimed result:** The authors claim failure for `n>2s`, including smooth compactly supported tests, a positive result for `n=1, s>1/2`, and a local coercivity criterion based on annular cancellation.
- **Assumptions and setting:** Symmetric nonlocal kernels of order `2s`, `0<s<1`, with the paper's ellipticity conditions; positive results require additional cancellation or kernel-class hypotheses.
- **Caveat:** Ellipticity alone fails to imply coercivity in the stated counterexample regime; the abstract does not settle every remaining dimension/order and kernel combination.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Analysis & PDE

### 9. [A counterexample to fixed-profile soliton resolution for the three-dimensional quintic wave equation](https://arxiv.org/abs/2611.17291)
- **Abstract:** The authors construct a bounded global solution of the focusing energy-critical 3D wave equation whose core approaches distinct stationary profiles along different times, contradicting fixed-profile soliton resolution in the stated setting.
- **Authors:** Xuwen Chen, Justin Holmer, Shunlin Shen
- **arXiv:** `2611.17291v1` (published 2026-11-12 18:53:35 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract states a concrete counterexample to a canonical asymptotic description and reports a computer-assisted certificate for the stationary state and its odd energy kernel.
- **Claimed result:** The authors claim a bounded forward-global solution asymptotic to a varying stationary profile plus one free wave, with two limits in distinct similarity orbits that rule out a fixed profile list in the asserted resolution form.
- **Assumptions and setting:** Focusing energy-critical quintic wave equation in three spatial dimensions; the constructed solution starts arbitrarily close to a sign-changing stationary state.
- **Caveat:** This is a constructed counterexample in a specified equation and near a specified stationary state; it does not classify asymptotics for all energy-critical wave solutions.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Analysis & PDE

## Trending Research Themes

- **Scaling limits of random interfaces:** The 3D Ising interface result gives a GFF limit in a low-temperature, positive-slope regime (2611.16943), while near-critical triangular-lattice percolation gets a unique loop-ensemble limit for fixed nonzero parameter (2611.15209). These are different models and limit objects, but scaling limits are the clearest shared technique in this selection.
- **Conjectures converted into quantitative theorems:** The Naor paper gives an explicit dimension bound for reverse isoperimetry (2611.16898), Pólya–Szegő is proved over dimensions 2–47 (2611.15243), the subset-sum paper resolves irregularity in stated ranges (2611.17205), and the complex-chaos paper proves a Fourier-dimension conjecture on specified parameter regions (2611.15733).
- **Probability, harmonic analysis, and mathematical physics:** Near-critical percolation, Ising interfaces, Gaussian multiplicative chaos, and the one-component plasma all study random structures, but with distinct methods and hypotheses (2611.15209, 2611.16943, 2611.15733, 2611.17174). This is a concentration in the selected papers, not a field-wide claim.
- **Counterexamples delimit broad principles:** The nonlocal-energy paper shows ellipticity alone is insufficient in its stated regime (2611.16682), and the wave-equation paper refutes a fixed-profile resolution assertion (2611.17291). They are independent results, not evidence of a shared mechanism.

## Open Problems and Research Directions

- **Author-stated boundary:** The buckling result covers dimensions 2–47, while the authors' calibration fails for `n≥48`; this leaves the conjecture beyond dimension 47 unresolved by this work (2611.15243). A follow-up could seek a different comparison argument that avoids this calibration barrier.
- **Author-stated scope boundary:** The complex-chaos Fourier-dimension identity is proved on the conjecture's stated parameter regions, with different behavior on the sloping boundary (2611.15733). Extending the identity or describing transitions in the remaining parameter regions would test the boundary of the result.
- **Author-stated scope boundary:** The plasma result establishes the claimed fluid properties only for `β≤2` (2611.17174). Extending correlation decay or identifying the obstruction beyond this threshold would address the unproved regime.
- **Author-stated limitation:** The nonlocal coercivity theorem gives a counterexample region and selected positive regimes, not a complete map of all dimensions, orders, and kernel classes (2611.16682). A systematic classification of which cancellation conditions restore coercivity is a concrete next step.
- **Synthesis:** The Ising-interface theorem assumes positive slopes and sufficiently large inverse temperature (2611.16943). Identifying the fluctuation amplitude and anisotropy map, and probing slope limits toward zero, would test how far the scaling limit extends.
- **Synthesis:** The subset-sum paper gives only a conditional description of many subsequential limits for `0<c<1` (2611.17205). Determining the full limit-point set for general `c` and formalizing additional cases would sharpen the arithmetic picture.
- **Synthesis:** The wave-equation counterexample uses a varying stationary core generated by radiation packets (2611.17291). Testing related constructions in other energy-critical equations could isolate which ingredients are essential to the failure of fixed-profile resolution.

## Takeaway

The standout signals are two distinct random-interface scaling limits, plus sharp conjecture-level claims in convex geometry, spectral theory, additive combinatorics, and random Fourier analysis. The ordering is an informed selection of mathematical claims, not evidence of readership: these are fresh preprints, citation and independent-attention signals are limited, and none of the results is independently proof-verified here.

## Method and sources

- **Window:** Daily; latest Mathematics announcement batch dated Friday 2026-11-13. No 2026-11-14 batch was listed at the snapshot, so this is the prior batch. Selected window: 2026-11-13 through 2026-11-13.
- **Coverage:** arXiv Mathematics (`math`) and math-primary cross-lists. The complete 774-entry batch was traversed; all selected abstracts and arXiv metadata were checked. The introductions/main-result statements for the first three entries were inspected in arXiv HTML; the buckling paper's introduction was also inspected.
- **Inference:** Selected and ordered by explicit theorem/counterexample claims, conjecture or open-problem scope, quantitative specificity, and cross-subfield relevance. Recency is only a tie-breaker; no numeric score or official popularity claim is used.
- **Attention evidence:** Semantic Scholar citation metadata was unavailable for this batch, and exact-title searches mostly returned arXiv records rather than independent expert discussion. Citation momentum therefore could not be measured; interpret this as a notable-paper selection, not demonstrated readership trends.
- **Snapshot:** 2026-11-14 01:20 UTC.
- **Sources:** [arXiv Mathematics recent submissions](https://arxiv.org/list/math/recent); each paper's linked arXiv abstract; arXiv API metadata for versions, UTC timestamps, authors, and categories; HTML main text for 2611.16943, 2611.15209, 2611.16898, 2611.15243, and 2611.17205; exact-title web searches for independent context.
