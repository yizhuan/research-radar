# Mathematics on arXiv — daily notable papers, 2 November 2026

Nine papers from the latest Mathematics announcement batch (2 November); the striking pattern is explicit conjecture resolutions and counterexamples, alongside rigorous probabilistic bounds. Spoken agenda: graph coloring and flows, rapid mixing, geometric invariants, then cross-field methods. This is a selection with an inferred ordering—not an official arXiv trending chart—and recent-paper citation evidence is limited, so it should not be read as measured popularity.

Window: 2 November 2026 announcement batch. Snapshot: 3 November 2026, 01:20:27 UTC. The latest batch available at snapshot time was the prior batch (2 November).

## Top papers (ranked)

### 1. [A Counterexample to the Alon-Krivelevich Conjecture and a New Lower Bound for Choosability of Bipartite Graphs](https://arxiv.org/abs/2610.42094)
- **Abstract:** The authors construct bipartite graphs whose list-chromatic number grows faster than any constant multiple of the logarithm of maximum degree, disproving the Alon–Krivelevich conjecture.
- **Authors:** Junran Yu, Gexin Yu
- **arXiv:** `2610.42094v1` (published 2026-10-30 17:39:18 UTC; categories: `math.CO`)
- **Evidence for ranking:** The claimed counterexample resolves an explicit longstanding conjecture and gives a quantitative lower bound; the authors combine weighted counting, probability, and a fixed-point argument. No independent expert discussion or citation-momentum signal was established for this new submission.
- **Claimed result:** The authors prove an uncolorability criterion for their explicit family and derive choice number at least `(1/32-o(1))(ln Δ)^2/(ln ln Δ)^3`, hence choice number divided by `ln Δ` tends to infinity.
- **Assumptions and setting:** Finite simple bipartite graphs; for integers `k≥2` and `r²>2(2k−1)ln(2k−1)`, the vertices are copies of the `k`-subsets of a `(2k−1)`-set, adjacent when their subsets intersect in at most `r` elements.
- **Caveat:** This is a new preprint's claimed disproof; the construction and proof have not been independently assessed here. Its asymptotic bound is the one derived for this construction, not a characterization of choosability for all bipartite graphs.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 2. [Rapid mixing of Potts Glauber dynamics throughout uniqueness](https://arxiv.org/abs/2610.42059)
- **Abstract:** The authors establish fast-mixing bounds for ferromagnetic Potts sampling across the full high-temperature uniqueness regimes on random regular graphs and lattice cubes or tori, and give a related random-cluster result.
- **Authors:** Antonio Blanca, Reza Gheissari, Heehyun Park, Xusheng Zhang
- **arXiv:** `2610.42059v1` (published 2026-10-30 17:20:57 UTC; categories: `math.PR`, `cs.DM`, `math-ph`)
- **Evidence for ranking:** The abstract states sharp threshold-scale results for two graph families and a separate logarithmic-time result for Swendsen–Wang dynamics; it also crosses probability, discrete mathematics, and mathematical physics. These are mathematical-significance signals, not evidence of readership.
- **Claimed result:** The authors prove `n polylog(n)` mixing with high probability on uniformly random `Δ`-regular graphs for `β<β_u(q,T_Δ)`, inverse spectral gap `n^(1+o(1))` on lattice cubes/tori for `β<β_c(q,Z^d)`, and `O(log n)` Swendsen–Wang mixing on random regular graphs throughout uniqueness.
- **Assumptions and setting:** Ferromagnetic `q`-state Potts model, every `q`; `Δ≥3` for random regular graphs and `d≥2` for lattice cubes or tori. The temperature bounds are strictly below the stated uniqueness/critical thresholds.
- **Caveat:** Results cover the specified random-regular and lattice graph families, not every bounded-degree graph; mixing bounds are asymptotic and the work is a new preprint. The authors disclose assistance from ChatGPT 5.6 and 6.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics; Mathematical physics

### 3. [The Cranston--Li--Su--Wang--Xu (2026) conjecture is true](https://arxiv.org/abs/2610.40863)
- **Abstract:** The author proves that in every finite graph with all degrees even, the graph of nowhere-zero flows is connected under the conjectured cycle changes, for finite abelian groups of size at least four and for integer flows with values bounded away from zero by the stated range.
- **Authors:** Dave Goel
- **arXiv:** `2610.40863v1` (published 2026-10-29 18:38:38 UTC; categories: `math.CO`)
- **Evidence for ranking:** The paper states a full resolution of a named conjecture and reports a Lean 4 formal proof with a public supporting-material link. The theorem's flow-reconfiguration setting also ties graph theory to formalized mathematics.
- **Claimed result:** The author proves both conjectured connectivity statements for even graphs: all finite abelian groups `A` with `|A|≥4`, and integer `k`-flows for every `k≥4`; the paper reports that all results are formalized in Lean 4 from its standard axioms.
- **Assumptions and setting:** Finite graphs (loops and parallel edges allowed) in which every vertex has even degree; intermediate flows must remain nowhere-zero, and moves are cycle changes of the specified nonzero value.
- **Caveat:** The Lean artifact supports checking the formalized statements but does not replace scrutiny of whether the formal definitions match intended conventions; the result is a recent preprint and has not been independently reviewed here.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Combinatorics & discrete mathematics; Logic & foundations

### 4. [Fluctuation bounds for rotationally invariant first-passage percolation](https://arxiv.org/abs/2610.42124)
- **Abstract:** For rotationally invariant first-passage percolation in dimensions `d≥2`, the authors prove stretched-exponential concentration of passage time around its time constant, implying a variance upper bound of order `n^(1−ε)`.
- **Authors:** Scott Armstrong, Ahmed Bou-Rabee
- **arXiv:** `2610.42124v1` (published 2026-10-30 17:54:21 UTC; categories: `math.PR`)
- **Evidence for ranking:** The result extends a sublinear variance bound described by the authors as previously proved in the planar case to rotationally invariant models in all dimensions `d≥2`; the listing notes a Lean 4 formalization. The concrete extension, rather than citation data, motivates this placement.
- **Claimed result:** The authors bound `E[exp(|T_n−μn|/n^(1/2(1−ε)))]` by a constant for some `ε>0`, implying `Var(T_n)≤C n^(1−ε)`; their proof combines scale induction, averaging, and an improved Efron–Stein inequality.
- **Assumptions and setting:** Rotationally invariant first-passage percolation on `R^d`, `d≥2`; `μ` is the time constant and `C, ε` are model-dependent constants as stated in the paper.
- **Caveat:** The abstract gives existence, not an explicit value, of the positive exponent `ε`; conclusions depend on the model's rotational-invariance assumptions.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Probability & statistics

### 5. [The metric Zariski multiplicity conjecture in dimension 4](https://arxiv.org/abs/2610.41954)
- **Abstract:** The author proves a metric version of multiplicity invariance for complex hypersurface germs under a bi-Lipschitz map, with a tangent-cone singular-locus hypothesis, and obtains the embedded bi-Lipschitz invariance in dimensions at most four.
- **Authors:** José Edson Sampaio
- **arXiv:** `2610.41954v1` (published 2026-10-30 16:08:06 UTC; categories: `math.AG`, `math.CV`, `math.MG`)
- **Evidence for ranking:** The paper gives a dimension-four result on an explicit geometric conjecture and links algebraic, complex, and metric geometry. Its author describes the earlier `n≤3` cases as known; no citation-momentum evidence was established.
- **Claimed result:** For reduced holomorphic function germs `f,g:(C^n,0)→(C,0)` related by a bi-Lipschitz homeomorphism of their zero sets, the author proves equality of multiplicities when every irreducible component of the tangent cone of `V(f)` has singular locus of dimension at most two. The paper also proves a degree-invariance statement for certain homogeneous hypersurfaces under a homeomorphism fixing the origin.
- **Assumptions and setting:** Complex analytic hypersurface germs at the origin; reduced defining functions, a bi-Lipschitz equivalence, and the stated tangent-cone singular-locus bound. The paper says this yields embedded bi-Lipschitz multiplicity invariance for `n≤4`.
- **Caveat:** The dimension-four theorem is conditional on the tangent-cone hypothesis; it does not assert the unrestricted topological Zariski multiplicity conjecture in dimension four.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Geometry & topology; Algebra & number theory

### 6. [Hedetniemi's conjecture for Shannon OR-capacity: counterexamples and asymptotic separation](https://arxiv.org/abs/2610.41977)
- **Abstract:** The author constructs graph pairs showing that Shannon OR-capacity of a categorical product can fall below the smaller factor capacity, including examples with an asymptotically large separation.
- **Authors:** Julius A. Zeiss
- **arXiv:** `2610.41977v1` (published 2026-10-30 16:26:18 UTC; categories: `math.CO`)
- **Evidence for ranking:** This gives explicit counterexamples to a named capacity identity and an asymptotic separation, with an open endpoint stated in the abstract. The result is a concrete discrete-mathematical claim, not a measured-attention signal.
- **Claimed result:** The author disproves the Shannon OR-capacity analogue of Hedetniemi's conjecture; constructions yield factors of arbitrarily large capacity whose product capacity is subpolynomial in the smaller factor's capacity.
- **Assumptions and setting:** Finite graphs under categorical product and Shannon OR-capacity; the constructions include one complete-graph factor, and one result applies for sufficiently large complete graphs.
- **Caveat:** The abstract leaves open whether product capacity must still tend to infinity whenever both factor capacities tend to infinity; the new construction does not settle that asymptotic question.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Combinatorics & discrete mathematics

### 7. [An odd version of the Grothendieck--Teichmüller Lie algebra and the odd Deligne--Drinfeld conjecture](https://arxiv.org/abs/2610.41766)
- **Abstract:** The authors define an odd graded-Lie-algebra analogue of the Grothendieck–Teichmüller Lie algebra and prove an odd Deligne–Drinfeld statement identifying it with a free graded Lie algebra on one generator of weight three.
- **Authors:** Florian Naef, Thomas Willwacher
- **arXiv:** `2610.41766v1` (published 2026-10-30 14:07:07 UTC; categories: `math.QA`, `math.AT`)
- **Evidence for ranking:** The abstract states a conjecture analogue and an associated graph-cohomology computation, with a direct bridge between quantum algebra and algebraic topology. No external attention or citation-momentum evidence was established.
- **Claimed result:** The authors prove the odd Deligne–Drinfeld conjecture: the odd Grothendieck–Teichmüller Lie algebra is free graded Lie on one odd generator of weight `3`; they consequently compute bottom-degree odd graph cohomology, which is mostly zero.
- **Assumptions and setting:** The odd variant is defined by replacing free Lie algebras in even generators with free graded Lie algebras in odd generators; its graph-complex relationship is the odd analogue of the classical one.
- **Caveat:** The stated cohomology conclusion concerns the bottom cohomological degree, not a complete computation of odd graph-complex cohomology in every degree.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Algebra & number theory; Geometry & topology

### 8. [Spectral Beurling-Selberg Approximation and Applications to Effective Motivic Chebotarev-Sato-Tate Estimates](https://arxiv.org/abs/2610.42022)
- **Abstract:** The author constructs spectral majorants and minorants for sets with controlled boundary geometry on compact Riemannian manifolds and applies them to effective equidistribution and conditional motivic Chebotarev–Sato-Tate estimates.
- **Authors:** Yassine El Kaouni
- **arXiv:** `2610.42022v1` (published 2026-10-30 16:53:30 UTC; categories: `math.NT`, `math.AG`, `math.DG`, `math.RT`)
- **Evidence for ranking:** The paper cross-lists four mathematical subfields and connects explicit spectral approximation to arithmetic equidistribution; it states uniformity under common boundary-content bounds. This is a cross-field and result-specific signal, not popularity evidence.
- **Claimed result:** The author proves spectral Beurling–Selberg approximations with controlled coefficients and Hausdorff stability, extends them to certain singular spaces, and derives effective motivic Chebotarev-Sato-Tate estimates under the stated conjectural motivic L-function formalism.
- **Assumptions and setting:** Compact connected Riemannian manifolds; target sets have boundaries of finite upper Minkowski content. The motivic estimates assume the specified L-function formalism, including the motivic Riemann hypothesis.
- **Caveat:** The arithmetic estimates are conditional on conjectural L-function properties; their strength depends on the boundary regularity and uniformity assumptions.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Analysis & PDE; Geometry & topology; Algebra & number theory

### 9. [Baker--Akhiezer sections from Higgs bundles and Landau levels in hyperbolic band theory](https://arxiv.org/abs/2610.42134)
- **Abstract:** The authors identify lowest-Landau-level states and vortices in a hyperbolic band model with Baker–Akhiezer sections and divisors of rank-two twisted Higgs bundles, explaining the level jump at zero momentum through a limiting process.
- **Authors:** Duong Dinh, Steven Rayan
- **arXiv:** `2610.42134v1` (published 2026-10-30 17:58:18 UTC; categories: `math-ph`, `cond-mat.mes-hall`, `hep-th`, `math.AG`)
- **Evidence for ranking:** The paper explicitly connects algebraic geometry of Higgs bundles with Landau-level states and hyperbolic band theory, and is cross-listed across four areas including `math.AG`. Its placement reflects a specific cross-disciplinary construction, not evidence of popularity.
- **Claimed result:** The authors identify the one-dimensional lowest Landau level at nonzero momentum with Baker–Akhiezer sections and its vortices with their divisors; they characterize the two-dimensional zero-momentum level via limiting directions and a degeneration to the Hitchin section.
- **Assumptions and setting:** Rank-two `O(3)`-twisted Higgs bundles on the projective line encoding genus-two hyperbolic crystals, in a uniform magnetic field with two flux quanta.
- **Caveat:** This is a first-version, 26-page preprint; the identification is in the stated genus-two model and field setting and is not a general classification of hyperbolic band systems.
- **Announcement type:** new submission, 2 Nov 2026
- **Themes:** Mathematical physics; Geometry & topology

## Trending Research Themes

- **Conjecture resolution and explicit obstruction constructions.** Separate papers claim a counterexample to the Alon–Krivelevich list-coloring bound, counterexamples for Shannon OR-capacity, and a proof of the even-graph flow-reconfiguration conjecture ([Yu & Yu](https://arxiv.org/abs/2610.42094), [Zeiss](https://arxiv.org/abs/2610.41977), [Goel](https://arxiv.org/abs/2610.40863)). This is a cluster within this announcement batch, not evidence of a field-wide shift.
- **Probability methods meeting combinatorial structure.** The list-coloring construction uses weighted/probabilistic counting, while the Potts result uses a shattering/escape dichotomy to obtain mixing without the usual correlation-decay assumptions; the first-passage-percolation paper also sharpens a concentration argument ([Yu & Yu](https://arxiv.org/abs/2610.42094), [Blanca et al.](https://arxiv.org/abs/2610.42059), [Armstrong & Bou-Rabee](https://arxiv.org/abs/2610.42124)). These are distinct proof techniques, not one shared method.
- **Formal verification appears alongside substantial graph-theoretic claims.** Goel reports a Lean 4 proof of both flow theorems, while Armstrong and Bou-Rabee list a Lean formalization for their fluctuation result; independent checking of the artifacts remains worthwhile ([Goel](https://arxiv.org/abs/2610.40863), [Armstrong & Bou-Rabee](https://arxiv.org/abs/2610.42124)).
- **Geometry bridges appear at two different scales.** A metric-geometric hypothesis controls multiplicity of analytic hypersurface germs, while Higgs-bundle data parametrizes states and vortices in a specific hyperbolic band model ([Sampaio](https://arxiv.org/abs/2610.41954), [Dinh & Rayan](https://arxiv.org/abs/2610.42134)). These are independent examples, not a common technique.
- **Spectral and algebraic tools cross into arithmetic.** The Beurling–Selberg paper links Riemannian spectral approximation to motivic equidistribution, conditional on conjectural L-function input; the odd Grothendieck–Teichmüller work links graded Lie algebras to graph cohomology ([El Kaouni](https://arxiv.org/abs/2610.42022), [Naef & Willwacher](https://arxiv.org/abs/2610.41766)).

## Open Problems and Research Directions

- **Author-stated open question:** Zeiss asks whether categorical-product Shannon OR-capacity must tend to infinity whenever both factor capacities tend to infinity. Follow-up work could seek constructions with both factors tending to infinity while product capacity stays bounded, or prove a weaker unavoidable growth rate ([Zeiss](https://arxiv.org/abs/2610.41977)).
- **Unresolved validation/generalization:** Yu and Yu's preprint claims a counterexample to the Alon–Krivelevich conjecture. Independent proof checking is the immediate research task; separately, one could test whether their lower-bound order is sharp for the constructed family or improve it ([Yu & Yu](https://arxiv.org/abs/2610.42094)).
- **Scope extension:** The Potts theorem treats random regular graphs and lattice cubes or tori. Establishing comparably sharp mixing bounds for broader bounded-degree graph families, especially near the uniqueness threshold, would test how far the dichotomy principle extends ([Blanca et al.](https://arxiv.org/abs/2610.42059)).
- **Quantitative boundary:** Armstrong and Bou-Rabee establish existence of some `ε>0` in the sublinear variance exponent. Determining explicit admissible exponents or testing whether the exponent can be improved under stronger distributional assumptions would sharpen the result ([Armstrong & Bou-Rabee](https://arxiv.org/abs/2610.42124)).
- **Conditional arithmetic input:** El Kaouni's effective motivic estimates assume the specified conjectural L-function formalism, including the motivic Riemann hypothesis. A natural direction is to identify concrete families where these hypotheses can be verified or to weaken them for narrower equidistribution conclusions ([El Kaouni](https://arxiv.org/abs/2610.42022)).
- **Dimensional boundary:** Sampaio proves the metric multiplicity statement under a tangent-cone singular-locus condition and obtains the embedded invariant for dimensions at most four. Extending the criterion or finding examples in higher dimensions that test its necessity would clarify the boundary of the method ([Sampaio](https://arxiv.org/abs/2610.41954)).
- **Cohomological range:** Naef and Willwacher compute the odd graph cohomology in the bottom cohomological degree. Extending the computation to higher degrees could reveal whether the freeness phenomenon has a broader cohomological counterpart ([Naef & Willwacher](https://arxiv.org/abs/2610.41766)).

## Takeaway

This batch is unusually rich in papers claiming explicit conjecture resolutions or counterexamples, with several backed by proof-assistant artifacts, while probability and geometry supply methods that travel across mathematical settings. These are author-reported preprint claims; the ranking reflects concrete mathematical scope and cross-field connections, not an official or measured popularity list.

## Method and sources

- **Window and snapshot:** The latest arXiv Mathematics announcement batch available at 2026-11-03 01:20 UTC was Monday, 2 November 2026; the daily window is that batch (2 November only), not the UTC snapshot date.
- **Archive coverage:** Traversed the full `math` recent listing for the 2 November batch (`show=500`, 422 entries). The arXiv API supplied candidate version, timestamps, authors, categories, comments, and cross-lists. Ten selected abstract pages were verified directly; the nine reported papers are new submissions (`v1`), not revisions. Abstracts were the basis for summaries; the introduction and main-results text was additionally inspected for the top three: arXiv:2610.42094, 2610.42059, and 2610.40863. No proof was independently checked.
- **Inference:** arXiv provides no official trending chart. Semantic Scholar citation fields were queried but returned no usable records during this run; with these very recent submissions, citation momentum is therefore not a sound basis for ranking. Exact-title web searches mainly returned arXiv records and discovery mirrors, not corroborated seminar or independent expert discussion. The entries are consequently a curated list of notable recent papers, ordered by concrete stated results, cross-subfield reach, and checkable formal artifacts—not by readership, downloads, author reputation, or arXiv listing order.
- **Retrieval limitations:** The configured `web_extract` backend was search-only for these URLs; browser retrieval and the arXiv API were used instead. The Semantic Scholar batch request was rate-limited, so no citation counts are reported.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); [arXiv API](https://export.arxiv.org/api/query); individual abstract pages linked in each paper heading. Formal artifacts are linked from the relevant arXiv comments/abstracts.
