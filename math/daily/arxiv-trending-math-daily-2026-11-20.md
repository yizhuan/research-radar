# arXiv Mathematics — daily notable papers (20 November 2026)

## Headline

Today's arXiv Mathematics (`math`) announcement batch (Friday, 20 November 2026): 10 notable recent papers selected from 405 entries. The strongest pattern is precise bounds and conjecture-oriented results, spanning harmonic analysis, topology, percolation, and combinatorics. Spoken agenda: sharp estimates first, then exact probability and structural results, and finally the formalization/AI thread. This is an inferred, evidence-weighted ordering—not an official arXiv trending chart—and citation evidence is sparse for papers announced today; it is not a readership ranking.

## Top papers (ranked)

### 1. [Amplitude dependent wave envelope type estimates for moment curves and applications](https://arxiv.org/abs/2611.26581)
- **Abstract:** The authors prove amplitude-dependent wave-envelope estimates for moment curves in arbitrary dimensions and derive sharp small-cap decoupling for dimensions n ≥ 4, resolving the Demeter–Guth–Wang exponential-sum conjecture in all dimensions.
- **Authors:** Sangwon Jeong, Changkeun Oh
- **arXiv:** `2611.26581v1` (published Thu, 19 Nov 2026 18:43:18 UTC; categories: `math.CA`)
- **Evidence for ranking:** The paper reports an all-dimensional conjecture resolution, with new sharp small-cap estimates for n ≥ 4; its proof builds on sharp square-function estimates, giving a specific mathematical basis for prominence.
- **Claimed result:** The authors prove amplitude-dependent wave-envelope-type estimates and use them to establish sharp small-cap decoupling for the moment curve in every dimension n ≥ 4; they state this completes the Demeter–Guth–Wang conjecture on exponential sums across dimensions.
- **Assumptions and setting:** The estimates concern the moment curve; the new small-cap theorem is stated for dimensions n ≥ 4 and uses prior sharp square-function estimates.
- **Caveat:** The result is a preprint claim; its main argument depends on the cited square-function estimates, and the full proof has not been independently assessed here.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Analysis & PDE

### 2. [Sharp topological overlap in every dimension](https://arxiv.org/abs/2611.26229)
- **Abstract:** For continuous and affine maps from high-dimensional simplices to R^d, the authors determine the optimal asymptotic fraction of d-faces whose images share a point, obtaining (d+1)!/(d+1)^(d+1) in every dimension.
- **Authors:** Sergey Norin
- **arXiv:** `2611.26229v1` (published Thu, 19 Nov 2026 15:04:17 UTC; categories: `math.CO`, `cs.CG`)
- **Evidence for ranking:** The exact formula settles the Bukh–Matoušek–Nivasch conjecture for the affine constant while matching it with the topological constant; the author also links a Lean formalization, an unusually concrete verification artifact for this result.
- **Claimed result:** The author proves c_d^top = c_d^aff = (d+1)!/(d+1)^(d+1) for every integer d ≥ 1, confirming the cited conjecture.
- **Assumptions and setting:** The constants are asymptotic minima over maps from the n-simplex to R^d as n tends to infinity; the topological case allows every continuous map, while the affine case restricts to affine maps.
- **Caveat:** The preprint reports that AI helped discover the proof under the author's direction. The linked Lean formalization is described as based on an earlier draft, so it should not be treated as a formal check of every detail of this exact version without comparing the texts.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 3. [On Romik's rationality conjectures for critical percolation](https://arxiv.org/abs/2611.26570)
- **Abstract:** For nested-arch events in the critical-percolation loop representation, the authors derive Pfaffian formulas that imply rational dependence on cylinder circumference and rational limiting probabilities in the half-plane.
- **Authors:** Melda Akyazi-Zavadski, Nathanaël Berestycki, Sunil Chhita
- **arXiv:** `2611.26570v1` (published Thu, 19 Nov 2026 18:36:31 UTC; categories: `math.PR`, `math-ph`, `math.CO`)
- **Evidence for ranking:** The paper combines three subject areas and reports explicit formulas for a family of probabilities, proving key parts of a named conjecture rather than only offering numerical evidence.
- **Claimed result:** For k nested arches on a semi-infinite cylinder of circumference 2N, with k < N, the authors give Pfaffian formulas and prove rational-function dependence on N; the corresponding half-plane probabilities are rational.
- **Assumptions and setting:** The model is the completely packed O(1) loop representation of critical bond percolation on the square lattice; the stated cylinder result covers k < N.
- **Caveat:** The paper does not establish Romik's predicted denominator properties or dyadic rationality, and excludes the boundary case N = k. The authors note that Dan Romik separately obtained a full solution with AI, to be reported in forthcoming work; that result is not established by this preprint.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Probability & statistics; Mathematical physics; Combinatorics & discrete mathematics

### 4. [An asymptotic bound for Yuster's independent transversal factor conjecture](https://arxiv.org/abs/2611.26259)
- **Abstract:** For graphs split into r independent parts with pairwise matching edges, the author proves that a partition into independent transversals exists once the part size is at least r + O(r^(20/21)), for sufficiently large r.
- **Authors:** Xin Zhang
- **arXiv:** `2611.26259v1` (published Thu, 19 Nov 2026 15:32:17 UTC; categories: `math.CO`, `cs.DM`)
- **Evidence for ranking:** The bound gives a near-linear threshold and implies f(r)/r → 1, a direct asymptotic advance on a named factor conjecture; the result also crosses combinatorics and discrete mathematics.
- **Claimed result:** The author proves f(r) ≤ r + O(r^(20/21)) and hence f(r)/r → 1, where f(r) is the least part-size threshold guaranteeing a partition into independent transversals.
- **Assumptions and setting:** An [r,n,1]-graph has r independent parts of size n and a matching between each pair; the theorem is for all sufficiently large r and n ≥ ceil(r + A r^(20/21)) for an absolute A > 0.
- **Caveat:** This is an asymptotic form, not the exact threshold in Yuster's 2021 conjecture; the stated error term remains above the conjectured linear threshold.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Combinatorics & discrete mathematics

### 5. [Permanence and 144-periodicity of x_{153,3} in the stable stems at the prime three](https://arxiv.org/abs/2611.26621)
- **Abstract:** The author proves that a class in the 3-primary Adams–Novikov spectral sequence survives and generates a period-144 family, answering both parts of a question by Carrick and Davies.
- **Authors:** Zheyan Wan
- **arXiv:** `2611.26621v1` (published Thu, 19 Nov 2026 18:58:55 UTC; categories: `math.AT`)
- **Evidence for ranking:** The paper answers a stated question with both a permanence result and a periodic family, and supplies a concrete finite-spectrum lift with nonzero detector images.
- **Claimed result:** The author shows that x_{153,3}, in stable degree 153 and filtration 3, survives and begins a period-144 family; iterates have nonzero image in the specified height-two detector.
- **Assumptions and setting:** The setting is the 3-primary Adams–Novikov spectral sequence of the sphere; the argument uses comparison with periodic topological modular forms and a bound on possible differential targets.
- **Caveat:** The detector and permanence argument establish the claimed family in this specific 3-primary setting, not a general periodicity statement for stable stems.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Geometry & topology

### 6. [Algebraic matroids with non-algebraic duals exist in any positive characteristic](https://arxiv.org/abs/2611.26429)
- **Abstract:** The author constructs, over every positive-characteristic field, an algebraic matroid whose dual is not algebraic over any field, and uses it to separate two classes of polynomial supports.
- **Authors:** Lukas Grund
- **arXiv:** `2611.26429v1` (published Thu, 19 Nov 2026 15:04:17 UTC; categories: `math.CO`, `math.AG`)
- **Evidence for ranking:** The theorem is uniform over every positive characteristic and gives a strong non-realizability conclusion for the dual; its application connects matroid theory with algebraic geometry and volume polynomials.
- **Claimed result:** The author proves that for every field K of positive characteristic, some matroid algebraic over K has a dual that is not algebraic over any field; realizable volume- and covolume-polynomial support classes consequently differ.
- **Assumptions and setting:** The construction applies to fields of positive characteristic and uses matroids over one-dimensional algebraic groups.
- **Caveat:** This is an existence result in positive characteristic; the abstract does not classify such matroids or establish the same separation in characteristic zero.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 7. [Remark on Kobayashi's conjecture: a volume Schwarz lemma](https://arxiv.org/abs/2611.26524)
- **Abstract:** The author reconstructs an AI-assisted proof of Kobayashi's ampleness conjecture for compact Kähler manifolds and proves a volume comparison yielding a general-type criterion under a bounded-indicatrix hypothesis.
- **Authors:** Shiyu Zhang
- **arXiv:** `2611.26524v1` (published Thu, 19 Nov 2026 18:00:54 UTC; categories: `math.DG`, `math.CV`)
- **Evidence for ranking:** The paper spans differential and complex geometry, states a new volume Schwarz lemma and pointwise comparison, and draws a concrete birational-geometric consequence from them.
- **Claimed result:** The author claims that a compact Kähler manifold with nef canonical bundle and a bounded Kobayashi–Royden indicatrix at some point is of general type, as a consequence of the volume comparison.
- **Assumptions and setting:** The comparison assumes a Kähler metric with Ric(ω) ≥ −ω and uses intrinsic volume forms associated with Kähler–Einstein metrics on pseudoconvex domains containing the Kobayashi–Royden indicatrix.
- **Caveat:** The abstract describes an expository reconstruction of an AI-assisted proof plus new results; these remain preprint claims and require expert review, especially for the conjecture-level argument and its hypotheses.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Geometry & topology

### 8. [Generic arm separation for planar percolation models](https://arxiv.org/abs/2611.26458)
- **Abstract:** The authors give a model-independent exploration approach to arm separation for planar percolation and apply it to obtain a strong arm-separation result for critical planar FK percolation.
- **Authors:** Loïc Gassmann, Ioan Manolescu, Maran Mohanarangan
- **arXiv:** `2611.26458v1` (published Thu, 19 Nov 2026 17:22:05 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** It provides a reusable method across planar models and a specific critical FK application, while linking probability with mathematical physics.
- **Claimed result:** The authors prove a generic arm-separation statement for arbitrary planar percolation models by exploring conditioned configurations so exposed arms are revealed with positive probability, then derive strong separation for critical planar FK percolation.
- **Assumptions and setting:** The method concerns planar models and polychromatic arm events; the application is critical planar FK percolation.
- **Caveat:** Arm separation is an input to other conclusions such as quasi-multiplicativity and exponent identification; this paper's abstract does not claim those consequences follow without additional hypotheses and estimates.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Probability & statistics; Mathematical physics

### 9. [Nondegeneracy and uniqueness of ground states of the Schrödinger equation with Neumann conditions in a weakly nonlocal regime](https://arxiv.org/abs/2611.26428)
- **Abstract:** For a fractional Schrödinger equation in a half-space with nonlocal Neumann conditions and fractional order close to two, the authors prove ground-state nondegeneracy and uniqueness up to tangential translation and sign.
- **Authors:** Serena Dipierro, María Medina, Enrico Valdinoci
- **arXiv:** `2611.26428v1` (published Thu, 19 Nov 2026 17:07:10 UTC; categories: `math.AP`)
- **Evidence for ranking:** It addresses a less-studied nonlocal Neumann half-space setting and derives both a linearized-kernel characterization and uniqueness, rather than only existence.
- **Claimed result:** The authors prove that the only solutions of the linearized equation are tangential derivatives of the ground state and conclude uniqueness up to tangential translations and sign.
- **Assumptions and setting:** The equation is driven by a fractional Laplacian of order 2s with s close to 1, in a half-space under nonlocal Neumann conditions.
- **Caveat:** The theorem is restricted to the weakly nonlocal regime (s close to 1); the abstract gives no explicit numerical range for s.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Analysis & PDE

### 10. [Paper2Lean: Agentic Autoformalization of Mathematical Research Papers at Scale](https://arxiv.org/abs/2611.26272)
- **Abstract:** The authors introduce an agentic pipeline for turning mathematical research papers into Lean projects and report 20 optimization papers formalized into compilable projects, followed by human semantic review and repair.
- **Authors:** Yifan Bai, Yantao Li, Jian Yu, Jingwei Liang
- **arXiv:** `2611.26272v1` (published Thu, 19 Nov 2026 15:39:43 UTC; categories: `math.OC`)
- **Evidence for ranking:** It reports a paper-level evaluation with 20 projects and a public dataset of 494 Lean files and 110,910 lines, making the reproducible artifact a concrete signal beyond the framework description.
- **Claimed result:** The authors report that all 20 generated projects compile without proof placeholders; after human review and semantic repair, the OptPaper-20 corpus has 20 corrected formalizations, all passing clean builds.
- **Assumptions and setting:** Evaluation uses 20 mathematical optimization papers, mathlib, and a shared library of supporting results; the corrected corpus is publicly linked by the authors.
- **Caveat:** Compilation checks formal proof terms, not whether the formalized statements faithfully capture each source paper; the reported corpus required human review and semantic repair, as the authors acknowledge.
- **Announcement type:** new submission, announcement batch Fri, 20 Nov 2026
- **Themes:** Optimization & control; Machine learning theory

## Trending Research Themes

- **Sharp quantitative bounds across distinct areas:** the moment-curve decoupling result, exact topological-overlap constants, and near-linear independent-transversal threshold each sharpen a quantitative frontier, but use different methods and should not be read as one shared technical trend. ([Jeong–Oh](https://arxiv.org/abs/2611.26581), [Norin](https://arxiv.org/abs/2611.26229), [Zhang](https://arxiv.org/abs/2611.26259))
- **Exact structure in critical percolation:** one paper uses TSSCPP enumeration, dimers, and Pfaffian formulas to prove rationality for nested-arch probabilities; another develops a general exploration method for arm separation and applies it to critical FK percolation. These are complementary but distinct approaches. ([Akyazi-Zavadski–Berestycki–Chhita](https://arxiv.org/abs/2611.26570), [Gassmann–Manolescu–Mohanarangan](https://arxiv.org/abs/2611.26458))
- **Structural algebra and topology:** a 3-primary periodic family in stable homotopy and positive-characteristic matroids with non-algebraic duals are isolated, high-specificity structural results, not evidence of a broad shared method. ([Wan](https://arxiv.org/abs/2611.26621), [Grund](https://arxiv.org/abs/2611.26429))
- **AI-assisted mathematics and proof formalization:** the topological-overlap paper reports AI-assisted discovery and links a Lean formalization; Paper2Lean evaluates whole-paper formalization at scale. These two papers are a notable intersection of mathematical research and AI/formal methods, but are isolated signals in this daily sample. ([Norin](https://arxiv.org/abs/2611.26229), [Bai et al.](https://arxiv.org/abs/2611.26272))

## Open Problems and Research Directions

- **Author-stated open points:** the percolation paper leaves Romik's denominator properties and dyadic-rationality claims unresolved in its proved results, and its cylinder theorem excludes N = k. The authors also report that Dan Romik has a separate AI-assisted full solution forthcoming; that reported work is not verified here. A concrete follow-up is to establish the denominator formula uniformly, including the boundary case, and compare it with the forthcoming argument. ([Akyazi-Zavadski–Berestycki–Chhita](https://arxiv.org/abs/2611.26570))
- **Remaining conjecture gap:** the independent-transversal result proves f(r) ≤ r + O(r^(20/21)), implying f(r)/r → 1, but does not reach Yuster's stated exact threshold. Improving the error term or identifying extremal examples would test how close the asymptotic result is to the original conjecture. ([Zhang](https://arxiv.org/abs/2611.26259))
- **Scope extension (synthesis):** the ground-state theorem is limited to s close to 1 and a half-space with nonlocal Neumann conditions. One follow-up is to determine an explicit admissible s-range and test whether the kernel/uniqueness conclusion persists for broader domains or farther from the local limit. ([Dipierro–Medina–Valdinoci](https://arxiv.org/abs/2611.26428))
- **Formal verification follow-up (synthesis):** compare the linked Lean formalization for topological overlap with the final preprint line by line, since the paper says it was built from an earlier draft; the same audit principle applies to semantic correspondence in Paper2Lean's optimization corpus. ([Norin](https://arxiv.org/abs/2611.26229), [Bai et al.](https://arxiv.org/abs/2611.26272))

## Takeaway

The day's strongest mathematical signals are precise estimates and explicit structure: a conjecture-completing decoupling result, an exact overlap constant, and sharp progress on percolation probabilities and transversal factors. Several claims are substantial but appear as fresh preprints with little independent attention data, so this is a curated map of promising results—not a measured popularity leaderboard or a substitute for expert proof review.

## Method and sources

- **Window:** daily arXiv Mathematics announcement batch for Friday, 20 November 2026; exact date range 2026-11-20 to 2026-11-20. The selected papers are new v1 submissions; their first-submission timestamps are recorded individually above, and their announcement batch is dated 20 November.
- **Snapshot:** 2026-11-20 17:18:01 UTC.
- **Coverage:** traversed the full `math` recent listing for the 20 November batch (405 entries); preserved each selected paper's primary and cross-list categories. Verified all ten selected records against their arXiv abstract pages and read the abstracts. Also inspected introductions/main-result material for the three leading papers.
- **Inference:** arXiv supplies no official trending chart. The order weights concrete mathematical claims, named conjecture progress, scope/cross-listing, and linked reproducibility artifacts. Semantic Scholar citation evidence was not usable for these just-announced papers, and no independent expert-discussion signal was established in the checks; therefore the order is “notable recent papers,” not measured popularity. Citation totals are not presented as gains during this window.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); linked arXiv abstract pages above; [Lean formalization for topological overlap](https://github.com/snorin239/SharpTopologicalOverlap); [Paper2Lean/OptPaper repository](https://github.com/TTony2019/OptPaper).
