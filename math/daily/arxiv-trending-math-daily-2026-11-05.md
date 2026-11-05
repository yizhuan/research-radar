# Mathematics on arXiv — 5 November 2026 announcement batch

9 notable recent papers; the clearest concentration is graph theory moving from conjectural structure to sharper quantitative bounds, alongside a few major-looking classification, probability, and PDE claims. I’ll go from graph bounds to random structures and geometry, then close on the most delicate analytical result. This is an inferred ranking: arXiv supplies no official trending chart, and citation evidence is limited for papers this recent.

## Top papers (ranked)

### 1. [A Viscous Cascade Construction of Nonunique Leray--Hopf Solutions to the Unforced 3D Navier--Stokes Equations](https://arxiv.org/abs/2611.06117)
- **Abstract:** The authors construct a continuum of distinct suitable Leray--Hopf solutions to unforced 3D Navier--Stokes from one nonzero finite-energy datum, with strong L2 trace and global and local energy equalities.
- **Authors:** Thomas Y. Hou, Xiang Qin, Peicong Song, Wenhan Zhang
- **arXiv:** `2611.06117v1` (published 2026-11-04T08:01:00Z; categories: `math.AP`)
- **Evidence for ranking:** The abstract makes a precise, theorem-scale claim of nonuniqueness inside the suitable Leray--Hopf class, including equality in both energy balances; that is a potentially consequential result, but remains an author-claimed preprint result.
- **Claimed result:** The authors claim a continuum of pairwise distinct suitable Leray--Hopf solutions for one initial datum, with all stated energy equalities and simultaneous mixed-norm bounds on the strict supercritical side.
- **Assumptions and setting:** Unforced incompressible Navier--Stokes on R^3; the datum is axisymmetric, divergence-free, smooth away from the origin, in L2 and every Lq for 1≤q<3, but not in L3; solutions also lie in L∞_t L^{3,∞}_x.
- **Caveat:** The example uses data outside strong L3, so it does not contradict uniqueness results under stronger L3 or Prodi--Serrin hypotheses; the long analytic construction remains a preprint claim requiring expert scrutiny.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Analysis & PDE

### 2. [Off-Diagonal Induced Ramsey Numbers](https://arxiv.org/abs/2611.06886)
- **Abstract:** For graphs F and H, the authors prove a polynomial upper bound in v(H) for the induced Ramsey number when F is fixed, with an exponent bounded by an absolute constant times v(F)^2.
- **Authors:** Bruno Andrades, Marcelo Campos, Rafael Filipe, Anastasiia Kats
- **arXiv:** `2611.06886v1` (published 2026-11-04T18:40:56Z; categories: `math.CO`)
- **Evidence for ranking:** The paper claims a proof of the Kohayakawa--Prömel--Rödl conjecture; its introduction reports that a different proof was posted by Zhong, Kashima, and Mao on 21 October 2026, providing an independent-convergence signal.
- **Claimed result:** The authors prove r_ind(F,H) ≤ v(H)^{C v(F)^2} for all graphs F,H, for an absolute C, and also give a multicolour extension.
- **Assumptions and setting:** Finite simple graphs; the main theorem is uniform over F and H, with polynomial dependence on v(H) for each fixed F.
- **Caveat:** The exponent’s quadratic dependence on v(F) is not optimized; the authors explicitly ask whether it can be reduced to linear dependence.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Combinatorics & discrete mathematics

### 3. [Polylogarithmic bound for the Gyárfás-Sumner conjecture](https://arxiv.org/abs/2611.06699)
- **Abstract:** For every fixed tree T and clique bound k, the authors improve the known subpolynomial chromatic-number estimate for induced-T-free graphs to an explicit polylogarithmic bound.
- **Authors:** Martin Bierbaumer, Matija Bucić
- **arXiv:** `2611.06699v1` (published 2026-11-04T16:01:51Z; categories: `math.CO`)
- **Evidence for ranking:** The full paper gives χ(G) ≤ C_{T,k}(log |G|)^{14k}, sharpening a recent |G|^{o(1)} bound while retaining a direct link to the long-standing Gyárfás--Sumner conjecture.
- **Claimed result:** For every fixed tree T and positive integer k, the authors prove χ(G) ≤ C_{T,k}(log |G|)^{14k} whenever G is induced-T-free and has clique number at most k.
- **Assumptions and setting:** Finite graphs with |G|≥2; T and the clique-number bound k are fixed, and the constant C_{T,k} depends on both.
- **Caveat:** This is a polylogarithmic bound, not the conjectured bound independent of |G|; the authors state that removing the residual polylog factor remains open.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Combinatorics & discrete mathematics

### 4. [Gaussian free field limit for the Airy_β line ensemble](https://arxiv.org/abs/2611.05852)
- **Abstract:** The centered height function of the Airy_β line ensemble converges, after rescaling space and time, to the Gaussian free field in the half-plane for every β>0.
- **Authors:** Vadim Gorin, Lingfu Zhang
- **arXiv:** `2611.05852v1` (published 2026-11-04T02:43:23Z; categories: `math.PR` ; cross-lists: `math-ph`)
- **Evidence for ranking:** The paper bridges a random-matrix line ensemble and a two-dimensional random field, and is cross-listed in probability and mathematical physics; the stated result covers every β>0.
- **Claimed result:** The authors prove the rescaled centered height-function limit is the half-plane Gaussian free field, with spatial coordinate x↦√(-x) and β-dependence isolated by a √β field rescaling.
- **Assumptions and setting:** Airy_β line ensemble for β>0; the limit is in the specified half-plane scaling and conformal coordinate.
- **Caveat:** The result concerns this ensemble and scaling regime; the proof uses asymptotic expansions for Laplace-transform moments developed in earlier work with Xu.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Probability & statistics, Mathematical physics

### 5. [Representation embeddings and the third Brauer--Thrall conjecture](https://arxiv.org/abs/2611.06325)
- **Abstract:** For a representation-infinite finite-dimensional algebra over an algebraically closed field, the authors construct an indecomposable module of every infinite cardinal dimension, settling Simson’s third Brauer--Thrall conjecture in that setting.
- **Authors:** Haruhisa Enomoto
- **arXiv:** `2611.06325v1` (published 2026-11-04T10:57:46Z; categories: `math.RT` ; cross-lists: `math.RA`)
- **Evidence for ranking:** The abstract claims resolution of a named conjecture and the arXiv comment links a full Lean formalization of the main results; it is cross-listed in representation theory and rings/algebras.
- **Claimed result:** The author extends a representation embedding so that every infinite cardinal κ occurs as the dimension of an indecomposable module over the given algebra.
- **Assumptions and setting:** A finite-dimensional representation-infinite algebra A over an algebraically closed field k; the conclusion concerns infinite cardinal dimensions of indecomposable A-modules.
- **Caveat:** The theorem is stated over algebraically closed fields and for finite-dimensional representation-infinite algebras; it does not by itself cover other base-field or categorical settings.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Algebra & number theory, Logic & foundations

### 6. [Linear-length cycles in the supercritical percolated hypercube](https://arxiv.org/abs/2611.05634)
- **Abstract:** For edge-percolation on the d-dimensional hypercube with p=(1+ε)/d and sufficiently small fixed ε>0, the authors prove that the longest cycle has length Θ(ε²2^d) with high probability.
- **Authors:** Michael Anastos
- **arXiv:** `2611.05634v1` (published 2026-11-03T21:20:51Z; categories: `math.CO` ; cross-lists: `math.PR`)
- **Evidence for ranking:** The paper confirms a long-standing folklore prediction about cycles appearing with the giant component and identifies the optimal order in ε up to constants; it is cross-listed in combinatorics and probability.
- **Claimed result:** The author proves that near the threshold p=(1+ε)/d the longest cycle has length Θ(ε²2^d) with high probability, with the ε-dependence optimal up to constant factors.
- **Assumptions and setting:** Each edge of the binary d-cube is retained independently; ε is a sufficiently small positive constant and the probability statement is asymptotic in d.
- **Caveat:** The theorem is near the critical threshold for sufficiently small fixed ε; it gives order up to constants rather than an exact leading constant or full finite-d distribution.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Probability & statistics, Combinatorics & discrete mathematics

### 7. [Pointless K3 surfaces over finite fields](https://arxiv.org/abs/2611.06366)
- **Abstract:** The authors give an algorithm for ordinary K3 surfaces over finite fields, prove that no K3 surface is pointless for prime powers q≥13, and exhibit pointless examples for q≤11.
- **Authors:** Simon Brandhorst, Yuta Takada
- **arXiv:** `2611.06366v1` (published 2026-11-04T11:26:36Z; categories: `math.AG`)
- **Evidence for ranking:** The paper combines an enumerative algorithm with a geometric proof for elliptic K3 surfaces and supplies an explicit threshold/classification statement over finite fields.
- **Claimed result:** The authors claim nonexistence of K3 surfaces without F_q-rational points for every prime power q≥13 and explicit pointless K3 surfaces for every prime power q≤11.
- **Assumptions and setting:** K3 surfaces over finite fields F_q; the enumeration algorithm concerns ordinary K3 surfaces, and the abstract highlights a computer-free geometric proof for elliptic K3 surfaces.
- **Caveat:** The finite-field and K3 hypotheses are essential; the algorithmic enumeration applies to ordinary surfaces, while the abstract’s nonexistence claim is broader and uses an additional elliptic argument.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Algebra & number theory, Geometry & topology

### 8. [Floer theory on based loops and fundamental groups of Lagrangians in C^n](https://arxiv.org/abs/2611.06574)
- **Abstract:** Using Floer theory on the based loop space, the author derives topological constraints on Lagrangians in C^n and rules out embeddings of certain even-dimensional connected sums.
- **Authors:** Shuhao Li
- **arXiv:** `2611.06574v1` (published 2026-11-04T14:34:06Z; categories: `math.SG` ; cross-lists: `math.AT`, `math.GT`)
- **Evidence for ranking:** The result generalizes a theorem of Fukaya--Irie and is cross-listed across symplectic, algebraic, and geometric topology; the abstract gives a concrete embedding obstruction.
- **Claimed result:** The author proves that non-trivial connected sums of closed, spin, aspherical manifolds of even dimensions do not admit Lagrangian embeddings into C^n.
- **Assumptions and setting:** Lagrangian submanifolds of standard symplectic C^n; the excluded manifolds are closed, spin, aspherical, even-dimensional non-trivial connected sums.
- **Caveat:** The obstruction applies only to the stated spin, aspherical, even-dimensional connected-sum class; it is not a classification of all Lagrangian embeddings.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Geometry & topology

### 9. [Uniqueness of the hexagonal lattice's universal optimality](https://arxiv.org/abs/2611.06278)
- **Abstract:** Building on recent universal optimality of the planar hexagonal lattice, the authors prove it is the only periodic configuration with that property, up to Euclidean motion.
- **Authors:** Markus Faulhuber, Philipp Petersen
- **arXiv:** `2611.06278v1` (published 2026-11-04T10:20:41Z; categories: `math.MG`)
- **Evidence for ranking:** The paper strengthens an existing planar optimality theorem to a uniqueness/classification statement; the authors identify the periodic restriction as the meaningful uniqueness class.
- **Claimed result:** The authors claim that among periodic point configurations of density one, the hexagonal lattice is, up to Euclidean motion, the unique minimizer for every Gaussian energy, with a corresponding result for completely monotone potentials.
- **Assumptions and setting:** Periodic point configurations in R² of fixed density; energy comparisons concern all Gaussian potentials, with an extension to completely monotone potentials under finite-energy assumptions.
- **Caveat:** Uniqueness is restricted to periodic configurations: deleting finitely many points preserves density and Gaussian energy, so uniqueness cannot hold literally among arbitrary point configurations.
- **Announcement type:** new submission, 5 November 2026 batch
- **Themes:** Geometry & topology

## Trending Research Themes

- **Quantitative graph structure and induced patterns:** The Gyárfás--Sumner paper improves a near-polynomial chromatic bound to a polylogarithmic one, while the induced Ramsey paper proves polynomial dependence for fixed F; both use distinct structural arguments (block systems versus geometric random constructions and containers). The percolated-hypercube result adds a separate probabilistic cycle-length theorem, not a shared method. [2611.06699](https://arxiv.org/abs/2611.06699), [2611.06886](https://arxiv.org/abs/2611.06886), [2611.05634](https://arxiv.org/abs/2611.05634).
- **Probability and large-scale limits:** The Airy_β result identifies a Gaussian-free-field limit for a rescaled line ensemble, whereas hypercube percolation quantifies the longest cycle just above a threshold. These are two distinct instances of asymptotic structure, not evidence of a field-wide method shift. [2611.05852](https://arxiv.org/abs/2611.05852), [2611.05634](https://arxiv.org/abs/2611.05634).
- **Geometric classification and obstruction:** The K3 paper gives a finite-field rational-point threshold; the hexagonal-lattice paper upgrades energy optimality to uniqueness among periodic configurations; the Floer paper uses loop-space Floer theory to obstruct a specified class of Lagrangian embeddings. The settings and methods differ. [2611.06366](https://arxiv.org/abs/2611.06366), [2611.06278](https://arxiv.org/abs/2611.06278), [2611.06574](https://arxiv.org/abs/2611.06574).
- **Isolated PDE signal:** The Navier--Stokes preprint claims nonuniqueness in the suitable Leray--Hopf class for a carefully specified datum outside L³; one paper is not enough to infer a broader shift in PDE research. [2611.06117](https://arxiv.org/abs/2611.06117).

## Open Problems and Research Directions

- **Author-stated open problem — Gyárfás--Sumner:** Remove the remaining polylogarithmic factor to obtain the conjectured bounded chromatic number; the authors also identify removing the dependence of the exponent on clique bound k as an intermediate target. A concrete test is to seek a linear-size independent set or improve their `14k` exponent. [2611.06699](https://arxiv.org/abs/2611.06699).
- **Author-stated direction — induced Ramsey:** The authors ask whether the exponent’s quadratic dependence on v(F) can be reduced to linear. Compare their geometric/container proof with the alternative proof they cite, tracking which part controls the F-dependence. [2611.06886](https://arxiv.org/abs/2611.06886).
- **Synthesis — Navier--Stokes endpoint:** The construction separates weak-L³ from strong-L³ uniqueness regimes. A natural follow-up is to identify additional smallness, localization, or initial-trace conditions at the weak-L³ endpoint that restore uniqueness, while preserving the exact energy-class requirements. This is a proposed direction based on the paper’s stated function-space boundary, not an author claim. [2611.06117](https://arxiv.org/abs/2611.06117).
- **Synthesis — periodic versus general configurations:** Since finite point deletions prevent literal uniqueness for arbitrary configurations, investigate whether an energy-minimizer classification can be formulated modulo zero-density changes, or for broader nonperiodic classes with an explicit equivalence notion. [2611.06278](https://arxiv.org/abs/2611.06278).

## Takeaway

Today’s batch contains several concrete advances in graph bounds and a striking set of classification and limit theorems, but the ordering is a map of mathematically notable claims rather than measured readership. The Navier--Stokes nonuniqueness result is the highest-stakes claim here and should be treated as provisional until independent expert scrutiny.

## Method and sources

- **Window:** daily announcement batch dated 2026-11-05; start date 2026-11-05, end date 2026-11-05. The latest batch was used (not a prior batch). Snapshot: 2026-11-05 17:16:08 UTC.
- **Coverage:** arXiv Mathematics archive (`math`); traversed all 364 entries in the 2026-11-05 announcement batch, retained nine new submissions, and verified their abstract pages. Categories are preserved as arXiv subject classes.
- **Inference:** no official arXiv trending ranking exists. Selection/ordering emphasizes concrete theorem-level claims, sharper bounds or classifications, cross-listing, proof artifacts, and the paper authors’ report of an independent proof where available; recency is only a tie-breaker. Citation totals were not used.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); each linked arXiv abstract page above; arXiv HTML full text for the three leading graph/PDE papers. The configured `web_extract` backend could not extract pages, so the listing and abstracts were checked directly in the browser. Semantic Scholar Graph citation data could not be retrieved in this snapshot; citation and influential-citation evidence are therefore unavailable.
