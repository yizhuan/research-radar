# arXiv Mathematics — latest batch: Monday, 12 October 2026

Seven notable recent papers, led by a long-standing sandpile question resolved in two dimensions, a formalization of geometrization, and new arithmetic- and differential-geometric results. Spoken agenda: probability and formal verification first, then conjectures, geometric counterexamples, and a topology–machine-learning bridge. This is an inferred selection, not an official arXiv trend ranking: arXiv publishes no trending chart, and citation evidence is sparse for papers only days old, so order reflects a small amount of independent discussion plus the specificity and reach of the claimed results—not measured popularity.

## Top papers (ranked)

### 1. [Sandpile avalanches in two dimensions are finite](https://arxiv.org/abs/2610.13940)
- **Abstract:** In the stationary abelian sandpile on \(\mathbb{Z}^2\), the author proves that adding one grain almost surely stabilizes, despite the divergent two-dimensional random-walk Green function, with a polylogarithmic upper bound on the chance the avalanche reaches distance \(R\).
- **Authors:** Ahmed Bou-Rabee
- **arXiv:** `2610.13940v1` (published 2026-10-09 17:57:56 UTC; categories: `math.PR`)
- **Evidence for ranking:** The abstract identifies a question repeatedly posed in the sandpile literature; arXiv links a Lean formalization, and a contemporaneous X post discusses the result. These are checkable attention/artifact signals, not citation gains.
- **Claimed result:** The author proves that for almost every stationary sandpile, adding a grain at the origin stabilizes; the probability that the avalanche radius exceeds \(R\) is at most \(C(\log(R+2))^{-a}\) for constants \(a>0\), \(C<\infty\). The paper reduces the problem to a uniform-spanning-tree estimate proved by a multiscale electrical argument.
- **Assumptions and setting:** The infinite-volume stationary state is the local limit of uniform recurrent sandpiles on wired boxes in \(\mathbb{Z}^2\); the event concerns one grain added at the origin.
- **Caveat:** The tail estimate is an upper bound, not a sharp asymptotic; I have not independently checked the proof or Lean artifact.
- **Announcement type:** new submission, announcement batch 2026-10-12
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics

### 2. [A Lean Formalization of the Hamilton--Perelman Proof of Thurston's Geometrization Conjecture](https://arxiv.org/abs/2610.13897)
- **Abstract:** The authors formalize the Hamilton–Perelman Ricci-flow proof of geometrization and state a Lean theorem producing prime factors, incompressible-torus decompositions, and complete geometric structures on the resulting pieces.
- **Authors:** Yuan Liao, Ziyang Qin, Jui-Hui Chung, Ayush Khaitan, Zhengyang Zhang, et al.
- **arXiv:** `2610.13897v1` (published 2026-10-09 17:43:01 UTC; categories: `math.DG`)
- **Evidence for ranking:** Papers with Lean lists the formalization, and a coauthor publicly announced its completion; the paper also points to a public Lean declaration and formal artifact. This is visible community attention and a verifiable artifact, not a citation-count trend.
- **Claimed result:** The authors report a Lean formalization of geometrization for connected, closed, oriented smooth 3-manifolds, following the Ricci-flow route. The paper states that each prime factor can be cut along a finite disjoint family of incompressible tori so the interiors of the pieces admit complete Thurston geometries.
- **Assumptions and setting:** The theorem's input is a connected, closed, oriented smooth 3-manifold. The paper clarifies that the torus family need not be the canonical JSJ family and asserts finite volume only for hyperbolic pieces.
- **Caveat:** The claim is about the reproduced Lean endpoint and its stated theorem; independent reproduction of the pinned formal artifact and its dependencies is still the useful verification step for readers.
- **Announcement type:** new submission, announcement batch 2026-10-12
- **Themes:** Geometry & topology; Logic & foundations

### 3. [The Tate Conjecture for Ordinary Calabi-Yau Threefolds](https://arxiv.org/abs/2610.13939)
- **Abstract:** Using canonical lifts, the author proves the integral geometric Tate conjecture for ordinary Calabi–Yau threefolds over finite fields, with related divisor-class results in higher dimensions.
- **Authors:** Lukas Brantner
- **arXiv:** `2610.13939v1` (published 2026-10-09 17:57:50 UTC; categories: `math.AG`, `math.NT`)
- **Evidence for ranking:** The paper is cross-listed in algebraic geometry and number theory, and its introduction states a precise theorem on a central cycle-class conjecture. The sources checked did not provide a reliable attention or citation-momentum measure for this very new submission.
- **Claimed result:** The author proves the integral geometric Tate conjecture for ordinary Calabi–Yau threefolds, and also for strict 1-ordinary threefolds; in higher dimensions, the paper proves it for divisor classes under 2-ordinarity and a cohomology vanishing condition.
- **Assumptions and setting:** The threefold result is over a finite field and applies to smooth, projective, geometrically irreducible Calabi–Yau varieties with trivial canonical bundle; the stated cases impose ordinarity or 1-ordinarity plus strictness. The higher-dimensional statement is only for divisor classes and assumes 2-ordinarity and \(H^2(X,\mathcal O_X)=0\).
- **Caveat:** This is not a proof of the Tate conjecture for arbitrary Calabi–Yau varieties; the ordinarity and related hypotheses are essential to the stated results.
- **Announcement type:** new submission, announcement batch 2026-10-12
- **Themes:** Algebra & number theory; Geometry & topology

### 4. [A counterexample to Nirenberg's conjecture on closed asymptotic curves](https://arxiv.org/abs/2610.13848)
- **Abstract:** The authors construct a negatively curved embedded annulus in \(\mathbb{R}^3\) with two closed asymptotic curves, contradicting the stated 1962 conjecture.
- **Authors:** Harrison Banks, Mohammad Ghomi, Hongda Qiu, Matteo Raffaelli
- **arXiv:** `2610.13848v1` (published 2026-10-09 16:55:33 UTC; categories: `math.DG`)
- **Evidence for ranking:** A concrete counterexample to a named historical conjecture is the primary significance signal; the paper is short and gives a specific construction. No independent discussion or citation momentum was established in the sources checked.
- **Claimed result:** The authors construct a smooth embedded annulus with negative Gauss curvature in its interior, whose boundary consists of two strictly convex curves in tangent planes, and which contains two closed asymptotic curves. They use Lelieuvre's formula and a periodic Riccati-equation solution.
- **Assumptions and setting:** The construction is a surface in Euclidean \(\mathbb{R}^3\), with the specified curvature and boundary geometry; the counterexample concerns the conjecture about closed asymptotic curves in this setting.
- **Caveat:** The result supplies a counterexample to the stated conjecture, not a general classification of closed asymptotic curves on negatively curved surfaces.
- **Announcement type:** new submission, announcement batch 2026-10-12
- **Themes:** Geometry & topology

### 5. [The Bernstein problem in higher dimensional Heisenberg groups](https://arxiv.org/abs/2610.13913)
- **Abstract:** For every sub-Riemannian Heisenberg group \(\mathbb{H}^n\), \(n\geq2\), the authors prove that there is a global perimeter minimizer whose boundary is a smooth, non-characteristic entire intrinsic graph but is not a vertical hyperplane.
- **Authors:** Gianmarco Giovannardi, Simone Verzellesi
- **arXiv:** `2610.13913v1` (published 2026-10-09 17:50:55 UTC; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** The result gives an explicit nonflat global minimizer in every stated dimension and connects differential geometry with PDE/variational analysis through its cross-listing. No independent attention or citation-momentum signal was available in the sources checked.
- **Claimed result:** The authors prove existence of an entire intrinsic graph that minimizes perimeter globally while not being a vertical hyperplane, for each \(n\geq2\).
- **Assumptions and setting:** This is the sub-Riemannian perimeter problem in higher-dimensional Heisenberg groups; it is not the classical Euclidean Bernstein problem.
- **Caveat:** The abstract's result is limited to \(n\geq2\) Heisenberg groups and the stated intrinsic-graph class; it does not settle other Bernstein problems.
- **Announcement type:** new submission, announcement batch 2026-10-12
- **Themes:** Geometry & topology; Analysis & PDE

### 6. [On some rigidity results for high-dimensional confoliations](https://arxiv.org/abs/2610.13927)
- **Abstract:** The authors prove an obstruction to contact regions for c-symplectic confoliations in odd dimensions, derive a five-dimensional Reeb-stability analogue under stronger assumptions, and construct strong symplectic foliations that cannot be contact approximated in two specified senses.
- **Authors:** Fabio Gironella, Seungook Yu
- **arXiv:** `2610.13927v1` (published 2026-10-09 17:55:00 UTC; categories: `math.SG`, `math.GT`)
- **Evidence for ranking:** The paper links symplectic geometry and geometric topology, with results stated for any odd ambient dimension and a specific 5D application. The ranking is based on the scope and concrete applications of the abstract, not measured readership.
- **Claimed result:** The authors establish the contact-region obstruction and two notions of contact approximation; they give an odd-dimensional example of a c-symplectic, strong symplectic foliation that admits neither of those approximations, using pseudoholomorphic-curve theory.
- **Assumptions and setting:** The results concern c-symplectic confoliations and the paper's specified contact-approximation notions; its 5D Reeb-stability analogue requires stronger assumptions than the 3D theorem it generalizes.
- **Caveat:** These are structured hypotheses and approximation notions, not a blanket obstruction for all confoliations or all contact approximations.
- **Announcement type:** new submission, announcement batch 2026-10-12
- **Themes:** Geometry & topology

### 7. [Constructive Bounds for the Topological Expressivity of Neural Networks](https://arxiv.org/abs/2610.13931)
- **Abstract:** The author gives constructive architecture bounds for ReLU networks to represent spaces with prescribed Betti-number patterns, shifting the topological expressivity target from decision boundaries to network outputs.
- **Authors:** Kosio Beshkov
- **arXiv:** `2610.13931v1` (published 2026-10-09 17:55:33 UTC; categories: `math.AT`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed between algebraic topology and machine learning and states explicit constructive bounds, making it a clear cross-field contribution. No paper-specific independent discussion or citation momentum was established in the sources checked.
- **Claimed result:** The author proves sufficient architecture bounds for ReLU networks to express spaces homotopy equivalent to wedge sums of spheres with arbitrary Betti numbers, and improves the bounds for Betti-number sequences arising from products of spheres. A tighter bound for a sphere is presented as a conjecture, not a theorem.
- **Assumptions and setting:** The result concerns topological expressivity of network outputs (the topology of \(\Phi(X)\)) and ReLU architectures; it is a representation result rather than a claim about training or predictive performance.
- **Caveat:** The stronger proposed architecture bound is conjectural, and the proved bounds do not by themselves imply that optimization will find the represented topology.
- **Announcement type:** new submission, announcement batch 2026-10-12
- **Themes:** Geometry & topology; Machine learning theory

## Trending Research Themes

- **A cluster of sharp yes/no geometric and arithmetic statements:** the sandpile paper settles an explicit 2D finiteness question, the Tate paper proves a conjecture in ordinary/strict-ordinary Calabi–Yau cases, and the Nirenberg and Heisenberg papers give counterexamples to Bernstein-type or geometric expectations in sharply specified settings. These are distinct problems, not evidence of a single field-wide shift.
- **Proofs as mathematical infrastructure:** the geometrization formalization and the sandpile paper's linked Lean artifact make formal verification visible alongside deep classical arguments. The geometrization paper is a broad formalization claim; the sandpile artifact is linked, but its proof has not been independently audited here.
- **Cross-field methods and objects:** confoliations combine symplectic and contact geometry; the Heisenberg minimizer sits at the geometry/PDE interface; and the ReLU expressivity paper connects algebraic topology with machine learning. Each bridge is paper-specific rather than a measured increase in cross-disciplinary submissions.

## Open Problems and Research Directions

- **Author-stated — sandpile tail:** the paper proves only a negative-power-of-log upper bound for the radius tail. Sharpening the decay or identifying a matching lower bound would refine the result; the paper's main result and limitation are in [2610.13940](https://arxiv.org/abs/2610.13940).
- **Author-stated — broader Tate cases:** the author notes that canonical-lift methods may help with further Tate-conjecture cases. A concrete next test is to identify which nonordinary or weaker-ordinarity Calabi–Yau families still admit a lift/specialization argument, while preserving the integral cycle-class conclusion ([2610.13939](https://arxiv.org/abs/2610.13939)).
- **Synthesis — formal verification and geometric scope:** independently reproduce the geometrization Lean artifact and document its dependencies, then assess which neighboring statements (for example, uniqueness/canonicity of the decomposition) are formalized or remain outside the theorem as stated ([2610.13897](https://arxiv.org/abs/2610.13897)). This is a verification/generalization task, not a claim that the formalization is incorrect.
- **Synthesis — boundary of the Heisenberg result:** characterize which geometric features permit nonvertical global minimizers, and test whether analogous constructions persist under nearby sub-Riemannian structures or additional constraints ([2610.13913](https://arxiv.org/abs/2610.13913)).

## Takeaway

The clearest headline is a resolution of a long-standing two-dimensional sandpile finiteness question, accompanied by an unusually broad formalization claim and several crisp conjecture/counterexample results. Because the batch is very recent and independent citation evidence is thin, treat this as a curated notable-paper list—not a popularity leaderboard—and read the preprints for hypotheses and proof details.

## Method and sources

- **Window:** daily; latest arXiv Mathematics announcement batch visible on 2026-10-14 was Monday, 2026-10-12. The calendar day 2026-10-14 had no newer batch at the 00:20:22 UTC snapshot. The batch listing showed 388 entries; it was screened as a complete batch, and the seven selected abstracts were checked against arXiv records.
- **Coverage:** arXiv Mathematics (`math`), retaining math primary/cross-list categories; neighboring categories are shown only where the selected paper is cross-listed.
- **Ranking:** inferred from a limited, checkable set of independent attention/artifact signals (including Papers with Lean and a contemporaneous X post for the top formalization/sandpile results), explicitness and scope of claimed mathematical results, and cross-subfield relevance. No official arXiv trend chart exists. Current citation evidence was too sparse to support a popularity or citation-momentum ranking; no numeric score is used.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); individual arXiv abstract pages linked above. Additional attention checks: [Papers with Lean](https://paperswithlean.com/) and [coauthor announcement on X](https://x.com/ayushkhaitan343/status/2108654050203840528); for the sandpile paper, [contemporaneous X discussion](https://x.com/AmericaGetBig/status/2109985058983436712). Abstracts and the introduction/main-results sections of the sandpile, Tate, and geometrization papers were read; no proof was independently verified.
- **Snapshot:** 2026-10-14 00:20:22 UTC.
