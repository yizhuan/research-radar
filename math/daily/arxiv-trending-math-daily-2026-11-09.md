# Mathematics — Monday, 9 November 2026

Daily window: the latest Mathematics announcement batch, 2026-11-09 (one-day window); the selected papers were first submitted on 2026-11-06. This report selects 10 notable papers from the 346-entry batch. The recurring pattern is sharp theorem-making—conjecture resolutions, exact thresholds, and improved asymptotics. Brief agenda: algebraic geometry and combinatorics first, then probability, analysis, and a matrix-multiplication result. This is an inferred ordering, not an official arXiv trending chart; citation evidence for papers only days old is limited, so these are notable recent papers rather than measured popularity leaders.

## Top papers (ranked)

### 1. [The Woo-Yong conjecture](https://arxiv.org/abs/2611.09237)
- **Abstract:** The author proves the Woo-Yong conjecture for type A Schubert varieties, extends divisor-class detection to torsion classes in arbitrary finite crystallographic type, and gives a type D example showing why the broader claim needs qualification.
- **Authors:** Minghua Dou
- **arXiv:** `2611.09237v1` (published 2026-11-06 09:57:45 UTC; categories: `math.AG` [primary], `math.AC` [cross-list])
- **Evidence for ranking:** A concrete conjecture resolution with a stronger all-Weil-divisor statement in type A, a finite-type extension, and ancillary verification programs and exact certificates recorded on the arXiv page.
- **Claimed result:** The paper's Theorem 1.2 says that for every scheme point of a type A complete or partial flag Schubert variety, local divisor classes are detected at the generic points of the maximal singular components through that point; applying this to the canonical divisor proves the Woo-Yong conjecture.
- **Assumptions and setting:** Type A Schubert varieties admit the full local detection statement. For arbitrary finite crystallographic type, the paper proves injectivity only on the torsion subgroup of the source local class group.
- **Caveat:** The paper gives a type D family where the full, unrestricted analogue fails; the torsion qualification outside type A is essential.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Geometry & topology; Algebra & number theory

### 2. [The small ball problem for the Brownian sheet: sharp bounds via entropy numbers in L∞](https://arxiv.org/abs/2611.09495)
- **Abstract:** The authors settle the uniform small-deviation conjecture for Brownian sheets in every dimension d ≥ 2 using sharp entropy and Kolmogorov estimates, and derive related bounds for several mixed-smoothness function classes and Gaussian fields.
- **Authors:** Dmitriy Bilyk, Sebastian Neumayer, Tino Ullrich
- **arXiv:** `2611.09495v1` (published 2026-11-06 14:15:50 UTC; categories: `math.FA` [primary], `math.PR` [cross-list])
- **Evidence for ranking:** Theorem 1.1 resolves the stated conjecture for all dimensions d ≥ 2; the paper links probability to functional analysis and provides a Lean certificate link in its abstract.
- **Claimed result:** Theorem 1.1 claims −log P(‖B‖∞ ≤ ε) ≍d ε⁻²(log(1/ε))^(2d−1) as ε ↓ 0 for the d-dimensional Brownian sheet; the authors also obtain entropy, small-deviation, quantization, and approximation consequences.
- **Assumptions and setting:** B is the centered continuous Gaussian sheet on [0,1]^d with covariance ∏ᵢ min(sᵢ,tᵢ), measured in the uniform norm; d ≥ 2.
- **Caveat:** The theorem gives asymptotic order with dimension-dependent comparison constants, not a leading constant; the proof uses a probabilistic small-ball inequality rather than resolving the separate deterministic Haar-function inequality discussed in the introduction.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Probability & statistics; Analysis & PDE

### 3. [The BCC lattice is the optimal 3D lattice quantizer for all p ≥ 1](https://arxiv.org/abs/2611.09523)
- **Abstract:** The author proves that among three-dimensional lattices of covolume one, the body-centered cubic lattice uniquely minimizes every finite p-th moment of the Voronoi cell, up to orthogonal transformations, resolving the Graf–Luschgy conjecture for lattice quantizers.
- **Authors:** Senping Luo
- **arXiv:** `2611.09523v1` (published 2026-11-06 14:36:48 UTC; categories: `math.AP` [primary], `math-ph`, `math.CO`, `math.OC` [cross-lists])
- **Evidence for ranking:** Theorem 1.1 gives a unique optimizer for the full finite range p ≥ 1 and resolves a named conjecture; the paper spans four mathematical classifications and describes exact interval/numerical polynomial comparisons in its proof.
- **Claimed result:** Theorem 1.1 claims that for every 1 ≤ p < ∞, the unit-covolume BCC lattice uniquely minimizes the normalized Voronoi p-moment among full-rank 3D lattices, modulo orthogonal transformations.
- **Assumptions and setting:** The optimization is over Bravais lattices in R³ with fixed covolume one; p is finite and at least one.
- **Caveat:** This is a lattice-class result, not a proof that BCC is optimal among unrestricted point configurations or all non-lattice quantizers; the proof includes computer-assisted interval/polynomial bounds that this report has not independently checked.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Optimization & control; Mathematical physics; Combinatorics & discrete mathematics

### 4. [Macdonald intersections and the N!/k conjecture](https://arxiv.org/abs/2611.09638)
- **Abstract:** The authors prove the conjectured Frobenius-characteristic formula for intersections of Garsia–Haiman modules and, as a consequence, resolve the N!/k conjecture using the geometry of the Hilbert scheme of points on the plane.
- **Authors:** Peter L. Guo, Mingyang Kang, Changjian Su, Rui Xiong
- **arXiv:** `2611.09638v1` (published 2026-11-06 15:52:37 UTC; categories: `math.CO` [primary], `math.AG` [cross-list])
- **Evidence for ranking:** A named conjecture is resolved, with a direct bridge between algebraic combinatorics and algebraic geometry; the arXiv abstract identifies Haiman's Hilbert-scheme geometry as the proof framework.
- **Claimed result:** The authors prove the Bergeron–Garsia-predicted Frobenius characteristic formula for the relevant Garsia–Haiman module intersections; their Corollary 1.1 gives dimension N!/k under the same hypotheses.
- **Assumptions and setting:** For n ≥ 2, k ≥ 1, N = n−1, and a partition λ of n, take k distinct partitions of N obtained by removing a corner cell from λ; the formula concerns the intersection of their associated bigraded Garsia–Haiman modules.
- **Caveat:** The result is for this specific corner-removal family of module intersections; it does not resolve other Macdonald-polynomial conjectures beyond the stated formula and N!/k consequence.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 5. [Harper's beyond square-root conjecture for random matrices](https://arxiv.org/abs/2611.09753)
- **Abstract:** For a Haar unitary matrix U_N, the authors prove that E|tr(Sym^k U_N)| tends to zero as min(N,k) tends to infinity, settling the random-matrix version of Harper's conjecture without restricting k/N.
- **Authors:** William Verreault, Max Wenqiang Xu
- **arXiv:** `2611.09753v1` (published 2026-11-06 17:21:41 UTC; categories: `math.NT` [primary], `math.PR` [cross-list])
- **Evidence for ranking:** The paper settles a specifically named random-matrix conjecture uniformly across the relative-growth regimes of k and N, and connects number theory, probability, and holomorphic multiplicative chaos.
- **Claimed result:** The authors establish the vanishing first absolute moment for traces of symmetric powers of Haar unitary matrices as min(N,k) → ∞, using exact weighted trace moments and a Gaussian change of measure.
- **Assumptions and setting:** U_N is Haar-distributed on the unitary group of size N; the limit requires both N and k to tend to infinity, with no condition on their ratio.
- **Caveat:** This proves the random-matrix analogue, not Harper's original arithmetic conjecture about random multiplicative functions or its number-theoretic consequences.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Probability & statistics; Algebra & number theory; Mathematical physics

### 6. [Sharp universality thresholds for random profinite groups](https://arxiv.org/abs/2611.09477)
- **Abstract:** The authors determine sharp conditions for random quotients of free profinite groups to converge to the Liu–Wood distribution, including a sharp factor-count threshold and an exact parity-and-length criterion for random words.
- **Authors:** Jiwan Jung, Jungin Lee
- **arXiv:** `2611.09477v1` (published 2026-11-06 13:58:58 UTC; categories: `math.PR` [primary], `math.GR` [cross-list])
- **Evidence for ranking:** The abstract supplies both sufficient and sharp failure thresholds and an if-and-only-if criterion; probability and group theory are both primary mathematical components.
- **Claimed result:** For fixed u ≥ 0 and quotients of the free profinite group on n generators by n+u independent random relations, the authors prove universality under stated coset-balance conditions; for fixed-length random words, convergence holds exactly when lengths are eventually odd and ℓₙ − log n → ∞.
- **Assumptions and setting:** The number u is fixed; relations are independent, and the factor-product results require the paper's coset-balance hypotheses. The word-length threshold is asymptotic in n.
- **Caveat:** These thresholds are model-specific; the abstract does not claim the same conditions for arbitrary dependent relations or all random profinite-group constructions.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Probability & statistics; Algebra & number theory

### 7. [The maximum size of 3-distance binary codes](https://arxiv.org/abs/2611.09675)
- **Abstract:** The authors show that for every n ≥ 24, the largest family in {−1,1}ⁿ with at most three distinct pairwise Hamming distances has size C(n,3)+n, and that the threshold n = 24 is best possible.
- **Authors:** Valjakas Djaljapayan, Hao Huang, Wei-Hsuan Yu
- **arXiv:** `2611.09675v1` (published 2026-11-06 16:25:58 UTC; categories: `math.CO` [primary])
- **Evidence for ranking:** It gives an exact extremal value uniformly for all n ≥ 24, with a sharp threshold witnessed by the length-23 dual binary Golay code; the abstract's claim is stronger than a bound for a restricted choice of distances.
- **Claimed result:** The authors prove that every binary family whose pairwise Hamming distances take at most three distinct values has size at most C(n,3)+n for n ≥ 24, and exhibit a family attaining the bound.
- **Assumptions and setting:** The ambient space is {−1,1}ⁿ with Hamming distance; “3-distance” means at most three distinct distances among pairs of distinct vectors.
- **Caveat:** The paper states that classifying all extremal families remains unresolved; at n = 24 there is already a non-isometric extremal construction.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Combinatorics & discrete mathematics

### 8. [Division ring extensions and a counterexample to the pure semisimplicity conjecture](https://arxiv.org/abs/2611.09749)
- **Abstract:** The authors construct division-ring extensions yielding, in characteristic zero, a hereditary right pure-semisimple ring of infinite representation type, a counterexample to the pure semisimplicity conjecture; they also construct finite-type examples in characteristic p ≥ 3.
- **Authors:** A. I. Generalov, A. Tursunbaev
- **arXiv:** `2611.09749v1` (published 2026-11-06 17:18:35 UTC; categories: `math.RA` [primary], `math.RT` [cross-list])
- **Evidence for ranking:** The paper gives an explicit counterexample to a named conjecture and a family of characteristic-p constructions; its algebraic objects connect ring theory and representation theory.
- **Claimed result:** In characteristic zero, the authors claim a hereditary right pure-semisimple ring with infinitely many indecomposable finitely generated modules; for every prime p ≥ 3, they construct a hereditary artinian ring of finite representation type with Coxeter diagram I₂(p+2).
- **Assumptions and setting:** The counterexample is built from a division-ring extension over a characteristic-zero field; the second family is for fields of characteristic p ≥ 3.
- **Caveat:** The counterexample is one-sided (right pure semisimplicity); it does not assert left pure semisimplicity or a two-sided analogue.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Algebra & number theory

### 9. [Sharper energy scaling bounds of the singularly perturbed Tartar square](https://arxiv.org/abs/2611.09500)
- **Abstract:** The author improves the lower-bound argument so that the lower and upper bounds for the singularly perturbed Tartar square have matching logarithmic powers, with order exp(−C(log(ε⁻¹))^(1/2)) for suitable constants.
- **Authors:** Lennart Machill
- **arXiv:** `2611.09500v1` (published 2026-11-06 14:21:54 UTC; categories: `math.AP` [primary])
- **Evidence for ranking:** It closes a previously reported logarithmic-power mismatch between lower and upper scaling bounds and gives distinct Fourier-multiplier and iterated-branching refinements.
- **Claimed result:** The author claims matching logarithmic exponents in the energy scaling law, improving the ansatz-free lower bound and sharpening an upper construction by iterated branching.
- **Assumptions and setting:** The setting is the singular perturbation parameter ε for the Tartar-square problem; the result is an asymptotic scaling estimate with suitable lower- and upper-bound constants.
- **Caveat:** Matching exponents do not identify a common sharp constant; the paper quantifies a remaining gap between its lower- and upper-bound constants.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Analysis & PDE; Mathematical physics

### 10. [Tensor value and the 9/4 bound for matrix multiplication](https://arxiv.org/abs/2611.09716)
- **Abstract:** The authors give an exposition of the recent bound that the matrix-multiplication exponent is at most 9/4 over every field, using a fractional symmetrized tensor value and a superadditivity inequality for partially direct sums.
- **Authors:** Mahmut Levent Doğan, Vladimir Lysikov, Keiya Sakabe, Michael Walter
- **arXiv:** `2611.09716v1` (published 2026-11-06 16:56:52 UTC; categories: `cs.CC` [primary], `math.RT` [cross-list])
- **Evidence for ranking:** The paper is cross-listed in representation theory and computational complexity and gives a new tensor-value framework for deriving a major recent exponent bound; the arXiv abstract explicitly labels the work an exposition of OpenAI's result.
- **Claimed result:** The authors prove a superadditivity inequality for a power of their fractional symmetrized tensor value on partially direct sums; combined with polynomial-multiplication tensor degenerations from the prior OpenAI proof, this yields the stated 9/4 bound.
- **Assumptions and setting:** The bound is stated over every field; the method concerns tensor degenerations and partially direct sums with a shared factor and independent subspaces in the other factors.
- **Caveat:** This preprint is an exposition and alternate proof framework for a result already announced by OpenAI, not the original discovery of the 9/4 bound.
- **Announcement type:** new submission, announcement-batch date 2026-11-09
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

## Trending Research Themes

- Algebraic geometry is carrying several explicit structural results: the Woo-Yong paper localizes divisor classes on type A Schubert varieties, while the Macdonald-intersection paper uses Hilbert-scheme geometry to prove a representation-theoretic formula. These are distinct arguments, not one shared technique.
- Sharp thresholds and exact extremal statements recur across otherwise different areas: the Brownian-sheet paper gives an all-dimension small-deviation exponent, the profinite-group paper gives sharp universality conditions, and the binary-code paper determines an exact maximum above a best-possible threshold. The BCC and Tartar papers add sharp optimization and energy-scaling estimates, respectively.
- Probability links to several mathematical settings rather than forming a single topic cluster: Brownian-sheet small deviations connect Gaussian probability to entropy numbers; Harper's result connects random matrices with number theory; random profinite quotients connect probability and group theory.
- Proof-support artifacts appear in isolated high-profile results: the Woo-Yong record lists verification programs and certificates, and the Brownian-sheet abstract links a Lean certificate. These are checkable artifacts, but not evidence that the underlying proofs have been independently audited here.
- The 9/4 matrix-multiplication paper is an isolated bridge between computational complexity and representation theory; its role is to explain a new tensor-value route to a recently announced bound, not to indicate a broader shift in the math archive.

## Open Problems and Research Directions

- **Author-stated limitation — broader divisor detection:** For non-type-A Schubert varieties, the paper proves torsion-class detection, while its type D example rules out an unrestricted extension. A follow-up could characterize which non-torsion classes fail and whether additional geometric hypotheses recover full detection. [Woo-Yong conjecture](https://arxiv.org/abs/2611.09237)
- **Author-stated open problem — deterministic small-ball inequality:** The Brownian-sheet paper notes that the deterministic Haar-function small-ball inequality remains open. One direction is to test whether its probabilistic smooth-atom inequality can yield the missing deterministic estimate. [Brownian sheet](https://arxiv.org/abs/2611.09495)
- **Scope gap — unrestricted quantization:** The BCC theorem optimizes only over lattices; unrestricted three-dimensional quantization is tied to the broader Gersho problem. Extending the comparison beyond lattice cells would test how far the BCC conclusion generalizes. [BCC quantizer](https://arxiv.org/abs/2611.09523)
- **Author-stated open problem — extremal classification:** The 3-distance paper determines the maximum size but leaves classification of extremizers open; its n = 24 example already shows that extremizers need not be unique up to isometry. [3-distance codes](https://arxiv.org/abs/2611.09675)
- **Author-stated quantitative gap — energy constants:** The Tartar-square paper matches the logarithmic powers but still has distinct lower- and upper-bound constants. Improving either bound or identifying the sharp constant would sharpen the scaling law. [Tartar square](https://arxiv.org/abs/2611.09500)
- **Research direction (synthesis) — arithmetic transfer:** Harper's result settles only a random-matrix analogue. A separate question is whether techniques or consequences transfer to the original arithmetic conjecture about random multiplicative functions; this preprint alone does not establish that transfer. [Harper random-matrix paper](https://arxiv.org/abs/2611.09753)

## Takeaway

Today's clearest signals are mathematically concrete: named conjectures proved or refuted, plus sharp estimates whose hypotheses and remaining gaps are explicit. They span several fields rather than one unified methodological wave; the ordering should be read as a reasoned shortlist, not a measure of readership or downloads.

## Method and sources

- Window: daily latest arXiv Mathematics announcement batch dated 2026-11-09; selected submissions were v1 papers first posted 2026-11-06. Window start/end: 2026-11-09 to 2026-11-09. Snapshot: 2026-11-09 17:33:45 UTC.
- Coverage: the full `math/recent` announcement batch was traversed (346 entries). Selection was based on the stated theorem/result, category cross-listing, sharpness or conjecture status, and verifiable proof artifacts; all 10 selected arXiv abstract pages and relevant HTML result statements were checked. No numeric trend score was assigned.
- Attention evidence: Semantic Scholar did not return usable records in this pass, and no independent seminar or expert-discussion signal was verified. Therefore the order reflects potential mathematical significance and cross-subfield relevance, not measured popularity; current citations are not reported as period gains. All results are presented as claims in new arXiv preprints; this report does not certify their proofs or peer-review status.
- Retrieval note: `web_extract` was unavailable because the configured backend was search-only. Abstracts and result statements were read from arXiv's abstract/HTML pages; web search was used for corroborating source discovery. Semantic Scholar requests returned HTTP errors, so citation counts and influential-citation data were excluded.
- Core archive source: [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent). Paper sources: the linked arXiv abstract pages above; top-result statements were checked in the linked HTML versions. arXiv publishes no official trending chart.
