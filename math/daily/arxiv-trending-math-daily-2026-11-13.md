# arXiv Mathematics — Friday, 13 November 2026

Latest announcement batch: 13 November 2026; 7 papers highlighted. The strongest pattern is theorem-level work that resolves named conjectures or sharply limits a conjecture's scope, including results in random polynomials, convex geometry, nonlocal PDE, and dispersive waves. Spoken agenda: four unusually concrete claims, then a formalized subset-sum result, a function-theory counterexample, and a computer-assisted Calabi–Yau construction. Global caveat: arXiv publishes no official trending chart; this ordering is inferred, and citation evidence for such a fresh batch is limited. Treat these as notable recent papers, not a measured popularity ranking.

## Top papers (ranked)

### 1. [The limit point set of real roots of random polynomials: a resolution of Erdős Problem 521](https://arxiv.org/abs/2611.16157)
- **Abstract:** For i.i.d. real coefficients of mean zero, variance one, and a finite absolute exponential moment, the authors determine the almost-sure liminf, limsup, and complete interval of subsequential limits for the real-root count of Kac polynomials divided by log n.
- **Authors:** Zengjing Chen, Xiaodong Liu, Jie Peng, Hanchao Wang, Mingjian Zhang
- **arXiv:** `2611.16157v1` (published: 2026-11-12; UTC time: Not available from the sources checked; categories: `math.PR`)
- **Evidence for ranking:** The abstract claims a resolution of a named, longstanding problem and gives an explicit almost-sure limit set. The independent Erdős Problems record #521 confirms the historical question being addressed; the paper's own introduction explains the stronger limit-set result.
- **Claimed result:** The authors prove almost surely that the normalized number of distinct real roots has liminf 1/π, limsup 1/π+C*, and every value in between as a subsequential limit; C*>1/π is defined by an entropy-one equation. The lower-limit identity holds under a finite 2+δ moment, while the full limit-set statement uses the stronger exponential-moment hypothesis.
- **Assumptions and setting:** One infinite i.i.d. sequence of real, mean-zero, variance-one coefficients; finite absolute exponential moment for the full interval theorem. For the lower endpoint alone, a finite 2+δ moment suffices.
- **Caveat:** The exact upper endpoint and full interval are not established under only the weaker 2+δ moment assumption.
- **Announcement type:** new submission, announcement batch 13 Nov 2026
- **Themes:** Probability & statistics

### 2. [A complete solution to the Naor isomorphic reverse isoperimetry conjecture](https://arxiv.org/abs/2611.16898)
- **Abstract:** For every origin-symmetric convex body in R^n, the authors find a volume-preserving linear image containing a nearby symmetric convex body whose isoperimetric quotient is at most 40 ε^-1√n, resolving Naor's conjecture.
- **Authors:** Su Mengwei, Sun Qiang, Xiong Ge
- **arXiv:** `2611.16898v1` (published: 2026-11-12; UTC time: Not available from the sources checked; categories: `math.MG`)
- **Evidence for ranking:** The paper states an explicit resolution for every origin-symmetric convex body, with quantitative constants. Search results surfaced Naor's earlier source for the conjecture, providing context for the claimed target; the introduction and Theorem 1.1 give the hypotheses and bound.
- **Claimed result:** The authors prove that for every origin-symmetric convex body K⊂R^n there is T∈SL_n(R) such that, for each ε∈(0,1), an origin-symmetric L exists with (1−ε)TK⊆L⊆TK and iq(L)≤40 ε^-1√n.
- **Assumptions and setting:** Finite-dimensional R^n, origin-symmetric convex bodies, and a volume-preserving linear transformation; the approximation parameter ε is strictly between 0 and 1.
- **Caveat:** The quantitative guarantee depends on ε through ε^-1; the theorem is an isomorphic, approximate-body statement, not an exact bound for TK itself.
- **Announcement type:** new submission, announcement batch 13 Nov 2026
- **Themes:** Geometry & topology

### 3. [The coercivity conjecture for nonlocal energies](https://arxiv.org/abs/2611.16682)
- **Abstract:** The authors disprove a general implication from ellipticity to fractional Sobolev coercivity for symmetric nonlocal kernels in much of the parameter range, while proving coercivity for selected kernel classes via annular cancellation.
- **Authors:** Linus Behn, Roberto Colombo, Xavier Fernández-Real, Florian Grube, Harsh Prasad, Xavier Ros-Oton
- **arXiv:** `2611.16682v1` (published: 2026-11-12; UTC time: Not available from the sources checked; categories: `math.AP`)
- **Evidence for ranking:** The abstract pairs a counterexample to a central coercivity conjecture with positive criteria and an application to the Gressman–Strain estimate. This is a particularly broad result within its stated kernel framework; the introduction specifies the ellipticity conditions.
- **Claimed result:** The authors show that the conjectured coercivity fails when n>2s, including for smooth compactly supported tests, and holds for n=1, s>1/2. They also establish a local coercivity criterion based on annular cancellation, derive results for several kernel classes, and obtain Hölder estimates under ellipticity and cancellation assumptions.
- **Assumptions and setting:** Symmetric measurable nonlocal kernels of order 2s, 0<s<1, satisfying the paper's upper and directional lower ellipticity conditions; positive results require additional cancellation or class-specific hypotheses.
- **Caveat:** Ellipticity alone is insufficient in the counterexample regime, and the positive results do not assert coercivity for every kernel in the remaining parameter range.
- **Announcement type:** new submission, announcement batch 13 Nov 2026
- **Themes:** Analysis & PDE

### 4. [A counterexample to fixed-profile soliton resolution for the three-dimensional quintic wave equation](https://arxiv.org/abs/2611.17291)
- **Abstract:** For the three-dimensional focusing energy-critical wave equation, the authors construct a bounded forward-global solution near a sign-changing stationary state whose stationary core has two distinct similarity-orbit limits, contradicting a fixed-profile resolution assertion.
- **Authors:** Xuwen Chen, Justin Holmer, Shunlin Shen
- **arXiv:** `2611.17291v1` (published: 2026-11-12; UTC time: Not available from the sources checked; categories: `math.AP`)
- **Evidence for ranking:** The abstract and Theorem 1.1 state a concrete counterexample to a precise version of soliton resolution. Its construction combines controlled radiation with a computer-assisted certificate for the stationary state and its odd energy kernel.
- **Claimed result:** The authors construct a bounded forward-global solution, arbitrarily close initially to a sign-changing stationary state, asymptotic to a varying stationary profile plus a free wave; two separated similarity-orbit limits rule out any fixed finite list of stationary profiles for the stated full-time resolution assertion.
- **Assumptions and setting:** The focusing energy-critical equation u_tt−Δu=u^5 on [0,∞)×R^3 in the energy space; the construction has a specified odd symmetry and concerns the fixed-profile quantifier order described in the paper.
- **Caveat:** This refutes the stated fixed-profile formulation, not every weaker or sequence-dependent formulation of soliton resolution.
- **Announcement type:** new submission, announcement batch 13 Nov 2026
- **Themes:** Analysis & PDE; Mathematical physics

### 5. [Forbidden subset sums in a linear range: an inverse theorem and the Erdős-Graham irregularity problem](https://arxiv.org/abs/2611.17205)
- **Abstract:** The author studies the largest subset of {1,…,⌊cn⌋} avoiding a distinct-element sum of n, proves an exact formula for c≥1 and limit-point results for c<1, and gives an inverse theorem for subset sums.
- **Authors:** Mateo Matijasevick
- **arXiv:** `2611.17205v1` (published: 2026-11-12; UTC time: Not available from the sources checked; categories: `math.CO`, `math.NT`)
- **Evidence for ranking:** The abstract gives exact and asymptotic results for a named Erdős–Graham problem and reports Lean 4 formalization for several specified subclaims; the paper also bridges combinatorics and number theory.
- **Claimed result:** For c≥1, f_c(n)=⌊cn⌋−⌈n/2⌉; for 0<c<1, the normalized sequence fails to converge and has multiple limit points, including the exact set {1/6,1/4} at c=1/2. An inverse theorem supplies a uniform sufficient condition for a subset sum, with some results machine-checked in Lean 4.
- **Assumptions and setting:** f_c(n) maximizes |A| over A⊆{1,…,⌊cn⌋} for which n is not a sum of distinct elements; the inverse theorem has additional parameters and range restrictions stated in the abstract.
- **Caveat:** The formalized portion is only a subset of the results (notably cases with q∈{2,3}); the broader asymptotic statements remain author-reported proofs in the preprint.
- **Announcement type:** new submission, announcement batch 13 Nov 2026
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 6. [The Brown--Shields Conjecture: Two Approximation Theorems and a Counterexample](https://arxiv.org/abs/2611.16997)
- **Abstract:** The authors construct an outer function in the classical Dirichlet space whose radial zero set has logarithmic capacity zero but whose polynomial multiples do not approximate 1, disproving the Brown–Shields conjecture.
- **Authors:** Bonan Chen, Xiang Fang, Feng Guo
- **arXiv:** `2611.16997v1` (published: 2026-11-12; UTC time: Not available from the sources checked; categories: `math.FA`)
- **Evidence for ranking:** The abstract reports a direct counterexample to a named conjecture plus two approximation theorems that support the construction; it specifies a strong capacity-zero property for the zero set.
- **Claimed result:** The authors prove that a counterexample can be built with an outer Dirichlet-space function whose radial zero set is polar, and show that counterexamples of this type approximate every proper outer canonical generator in both Dirichlet norm and boundary-log L^1 norm.
- **Assumptions and setting:** Classical Dirichlet space and its canonical generators; the construction uses a complete metric and a nested-ball argument to preserve outerness and noncyclicity.
- **Caveat:** The arXiv comments identify this as an expository version with navigational aids, not intended for publication; its result is a counterexample rather than a full replacement characterization of cyclicity.
- **Announcement type:** new submission, announcement batch 13 Nov 2026
- **Themes:** Analysis & PDE

### 7. [A constructive computer-assisted existence proof for a Calabi--Yau metric](https://arxiv.org/abs/2611.16908)
- **Abstract:** The authors give a rigorous constructive proof of a Ricci-flat Kähler metric on the Fermat quartic, combining numerical approximation, a fixed-point theorem, and verified bounds.
- **Authors:** Michael R. Douglas, Javier Gómez-Serrano, Fabian Lehmann, Daniel Platt, Yidi Qi
- **arXiv:** `2611.16908v1` (published: 2026-11-12; UTC time: Not available from the sources checked; categories: `math.DG`, `hep-th`)
- **Evidence for ranking:** This is a constructive, computer-assisted existence claim for a central geometric object, with verified numerics and a cross-list in high-energy theory; the abstract explicitly distinguishes the approach from relying on Yau's existence theorem.
- **Claimed result:** The authors prove constructively that the Fermat quartic admits a Ricci-flat Kähler metric and provide an explicit accurate analytic approximation, using computation to obtain an approximate solution and verified numerics to close a fixed-point argument.
- **Assumptions and setting:** The specific Fermat quartic hypersurface and the authors' validated computational bounds; broader manifolds are discussed as future applications of the method.
- **Caveat:** The existence theorem is established for the stated example; the abstract does not establish that the method is already effective for other manifolds.
- **Announcement type:** new submission, announcement batch 13 Nov 2026
- **Themes:** Geometry & topology; Mathematical physics

## Trending Research Themes

- **Named conjectures under pressure:** The random-polynomial paper gives an almost-sure limit set rather than the conjectured single constant; the nonlocal-energy paper finds a regime where ellipticity does not imply coercivity; and the soliton paper disproves one fixed-profile formulation. These are distinct settings, not evidence of one shared technical method.
- **Exact bounds and quantitative structure:** The convex-geometry paper gives an explicit √n isoperimetric-quotient bound with an ε-dependent loss, while the subset-sum paper supplies an exact formula for c≥1 and structured limit points below that threshold.
- **Rigorous computation alongside analysis:** The wave-equation construction uses a computer-assisted spectral certificate, the Fermat-quartic result combines verified numerics with a fixed-point theorem, and the subset-sum work formalizes selected claims in Lean 4. These are separate validation strategies, not a field-wide shift.
- **Probability and geometry are isolated signals in this batch:** The Kac-polynomial limit-set theorem is a probability result and the Calabi–Yau construction is a geometry result; each is individually notable, but neither establishes a broader trend by itself.

## Open Problems and Research Directions

- **Author-stated scope gap — random polynomials:** The complete interval of subsequential limits requires a finite absolute exponential moment, while the lower endpoint needs only a finite 2+δ moment. A follow-up could test whether the upper endpoint and interval description survive under weaker coefficient tails. [2611.16157]
- **Author-stated limitation — nonlocal coercivity:** The paper establishes failure in n>2s and a positive result for n=1, s>1/2, plus criteria for selected kernels. A useful next step is to map the remaining dimension/order regimes against the precise symmetry and cancellation assumptions. [2611.16682]
- **Author-stated boundary — subset-sum formalization:** The abstract says only portions of the theorem, including cases q∈{2,3}, are Lean-checked. Extending the formal proof to the other stated parameter cases would clarify which parts of the full inverse theorem admit the same machine-checking. [2611.17205]
- **Synthesis — profile flexibility:** Since [2611.17291] rules out a fixed finite profile list in its specified full-time formulation, investigate what weaker time-dependent profile selection or subsequence-dependent decomposition is sufficient for this class of solutions.
- **Synthesis — constructive geometry:** [2611.16908] proposes applying its validated-numerics strategy to other manifolds. A concrete extension is to identify which geometric and numerical conditioning hypotheses make the fixed-point bounds certifiable beyond the Fermat quartic.
- **Synthesis — cyclicity criteria:** The polar-zero-set counterexample in [2611.16997] suggests testing which additional boundary or norm conditions, beyond logarithmic-capacity-zero radial zeros, can still guarantee cyclicity in the Dirichlet space.

## Takeaway

Today's most striking submissions are specific, substantial claims: a complete almost-sure limit-set description for random-polynomial real roots, explicit resolution of a convex-geometric conjecture, and counterexamples delimiting coercivity and soliton-resolution principles. Because attention and citation data are sparse for this announcement batch, the report identifies mathematically notable claims rather than asserting measured popularity; each remains a preprint claim pending expert scrutiny.

## Method and sources

- Window: daily, latest Mathematics announcement batch dated 13 Nov 2026 (not a prior batch); batch window 2026-11-13 to 2026-11-13. Snapshot: 2026-11-13 17:16:39 UTC.
- Coverage: arXiv Mathematics recent listing, all 774 entries in the Friday batch traversed; selected papers' abstract pages checked individually. The first four papers' HTML introductions/main-results statements were inspected; remaining summaries use their arXiv abstracts and metadata.
- Ranking: inferred from concrete author-claimed results, named conjectures/problems, explicit bounds, cross-listing, formalization or verified-computation signals, and available independent context. No numeric trend score was assigned. Recent citation and attention signals were insufficient to measure popularity; Semantic Scholar metadata was not available for this batch at snapshot time.
- Sources: arXiv recent Mathematics listing (https://arxiv.org/list/math/recent); each linked arXiv abstract and, for the first four, the corresponding arXiv HTML paper; independent problem context for Erdős Problem 521 (https://www.erdosproblems.com/521); search results for Naor's original conjecture source (https://arxiv.org/abs/2112.11523).
