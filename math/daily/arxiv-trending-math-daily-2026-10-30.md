# arXiv Mathematics — daily notable papers — Friday, 30 October 2026

Nine papers from the latest Mathematics announcement batch stand out for concrete conjecture resolutions, a claimed counterexample to a long-standing module-theory conjecture, and rigorous constructions bridging neighboring fields. Spoken agenda: three headline claims, then probability, geometry, quantum symmetry, and the limits still open. This is an inferred ranking—not an official arXiv trending chart—and citation evidence is limited for papers announced so recently; treat it as a notable-paper selection, not a popularity measurement.

## Top papers (ranked)

### 1. [A counterexample to the pure semisimplicity conjecture](https://arxiv.org/abs/2610.39883)
- **Abstract:** The paper constructs a division-ring extension yielding a triangular ring that is right pure semisimple but neither left pure semisimple nor of finite representation type, contradicting the pure semisimplicity conjecture.
- **Authors:** Junpeng Ren
- **arXiv:** `2610.39883v1` (published 2026-10-29T11:58:26Z; categories: `math.RA` primary; no cross-lists)
- **Evidence for ranking:** A concrete counterexample to a long-standing conjecture, an accompanying Lean 4 formalization linked from the arXiv comments, and early external coverage by MathWorld and AI Proof Watch. These are attention/checkability signals, not peer review; no journal reference was listed in the sources checked.
- **Claimed result:** The author proves that the triangular ring built from the specified division-ring extension is right pure semisimple, but not left pure semisimple and not of finite representation type; this would refute the conjecture.
- **Assumptions and setting:** The construction uses a division ring T formed from fraction division rings of nearest-neighbour quantum Laurent algebras with parameter 1/2, and a subring H with right dimension sequence (1,2,2,…).
- **Caveat:** This is a preprint claim. The arXiv comment says the Lean development corresponds to an earlier manuscript snapshot, so it does not alone certify the current version.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Algebra & number theory

### 2. [A proof of the Murty--Simon conjecture on diameter-2-critical graphs](https://arxiv.org/abs/2610.39032)
- **Abstract:** The authors prove that every finite n-vertex diameter-2-critical graph has at most floor(n²/4) edges, with equality only for the balanced complete bipartite graph, for every n.
- **Authors:** Sanjana Das, Jacob Fox
- **arXiv:** `2610.39032v1` (published 2026-10-28T23:04:24Z; categories: `math.CO` primary; no cross-lists)
- **Evidence for ranking:** The claimed result closes the all-n conjecture, including its equality case; a public Lean 4/Mathlib formalization was independently located and checked. This is a theorem-and-verifiability basis for placement, not a citation-based popularity signal.
- **Claimed result:** The paper proves the Murty--Simon edge bound and uniqueness of the extremal graph for every n≥3; its introduction reduces the proof to a maximal-matching inequality and a characterization of equality.
- **Assumptions and setting:** Finite diameter-2-critical graphs: every vertex pair is at distance at most 2, and deleting any edge destroys that property.
- **Caveat:** The authors state that AI first found the edge-bound proof; they simplified it and developed the equality-case argument themselves. This remains a preprint claim requiring mathematical review.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 3. [Nonuniqueness of the 2D Euler Evolutions with L¹∩Lᵖ Vorticity](https://arxiv.org/abs/2610.40553)
- **Abstract:** For each fixed 1<p<∞, the authors construct one compactly supported initial vorticity in L¹∩Lᵖ that has two distinct, exactly transported evolutions of the unforced planar Euler equation on [0,1].
- **Authors:** Thomas Y. Hou, Xiang Qin, Peicong Song, Wenhan Zhang
- **arXiv:** `2610.40553v1` (published 2026-10-29T17:39:32Z; categories: `math.AP` primary; no cross-lists)
- **Evidence for ranking:** The introduction states a precise theorem for every finite p, with both evolutions strongly continuous in the stated norms and transported by regular Lagrangian flows. The authors also identify a contemporaneous independent construction using essentially the same core mechanism.
- **Claimed result:** The authors prove nonuniqueness by coupling unstable four-vortex configurations across infinitely many scales so a vanishing initial perturbation leaves a detectable difference at positive time.
- **Assumptions and setting:** Unforced two-dimensional incompressible Euler; the datum is real and compactly supported, and may depend on the prescribed finite exponent p. Each flow is almost-everywhere invertible and measure-preserving.
- **Caveat:** The construction does not claim nonuniqueness at p=∞; the authors distinguish finite-Lᵖ membership from stronger quantitative control as p grows. They also cite Choi's independently developed work using essentially the same mechanism.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Analysis & PDE

### 4. [JT gravity as a conformal scaling limit of random flat combinatorial disks](https://arxiv.org/abs/2610.40645)
- **Abstract:** The paper proves a criterion based on branching explorations and applies it to a Boltzmann ensemble of rectilinear-boundary combinatorial disks, whose rescaled surfaces converge to the continuum random surface prescribed by flat JT gravity.
- **Authors:** Morris Ang
- **arXiv:** `2610.40645v1` (published 2026-10-29T17:59:13Z; categories: `math.PR` primary, `math-ph` cross-list)
- **Evidence for ranking:** Cross-listed in probability and mathematical physics; the abstract states a scaling-limit theorem and a branching-exploration criterion, with a conformal-welding theorem supplied by a companion paper. Semantic Scholar reports 0 citations at the snapshot; that is a current total, not a period gain.
- **Claimed result:** As a distinguished boundary side tends to infinite length, the rescaled disk converges in law, in the stated interior conformal-factor topology, to the flat JT-gravity surface; under a tightness condition the criterion extends to discrete disks.
- **Assumptions and setting:** The worked example is a Boltzmann ensemble of disks with rectilinear boundary; the limit uses uniformization in a fixed domain and a branching exploration with conditioned Cauchy-process lengths.
- **Caveat:** The theorem is established for the stated ensemble and criterion; other natural disk models are proposed as applications, not proved scaling limits here.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 5. [An Adian-Rabin theorem for quantum automorphism groups of graphs](https://arxiv.org/abs/2610.40590)
- **Abstract:** The authors prove that many properties of graph quantum-automorphism groups—including having quantum symmetries and having a nontrivial discrete quantum automorphism group—are undecidable.
- **Authors:** Josse van Dobben de Bruyn, William Slofstra
- **arXiv:** `2610.40590v1` (published 2026-10-29T17:48:22Z; categories: `math.QA` primary; `math.CO`, `math.GR`, `math.OA` cross-lists)
- **Evidence for ranking:** It is cross-listed across four mathematical subjects and gives explicit undecidability results; Semantic Scholar currently lists 1 citation and 0 influential citations, a current total rather than a period gain.
- **Claimed result:** The authors establish an Adian-Rabin theorem for quantum automorphism groups of graphs and for solution groups associated with linear-system nonlocal games.
- **Assumptions and setting:** The objects are graph quantum-automorphism algebras and their discrete quantum groups; the method reduces questions to solution groups of linear-system games.
- **Caveat:** Undecidability rules out a general decision procedure but does not classify the quantum symmetries of any particular graph.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics; Mathematical physics

### 6. [Serre's conjectures for Q(√13)](https://arxiv.org/abs/2610.38884)
- **Abstract:** Assuming GRH and a minor technical result, the authors claim to prove Serre's conjectures for Q(√13) and establish a reduction-to-level-1 result for real quadratic fields with narrow class number one.
- **Authors:** Luis Dieulefait, Ariel Pacetti
- **arXiv:** `2610.38884v1` (published 2026-10-28T20:48:06Z; categories: `math.NT` primary; no cross-lists)
- **Evidence for ranking:** The abstract combines a named conjecture for a specific field with a reduction theorem over a broader class of real quadratic fields; the result is explicitly conditional rather than an unconditional resolution.
- **Claimed result:** The authors prove the conjectures for Q(√13) under the stated assumptions and a reduction-to-level-1 theorem for every real quadratic field of narrow class number one.
- **Assumptions and setting:** GRH and one minor technical result are assumed; the field-specific base cases are established only for Q(√13).
- **Caveat:** The argument is conditional, and the authors say they cannot yet establish the needed base cases for other fields.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Algebra & number theory

### 7. [A complete solution to the reverse isoperimetric problem for λ-convex bodies](https://arxiv.org/abs/2610.40291)
- **Abstract:** For λ>0, the authors show that among λ-convex bodies in Euclidean space with fixed surface area, the intersection of two radius-1/λ balls minimizes volume, confirming Borisenko's conjecture in every dimension n≥2.
- **Authors:** Kostiantyn Drach, Kateryna Tatarko
- **arXiv:** `2610.40291v1` (published 2026-10-29T15:41:08Z; categories: `math.MG` primary, `math.DG` cross-list)
- **Evidence for ranking:** The abstract claims a complete all-dimensions resolution and extends the inequality to all constant-curvature model spaces; cross-listed in metric and differential geometry.
- **Claimed result:** The λ-convex lens minimizes volume at fixed surface area in Rⁿ, and the authors extend the reverse inequality to constant-curvature model spaces in arbitrary dimension and for every λ>0.
- **Assumptions and setting:** λ-convex means an intersection of balls of radius 1/λ; λ is positive and surface area is fixed.
- **Caveat:** The result concerns this constrained class and the stated constant-curvature model spaces, not arbitrary convex bodies in arbitrary ambient geometries.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Geometry & topology

### 8. [A self-normalized law of the iterated logarithm for Rademacher random multiplicative functions](https://arxiv.org/abs/2610.40605)
- **Abstract:** For a squarefree-supported Rademacher random multiplicative function, the authors prove a two-sided law of the iterated logarithm normalized by its full predictable quadratic variation, with almost-sure cluster set [-1,1].
- **Authors:** Dariusz Buraczewski, Alexander Iksanov
- **arXiv:** `2610.40605v1` (published 2026-10-29T17:52:57Z; categories: `math.PR` primary, `math.NT` cross-list)
- **Evidence for ranking:** A precise almost-sure limit theorem and an explicit probability/number-theory bridge; the abstract also isolates a remaining growth dichotomy rather than claiming it is settled.
- **Claimed result:** The normalized partial sums have limsup 1, liminf -1, and cluster set [-1,1]; moreover, no positive deterministic q makes Q(x)/q(x) converge in probability to 1.
- **Assumptions and setting:** f is a Rademacher random multiplicative function supported on squarefree integers, and Q is the full predictable quadratic variation of the prime-revealing martingale.
- **Caveat:** The authors do not decide whether a second limsup, normalized by √x(log log x)^(1/4), is finite and positive with a nondegenerate law or infinite almost surely.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Probability & statistics; Algebra & number theory

### 9. [Multicomplexes in Action: Strong Formality of Compact Hyperkähler Manifolds](https://arxiv.org/abs/2610.40639)
- **Abstract:** The author proves that every compact hyperkähler manifold is bigraded strongly formal in the sense of Milivojević and Stelzig, using algebraic formality results for multicomplexes and commutative n-differential graded algebras.
- **Authors:** Antonio Pio Contrò
- **arXiv:** `2610.40639v1` (published 2026-10-29T17:58:39Z; categories: `math.AT` primary; `math.AG`, `math.DG` cross-lists)
- **Evidence for ranking:** Cross-listed across algebraic topology, algebraic geometry, and differential geometry; the abstract states a general algebraic theorem and a geometric application. No citation or independent discussion signal was available in the sources checked.
- **Claimed result:** The author establishes a generalized ∂∂̄-lemma and an algebraic formality theorem for the stated multicomplex setting, yielding strong formality for compact hyperkähler manifolds.
- **Assumptions and setting:** The geometric conclusion is for compact hyperkähler manifolds; the algebraic framework is categories of multicomplexes and commutative n-differential graded algebras.
- **Caveat:** The abstract does not claim the same conclusion for broader classes of non-Kähler manifolds.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Geometry & topology

## Trending Research Themes

- **Conjecture resolution and counterexample construction are a visible, but not field-wide, pattern in this batch:** Ren's proposed counterexample to pure semisimplicity [1], Das–Fox's all-n proof of Murty--Simon [2], and Drach–Tatarko's confirmation of Borisenko's conjecture [7] make distinct kinds of global claims.
- **Several papers make explicit bridges across mathematical areas:** random multiplicative functions connect probability and number theory [8]; JT gravity links random-disk explorations to continuum mathematical physics [4]; and quantum graph symmetries connect quantum algebra, combinatorics, group theory, and operator algebras [5]. These are distinct bridges, not evidence of a shared technique.
- **Constructive and auditability signals recur in a few entries:** the pure-semisimplicity and Murty--Simon papers have Lean artifacts [1, 2], while the Euler result relies on exact vortex-patch constructions [3]. The proofs and formalization scopes still need independent mathematical scrutiny.
- The papers do not establish a single dominant method or a field-wide shift. The small daily sample contains very different objects and hypotheses.

## Open Problems and Research Directions

- **Author-stated unresolved question — [8]:** Determine which alternative holds for the limsup normalized by √x(log log x)^(1/4): a finite positive nondegenerate random limit superior, or infinity almost surely. A follow-up could seek sharper tail or distributional estimates for Q(x) and M(x).
- **Author-stated limitation — [6]:** The reduction-to-level-1 theorem covers real quadratic fields with narrow class number one, but the necessary base cases are supplied only for Q(√13), under GRH and a minor technical assumption. Establishing or testing those base cases for other fields is a natural extension; this is a proposed direction, not a claim of novelty or tractability.
- **Synthesis from the hypotheses — [3]:** Since the constructed datum and parameters depend on each finite p, a useful next question is how this nonuniqueness result fits alongside known uniqueness regimes under stronger vorticity controls, and how the boundary between those function-space assumptions can be described. The paper itself also notes a contemporaneous construction with a similar core mechanism.
- **Validation direction — [1, 2]:** The two conjecture-level claims merit independent proof review; for [1], the Lean snapshot is explicitly earlier than the submitted manuscript, while [2] reports AI assistance in the initial proof. Comparing the formal artifacts against the exact submitted arguments is a concrete check, not a statement that either claim is incorrect.

## Takeaway

The batch's strongest mathematical stories are several sharply stated conjecture-level claims and constructions whose hypotheses matter: the pure-semisimplicity counterexample, the all-n Murty--Simon proof, and Euler nonuniqueness in every finite Lᵖ class. They are striking author claims in fresh preprints, not settled community consensus; conditional assumptions, formalization scope, and independent proof review remain central uncertainties.

## Method and sources

- **Window:** daily; the exact announcement-batch window is 2026-10-30 through 2026-10-30. The latest Mathematics listing showed Friday, 30 October 2026, with 874 entries in that batch; the full batch was screened. Saturday, 31 October had no batch, so this uses the prior batch. Snapshot time: 2026-10-31T17:33:37Z.
- **Coverage:** arXiv Mathematics (`math`) recent listing, retaining its subject categories and cross-lists. Each selected abstract page and submission history was checked live; the top three papers' introductions/main-result statements were inspected in arXiv HTML. The arXiv API XML was used to cross-check versions, UTC timestamps, authors, categories, abstracts, and comments. The configured `web_extract` service could not extract URLs, so the browser and arXiv API were used instead.
- **Ranking:** qualitative and inferred from concrete claims, cross-listing, linked proof artifacts, and early external coverage, with recency only a tie-breaker. There is no official arXiv trend ranking. Semantic Scholar returned records for only two selected papers: the JT-gravity paper had 0 current citations; the quantum-automorphism paper had 1 current citation and 0 influential citations. These are current totals, not gains in this window; evidence is too sparse to measure popularity. Web searches found no independent seminar discussion for the selected papers.
- **Sources:** [Mathematics recent listing](https://arxiv.org/list/math/recent); the nine linked arXiv abstracts above; [Semantic Scholar Graph API record for 2610.40645](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.40645?fields=title,authors,year,citationCount,influentialCitationCount,referenceCount,publicationTypes,fieldsOfStudy,externalIds) and [2610.40590](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.40590?fields=title,authors,year,citationCount,influentialCitationCount,referenceCount,publicationTypes,fieldsOfStudy,externalIds); [MathWorld on pure semisimplicity](https://mathworld.wolfram.com/PureSemisimplicityConjecture.html); [AI Proof Watch coverage](https://aiproofwatch.com/updates/a-counterexample-to-the-pure-semisimplicity-conjecture-ff5b8d97); [Murty--Simon Lean formalization](https://github.com/jtraverso/murty-simon-conjecture).
