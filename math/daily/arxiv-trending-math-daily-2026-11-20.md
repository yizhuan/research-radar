# arXiv Mathematics — daily research snapshot, 2026-11-20

## Headline

Latest available announcement batch: Friday, 20 November 2026 (the Saturday snapshot uses this prior batch). Eleven notable papers selected from 405 entries stand out, especially sharp estimates and exact results that settle or narrow named conjectures; the agenda runs from Fourier analysis and topological overlap to hypergraph thresholds, representation theory, and percolation. This is an inferred shortlist, not an official arXiv trending chart; citation and independent-attention evidence is limited for papers this recent, so the ordering reflects mathematical claims and scope rather than measured popularity.

## Top papers (ranked)

### 1. [Amplitude dependent wave envelope type estimates for moment curves and applications](https://arxiv.org/abs/2611.26581)
- **Abstract:** The authors prove amplitude-dependent wave-envelope estimates for moment curves in arbitrary dimensions and use them to establish sharp small-cap decoupling inequalities for dimensions `n≥4`, resolving the Demeter–Guth–Wang exponential-sum conjecture in all dimensions.
- **Authors:** Sangwon Jeong, Changkeun Oh
- **arXiv:** `2611.26581v1` (published 2026-11-19 18:43:18 UTC; categories: `math.CA`)
- **Evidence for ranking:** The abstract claims sharp small-cap decoupling in every dimension `n≥4` and completion of a named conjecture on exponential sums; this is a specific, consequential result signal, not an attention metric.
- **Claimed result:** The authors prove amplitude-dependent wave-envelope estimates for moment curves and derive sharp small-cap decoupling for the moment curve in every dimension `n≥4`.
- **Assumptions and setting:** Fourier restriction/decoupling for moment curves; the new sharp small-cap conclusion is for dimensions `n≥4` and uses prior sharp square-function estimates by Maldague and Guth–Maldague.
- **Caveat:** The result concerns the moment curve, not general manifolds; the paper builds on those prior square-function estimates, and this summary has not independently checked the proof.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Analysis & PDE

### 2. [Sharp topological overlap in every dimension](https://arxiv.org/abs/2611.26229)
- **Abstract:** The author determines the asymptotic topological and affine overlap constants for maps of high-dimensional simplices into `R^d`, obtaining the same exact value in every dimension.
- **Authors:** Sergey Norin
- **arXiv:** `2611.26229v1` (published 2026-11-19 15:04:17 UTC; categories: `math.CO`, `cs.CG`)
- **Evidence for ranking:** The paper gives an exact all-dimensional constant and confirms the Bukh–Matoušek–Nivasch conjecture; its combinatorics/computational-geometry cross-listing corroborates scope, while no popularity claim is made.
- **Claimed result:** The author proves `c_d^top = c_d^aff = (d+1)!/(d+1)^(d+1)` for every integer `d≥1`, confirming the conjectured affine value and matching it with the topological constant.
- **Assumptions and setting:** As `n→∞`, for continuous or affine maps from the `n`-simplex to `R^d`, some point lies in the images of at least `(c−o(1)) binom(n+1,d+1)` of the `d`-faces.
- **Caveat:** The abstract says the proof was found by GPT-6 Astra following the author's directions; it remains a preprint claim and has not been independently or formally verified here.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 3. [Hypergraph Hajnal-Szemerédi](https://arxiv.org/abs/2611.26513)
- **Abstract:** The authors improve the minimum-codegree sufficient condition for a perfect clique-factor in uniform hypergraphs, bringing it closer to the known codegree Turán lower bound.
- **Authors:** Michelle Delcourt, Cicely Henderson, Thomas Lesgourgues, Luke Postle
- **arXiv:** `2611.26513v1` (published 2026-11-19 17:58:38 UTC; categories: `math.CO`)
- **Evidence for ranking:** The authors give a concrete improvement to a long-standing general threshold problem and connect it to the known Turán obstruction; the paper also reports a fractional-threshold result and an independent-set lemma.
- **Claimed result:** The preprint proves that for each `r≥3` there is `c>0` such that, for `q>r` and sufficiently large `n` divisible by `q`, codegree at least `(1−c log^{1−1/(r−1)}(q)/q^(r−1))n` guarantees a `K_q^r`-factor.
- **Assumptions and setting:** `G` is an `r`-uniform hypergraph; the theorem assumes `r≥3`, `q>r`, `q|n`, and sufficiently large `n`. The bound is sufficient, not asserted to be exact.
- **Caveat:** The exact threshold remains open: the paper says its upper and lower bounds differ by a factor of order `log^{1/(r−1)} q`; its suggested matching threshold is conjectural, not proved here.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Combinatorics & discrete mathematics

### 4. [A proof of Casselman's comparison conjecture](https://arxiv.org/abs/2611.25367)
- **Abstract:** The paper compares nilradical homology and related derived functors for the Harish–Chandra module of a representation and its smooth globalization.
- **Authors:** Junyan Xiao, Jun Yu
- **arXiv:** `2611.25367v1` (published 2026-11-19 02:04:10 UTC; categories: `math.RT`)
- **Evidence for ranking:** The authors claim a proof of a named comparison conjecture across standard parabolics, with additional Tor/Ext and closed-image statements; the introduction identifies the broader conjectural context.
- **Claimed result:** For a real linear reductive group, standard parabolic `Q=LU`, Casselman–Wallach representation `π`, and every `i≥0`, the inclusion of `K`-finite vectors induces a topological `L`-equivariant isomorphism between the globalization of `H_i(u,π_K)` and `H_i(u,π)`; the authors also prove stated Tor/Ext comparisons for augmentation quotients.
- **Assumptions and setting:** Real linear reductive groups, standard parabolic subgroups, Casselman–Wallach representations, and associated Lie-algebra homology/cohomology and topological modules.
- **Caveat:** The theorem has this specified real-group and smooth-globalization scope; it does not by itself settle every comparison problem for other canonical globalizations.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Algebra & number theory

### 5. [On Romik's rationality conjectures for critical percolation](https://arxiv.org/abs/2611.26570)
- **Abstract:** For nested boundary-connection events in the critical-percolation `O(1)` loop model, the authors derive Pfaffian formulas and rationality in the cylinder and half-plane limits.
- **Authors:** Melda Akyazi-Zavadski, Nathanaël Berestycki, Sunil Chhita
- **arXiv:** `2611.26570v1` (published 2026-11-19 18:36:31 UTC; categories: `math.PR`, `math-ph`, `math.CO`)
- **Evidence for ranking:** The result is cross-listed across probability, mathematical physics, and combinatorics and proves a precise part of a named conjecture using an explicit bridge through plane partitions, dimers, and Pfaffians.
- **Claimed result:** The authors show that probabilities of `k` nested arches are rational functions of cylinder circumference for `N>k` and rational in the half-plane limit, establishing key aspects of Romik's conjectures.
- **Assumptions and setting:** Completely packed `O(1)` loops representing critical square-lattice bond percolation; fixed `k` nested-arch events on a semi-infinite cylinder of circumference `2N`, with `N>k`, and the infinite-circumference half-plane limit.
- **Caveat:** The proof covers nested-arch events, not all boundary submatchings; the predicted denominator and numerator structure, dyadic rationality, and boundary case `N=k` remain unresolved in the paper.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Probability & statistics; Mathematical physics; Combinatorics & discrete mathematics

### 6. [The existence of generalized Steiner systems](https://arxiv.org/abs/2611.26226)
- **Abstract:** The authors prove eventual existence of generalized `q`-ary Steiner systems at the Johnson-type bound for fixed parameters whenever the necessary divisibility conditions hold.
- **Authors:** Xuan Wang, Shitao Li, Minjia Shi
- **arXiv:** `2611.26226v1` (published 2026-11-19 15:02:21 UTC; categories: `math.CO`)
- **Evidence for ranking:** The abstract explicitly answers an existence question posed after a 2025 asymptotic result, upgrading asymptotic attainment to exact attainment for all sufficiently large admissible lengths.
- **Claimed result:** For fixed `q≥3` and `w>t≥1`, the authors prove a `GS(t,w,n,q)` exists for every sufficiently large `n` satisfying the stated divisibility conditions; distinct codeword supports can be chosen to intersect in at most `t` coordinates.
- **Assumptions and setting:** Fixed integer parameters `q≥3` and `w>t≥1`; `n` is sufficiently large and satisfies `binom(w−i,t−i) | (q−1)^(t−i) binom(n−i,t−i)` for each `0≤i<t`.
- **Caveat:** The abstract gives an eventual-existence theorem, not an explicit effective threshold for `n` or a practical construction algorithm.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Combinatorics & discrete mathematics

### 7. [Dynamical edge universality and the Airy$_β$ line ensemble](https://arxiv.org/abs/2611.25364)
- **Abstract:** The authors prove convergence of rescaled edge trajectories to the Airy$_β$ line ensemble for three families of interacting-particle systems from general non-equilibrium initial data under a regular-edge condition.
- **Authors:** Jiaoyang Huang, Shengjing Xu, Yulei Xu
- **arXiv:** `2611.25364v1` (published 2026-11-19 02:02:08 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** It treats three model families and every `β>0`, and is cross-listed in probability and mathematical physics; the abstract states a multi-time convergence claim rather than a single-time limit.
- **Claimed result:** For each fixed `k`, after the stated edge and time rescalings, the top `k` particle trajectories converge jointly in distribution to the top `k` curves of the Airy$_β$ line ensemble.
- **Assumptions and setting:** `β`-Dyson Brownian motion with analytic potential, weighted `β`-corners processes, and a class of discrete-time Markov chains; general non-equilibrium initial data and a regular square-root limiting-density edge.
- **Caveat:** The theorem is limited to the three model classes and regular square-root edges described; it does not assert universality at singular edges or for arbitrary interacting systems.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Probability & statistics; Mathematical physics

### 8. [Proof of Stanley's Conjecture on the Leading Ehrhart Coefficients of the Birkhoff Polytope](https://arxiv.org/abs/2611.25973)
- **Abstract:** For each fixed nonnegative `k`, the authors establish the asymptotic ratio of the coefficient `c(n,k)` to the leading Ehrhart coefficient of the `n×n` Birkhoff polytope, confirming Stanley's conjecture.
- **Authors:** Jiahang Liu, Jinlong Tang
- **arXiv:** `2611.25973v1` (published 2026-11-19 11:56:24 UTC; categories: `math.CO`)
- **Evidence for ranking:** A precise conjecture confirmation with an explicit asymptotic formula makes this a checkable result signal rather than a title-only claim.
- **Claimed result:** The authors prove `c(n,k)/c(n,0) ~ n^(3k)/(2^k k!)` as `n→∞` for every fixed nonnegative integer `k`.
- **Assumptions and setting:** Ehrhart polynomial of the `n×n` Birkhoff polytope; `k` is fixed while `n` tends to infinity.
- **Caveat:** This is a fixed-`k` asymptotic statement, not an exact formula for finite `n` or a result uniform over growing `k`.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Combinatorics & discrete mathematics

### 9. [The rational points of the non-split Cartan modular curve of level 121](https://arxiv.org/abs/2611.25183)
- **Abstract:** The author determines all rational points on the genus-511 level-121 non-split Cartan modular curve and relates this case to Galois images of non-CM elliptic curves over `Q`.
- **Authors:** Manvir Jaswal
- **arXiv:** `2611.25183v1` (published 2026-11-18 21:07:06 UTC; categories: `math.NT`, `math.AG`)
- **Evidence for ranking:** The paper cross-lists number theory and algebraic geometry and reports an exact rational-point classification for a high-genus curve, addressing a specified level case of a published conjecture.
- **Claimed result:** The author claims that `X_ns^+(121)` has exactly seven rational points, all CM; together with the cited theorem of Rouse, Sutherland, and Zureick-Brown, this determines the 11-adic Galois images for non-CM elliptic curves over `Q`.
- **Assumptions and setting:** Rational points on the normalizer of a non-split Cartan modular curve at level `121`, of genus `511`; the Galois-image consequence is for non-CM elliptic curves over `Q`.
- **Caveat:** The result resolves the level-121 case only; it relies on specialized quadratic-Chabauty and Hecke-intersection arguments and does not classify all levels.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Algebra & number theory; Geometry & topology

### 10. [Infinitely Many Plasma Echo Cascades and Sobolev Norm Divergence at the Gevrey-3 Threshold](https://arxiv.org/abs/2611.25540)
- **Abstract:** The author constructs a global confined Vlasov–Poisson solution with infinitely many nonlinear plasma-echo cascades, producing Sobolev norm divergence despite decay of macroscopic fields.
- **Authors:** Yue Luo
- **arXiv:** `2611.25540v1` (published 2026-11-19 05:43:52 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract describes a constructed instability at a stated critical regularity scale, while also specifying scattering and field decay, making the contrast mathematically concrete.
- **Claimed result:** Near a fixed homogeneous Penrose-stable equilibrium, for every sufficiently small `ε`, the author constructs a real, neutral global solution with nonnegative distribution, initial size `O(ε)` in Gevrey-3 radius `λ₀≈ε^(1/3)`, and `||f(t)||_{H^1000_{z,v}}→∞` as `t→∞`, although the kinetic profile scatters in a lower Sobolev topology and density and electric field decay.
- **Assumptions and setting:** Confined Vlasov–Poisson system near a fixed homogeneous Penrose-stable equilibrium; small perturbations at the amplitude-dependent Gevrey-3 radius specified in the abstract.
- **Caveat:** This is a constructed solution in a particular confined model and norm; it does not establish the same instability for general equilibria or Vlasov–Poisson settings.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Analysis & PDE

### 11. [Permanence and 144-periodicity of $x_{153,3}$ in the stable stems at the prime three](https://arxiv.org/abs/2611.26621)
- **Abstract:** The author shows that a specified class in the 3-primary Adams–Novikov spectral sequence survives and generates a period-144 family in stable homotopy, answering a question of Carrick and Davies.
- **Authors:** Zheyan Wan
- **arXiv:** `2611.26621v1` (published 2026-11-19 18:58:55 UTC; categories: `math.AT`)
- **Evidence for ranking:** The result directly answers both parts of a named question and identifies a periodic family, a concrete signal within algebraic topology rather than evidence of broad attention.
- **Claimed result:** The author proves permanence of `x_{153,3}` and the existence of a period-144 family, with iterates detected nontrivially at height two.
- **Assumptions and setting:** The 3-primary Adams–Novikov spectral sequence of the sphere; the class is in stable degree 153 and filtration 3.
- **Caveat:** This establishes a family from one specified class at the prime three; it does not imply periodicity for other classes or primes.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Geometry & topology

## Trending Research Themes

- **Sharp estimates and extremal structure:** The moment-curve decoupling theorem (1), exact overlap constant (2), and hypergraph factor threshold (3) each sharpen a frontier, but by different methods; this is a cluster of results, not evidence of a shared technique.
- **Conjecture-oriented combinatorics:** Hypergraph clique factors (3), generalized Steiner systems (6), and Ehrhart coefficients of the Birkhoff polytope (8) all translate structural constraints into existence or asymptotic theorems. The specific problems and proof methods differ.
- **Probability and mathematical physics at two scales:** The percolation paper (5) uses exact enumeration/Pfaffian structure for finite boundary events and their limit; the edge-universality paper (7) proves multi-time scaling limits for interacting particles. Both bridge probability and mathematical physics, but their techniques are distinct.
- **Other isolated signals:** Casselman's globalization comparison (4), the modular-curve classification (9), the plasma-echo construction (10), and the stable-stem family (11) are substantial results in different specialties; this single batch does not establish broader field-wide shifts.

## Open Problems and Research Directions

- **Open problem (authors, paper 3):** The hypergraph-factor upper bound remains within a factor of order `log^{1/(r−1)} q` of the lower-bound scale. The authors suggest a sharper matching threshold and note that analogous minimum `d`-degree thresholds remain to be studied.
- **Open problems (authors, paper 5):** The prescribed numerator/denominator in the cylinder conjecture and dyadic rationality in the half-plane remain unproved for nested arches; the boundary case `N=k` is not covered. The paper also gives conjectures for extending the rational-function identity to that boundary and for the exact dyadic denominator.
- **Research direction (synthesis, papers 3 and 6):** For hypergraph factors, pursue sharper lower bounds or constructions that close the logarithmic gap; for generalized Steiner systems, seek effective bounds on the first admissible `n` and more explicit constructions. These would test the limits of the stated asymptotic existence theorems.
- **Research direction (synthesis, paper 7):** Test whether the Airy$_β$ trajectory limit persists at non-regular or singular edges, or in additional particle-system classes; the current result assumes a regular square-root edge.
- **Research direction (synthesis, paper 8):** Determine whether Stanley's fixed-`k` coefficient asymptotic admits controlled lower-order terms or a range where `k` grows with `n`; neither is claimed in the abstract.

## Takeaway

This batch has several unusually concrete author-claimed results: an all-dimensional decoupling conjecture resolution, an exact topological-overlap constant, and a substantially sharper hypergraph-factor threshold. These are mathematical-significance signals, not measurements of reader attention; citation and independent-discussion evidence remains too sparse for a popularity ranking.

## Method and sources

- **Window:** Daily; selected batch date 2026-11-20, start 2026-11-20 and end 2026-11-20. This is the prior announcement batch available at the snapshot: Saturday 2026-11-21, with Friday 2026-11-20 the newest batch on the Mathematics recent listing.
- **Snapshot:** 2026-11-21 17:25:12 UTC.
- **Coverage:** Full first Mathematics recent-listing batch (405 entries) traversed; arXiv `math.*` categories retained, with neighboring-category papers included only when cross-listed in `math.*`. Abstract pages were checked for all eleven selected papers. Introduction/main-results sections were inspected for the first three.
- **Inference:** arXiv supplies no official trending chart. Recent submissions provide little time for citation momentum; the ordering prioritizes concrete conjecture/threshold claims, breadth of mathematical relevance, and cross-listing where applicable, with recency only as context. Search results did not verify independent expert/seminar discussion for the selected set. The Semantic Scholar citation batch returned no usable records, so no citation totals are reported. The configured generic page-extraction backend was unavailable; official arXiv pages were retrieved directly.
- **Sources:** [Mathematics recent listing](https://arxiv.org/list/math/recent); [moment-curve estimates](https://arxiv.org/abs/2611.26581); [topological overlap](https://arxiv.org/abs/2611.26229); [hypergraph Hajnal-Szemerédi](https://arxiv.org/abs/2611.26513); [Casselman comparison](https://arxiv.org/abs/2611.25367); [Romik/percolation](https://arxiv.org/abs/2611.26570); [generalized Steiner systems](https://arxiv.org/abs/2611.26226); [dynamical edge universality](https://arxiv.org/abs/2611.25364); [Stanley's conjecture](https://arxiv.org/abs/2611.25973); [level-121 modular curve](https://arxiv.org/abs/2611.25183); [plasma echoes](https://arxiv.org/abs/2611.25540); [stable stems](https://arxiv.org/abs/2611.26621).
