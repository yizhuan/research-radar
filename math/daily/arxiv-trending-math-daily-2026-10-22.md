# Math on arXiv — latest batch: Thu, 22 Oct 2026

Six notable papers from the latest math announcement batch. The strongest common pattern is sharp, concrete statements—conjecture resolutions, optimal rates, and threshold/bound results—rather than one shared technique. I’ll flag a debated probability-conjecture claim, then cover combinatorics, statistics, number theory, and PDE. This is an inferred selection, not an official arXiv trending chart; citation evidence is limited because these papers are extremely recent.

## Top papers (ranked)

### 1. [On the proof of the Kozma-Nitzan conjecture](https://arxiv.org/abs/2610.30063)
- **Abstract:** The author says this short note exposits a recent proof of the Kozma–Nitzan conjecture attributed to OpenAI.
- **Authors:** Jean-Baptiste Gouéré
- **arXiv:** `2610.30063v1` (published 2026-10-21T17:23:22Z; categories: `math.PR`)
- **Evidence for ranking:** A targeted search surfaced an October MathDB entry describing an exposition of the claimed AI proof and earlier discussion of the claim by mathematician Gil Kalai; this indicates topic-level attention, not verification of this particular note ([MathDB](https://mathdb.com/p/408931/kozma-nitzan-conjecture), [Gil Kalai’s blog](https://gilkalai.wordpress.com/2026/09/03/amazing-there-is-no-percolation-at-the-critical-probability-in-all-dimensions-solved-by-ai-via-a-conjecture-of-gady-kozma-and-shahaf-nitzan/)).
- **Claimed result:** The abstract reports an exposition of the recent proof; it does not state the theorem or proof details, so the result is reported only as the author characterizes it.
- **Assumptions and setting:** A probability-theory conjecture; the abstract does not specify the conjecture’s hypotheses.
- **Caveat:** This is an exposition of a claimed proof, not independent proof verification; the abstract alone is insufficient to assess the argument or its exact scope.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Probability & statistics

### 2. [A weighted inequality for matroid flats and log-concavity of Whitney numbers](https://arxiv.org/abs/2610.29893)
- **Abstract:** Using Hodge–Riemann relations for matroid Chow rings, the authors prove a weighted inequality for flats and apply it to the points–lines–planes conjecture and Brylawski’s ultra-log-concavity conjecture, including equality cases.
- **Authors:** Yuxian Dong, Yanxin Liu
- **arXiv:** `2610.29893v1` (published 2026-10-21T15:35:40Z; categories: `math.CO`)
- **Evidence for ranking:** The claimed results resolve two specifically named conjectures and characterize equality in both; an independent commentary page also discusses the result, though it is not a peer-review signal ([Moonlight review](https://www.themoonlight.io/zh/review/a-weighted-inequality-for-matroid-flats-and-log-concavity-of-whitney-numbers)).
- **Claimed result:** The authors’ main theorem is a weighted inequality for rank-graded flats of a loopless matroid; they derive the points–lines–planes inequality and Brylawski’s ultra-log-concavity of first-kind Whitney numbers, with equality characterizations.
- **Assumptions and setting:** Finite loopless matroids; the weighted theorem assigns real weights to flats of a fixed intermediate rank.
- **Caveat:** These are preprint claims; the report checked the introduction and stated main theorem, not the proofs.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 3. [Hitting time for loose Hamilton cycles in the random hypergraph process](https://arxiv.org/abs/2610.29894)
- **Abstract:** For even vertex counts, the authors prove that a random 3-uniform hypergraph process gets a loose Hamilton cycle exactly when its last isolated vertex disappears, with high probability, and report extensions to other fixed uniformities and counting estimates.
- **Authors:** Jared León, Xizhi Liu
- **arXiv:** `2610.29894v1` (published 2026-10-21T15:36:29Z; categories: `math.CO`)
- **Evidence for ranking:** The introduction identifies the hitting-time question as posed in earlier literature; the paper links a Lean 4 formalization and describes extensions to fixed higher uniformities and cycle counts. These are concrete corroborating artifacts, not readership measures ([formalization source](https://github.com/WozMit/hitting-time-loose-hamilton)).
- **Claimed result:** For even `n`, the first loose Hamilton cycle in the 3-uniform process appears with high probability at the same step that the final isolated vertex disappears. The authors also state corresponding extensions for fixed `r ≥ 4` when `(r−1) | n`, and estimates of cycle counts within a factor `exp{o(n)}`.
- **Assumptions and setting:** Uniformly add missing edges to an initially empty hypergraph; the main 3-uniform result is asymptotic through even `n`.
- **Caveat:** The main theorem is asymptotic and has a parity restriction; the reported counting estimate is only within a subexponential factor, not a sharp asymptotic equivalent.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 4. [Minimax Optimality of the NPMLE for Gaussian Mixtures in Hellinger Distance](https://arxiv.org/abs/2610.30109)
- **Abstract:** For univariate Gaussian location mixtures, the authors establish minimax squared-Hellinger risk rates for unconstrained and compact-support-constrained nonparametric maximum-likelihood estimators, using local bracketing-entropy bounds.
- **Authors:** Shayan Hundrieser, Tudor Manole
- **arXiv:** `2610.30109v1` (published 2026-10-21T17:53:10Z; categories: `math.ST`, `cs.IT`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed in statistics, information theory, and machine learning, and states two distinct minimax-optimal rates plus an entropy technique; its introduction and main results were inspected.
- **Claimed result:** For `n` i.i.d. observations, the unconstrained NPMLE attains squared-Hellinger rate `log(n)/n` for sub-Gaussian mixing measures; with compactly supported true mixing measure and a matching compact constraint, the rate is `log(n)/(n log log n)`. The authors also claim regret-optimality for Gaussian empirical-Bayes `g`-modeling with bounded priors.
- **Assumptions and setting:** Univariate location mixtures with known standard Gaussian kernel; sub-Gaussian mixing for the unconstrained result, and compact support for the faster constrained result.
- **Caveat:** The guarantees concern density estimation in this specific mixture model; they do not establish the same rates for multivariate mixtures, unknown component variance, or arbitrary mixing tails.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Probability & statistics; Machine learning theory

### 5. [A Sharp Bound for Additive Complements](https://arxiv.org/abs/2610.29963)
- **Abstract:** For infinite nonnegative-integer sets whose sum contains all sufficiently large integers, the author proves a sharp implication from a limsup bound on the product of their counting functions.
- **Authors:** Zihan Zhang
- **arXiv:** `2610.29963v1` (published 2026-10-21T16:18:33Z; categories: `math.NT`)
- **Evidence for ranking:** The abstract states an explicit sharp constant and a discrete gap argument, making the claim readily checkable; no separate attention signal was found in the sources checked.
- **Claimed result:** If `A+B` contains every sufficiently large integer and `limsup_{x→∞} A(x)B(x)/x < 3/2`, then `A(x)B(x)−x → +∞`; the author says `3/2` is best possible.
- **Assumptions and setting:** `A` and `B` are infinite subsets of nonnegative integers, `A(x), B(x)` are their counting functions, and their sumset is cofinite.
- **Caveat:** The implication assumes a strict limsup bound below `3/2`; it does not settle the boundary case at equality.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Algebra & number theory

### 6. [On ABP Estimates for a Class of Fully Nonlinear Singular-Degenerate Elliptic Equations and Applications](https://arxiv.org/abs/2610.30112)
- **Abstract:** The authors establish a weighted Alexandrov–Bakelman–Pucci estimate for fully nonlinear elliptic equations with singular or degenerate coefficients and gradient dependence, then apply it to several nonlinear PDE classes.
- **Authors:** Junyuan Fang, Jack Peltier, Tuoc Phan
- **arXiv:** `2610.30112v1` (published 2026-10-21T17:53:54Z; categories: `math.AP`)
- **Evidence for ranking:** The abstract extends a classical estimate to a broad singular-degenerate setting and lists applications to generalized Monge–Ampère, Hessian, Hessian-quotient, and anisotropic mean-curvature-type equations; this is a mathematically broad but isolated signal in this selection.
- **Claimed result:** A weighted ABP-type bound for classical subsolutions and viscosity subsolutions with locally Lipschitz gradients, allowing general gradient-growth rates subject to a smallness condition when the associated weight has finite integral.
- **Assumptions and setting:** Fully nonlinear elliptic equations with singular or degenerate coefficients and nonlinear gradient dependence; Hessian-quotient applications require an additional condition on the contact Hessian.
- **Caveat:** The estimate’s applicability depends on the stated regularity, gradient-weight, and data-smallness conditions; the Hessian-quotient application has an extra contact-Hessian hypothesis.
- **Announcement type:** new submission, 2026-10-22 announcement batch
- **Themes:** Analysis & PDE

## Trending Research Themes

- **Combinatorial inequalities and structures:** Dong–Liu use matroid Chow-ring Hodge–Riemann relations to prove inequalities for flats and Whitney numbers; León–Liu study a different extremal threshold problem in random hypergraphs. The connection is the use of structural constraints to obtain sharp global statements, not a shared proof method.
- **Probability, from random structures to inference:** The hypergraph paper gives a hitting-time theorem, while Hundrieser–Manole derive estimation rates for Gaussian mixtures. The latter also bridges mathematical statistics with information theory and machine learning through cross-listing and empirical-Bayes implications.
- **Sharpness and boundary conditions recur:** Zhang’s `3/2` constant is stated to be best possible; the mixture paper distinguishes sub-Gaussian and compact-support regimes; Fang–Peltier–Phan make data smallness conditional on an integrable gradient weight. These are separate results, but each makes the hypotheses central to the guarantee.
- **Isolated signal—nonlinear PDE:** The ABP estimate is the sole selected analysis/PDE paper, so it signals activity in this batch rather than a field-wide trend.

## Open Problems and Research Directions

- **Proof status (selected-paper caveat):** Gouéré’s note presents an exposition of a claimed proof but its abstract does not state the theorem or supporting details. Independent expert verification of the exact statement and argument is the immediate evidence-tied direction; this report does not verify it. ([2610.30063](https://arxiv.org/abs/2610.30063))
- **Matroid inequalities:** Dong–Liu report equality cases for two inequalities. A natural follow-up is to test which stronger weighted inequalities or equality classifications persist under common matroid operations and in boundary ranks; this is a proposed extension, not an open problem claimed by the authors. ([2610.29893](https://arxiv.org/abs/2610.29893))
- **Random hypergraphs:** The paper reports an `exp{o(n)}`-factor estimate for cycle counts. Sharpening that to a leading constant or asymptotic equivalent, and examining whether the fixed-uniformity divisibility conditions can be broadened, are synthesis directions suggested by the stated scope. ([2610.29894](https://arxiv.org/abs/2610.29894))
- **Gaussian-mixture estimation:** The stated guarantees separate sub-Gaussian tails from compact support. Testing which rates survive under weaker tail assumptions, unknown variance, or multivariate mixtures would probe the boundary of the theorem; these generalizations are not claimed results. ([2610.30109](https://arxiv.org/abs/2610.30109))
- **Additive complements and ABP estimates:** Zhang’s strict `<3/2` hypothesis leaves its equality boundary unaddressed by the abstract; Fang–Peltier–Phan’s finite-integral gradient-weight case requires small data. Studying the boundary case and whether the PDE smallness condition can be relaxed are concrete follow-ups, not claims that either is tractable. ([2610.29963](https://arxiv.org/abs/2610.29963), [2610.30112](https://arxiv.org/abs/2610.30112))

## Takeaway

Today’s batch contains several clean, high-stakes mathematical claims—two named matroid conjectures, a random-hypergraph hitting time, and sharp statistical and number-theoretic bounds. These stand out for their theorem statements and, in one case, external discussion, not for demonstrated readership; the most controversial item still needs independent proof assessment.

## Method and sources

- **Window:** daily, latest arXiv announcement batch dated 2026-10-22 (Thu); announcement-window start and end are both 2026-10-22. The listed papers carry arXiv publication timestamps on 2026-10-21 UTC. This is a batch window, not a rolling 24-hour window.
- **Scope:** arXiv Mathematics archive (`math.*`), retaining specific subject categories and noting cross-lists. No subfield filter.
- **Snapshot:** 2026-10-23T00:14:30Z.
- **Inference:** arXiv supplies no official trending chart. Order is inferred from checkable claimed results, explicit prior open questions, cross-listing, linked formalization, and independent topic discussion. Semantic Scholar currently lists 0 citations and 0 influential citations for each of these six papers; at this age the totals do not measure within-window momentum. No download or readership ranking was available.
- **Coverage limitation:** arXiv’s recent page reports 381 entries in the Thu batch. A submitted/updated-date API query for `math.*` returned 280 records, and the difference was not reconciled in this run; therefore this is a curated, non-exhaustive sample, not a complete ranking of all 381. The six selected abstract records were verified against arXiv, and the introductions/main-result statements of the first three were inspected. The configured `web_extract` backend could not retrieve pages; arXiv HTML was read in the browser instead. The limited web searches found no broader independent attention signal beyond the linked discussion above.

**Sources:** [arXiv math recent listing](https://arxiv.org/list/math/recent), arXiv abstract pages linked above, [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/), and the linked discussion pages.
