Window (UTC): 2026-08-29 00:00:00 to 2026-09-04 23:59:59
Snapshot time (UTC): 2026-09-04 01:20:21
Archive coverage: arXiv “math” recent listings (taken from arxiv.org/list/math/recent; selected the first 40 entries on that listing and then ranked within this pool).

Important note on “hottest”: arXiv does not provide an official “trending” chart and Semantic Scholar momentum signals were unavailable from this environment (HTTP 429 “Too Many Requests”). The ordering below is therefore inferred using metadata proxies:
- whether the preprint was revised after initial submission within the window,
- comments length / presence of more detailed metadata,
- cross-listed arXiv subject coverage within the math archive.

1) Headline
This week’s most notable math preprints cluster around (i) sharper complexity lower bounds for gradient descent under flexible step schedules, (ii) rigidity/comparison results in metric-measure geometry and Laplace eigenvalues, and (iii) “positivity/structure” theorems connecting algebraic geometry, combinatorics, and operator-algebraic approximation properties.

2) Top papers (ranked by inferred metadata “momentum” within the selected pool)

1. Improved Gradient Descent Lower Bounds Beyond Nesterov
   - Authors: Yuhan Ye, Kaizhao Liu
   - arXiv:2609.02855 (v1), submitted 2026-09-02, revised 2026-09-03
   - Categories: Optimization and Control (math.OC); Machine Learning (cs.LG); Machine Learning (stat.ML)
   - What they prove (per abstract): For smooth convex optimization, they study how well gradient descent (GD) can be accelerated by predetermined stepsizes. They prove improved non-anytime and anytime lower bounds: Ω(n^-1.6342) in the non-anytime setting and Ω(n^-1.2408) in the anytime setting, improving earlier Ω(n^-1.932) / Ω(n^-4/3) results. They also allow stepsizes to be negative, and the anytime bound shows an unattainability statement for the “non-anytime silver schedules” rate in the anytime setting.
   - Caveat: The abstract describes the lower bounds precisely; details of the oracle model and stepsize schedule class are part of the paper’s setup.
   - Link: https://arxiv.org/abs/2609.02855

2. Canonical-row Chern flow on Bott--Samelson towers: realizable-volume models for Schubert, Grothendieck, and Lascoux polynomials
   - Authors: Khai-Hoan Nguyen-Dang, Zhenpeng Wang
   - arXiv:2609.02850 (v1), submitted 2026-09-02, revised 2026-09-03
   - Categories: Combinatorics (math.CO)
   - What they prove (per abstract): Over an arbitrary field they construct realizable-volume models for factorially normalized homogeneous Lascoux, Lascoux-atom, and positive Grothendieck packets. Over ℂ the polynomials are Lorentzian. Consequently, they identify the supports of Grothendieck/Lascoux/Lascoux-atom polynomials with lattice points of integral generalized-polymatroid Newton polytopes (in a realizable-volume form), thereby proving conjectures of Huh–Matherne–Mészáros–St. Dizier and related saturated-Newton-polytope / Grothendieck-support conjectures of other authors.
   - Caveat: This is “over an arbitrary field” / “over ℂ” in the abstract; the exact strength depends on the packet normalization and the positivity conventions defined in the paper.
   - Link: https://arxiv.org/abs/2609.02850

3. Petersson-Rigid Lattices in a Census of 100 Rank-Three Root Bases
   - Author: Eungang Cho
   - arXiv:2609.02843, submitted 2026-09-02, revised 2026-09-02
   - Categories: Number Theory (math.NT); Representation Theory (math.RT)
   - What they prove (per abstract): After enumerating rank-three hyperbolic Cartan matrices / edits / root bases and computing the obstruction space S_{5/2}(ρ_L), they identify which lattices in the census are “Petersson-rigid” under a condition that pins down the Petersson pairing up to a scalar. They reduce the “absolutely irreducible action” condition to a small number of cases and conclude that there are three rigid lattices (with special faces “coming off”), generalizing earlier single-point invariants. The abstract emphasizes rigidity observations and the numerical checking setup.
   - Caveat: Rigidity and the exact condition are internal to the paper’s definitions and computations; the abstract does not include the full criterion.
   - Link: https://arxiv.org/abs/2609.02843

4. A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line
   - Author: Youness Lamzouri
   - arXiv:2609.02882, submitted 2026-09-02, revised 2026-09-02
   - Categories: Number Theory (math.NT); Complex Variables (math.CV)
   - What they prove (per abstract): They give an unconditional proof that over 67.25% of non-trivial ζ(s) zeros are simple and on the critical line, and that at least 83.62% are distinct. The abstract describes replacing a finite-dimensional matrix framework by a Hilbert space inequality, enabling a direct application of Montgomery’s theorem on the (unconditional) pair correlation of zeta zeros.
   - Caveat: The quantitative percentages are as stated in the abstract; the technical transparency depends on the Hilbert space inequality and the explicit formula details.
   - Link: https://arxiv.org/abs/2609.02882

5. Estimating the number of real zeros of linear combinations of radicals of polynomials
   - Authors: Gal Binyamini, Avner Kiro, Alexander Logunov, Dmitry Novikov, Dmitrii Zakharov
   - arXiv:2609.02871, submitted 2026-09-02, revised 2026-09-02
   - Categories: Classical Analysis and ODEs (math.CA); Algebraic Geometry (math.AG); Analysis of PDEs (math.AP)
   - What they prove (per abstract): They bound the number of real zeros of functions of the form Σ c_k (P_k(x))^{α_k} where P_k are real polynomials non-negative on an interval I. They improve bounds from exponential-in-previous-work to bounds that are polynomial in n, linear in degree d, and independent of exponents α_k. They prove a linear bound (2n) for linear combinations of square roots of positive quadratic polynomials, answering a question of N. Alon, and also address a related question tied to Maxwell’s conjecture / nodal domain counts via a PDE perspective.
   - Caveat: The dependence on the interval positivity and on the structure “positive quadratic” is explicit in the abstract.
   - Link: https://arxiv.org/abs/2609.02871

6. Continuous data assimilation in steady Navier-Stokes equations with unknown viscosity: robust and efficient solvers and fast parameter recovery
   - Authors: L. Rebholz, J. Reyes, J. Whitehead
   - arXiv:2609.02862, submitted 2026-09-02, revised 2026-09-02
   - Categories: Numerical Analysis (math.NA); Analysis of PDEs (math.AP)
   - What they prove (per abstract): They recover an unknown viscosity parameter in steady Navier–Stokes from partial incompressible flow observations using continuous data assimilation (CDA). They propose an efficient parameter-recovery algorithm and nonlinear solver (CDA-Picard + CDA-Newton), and provide analysis giving well-posedness plus quadratic convergence claims; experiments show fast parameter restoration from poor initial guesses.
   - Caveat: The abstract focuses on “steady” NSE and on the observation model; applicability to other regimes depends on the paper’s assumptions.
   - Link: https://arxiv.org/abs/2609.02862

7. Localized Persistent Commutative Algebra
   - Authors: Kaiyue He, Faisal Suwayyid, Guo-Wei Wei
   - arXiv:2609.02858, submitted 2026-09-02, revised 2026-09-02
   - Categories: Commutative Algebra (math.AC); Combinatorics (math.CO)
   - What they prove (per abstract): They build a localized persistent commutative algebra theory for Stanley–Reisner rings using local cohomology supported at a coordinate prime (not at the maximal ideal). They prove graded decompositions of H^q_{p_i}(k[Δ]) in terms of maximal-support local cohomology of deletion/link pieces, recover a vertex-prime case of Rahimi’s formula, and then develop per-vertex persistent numbers, interval decompositions, a bottleneck stability theorem, and show that multiplication by the uninverted variable is not determined by barcodes alone. They also extend to arbitrary coordinate primes.
   - Caveat: Persistence module formalism is central; the abstract’s exact persistence-module construction details are not repeated here.
   - Link: https://arxiv.org/abs/2609.02858

8. Finite extensions of abelian schemes and duality for commutative group stacks
   - Authors: Ajneet Dhillon, Brett Nasserden
   - arXiv:2609.02826, submitted 2026-09-02, revised 2026-09-02
   - Categories: Algebraic Geometry (math.AG); Number Theory (math.NT)
   - What they prove (per abstract): For a DVR R, they prove structure theorems for proper flat finitely presented commutative R-group schemes: such a group scheme P admits an exact sequence with a finite flat part E and an abelian scheme part B; for “quasiabelian” models they show normalization is abelian and the model is constructed via pushouts involving finite flat group schemes. They develop duality/duality-category results, including biduality and (when 2 is invertible) proof of Brochard’s duality conjecture in the group-stacks context. They also give derived-category equivalences via a kernel-algebra Fourier–Mukai argument.
   - Caveat: Some results depend on “2 invertible” and on “quasiabelian” hypotheses.
   - Link: https://arxiv.org/abs/2609.02826

9. Actions of quantum groups on dual operator spaces and their crossed products
   - Authors: Jason Crann, Joeri De Ro, Jacek Krajczok
   - arXiv:2609.02822, submitted 2026-09-02, revised 2026-09-02
   - Categories: Operator Algebras (math.OA); Functional Analysis (math.FA)
   - What they prove (per abstract): They study dual operator spaces with actions of locally compact quantum groups G. They show equality of the Fubini crossed product and weak* crossed product functors holds iff G has the approximation property of Haagerup and Kraus. The abstract also characterizes the approximation property via an L^1(G)-module approximation property for B(L^2(G))_* and investigates exactness of the Fubini crossed product functor in relation to amenability properties.
   - Caveat: The operator-algebraic functor definitions and “approximation property” characterization require the paper’s technical setup.
   - Link: https://arxiv.org/abs/2609.02822

10. Minimizers of Laplace eigenvalues under a lower curvature bound
   - Author: Aditya Tiwari
   - arXiv:2609.02808, submitted 2026-09-02, revised 2026-09-02
   - Categories: Differential Geometry (math.DG); Spectral Theory (math.SP)
   - What they prove (per abstract): Under a lower curvature bound in the sense of one-dimensional CD(1,2) spaces plus a convexity condition on the density, they obtain a sharp comparison of Neumann Laplace eigenvalues against the Legendre model, with Obata-type rigidity. They derive non-collapsing for minimizers of the k-th Laplace eigenvalue among closed surfaces of Gaussian curvature at least 1 (for k ≥ 2) in the measured Gromov–Hausdorff completion, and they give a variational proof that smooth minimizers are round.
   - Caveat: The abstract’s “1-dimensional CD(1,2)” and “convexity condition on the density” are essential.
   - Link: https://arxiv.org/abs/2609.02808

3) Trending mathematical themes (evidence-tied)
- Optimization lower bounds for first-order methods: new lower bounds that separate anytime vs non-anytime settings for gradient descent (2609.02855).
- Metric-measure rigidity via eigenvalue comparison: sharp Neumann eigenvalue comparison, non-collapsing, and Obata-type rigidity (2609.02808).
- “Recovery from data” in PDE parameter inference: continuous data assimilation for unknown viscosity in steady Navier–Stokes with well-posedness and quadratic convergence (2609.02862).
- Structural positivity/realizability in algebraic combinatorics: realizable-volume models leading to Lorentzian/convex-geometric support statements and proof of multiple conjectures (2609.02850).
- Quantitative progress on the distribution of zeta zeros: improved simple-zero and distinct-zero proportions via an alternative conceptual mechanism (2609.02882).
- Algebraic duality and representation-theoretic rigidity: census-based identification of rigid lattices (2609.02843) and group-stack duality with Fourier–Mukai-type derived equivalences (2609.02826).
- Persistent invariants localized at coordinate primes: per-vertex persistent cohomology, stability, and the fact that barcodes don’t determine multiplication by uninverted variables (2609.02858).
- Operator-algebraic functoriality tied to approximation properties: equivalence of crossed-product functors and characterization of Haagerup–Kraus approximation (2609.02822).

4) Research opportunities (informed, not claiming “open problems”)
- Optimization complexity: build on the anytime/non-anytime separation (2609.02855) to ask which step-schedule classes maintain provable separations for other algorithmic families (e.g., accelerated schemes or nonconvex relaxations).
- Combinatorics–geometry bridges: extend realizable-volume / Lorentzian support technology beyond Bott–Samelson towers or beyond the specific packet families and normalizations studied in (2609.02850).
- Quantitative zeta-zero questions: the new Hilbert-space mechanism (2609.02882) suggests retooling arguments around pair correlation; a concrete opportunity is to see how far the framework can push simple-zero proportions or adapt to related L-functions.
- Algebraic geometry and duality: the group-stack duality and biduality package (2609.02826) points to testing how “2 invertible” enters and whether analogous statements hold under other residue-characteristic conditions.
- Persistence modules: since barcodes don’t determine multiplication by the uninverted variable (2609.02858), a natural direction is to identify minimal additional invariants/data needed for full functorial reconstruction.
- PDE inverse problems: the CDA-NSE solver package (2609.02862) invites extension toward noise-robust inference models, other observation regimes, or time-dependent settings.
- Quantum groups and crossed products: once functor equality characterizes Haagerup–Kraus approximation (2609.02822), one can test whether related crossed-product variants isolate other approximation/amenability properties.
- Eigenvalue rigidity in curvature bounds: the sharp CD(1,2) / Legendre-model comparison (2609.02808) suggests exploring similar sharp comparisons in broader curvature-dimension regimes or higher-dimensional analogues.

5) Takeaway
Even without official “trending” statistics, this week’s cluster suggests simultaneous momentum in (a) sharper quantitative theory (lower bounds, zeta zero proportions), (b) rigidity/comparison phenomena under geometric constraints, and (c) deep structural frameworks tying together algebraic geometry, combinatorics, persistence, and operator-algebraic approximation.

6) Method and sources
- Window definition: last 7 calendar days in UTC (start/end as listed at top).
- Candidate pool: first 40 entries on arXiv math recent listing (arxiv.org/list/math/recent) that fall within the window by their arXiv “Submitted on” date.
- Ranking: inferred from metadata proxies (revision timing, subject cross-coverage, comments/presentation metadata). Semantic Scholar momentum signals were not accessible (repeated HTTP 429) from this environment, so citation-based “hottest” ordering is not used.
- Primary sources for statements: arXiv abstract pages for the selected papers (IDs listed above).