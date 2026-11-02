# arXiv Mathematics — daily batch, 2026-11-02

**Headline.** The Monday, 2 November 2026 announcement batch contains 422 Mathematics entries; this report selects seven notable papers, led by sharp results on Potts-model mixing, graph choosability, and random-media fluctuations. Agenda: first the sampling and coloring results, then two random-media estimates, followed by finite-field tiling, stochastic thin films, and multiparameter topology. This is an inferred ordering, not an official arXiv trending chart; very recent papers have little usable citation evidence, so it should not be read as measured popularity.

**Window and snapshot:** the 2026-11-02 arXiv announcement batch only (the latest batch, not a prior batch); first submissions below are dated 2026-10-30. Snapshot: 2026-11-02 17:23:24 UTC.

## Top papers (ranked)

### 1. [Rapid mixing of Potts Glauber dynamics throughout uniqueness](https://arxiv.org/abs/2610.42059)
- **Abstract:** The authors prove fast Potts Glauber mixing for every number of states throughout the high-temperature uniqueness regimes on random regular graphs and lattice cubes or tori, and also obtain logarithmic-time Swendsen–Wang mixing on random regular graphs.
- **Authors:** Antonio Blanca, Reza Gheissari, Heehyun Park, Xusheng Zhang
- **arXiv:** `2610.42059v1` (published 2026-10-30T17:20:57Z; categories: `math.PR`, `cs.DM`, `math-ph`)
- **Evidence for ranking:** The paper states quantitative bounds at the tree-uniqueness and lattice-critical thresholds and introduces a shattering–escape dichotomy for handling pinnings; the cross-listing connects probability, discrete mathematics, and mathematical physics. The introduction identifies the random-regular-graph result as resolving the stated open mixing question for the natural Glauber chain.
- **Claimed result:** In the paper’s Theorems 1.1–1.2, for fixed `q ≥ 2`, Glauber dynamics has `O(n(log n)^κ)` mixing time with high probability on uniformly random `Δ`-regular graphs when `β < β_u(q,T_Δ)`, and inverse spectral gap `n^(1+o(1))` on `d`-dimensional cubes or tori when `β < β_c(q,Z^d)`; the authors also claim `O(log n)` Swendsen–Wang mixing on random regular graphs throughout uniqueness.
- **Assumptions and setting:** Ferromagnetic `q`-state Potts model; the graph is sampled uniformly from simple `Δ`-regular graphs in the first result, while the second concerns cubes or tori in `Z^d`; the temperature is strictly below the stated threshold.
- **Caveat:** The random-regular-graph guarantee is high-probability for that graph ensemble, not for every bounded-degree graph. For the lattice result, the paper notes that the inverse-gap estimate gives a mixing bound of `n^(2+o(1))`, while the authors expect `O(n log n)` and do not prove it.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics; Mathematical physics

### 2. [A Counterexample to the Alon-Krivelevich Conjecture and a New Lower Bound for Choosability of Bipartite Graphs](https://arxiv.org/abs/2610.42094)
- **Abstract:** The authors construct bipartite graphs whose list-chromatic number grows asymptotically faster than the logarithm of maximum degree, disproving the Alon–Krivelevich conjecture.
- **Authors:** Junran Yu, Gexin Yu
- **arXiv:** `2610.42094v1` (published 2026-10-30T17:39:18Z; categories: `math.CO`)
- **Evidence for ranking:** The authors give an explicit family and a quantitative lower bound that contradicts a named conjecture; the abstract identifies a proof bridge using weighted counting, probability, and Brouwer’s fixed-point theorem. The introduction states the conjecture’s former logarithmic upper-bound form and the constructed family’s asymptotic separation.
- **Claimed result:** The authors prove that for integers `k ≥ 2` and `r² > 2(2k−1) ln(2k−1)`, their bipartite graph is not colorable from its standard lists, yielding `ch(G) ≥ (1/32−o(1))(ln Δ)²/(ln ln Δ)³` and hence `ch(G)/ln Δ → ∞` along the family.
- **Assumptions and setting:** Finite simple bipartite graphs; both vertex classes are copies of the `k`-subsets of a `(2k−1)`-element set, with adjacency defined by intersection size at most `r`; each vertex’s list is its corresponding subset.
- **Caveat:** The bound is a lower bound for the constructed family, not an asymptotic characterization of its true choosability; the authors explicitly note that the actual value may be larger.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 3. [Fluctuation bounds for rotationally invariant first-passage percolation](https://arxiv.org/abs/2610.42124)
- **Abstract:** For rotationally invariant continuum first-passage percolation in dimension at least two, the authors establish exponential concentration on a sub-square-root scale and infer a variance bound of order at most `n^(1−ε)`.
- **Authors:** Scott Armstrong, Ahmed Bou-Rabee
- **arXiv:** `2610.42124v1` (published 2026-10-30T17:54:21Z; categories: `math.PR`)
- **Evidence for ranking:** The introduction states that the result extends the planar variance saving to every dimension in the paper’s continuum setting and replaces a geodesic-chaos argument with translation averaging and a logarithmic Efron–Stein improvement; a Lean 4 formalization is linked in the arXiv comments.
- **Claimed result:** Theorem 1.1 gives constants `ε>0` and `C<∞` such that `E exp(|T(0,x)−μ|x||/(C|x|^(1/2(1−ε)))) ≤ 2` for every `|x|≥1` under the specified smoothed-Gaussian density; the paper’s Theorem 1.2 extends this to its stated general-density assumptions and implies `Var[T(0,x)] ≤ C'|x|^(1−ε)`.
- **Assumptions and setting:** Continuum first-passage percolation in `R^d`, `d≥2`; the general theorem assumes a measurable, uniformly positive and bounded, locally determined density equivariant under rigid motions, driven by Gaussian white noise or a homogeneous Poisson process.
- **Caveat:** This is not a solution of the lattice version of Kesten’s question: the introduction notes that the lattice question remains open, and its companion-paper observation requires a nondegenerate `C²,α` time-constant condition not known for any weight distribution.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Probability & statistics

### 4. [Tiling without a subspace complement: a sharp counterexample in dimension nine over the field with two elements](https://arxiv.org/abs/2610.42005)
- **Abstract:** The authors exhibit a 64-point subset of `F₂⁹` that tiles by translation but has no linear-subspace tiling complement, establishing a sharp dimension threshold for the existence of such complements.
- **Authors:** Samuel J. Ferguson, Joshua Iosevich
- **arXiv:** `2610.42005v1` (published 2026-10-30T16:45:42Z; categories: `math.CO`, `math.CA`)
- **Evidence for ranking:** The paper claims an explicit counterexample and complete classifications of its tiling complements and spectra; its cross-listing links finite combinatorics with classical analysis. The listing also notes ancillary Python verification scripts and data.
- **Claimed result:** The authors show that every nonempty translational tile in `F₂^d` has a linear-subspace complement exactly when `d≤8`; their dimension-nine example has 512 tiling complements and 64 spectra, each classification forming one translation class.
- **Assumptions and setting:** Finite vector spaces over `F₂`; “tiles” means unique translational factorizations of the whole group. The example is spectral, so it is not a counterexample to Fuglede’s conjecture.
- **Caveat:** The positive assertion in dimension eight for the remaining 16-point case relies on the authors’ earlier theorem based on classifying perfect binary codes of length fifteen; the present paper’s abstract and introduction flag that dependency.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Analysis & PDE

### 5. [Dirichlet form approach to stochastic thin-film equations](https://arxiv.org/abs/2610.42086)
- **Abstract:** The authors use Dirichlet-form methods to construct stochastic thin-film dynamics, prove existence and uniqueness of the evolution of laws, and establish tightness and convergence results for spatial discretizations.
- **Authors:** Benjamin Gess, Felix Otto, Max Sauerbrey
- **arXiv:** `2610.42086v1` (published 2026-10-30T17:37:08Z; categories: `math.PR`, `math.AP`, `math.NA`)
- **Evidence for ranking:** This is cross-listed in probability, PDE, and numerical analysis, and links continuum stochastic dynamics to Galerkin/spectral approximation through uniform tightness and Mosco convergence in the simplified setting.
- **Claimed result:** The authors establish existence and uniqueness for the law-valued evolution and regularity of process realizations; for a Gaussian reference measure and non-degenerate mobility they identify an energy solution, and prove uniform tightness of Galerkin and spectral approximations plus Mosco convergence in that simplified case.
- **Assumptions and setting:** An overdamped gradient-flow model of a thin liquid film with thermal noise. The Dirichlet-form construction uses a Gibbsian equilibrium measure; the paper treats the resulting `(1+1)`-dimensional setting.
- **Caveat:** The need for an available Gibbsian equilibrium measure limits the treatment to one spatial dimension; the energy-solution characterization and Mosco convergence are stated for a simplified Gaussian-reference, non-degenerate-mobility case.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Probability & statistics; Analysis & PDE; Numerical analysis & computation

### 6. [Landscape Intervals: A Geometric Framework for Multiparameter Persistence Landscapes](https://arxiv.org/abs/2610.42090)
- **Abstract:** The authors define landscape intervals and derive stable multiparameter persistence-landscape invariants that generalize existing one- and multiparameter constructions, with a numerical framework illustrated on mesh and medical-image data.
- **Authors:** Pan Fang, Washington Mio, Tom Needham
- **arXiv:** `2610.42090v1` (published 2026-10-30T17:38:12Z; categories: `math.AT`)
- **Evidence for ranking:** The paper provides exact identities with erosion distances, perturbation stability, and refined interleaving-stability bounds; it also links a topological invariant to numerical extraction and machine-learning pipelines.
- **Claimed result:** The authors prove that their two invariants recover Bubenik’s landscapes in the one-parameter case and encompass Vipond’s multiparameter landscapes, establish two exact erosion-distance identities and perturbation stability, and show finite-information recovery on a specified class of modules.
- **Assumptions and setting:** Persistence modules indexed by a multiparameter space; the finite-information recovery claim applies only to a certain class of modules, while the proposed numerical workflow is illustrated on surface meshes and medical images.
- **Caveat:** The abstract does not claim finite-information recovery for arbitrary multiparameter modules, and the data examples are illustrations rather than broad empirical validation.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Geometry & topology

### 7. [Maximum of the Two-Dimensional Directed Polymer in the Critical Window](https://arxiv.org/abs/2610.41989)
- **Abstract:** For a two-dimensional directed polymer in a Gaussian environment at critical-window inverse temperature, the authors prove that the maximum log partition function over a square of side order `√N`, divided by `√log N`, converges in probability to `2√2`.
- **Authors:** Clement Cosco, Shuta Nakajima, Ofer Zeitouni
- **arXiv:** `2610.41989v1` (published 2026-10-30T16:36:44Z; categories: `math.PR`)
- **Evidence for ranking:** The abstract states an explicit asymptotic constant for a spatial maximum in the critical regime. It is placed below the broader cross-area or conjecture-resolving results because the stated theorem is confined to one random-media model and no independent discussion surfaced in the sources checked.
- **Claimed result:** The authors prove that for every fixed real `ϑ`, with `β_N=√((1−ϑ/log N)/R_N)` and `R_N∼(log N)/π`, the maximum `𝔐_N` of `log Z_N(x)` over `|x|_∞≤√N` satisfies `𝔐_N/√(log N) → 2√2` in probability.
- **Assumptions and setting:** Two-dimensional lattice directed polymer, Gaussian environment, critical-window scaling as above, and the maximum over starting points in the specified box.
- **Caveat:** The result is a first-order in-probability asymptotic in this Gaussian two-dimensional scaling; it does not state a fluctuation law for the centered maximum or cover other environments and dimensions.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Probability & statistics

## Trending Research Themes

- **Sharp thresholds, bounds, and counterexamples:** Yu and Yu disprove a logarithmic choosability conjecture with a quantified lower bound, while Ferguson and Iosevich identify the exact dimension boundary for subspace tiling complements. These are distinct constructions, not evidence of a shared proof technique.
- **Random media and stochastic systems:** Armstrong and Bou-Rabee establish all-dimensional continuum first-passage concentration under rotational invariance, while Cosco, Nakajima, and Zeitouni quantify a critical-window spatial maximum for a 2D directed polymer. Gess, Otto, and Sauerbrey instead treat a stochastic PDE and its approximations; the three results concern different models and methods.
- **Sampling across statistical physics and algorithms:** Blanca et al. connect uniqueness thresholds to mixing guarantees for Potts Glauber and Swendsen–Wang dynamics, using a shattering–escape dichotomy. This is a substantial result in one paper, not a batch-wide shift by itself.
- **Topology made quantitative and computable:** Fang, Mio, and Needham connect multiparameter persistence landscapes to erosion distances, stability bounds, and a numerical workflow. This is an isolated signal in today’s selected set.

## Open Problems and Research Directions

- **Author-identified gap — sharper lattice mixing:** Blanca et al. expect `O(n log n)` Potts Glauber mixing on cubes and tori, but their inverse-spectral-gap estimate yields only `n^(2+o(1))` mixing; they point to a sharper log-Sobolev estimate as a missing ingredient. A direct route to that estimate would test the conjectured rate. [2610.42059]
- **Scope extension — Potts uniqueness:** The theorem covers random regular graphs with high probability and lattice cubes or tori, not arbitrary bounded-degree graphs. One possible follow-up is to determine whether the shattering–escape dichotomy can yield guarantees on broader graph families. This is a proposed extension, not a result claimed by the authors. [2610.42059]
- **Author-acknowledged quantitative gap — choosability:** Yu and Yu note that their lower bound need not equal the true choosability of their constructed graphs. Improving upper bounds for that family, or narrowing the gap between its actual value and the proved lower bound, would sharpen the counterexample. [2610.42094]
- **Author-identified dependency — dimension eight tilings:** The remaining 16-point case in the dimension-eight positive assertion uses the authors’ earlier result based on perfect binary codes of length fifteen. A self-contained or structurally different proof of that case would remove the stated dependency. [2610.42005]
- **Author-identified dimensional limitation — stochastic thin films:** The available Gibbsian equilibrium measure restricts the Dirichlet-form treatment to one spatial dimension. Developing a higher-dimensional construction without that measure is a natural direction, but the present paper does not establish that such an extension is available. [2610.42086]
- **Proposed generalization — landscape intervals:** Since finite-information recovery is proved only for a certain class of modules, characterize larger classes where it holds and test how the numerical invariants behave under controlled perturbations of mesh and imaging data. [2610.42090]
- **Proposed asymptotic refinement — directed polymers:** The theorem gives a first-order limit for the maximum, not its centered fluctuations. Determining a fluctuation scale or limiting law in the same critical Gaussian setting would refine the reported result; this is a suggested direction, not an open problem explicitly stated in the abstract. [2610.41989]

## Takeaway

Today’s strongest selected signals are theorem-level: a new mixing method at uniqueness thresholds, a counterexample to a graph-coloring conjecture, and improved continuum first-passage concentration. They sit beside concrete advances in finite-group tilings, stochastic PDEs, persistence invariants, and directed polymers, but the batch is too fresh—and attention metrics too sparse—to infer a broader popularity shift.

## Method and sources

- **Window:** the latest arXiv Mathematics announcement batch dated 2026-11-02, not a prior batch; exact batch count 422, as shown by the recent-list heading. All selected entries are new submissions in this batch, first submitted on 2026-10-30. Snapshot time: 2026-11-02 17:23:24 UTC.
- **Coverage:** traversed the full 422-entry batch at [arXiv Mathematics recent submissions](https://arxiv.org/list/math/recent?show=500); selected seven candidates and verified each version, author list, submitted date, abstract, and categories on its arXiv abstract page. The arXiv Atom API was used to check structured metadata. The first three papers’ arXiv HTML versions were also inspected for introductions and main theorem statements; no proof verification was performed.
- **Inference:** arXiv provides no official trending chart. The ordering uses concrete claimed results, cross-list relevance, mathematical setting, linked formalization/data where applicable, and limited search for independent discussion. It is therefore a notable-paper selection, not a readership or download ranking.
- **Attention evidence:** same-day papers have little time to accumulate citation signals; no independent seminar or expert discussion for the selected papers surfaced in the searches checked. Semantic Scholar citation metrics could not be obtained for this snapshot, so citation totals and age-normalized citation momentum are omitted.
- **Retrieval note:** the configured web-extraction backend was search-only, so arXiv abstract pages were verified with the browser and metadata with the Atom API instead. Search results were checked for independent discussion and corroborating context; arXiv pages were used as the source of record.
- **Sources:** arXiv recent listing above; the seven canonical abstract URLs linked in the paper titles; HTML introductions/main results for [2610.42059](https://arxiv.org/html/2610.42059v1), [2610.42094](https://arxiv.org/html/2610.42094v1), and [2610.42124](https://arxiv.org/html/2610.42124v1); and web searches for the candidate titles and conjectures.
