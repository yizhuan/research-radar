# Mathematics on arXiv — latest batch: 16 October 2026

Nine notable papers from the latest Mathematics announcement batch. The newest batch is Friday, 16 October; there was no newer batch by the Sunday, 18 October snapshot. The ordering is an editorial, inferred prioritization based on the specificity and scope of the claimed results, not a popularity ranking: arXiv has no official trending chart, and recent-paper citation and attention evidence is too sparse for a defensible measured ranking.

## Top papers (ranked)

### 1. [Region bounds, error margins and certified positivity in the numerical conformal bootstrap; Or the first mathematically rigorous bounds on the 3d Ising CFT critical exponents](https://arxiv.org/abs/2610.20701)
- **Abstract:** The author closes four gaps between numerical conformal-bootstrap bounds and theorems—parameter-region coverage, unbounded spin, true rather than truncated conformal blocks, and floating-point rounding—and applies exact certificates to bound 3d Ising critical exponents under stated spectrum assumptions.
- **Authors:** Marten Reehorst
- **arXiv:** `2610.20701v1` (published 2026-10-14; UTC time not listed; categories: `hep-th`, `cond-mat.stat-mech`, `math-ph`)
- **Evidence for ranking:** A concrete mathematical certification framework with released machine-checkable certificates, plus a flagship rigorous exclusion region for the 3d Ising CFT; its central contribution is mathematical despite its cross-listed categories.
- **Claimed result:** The author certifies that for `Δσ∈[0.505,0.5405]`, the range `Δε∈(1/2,3]` is excluded except for a small rectangle containing the 3d Ising island, yielding two-sided bounds on `η` and `ν` under explicit spectrum assumptions.
- **Assumptions and setting:** Numerical conformal bootstrap for the 3d Ising CFT; the flagship bounds depend on the paper's explicitly stated spectrum assumptions. Certification uses exact arithmetic, Bernstein-basis positivity certificates, and control of the infinite-spin tail and true conformal blocks.
- **Caveat:** The result is conditional on the assumed spectrum and is not a proof of the full CFT construction. The paper says the mixed-correlator extension still has a finite list of certificates to run.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Mathematical physics; Numerical analysis & computation

### 2. [The Bardos-Tartar Conjecture for the Navier-Stokes Equations](https://arxiv.org/abs/2610.21530)
- **Abstract:** The authors prove the Bardos–Tartar density conjecture for two-dimensional periodic Navier–Stokes with time-independent forcing, extend it to a hyperviscous family, and establish additional backward-extendability results in dimensions two and three.
- **Authors:** Douglas Barnes, Samuel Liew, Edriss S. Titi
- **arXiv:** `2610.21530v1` (published 2026-10-15; UTC time not listed; categories: `math.AP`)
- **Evidence for ranking:** The paper states a resolution of a named conjecture from 1973 and a more general hyperviscous analogue; its main theorem is explicit about the strong `L²` topology and forcing assumptions.
- **Claimed result:** For 2D periodic Navier–Stokes, the authors prove that data whose solutions extend backwards to any fixed positive time are dense in the mean-zero divergence-free `L²` space; they also prove the analogous density result for their hyperviscous equations.
- **Assumptions and setting:** Incompressible viscous equations on the periodic domain, positive viscosity, time-independent forcing; the density theorem is in dimension two. Separate backward-extendability statements cover dimensions two and three.
- **Caveat:** The conjecture-resolution claim is two-dimensional; the additional 3D results do not establish global regularity or a 3D version of the density theorem.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Analysis & PDE

### 3. [A quantitative form of the planar Falconer distance theorem](https://arxiv.org/abs/2610.22222)
- **Abstract:** The authors give a quantitative planar distance-set lower bound under Frostman growth assumptions, recovering positive Lebesgue measure for compact planar sets of Hausdorff dimension above one.
- **Authors:** Guozheng Cheng, Xiang Fang, Menghan Li, Hongdou Qu, Chengbo Xiao
- **arXiv:** `2610.22222v1` (published 2026-10-15; UTC time not listed; categories: `math.CA`)
- **Evidence for ranking:** A concrete theorem at the planar Falconer threshold, with explicit dependence on Frostman data; the abstract identifies the multiscale argument and quantitative estimate rather than a conjectural direction.
- **Claimed result:** The authors prove that a compact planar set of Hausdorff dimension greater than one has a distance set of positive Lebesgue measure; they also state a uniform positive lower bound for normalized Frostman measures.
- **Assumptions and setting:** Compact subsets of the plane; the normalized theorem assumes support in the unit ball and a probability measure satisfying `ν(B(x,r)) ≤ 2r^(1+η)`, for `0<η<1`. The quantitative extension assumes a Frostman bound with exponent `1+ε`.
- **Caveat:** The quantitative estimate is not claimed to be sharp and gives neither the endpoint power nor a pinned-distance conclusion. The authors describe their approach as a planar development of an earlier multiscale manuscript.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Analysis & PDE

### 4. [Imaginary quadratic fields of class number at most 2000](https://arxiv.org/abs/2610.21511)
- **Abstract:** The paper reports an unconditional classification of imaginary quadratic fields with class number at most 2000, including a list of 16,453,493 fields and Lean-checked zero-free-region and discriminant-bound arguments.
- **Authors:** Iwao Kimura
- **arXiv:** `2610.21511v1` (published 2026-10-15; UTC time not listed; categories: `math.NT`)
- **Evidence for ranking:** A substantial extension of the reported unconditional range from class number 100 to 2000, supported by a published-data comparison, downloadable lists/code, and formalized core analytic bounds.
- **Claimed result:** The author reports exactly 16,453,493 fields, with largest absolute discriminant 1,062,350,083; the zero-gap and resulting large-discriminant bounds are formalized in Lean and reported as checked by two kernels.
- **Assumptions and setting:** Imaginary quadratic fields, class number at most 2000; the computation combines a zero-free-region bound, class-group tables for smaller discriminants, and a sieve for the remaining range.
- **Caveat:** The paper states that the sieve program itself is not formally verified, and that some low-discriminant class-number data come from prior tables. The underlying recent zero-free-region manuscript it builds on is explicitly described as not refereed.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Algebra & number theory

### 5. [The asymptotic Erdős–Frankl–Füredi cover-free conjecture](https://arxiv.org/abs/2610.22021)
- **Abstract:** The authors prove the Erdős–Frankl–Füredi asymptotic threshold for when an `r`-cover-free family can have more members than points, establishing `T(r) ≥ r²+r+2` for every `r≥1`.
- **Authors:** Xinqi Huang, Hong Liu
- **arXiv:** `2610.22021v1` (published 2026-10-15; UTC time not listed; categories: `math.CO`)
- **Evidence for ranking:** The abstract states a resolution of a named 1985 extremal-combinatorics conjecture, with a uniform explicit lower bound rather than only an asymptotic estimate.
- **Claimed result:** The authors prove `T(r) ≥ r²+r+2` for all `r≥1`, which together with the known asymptotic construction yields `T(r)=(1+o(1))r²`.
- **Assumptions and setting:** `T(r)` is the least ground-set size for which an `r`-cover-free family has more sets than points; no member of such a family is contained in the union of at most `r` other members.
- **Caveat:** The theorem establishes the asymptotic threshold, not an exact value of `T(r)` for every `r`; the matching upper bound is supplied by the known affine-plane construction asymptotically.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Combinatorics & discrete mathematics

### 6. [A Proof of the Area Vanishing Square Peg Conjecture](https://arxiv.org/abs/2610.21076)
- **Abstract:** The author resolves a problem posed by Tao related to the Toeplitz square-peg conjecture, proving that four once-winding polygonal curves in a cylinder jointly inscribe a square when an alternating area condition vanishes.
- **Authors:** Lorenzo Valerio
- **arXiv:** `2610.21076v1` (published 2026-10-15; UTC time not listed; categories: `math.SG`)
- **Evidence for ranking:** A named open-problem resolution with a crisp geometric criterion and a Floer-homological proof mechanism stated in the abstract.
- **Claimed result:** Four simple closed polygonal curves in the cylinder, each winding once positively, jointly inscribe a square if the alternating sum of their `∫y dx` integrals is zero.
- **Assumptions and setting:** Four simple closed polygonal curves in a cylinder, each with winding number one in the positive direction, satisfying the specified alternating integral constraint.
- **Caveat:** The result proves the area-vanishing case related to the Toeplitz square-peg problem, not the full square-peg conjecture for arbitrary curves.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Geometry & topology

### 7. [A counterexample to the generalized Viterbo conjecture on the spectral distance in a disc cotangent bundle](https://arxiv.org/abs/2610.22175)
- **Abstract:** The authors prove unboundedness of spectral distance for Lagrangians Hamiltonian-isotopic to the zero section under topological assumptions on a closed manifold, disproving a generalized Viterbo conjecture; they also classify surfaces where the conjecture holds over `Z₂`.
- **Authors:** Filip Broćić, Baptiste Serraille, Ibrahim Trifa
- **arXiv:** `2610.22175v1` (published 2026-10-15; UTC time not listed; categories: `math.SG`)
- **Evidence for ranking:** A claimed counterexample to a named symplectic-geometry conjecture paired with a classification result for the surface case.
- **Claimed result:** The authors report that spectral distance is unbounded on the stated space of Lagrangians for closed manifolds satisfying specified topological assumptions; they classify all surfaces for which the conjecture holds over `Z₂`.
- **Assumptions and setting:** Lagrangians Hamiltonian-isotopic to the zero section in a disc cotangent bundle of a closed manifold, with the theorem's topological assumptions; the surface classification uses coefficients `Z₂`.
- **Caveat:** The counterexample applies under the stated topological assumptions; the result does not say the conjecture fails for every closed manifold or every coefficient system.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Geometry & topology

### 8. [A New Bound for the Gauss Circle Problem](https://arxiv.org/abs/2610.21730)
- **Abstract:** The authors improve the uniform error term in the planar Gauss circle problem to `E(X)=Oε(X^(209/670+ε))` for every `ε>0`.
- **Authors:** Xi Cen, Xitao Gao, Cheng Zhang, Junyong Zhang
- **arXiv:** `2610.21730v1` (published 2026-10-15; UTC time not listed; categories: `math.NT`)
- **Evidence for ranking:** The abstract gives a precise improved exponent and identifies the prior `5/16` barrier it surpasses, alongside concrete new estimates used in the proof.
- **Claimed result:** For real `X≥4`, the authors prove `E(X)=Oε(X^(209/670+ε))` for every `ε>0`.
- **Assumptions and setting:** `E(X)` is the lattice-point count in the radius-`√X` disk minus its area `πX`; the estimate is uniform in real `X≥4`.
- **Caveat:** The paper presents an exponent improvement, not an optimal error term; no sharpness claim is made in the abstract.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Algebra & number theory

### 9. [The monodromy conjecture for high order poles, and norms of residue antiderivatives](https://arxiv.org/abs/2610.22111)
- **Abstract:** The author proves a strong local monodromy statement for poles of order at least `n−1` of the naive motivic zeta function of a complex polynomial in `n` variables, and constructs associated homology eigencycles.
- **Authors:** Alexander Esterov
- **arXiv:** `2610.22111v1` (published 2026-10-15; UTC time not listed; categories: `math.AG`)
- **Evidence for ranking:** A theorem addressing a named conjecture in a specified high-order regime, with an explicit geometric construction attached to each covered pole.
- **Claimed result:** The author states that every covered pole has a local homology `exp(2πis)`-eigencycle near a contributing one-dimensional exceptional stratum; the proof combines topological methods with a birational-geometric fact described as AI-discovered.
- **Assumptions and setting:** A complex polynomial in `n` variables and poles of order at least `n−1` of its naive motivic zeta function; the construction is local near a contributing one-dimensional exceptional stratum.
- **Caveat:** The stated result covers only the specified high-order poles; it should not be read as resolving the conjecture for every pole. This is a new preprint, not an independently reviewed result.
- **Announcement type:** new submission, 2026-10-16 batch
- **Themes:** Geometry & topology

## Trending Research Themes

- **Certified quantitative bounds (several distinct signals):** the conformal-bootstrap paper turns numerical exclusions into exact certificates; the Falconer paper quantifies distance-set measure under Frostman growth; the Gauss-circle paper improves a lattice-point exponent. Their problems and methods differ, so this is not evidence of a single field-wide shift.
- **PDE structure and solution-space geometry:** the Navier–Stokes paper resolves a density conjecture in 2D and analyzes backward extendability in 2D/3D; this is a notable isolated PDE result in the selected batch.
- **Conjectures under structural hypotheses:** the cover-free paper proves an asymptotic threshold, while the square-peg and Viterbo papers settle or refute specified symplectic-geometric formulations. These are independent results, not a shared technique.
- **Formalized and computational number theory (isolated signal):** Kimura combines analytic bounds, class-group data, computation, and Lean formalization to extend a reported unconditional classification range.

## Open Problems and Research Directions

- **3d Ising bootstrap:** the reported exponent bounds depend on explicit spectrum assumptions; the paper says a finite list of certificates remains to be run for its mixed-correlator extension. Completing those checks and determining whether the assumptions can be weakened would test the scope of the result. [2610.20701]
- **Navier–Stokes:** the density conjecture is proved in the stated 2D periodic setting, not in 3D. A natural direction is to determine which parts of the density or backward-extendability picture survive under three-dimensional assumptions; this is a proposed extension, not a claim of the paper. [2610.21530]
- **Falconer estimate:** the paper leaves sharpness, the endpoint dependence on the Frostman constant, and pinned-distance statements open in its own scope. Follow-up work could test whether the quantitative constants or method extend to higher dimensions; the authors say those cases are planned for later versions. [2610.22222]
- **Class-number enumeration:** the paper itself distinguishes Lean-checked analytic bounds from a sieve computation that is not formally verified. Independent reproduction or formal verification of that computational component would strengthen the end-to-end certification. [2610.21511]
- **Square peg / Viterbo:** the square-peg result is limited to the area-vanishing case, while the Viterbo paper gives a counterexample only under stated topological assumptions and classifies surfaces over `Z₂`. Extending either theorem to broader curve, manifold, or coefficient settings is a concrete follow-up direction. [2610.21076; 2610.22175]

## Takeaway

The batch's strongest signals are unusually concrete: exact bootstrap certificates for 3d Ising bounds, a 2D Navier–Stokes conjecture resolution, a planar Falconer estimate, and several conjecture-level results in combinatorics and symplectic geometry. These remain preprint claims, not independently validated conclusions; the assumptions and scope—especially in the bootstrap and computational number-theory papers—matter.

## Method and sources

- **Window:** daily; the latest arXiv Mathematics announcement batch was Friday, 2026-10-16. The current calendar day (2026-10-18) had no newer batch at the time checked, so this report uses the prior batch. Exact batch window: 2026-10-16 through 2026-10-16.
- **Coverage:** the full Mathematics recent listing for the 16 October batch (437 entries) was traversed and screened for explicit theorem, conjecture, classification, bound, or counterexample claims. Selected papers are from the `math.*` archive, except the conformal-bootstrap paper, included because its central contribution is mathematical; all listed arXiv categories are preserved.
- **Snapshot:** 2026-10-18 00:18:17 UTC.
- **Inference:** arXiv provides no official trending chart. Recent papers have too little comparative citation and independent-attention evidence for a measured popularity ranking, so these are notable recent papers ordered by the specificity and scope of their stated results. Semantic Scholar coverage and independent expert/seminar discussion could not be established for these candidates; this is not evidence of zero citations.
- **Sources:** individual arXiv abstract pages linked above; for the top three, the arXiv HTML versions were also inspected for the introduction and main-result statements. The authors' claims are summarized as preprint claims, not as independently checked proofs.
