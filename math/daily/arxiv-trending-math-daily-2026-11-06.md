# arXiv Mathematics — Friday, 6 November 2026

## Headline

Latest available daily announcement batch: Friday, 6 November 2026; 5 notable papers selected from 409 entries. The strongest pattern is precise theorem-making—sharp discrepancy rates, finite-field classification, and geometric bounds—with a smaller proof-method signal in AI-assisted numerical analysis. Spoken agenda: discrepancy and online thinning, K3 rational points, geometric rigidity, and proof verification. arXiv publishes no official trending chart, so this is an inferred order; the papers are very new and citation evidence is limited.

## Top papers (ranked)

### 1. [Tusnády’s problem and online two-sample thinning](https://arxiv.org/abs/2611.08455)
- **Abstract:** The author proves the sharp fixed-dimension Tusnády discrepancy order, a robust lower bound for random samples, and minimax online-thinning rates for two samples from an unknown common distribution.
- **Authors:** Yuhao Lei
- **arXiv:** `2611.08455v1` (published 2026-11-05T18:47:43Z; categories: `math.CO` (primary), `cs.DS`, `math.PR`)
- **Evidence for ranking:** A dedicated Polymath Hub discussion is an independent attention signal; the result also links combinatorial discrepancy, algorithms, and probability. The paper claims a sharp order and gives explicit online prefix/terminal guarantees.
- **Claimed result:** The author proves that box discrepancy is \(\Theta_d((\log N)^{d-1/2})\) for every fixed \(d\ge2\). For online thinning with fixed \(k\ge1\) and expected deletion budget \(\rho n\), \(0<\rho<2\), the minimax expected prefix discrepancy is \(\Theta_{k,\rho}((\log n)^{k+1/2})\); in one dimension the terminal rate is \(\Theta_\rho((\log\log n)^{3/2})\).
- **Assumptions and setting:** The discrepancy order holds with dimension fixed. Thinning concerns two independent size-\(n\) samples from the same unknown Borel distribution; keep/discard choices are online and irrevocable.
- **Caveat:** For \(k\ge2\), the paper's terminal upper and lower bounds still differ by a factor of \(\log n\).
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 2. [Pointless K3 surfaces over finite fields](https://arxiv.org/abs/2611.08356)
- **Abstract:** The authors prove that a K3 surface without an \(\mathbb F_q\)-rational point exists if and only if \(q\le11\), using lattice bounds, the Artin–Tate formula, and embeddings into Niemeier lattices.
- **Authors:** Asher Auel, Philip Engel, Kiran S. Kedlaya, Sair Shaikh
- **arXiv:** `2611.08356v1` (published 2026-11-05T17:36:46Z; categories: `math.NT` (primary), `math.AG`)
- **Evidence for ranking:** The exact cutoff is independently reached in another recent arXiv paper, by Brandhorst and Takada, using a different approach; this convergence and the number-theory/algebraic-geometry link are checkable signals. A public mathematics account also highlighted the submission. This paper itself notes that the relation between the two proofs is not yet understood.
- **Claimed result:** The authors’ Theorem 1 establishes existence of pointless K3 surfaces over \(\mathbb F_q\) exactly for prime powers \(q\le11\), sharpening the general Weil-bound cutoff and improving a bound used in related threefold results.
- **Assumptions and setting:** Smooth K3 surfaces over finite fields; the theorem concerns existence of at least one pointless surface for each field size.
- **Caveat:** The proof uses numerical linear-programming certificates and lattice computations; the authors provide code/data and describe a separate proof of the same cutoff.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Algebra & number theory; Geometry & topology

### 3. [On do Carmo’s Question: The Properly Embedded Case](https://arxiv.org/abs/2611.08454)
- **Abstract:** The author proves that every complete, noncompact, two-sided, properly embedded constant-mean-curvature hypersurface of finite Morse index in Euclidean space is minimal, in every dimension.
- **Authors:** Gongping Niu
- **arXiv:** `2611.08454v1` (published 2026-11-05T18:47:40Z; categories: `math.DG` (primary), `math.AP`)
- **Evidence for ranking:** A differential-geometry papers account independently highlighted it, and the result connects differential geometry with geometric PDE. The claimed theorem removes curvature and volume-growth bounds in the properly embedded finite-index case.
- **Claimed result:** The author’s main theorem says the mean curvature must vanish under the stated hypotheses. The proof uses the inscribed-ball radius to build a weight, combines a weighted-volume estimate with stability outside a compact set, and derives a contradiction if the mean curvature is nonzero.
- **Assumptions and setting:** Smooth connected hypersurfaces without boundary in Euclidean space, arbitrary dimension; completeness, noncompactness, two-sidedness, proper embeddedness, and finite Morse index are required.
- **Caveat:** Proper embeddedness is essential to the presented argument; the broader finite-index question for general immersed hypersurfaces remains open.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Geometry & topology; Analysis & PDE

### 4. [Improved Index and Intersection bounds for Min-Max Geodesics](https://arxiv.org/abs/2611.08450)
- **Abstract:** The authors improve a bound for geodesics realizing the \(p\)-widths of a closed surface, showing that the sum of their Morse indices and a count of their intersections is at most \(p\).
- **Authors:** Lorenzo Sarnataro, Douglas Stryker, Jared Marx-Kuo
- **arXiv:** `2611.08450v1` (published 2026-11-05T18:44:58Z; categories: `math.DG` (primary))
- **Evidence for ranking:** It was included in a public differential-geometry papers roundup and gives a concrete improvement over the authors’ previous bound. Its method combines geodesic Jacobi-field variations with localized variations near intersection vertices.
- **Claimed result:** Theorem 1.2 bounds the sum of the Morse indices plus the sum, over intersection vertices, of squared vertex orders by \(p\), for a collection of closed immersed geodesics realizing the \(p\)-width of a closed Riemannian surface.
- **Assumptions and setting:** Closed Riemannian surfaces and geodesic unions arising as \(p\)-width limits; the theorem also applies to the Allen–Cahn limit-varifold setting described by the authors.
- **Caveat:** The stated min-max application is for surfaces and geodesics realizing \(p\)-widths; it does not establish analogous bounds in higher ambient dimensions.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Geometry & topology

### 5. [A stability order barrier and SSP bound for Runge–Kutta methods with non-negative coefficients: AI-assisted proofs](https://arxiv.org/abs/2611.07981)
- **Abstract:** The authors prove SSP-coefficient bounds for implicit Runge–Kutta methods with non-negative coefficients, settle a conjecture at order two, and show that third-order methods with non-negative \(A\) and \(b\) cannot be algebraically stable.
- **Authors:** Sigal Gottlieb, Zachary Grant, Lior Horesh, Lajos Lóczi, Avraham Shinnar, Barry Trager
- **arXiv:** `2611.07981v1` (published 2026-11-05T13:12:03Z; categories: `math.NA` (primary))
- **Evidence for ranking:** A named conjecture is claimed settled, and the paper documents an unusual mathematical bridge from SSP conditions to phase-type distributions. Its introduction says elementary proof components and reductions were machine-verified in Lean 4; that is a proof artifact, not a measure of popularity.
- **Claimed result:** For every \(s\)-stage implicit Runge–Kutta method of order at least two with non-negative coefficients, the SSP coefficient is at most \(2s\), sharply attained at order two; the paper also gives a bound for order at least three and rules out third-order algebraic stability when \(A\) and \(b\) are entrywise non-negative.
- **Assumptions and setting:** Implicit Runge–Kutta methods with non-negative coefficients; the three claims have the distinct order and coefficient hypotheses stated above.
- **Caveat:** The authors report Lean verification for elementary components and reductions, not the entire paper as a formal proof; the results are restricted to the specified non-negative-coefficient classes.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Numerical analysis & computation

## Trending Research Themes

- **Discrepancy meets online algorithms:** Lei’s paper proves the fixed-dimensional sharp Tusnády order and extends it to two-sample thinning. A separate recent preprint by Wengiel also claims the sharp discrepancy order, so there is a concentrated burst of work on this problem; the papers use different routes, not one shared method. [Lei](https://arxiv.org/abs/2611.08455); [Wengiel](https://arxiv.org/abs/2611.06998).
- **A finite-field K3 cutoff, independently established:** Auel–Engel–Kedlaya–Shaikh and Brandhorst–Takada both give the cutoff \(q\le11\) for pointless K3 surfaces, with differing methods. The first paper explicitly leaves the relationship between the approaches open; this is a focused convergence, not evidence of a wider shift in arithmetic geometry. [Auel et al.](https://arxiv.org/abs/2611.08356); [Brandhorst–Takada](https://arxiv.org/abs/2611.06366).
- **Two separate geometric-analysis results:** Niu treats finite-index CMC hypersurfaces, while Sarnataro–Stryker–Marx-Kuo improve a min-max geodesic bound on surfaces. Both sharpen geometric structure statements, but they address distinct settings and do not establish a shared technique. [Niu](https://arxiv.org/abs/2611.08454); [Sarnataro et al.](https://arxiv.org/abs/2611.08450).
- **Proof methods as a single-paper signal:** The Runge–Kutta paper connects SSP theory with phase-type distributions and reports partial Lean verification. This is an interesting isolated signal, not enough to infer a field-wide shift toward AI-assisted proofs. [Gottlieb et al.](https://arxiv.org/abs/2611.07981).

## Open Problems and Research Directions

- **Author-stated gap:** In online thinning for dimensions \(k\ge2\), terminal discrepancy bounds differ by a factor of \(\log n\). A direct next test is whether an improved terminal algorithm or a stronger lower bound closes the gap without changing the already sharp prefix rate. [Lei](https://arxiv.org/abs/2611.08455).
- **Author-stated open case:** Niu notes that the finite-index result for general immersed CMC hypersurfaces would follow if one could construct an appropriate positive weight without proper embeddedness. Constructing such a weight, or finding an obstruction to it, would address the larger version of do Carmo’s question. [Niu](https://arxiv.org/abs/2611.08454).
- **Author-stated connection:** The K3 paper says the relation between its Artin–Tate/lattice proof and the independent Brandhorst–Takada proof is not worked out. Comparing their intermediate lattice constraints could clarify which parts yield reusable rational-point bounds. [Auel et al.](https://arxiv.org/abs/2611.08356); [Brandhorst–Takada](https://arxiv.org/abs/2611.06366).
- **Research direction (synthesis):** The min-max index/vertex estimate is formulated on surfaces; testing whether analogous combined bounds hold for higher-dimensional minimal hypersurfaces would probe the role of vertex desingularization and Jacobi-field variations. This is a proposed extension, not a claim of the paper. [Sarnataro et al.](https://arxiv.org/abs/2611.08450).

## Takeaway

The clearest attention signal is the sharp discrepancy result and its online-thinning extension; the other strong entries are theorem-led, with an independent two-paper convergence on the K3 cutoff. The ordering is a qualitative inference from discussion and mathematical signals, not measured readership, and these preprints’ claims still require expert scrutiny.

## Method and sources

- **Window:** Daily, 2026-11-06 through 2026-11-06; the latest batch available on Saturday 2026-11-07 was Friday’s announcement batch, so this is a prior batch. Snapshot time: 2026-11-07 17:21:44 UTC.
- **Coverage:** Traversed the complete Friday Mathematics recent-listing block (409 entries). Scope is the arXiv `math` archive, retaining neighboring-category cross-lists only for mathematics papers. The five selected entries are all new submissions; the report is a selective digest, not a comprehensive survey.
- **Ranking:** Labeled “notable recent papers” in substance because the new batch is too young for a useful citation-momentum ranking. Relative order weighs independent discussion or convergence first, then concrete theorem/conjecture resolution, cross-subfield relevance, and proof artifacts; no popularity inference is drawn from arXiv order. Semantic Scholar citation data was not usable for this snapshot (the Graph API returned HTTP 429), so no citation totals are used.
- **Reading and verification:** Each selected arXiv abstract page was checked for version, authors, categories, and submission timestamp. The introductions and main-result statements were inspected for the leading papers; the do Carmo introduction was extracted from the arXiv PDF. Proofs were not independently verified.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); selected arXiv abstract pages linked above; [Polymath Hub discussion of Tusnády’s problem](https://pol.polaimath.com/science/21906-tusnadys-problem-and-online-two-sample-thinning/); [K3 discussion mention](https://x.com/PQBW/status/2118761240629518730); [differential-geometry paper roundup](https://x.com/mathDGb/status/2118575565804392664); [do Carmo discussion mention](https://x.com/GeometryPapers/status/2118783855498760536).
