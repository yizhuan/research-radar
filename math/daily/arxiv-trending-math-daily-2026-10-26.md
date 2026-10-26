# Mathematics on arXiv — daily notable papers, 26 October 2026

Nine papers from the Monday announcement batch; the clearest concentration is rigorous probability and mathematical physics, from sparse-graph phase transitions to near-critical interfaces and field-theory renormalization. Spoken agenda: first the conjecture-resolving graph result, then the Ising/Sine–Gordon advances, followed by number theory, fractal geometry, and analysis. Global caveat: arXiv publishes no official trending chart, and citation/attention evidence is sparse or unavailable for papers only days old; this is an inferred notable-paper ordering, not a measured popularity ranking.

## Top papers (ranked)

### 1. [The lower tail of triangle counts in sparse random graphs](https://arxiv.org/abs/2610.32879)
- **Abstract:** For Erdős–Rényi graphs with \(n^{-1/2}\ll p\ll1\), the authors solve the graphon variational problem for every fixed lower-tail fraction, identifying the minimizing structures and a first-order transition between homogeneous random graphs and balanced two-block models.
- **Authors:** Dong Huang, Shuangping Li
- **arXiv:** `2610.32879v1` (published 2026-10-23 16:46:20 UTC; categories: `math.PR` (primary), `math.CO` (cross-list))
- **Evidence for ranking:** The abstract and introduction explicitly state that the solution resolves Zhao’s conjecture and an open problem of Janson–Warnke; the paper spans probability and combinatorics. The introduction and main theorem were inspected. The arXiv record lists no journal reference or DOI.
- **Claimed result:** The authors prove that every variational minimizer is constant or a balanced two-block graphon, with a first-order transition at \(\eta_*=0.009217\ldots\); the conditioned graph is correspondingly close to an Erdős–Rényi graph or a symmetric two-block stochastic block model. (Abstract; Theorems 1.1–1.2.)
- **Assumptions and setting:** Fixed \(\eta\in(0,1)\), and sparse edge probability \(n^{-1/2}\ll p\ll1\); the conclusions describe the leading lower-tail rate and conditional structure in that asymptotic regime.
- **Caveat:** The result does not extend to \(p\) at or below the stated sparse threshold; the authors note that a different lower-tail mechanism applies there. The conditioned graph is described up to small cut-norm error, not an exact coupling.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics

### 2. [Near-critical Ising interfaces in the thermal direction: Absolute continuity with respect to SLE₃](https://arxiv.org/abs/2610.32860)
- **Abstract:** For the Ising model in the Dobrushin square at mesh \(\delta\) and inverse temperature \(\beta=\beta_c-m\delta\) with fixed nonzero \(m\), the author proves uniformly bounded positive and negative moments of the interface likelihood ratio against critical Ising and mutual absolute continuity of every subsequential scaling limit with chordal \(\mathrm{SLE}_3\).
- **Authors:** Yu Feng
- **arXiv:** `2610.32860v1` (published 2026-10-23 16:32:32 UTC; categories: `math.PR` (primary), `math-ph` (cross-list))
- **Evidence for ranking:** The abstract states a sharp comparison between a near-critical single interface and critical \(\mathrm{SLE}_3\); the introduction says this addresses a previously posed absolute-continuity question. It bridges probability and mathematical physics. The introduction and Theorem 1.1 were inspected; no journal reference or DOI is listed.
- **Claimed result:** The author proves uniform-in-mesh bounds on all positive and negative likelihood-ratio moments (and both KL divergences), then deduces that every subsequential limit is mutually absolutely continuous with \(\mathrm{SLE}_3\), with Radon–Nikodym derivatives in every finite \(L^p\). (Abstract; Theorem 1.1.)
- **Assumptions and setting:** Square-lattice Ising model with Dobrushin boundary conditions in the Dobrushin square, mesh \(\delta=1/n\), and fixed \(m\ne0\) in the thermal scaling window \(\beta=\beta_c-m\delta\).
- **Caveat:** The paper does not identify the subsequential limit uniquely or identify it as a particular massive-SLE law; the author flags uniqueness and extensions beyond the square as open directions.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Probability & statistics; Mathematical physics

### 3. [Probabilistic ultraviolet renormalization of the two-dimensional Sine-Gordon model](https://arxiv.org/abs/2610.32927)
- **Abstract:** The authors construct the two-dimensional Sine–Gordon measure by a probabilistic martingale method for every real activity and the full subcritical coupling range \(\beta^2\in[0,4)\), on bounded convex domains for a broad class of log-correlated Gaussian covariances.
- **Authors:** Benjamin Bonnefont, Hermanni Rajamäki, Vincent Vargas
- **arXiv:** `2610.32927v1` (published 2026-10-23 17:24:42 UTC; categories: `math.PR` (primary), `math-ph` (cross-list))
- **Evidence for ranking:** The abstract and introduction claim coverage of the full subcritical range for a broad covariance class, with a probability/mathematical-physics cross-list. The introduction and main construction theorem were inspected. No journal reference or DOI is listed.
- **Claimed result:** Under the paper’s covariance and decomposition assumptions, normalized renormalized partition functions converge to a probability measure throughout \(\beta^2<4\), for all \(\alpha\in\mathbb R\). (Abstract; Theorem 2.3.)
- **Assumptions and setting:** A bounded convex domain in two dimensions; a log-correlated Gaussian field with covariance \(K(x,y)=-\log|x-y|+O(1)\), a bounded nonnegative density, and the paper’s white-noise-decomposition assumption; coupling remains strictly below the BKT threshold \(\beta^2=4\).
- **Caveat:** The critical endpoint \(\beta^2=4\) is not covered. The authors say construction of correlation functions is deferred to forthcoming work.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Mathematical physics; Probability & statistics

### 4. [A counterexample to Tokareva's conjecture on sums of two bent functions](https://arxiv.org/abs/2610.32239)
- **Abstract:** The authors disprove Tokareva’s converse conjecture by giving a degree-four Boolean function on \(\mathbb F_2^8\) that is not a sum of two bent functions, extend the counterexamples to every even dimension at least eight, and derive counterexamples to a related derivative conjecture in every even dimension at least ten.
- **Authors:** Yansong Feng, Hao Jiang, Guancheng Li, Tianyi Li, Lili Tang
- **arXiv:** `2610.32239v1` (published 2026-10-23 06:48:58 UTC; categories: `math.CO` (primary), `cs.IT` (cross-list))
- **Evidence for ranking:** A concrete counterexample settles a stated conjecture and extends to infinite families of dimensions; the paper is cross-listed in combinatorics and information theory. The arXiv comment describes an LLM-agent-assisted search and independent audit rounds, making the proof pipeline unusually explicit. No journal reference or DOI is listed.
- **Claimed result:** The authors exhibit \(x_1x_2(x_3x_4+x_5x_6+x_7x_8)\) as a non-sum of two bent functions on \(\mathbb F_2^8\), extend this construction to all even \(n\ge8\), and use Shaporenko’s reduction for derivative-conjecture counterexamples for all even \(n\ge10\). (Abstract.)
- **Assumptions and setting:** Boolean functions on even-dimensional binary vector spaces; the original converse concerns functions of algebraic degree at most \(n/2\).
- **Caveat:** The authors’ comment says the counterexamples and proofs arose through a large LLM-agent campaign and invites feedback on correctness, exposition, and attribution; independent mathematical verification remains important.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Combinatorics & discrete mathematics

### 5. [Biases in gaps between zeros of Dirichlet L-functions](https://arxiv.org/abs/2610.31744)
- **Abstract:** The authors identify and classify a rare family of Dirichlet \(L\)-functions with a nonvanishing Gauss-type sum, report an experimentally observed bias in zero-gap distributions for that family, and prove that these are the only cuspidal automorphic \(L\)-functions on \(\mathrm{GL}(1)/\mathbb Q\) or \(\mathrm{GL}(2)/\mathbb Q\) whose associated \(Z\)-functions have a large integrated mean.
- **Authors:** Jonathan W. Bober, Zhenchao Ge, Micah B. Milinovich
- **arXiv:** `2610.31744v1` (published 2026-10-22 17:50:00 UTC; categories: `math.NT` (primary))
- **Evidence for ranking:** The abstract combines a complete arithmetic classification with a claimed uniqueness result over the stated GL(1)/GL(2) family; targeted search found the arXiv abstract and PDF, but no independent discussion. No cross-list, journal reference, or DOI is listed.
- **Claimed result:** The authors classify characters for which the Gauss-type sum is nonzero and derive the stated uniqueness of the automorphic families with large integrated \(Z\)-function mean. They also report a previously undetected zero-gap bias in that rare family. (Abstract.)
- **Assumptions and setting:** Primitive Dirichlet characters and cuspidal automorphic \(L\)-functions over \(\mathbb Q\), restricted to GL(1) and GL(2); the family with the bias has density zero among primitive characters.
- **Caveat:** The zero-gap bias is described as experimentally observed; the abstract’s rigorous classification concerns the Gauss-type sum and the resulting mean-value statement, not a claim that the phenomenon is common.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Algebra & number theory

### 6. [Sharp Projection Bounds for Intermediate Dimensions of Measures](https://arxiv.org/abs/2610.32808)
- **Abstract:** The authors prove sharp almost-everywhere and exceptional-set bounds for upper and lower intermediate dimensions under orthogonal and radial projection, and construct a measure whose projected dimension functions vary on open sets of directions.
- **Authors:** Shengyang Zang, Yingyu Zhao, Yunhao Zhao, Chen Zhou
- **arXiv:** `2610.32808v1` (published 2026-10-23 15:45:49 UTC; categories: `math.CA` (primary))
- **Evidence for ranking:** The abstract states sharp bounds and an explicit family attaining sharpness, as well as a fixed-measure construction showing direction-dependent behavior; no cross-list, journal reference, or DOI is listed.
- **Claimed result:** The authors show both dimension functions are preserved almost everywhere when the quasi-Assouad dimension is at most the target dimension, give sharp exceptional-set estimates using the source dimension function, and construct the stated open-direction variation example. (Abstract.)
- **Assumptions and setting:** Compactly supported measures; orthogonal and radial projections; the almost-everywhere preservation statement assumes the quasi-Assouad dimension does not exceed the target dimension.
- **Caveat:** The result is about the specified intermediate-dimension functions and projection settings; the exceptional-set bounds depend on the source dimension function and should not be read as a universal projection theorem for arbitrary measures or dimension notions.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Geometry & topology

### 7. [Homogenization of the Stokes equations in a domain perforated by a thin truss](https://arxiv.org/abs/2610.32804)
- **Abstract:** For stationary Stokes flow through periodic domains perforated by trusses whose width shrinks faster than the period, the authors identify scaling regimes yielding effective Stokes, Brinkman, or Darcy equations and compute the effective coefficients in the Darcy and Brinkman regimes.
- **Authors:** Pascal Hadré, Richard M. Höfer
- **arXiv:** `2610.32804v1` (published 2026-10-23 15:42:46 UTC; categories: `math.AP` (primary))
- **Evidence for ranking:** The abstract gives a full regime classification with explicit effective coefficients and also treats a related cylinder forest and fence geometry; no cross-list, journal reference, or DOI is listed.
- **Claimed result:** The authors derive Brinkman equations in the critical regime, unchanged Stokes equations in the subcritical regime, and Darcy’s law in a subrange of the supercritical regime, with explicit coefficients for the Darcy and Brinkman limits. (Abstract.)
- **Assumptions and setting:** Stationary Stokes equations in periodically perforated domains; truss width \(a_\epsilon\) tends to zero faster than period size \(\epsilon\). The effective Darcy regime is only claimed for a subrange of the supercritical scaling.
- **Caveat:** The Darcy result does not cover the entire supercritical range; the abstract does not claim a universal effective law for arbitrary perforation geometries.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Analysis & PDE; Numerical analysis & computation

### 8. [Large deviations and applications in homogeneous dynamics](https://arxiv.org/abs/2610.32814)
- **Abstract:** Assuming exponential mixing, the authors prove a sub-Gaussian large-deviation estimate for smooth compactly supported test functions under a semisimple homogeneous action and apply it to effective uniqueness of the maximal-entropy measure and pointwise equidistribution on full expanding horospheres for Haar-almost every point.
- **Authors:** Taehyeong Kim, Ron Mor
- **arXiv:** `2610.32814v1` (published 2026-10-23 15:48:32 UTC; categories: `math.DS` (primary))
- **Evidence for ranking:** The abstract provides two quantitative applications of a general large-deviation estimate, linking dynamical systems and probability methods; no cross-list, journal reference, or DOI is listed.
- **Claimed result:** For left translation by \(a\) on finite-volume \(G/\Gamma\), with \(\operatorname{Ad}(a)\) diagonalizable over \(\mathbb R\), the authors prove sub-Gaussian deviations under exponential mixing; they derive effective uniqueness of the maximal-entropy measure and quantitative pointwise equidistribution on each full expanding horosphere for Haar-a.e. point. (Abstract.)
- **Assumptions and setting:** Semisimple homogeneous space of finite volume; smooth compactly supported observables; exponential mixing; real-diagonalizable adjoint action.
- **Caveat:** The large-deviation theorem is conditional on exponential mixing, and the equidistribution conclusion is an almost-everywhere statement rather than a claim for every point.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Geometry & topology; Probability & statistics

### 9. [Graph distance and percolation dimension of three-dimensional Brownian motion](https://arxiv.org/abs/2610.32137)
- **Abstract:** The author proves that the minimum Hausdorff dimension of a continuous path joining the endpoints within the range of three-dimensional Brownian motion is an almost-sure deterministic constant \(\gamma_3\in(1,5/3]\), relates it to a graph-distance growth exponent by \(\gamma_3=2\theta\), and establishes moment-growth asymptotics.
- **Authors:** Daisuke Shiraishi
- **arXiv:** `2610.32137v1` (published 2026-10-23 04:05:23 UTC; categories: `math.PR` (primary))
- **Evidence for ranking:** The abstract gives a deterministic geometric exponent, constructs continuum many distinct minimizing curves, and ties the dimension to graph-distance growth; no cross-list, journal reference, or DOI is listed.
- **Claimed result:** The author proves almost-sure existence of \(\gamma_3\), constructs continuum many simple minimizing curves with that Hausdorff and box dimension, and shows the endpoint graph distance and diameter share an exponent \(\theta\) with \(\gamma_3=2\theta\). (Abstract.)
- **Assumptions and setting:** The range of standard three-dimensional Brownian motion on \([0,1]\); paths join \(W_0\) to \(W_1\) while staying inside that random range.
- **Caveat:** The abstract bounds \(\gamma_3\) and characterizes it through \(\theta\), but gives no explicit numerical value for either exponent.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Probability & statistics; Geometry & topology

## Trending Research Themes

- **Large deviations are being pushed from rates to structure.** The sparse-triangle paper solves the minimizing graphon and conditioned-graph shape, while the homogeneous-dynamics paper turns exponential mixing into quantitative deviation and equidistribution statements. These are distinct settings, not evidence of one shared technique. (Huang–Li; Kim–Mor.)
- **Probability meets mathematical physics at the level of measures and interfaces.** Feng compares a near-critical Ising interface law with \(\mathrm{SLE}_3\), while Bonnefont–Rajamäki–Vargas construct the two-dimensional Sine–Gordon measure across its subcritical regime. In both, controlling a limiting law is central, but the Ising work concerns a discrete scaling limit and the Sine–Gordon work concerns ultraviolet renormalization. (Feng; Bonnefont et al.)
- **Geometry is being quantified through sharp exponents and scaling regimes.** Projection dimension bounds and the Brownian-range path exponent give sharp/fractal geometric quantities; thin-truss homogenization instead maps microscopic geometry to macroscopic PDE laws. This is a cross-topic synthesis rather than a single shared method. (Zang et al.; Shiraishi; Hadré–Höfer.)
- **Concrete conjecture tests stand out in discrete mathematics and arithmetic.** The bent-function paper provides an explicit infinite family of counterexamples, while the Dirichlet \(L\)-function paper classifies an exceptional arithmetic family and derives a uniqueness statement for large mean values. (Yansong Feng et al.; Bober–Ge–Milinovich.)

## Open Problems and Research Directions

- **Author-stated, sparse-graph lower tails:** Huang and Li ask whether the conditioned graph can be sandwiched by nearby Erdős–Rényi graphs above the transition (and nearby two-block models below it), and how the minimizers and transition extend to other nonbipartite subgraphs. A concrete next step is to test the proposed balanced \((k-1)\)-block picture for graphs of chromatic number \(k\), first in small-target regimes where existing results apply. (Huang–Li, §8.)
- **Author-stated, near-critical Ising:** Feng leaves uniqueness and identification of the subsequential interface limit open, and discusses extending the comparison from the square to smooth or more general Dobrushin domains. A focused extension is to prove the requisite boundary estimates and strip identity near curved or tilted marked points. (Feng, §1.5.)
- **Author-stated, Sine–Gordon:** the authors defer construction of correlation functions to future work. Extending the martingale construction to those observables, and checking which covariance assumptions suffice, follows directly from their stated next step. (Bonnefont et al., Theorem 2.3 discussion.)
- **Research direction (synthesis):** Shiraishi’s relation \(\gamma_3=2\theta\) suggests seeking explicit bounds or a numerical estimate for the graph-distance exponent, then translating them into improved bounds for the minimal path dimension. The paper’s abstract establishes the relation but does not report a numerical value. (Shiraishi.)
- **Verification direction:** The bent-function authors explicitly invite correctness and attribution feedback on their agent-assisted proof process. Independent proof checking or a compact certificate would clarify which parts of the counterexample construction can be verified mechanically. (Yansong Feng et al., arXiv comment.)

## Takeaway

The strongest single result in this batch is the complete sparse-triangle lower-tail variational solution, which settles two stated open questions in a specific sparse regime. The Ising and Sine–Gordon papers also make substantial author-claimed advances in controlling two-dimensional probability laws, but all selected items remain fresh preprints; neither the order nor the mathematical claims should be mistaken for community consensus.

## Method and sources

- **Window:** daily; exact announcement-batch date 2026-10-26 (Monday). The arXiv mathematics recent listing showed 326 entries in the primary math batch; the full listing page was loaded with all 500 current entries, including cross-listed additions. The selected papers are new submissions, not revisions, first submitted 2026-10-22 or 2026-10-23. No prior-batch substitution was needed.
- **Snapshot:** 2026-10-26 17:24:51 UTC (retrieval snapshot).
- **Coverage:** arXiv Mathematics recent listings, with the arXiv categories retained per paper. Candidate abstract pages were checked for all nine selected entries; the full HTML introductions/main results were additionally inspected for the top three. The triangle paper’s open-problems section and the Ising paper’s outlook were read.
- **Inference:** arXiv has no official readership/trending ranking. Selection and ordering favor author-stated conjecture resolution, concrete classifications/constructions, conditional assumptions and scope, and cross-subfield relevance; recency only breaks ties. Targeted searches for leading candidates did not surface independent expert/seminar discussion. Semantic Scholar citation metrics could not be retrieved in this snapshot, so no citation totals or age-normalized momentum are used.
- **Sources:** arXiv recent listing: https://arxiv.org/list/math/recent ; selected arXiv abstract and HTML pages linked above; arXiv Atom API metadata for version, dates, categories, comments, and publication fields; targeted web searches for independent discussion; Semantic Scholar Graph API requested for citation and related metadata. Retrieval note: the Semantic Scholar Graph endpoint was rate-limiting requests, so no metrics are reported. No selected record exposed a journal reference or DOI in the arXiv metadata checked.
