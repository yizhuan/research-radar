# arXiv Trending Math — daily | 2026-10-23

Today's Mathematics announcement batch contains 390 listings; these eight notable picks lean toward explicit combinatorial bounds and classifications, alongside a critical stochastic-PDE construction. Spoken agenda: a thrackle bound, random media, finite structures, and one unusually bold number-theory claim. arXiv publishes no official trending chart, so this is an inferred ordering rather than a popularity ranking; the papers are very recent, and Semantic Scholar currently shows zero citations and zero influential citations for all eight, leaving little citation-based attention evidence.

## Top papers (ranked)

### 1. [Conway's thrackle conjecture: a new upper bound of $\frac43n$](https://arxiv.org/abs/2610.31589)
- **Abstract:** The paper proves that every thrackle on $n\ge4$ vertices has at most $\lfloor4(n-1)/3\rfloor$ edges, using a small-instance computer-assisted result and a discharging argument.
- **Authors:** Dániel Gábor Simon
- **arXiv:** `2610.31589v1` (published 2026-10-22 17:23:50 UTC; categories: `math.CO`, `math.GN`, `math.GT`)
- **Evidence for ranking:** The introduction compares this bound with the previous $18/13(n-1)$ bound; the result spans three mathematical categories and combines a previously established finite verification with a new embedding/discharging argument.
- **Claimed result:** The author proves $m\le\lfloor4(n-1)/3\rfloor$ for every thrackleable graph with $n\ge4$; the original $m\le n$ conjecture remains unresolved.
- **Assumptions and setting:** Finite simple graphs drawn in the plane so every pair of edges meets exactly once, at a shared endpoint or a proper crossing.
- **Caveat:** This is an improved upper bound, not a proof or disproof of Conway's conjectured $m\le n$ bound; the proof uses Pammer's computer-assisted verification for at most 12 vertices.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 2. [The Critical 2D KPZ Process](https://arxiv.org/abs/2610.31614)
- **Abstract:** The authors construct a non-Gaussian, distribution-valued critical two-dimensional KPZ process as a limit of centred Gaussian-directed-polymer log partition functions and of a renormalised logarithm of the critical stochastic heat flow.
- **Authors:** Quentin Berger, Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, et al.
- **arXiv:** `2610.31614v1` (published 2026-10-22 17:40:36 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** The paper cross-lists probability and mathematical physics and states a concrete common limiting process for two regularisation routes, with additional local covariance and non-Gaussianity results in the main text.
- **Claimed result:** The authors prove convergence in local negative Sobolev spaces, jointly at finitely many positive times and bounded continuous initial conditions, both from critically tuned Gaussian polymer partition functions and from regularised log-SHF; they also identify a log-log covariance singularity and Gaussian small-scale averages.
- **Assumptions and setting:** Two spatial dimensions, critical tuning, Gaussian disorder for the polymer approximation, and initial data in $L^\infty(\mathbb R^2)\cap C(\mathbb R^2)$.
- **Caveat:** The theorem is for the stated critical constructions, not a universality result for arbitrary disorder. The authors disclose extensive generative-AI assistance; the manuscript still needs independent expert scrutiny. The noise-mollified SHE limit is described by the authors as expected, with technical adaptations omitted.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Probability & statistics; Mathematical physics

### 3. [Positive sectional curvature on exotic spheres in infinitely many dimensions](https://arxiv.org/abs/2610.31528)
- **Abstract:** The author constructs exotic spheres with strictly positive sectional curvature in every dimension $n\equiv3\pmod4$, $n\ge11$, except dimensions congruent to 255 modulo 256.
- **Authors:** Fernando Galaz-García
- **arXiv:** `2610.31528v1` (published 2026-10-22 16:36:34 UTC; categories: `math.DG`)
- **Evidence for ranking:** The result gives an infinite family beyond the previously known high-dimensional examples described in the introduction; the paper links computation programs and outputs in a Zenodo archive.
- **Claimed result:** For the specified family of $S^3$-bundle quotient homotopy spheres, the author computes the Eells–Kuiper invariant and finds maps yielding nonzero invariant, which implies exotic smooth structure; the positive-curvature metric comes from the compatible-disk construction cited in the paper.
- **Assumptions and setting:** Spheres of dimension $4b+3$ arising from the representation of $S^3$ on $\mathbb R^3\oplus\mathbb H^b$, for $b\ge2$; the nonvanishing argument covers $b\not\equiv63\pmod{64}$.
- **Caveat:** The general theorem leaves the congruence class $b\equiv63\pmod{64}$ untreated; a computer calculation only reports additional dimensions in that class below $2^{16}$.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Geometry & topology

### 4. [Fuglede's conjecture holds in $\mathbb{F}_{p}^{d}$ for $p=2,\,d=8$ and $p=11,\,d=3$](https://arxiv.org/abs/2610.30712)
- **Abstract:** The authors prove the finite-field Fuglede conjecture in $\mathbb F_2^8$ and $\mathbb F_{11}^3$, and derive further structural results and reductions in $\mathbb F_2^9$.
- **Authors:** Samuel J. Ferguson, Joshua Iosevich
- **arXiv:** `2610.30712v1` (published 2026-10-22 04:30:10 UTC; categories: `math.CO`)
- **Evidence for ranking:** It settles two specific cases of a major tiling/spectral-set conjecture, pushes structural results into dimension nine, and supplies appendices describing exact computations and verification programs.
- **Claimed result:** The authors show tiling and spectrality are equivalent for nonempty sets in $\mathbb F_2^8$ and $\mathbb F_{11}^3$; in $\mathbb F_2^9$ every tile is spectral, every spectral set has power-of-two size, and all spectral cardinalities except 64 are shown to tile.
- **Assumptions and setting:** Finite vector spaces over prime fields, with “spectral” meaning that the set admits an orthogonal character basis and “tiles” meaning it tiles by translation.
- **Caveat:** The dimension-nine argument leaves spectral cardinality 64 unresolved; the authors provide reductions rather than a full resolution there.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Combinatorics & discrete mathematics

### 5. [Deep holes of full-length Reed--Solomon codes: uniform bounds and exact classifications](https://arxiv.org/abs/2610.31460)
- **Abstract:** The author classifies deep holes for specified interpolation-degree offsets over all finite fields, and proves uniform nonexistence/classification bounds for larger offsets under stated field-size conditions.
- **Authors:** Xiang Fan
- **arXiv:** `2610.31460v1` (published 2026-10-22 15:53:11 UTC; categories: `cs.IT`, `math.CO`, `math.NT`)
- **Evidence for ranking:** The paper cross-lists coding theory, combinatorics, and number theory; it gives exact cases for offsets 3–7 and provides certificates and deterministic verification programs for remaining finite cases.
- **Claimed result:** For full-length $\operatorname{RS}_q(k)$ and interpolation degree $k+m$, all cases $m=3,4,5,6,7$ are classified over every finite field; for general $m\ge3$, if $\sqrt q\ge12(m+1)\log(2m+2)$, the author rules out deep holes when $q$ is odd, or $k\ge3$, or $m$ is odd; if $q>16(m+2)^4$, the paper gives a complete classification at every admissible $k$.
- **Assumptions and setting:** Received words for the full-length Reed–Solomon code over a finite field; the classification depends on $m$, field size $q$, dimension $k$, and characteristic, with explicit characteristic-two exceptions at $m=4,6$.
- **Caveat:** The uniform bounds require large fields, and the exact exceptional families in small characteristic are part of the statement; the result does not erase those cases.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 6. [Upper tail large deviations of regular subgraph counts in sparse random regular graphs](https://arxiv.org/abs/2610.31590)
- **Abstract:** The authors determine upper-tail large-deviation rates for regular-subgraph counts in sparse random regular graphs across two regimes and describe the conditioned graph structure in key cases.
- **Authors:** Anirban Basak, Shaibal Karmakar
- **arXiv:** `2610.31590v1` (published 2026-10-22 17:24:21 UTC; categories: `math.PR`, `math.CO`)
- **Evidence for ranking:** The paper bridges probability and graph combinatorics, distinguishes the cycle case from higher-degree regular patterns, and identifies typical structures under the rare event rather than giving only a rate.
- **Claimed result:** For connected $\Delta$-regular $H$, the authors obtain speeds and rate functions for copies of $H$ in $\mathbb G_n^d$ when $p=d/n\ll1$ and $np^{\Delta/2}\gg(\log n)^{1/(v_H-2)}$; for $\Delta\ge3$ these match Erdős–Rényi, while for cycles the rate function differs. They also establish matching Erdős–Rényi rates in a complementary sparse regime for strictly balanced graphs.
- **Assumptions and setting:** Random $d$-regular graphs, sparse edge density, and the explicit asymptotic regimes in the abstract; conditioned-structure claims concern the corresponding upper-tail events.
- **Caveat:** The conclusions are regime-specific; cycle counts behave differently from the $\Delta\ge3$ case, and the paper does not claim one rate formula across all densities.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics

### 7. [A new lower bound for the sixth Schur number: $S(6)\ge 537$](https://arxiv.org/abs/2610.31362)
- **Abstract:** The authors give an explicit partition of $\{1,\ldots,537\}$ into six sum-free sets, improving the known lower bound for the sixth Schur number by one.
- **Authors:** Zhiyang Chen, Ligeng Zhu, Fan Long
- **arXiv:** `2610.31362v1` (published 2026-10-22 14:40:14 UTC; categories: `math.CO`, `cs.DM`)
- **Evidence for ranking:** The paper improves a published benchmark dating to 2000, reports 131 inequivalent partitions, and includes the explicit witness data and a verification script.
- **Claimed result:** The authors establish $S(6)\ge537$ and use known recursive constructions to obtain improved lower bounds $S(8)\ge5{,}372$, $S(11)\ge204{,}208$, $S(13)\ge2{,}042{,}082$, and $R_6(3)\ge539$.
- **Assumptions and setting:** Schur numbers concern partitions of initial positive integers into sum-free color classes; the paper supplies explicit finite partitions rather than an exact value for $S(6)$.
- **Caveat:** This is a lower-bound improvement, not a determination of the sixth Schur number; the reported searches do not establish that the listed partitions exhaust all possibilities.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Combinatorics & discrete mathematics

### 8. [An explicit elementary proof of no Landau--Siegel zeros](https://arxiv.org/abs/2610.30476)
- **Abstract:** The author claims an explicit lower bound $(1-\beta)\log q>1/100$ for every real zero $\beta$ of a primitive quadratic Dirichlet $L$-function of conductor $q\ge3$.
- **Authors:** Victor Zhenyu Guo
- **arXiv:** `2610.30476v1` (published 2026-10-21 21:48:17 UTC; categories: `math.NT`)
- **Evidence for ranking:** The stated uniform, explicit zero-free claim would be highly consequential if correct, so it is included as a high-interest claim to scrutinize; the evidence is the precise theorem statement, not observed attention or independent confirmation.
- **Claimed result:** The author asserts that every real zero $\beta\in(0,1)$ for every primitive quadratic Dirichlet character $\chi$ of conductor $q\ge3$ satisfies $(1-\beta)\log q>0.01$.
- **Assumptions and setting:** Real zeros of Dirichlet $L(s,\chi)$ for primitive quadratic characters, with no conductor exception beyond $q\ge3$ according to the abstract.
- **Caveat:** This is an exceptionally strong, unrefereed preprint claim with no journal reference in the arXiv record; neither its proof nor independent expert validation was checked here, so it should not be treated as established.
- **Announcement type:** new submission, announcement-batch date 2026-10-23
- **Themes:** Algebra & number theory

## Trending Research Themes

- **Explicit witnesses, finite classifications, and sharp bounds recur across discrete mathematics.** The thrackle paper combines a finite computer-assisted check with discharging; the Schur paper supplies a new partition witness; the Fuglede and Reed–Solomon papers combine classification arguments with finite-case certificates. These are related proof strategies, not a single shared algorithm or a field-wide shift.
- **Probability papers connect rare-event geometry and critical continuum limits.** The random-regular-graph paper describes both large-deviation rates and conditioned graph structure, while the KPZ paper constructs a critical random distribution from polymer and stochastic-heat-flow approximations. The objects and techniques differ; the common theme is extracting limiting or conditioned structure, not a common proof method.
- **Positive curvature on exotic spheres is a strong but isolated geometry signal in this selected set.** The result extends a specific family of positively curved examples to infinitely many dimensions; the remaining congruence class is not resolved by the general argument.
- **The number-theory item is an isolated, potentially major claim rather than evidence of a trend.** Its explicit zero bound warrants independent checking before drawing mathematical conclusions.

## Open Problems and Research Directions

- **Open problem (stated in the paper):** Conway's thrackle conjecture still asks whether every thrackle has at most as many edges as vertices. A follow-up could test whether the discharging constraints can be strengthened beyond the new $4/3$ coefficient or identify extremal families that obstruct this. [2610.31589]
- **Open gap (stated by the authors):** The KPZ manuscript expects, but omits for brevity, technical adaptations for convergence from the noise-mollified SHE approximation. A concrete direction is to establish that version and test which parts persist beyond Gaussian disorder or under broader initial-data assumptions. [2610.31614]
- **Open case (stated in the abstract):** In $\mathbb F_2^9$, spectral cardinality 64 remains unresolved for the tiling implication. One direct next step is to settle that finite case using the reductions and verification machinery in the paper. [2610.30712]
- **Open range within the construction:** The positive-curvature exotic-sphere argument does not cover $b\equiv63\pmod{64}$, apart from a finite computer calculation below $2^{16}$. Extending the invariant calculation or finding other admissible maps could test the remaining dimensions. [2610.31528]
- **Proposed verification direction:** The Landau–Siegel preprint makes a uniform explicit claim across all primitive quadratic characters. Independent specialists could audit the parameter choices and inequalities, especially the uniformity in conductor, before the asserted conclusion is relied upon. [2610.30476]

## Takeaway

Today's strongest-looking signals are concrete improvements and partial classifications, especially in extremal combinatorics and finite structures, alongside a technically ambitious critical 2D KPZ construction. The claimed impact is not the same as verified consensus: all selected papers are fresh, measurable attention signals are sparse, and the Landau–Siegel assertion in particular needs expert checking.

## Method and sources

- **Window:** daily, 2026-10-23 through 2026-10-23; this is the latest Mathematics announcement batch, not a rolling 24-hour window. The listing labels the batch “Fri, 23 Oct 2026” and reports 390 entries.
- **Scope and completeness:** arXiv Mathematics archive (`math`), including cross-lists only where the selected paper also has a `math.*` category. The full 390-entry batch was traversed; the eight chosen papers were then checked on their individual abstract pages. All eight are new v1 submissions in that announcement batch, although their arXiv timestamps are on 21–22 October UTC.
- **Ranking method:** inferred, not official. Selection favors concrete results, mathematical breadth/cross-listing, explicit verification artifacts, and relevance across multiple subfields. No numeric score was used. Semantic Scholar Graph API was queried for current citation and influential-citation totals; all eight were indexed at 0/0, so those counts provide no useful ordering signal. Targeted web searches for the thrackle, KPZ, and Reed–Solomon papers surfaced arXiv records but no independent seminar or expert discussion in the results checked.
- **Snapshot:** 2026-10-23 16:19:34 UTC.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent?skip=0&show=500); individual abstract pages linked above; [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.31589?fields=title%2CcitationCount%2CinfluentialCitationCount) for citation signals. Direct web extraction was unavailable in the configured extraction service, so the arXiv listing, abstract pages, and top-three HTML papers were checked through the browser instead.
