# arXiv Mathematics: daily notable papers — announcement batch 10 November 2026

The batch contains 792 mathematics entries; this report selects 10 for a closer look. The dominant pattern is authors claiming to close conjectures or complete classifications, often with sharp hypotheses or checkable proof components. I’ll move from complex analysis and graph theory to arithmetic, PDE, algebra, and geometry. Caveat: arXiv supplies no official trending chart, so this is an inferred ranking, and citation evidence is limited for a just-announced batch.

## Top papers (ranked)

### 1. [A proof of the Erdős-Herzog-Piranian lemniscate conjecture](https://arxiv.org/abs/2611.12830)
- **Abstract:** For every monic complex polynomial of degree at least one, the paper claims the unit lemniscate has maximal length for a translate and rotation of `z^n − 1`, with exactly those equality cases.
- **Authors:** Teng Zhang
- **arXiv:** `2611.12830v1` (published 2026-11-09 18:29:49 UTC; categories: `math.CV`)
- **Evidence for ranking:** The claim resolves a conjecture posed in 1958 for every degree and specifies all maximizers; the introduction places the result after prior work covering sufficiently large degrees and the cases n=2,3. Its stated combination of analytic estimates and certified finite-degree calculations is a concrete significance signal, not a readership measure.
- **Claimed result:** The author proves that for any monic degree-n polynomial p, the length of `{z: |p(z)|=1}` is at most the length for `z^n−1`; equality holds exactly for `p(z)=(z−z₀)^n−e^{iθ}` (arXiv abstract and Theorem 1.3).
- **Assumptions and setting:** A monic polynomial over the complex numbers, degree n≥1, with the unit-level lemniscate measured by arclength.
- **Caveat:** The proof uses rigorous computer-assisted estimates in a finite range of degrees; the paper is a preprint, and this summary has not checked those certificates or the full proof.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Analysis & PDE

### 2. [Average distance and maximum induced linear forest](https://arxiv.org/abs/2611.12781)
- **Abstract:** For every connected graph, the authors claim the average pairwise distance is at most half the maximum order of an induced subgraph whose components are paths.
- **Authors:** Mathieu Bouchard, Alain Hertz
- **arXiv:** `2611.12781v1` (published 2026-11-09 17:54:36 UTC; categories: `math.CO`)
- **Evidence for ranking:** The paper explicitly identifies its result as proving a conjecture dating to 2009, strengthening previously stated bounds using induced forests and the independence number; the full-scope theorem is stated for all connected graphs.
- **Claimed result:** The authors prove `μ(G) ≤ L(G)/2`, equivalently `4W(G) ≤ L(G)n(n−1)`, where μ is average distance, W is the Wiener index, and L is the largest induced linear-forest order (arXiv abstract and Conjecture 1.1).
- **Assumptions and setting:** Finite connected graph G of order n; a linear forest is an induced subgraph all of whose connected components are chains (paths).
- **Caveat:** The theorem is an attributed preprint claim; the abstract gives the universal bound but does not state a separate classification of equality cases.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Combinatorics & discrete mathematics

### 3. [A complete symmetric rank-two modularity classification, obtained through a sharp uniform degree bound](https://arxiv.org/abs/2611.12868)
- **Abstract:** The author classifies modular rank-two Nahm sums for rational symmetric positive-definite matrices and rational shifts, finding rational-point families, split products, and 34 exceptional triples, with no further cases under those hypotheses.
- **Authors:** Cetin Hakimoglu-Brown
- **arXiv:** `2611.12868v1` (published 2026-11-09 18:53:47 UTC; categories: `math.NT`)
- **Evidence for ranking:** The introduction frames exhaustiveness in the symmetric rank-two problem as a longstanding gap; the result gives an explicit complete list, a sharp degree-four bound, exact certificates, independently implemented checks, and a computational companion archived at DOI `10.5281/zenodo.24062300`.
- **Claimed result:** The author states an if-and-only-if classification: up to exchanging coordinates, every modular datum is in one of three rational-point families, a product of two modular rank-one sums, or the list of 34 exceptional triples on 12 matrices (arXiv abstract and Theorem 1.1).
- **Assumptions and setting:** Nahm sums with a rational symmetric positive-definite 2×2 matrix, rational vector shifts, and rational scalar shift; modularity means a modular function for a finite-index subgroup of SL₂(Z), meromorphic at cusps, allowing a finite-order multiplier.
- **Caveat:** The classification does not cover higher rank, nonsymmetric matrices, or irrational input data; its exhaustive finite arithmetic steps and companion certificates merit independent checking.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Algebra & number theory

### 4. [Quantitative global regularity for Navier--Stokes equations with odd viscosity on the cubic three-torus](https://arxiv.org/abs/2611.12862)
- **Abstract:** For three-dimensional incompressible Navier–Stokes on the cubic torus, the authors claim global strong solutions for arbitrary mean-zero divergence-free H² data and steady H² forcing once one odd-viscosity coefficient exceeds a sufficient data-dependent threshold, and also give bounded-data regions with regularity at every coefficient.
- **Authors:** Jinzheng Li, Yuqi Li, Hao-Yu Sun
- **arXiv:** `2611.12862v1` (published 2026-11-09 18:50:49 UTC; categories: `math.AP`, `math-ph`, `physics.flu-dyn`)
- **Evidence for ranking:** The result is cross-listed across PDE and mathematical physics, states quantitative conditions rather than only qualitative regularity, and reports formal verification of its three main theorems in Lean 4 with Mathlib.
- **Claimed result:** The authors claim unique global strong solutions when the magnitude of one fixed odd-viscosity coefficient exceeds a sufficient threshold; in the unforced case the solution is smooth at positive times. They also claim explicit bounded data/force regions giving regularity for every coefficient (arXiv abstract).
- **Assumptions and setting:** Three-dimensional incompressible flow on the cubic three-torus, with the specified constant odd-viscosity operator; real mean-zero divergence-free initial data and independent steady force in second-order Sobolev space for the threshold theorem.
- **Caveat:** This is a modified system with a sufficient, not claimed optimal, threshold; the authors explicitly leave the sharp threshold for the original equation open, so it is not a resolution of regularity for standard 3D Navier–Stokes.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Analysis & PDE; Mathematical physics

### 5. [Classification of quasi-lisse simple affine vertex algebras](https://arxiv.org/abs/2611.12723)
- **Abstract:** The authors classify all noncritical levels giving quasi-lisse simple affine vertex algebras for every finite-dimensional complex simple Lie algebra and determine associated varieties for ranks at most six and for E₇ and E₈.
- **Authors:** Drazen Adamovic, Xuanzhong Dai, Kaiwen Sun
- **arXiv:** `2611.12723v1` (published 2026-11-09 17:07:48 UTC; categories: `math.RT`, `math-ph`, `math.QA`)
- **Evidence for ranking:** A broad classification is cross-listed in representation theory, mathematical physics, and quantum algebra; the abstract gives a precise level-reduction criterion and explicitly names the exceptional associated-variety coverage.
- **Claimed result:** The authors classify the noncritical quasi-lisse levels for every finite-dimensional complex simple Lie algebra and establish the stated equivalence between levels involving q and q/gcd(q,r), with r the lacing number; they also determine associated varieties in the specified Lie-type range (arXiv abstract).
- **Assumptions and setting:** Simple affine vertex algebra `L_k(g)`, with g a finite-dimensional complex simple Lie algebra and k noncritical; the level criterion uses coprime positive integers p,q.
- **Caveat:** The associated-variety determination is stated only for rank at most six and E₇/E₈; the preprint is lengthy (126 pages), so its classification arguments need specialist review.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Algebra & number theory; Mathematical physics

### 6. [A proof of the Theta conjecture](https://arxiv.org/abs/2611.12451)
- **Abstract:** The authors prove a touching refinement of the Theta conjecture via a parking-function formula and derive the Theta conjecture and two valley Delta conjectures as corollaries.
- **Authors:** Haojun Bai, Feng Gu, Zhuowei Lin, Dun Qiu, Minhao Zhang
- **arXiv:** `2611.12451v1` (published 2026-11-09 14:05:43 UTC; categories: `math.CO`)
- **Evidence for ranking:** One refined identity is claimed to imply several named conjectures; the abstract also identifies the proof mechanism as matching algebraic and combinatorial recurrences with common initial conditions.
- **Claimed result:** The authors give a weighted parking-function formula for `Θ_{e_l}Θ_{e_k}∇E_{d,j}` with decorated rises, valleys, and touch number j; summing over j yields the Theta conjecture, with the valley Delta conjecture and its generalized version as corollaries (arXiv abstract).
- **Assumptions and setting:** Identities in the combinatorial algebra of symmetric and quasisymmetric functions, with parking functions and Dyck-path algebra; the abstract’s indices and objects are those of the conjectures cited by the authors.
- **Caveat:** The result concerns these specific generating-function identities; the abstract does not claim a general extension beyond the stated Theta/Delta conjectures.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Combinatorics & discrete mathematics

### 7. [Chvátal's Toughness Conjecture for Dense Almost Regular Graphs](https://arxiv.org/abs/2611.12519)
- **Abstract:** The author proves that sufficiently large 4-tough graphs with linear minimum degree and a sufficiently small linear degree spread are Hamiltonian, and constructs 3/2-tough regular non-Hamiltonian graphs of linear degree.
- **Authors:** Songling Shan
- **arXiv:** `2611.12519v1` (published 2026-11-09 14:57:14 UTC; categories: `math.CO`)
- **Evidence for ranking:** The abstract supplies a precise regime for a longstanding Hamiltonicity conjecture and a counterexample family showing the stated toughness constant cannot simply be reduced to 3/2.
- **Claimed result:** For every α>0 there are ε>0 and n₀ such that an n-vertex 4-tough graph with n≥n₀, minimum degree at least αn, and maximum-minus-minimum degree at most εn is Hamiltonian; the author also constructs 3/2-tough regular non-Hamiltonian graphs of linear degree (arXiv abstract).
- **Assumptions and setting:** Finite graphs in the sufficiently-large-n regime, with fixed positive density parameter α and degree-spread parameter ε depending on α.
- **Caveat:** The theorem handles dense almost-regular graphs, not all t-tough graphs; it proves a restricted case rather than Chvátal’s full conjecture.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Combinatorics & discrete mathematics

### 8. [A relative trace formula for the orthogonal Gan-Gross-Prasad model and the proof of its fundamental lemma](https://arxiv.org/abs/2611.12724)
- **Abstract:** The authors set up a comparison of relative trace formulas for the Gan–Gross–Prasad conjecture, match regular orbits, formulate the fundamental lemma and smooth-transfer conjecture, and prove the fundamental lemma for the Hecke-algebra unit element.
- **Authors:** Zhengyu Mao, Chen Wan
- **arXiv:** `2611.12724v1` (published 2026-11-09 17:09:27 UTC; categories: `math.NT`, `math.RT`)
- **Evidence for ranking:** The paper bridges number theory and representation theory and states both a comparison framework and a proved fundamental-lemma case, rather than only proposing a conjecture.
- **Claimed result:** The authors unfold the relative trace formulas, match regular orbits, formulate the corresponding fundamental lemma and smooth transfer, and prove the fundamental lemma for the unit element of the Hecke algebra (arXiv abstract).
- **Assumptions and setting:** The orthogonal Gan–Gross–Prasad model and its associated relative trace formulas; the proved case is specifically the unit element.
- **Caveat:** The abstract formulates smooth transfer as a conjecture and proves the fundamental lemma only for the unit Hecke function, not in full generality.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Algebra & number theory

### 9. [Perdomo's index conjecture for minimal hypersurfaces in spheres](https://arxiv.org/abs/2611.12632)
- **Abstract:** For a full minimal immersion of a closed, connected, oriented n-manifold into the unit sphere, the authors claim Morse index at least n+3, with equality exactly for standard Clifford embeddings, and a stronger lower bound for non-Clifford images.
- **Authors:** Qian Fu, Fagui Li
- **arXiv:** `2611.12632v1` (published 2026-11-09 16:11:06 UTC; categories: `math.DG`)
- **Evidence for ranking:** The paper states a complete lower bound and equality characterization for a named geometric conjecture, with a clear distinction between equality and non-Clifford cases.
- **Claimed result:** The authors prove Morse index at least n+3, equality precisely for standard Clifford embeddings, and an (n+4)-dimensional negative-definite subspace for the Jacobi quadratic form when the image is non-Clifford (arXiv abstract).
- **Assumptions and setting:** Full minimal immersion `x:Mⁿ→Sⁿ⁺¹(1)`; M is closed, connected, and oriented, with n≥2.
- **Caveat:** The conclusion is limited to the stated full, closed, oriented setting and the unit sphere; no broader ambient geometry is claimed in the abstract.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Geometry & topology

### 10. [Sharpness of the Martin-O'Bryant autoconvolution inequality](https://arxiv.org/abs/2611.12685)
- **Abstract:** For every nonnegative f in L¹(R)∩L²(R), the authors show that the coefficient 1 in a stated autoconvolution inequality cannot be replaced uniformly by any smaller constant.
- **Authors:** Tonći Crmarić, Vjekoslav Kovač, Jelena Rupčić
- **arXiv:** `2611.12685v1` (published 2026-11-09 16:47:53 UTC; categories: `math.CA`)
- **Evidence for ranking:** The paper addresses sharpness of a specific functional inequality and gives a clean uniform impossibility statement in a focused analysis paper.
- **Claimed result:** There is no c<1 such that `||f*f||₂² ≤ c ||f*f||₁ ||f*f||∞` holds for every nonnegative `f∈L¹(R)∩L²(R)` (arXiv abstract).
- **Assumptions and setting:** Real-line convolution; f is nonnegative and belongs to both L¹ and L².
- **Caveat:** The abstract establishes that the coefficient cannot be uniformly lowered, but does not state whether equality is attained or characterize near-extremizing functions.
- **Announcement type:** new submission, announcement-batch date 2026-11-10
- **Themes:** Analysis & PDE

## Trending Research Themes

- **Conjecture closure with explicit equality or boundary cases:** The lemniscate paper identifies all maximizing polynomials, while the graph-distance paper proves its conjectured inequality for every connected graph (2611.12830; 2611.12781). The Theta paper also derives multiple identities from a refined formula, but is an isolated combinatorial strand rather than evidence of a broad field-wide shift (2611.12451).
- **Classification by reducing infinite possibilities to finite arithmetic or structural lists:** The Nahm-sum paper reduces its stated rank-two domain to three families, split products, and 34 exceptional triples; the quasi-lisse paper classifies levels across all finite-dimensional simple Lie algebras (2611.12868; 2611.12723). They share a classification goal, not a demonstrated common technique.
- **Proof artifacts and sharp hypotheses:** Exact certificates and companion checks accompany the Nahm-sum classification; the Navier–Stokes preprint reports Lean formalization; the graph Hamiltonicity result pairs a dense almost-regular theorem with explicit counterexamples at lower toughness (2611.12868; 2611.12862; 2611.12519). These are distinct ways to make verification and scope explicit, not evidence of a general methodological turn.
- **Bridges across mathematical areas:** The odd-viscosity work connects PDE and mathematical physics; the vertex-algebra classification spans representation theory, mathematical physics, and quantum algebra; the relative trace formula links number theory and representation theory (2611.12862; 2611.12723; 2611.12724). This is a cross-listing pattern among selected papers, not a claim about the entire 792-paper batch.

## Open Problems and Research Directions

- **Author-stated open problem:** The odd-viscosity paper says its polynomial sufficient threshold is not known to be sharp and leaves the sharp threshold for the original equation open. A concrete follow-up is to test whether weighted-energy estimates can be sharpened in the forced regimes and compare the resulting threshold with direct bounded-region barriers (2611.12862).
- **Author-stated scope gap:** The relative trace formula paper proves the fundamental lemma for the unit Hecke element while formulating smooth transfer as a conjecture. Extending the proved comparison to broader test functions, then checking what follows for smooth transfer, is a natural next step (2611.12724).
- **Scope gap and proposed research direction:** The Chvátal result applies to dense almost-regular graphs, and the abstract gives 3/2-tough non-Hamiltonian examples alongside a 4-tough theorem. Determining which additional degree hypotheses narrow this gap is a possible follow-up; this is a synthesis, not an explicitly stated problem in the abstract (2611.12519).
- **Proposed synthesis:** For the lemniscate theorem, investigate quantitative stability: if a monic polynomial’s lemniscate length is close to maximal, must its coefficients or critical values be close to those of a translate/rotation of `z^n−1`? The exact equality classification motivates the question; it is not presented here as author-stated (2611.12830).
- **Proposed generalization:** Extend the complete Nahm-sum classification beyond rational symmetric rank-two data, beginning with controlled relaxations of symmetry or rank. The paper’s degree-four reduction suggests a point of comparison, but tractability is not assumed (2611.12868).

## Takeaway

The clearest substantive pattern is authors presenting complete results: conjecture proofs, classifications, and the exact boundary of their hypotheses. Several claims come with verification artifacts, but all ten are new preprints; treat them as author-reported results pending expert assessment, not as a readership ranking.

## Method and sources

- **Window:** Daily Mathematics announcement batch 2026-11-10 (start and end date: 2026-11-10). At the 2026-11-11 snapshot, the latest listing had no 11 November batch, so this report uses the prior batch. Snapshot: 2026-11-11 01:26:59 UTC.
- **Coverage:** The `math` recent listing was opened in its full view; the latest batch displayed 792 entries. The selected papers are all in math.*; each arXiv abstract page and submission history were checked. Introductions and main-result statements were inspected for the top three selections.
- **Inference:** arXiv has no official trend chart. All ten are new submissions in one batch, so recency is not used to imply popularity. Selection and ordering emphasize concrete claimed results, scope, cross-listing, stated proof artifacts, and checkable external discussion. No reliable independent mathematical discussion for these same-day items was located. Citation evidence is limited for a batch less than a day old; counts are not treated as period gains. Semantic Scholar citation fields were not available at snapshot time. This is a ranked set of notable recent papers, not a measured popularity list.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); abstract/history pages linked in each title; arXiv HTML excerpts for [2611.12830v1](https://arxiv.org/html/2611.12830v1), [2611.12781v1](https://arxiv.org/html/2611.12781v1), and [2611.12868v1](https://arxiv.org/html/2611.12868v1); Semantic Scholar Graph API queried by arXiv identifier; candidate-specific web searches for independent discussion. The modularity paper points to a DOI-archived computational companion: https://doi.org/10.5281/zenodo.24062300.
