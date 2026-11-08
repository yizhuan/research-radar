# arXiv Mathematics — notable papers in the Friday, 6 November 2026 batch

The latest Mathematics announcement batch is Friday, 6 November (409 entries in the recent listing); Sunday, 8 November has no newer batch in the listing. This report selects 9 notable papers, led by two independent preprints claiming the sharp order in Tusnády’s discrepancy problem, with an online thinning result as an extension. Spoken agenda: discrepancy first, then a new rank-37 lattice and results across geometry, arithmetic, PDE, and probability. This ordering is inferred, not an official arXiv trending chart; citation evidence for papers announced only days ago is limited, and no citation-based ordering is used.

## Top papers (ranked)

### 1. [Resolving Tusnády's Problem](https://arxiv.org/abs/2611.06998)
- **Abstract:** The author proves a matching lower bound of order $(\log N)^{d-1/2}$ for combinatorial discrepancy of anchored boxes in each fixed dimension $d\ge3$, which—combined with existing upper and planar lower bounds—settles the order for axis-parallel boxes in all fixed dimensions $d\ge2$.
- **Authors:** Nicola Wengiel
- **arXiv:** `2611.06998v1` (published 2026-11-04 18:58:56 UTC; primary category: `math.CA`; cross-lists: `cs.CG`, `cs.DS`, `math.CO`)
- **Evidence for ranking:** Its main theorem closes the remaining factor-$\sqrt{\log N}$ gap for every fixed $d\ge3$; the arXiv abstract identifies the matching earlier upper bound and planar result needed for the all-dimensions conclusion. A second preprint in the same batch independently claims the sharp order.
- **Claimed result:** Theorem 1.1 gives $\operatorname{disc}(N,\mathcal A_d)\ge c_d(\log N)^{d-1/2}$ for all sufficiently large $N$ and each fixed $d\ge3$; with the cited bounds, Corollary 1.2 gives $\Theta_d((\log N)^{d-1/2})$. These are the author's preprint claims.
- **Assumptions and setting:** Worst-case combinatorial discrepancy for $N$-point sets against anchored or axis-parallel boxes in Euclidean $d$-space; $d$ is fixed, and constants and the threshold may depend on $d$.
- **Caveat:** The author does not optimize the dimension-dependent constants or threshold; the lower-bound proof treats $d\ge3$, relying on a prior planar lower bound for $d=2$.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Combinatorics & discrete mathematics

### 2. [Tusnády's problem and online two-sample thinning](https://arxiv.org/abs/2611.08455)
- **Abstract:** The author proves the same sharp discrepancy order in every fixed dimension, a robust lower bound after limited deletions, and minimax bounds for online thinning of two samples, including a sharp one-dimensional terminal rate.
- **Authors:** Yuhao Lei
- **arXiv:** `2611.08455v1` (published 2026-11-05 18:47:43 UTC; primary category: `math.CO`; cross-lists: `cs.DS`, `math.PR`)
- **Evidence for ranking:** A same-batch independent proof of the sharp Tusnády order is paired with additional quantitative results on online thinning; the abstract cross-lists combinatorics, algorithms, and probability. For $k\ge2$, the paper also exposes a remaining logarithmic gap in its terminal-thinning bounds.
- **Claimed result:** Theorem 1.1 states $\Delta_d(N)=\Theta_d((\log N)^{d-1/2})$ for fixed $d\ge2$. Theorem 1.2 gives minimax expected prefix discrepancy $\Theta_{k,\rho}((\log n)^{k+1/2})$ for fixed $k\ge1$ and $0<\rho<2$; the author also proves a one-dimensional terminal order $\Theta_\rho((\log\log n)^{3/2})$ for fixed $0<\rho<2$. These are the author's preprint claims.
- **Assumptions and setting:** The geometry result is for worst-case finite point sets and axis-parallel boxes. The thinning model uses two independent size-$n$ samples from an unknown common Borel law; decisions to keep or discard are online and irrevocable, with expected deletion budget $\rho n$.
- **Caveat:** For dimensions $k\ge2$, the author leaves terminal discrepancy bounds separated by a factor of $\log n$; the claimed sharp prefix order does not close that terminal gap.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 3. [An extremal unimodular lattice of rank 37](https://arxiv.org/abs/2611.07138)
- **Abstract:** The author constructs a rank-37 extremal unimodular lattice of minimum four, resolving the last undetermined optimal minimum through rank 48, and derives a corresponding Type I self-dual $\mathbb Z/4\mathbb Z$ code.
- **Authors:** Eric Kubischta
- **arXiv:** `2611.07138v1` (published 2026-11-04 21:06:40 UTC; primary category: `math.CO`; cross-list: `math.NT`)
- **Evidence for ranking:** The introduction identifies rank 37 as the sole unresolved optimal-minimum case among integral unimodular lattices through rank 48; the claimed construction also settles the matching length-37 code case. The lattice and code results connect number-theoretic structure with discrete coding theory.
- **Claimed result:** The paper's main theorem constructs an integral unimodular lattice of rank 37 and minimum four, with automorphism group $\operatorname{AGL}(1,13)\times C_6$, and a 4-frame yielding a Type I self-dual $\mathbb Z/4\mathbb Z$ code of length 37 and minimum Euclidean weight 16.
- **Assumptions and setting:** Positive-definite integral unimodular lattices; “minimum” is the smallest squared norm of a nonzero lattice vector. The code conclusion uses a 4-frame in the constructed lattice.
- **Caveat:** The coding result depends on exhibiting a 4-frame; the paper reports that a computer search finds one and specifies representatives in an appendix. The result addresses rank 37, not optimal minima in higher ranks.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 4. [On do Carmo's Question: The Properly Embedded Case](https://arxiv.org/abs/2611.08454)
- **Abstract:** The author claims that every complete, noncompact, two-sided, properly embedded constant-mean-curvature hypersurface of finite Morse index in Euclidean space is minimal, in every dimension, without curvature or volume-growth bounds.
- **Authors:** Gongping Niu
- **arXiv:** `2611.08454v1` (published 2026-11-05 18:47:40 UTC; primary category: `math.DG`; cross-list: `math.AP`)
- **Evidence for ranking:** The stated theorem removes dimension restrictions and curvature/volume-growth bounds for the properly embedded finite-index case; its differential-geometric result is cross-listed in analysis of PDEs. The introduction contrasts it with earlier results requiring bounded curvature or limited ambient dimensions.
- **Claimed result:** Theorem 1 states that a smooth, connected, complete, noncompact, two-sided, properly embedded CMC hypersurface without boundary and with finite Morse index in $\mathbb R^{n+1}$ has zero mean curvature for every $n\ge2$.
- **Assumptions and setting:** The hypersurface is complete, noncompact, two-sided, properly embedded, boundaryless, and finite-index; the ambient space is Euclidean. The proof uses an inscribed-radius weight and stability outside a compact set.
- **Caveat:** Proper embeddedness is essential to the presented argument; the theorem does not cover arbitrary immersed hypersurfaces in every dimension.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Geometry & topology; Analysis & PDE

### 5. [Pointless K3 surfaces over finite fields](https://arxiv.org/abs/2611.08356)
- **Abstract:** The authors prove that a K3 surface without a rational point over $\mathbb F_q$ exists exactly for prime powers $q\le11$, using lattice bounds, the Artin–Tate formula, and embeddings into Niemeier lattices.
- **Authors:** Asher Auel; Philip Engel; Kiran S. Kedlaya; Sair Shaikh
- **arXiv:** `2611.08356v1` (published 2026-11-05 17:36:46 UTC; primary category: `math.NT`; cross-list: `math.AG`)
- **Evidence for ranking:** It gives a sharp existence/nonexistence cutoff in arithmetic geometry and links finite-field point counts to lattice packing and Niemeier-lattice embeddings. The paper itself notes an independent preprint by Brandhorst and Takada, arXiv:2611.06366, proving the same classification by a different method.
- **Claimed result:** The authors claim that a K3 surface without an $\mathbb F_q$-point exists if and only if $q\le11$; they also state this improves a bound used in certain threefold rational-point results.
- **Assumptions and setting:** Smooth K3 surfaces over finite fields, with $q$ a prime power; the conclusion concerns existence of at least one rational point over the field of definition.
- **Caveat:** The authors' approach uses numerical computations and lattice-embedding analysis; the independent preprint means the classification is not unique to this paper's proof.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Algebra & number theory; Geometry & topology

### 6. [Weak uniqueness for the stochastic heat equation with nondegenerate diffusion: the full Hölder regime](https://arxiv.org/abs/2611.07310)
- **Abstract:** The author claims weak well-posedness for a one-dimensional torus stochastic heat equation when its uniformly nondegenerate diffusion coefficient is Hölder continuous with any positive exponent, extending an earlier result above exponent $2/3$.
- **Authors:** Yi Han
- **arXiv:** `2611.07310v1` (published 2026-11-05 01:55:58 UTC; primary category: `math.PR`)
- **Evidence for ranking:** The abstract claims closure of the full positive-Hölder range left open by the author's earlier preprint and links a Lean formalization. The problem lies at the intersection of stochastic analysis and nonlinear parabolic equations.
- **Claimed result:** The author claims weak well-posedness for the scalar stochastic heat equation on the one-dimensional torus with uniformly nondegenerate, positively Hölder diffusion, and extends the argument to measurable drifts of linear growth by localized Girsanov change of measure.
- **Assumptions and setting:** Scalar equation on the one-dimensional torus; diffusion is uniformly nondegenerate and Hölder continuous with exponent $\alpha>0$. The drift extension is to measurable drifts of linear growth.
- **Caveat:** The claim is weak well-posedness, not a claim of pathwise uniqueness; the 121-page proof and linked Lean formalization were not independently audited here.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Probability & statistics; Analysis & PDE

### 7. [Global well-posedness for the energy-critical focusing NLS on $\mathbb T^3$](https://arxiv.org/abs/2611.07740)
- **Abstract:** The authors claim global well-posedness for the focusing quintic nonlinear Schrödinger equation on the standard three-dimensional torus for data below mass-corrected energy and Sobolev thresholds determined by the Euclidean ground state.
- **Authors:** Meng Chen; Han Wang
- **arXiv:** `2611.07740v1` (published 2026-11-05 09:49:05 UTC; primary category: `math.AP`)
- **Evidence for ranking:** The result is presented as a subthreshold focusing counterpart to a known defocusing theorem and combines periodic profile analysis with a recent Euclidean scattering theorem; it is a substantial nonlinear dispersive PDE claim.
- **Claimed result:** The authors claim global well-posedness and uniform finite-interval bounds under their stated subthreshold conditions for the energy-critical focusing NLS on $\mathbb T^3$.
- **Assumptions and setting:** Standard flat three-torus; focusing quintic (energy-critical) NLS; initial data must satisfy both mass-corrected energy and Sobolev-norm thresholds tied to the Euclidean ground state.
- **Caveat:** The theorem is subthreshold and does not cover data at or above the stated ground-state conditions.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Analysis & PDE

### 8. [Uniqueness of Extremizers and Convergence of the Euler-Lagrange Iteration for the Critical Hardy-Littlewood-Sobolev Inequality](https://arxiv.org/abs/2611.08222)
- **Abstract:** For $n\ge3$, $2\le\alpha<n$, and exponents satisfying $p^{-1}+r^{-1}=1+\alpha/n$, the author claims uniqueness of normalized nonnegative extremizers up to translations and dilations, radial nondegeneracy, and convergence of a normalized alternating iteration from nonnegative radially nonincreasing data.
- **Authors:** Hanwen Lu
- **arXiv:** `2611.08222v1` (published 2026-11-05 16:10:09 UTC; primary category: `math.AP`; cross-list: `math.CA`)
- **Evidence for ranking:** It combines a uniqueness theorem for a critical integral inequality with a convergence result for its Euler–Lagrange iteration, and is cross-listed between PDE and classical analysis.
- **Claimed result:** The author claims all positive finite-energy Euler–Lagrange solutions lie in a single translation/dilation orbit, and that the normalized alternating iteration converges strongly to an extremizing pair for every nonnegative radially nonincreasing initial datum.
- **Assumptions and setting:** $n\ge3$, $2\le\alpha<n$, $1<p,r<\infty$, and $p^{-1}+r^{-1}=1+\alpha/n$; the iteration theorem additionally assumes nonnegative, radially nonincreasing initial data.
- **Caveat:** The convergence guarantee is for radial nonincreasing initial data; it does not establish convergence from arbitrary nonnegative data.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Analysis & PDE

### 9. [A diameter-one set in $\mathbb{R}^5$ that cannot be covered by six diameter-one balls](https://arxiv.org/abs/2611.08198)
- **Abstract:** The authors construct a compact diameter-one set in $\mathbb R^5$ that cannot be covered by six diameter-one balls, with a finite-set version that still resists six balls of radius $0.50001$.
- **Authors:** A. Arman; A. Bondarenko; A. Prymak; D. Radchenko
- **arXiv:** `2611.08198v1` (published 2026-11-05 15:52:42 UTC; primary category: `math.MG`)
- **Evidence for ranking:** The paper gives a concrete counterexample to a strong covering assertion, including a finite witness with a stated radius margin; the proof connects a matrix-space construction to spherical coverings and Euler's formula.
- **Claimed result:** The authors claim a compact set of diameter 1 in $\mathbb R^5$ not coverable by six Euclidean balls of diameter 1; its convex hull also has this property, and a finite subset remains uncovered by six closed balls of radius $0.50001$.
- **Assumptions and setting:** Euclidean metric in dimension five; the covering is by six balls, with diameter one in the compact-set statement and the specified larger radius in the finite-set statement.
- **Caveat:** The construction and conclusion are dimension- and covering-number-specific; the abstract does not assert a general formula for other dimensions or numbers of balls.
- **Announcement type:** new submission, Friday, 6 November 2026
- **Themes:** Geometry & topology

## Trending Research Themes

- **Sharp discrepancy and online balancing:** The strongest repeated signal is two independent same-batch claims resolving the fixed-dimensional Tusnády order: Wengiel proves the new $d\ge3$ lower bound and combines it with prior results, while Lei proves the sharp order for $d\ge2$ and uses robust discrepancy to analyze two-sample thinning. Their proofs are distinct; both connect discrepancy to Gaussian methods, but only Lei develops the online keep/discard model and leaves a terminal-gap question.
- **Lattices as a bridge between arithmetic and discrete structures:** Kubischta's rank-37 construction yields a self-dual code; Auel, Engel, Kedlaya, and Shaikh use definite lattices and Niemeier embeddings to constrain K3 zeta functions. These are separate results, but both make lattice structure the bridge between an existence/classification question and another mathematical object.
- **Several isolated PDE/probability advances, not a single shared method:** Niu's CMC finite-index theorem, Chen–Wang's focusing NLS result, Han's weak uniqueness theorem, and Lu's HLS extremizer/iteration results span geometric analysis, dispersive PDE, stochastic PDE, and critical inequalities. The batch suggests activity across analysis, but these papers do not establish a common field-wide shift or technique.

## Open Problems and Research Directions

- **Tusnády constants (author-stated limitation):** Wengiel says the constants and thresholds depend on fixed dimension and are not optimized. A follow-up could seek explicit dimension dependence or sharper finite-$N$ thresholds; this is a proposed direction, not a claim of novelty.
- **Terminal thinning in dimensions $k\ge2$ (author-stated gap):** Lei's terminal minimax upper and lower bounds differ by a factor of $\log n$. Closing that gap, under the stated expected deletion budget and unknown common sampling law, is an explicit next problem.
- **Beyond proper embedding (scope-based open direction):** Niu's proof relies on proper embeddedness, and the theorem leaves general immersed finite-index CMC hypersurfaces outside its all-dimensional scope. One direction is to identify additional geometric hypotheses that could replace properness while preserving the conclusion.
- **HLS iteration beyond radial monotonicity (scope-based direction):** Lu proves convergence from nonnegative radially nonincreasing initial data. It would be useful to test whether weaker symmetry, rearrangement, or compactness assumptions suffice for convergence from a wider class of initial data.
- **Threshold NLS data (scope-based direction):** Chen and Wang's theorem is below the Euclidean ground-state thresholds. The boundary case at equality is a natural setting to examine separately; the report does not infer that the authors claim it is open.

## Takeaway

The clearest mathematical headline is the independent pair of preprints claiming the sharp fixed-dimensional order in Tusnády's problem, with Lei adding a substantial online-thinning application and a precisely stated remaining terminal gap. The other selected papers include a rank-37 lattice construction that closes a long-standing finite-rank case and sharp claims in geometry and analysis; all remain preprints, and this is a result-driven selection rather than a measured popularity ranking.

## Method and sources

- **Window:** daily, 2026-11-06 through 2026-11-06; latest available announcement batch was Friday, 6 November 2026, so this is a prior batch relative to Sunday, 8 November 2026.
- **Snapshot:** 2026-11-08 17:22:24 UTC.
- **Coverage:** arXiv Mathematics recent listing traversed through the full 409-entry Friday batch, including math subject classes and cross-listed neighboring categories when the math contribution was central. Nine papers were selected; arXiv API metadata and each selected abstract were checked. All nine are new submissions, not revisions.
- **Inference:** arXiv publishes no official trending or readership ranking. With papers only days old and no usable citation evidence, this is a ranking of notable recent results based on specific claimed theorems/constructions, corroboration such as the independent Tusnády and K3 preprints, cross-listing, and stated scope—not a measured popularity list. Semantic Scholar citation metadata was unavailable at this snapshot, so no citation counts or citation-momentum claims are used.
- **Sources:** arXiv Mathematics recent listing (https://arxiv.org/list/math/recent); arXiv API records and the linked abstract pages for all papers above; paper text/main-results statements where available via arXiv HTML/PDF; independent preprint cited in the K3 entry (https://arxiv.org/abs/2611.06366).
