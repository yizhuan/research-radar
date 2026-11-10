# arXiv mathematics — daily notable papers, 10 November 2026

Six papers from the Tuesday, 10 November announcement batch. The batch's strongest signal is several concrete conjecture resolutions or sharply delimited classification/regularity theorems; the six entries span graph theory, complex analysis, number theory, representation theory, and PDE. Spoken agenda: first the graph and polynomial conjectures, then a modularity classification and a trace-formula result, and finally a conditional Navier–Stokes regularity theorem. This is an inferred ordering, not an official arXiv trending chart; citation evidence is limited for papers announced today, so this is a notable-recent-papers list rather than a measured popularity ranking.

## Top papers (ranked)

### 1. [A proof of the Erdős-Herzog-Piranian lemniscate conjecture](https://arxiv.org/abs/2611.12830)
- **Abstract:** For every monic complex polynomial of degree at least one, the authors claim the unit lemniscate has length no greater than that of `z^n−1`, with equality exactly for its translated and rotated forms.
- **Authors:** Teng Zhang
- **arXiv:** `2611.12830v1` (published 2026-11-09 18:29:49 UTC; categories: `math.CV`)
- **Evidence for ranking:** The abstract and Theorem 1.3 give an all-degrees resolution of a conjecture dating to 1958 and characterize every equality case; the paper also explicitly identifies its finite-range estimates as computer-assisted. These are unusually concrete claims, not evidence of measured readership.
- **Claimed result:** The author claims the Erdős–Herzog–Piranian length inequality for every monic polynomial and the stated equality characterization (arXiv abstract and HTML Theorem 1.3).
- **Assumptions and setting:** Monic complex polynomials of degree `n ≥ 1`; compare the arclength of `{z: |p(z)|=1}` against the lemniscate for `z^n−1`.
- **Caveat:** The proof supplements analytic arguments with rigorous computer-assisted estimates over a finite degree range; the certificates and their implementation merit specialist review. The preprint is not presented here as peer-reviewed.
- **Announcement type:** new submission, 2026-11-10 batch
- **Themes:** Complex analysis (additional theme; no controlled theme fits precisely)

### 2. [Chvátal's Toughness Conjecture for Dense Almost Regular Graphs](https://arxiv.org/abs/2611.12519)
- **Abstract:** For each fixed `α>0`, the author claims every sufficiently large 4-tough graph with minimum degree at least `αn` and maximum-minus-minimum degree at most `εn` is Hamiltonian, and constructs 3/2-tough regular non-Hamiltonian examples of linear degree.
- **Authors:** Songling Shan
- **arXiv:** `2611.12519v1` (published 2026-11-09 14:57:14 UTC; categories: `math.CO`)
- **Evidence for ranking:** Theorem 1.3 makes a long-standing conjecture true in a broad degree-defined class without a separate forbidden-subgraph condition, and the paper gives a counterexample that constrains the toughness threshold. This is a prominent claim within graph theory, not an attention metric.
- **Claimed result:** The author proves the 4-tough Hamiltonicity result with the stated degree hypotheses and constructs 3/2-tough regular non-Hamiltonian graphs (arXiv abstract and HTML Theorem 1.3).
- **Assumptions and setting:** For every fixed `α>0`, there are `ε>0` and `n₀` such that the result holds for `n≥n₀`, minimum degree `δ(G)≥αn`, and degree spread `Δ(G)−δ(G)≤εn`.
- **Caveat:** This settles only a dense almost-regular regime, not Chvátal's unrestricted conjecture; the 4-tough theorem and 3/2-tough counterexamples leave a gap in the threshold.
- **Announcement type:** new submission, 2026-11-10 batch
- **Themes:** Combinatorics & discrete mathematics

### 3. [A complete symmetric rank-two modularity classification, obtained through a sharp uniform degree bound](https://arxiv.org/abs/2611.12868)
- **Abstract:** The author claims a complete classification of modular rank-two Nahm sums with rational symmetric positive-definite matrices and rational shifts, consisting of explicit families, split rank-one products, and 34 exceptional triples.
- **Authors:** Cetin Hakimoglu-Brown
- **arXiv:** `2611.12868v1` (published 2026-11-09 18:53:47 UTC; categories: `math.NT`)
- **Evidence for ranking:** The claimed classification is exhaustive under stated hypotheses and rests on a sharp degree-at-most-four bound; the abstract and arXiv comment point to exact certificates, verification programs, independent implementations, and a DOI-archived computational companion.
- **Claimed result:** The author claims that no further modular data occur in the specified rank-two rational setting, and that all distinguished Nahm points have joint degree at most four (arXiv abstract and HTML Theorem 1.1).
- **Assumptions and setting:** A rational symmetric positive-definite `2×2` matrix, rational shifts, and modular Nahm sums; classification is up to coordinate exchange and includes rational-point families, split products, and exceptional data.
- **Caveat:** The classification does not cover higher rank, nonsymmetric matrices, or irrational parameters. Its exhaustive arithmetic and computational certificates should be checked independently; the preprint is not presented as peer-reviewed.
- **Announcement type:** new submission, 2026-11-10 batch
- **Themes:** Algebra & number theory

### 4. [Average distance and maximum induced linear forest](https://arxiv.org/abs/2611.12781)
- **Abstract:** For every finite connected graph, the authors claim the 2009 conjectured upper bound that average pairwise distance is at most half the order of a largest induced linear forest.
- **Authors:** Mathieu Bouchard, Alain Hertz
- **arXiv:** `2611.12781v1` (published 2026-11-09 17:54:36 UTC; categories: `math.CO`)
- **Evidence for ranking:** The arXiv comment explicitly says the work establishes a conjecture dating to 2009; the abstract states the inequality for all connected graphs and notes that it strengthens earlier bounds involving induced forests and independence number.
- **Claimed result:** The authors prove `μ(G) ≤ L(G)/2`, equivalently `4W(G) ≤ L(G)n(n−1)`, for every connected graph (arXiv abstract).
- **Assumptions and setting:** A finite connected graph `G` of order `n`; `μ(G)` is average distance, `W(G)` the Wiener index, and `L(G)` the maximum order of an induced subgraph whose components are paths.
- **Caveat:** The claim concerns this one global inequality; the abstract does not claim an equality classification or a stability theorem.
- **Announcement type:** new submission, 2026-11-10 batch
- **Themes:** Combinatorics & discrete mathematics

### 5. [A relative trace formula for the orthogonal Gan-Gross-Prasad model and the proof of its fundamental lemma](https://arxiv.org/abs/2611.12724)
- **Abstract:** The authors compare relative trace formulas for the Gan–Gross–Prasad conjecture, match regular orbits, formulate the associated fundamental lemma and smooth-transfer conjecture, and prove the fundamental lemma for the unit Hecke-algebra element.
- **Authors:** Zhengyu Mao, Chen Wan
- **arXiv:** `2611.12724v1` (published 2026-11-09 17:09:27 UTC; categories: `math.NT`, `math.RT`)
- **Evidence for ranking:** A specific claimed fundamental-lemma proof, plus cross-listing in number theory and representation theory, gives this entry a concrete cross-area signal; the abstract also sets out a relative-trace-formula comparison framework.
- **Claimed result:** The authors claim the fundamental lemma for the unit element of the Hecke algebra for the orthogonal Gan–Gross–Prasad model (arXiv abstract).
- **Assumptions and setting:** The setting is the orthogonal Gan–Gross–Prasad model and a comparison of relative trace formulas; the stated theorem is for the unit Hecke-algebra element.
- **Caveat:** The abstract only claims the unit-element fundamental lemma; it formulates, rather than claims to prove, the smooth-transfer conjecture.
- **Announcement type:** new submission, 2026-11-10 batch
- **Themes:** Algebra & number theory

### 6. [Quantitative global regularity for Navier--Stokes equations with odd viscosity on the cubic three-torus](https://arxiv.org/abs/2611.12862)
- **Abstract:** For three-dimensional incompressible Navier–Stokes on the cubic torus, the authors claim a unique global strong solution for arbitrary mean-zero divergence-free `H²` initial data and independent steady `H²` forcing when a fixed odd-viscosity coefficient exceeds a norm-uniform sufficient threshold.
- **Authors:** Jinzheng Li, Yuqi Li, Hao-Yu Sun
- **arXiv:** `2611.12862v1` (published 2026-11-09 18:50:49 UTC; categories: `math.AP`, `math-ph`, `physics.flu-dyn`)
- **Evidence for ranking:** The claimed global theorem is quantitatively parameterized and cross-listed across analysis, mathematical physics, and fluid dynamics; the abstract says all three main theorems are formally verified in Lean 4 with Mathlib.
- **Claimed result:** The authors claim global strong well-posedness above a sufficient odd-viscosity threshold, positive-time smoothness in the unforced case, and additional regularity regions for explicit bounded data and forcing (arXiv abstract).
- **Assumptions and setting:** Three-dimensional incompressible flow on the cubic torus with vertical-derivative-of-curl odd viscosity; initial data and steady force are real, mean-zero/divergence-free as appropriate, and in second-order Sobolev spaces.
- **Caveat:** The threshold is sufficient, not claimed sharp; the authors explicitly leave the sharp threshold for the original equation open, and the theorem depends on the added odd-viscosity term.
- **Announcement type:** new submission, 2026-11-10 batch
- **Themes:** Analysis & PDE; Mathematical physics

## Trending Research Themes

- **Conjecture-driven graph theory:** Shan's toughness/Hamiltonicity result and Bouchard–Hertz's average-distance inequality are two distinct conjecture-resolution claims in combinatorics. Their shared feature is a sharpened global graph guarantee, not a single technique or evidence of a field-wide surge.
- **Exact scope and classification:** Hakimoglu-Brown's rank-two modularity classification and Mao–Wan's unit-element fundamental lemma both make sharply scoped claims in number theory/representation theory, but concern different objects and methods; this is an intersection signal, not a shared result.
- **Computer-assisted or formal certification (isolated cross-area signal):** Zhang reports rigorous finite-range estimates, Hakimoglu-Brown supplies exact certificates and verification programs, and Li–Li–Sun report Lean formalization. These are different verification approaches, so the small set does not establish a common methodological trend.
- **Conditional regularity in mathematical physics (isolated signal):** Li–Li–Sun study regularity with an added odd-viscosity mechanism; no second selected paper supports a broader PDE shift.

## Open Problems and Research Directions

- **Author-stated open problem — graph toughness:** Chvátal's unrestricted conjecture remains open outside the dense almost-regular theorem; the paper's 3/2-tough counterexamples and 4-tough result leave the sharp threshold unsettled. **Research direction (synthesis):** test whether additional degree-distribution hypotheses can close that gap, while separately seeking counterexamples below 4-toughness. [Shan](https://arxiv.org/abs/2611.12519)
- **Author-stated open problem — odd-viscosity threshold:** Li–Li–Sun explicitly do not claim optimality and leave the sharp threshold for the original equation open. **Research direction (synthesis):** derive necessary conditions or matching lower bounds in fixed normalized forcing regimes, then compare with their sufficient estimates. [Li, Li & Sun](https://arxiv.org/abs/2611.12862)
- **Author-stated gap — smooth transfer:** Mao–Wan formulate smooth transfer but state only the fundamental lemma for the unit Hecke-algebra element as proved. **Research direction (synthesis):** investigate what additional orbital-integral identities are needed to extend the comparison from the unit element to general test functions. [Mao & Wan](https://arxiv.org/abs/2611.12724)

## Takeaway

Today's selected papers are strongest where they state a precise conjecture resolution, an exhaustive classification, or a theorem with explicit hypotheses; two graph-theoretic claims and several cross-area certification artifacts stand out. They are all new preprints in the same announcement batch, so neither citation counts nor a lack of outside discussion can yet distinguish genuine community momentum from simply important-looking claims; expert and peer review remain essential.

## Method and sources

- **Window:** daily; Tuesday 2026-11-10 announcement batch (start date 2026-11-10; end date 2026-11-10). The latest batch was used, not a prior batch. Snapshot: 2026-11-10 17:21:52 UTC.
- **Coverage:** arXiv Mathematics recent listing, `math` archive and its subject classes. The listing reported 792 entries in the 10 November batch; the full batch was screened, then candidates were checked against their arXiv abstract pages and metadata. The six selected records are all new `v1` submissions dated 9 November UTC and announced on 10 November.
- **Inference:** no official arXiv trending chart exists. Papers were ordered by concrete, checkable claims (conjecture resolution, exhaustive classification, cross-listing, and proof artifacts), not by author reputation, API ordering, or a fabricated trend score. No citation counts or age-normalized citation momentum are claimed. Web searches found no independent expert/seminar discussion that could be used to validate attention for these just-announced papers.
- **Retrieval notes:** `web_extract` could not retrieve arXiv pages with the configured search-only backend, so the arXiv listing and abstract/HTML pages were read in the browser, with arXiv API metadata used for versions, timestamps, and categories. Semantic Scholar Graph requests returned no usable records at snapshot time; therefore its citation and influential-citation fields are not reported.
- **Sources:** [arXiv recent Mathematics listing](https://arxiv.org/list/math/recent); each paper's abstract URL is linked above. For the first three entries, the arXiv HTML introduction and main theorem statements were also inspected: [2611.12830v1](https://arxiv.org/html/2611.12830v1), [2611.12519v1](https://arxiv.org/html/2611.12519v1), [2611.12868v1](https://arxiv.org/html/2611.12868v1).