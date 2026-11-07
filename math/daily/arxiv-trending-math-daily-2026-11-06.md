# arXiv Mathematics — Friday, 6 November 2026

## Headline

Daily report for the latest available announcement batch (Friday, 6 November): 12 papers selected from 409 mathematics-listing entries (406 new submissions and 3 revisions). The most striking pattern is a cluster of sharp threshold results, especially two independent papers on Tusnády discrepancy; the spoken agenda is weak randomness, geometric and combinatorial thresholds, and where the new theorems still leave gaps. This is an inferred ranking, not an official arXiv trending chart; recent papers have little usable citation history, and only one selected paper yielded an independent quantitative attention signal.

## Top papers (ranked)

### 1. [Quadratic Extractors](https://arxiv.org/abs/2611.07266)
- **Abstract:** For quadratic sources over \(\mathbb F_2^n\), the authors give an explicit extractor whose min-entropy requirement is polylogarithmic in \(n\), far below the previous roughly \(n-\sqrt{\log n}\) requirement.
- **Authors:** Gautam Chandrasekaran, Jesse Goodman, David Zuckerman
- **arXiv:** `2611.07266v1` (published 2026-11-05T00:36:24Z; categories: `cs.CC`, `cs.CR`, `math.CO`)
- **Evidence for ranking:** The result crosses complexity, cryptography, and combinatorics and directly improves a long-standing parameter barrier. The independent ECCC report TR26-303 displayed 146 downloads when checked; this is an ECCC report count, not an arXiv download or citation count.
- **Claimed result:** The authors' Theorem 1.3 gives an explicit extractor for quadratic sources at min-entropy at least \(\log^C n\), with error \(n^{-\Omega(1)}\); they describe it as the first construction beyond the sumset-extractor barrier.
- **Assumptions and setting:** The source is the image of hidden uniform bits under a map of \(n\) quadratic polynomials over \(\mathbb F_2\); this is a structured-source result, not an extractor for arbitrary weak sources.
- **Caveat:** The theorem is limited to the quadratic-source model; it does not bypass the impossibility of deterministic extraction from unrestricted weak sources.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Combinatorics & discrete mathematics

### 2. [Pointless K3 surfaces over finite fields](https://arxiv.org/abs/2611.08356)
- **Abstract:** The authors prove that a K3 surface without an \(\mathbb F_q\)-rational point exists exactly when \(q\le 11\), using lattice bounds, the Artin–Tate formula, and Niemeier-lattice embeddings.
- **Authors:** Asher Auel, Philip Engel, Kiran S. Kedlaya, Sair Shaikh
- **arXiv:** `2611.08356v1` (published 2026-11-05T17:36:46Z; categories: `math.NT`, `math.AG`)
- **Evidence for ranking:** A clean if-and-only-if cutoff in arithmetic geometry, supported by a second mathematical area (number theory) and a concrete downstream improvement to a rational-point bound for threefold results.
- **Claimed result:** The authors' Theorem 1 proves existence of pointless K3 surfaces over \(\mathbb F_q\) if and only if \(q\le 11\), improving the prior general Weil-bound cutoff.
- **Assumptions and setting:** Smooth K3 surfaces over finite fields; the statement concerns existence of at least one surface for each field size.
- **Caveat:** The proof uses numerical computations, with code and data linked by the authors; they also note an independent proof and say the relationship between the two proof approaches is not worked out.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Algebra & number theory; Geometry & topology

### 3. [Resolving Tusnády's Problem](https://arxiv.org/abs/2611.06998)
- **Abstract:** The paper proves the missing higher-dimensional lower bound for combinatorial discrepancy of axis-parallel boxes, which together with the known upper bound and planar result gives the sharp order in every fixed dimension \(d\ge2\).
- **Authors:** Nicola Wengiel
- **arXiv:** `2611.06998v1` (published 2026-11-04T18:58:56Z; categories: `math.CA`, `cs.CG`, `cs.DS`, `math.CO`)
- **Evidence for ranking:** The authors claim to close a longstanding logarithmic-factor gap for every fixed dimension \(d\ge3\); the result is cross-listed across analysis, computational geometry, algorithms, and combinatorics.
- **Claimed result:** Theorem 1.1 gives a lower bound \(\Omega_d((\log N)^{d-1/2})\) for anchored-box discrepancy when \(d\ge3\); combined with Nikolov's upper bound and Wei's planar result, the authors conclude \(\Theta_d((\log N)^{d-1/2})\) for axis-parallel boxes for all fixed \(d\ge2\).
- **Assumptions and setting:** Worst-case discrepancy of finite \(N\)-point sets, with dimension fixed as \(N\) grows; constants and the threshold may depend on dimension.
- **Caveat:** The new lower-bound theorem is for fixed \(d\ge3\), and the constants are not optimized or uniform in dimension; the full conclusion also uses previously established upper and planar bounds.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Combinatorics & discrete mathematics

### 4. [Tusnády's problem and online two-sample thinning](https://arxiv.org/abs/2611.08455)
- **Abstract:** The paper proves the sharp fixed-dimensional Tusnády discrepancy order, a robust random-sample lower bound, and minimax rates for online thinning of two samples from an unknown common distribution.
- **Authors:** Yuhao Lei
- **arXiv:** `2611.08455v1` (published 2026-11-05T18:47:43Z; categories: `math.CO`, `cs.DS`, `math.PR`)
- **Evidence for ranking:** The cross-listing connects discrepancy, algorithms, and probability; beyond the sharp-box result, the paper provides explicit online prefix and terminal guarantees under a deletion budget.
- **Claimed result:** For fixed dimension \(k\) and expected deletion budget \(\rho n\), \(0<\rho<2\), the authors obtain minimax expected prefix discrepancy \(\Theta_{k,\rho}((\log n)^{k+1/2})\); in one dimension the optimal terminal rate is \(\Theta_\rho((\log\log n)^{3/2})\).
- **Assumptions and setting:** Two independent size-\(n\) samples from the same unknown distribution; decisions to keep or discard observations are online and irrevocable.
- **Caveat:** For dimensions \(k\ge2\), the paper's terminal upper and lower bounds still differ by a factor of \(\log n\). Its sharp Tusnády theorem also appears independently in paper 3 of this batch.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics

### 5. [Rational Turán exponents of a single \(k\)-uniform hypergraph](https://arxiv.org/abs/2611.07290)
- **Abstract:** For every integer \(k\ge2\) and rational \(r\in[0,1]\), the authors construct a single forbidden \(k\)-uniform hypergraph whose extremal number has order \(n^{k-r}\), and give an obstruction for part of the larger-exponent range.
- **Authors:** Chang Liu, Jue Dai
- **arXiv:** `2611.07290v1` (published 2026-11-05T01:12:41Z; categories: `math.CO`)
- **Evidence for ranking:** It extends a central rational-exponent realization from graphs to uniform hypergraphs in the single-forbidden-object setting, with an accompanying Lean 4 formalization.
- **Claimed result:** For each rational \(r\in[0,1]\), the authors prove existence of \(F_{k,r}\) with \(\mathrm{ex}_k(n,F_{k,r})=\Theta(n^{k-r})\); they also rule out such a single-\(F\) realization when \(k\ge4\) and \(\lceil k/2\rceil<r\le k-1\).
- **Assumptions and setting:** Fixed uniformity \(k\), rational exponent, and the standard extremal number for avoiding one finite hypergraph.
- **Caveat:** The Lean formalization is conditional on two explicitly stated axioms; the result covers \(r\in[0,1]\), while the paper gives a nonexistence obstruction only on the stated higher range.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Combinatorics & discrete mathematics

### 6. [Weak uniqueness for the stochastic heat equation with nondegenerate diffusion: the full Hölder regime](https://arxiv.org/abs/2611.07310)
- **Abstract:** For the scalar stochastic heat equation on the one-dimensional torus, the authors prove weak well-posedness for uniformly nondegenerate diffusion coefficients of every positive Hölder order and extend results to measurable drifts of linear growth.
- **Authors:** Yi Han
- **arXiv:** `2611.07310v1` (published 2026-11-05T01:55:58Z; categories: `math.PR`)
- **Evidence for ranking:** It closes the positive-Hölder regularity range left by the author's earlier result and provides a linked Lean formalization, making it a substantial stochastic-analysis result with a checkable proof artifact.
- **Claimed result:** Theorem 1.1 establishes existence and uniqueness in law for bounded, uniformly nondegenerate Hölder diffusion at every exponent \(\beta>0\); Theorem 1.2 treats additional measurable linear-growth drifts and certain unbounded diffusions.
- **Assumptions and setting:** Scalar equation driven by space-time white noise on the one-dimensional torus; the main theorem assumes deterministic \(L^2\) initial data and diffusion bounded above and away from zero.
- **Caveat:** The result is weak uniqueness (uniqueness in law), not pathwise uniqueness; the unbounded-diffusion extension uses bounded initial data in the stated case.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Analysis & PDE; Probability & statistics

### 7. [On do Carmo's Question: The Properly Embedded Case](https://arxiv.org/abs/2611.08454)
- **Abstract:** Every complete noncompact, two-sided, properly embedded constant-mean-curvature hypersurface of finite Morse index in Euclidean space is shown to be minimal, in every dimension.
- **Authors:** Gongping Niu
- **arXiv:** `2611.08454v1` (published 2026-11-05T18:47:40Z; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** The author claims a full-dimensional resolution of the properly embedded finite-index case without curvature or volume-growth bounds, linking differential geometry with geometric PDE.
- **Claimed result:** The paper proves that a complete, noncompact, two-sided, properly embedded CMC hypersurface of finite Morse index in Euclidean space has zero mean curvature.
- **Assumptions and setting:** Euclidean ambient space of arbitrary dimension; completeness, noncompactness, two-sidedness, proper embeddedness, and finite Morse index are all required.
- **Caveat:** This is the properly embedded case; it does not establish the corresponding statement for general immersed or non-proper hypersurfaces.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Geometry & topology; Analysis & PDE

### 8. [Gelfand numbers of Schatten class embeddings in the quasi-Banach range](https://arxiv.org/abs/2611.08448)
- **Abstract:** The paper proves a 2022 conjectured lower bound for finite-dimensional Schatten-class embeddings when \(0<p\le1\), yielding exact asymptotic orders in the previously unresolved range.
- **Authors:** Joscha Prochno
- **arXiv:** `2611.08448v1` (published 2026-11-05T18:43:22Z; categories: `math.FA`)
- **Evidence for ranking:** It resolves a named conjecture and, with the cited earlier upper estimate, completes the all-index asymptotic description for these embeddings.
- **Claimed result:** The author proves Conjecture 1.4 of Prochno and Strzelecki for indices bounded away from the ambient dimension by a fixed proportion, uniformly for target exponent \(2\le q\le\infty\); together with known upper estimates this yields the exact order.
- **Assumptions and setting:** Gelfand numbers of embeddings between finite-dimensional Schatten classes, in the quasi-Banach range \(0<p\le1\); target exponent \(q\ge2\).
- **Caveat:** The new lower bound has the stated proportional separation from ambient dimension; the all-index conclusion combines this paper with prior estimates rather than a single new bound covering every case.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Analysis & PDE

### 9. [Exotic smooth structures on complex projective spaces](https://arxiv.org/abs/2611.08406)
- **Abstract:** The authors give evidence for the conjecture that every \(\mathbb{CP}^n\), \(n>3\), admits an exotic smooth structure: the dimensions with such structures have natural density one, and 266 residue classes modulo 288 are covered.
- **Authors:** Yueshi Hou, Hana Jia Kong, Zhouli Xu
- **arXiv:** `2611.08406v1` (published 2026-11-05T18:13:47Z; categories: `math.AT`)
- **Evidence for ranking:** A concrete density-one result and a large explicit congruence-class construction turn a broad smooth-topology conjecture into a sharply quantified partial classification.
- **Claimed result:** The authors prove density one of complex dimensions admitting an exotic smooth structure and identify 266 congruence classes modulo 288, covering more than 92% of dimensions \(n>3\).
- **Assumptions and setting:** Smooth structures on the topological manifold underlying complex projective space, with dimensions \(n>3\); the proof uses stable cohomotopy and height-two chromatic computations.
- **Caveat:** The authors' conjecture that every dimension \(n>3\) works remains open; density one and the listed residue classes do not settle the exceptional dimensions.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Geometry & topology

### 10. [Two-row Schur times Schubert via parallel classes of positroid varieties](https://arxiv.org/abs/2611.07351)
- **Abstract:** The author gives a positive combinatorial formula for Schubert structure constants when one indexing partition has two rows, using increasing chains and parallel classes of positroid varieties.
- **Authors:** Tianyi Yu
- **arXiv:** `2611.07351v1` (published 2026-11-05T02:39:18Z; categories: `math.CO`, `math.AG`)
- **Evidence for ranking:** It resolves a specifically identified next case in the problem of positive formulas for Schubert structure constants and is cross-listed in combinatorics and algebraic geometry.
- **Claimed result:** The paper expresses the relevant two-row coefficients through Kostka numbers and combinatorial data from increasing chains and positroid parallel classes.
- **Assumptions and setting:** Schubert structure constants for complete flag varieties, with the second Schur/partition index restricted to a two-row partition.
- **Caveat:** The result addresses the two-row case, not a general positive formula for arbitrary indexing partitions.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 11. [Bergman Kernel Zeros on Rational Hartogs Triangles](https://arxiv.org/abs/2611.07480)
- **Abstract:** For relatively prime positive integers \(m>n\), the authors prove the Edholm–Mathew polynomial nonvanishing conjecture and characterize exactly when the associated rational Hartogs triangle has a zero-free Bergman kernel.
- **Authors:** Guantie Deng, Qian Fu
- **arXiv:** `2611.07480v1` (published 2026-11-05T05:38:43Z; categories: `math.CV`)
- **Evidence for ranking:** The paper resolves a named conjecture with an explicit positivity bound and a precise if-and-only-if classification for the rational family.
- **Claimed result:** The authors prove strict positivity of the associated trigonometric polynomial, deduce exactly \(m-n\) zeros in the punctured unit disc, and show the Hartogs triangle has zero-free Bergman kernel precisely when its exponent is the reciprocal of a positive integer.
- **Assumptions and setting:** Rational Hartogs triangles parameterized by relatively prime positive integers \(m>n\); zeros are counted with multiplicity.
- **Caveat:** The criterion is for this rational family and does not establish the corresponding classification for more general domains.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Analysis & PDE

### 12. [An Accelerated Proximal Gradient Method for Bures-Wasserstein Space](https://arxiv.org/abs/2611.08468)
- **Abstract:** By lifting suitable composite optimization problems on the Bures–Wasserstein space of Gaussian measures to Euclidean affine-transport maps, the authors obtain an accelerated method with an \(O(k^{-2})\) objective-gap rate.
- **Authors:** Jakob Nylöf, Sloan Nietert, Julien Pallage, Giancarlo Ferrari-Trecate, Daniel Kuhn, John Lygeros
- **arXiv:** `2611.08468v1` (published 2026-11-05T18:55:10Z; categories: `math.OC`)
- **Evidence for ranking:** The arXiv comment reports acceptance to a NeurIPS 2026 workshop; the paper states a minimax-optimal rate for a defined class and an improvement for Gaussian variational inference.
- **Claimed result:** Under convex smooth/proximable affine-lift assumptions, BW-FISTA achieves objective gap \(O(k^{-2})\); for Gaussian variational inference with a log-concave, log-smooth target, the authors improve the stated rate from \(O(k^{-1})\) to \(O(k^{-2})\).
- **Assumptions and setting:** Composite optimization over Gaussian measures in Bures–Wasserstein space, with the stated convexity and affine-lift regularity; the variational-inference application assumes a log-concave, log-smooth target.
- **Caveat:** Guarantees depend on those lift and regularity conditions; the paper's abstract reports synthetic numerical experiments rather than broad empirical validation.
- **Announcement type:** new submission, announcement-batch 2026-11-06
- **Themes:** Optimization & control

## Trending Research Themes

- **Two independent Tusnády papers in one batch:** Wengiel's lower-bound argument and Lei's robust-sample extension both state the sharp \(\Theta_d((\log N)^{d-1/2})\) order. Lei additionally studies online thinning; the papers use different proof routes, so this is a convergence on a problem, not evidence of a shared technique. [2611.06998](https://arxiv.org/abs/2611.06998), [2611.08455](https://arxiv.org/abs/2611.08455)
- **Sharp thresholds and explicit constructions:** The quadratic extractor, rational Turán exponents, and exotic \(\mathbb{CP}^n\) papers move explicit parameter boundaries in three different settings—structured randomness, forbidden hypergraphs, and smooth topology. Their methods are not interchangeable, but each gives a concrete theorem rather than a broad conjectural claim. [2611.07266](https://arxiv.org/abs/2611.07266), [2611.07290](https://arxiv.org/abs/2611.07290), [2611.08406](https://arxiv.org/abs/2611.08406)
- **Proof artifacts and computation:** The stochastic-heat and Turán papers link Lean formalizations (the latter conditional on two stated axioms); the K3 paper supplies numerical code/data. These tools improve inspectability but have different scopes and do not substitute for checking the mathematical hypotheses. [2611.07310](https://arxiv.org/abs/2611.07310), [2611.07290](https://arxiv.org/abs/2611.07290), [2611.08356](https://arxiv.org/abs/2611.08356)
- **Isolated but notable geometric analysis:** The finite-index CMC result [2611.08454](https://arxiv.org/abs/2611.08454) and the Bures–Wasserstein optimization method [2611.08468](https://arxiv.org/abs/2611.08468) are strong single-paper signals in their respective fields, not evidence of a wider shift.

## Open Problems and Research Directions

- **Open problem (authors' stated gap):** For online two-sample thinning in dimensions \(k\ge2\), the terminal discrepancy bounds still differ by a factor of \(\log n\). A follow-up could seek a matching terminal algorithm or lower bound, separately from the already sharp prefix rate. [2611.08455](https://arxiv.org/abs/2611.08455)
- **Open problem (authors' conjecture):** The exotic-smoothing conjecture for \(\mathbb{CP}^n\) remains unresolved in the exceptional dimensions outside the 266 listed classes. A concrete direction is to analyze the uncovered residue classes and identify whether the obstruction is arithmetic or genuinely smooth-topological. [2611.08406](https://arxiv.org/abs/2611.08406)
- **Open problem (authors' discussion):** The K3 paper notes that its Artin–Tate/lattice argument and the independent Brandhorst–Takada proof appear closely related, but leaves that relation unexplained. Comparing the two frameworks may yield sharper or more reusable rational-point bounds. [2611.08356](https://arxiv.org/abs/2611.08356)
- **Open boundary (authors' result):** The single-forbidden-hypergraph realization is established for rational \(r\in[0,1]\), while the paper proves impossibility for \(k\ge4\), \(\lceil k/2\rceil<r\le k-1\). The intervening ranges, where not already covered by prior work, invite constructions or further obstructions. [2611.07290](https://arxiv.org/abs/2611.07290)
- **Research direction (synthesis):** The two-row Schubert formula leaves a natural next test: determine whether the increasing-chain/positroid approach extends to three-row partitions or which obstruction first appears. This is a proposed extension, not a claim made by the paper. [2611.07351](https://arxiv.org/abs/2611.07351)

## Takeaway

The standout mathematical story is unusually concrete: new papers claim sharp discrepancy bounds, a cutoff classification for pointless K3 surfaces, and large parameter improvements for structured extraction and hypergraph extremal numbers. The order should not be mistaken for measured popularity: arXiv supplies no trending chart, citation evidence is immature, and the strongest independent attention observation is a single ECCC report count.

## Method and sources

- **Window:** Daily, announcement batch Friday 2026-11-06; the latest listing shown on Saturday 2026-11-07, so this uses the prior available batch (no 7 November batch was shown). Batch window: 2026-11-06 through 2026-11-06. Snapshot: 2026-11-07 01:32:33 UTC.
- **Coverage:** The complete latest `math` recent-listing batch was traversed: 409 entries, including `math.*` primaries and neighboring categories only when cross-listed in mathematics. The batch contains 406 v1 submissions and 3 revisions. The report selects 12 papers; it is not an exhaustive representation of mathematics.
- **Ranking:** Inferred from an evidence hierarchy of independent attention, then concrete theorem/conjecture resolution, cross-list relevance, and checkable proof/acceptance artifacts. The ECCC report for Quadratic Extractors displayed 146 downloads when checked; no Semantic Scholar citation momentum is used because usable citation evidence was not established for these very recent submissions. No popularity claim is made from arXiv ordering.
- **Abstract and paper text:** Selected abstract pages were checked directly at arXiv; introductions and main-result statements were inspected in arXiv HTML for the leading theorem papers. Proofs were not independently verified. The configured `web_extract` backend could not extract the arXiv pages, so live arXiv browser pages and the arXiv API were used instead.
- **Sources:** [arXiv mathematics recent listing](https://arxiv.org/list/math/recent); individual canonical abstract pages linked in each entry; [ECCC TR26-303, Quadratic Extractors](https://eccc.weizmann.ac.il/report/2026/303/).
