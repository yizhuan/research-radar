Math (arXiv announcement batch: Wednesday, 11 November 2026) — 10 notable recent papers. A strong pattern today is explicit resolution or tightening of long-standing bounds and conjectures, with several results spanning number theory, combinatorics, geometry, and analysis. Spoken agenda: hypergraph coloring and zeta gaps first, then arithmetic and geometric classifications, explicit constructions, and formalized proofs. This ordering is inferred, not an official arXiv trending chart; citation evidence for such new papers is limited.

## Top papers (ranked)

### 1. [The Proof of the Alon--Kim Conjecture](https://arxiv.org/abs/2611.13698)
- **Abstract:** For fixed integers k ≥ t ≥ 1 and ε > 0, the authors claim that every sufficiently high-degree k-uniform, t-simple multihypergraph H satisfies χ′(H) ≤ (t−1+1/t+ε)Δ(H).
- **Authors:** Chengshuo Qiao, Zhijun Lu, Huimin Song
- **arXiv:** `2611.13698v1` (published 2026-11-10 07:44:41 UTC; categories: `math.CO`)
- **Evidence for ranking:** The abstract and Theorem 1.5 state a resolution of the Alon–Kim conjecture, open since 1997, across all fixed k,t; the paper identifies its finite-dimensional convex-optimization and probabilistic approach.
- **Claimed result:** The authors state that for each fixed k ≥ t ≥ 1 and ε > 0 there is a threshold Δ₀(k,t,ε) such that every k-uniform, t-simple multihypergraph with Δ(H) ≥ Δ₀ obeys the conjectured edge-colouring bound.
- **Assumptions and setting:** The hypergraph may have parallel edges; t-simplicity means distinct edges intersect in at most t vertices, and k,t,ε are fixed while Δ grows.
- **Caveat:** The result is asymptotic: the threshold depends on k,t,ε, and the paper does not make it a finite-degree sharp bound.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 2. [The distribution of small gaps between zeros of the Riemann zeta function](https://arxiv.org/abs/2611.14486)
- **Abstract:** The author claims unconditionally that a positive proportion of consecutive nontrivial zeta-zero gaps are at most 0.7892 times their average spacing.
- **Authors:** Youness Lamzouri
- **arXiv:** `2611.14486v1` (published 2026-11-10 18:46:37 UTC; categories: `math.NT`)
- **Evidence for ranking:** The paper gives a concrete unconditional improvement over the previously cited explicit threshold 1−2.36×10⁻⁶; its introduction states the theorem and the role of an unconditional variant of Montgomery’s pair-correlation method.
- **Claimed result:** Theorem 1.1 states that D(λ) > 0 for every λ ≥ 0.7892, where D(λ) measures the lower limiting proportion of gaps no larger than λ times the mean spacing.
- **Assumptions and setting:** This is an unconditional statement about the ordinates of nontrivial zeta zeros, counted with multiplicity; it concerns a positive proportion, not all gaps.
- **Caveat:** The author notes that the constant is not optimized; a different explicit kernel would give λ > 0.7864, and further optimization may improve it.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Algebra & number theory

### 3. [The closure of the nonreal roots of bounded-height polynomials is connected exactly at pronic heights](https://arxiv.org/abs/2611.14517)
- **Abstract:** For the closure C_h of nonreal roots of integer polynomials with coefficient modulus at most h, the author claims connectedness exactly when h=q(q−1), q ≥ 2, and at least five components otherwise.
- **Authors:** Bernat Espigulé
- **arXiv:** `2611.14517v1` (published 2026-11-10 18:58:59 UTC; categories: `math.CV` (primary), `math.NT`)
- **Evidence for ranking:** Theorem A supplies an if-and-only-if classification for every integer height; the paper also reports an explicit computational companion at Zenodo and connects the height-two case with a numerical observation from twenty years earlier.
- **Claimed result:** The author proves that C_h is connected exactly at pronic heights and has at least five components at every other height, with further results showing infinitely many components for a density-one set of heights.
- **Assumptions and setting:** C_h is the planar closure of nonreal roots of integer polynomials whose coefficients have absolute value at most the positive integer h; real roots are excluded before closure.
- **Caveat:** Exact component infinitude remains unsettled at a small set of heights, including 1, 3, 4, 9, and 25, and at some square-adjacent heights.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

### 4. [The exponent 3/4 for the exceptional sets of the equations K/n=1/x+1/y+1/z](https://arxiv.org/abs/2611.14167)
- **Abstract:** For K ≥ 4, the author bounds the number E_K(N) of n ≤ N for which K/n has no representation as three positive unit fractions by N exp(−c((log N)³/K)^{1/4}) over a specified range, improving Vaughan’s exponent 2/3.
- **Authors:** Dmytro Trybushnyi
- **arXiv:** `2611.14167v1` (published 2026-11-10 14:53:35 UTC; categories: `math.NT`)
- **Evidence for ranking:** The abstract and Theorem 1.1 report an improved uniform exceptional-set estimate, explicit constants, and a full Lean 4 formalization archived with the paper.
- **Claimed result:** The author proves E_K(N) ≤ N exp(−c((log N)³/K)^{1/4}) for absolute c>0 when 4 ≤ K ≤ (log N)³/B, with an explicit B; the proof is formally checked in Lean 4.
- **Assumptions and setting:** E_K(N) counts integers 2 ≤ n ≤ N with no positive-integer solution to K/n=1/x+1/y+1/z; K=4 is the Erdős–Straus case, and the bound applies only in the stated K range and for sufficiently large N.
- **Caveat:** This improves a density bound but does not prove that every n is representable for K=4; its useful range is limited to K up to a constant multiple of (log N)³.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Algebra & number theory

### 5. [A counterexample to the strong version of the union of uniform closed balls conjecture in dimensions three and higher](https://arxiv.org/abs/2611.14181)
- **Abstract:** For every n ≥ 3, r > 0, and ε > 0, the author constructs a compact set with the interior r-sphere condition but a point not covered by any contained ball of radius (1/2+ε)r, making the universal r/2 radius optimal.
- **Authors:** Chadi Nour
- **arXiv:** `2611.14181v1` (published 2026-11-10 15:05:03 UTC; categories: `math.MG`)
- **Evidence for ranking:** The abstract states a dimension-by-dimension counterexample to the strong conjecture and an optimality conclusion for the universal radius, with an explicit simplex-based construction.
- **Claimed result:** The author claims the strong conjecture fails in each dimension n ≥ 3, even for compact sets, and proves the universal contained-ball radius r/2 cannot be increased; in the plane the optimal radius is r/√3.
- **Assumptions and setting:** The sets satisfy the interior r-sphere condition in Euclidean R^n; the counterexample is required for every positive ε and every n ≥ 3.
- **Caveat:** The construction establishes sharpness of the universal radius but does not classify all sets satisfying the sphere condition.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Geometry & topology

### 6. [Explicit restricted isometries with k=m^{2/3-o(1)}](https://arxiv.org/abs/2611.14475)
- **Abstract:** The authors construct explicit real m×n restricted isometries with m/n → 0, δ_k → 0, and sparsity k=m^{2/3-o(1)}, using a strongly regular graph and an incidence-geometric vertex-set result.
- **Authors:** Christian Kümmerle, Dustin G. Mixon
- **arXiv:** `2611.14475v1` (published 2026-11-10 18:37:57 UTC; categories: `math.FA` (primary), `cs.IT`, `math.CO`, `math.MG`)
- **Evidence for ranking:** This is a concrete explicit construction cross-listed across functional analysis, information theory, combinatorics, and metric geometry; the authors frame it as surpassing an m^{1/2} barrier for the stated entrywise-Gram-matrix proof technique.
- **Claimed result:** The authors prove existence of the stated family and show that the barrier for their proof method is m^{2/3}, which their construction reaches up to the o(1) in the exponent.
- **Assumptions and setting:** The matrices are real; m tends to infinity, the aspect ratio m/n tends to zero, and the restricted isometry constant δ_k tends to zero.
- **Caveat:** The exponent is 2/3−o(1), not an exact k=m^{2/3} guarantee; the paper’s result is an explicit family under these asymptotic conditions.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Analysis & PDE; Combinatorics & discrete mathematics

### 7. [Progression-free sets in class 2 and arbitrary finite groups](https://arxiv.org/abs/2611.14464)
- **Abstract:** The author transfers bounds through nilpotent groups of class 2 to prove r₃(G) ≤ C|G| exp(−c(log|G|)^{1/6}/(log log|G|)^{1/3}) for every sufficiently large finite group G.
- **Authors:** Luca Sabatini
- **arXiv:** `2611.14464v1` (published 2026-11-10 18:29:43 UTC; categories: `math.GR` (primary), `math.NT`)
- **Evidence for ranking:** The abstract gives an explicit asymptotic form for arbitrary finite groups and identifies a transfer of sharp abelian bounds via class-2 nilpotent groups as the proof route; it cross-lists group theory and number theory.
- **Claimed result:** Combining a recent result of Raghavan with the author’s theorem on large class-2 subgroups yields the stated upper bound, improving estimates based on Pyber’s abelian-subgroup theorem.
- **Assumptions and setting:** G ranges over arbitrary finite groups as |G|→∞; r₃(G) denotes the maximum size of a three-term-progression-free subset in the paper’s group setting.
- **Caveat:** The bound is asymptotic and the abstract does not specify numerical values for its constants C and c.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 8. [No 13-vertex triangulation of the three-torus](https://arxiv.org/abs/2611.14367)
- **Abstract:** The author rules out a 13-vertex triangulation of the three-torus, a case left open by standard lower bounds for the conjectured 15-vertex minimum.
- **Authors:** Geunho Lim
- **arXiv:** `2611.14367v1` (published 2026-11-10 17:23:48 UTC; categories: `math.GT` (primary), `math.CO`)
- **Evidence for ranking:** The abstract isolates a specific gap in a vertex-minimality conjecture and reports a proof combining a g₂ inequality, a simplicial-complement reduction, fundamental groups, and Alexander duality.
- **Claimed result:** The author excludes the 13-vertex case by reducing to a nine-vertex model of the punctured three-torus and deriving a contradiction from the deficiency of Z³.
- **Assumptions and setting:** The object is a simplicial triangulation of the three-torus; the result addresses exactly 13 vertices.
- **Caveat:** The 14-vertex case remains undecided by this paper, so it does not establish the conjectured 15-vertex minimum.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Geometry & topology; Combinatorics & discrete mathematics

### 9. [A Complete Classification of Maximal Hyperelliptic Curves Related to Chebyshev Polynomials](https://arxiv.org/abs/2611.14198)
- **Abstract:** For H_d: y²=φ_d(x), the authors classify pairs (d,p), with p prime not dividing 2d, for which H_d is maximal over a finite field of characteristic p and determine the corresponding fields.
- **Authors:** Saeed Tafazolian, Jaap Top
- **arXiv:** `2611.14198v1` (published 2026-11-10 15:21:08 UTC; categories: `math.NT` (primary), `math.AG`)
- **Evidence for ranking:** The abstract claims a complete classification in a defined family, including the previously partial p≡1 mod 4 case, and a Frobenius-polynomial computation for the stated odd-degree subcase.
- **Claimed result:** For odd d and p≡1 mod 4, the authors state that the Jacobian is supersingular exactly when H_d becomes maximal over a finite extension, and this occurs precisely for d=ℓ^n with prime ℓ≡1 mod 4 and p a generator modulo ℓ^n; they also compute the Frobenius polynomial.
- **Assumptions and setting:** The curves are the Chebyshev family y²=φ_d(x); p is prime with p∤2d, and the detailed equivalence quoted applies to odd d and p≡1 mod 4.
- **Caveat:** This classification concerns the specified Chebyshev-derived family, not arbitrary hyperelliptic curves.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

### 10. [Annular Counterexamples and Skew-Shape Block Identities](https://arxiv.org/abs/2611.14506)
- **Abstract:** The author gives counterexamples to unimodality and log-concavity claims in a rank-two annular cluster model, proves a skew-shape block-statistic identity under a specified convention, and provides Lean 4/Mathlib formalizations.
- **Authors:** Adam Tilèpe
- **arXiv:** `2611.14506v1` (published 2026-11-10 18:55:26 UTC; categories: `math.CO`)
- **Evidence for ranking:** The abstract reports two concrete counterexamples, a positive identity result, and an available complete Lean formalization; the paper is a self-contained combinatorial contribution with a checkable proof artifact.
- **Claimed result:** The author refutes a published unimodality assertion and a log-concavity conjecture in the rank-two annular model, while proving a skew-Young-diagram block-statistic identity proposed in earlier work.
- **Assumptions and setting:** The counterexamples use the stated annular cluster model; the identity holds for arbitrary finite skew Young diagrams under the paper’s explicit root-exclusion convention.
- **Caveat:** The counterexamples depend on the model and conventions specified in the paper; they do not establish failure of unimodality or log-concavity beyond that setting.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Combinatorics & discrete mathematics

## Trending Research Themes

- Sharp asymptotic bounds and conjecture resolution are the clearest recurring pattern: hypergraph edge-colouring ([1]), small zeta gaps ([2]), Egyptian-fraction exceptional sets ([4]), and progression-free subsets of finite groups ([7]) each sharpen a quantitative threshold or resolve a named conjecture. These are distinct techniques, not evidence of a single shared method.
- Exact classification and counterexample work appears across geometry and arithmetic: pronic-height connectedness of root closures ([3]), the higher-dimensional closed-ball counterexample ([5]), the Chebyshev hyperelliptic classification ([9]), and the three-torus vertex exclusion ([8]). These are separate results; their common thread is resolving a specific classification or extremal question.
- Explicit constructions link combinatorics to analytic inequalities: the restricted-isometry family uses strongly regular graphs and incidence geometry ([6]), while the progression-free bound moves between abelian, class-2 nilpotent, and arbitrary finite groups ([7]). This is a cross-field bridge in the selected papers, not a general field-wide shift.
- Formal verification is a small but checkable signal in this batch: the Egyptian-fraction sieve ([4]) and annular combinatorics ([10]) both provide Lean 4 formalizations; the bounded-height-root paper ([3]) also lists a computational companion. These artifacts support inspection, but do not substitute for assessing the arguments.

## Open Problems and Research Directions

- Open problem (reported by the authors): the zeta-gap paper says its 0.7892 threshold is not optimized and notes that an alternate kernel yields λ>0.7864 ([2]). A follow-up could optimize admissible kernels under the paper’s unconditional constraints and state the best constant that method supports.
- Open problem (reported by the authors): the root-closure paper leaves component infinitude unsettled at heights including 1, 3, 4, 9, and 25, and at at most one height in each sufficiently large square-adjacent triple ([3]). One concrete direction is to resolve those remaining heights with explicit separating series or connectivity constructions.
- Open problem (stated in the paper’s background): the 15-vertex three-torus triangulation is conjectured vertex-minimal; this paper excludes 13 vertices but leaves 14 open ([8]). Enumerating or structurally classifying the 14-vertex case would address the next gap.
- Open problem (noted in the paper): the hypergraph-coloring introduction says the optimal coefficient is not known for every fixed k ([1]). A natural extension is to determine whether the conjectured coefficient is sharp for fixed k,t, or make the Δ₀(k,t,ε) threshold effective.

## Takeaway

The day’s most substantial-looking items are a 1997 hypergraph-coloring conjecture claim, a strong unconditional zeta-gap improvement, and a complete arithmetic criterion for connectedness of a family of root closures. Several other papers make sharply delimited advances—often a counterexample, an explicit bound, or the resolution of one remaining finite case—so the ranking should be read as a significance-oriented shortlist rather than measured audience popularity.

## Method and sources

- Window: daily batch dated 2026-11-11; exact calendar window 2026-11-11 through 2026-11-11. The latest mathematics listing showed the Wednesday, 11 November 2026 batch; its papers were submitted on 10 November UTC. Snapshot time: 2026-11-11 17:23:07 UTC.
- Coverage: traversed the complete arXiv Mathematics recent listing for the batch (452 entries). The core corpus was math; selected papers retain their primary and cross-list categories. Each of the 10 selected arXiv abstract pages was checked; the introductions/main-result statements were also inspected for the leading three, with additional main-result text checked for [4].
- Ranking: arXiv publishes no trending/readership ranking. Attention signals were too sparse to support a popularity claim, so these are notable recent papers ranked by explicitness and scope of the claimed result, cross-field relevance, and checkable artifacts where available; recency was only a tie-breaker. Semantic Scholar current-citation metadata was available for two checked records and reported zero citations; no citation gains are inferred. The six exact-title web searches run did not surface independent expert/seminar discussion for those searched records.
- Sources: [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); verified abstract pages [2611.13698](https://arxiv.org/abs/2611.13698), [2611.14486](https://arxiv.org/abs/2611.14486), [2611.14517](https://arxiv.org/abs/2611.14517), [2611.14167](https://arxiv.org/abs/2611.14167), [2611.14181](https://arxiv.org/abs/2611.14181), [2611.14475](https://arxiv.org/abs/2611.14475), [2611.14464](https://arxiv.org/abs/2611.14464), [2611.14367](https://arxiv.org/abs/2611.14367), [2611.14198](https://arxiv.org/abs/2611.14198), and [2611.14506](https://arxiv.org/abs/2611.14506).