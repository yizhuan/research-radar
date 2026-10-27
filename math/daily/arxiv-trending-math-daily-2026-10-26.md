# Mathematics on arXiv — daily notable recent papers, 26 October 2026

Nine notable new submissions from the latest available Mathematics announcement batch (Monday, 26 October). A strong cluster links probability and mathematical physics: sparse-graph lower tails, near-critical random curves, and constructive field theory. Spoken agenda: a graphon phase transition, two advances on continuum laws, then algebraic geometry, projection theory, and singularity/homogenization results. Global caveat: arXiv has no official trending chart; this is an inferred ordering by mathematical signals, not measured popularity, and citation evidence is limited for papers only days old.

## Top papers (ranked)

### 1. [The lower tail of triangle counts in sparse random graphs](https://arxiv.org/abs/2610.32879)
- **Abstract:** For Erdős–Rényi graphs with \(n^{-1/2}\ll p\ll1\), the authors solve the graphon variational problem for every fixed lower-tail fraction, identifying the minimizing structures and a first-order transition between homogeneous random graphs and balanced two-block models.
- **Authors:** Dong Huang, Shuangping Li
- **arXiv:** `2610.32879v1` (published 2026-10-23 16:46:20 UTC; categories: `math.PR` (primary), `math.CO` (cross-list))
- **Evidence for ranking:** The authors state that the solution resolves Zhao’s conjecture and an open problem of Janson–Warnke; the result is cross-listed across probability and combinatorics. The introduction and main results were inspected.
- **Claimed result:** The authors claim every variational minimizer is constant or a balanced two-block graphon, with a first-order transition at \(\eta_*=0.009217\ldots\); conditioned graphs are correspondingly close to an Erdős–Rényi graph or a symmetric two-block stochastic block model. (Abstract; Theorems 1.1–1.2.)
- **Assumptions and setting:** Fixed \(\eta\in(0,1)\) and sparse edge probability \(n^{-1/2}\ll p\ll1\); the conclusions concern the leading lower-tail rate and conditional structure in this asymptotic regime.
- **Caveat:** The paper says a different lower-tail mechanism governs smaller \(p\); the conditioned structure is described up to small cut-norm error, not as an exact coupling.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics

### 2. [Probabilistic ultraviolet renormalization of the two-dimensional Sine-Gordon model](https://arxiv.org/abs/2610.32927)
- **Abstract:** The authors construct the two-dimensional Sine–Gordon measure by a probabilistic martingale method for every real activity and the full subcritical coupling range \(\beta^2\in[0,4)\), on bounded convex domains for a broad class of log-correlated Gaussian covariances.
- **Authors:** Benjamin Bonnefont, Hermanni Rajamäki, Vincent Vargas
- **arXiv:** `2610.32927v1` (published 2026-10-23 17:24:42 UTC; categories: `math.PR` (primary), `math-ph` (cross-list))
- **Evidence for ranking:** The abstract and introduction claim coverage of the full subcritical range for a broad covariance class, bridging probability and mathematical physics. The introduction and main construction result were inspected.
- **Claimed result:** Under the paper’s covariance and decomposition assumptions, the authors construct the renormalized measure throughout \(\beta^2<4\), for every \(\alpha\in\mathbb R\). (Abstract; Theorem 2.3.)
- **Assumptions and setting:** A bounded convex domain in two dimensions; a log-correlated Gaussian field with covariance \(K(x,y)=-\log|x-y|+O(1)\), a bounded nonnegative density, and the paper’s white-noise-decomposition assumption; coupling is strictly below \(\beta^2=4\).
- **Caveat:** The critical endpoint \(\beta^2=4\) is not covered; the authors defer construction of correlation functions to future work.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Mathematical physics; Probability & statistics

### 3. [Near-critical Ising interfaces in the thermal direction: Absolute continuity with respect to SLE₃](https://arxiv.org/abs/2610.32860)
- **Abstract:** For the Ising model in the Dobrushin square at mesh \(\delta\) and inverse temperature \(\beta=\beta_c-m\delta\) with fixed nonzero \(m\), the author proves uniformly bounded positive and negative moments of the interface likelihood ratio against critical Ising, implying mutual absolute continuity of every subsequential scaling limit with chordal \(\mathrm{SLE}_3\).
- **Authors:** Yu Feng
- **arXiv:** `2610.32860v1` (published 2026-10-23 16:32:32 UTC; categories: `math.PR` (primary), `math-ph` (cross-list))
- **Evidence for ranking:** The abstract and introduction address a previously posed comparison between near-critical and critical interface laws, with a probability/mathematical-physics cross-list. The introduction and Theorem 1.1 were inspected.
- **Claimed result:** The author claims uniform-in-mesh bounds on all positive and negative likelihood-ratio moments (and both KL divergences), then deduces mutual absolute continuity of every subsequential limit with \(\mathrm{SLE}_3\), with Radon–Nikodym derivatives in every finite \(L^p\). (Abstract; Theorem 1.1.)
- **Assumptions and setting:** Square-lattice Ising model with Dobrushin boundary conditions in the Dobrushin square, mesh \(\delta=1/n\), and fixed \(m\ne0\) in the thermal scaling window \(\beta=\beta_c-m\delta\).
- **Caveat:** The theorem concerns every subsequential limit and does not identify a unique limit or identify it as a particular massive-SLE law.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Probability & statistics; Mathematical physics

### 4. [Kazhdan–Lusztig Polynomials for permutations with \(P_{\mathrm{id},w}(1)=3\) and Irreducible Singular Locus](https://arxiv.org/abs/2610.32832)
- **Abstract:** For permutations whose Schubert variety has irreducible singular locus and whose Kazhdan–Lusztig polynomial evaluates to 3 at 1, the authors give explicit formulas in terms of pattern occurrences and a height statistic, proving the corresponding case of a 2009 Billey–Weed conjecture.
- **Authors:** Gaston Burrull, Zhitong Alex Li, Shixuan Zeng
- **arXiv:** `2610.32832v1` (published 2026-10-23 16:07:19 UTC; categories: `math.AG` (primary), `math.CO` (cross-list))
- **Evidence for ranking:** The abstract states an explicit classification formula and a conjecture-resolution claim; the work bridges algebraic geometry and combinatorics.
- **Claimed result:** When exactly one of patterns 3412 and 4231 occurs, the authors give \(P_{\mathrm{id},w}(q)=1+q^h+q^{h+1}\); when both occur, they give \(1+q+q^h\), with \(h>1\). They identify this as proving the irreducible-singular-locus case of the Billey–Weed conjecture. (Abstract.)
- **Assumptions and setting:** Permutations \(w\) with \(P_{\mathrm{id},w}(1)=3\), under the hypothesis that the Schubert variety \(X_w\) has irreducible singular locus; \(h\) is the specified minimum height of a 3412 occurrence, set to 1 if none occurs.
- **Caveat:** The classification is restricted to this polynomial value and irreducible singular-locus case; the stated formulas do not cover all Schubert varieties.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 5. [The boosted loop-erased random walk](https://arxiv.org/abs/2610.32821)
- **Abstract:** The authors construct boosted loop-erased random-walk scaling limits in the two-dimensional disk and three-dimensional ball and show a planar transition in mutual absolute continuity with classical LERW at boost rate \(m^2=\pi^2/4\), alongside macroscopic space-filling behavior at high boost.
- **Authors:** Gefei Cai, Xinyi Li, Daisuke Shiraishi, Aoteng Xia
- **arXiv:** `2610.32821v1` (published 2026-10-23 15:56:09 UTC; categories: `math.PR` (primary), `math-ph` (cross-list))
- **Evidence for ranking:** The abstract reports constructed scaling limits, an explicit planar threshold, and a change in absolute-continuity behavior, with probability/mathematical-physics cross-listing.
- **Claimed result:** The authors claim that in the disk the mutual-absolute-continuity transition occurs at \(m^2=\pi^2/4\); at each finite boost the Hausdorff dimension is unchanged even as unvisited cubes have side length \(O(m^{-1})\). (Abstract.)
- **Assumptions and setting:** Boosted LERW with weight adjusted according to the underlying walk length before loop-erasure; scaling limits are constructed in the unit disk in two dimensions and unit ball in three dimensions.
- **Caveat:** The explicit threshold is stated for the disk; the abstract does not assert the same threshold in the three-dimensional ball.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Probability & statistics; Mathematical physics

### 6. [Sharp Projection Bounds for Intermediate Dimensions of Measures](https://arxiv.org/abs/2610.32808)
- **Abstract:** The authors prove sharp almost-everywhere and exceptional-set bounds for upper and lower intermediate dimensions under orthogonal and radial projection, and construct a measure whose projected dimension functions vary on open sets of directions.
- **Authors:** Shengyang Zang, Yingyu Zhao, Yunhao Zhao, Chen Zhou
- **arXiv:** `2610.32808v1` (published 2026-10-23 15:45:49 UTC; categories: `math.CA`)
- **Evidence for ranking:** The abstract states sharp estimates and an explicit family witnessing sharpness, plus a construction with direction-dependent behavior.
- **Claimed result:** The authors show both dimension functions are preserved almost everywhere when the quasi-Assouad dimension is at most the target dimension, derive sharp exceptional-set estimates from the full source dimension function, and construct the stated open-direction variation example. (Abstract.)
- **Assumptions and setting:** Compactly supported measures; orthogonal and radial projections; the almost-everywhere preservation statement assumes the quasi-Assouad dimension does not exceed the target dimension.
- **Caveat:** The theorem concerns the specified intermediate-dimension functions and projection settings; its hypotheses should not be read as a universal projection theorem for arbitrary measures or dimension notions.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Geometry & topology

### 7. [Homogenization of the Stokes equations in a domain perforated by a thin truss](https://arxiv.org/abs/2610.32804)
- **Abstract:** For stationary Stokes flow through periodic domains perforated by trusses whose width shrinks faster than the period, the authors identify scaling regimes yielding effective Stokes, Brinkman, or Darcy equations and compute effective coefficients in the Darcy and Brinkman regimes.
- **Authors:** Pascal Hadré, Richard M. Höfer
- **arXiv:** `2610.32804v1` (published 2026-10-23 15:42:46 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract provides distinct limiting PDEs across scaling regimes, explicit coefficients in two regimes, and additional related cylinder geometries.
- **Claimed result:** The authors derive Brinkman equations in the critical regime, unchanged Stokes equations in the subcritical regime, and Darcy’s law in a subrange of the supercritical regime, with explicit coefficients for the Darcy and Brinkman limits. (Abstract.)
- **Assumptions and setting:** Stationary Stokes equations in periodically perforated domains; truss width \(a_\epsilon\) tends to zero faster than period size \(\epsilon\). The Darcy limit is claimed only for a subrange of supercritical scaling.
- **Caveat:** The Darcy result does not cover the entire supercritical range, and the abstract does not claim a universal law for arbitrary perforation geometries.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Analysis & PDE

### 8. [Self-similar solutions for the gSQG patch equations](https://arxiv.org/abs/2610.32857)
- **Abstract:** For each \(\alpha\in(7/4,2)\) and each \(T>0\), the authors claim a self-similar patch solution of the inviscid generalized surface quasi-geostrophic equations whose initially smooth, unbounded-graph boundary develops a corner singularity at time \(T\).
- **Authors:** Javier Gomez-Serrano, Marcus Pasquariello
- **arXiv:** `2610.32857v1` (published 2026-10-23 16:30:56 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract states an explicit finite-time singularity construction across a parameter interval and arbitrary positive terminal time.
- **Claimed result:** The authors claim existence, for every \(\alpha\in(7/4,2)\) and \(T>0\), of a self-similar patch solution with a smooth unbounded-graph boundary for \(0\le t<T\) and a corner at \(T\). (Abstract.)
- **Assumptions and setting:** Inviscid gSQG patch equations, with parameter \(\alpha\) strictly between \(7/4\) and 2; the construction is for the stated self-similar patch class.
- **Caveat:** The abstract’s parameter interval excludes both endpoints and does not claim this construction for the full gSQG family.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Analysis & PDE

### 9. [Foliations on abelian surfaces in positive characteristic](https://arxiv.org/abs/2610.32975)
- **Abstract:** The authors describe smooth linear and turbulent foliations on abelian surfaces in positive characteristic, give criteria for being \(p\)-closed, determine their moduli spaces, and apply the results to construct mildly singular \(p\)-closed foliations on Kummer K3 surfaces.
- **Authors:** Fabrizio Andreatta, Eyal Z. Goren
- **arXiv:** `2610.32975v1` (published 2026-10-23 17:58:46 UTC; categories: `math.AG`)
- **Evidence for ranking:** The abstract claims an explicit classification and moduli-space determination, with an application to Kummer K3 surfaces.
- **Claimed result:** The authors claim a description of all smooth foliations of the stated types, criteria for \(p\)-closedness, and explicit moduli spaces, then use these results to construct examples on Kummer K3 surfaces in positive characteristic. (Abstract.)
- **Assumptions and setting:** Foliations on abelian surfaces over fields of positive characteristic; the application concerns Kummer K3 surfaces and foliations with mild singularities.
- **Caveat:** The reported classification is for the specified surface and characteristic setting; the abstract does not claim a classification in higher dimensions or characteristic zero.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Geometry & topology

## Trending Research Themes

- **Probability and mathematical physics meet through laws of random structures.** Huang–Li identify conditioned sparse graphs via graphon minimizers; Feng compares a near-critical Ising interface law with \(\mathrm{SLE}_3\); Cai et al. construct boosted LERW scaling limits; Bonnefont–Rajamäki–Vargas construct the Sine–Gordon measure. These results share an interest in limiting laws, but use distinct variational, discrete-interface, and martingale-renormalization methods.
- **Sharp parameter regimes and transitions recur across otherwise different models.** The triangle paper gives a first-order threshold in the lower-tail fraction, while the LERW paper identifies a boost threshold for absolute continuity. The Sine–Gordon construction also makes its strict subcritical boundary explicit; these are separate results, not evidence of a single shared mechanism.
- **Geometry and analysis connect microscopic structure to global behavior.** Zang et al. quantify projection dimensions and exceptional directions; Hadré–Höfer derive macroscopic PDE limits from thin periodic trusses; Gomez-Serrano–Pasquariello construct a finite-time corner singularity in a fluid patch. This is a set of distinct analysis signals rather than a field-wide shift.
- **Algebraic geometry and combinatorics meet in singularity classification.** Burrull–Li–Zeng express Kazhdan–Lusztig polynomials through permutation patterns under a Schubert singular-locus hypothesis; Andreatta–Goren classify positive-characteristic foliations and their moduli. Both are geometry-centered, but the abstracts do not claim a shared technique.

## Open Problems and Research Directions

- **Author-stated scope gap — sparse-graph tails:** Huang and Li note that the condition \(p\gg n^{-1/2}\) cannot simply be dropped because a different mechanism governs smaller \(p\). A follow-up is to identify the transition between that mechanism and the graphon regime, including the conditioned graph structure. (Huang–Li, introduction.)
- **Scope gap and proposed extension — Ising interfaces:** The theorem proves mutual absolute continuity for every subsequential limit but does not identify a unique limit. Proving uniqueness and extending the comparison beyond the Dobrushin square would test how much of the result is geometry-independent. (Feng, abstract and Theorem 1.1; proposed extension.)
- **Boundary-case direction — Sine–Gordon:** The construction covers \(\beta^2<4\), not the critical endpoint. Investigating what additional renormalization is needed at \(\beta^2=4\), and extending the deferred correlation-function construction, follows from the stated scope but is a proposed direction rather than a claim of novelty. (Bonnefont et al., abstract and introduction.)
- **Classification extension — Schubert varieties:** The explicit Kazhdan–Lusztig formulas treat \(P_{\mathrm{id},w}(1)=3\) and irreducible singular locus. Extending the pattern-based description to other polynomial values or reducible singular loci is a natural synthesis direction; the paper’s abstract does not claim those cases are solved. (Burrull–Li–Zeng.)

## Takeaway

The most conspicuous result in this batch is the authors’ full variational solution for sparse-graph triangle lower tails, including a concrete phase-transition threshold and two stated problem resolutions. A second cluster controls continuum probability laws in near-critical Ising/LERW and Sine–Gordon settings. These are notable preprint claims, not a popularity chart or independent proof validation; the ordering remains uncertain without robust attention data.

## Method and sources

- **Window:** Daily; exact selected announcement batch 2026-10-26 through 2026-10-26. The current date is 2026-10-27, and the arXiv Mathematics recent page had no 27 October batch yet, so this is the prior available batch.
- **Coverage:** The arXiv Mathematics recent listing showed 326 entries in the 26 October batch; the full listing was loaded and traversed. The nine selected papers are new submissions, first submitted on 23 October 2026; none is treated as a revision. Their abstract pages supplied version, authors, dates, categories, and abstracts. Introductions/main-results statements were additionally inspected for the top three. The candidate scan covered the full Mathematics archive; each selected paper retains its arXiv subject classes rather than being flattened.
- **Snapshot:** 2026-10-27 01:24:16 UTC.
- **Inference:** There is no official arXiv trending chart. Ordering favors explicit conjecture resolution, sharp classification/construction or quantitative result, and cross-subfield relevance; recency is only a tie-breaker. Targeted web searches did not verify independent expert or seminar discussion for the leading papers. Semantic Scholar citation lookup was rate-limited in this snapshot, so citation counts and age-normalized momentum are not used. This is therefore a notable-recent-paper ranking, not a measured popularity ranking.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); the nine linked arXiv abstract pages; full HTML pages for the leading three (`/html/2610.32879`, `/html/2610.32927`, `/html/2610.32860`); arXiv Atom metadata; targeted web searches. No journal reference or DOI was used as a ranking signal for these selected records. Retrieval limitation: scholarly citation metadata was unavailable in this snapshot.
