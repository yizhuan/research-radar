# arXiv Mathematics — 16 November 2026 batch: eight notable new papers

Today's latest arXiv Mathematics announcement batch is dated 16 November 2026; this report covers eight notable new submissions, with higher-order Fourier analysis, sharp geometric bounds, and explicit constructions among its strongest results. The short agenda: a conjecture resolved through nilspace embeddings, a tighter four-dimensional Borsuk bound, new Euler blow-up data, and several exact or formally checked results. This is an inferred ordering, not an official arXiv trending chart; citation evidence is limited for such recent papers.

## Top papers (ranked)

### 1. [A proof of the Jamneshan-Tao conjecture by embedding nilspaces in nilmanifolds](https://arxiv.org/abs/2611.17567)
- **Abstract:** The authors embed every compact finite-rank nilspace into a toral nilspace and use this to prove the Jamneshan–Tao conjecture, obtaining a Gowers-norm inverse theorem for second-countable compact abelian groups with nilmanifold correlators.
- **Authors:** Pablo Candela, Diego González-Sánchez, Balázs Szegedy
- **arXiv:** `2611.17567v1` (published 2026-11-12 22:46:05 UTC; categories: `math.GR`, `math.CO`, `math.DS`)
- **Evidence for ranking:** An independent Post-Cutoff research explainer discusses the conjecture’s resolution; the paper spans group theory, combinatorics, and dynamics and states a concrete structural theorem with consequences for higher-order Fourier analysis. These signals support mathematical attention, not a measured popularity ranking.
- **Claimed result:** The authors prove every compact finite-rank k-step nilspace embeds continuously into a k-step toral nilspace, then derive the Jamneshan–Tao inverse theorem: for each k and δ, a 1-bounded Borel function on a second-countable compact Hausdorff abelian group with U^(k+1) norm at least δ correlates by at least ε(k,δ) with a bounded-Lipschitz function pulled back from one of a finite family of connected filtered nilmanifolds.
- **Assumptions and setting:** The inverse theorem is for k≥1, 0<δ≤1, second-countable compact Hausdorff abelian groups, and 1-bounded Borel functions; the target family and constants depend on k and δ.
- **Caveat:** It builds on the general nilspace inverse theorem and substantial prior nilspace structure results; the claimed conclusion is not an unconditional inverse theorem for arbitrary non-abelian groups.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 2. [The four-dimensional Borsuk number is five or six](https://arxiv.org/abs/2611.17375)
- **Abstract:** For every bounded subset of R^4 with positive diameter, the authors prove a partition into at most six sets of smaller diameter, improving the previous upper bound of seven; they formalize the theorem in Lean.
- **Authors:** Logan R. Chalmers
- **arXiv:** `2611.17375v1` (published 2026-11-10 23:34:55 UTC; categories: `math.MG`)
- **Evidence for ranking:** The paper sharply improves a recent bound on a classical geometric partition problem, and the full main theorem is formalized in Lean 4; the abstract and introduction spell out the earlier seven-part bound it improves.
- **Claimed result:** The author proves that every bounded positive-diameter subset of R^4 partitions into at most six smaller-diameter parts. A regular 4-simplex requires five, so the Borsuk number b4 is either five or six. The construction separates small, intermediate, and large circumradius cases.
- **Assumptions and setting:** Arbitrary bounded subsets of four-dimensional Euclidean space with positive diameter; no convexity assumption is stated in the theorem.
- **Caveat:** The exact value remains unresolved: this proves 5≤b4≤6, not whether five always suffice. Lean formalization is a checked proof artifact, not independent peer review.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Geometry & topology

### 3. [Sharp Finite-Time Blow-Up for Unforced Axisymmetric Euler Without Swirl via Multiscale Data](https://arxiv.org/abs/2611.18151)
- **Abstract:** The authors construct compactly supported vorticity for an unforced axisymmetric Euler flow without swirl that blows up in finite time, with initial vorticity in every Hölder class C^α for α<1/3 simultaneously.
- **Authors:** Jeaheang Bang, Alexey Cheskidov
- **arXiv:** `2611.18151v1` (published 2026-11-13 13:28:08 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract places the result at the sharp regularity threshold for axisymmetric no-swirl Euler and distinguishes it from previous constructions that handled each subcritical exponent separately; the authors describe a new multiscale cascade and angular-redistribution mechanism.
- **Claimed result:** The authors construct a divergence-free axisymmetric velocity without swirl, with compactly supported vorticity and initial velocity in L² and C^{1,α} for every α<1/3 (smooth away from the origin), whose classical solution loses regularity in finite time. The corresponding initial vorticity is simultaneously in all C^α, α<1/3.
- **Assumptions and setting:** Unforced incompressible Euler in R^3, axisymmetry, no swirl, and rough data strictly below the known global-regularity threshold α=1/3.
- **Caveat:** The construction is not from smooth initial data and does not settle the distinct smooth-data blow-up problem, particularly in the axisymmetric-with-swirl setting.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Analysis & PDE

### 4. [The roads taken in the directed landscape](https://arxiv.org/abs/2611.18360)
- **Abstract:** Almost surely, every finite-landscape-length path spends all but a set of times of Hausdorff dimension at most 57/61 on interiors of geodesics; the authors also construct paths with exceptional-time dimension at least 1/3.
- **Authors:** Pranay Agarwal, Sourav Sarkar, Bálint Virág
- **arXiv:** `2611.18360v1` (published 2026-11-13 16:07:47 UTC; categories: `math.PR`)
- **Evidence for ranking:** The result has an independent Fields Institute talk listing and a University of Toronto mathematics-seminar listing; it gives a quantitative almost-sure statement in the directed-landscape/KPZ setting.
- **Claimed result:** For G, the union of interiors of all directed-landscape geodesics, the authors prove that almost surely every finite-length path lies in G except on a time set of Hausdorff dimension at most 57/61; they also exhibit finite-length paths with exceptional set dimension at least 1/3.
- **Assumptions and setting:** The random directed landscape, almost-surely; the upper bound applies to every finite-landscape-length path in a realization.
- **Caveat:** The upper and lower exceptional-set bounds leave a substantial gap; the abstract does not claim the exponent 57/61 is sharp.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Probability & statistics

### 5. [Smale's mean value constant (1981) equals 4](https://arxiv.org/abs/2611.17373)
- **Abstract:** For the extremal quantity K(d) defined from critical values of normalized complex polynomials of degree d, the authors prove sup_d K(d)=4 and K(d) tends to 4 as d tends to infinity; the main theorem is also formalized in Lean 4.
- **Authors:** Dave Goel
- **arXiv:** `2611.17373v1` (published 2026-11-10 13:27:58 UTC; categories: `math.CV`)
- **Evidence for ranking:** The paper resolves the value of a classical constant left open since Smale’s 1981 result and links a new explicit construction with a Lean 4 proof artifact. A public mathematics account also surfaced the result in the checked search.
- **Claimed result:** For each complex polynomial p of degree d≥2 with p(0)=0 and p′(0)≠0, let S(p)=min_c |p(c)/(c p′(0))| over critical points c, and K(d)=sup_p S(p). The author proves sup_d K(d)=4 and K(d)→4.
- **Assumptions and setting:** The supremum defining K(d) is over the normalized complex polynomials described above; the result concerns the degree-varying supremum and its limit.
- **Caveat:** Every individual K(d) is strictly below 4, so no fixed degree attains the supremum; the abstract does not give exact K(d) for each finite degree.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Analysis & PDE

### 6. [No free lattice contains an infinite ascending chain of copies of FL(3)](https://arxiv.org/abs/2611.18541)
- **Abstract:** The authors answer Dean’s problem by proving that no free lattice contains an infinite strictly ascending chain of sublattices isomorphic to the free lattice on three generators; the theorem is checked in Agda.
- **Authors:** William DeMeo, Ralph Freese
- **arXiv:** `2611.18541v1` (published 2026-11-13 18:49:26 UTC; categories: `math.RA`, `cs.LO`, `math.GR`, `math.LO`)
- **Evidence for ranking:** It resolves a specific long-standing question, is cross-listed across algebra, group theory, and logic, and provides a formal Agda development. The arXiv comment links the formal proof.
- **Claimed result:** The authors prove that no free lattice contains an infinite strictly ascending chain of copies of FL(3), the free lattice on three generators; their abstract also establishes that without requiring the links to be free, FL(3) does contain an infinite ascending chain of 3-generated sublattices.
- **Assumptions and setting:** Free lattices over generator sets with decidable equality for the stated Agda formalization; the theorem itself is claimed for free lattices, with the proof checked under Agda’s safe flags.
- **Caveat:** The chain prohibition depends on each link being isomorphic to FL(3); it does not imply stabilization for arbitrary 3-generated sublattices, which the paper shows can fail.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Algebra & number theory; Logic & foundations; Combinatorics & discrete mathematics

### 7. [Many more odd zeta values are irrational](https://arxiv.org/abs/2611.16156)
- **Abstract:** For every sufficiently large odd s, the authors prove that at least 2.78√(s log log s / log s) among ζ(3), ζ(5), …, ζ(s) are irrational, improving the previous estimate by a factor involving √(log log s).
- **Authors:** Stéphane Fischler, Li Lai, Johannes Sprang, Wadim Zudilin
- **arXiv:** `2611.16156v1` (published 2026-11-12 01:32:10 UTC; categories: `math.NT`, `math.CA`, `math.CO`)
- **Evidence for ranking:** The paper improves a quantitative irrationality bound and connects number theory, analysis, and combinatorics; its abstract identifies the arithmetic, hypergeometric, and Hankel-determinant ingredients.
- **Claimed result:** The authors establish the stated lower bound for the number of irrational odd zeta values up to s, for all sufficiently large odd integers s.
- **Assumptions and setting:** An asymptotic lower bound as odd s becomes sufficiently large; no explicit threshold for “sufficiently large” is given in the abstract.
- **Caveat:** The result bounds how many values are irrational, but does not identify which individual ζ(2k+1) are irrational or prove that all odd zeta values are irrational.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Algebra & number theory; Analysis & PDE; Combinatorics & discrete mathematics

### 8. [Matrix ultraproducts have trivial fundamental group](https://arxiv.org/abs/2611.18328)
- **Abstract:** The authors claim that every tracial ultraproduct of complex matrix algebras has trivial fundamental group, implying uncountably many nonisomorphic matrix ultraproducts and answering a question of Sorin Popa.
- **Authors:** Hiroshi Ando, Isaac Goldbring
- **arXiv:** `2611.18328v1` (published 2026-11-13 15:40:56 UTC; categories: `math.OA`, `math.LO`, `math.RT`)
- **Evidence for ranking:** A concrete operator-algebra classification claim with an explicit connection to model theory and representation theory; the authors say it answers a question of Popa and prove a stronger first-order version.
- **Claimed result:** The authors prove that every tracial ultraproduct of matrix algebras has trivial fundamental group and, more strongly, trivial first-order fundamental group; they infer that there are uncountably many nonisomorphic such ultraproducts.
- **Assumptions and setting:** Tracial ultraproducts of complex matrix algebras; the abstract does not further specify the ultrafilter or matrix-size sequence.
- **Caveat:** The arXiv comment describes this as a first draft and invites comments; the strong classification claim should be treated as a preprint result pending expert scrutiny.
- **Announcement type:** new submission, 16 November 2026 batch
- **Themes:** Algebra & number theory; Logic & foundations

## Trending Research Themes

- **Structural inverse theorems through nilspaces:** Candela, González-Sánchez, and Szegedy turn finite-rank nilspaces into toral ones to obtain nilmanifold structure in Gowers-norm inverse theorems. This is the clearest cross-field bridge in the selection, linking additive combinatorics, group theory, and dynamics ([paper 1](https://arxiv.org/abs/2611.17567)).
- **Sharp bounds and endpoint behavior:** Chalmers narrows the four-dimensional Borsuk number to {5,6}; Bang and Cheskidov reach every subcritical Hölder class simultaneously up to the known 1/3 threshold; Fischler et al. improve a quantitative lower bound on irrational odd zeta values. These are distinct isolated advances, not evidence of one field-wide shift ([papers 2](https://arxiv.org/abs/2611.17375), [3](https://arxiv.org/abs/2611.18151), [7](https://arxiv.org/abs/2611.16156)).
- **Formal verification as a companion to difficult proofs:** The Borsuk partition theorem and Smale-constant result include Lean formalizations, while the free-lattice chain theorem includes Agda. The overlap is a small, concrete signal in this batch—not a claim that formalization is newly dominant across mathematics ([papers 2](https://arxiv.org/abs/2611.17375), [5](https://arxiv.org/abs/2611.17373), [6](https://arxiv.org/abs/2611.18541)).
- **Geodesic structure in random geometry:** Agarwal, Sarkar, and Virág quantify how finite-length directed-landscape paths spend almost all their time on geodesics. This is a focused probability signal supported by a related seminar listing, rather than a multi-paper trend ([paper 4](https://arxiv.org/abs/2611.18360)).
- **Explicit constructions settle extremal or structural questions:** Goel’s polynomial construction approaches the Smale bound, the Euler paper builds multiscale vortex data, and DeMeo–Freese analyze coherent self-embeddings to rule out a chain. The common feature is constructive proof architecture, though the underlying fields and techniques differ ([papers 3](https://arxiv.org/abs/2611.18151), [5](https://arxiv.org/abs/2611.17373), [6](https://arxiv.org/abs/2611.18541)).

## Open Problems and Research Directions

- **Open problem (authors’ statement):** The four-dimensional Borsuk number is still either five or six. Chalmers asks whether a diameter-one compact set on a sphere of radius at most 1/√2 can require six smaller-diameter parts; such an example would imply lower bounds in every dimension d≥4. ([Paper 2](https://arxiv.org/abs/2611.17375))
- **Open problem (authors’ statement):** Smooth-data finite-time blow-up for unforced Euler with axisymmetry and swirl remains open. The authors suggest their no-swirl multiscale mechanism as a possible route; testing whether its angular-redistribution estimates survive swirl is a research direction, not a result of this paper. ([Paper 3](https://arxiv.org/abs/2611.18151))
- **Research direction (synthesis from stated bounds):** Narrow the gap between the 1/3 lower bound and 57/61 upper bound for exceptional-time Hausdorff dimension in the directed landscape, and determine whether either bound is sharp for natural classes of finite-length paths. ([Paper 4](https://arxiv.org/abs/2611.18360))
- **Research direction (synthesis from theorem hypotheses):** Investigate whether the nilmanifold inverse theorem can be extended beyond second-countable compact abelian groups, or whether second-countability is essential to the finite-family and uniform-Lipschitz conclusions. This is a boundary-case question suggested by the stated scope, not asserted by the authors to be open. ([Paper 1](https://arxiv.org/abs/2611.17567))
- **Research direction (synthesis from the asymptotic estimate):** Seek sharper constants or thresholds in the irrational-value count, and determine whether methods from the combined elimination, hypergeometric, and Hankel-determinant approach can isolate particular odd zeta values. The paper’s bound alone does not settle individual irrationality questions. ([Paper 7](https://arxiv.org/abs/2611.16156))

## Takeaway

The most substantial shared signal is a set of precise, hypothesis-sensitive advances: a broad inverse theorem, a stronger four-dimensional partition bound, a sharp subcritical Euler blow-up construction, and new exact bounds in probability and analysis. Several proofs come with formal artifacts, but the batch is too recent and citation evidence too thin to interpret this as a robust popularity ranking; the open boundary cases remain meaningful.

## Method and sources

- **Window:** daily report for the latest arXiv Mathematics announcement batch, 2026-11-16 through 2026-11-16 (UTC batch date). Today is 2026-11-17 and no 17 November batch appeared in the recent listing, so this uses the prior batch dated 16 November. The listed batch contains 322 entries; all 322 entries in that batch were traversed, and the eight selected abstract pages were individually checked.
- **Snapshot:** 2026-11-17 01:27:31 UTC.
- **Coverage:** arXiv Mathematics archive (`math`), retaining original math primary/cross-list categories. All selected works are new submissions, not revisions. Metadata and abstracts were checked against individual arXiv abstract pages; arXiv HTML introductions/main results were additionally inspected for papers 1–3.
- **Inference:** ranked by a transparent but qualitative combination of independently found discussion where available, cross-listing, formal proof artifacts, and the concreteness and potential reach of the stated results. Because citation evidence is sparse for this very recent batch and could not be corroborated in this snapshot, this is a list of notable recent papers, not a measurement of popularity.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); the eight linked arXiv abstract pages above; [Jamneshan–Tao independent explainer](https://postcutoff.com/e/2026-11-12-jamneshan-tao-conjecture-nilspaces-gpt-astra/); [Fields Institute directed-landscape seminar](https://www.fields.utoronto.ca/talks/Roads-taken-Directed-Landscape); [University of Toronto mathematics seminar listing](https://seminars.math.toronto.edu/pages/seminars?case=view_talk&talk_id=1794859800-1794504451-154); [public mathematics account mentioning the Smale result](https://x.com/AlgebraFact/status/2121389803165929886). Semantic Scholar citation fields were not usable in this snapshot; no citation counts are claimed.
