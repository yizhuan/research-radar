# arXiv Mathematics — latest announcement batch (12 October 2026)

Seven notable papers selected from the 388 entries in the latest math announcement batch. The strongest shared pattern is rigorous resolution or formalization of long-standing mathematical questions, alongside major advances in scaling limits and arithmetic geometry. Brief agenda: a two-dimensional sandpile finiteness theorem, a rigorous Ising-to-CFT correspondence, and five notable results across geometry, topology, PDE, and spectral theory. arXiv has no official trending chart; this is an inferred significance-oriented ordering, not a popularity list. All seven are very recent: Semantic Scholar currently reports zero citations and zero influential citations for each, so citation momentum cannot distinguish them.

## Top papers (ranked)

### 1. [Sandpile avalanches in two dimensions are finite](https://arxiv.org/abs/2610.13940)
- **Abstract:** For the stationary abelian sandpile on the square lattice, avalanches are almost surely finite, with the probability of reaching distance R bounded by a negative power of log R.
- **Authors:** Ahmed Bou-Rabee
- **arXiv:** `2610.13940v1` (published 2026-10-09T17:57:56Z; categories: `math.PR`)
- **Evidence for ranking:** The full 12 October batch lists this as a new probability submission; its abstract and Theorem 1.1 resolve a repeatedly posed question for the two-dimensional model and give an explicit logarithmic-power tail bound. The proof links avalanche events to uniform spanning trees.
- **Claimed result:** The author proves that adding a grain at the origin to the stationary sandpile on Z² almost surely stabilizes; the radius tail is at most C(log(R+2))^-a for constants C<∞ and a>0 (arXiv abstract and Theorem 1.1).
- **Assumptions and setting:** The infinite-volume stationary state is the local limit of uniform recurrent sandpiles in wired finite boxes; the result concerns a single grain added at the origin.
- **Caveat:** The quantitative tail is only a negative power of log distance; the paper does not claim a sharp tail or finite expected avalanche radius.
- **Announcement type:** new submission, announcement-batch date 2026-10-12
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics

### 2. [Critical Ising model as the M(4,3) minimal model of conformal field theory](https://arxiv.org/abs/2610.13705)
- **Abstract:** The authors construct a correspondence from local spin polynomials in critical Ising to states of the M(4,3) minimal model and prove nontrivial scaling limits for all non-null fields on isoradial graphs.
- **Authors:** Dmitry Chelkak, Konstantin Izyurov, Kalle Kytölä
- **arXiv:** `2610.13705v1` (published 2026-10-09T15:00:04Z; categories: `math-ph`, `math.PR`)
- **Evidence for ranking:** The abstract and introduction claim a rigorous classification of all local spin-polynomial fields, not only selected primary observables; the paper bridges discrete complex analysis, probability, and conformal field theory across two arXiv categories.
- **Claimed result:** A surjective map sends each lattice spin polynomial to an M(4,3) state, with kernel exactly the null fields. For every non-null local field, suitable mesh rescaling yields a nontrivial scaling limit in correlations, expressed through minimal-model primary correlations and Virasoro action (arXiv abstract and introduction).
- **Assumptions and setting:** Critical Ising on isoradial graphs; the lattice mesh tends to zero, and observables are local polynomials in spins inserted in correlations.
- **Caveat:** The result concerns local spin-polynomial observables and the stated scaling-limit regime; it does not by itself classify every nonlocal observable or every boundary setup.
- **Announcement type:** new submission, announcement-batch date 2026-10-12
- **Themes:** Mathematical physics; Probability & statistics

### 3. [The Tate Conjecture for Ordinary Calabi-Yau Threefolds](https://arxiv.org/abs/2610.13939)
- **Abstract:** Using canonical lifts, the author proves the integral geometric Tate conjecture for ordinary Calabi-Yau threefolds over finite fields and proves it for divisor classes in certain ordinary Calabi-Yau varieties.
- **Authors:** Lukas Brantner
- **arXiv:** `2610.13939v1` (published 2026-10-09T17:57:50Z; categories: `math.AG`, `math.NT`)
- **Evidence for ranking:** The paper states a concrete cycle-class-surjectivity theorem in both algebraic geometry and number theory; the full paper identifies canonical lifts as the mechanism transferring characteristic-zero results to positive characteristic.
- **Claimed result:** Theorem A proves the integral geometric Tate conjecture for a Calabi-Yau threefold over a finite field if it is ordinary, or if it is strict and 1-ordinary. Theorem B treats divisor classes for 2-ordinary Calabi-Yau varieties with H²(X,O_X)=0 (paper, Theorems A and B).
- **Assumptions and setting:** Smooth, projective, geometrically irreducible Calabi-Yau varieties over finite fields, under the stated ordinarity/strictness and cohomology hypotheses.
- **Caveat:** This is not a proof of the Tate conjecture for arbitrary Calabi-Yau varieties: the threefold theorem has ordinarity conditions, while the broader-dimensional statement is limited to divisor classes.
- **Announcement type:** new submission, announcement-batch date 2026-10-12
- **Themes:** Algebra & number theory

### 4. [A Lean Formalization of the Hamilton--Perelman Proof of Thurston's Geometrization Conjecture](https://arxiv.org/abs/2610.13897)
- **Abstract:** The authors formalize the Hamilton--Perelman Ricci-flow proof of Thurston's geometrization conjecture and reproduce the public Lean theorem declaration.
- **Authors:** Yuan Liao, Ziyang Qin, Jui-Hui Chung, Ayush Khaitan, Zhengyang Zhang, Hongzhou Lin, Zijian Zhang, Ligeng Zhu, Peng Lu, Bennett Chow
- **arXiv:** `2610.13897v1` (published 2026-10-09T17:43:01Z; categories: `math.DG`)
- **Evidence for ranking:** This is a substantial proof-assistant artifact for a central three-manifold theorem; the paper exposes the endpoint declaration and explains its geometric interpretation and verification. Its inclusion reflects the formalization milestone, not a citation trend.
- **Claimed result:** The public Lean endpoint formalizes a prime connected-sum decomposition and, for each factor, torus cuts whose resulting interiors carry complete metrics locally modeled on Thurston geometries, with finite volume in the hyperbolic case (paper, Theorem 1 and Lean declaration).
- **Assumptions and setting:** Connected, closed, oriented smooth three-manifolds; the theorem returns prime factors and possibly noncanonical torus decompositions.
- **Caveat:** The formalized statement explicitly makes no uniqueness or canonical-JSJ-family claim for the cutting tori; the theorem's scope is the precise encoded declaration and its verified Lean dependencies.
- **Announcement type:** new submission, announcement-batch date 2026-10-12
- **Themes:** Geometry & topology; Logic & foundations

### 5. [A counterexample to Nirenberg's conjecture on closed asymptotic curves](https://arxiv.org/abs/2610.13848)
- **Abstract:** The authors construct a smooth negatively curved embedded annulus with convex boundary in tangent planes and two closed asymptotic curves, contradicting Nirenberg's 1962 conjecture.
- **Authors:** Harrison Banks, Mohammad Ghomi, Hongda Qiu, Matteo Raffaelli
- **arXiv:** `2610.13848v1` (published 2026-10-09T16:55:33Z; categories: `math.DG`)
- **Evidence for ranking:** The paper gives a concrete counterexample to a named conjecture in differential geometry; the introduction states the full geometric properties and relates the result to rigidity of negatively curved surfaces.
- **Claimed result:** There exists a smooth embedded annulus in R³ with negative interior Gauss curvature, two distinct closed asymptotic curves, and strictly convex boundary components in parallel tangent planes (paper, Theorem 1.1).
- **Assumptions and setting:** A smooth embedded annulus in Euclidean three-space with the specified curvature and boundary geometry.
- **Caveat:** The construction disproves the stated conjecture but does not settle all rigidity questions for negatively curved surfaces; the authors report checking computations in a Mathematica notebook, rather than a machine-checked formal proof.
- **Announcement type:** new submission, announcement-batch date 2026-10-12
- **Themes:** Geometry & topology

### 6. [Topping's conjecture for solutions of harmonic map flow with isolated bubbles](https://arxiv.org/abs/2610.13746)
- **Abstract:** The authors prove Topping's conjecture on continuity of the body map for harmonic-map-flow solutions at finite-time singularities where only isolated bubbles form.
- **Authors:** Melanie Rupflin, Alex Waldron, Sebastian Woodward
- **arXiv:** `2610.13746v1` (published 2026-10-09T15:37:15Z; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** The abstract states a conjecture resolution, and the result is cross-listed between geometric analysis and PDE; the proof's weighted Łojasiewicz–Simon inequality is a concrete analytic mechanism.
- **Claimed result:** A weighted Łojasiewicz–Simon inequality near a fixed harmonic map modulo scaling yields the claimed continuity of the body map in the isolated-bubble finite-time-singularity case (arXiv abstract).
- **Assumptions and setting:** Solutions of harmonic map flow with finite-time singularities at which only isolated bubbles form.
- **Caveat:** The stated theorem is limited to isolated-bubble singularities; the abstract does not claim the result for general bubbling configurations.
- **Announcement type:** new submission, announcement-batch date 2026-10-12
- **Themes:** Geometry & topology; Analysis & PDE

### 7. [Sharp upper bounds for Steklov eigenvalues on warped products](https://arxiv.org/abs/2610.13738)
- **Abstract:** The authors establish sharp isoperimetric-type upper bounds for Steklov eigenvalues on warped products, including one-dimensional fibres, using comparison and spectral approximation methods.
- **Authors:** Jade Brisson, Bruno Colbois, Alexandre Girouard, Katie Gittins, Jean Lagacé-Taylor
- **arXiv:** `2610.13738v1` (published 2026-10-09T15:33:03Z; categories: `math.SP`, `math.AP`, `math.DG`)
- **Evidence for ranking:** The arXiv abstract explicitly says this supersedes the authors' earlier arXiv:2512.15416 bounds and extends the setting to fibres of any dimension, obtaining sharp bounds; its three mathematical cross-lists connect spectral theory, PDE, and geometry.
- **Claimed result:** The authors prove sharp isoperimetric-type upper bounds involving the warped-product and boundary volumes, fibre Laplace eigenvalues, and base Steklov eigenvalues; comparison uses weighted Helmholtz–Steklov problems and spectral approximation (arXiv abstract).
- **Assumptions and setting:** Warped products with compact Riemannian bases with boundary and closed Riemannian fibres; additional natural warping constraints are studied separately.
- **Caveat:** The estimates depend on geometric and spectral data of both base and fibre; the abstract does not imply a universal bound independent of those inputs.
- **Announcement type:** new submission, announcement-batch date 2026-10-12
- **Themes:** Analysis & PDE; Geometry & topology

## Trending Research Themes

- **Long-standing questions meet quantitative bounds.** The sandpile paper resolves almost-sure finiteness in the recurrent two-dimensional model but leaves a slow logarithmic tail (Bou-Rabee); the Tate paper proves integral cycle-class surjectivity under ordinarity hypotheses rather than in full generality (Brantner).
- **Rigorous bridges between representations.** The Ising paper turns the physics identification with the M(4,3) conformal field theory into a field-by-field scaling-limit theorem for local spin polynomials; its technical bridge uses lattice fermions, Fock spaces, and discrete complex analysis (Chelkak, Izyurov, Kytölä).
- **Formal and geometric structure.** The Lean work packages the Ricci-flow route to geometrization into a checked declaration, while the Nirenberg paper uses an explicit ruled-annulus construction to show that a proposed rigidity condition fails (Liao et al.; Banks et al.). These are distinct methods, not a common proof technique.
- **Analysis shaped by geometry.** The harmonic-map-flow result uses a weighted Łojasiewicz–Simon inequality under isolated bubbling, while the Steklov paper uses warped-product structure and spectral comparison to get sharp bounds (Rupflin et al.; Brisson et al.).

## Open Problems and Research Directions

- **Research direction (informed by the theorem's hypotheses):** Test whether the canonical-lift strategy for the Tate conjecture can cover nonordinary Calabi-Yau threefolds or higher-codimension cycles; the current results establish only the stated ordinary/1-ordinary cases and broader-dimensional divisor case (Brantner, [arXiv:2610.13939](https://arxiv.org/abs/2610.13939)).
- **Research direction (quantitative follow-up):** Determine whether the logarithmic-power tail for two-dimensional sandpile avalanches can be sharpened, or whether matching lower bounds hold; the paper proves an upper bound but does not identify a sharp exponent or tail asymptotic (Bou-Rabee, [arXiv:2610.13940](https://arxiv.org/abs/2610.13940)).
- **Research direction (scope extension):** Investigate which broader bubbling patterns permit continuity of the harmonic-map-flow body map beyond isolated bubbles; the current result is explicitly restricted to the isolated-bubble finite-time case (Rupflin et al., [arXiv:2610.13746](https://arxiv.org/abs/2610.13746)).
- **Research direction (scope extension):** Explore whether the Ising local-field correspondence can be extended to boundary or nonlocal observables with similarly explicit convergence statements (Chelkak et al., [arXiv:2610.13705](https://arxiv.org/abs/2610.13705)).

## Takeaway

The strongest mathematical signal in this batch is not a measured surge in attention but several unusually concrete theorem-level claims: a resolution of the 2D sandpile finiteness question, a rigorous all-local-field scaling correspondence for critical Ising, and a conditional integral Tate theorem. The geometrization formalization and geometric counterexample are striking but remain preprints; their exact statements and hypotheses matter as much as their headline claims.

## Method and sources

Daily window: the latest arXiv Mathematics announcement batch, Monday 12 October 2026; the papers' v1 submission timestamps are on Friday 9 October 2026. Snapshot: 2026-10-13 00:14:05 UTC. I traversed the complete `math/recent` listing for that batch (388 entries), then checked arXiv abstract pages for all seven selected papers and inspected the HTML full texts/introduction or main results for the sandpile, Ising, Tate, Lean, and Nirenberg papers. The ordering is inferred from explicit theorem/conjecture-resolution claims, stated quantitative improvements, and cross-subfield relevance; it is not a measure of downloads or readership. A Semantic Scholar Graph API batch lookup returned zero current citations and zero influential citations for each selected paper; such counts are especially uninformative this soon after announcement. Sources: [arXiv math recent](https://arxiv.org/list/math/recent?show=500); linked abstract/full-text pages above; Semantic Scholar Graph API, queried 2026-10-13 UTC.
