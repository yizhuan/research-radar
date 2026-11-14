Headline — Mathematics, latest announcement batch Friday 13 November 2026: 7 selected papers from 774 math-archive entries. The strongest pattern in this curated set is sharp theorem-making—counterexamples to rigidity or fixed-profile claims, and exact asymptotics for extremal problems. A quick agenda: subset sums, geometric/PDE rigidity, then regularity, arithmetic, and random-field results. This is an inferred “notable recent papers” selection, not a popularity ranking: arXiv has no official trending chart, and citation evidence is sparse for papers only about two days old.

## Top papers (ranked)

### 1. [Forbidden subset sums in a linear range: an inverse theorem and the Erdős-Graham irregularity problem](https://arxiv.org/abs/2611.17205)
- **Abstract:** The paper determines the extremal subset-sum function in the regular range and proves arithmetic-dependent asymptotics and non-convergence in the irregular range, including an inverse theorem and Lean-checked cases.
- **Authors:** Mateo Matijasevick
- **arXiv:** `2611.17205v1` (published 2026-11-12 18:05:45 UTC; categories: `math.CO`, `math.NT`)
- **Evidence for ranking:** The authors say this resolves Erdős–Graham Problem #361 and give an inverse theorem; the arXiv page reports Lean 4 formalization for several principal cases, with an author-linked proof repository at https://github.com/matejasevick/erdos361. Semantic Scholar reports 0 current citations and 0 influential citations; no period gain is implied. The number-theory/combinatorics cross-list reinforces the breadth of the result, not its popularity.
- **Claimed result:** For `c ≥ 1`, the authors prove `f_c(n)=⌊cn⌋−⌈n/2⌉`; for `0<c<1`, they prove non-convergence of `f_c(n)/n`, give its limsup and arithmetic-class limits under stated conditions, and establish a density-threshold inverse theorem for subset sums (arXiv abstract and Theorems 1.1–1.4).
- **Assumptions and setting:** `f_c(n)` is the largest size of a subset of `{1,…,⌊cn⌋}` avoiding `n` as a sum of distinct elements. The inverse theorem assumes integer `s≥1`, `q` the least positive integer not dividing `s`, `ε>0`, sufficiently large `T`, and `2^(q−2)E≤sT`; a set `A⊆[1,E]` with `|A|≥E/q+εT` then contains a subset summing to `sT`.
- **Caveat:** The authors leave behavior along classes with least non-divisor outside their eligible set `Q(c)` open; not all higher-`q` cases are machine-checked.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 2. [Nonrigidity of smooth tight surfaces](https://arxiv.org/abs/2611.17269)
- **Abstract:** The authors construct noncongruent smooth isometric embeddings of positive-genus closed surfaces in Euclidean 3-space that remain tight and differ only in a compact part of the negatively curved region.
- **Authors:** Mohammad Ghomi, Hongda Qiu, Matteo Raffaelli, Yuetong Zhang
- **arXiv:** `2611.17269v1` (published 2026-11-12 18:46:45 UTC; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** The authors’ main theorem gives uncountably many noncongruent embeddings and they identify it as settling questions of Nirenberg and Banchoff–Kühnel; the differential-geometry/PDE cross-list is a secondary relevance signal. Semantic Scholar reports 0 current citations and 0 influential citations; this is not evidence of measured attention.
- **Claimed result:** For every genus `g≥1`, the authors construct a metric admitting uncountably many smooth noncongruent tight isometric embeddings into `R³`; the embeddings agree outside a compact subset and enclose different volumes (Theorem 1.1).
- **Assumptions and setting:** Closed orientable surfaces of positive genus with a constructed Riemannian metric; embeddings are smooth (`C∞`) and tight in the stated total-positive-curvature sense.
- **Caveat:** The authors explicitly leave open whether their examples are flexible, meaning they lie in a continuous one-parameter family of noncongruent isometric embeddings.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Geometry & topology; Analysis & PDE

### 3. [A counterexample to fixed-profile soliton resolution for the three-dimensional quintic wave equation](https://arxiv.org/abs/2611.17291)
- **Abstract:** For the 3D focusing energy-critical wave equation, the authors construct a bounded forward-global solution near a sign-changing stationary state whose stationary core has two distinct similarity-orbit limits after subtracting radiation.
- **Authors:** Xuwen Chen, Justin Holmer, Shunlin Shen
- **arXiv:** `2611.17291v1` (published 2026-11-12 18:53:35 UTC; categories: `math.AP`)
- **Evidence for ranking:** Theorem 1.1 is a concrete counterexample to a precise fixed-profile assertion, and the authors include a computer-assisted certificate for the stationary state and its odd energy kernel. Semantic Scholar reports 0 current citations and 0 influential citations; the single-category listing and lack of corroborating discussion keep this a result-based, not attention-based, selection.
- **Claimed result:** The authors disprove the specified full-time resolution assertion with a fixed finite list of stationary profiles and fixed Lorentz velocities by constructing a bounded forward-global solution with subsequences approaching stationary states in distinct similarity orbits (arXiv abstract and Theorem 1.1).
- **Assumptions and setting:** The equation is the three-dimensional focusing energy-critical quintic wave equation; the constructed solution is forward-global, bounded in the energy space, and starts arbitrarily close to a sign-changing stationary state.
- **Caveat:** The result targets the fixed-profile quantifier order; it does not rule out sequential decompositions in which profiles may be chosen for a particular time sequence. The certificate is computationally assisted and remains part of an unreviewed preprint.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Analysis & PDE

### 4. [On L^p density of self-similar measures and Bernoulli convolutions](https://arxiv.org/abs/2611.17277)
- **Abstract:** The authors show that every absolutely continuous self-similar measure in their setting has an `L^p` density for some `p>1` and establish explicit Bernoulli convolutions with continuous densities.
- **Authors:** Samuel Kittle, Constantin Kogler
- **arXiv:** `2611.17277v1` (published 2026-11-12 18:50:34 UTC; categories: `math.DS`, `math.CA`, `math.PR`)
- **Evidence for ranking:** The result links dynamical systems, analysis, and probability; the authors’ paper states that the new results are formalized in Lean. Semantic Scholar reports 0 current citations and 0 influential citations, so cross-listing and checkable formalization—not observed readership—support its placement.
- **Claimed result:** For a probability measure supported on finitely many contracting similarities of `R^d`, absolute continuity of its self-similar measure implies its density belongs to `L^p(R^d)` for some `p>1`; the paper also gives explicit Bernoulli-convolution examples with continuous density (arXiv abstract and Theorems 1.1–1.2).
- **Assumptions and setting:** The general theorem assumes finitely many contracting similarities and an absolutely continuous associated self-similar probability measure. The Bernoulli-convolution examples use additional parameter conditions.
- **Caveat:** The general result promises some `p>1`, not a universal exponent; the explicit continuous-density examples cover a restricted parameter range.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Analysis & PDE; Probability & statistics

### 5. [The lifting problem for Galois representations of global fields](https://arxiv.org/abs/2611.17255)
- **Abstract:** The author proves that every mod-2 Galois representation of a global field lifts mod 4, constructs non-liftable examples for every odd prime at the next prime-power level, and completes a classification of liftable finite groups.
- **Authors:** Federico Scavia
- **arXiv:** `2611.17255v1` (published 2026-11-12 18:40:26 UTC; categories: `math.NT`)
- **Evidence for ranking:** The abstract combines a uniform mod-2 lifting theorem, counterexamples at every odd prime, and a stated completion of a finite-group classification. Semantic Scholar reports 1 current citation and 0 influential citations (about 0.51 current citations per paper-age day at snapshot; a one-citation rate is too small to establish momentum).
- **Claimed result:** All mod-2 Galois representations of a global field lift modulo 4; for each odd prime `p`, the author gives global-field representations mod `p` that do not lift mod `p²`, and proves liftability of generalized quaternion groups (arXiv abstract).
- **Assumptions and setting:** Galois representations of global fields with the stated mod-2/mod-4 or mod-`p`/mod-`p²` coefficient levels; the group-classification consequence concerns liftable finite groups.
- **Caveat:** The abstract’s positive and negative results concern these specific adjacent coefficient levels; it does not assert a general lifting criterion at all powers or for all coefficient rings.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Algebra & number theory

### 6. [On the maximum of Poissonian log-correlated fields](https://arxiv.org/abs/2611.17236)
- **Abstract:** For a stationary log-correlated field built from a Poisson sequence of random frequencies and uniform phases, the authors obtain a high-probability maximum asymptotic with a random-time fluctuation and logarithmic correction.
- **Authors:** Nicholas A. Cook, Haotian Gu
- **arXiv:** `2611.17236v1` (published 2026-11-12 18:24:03 UTC; categories: `math.PR`)
- **Evidence for ranking:** The paper states an explicit three-term maximum asymptotic and connects its proof to branching random walks in a random time environment. Semantic Scholar reports 1 current citation and 0 influential citations (about 0.51 current citations per paper-age day at snapshot; not a period gain and too little data for a momentum claim).
- **Claimed result:** For centered analytic 1-periodic `f` and the stated rate-1 Poisson arrival-time/uniform-phase model, the authors prove with high probability `max X_n = c₁n+c₂τ_n−(c₃+o(1))log n`, with positive constants depending on `f` (arXiv abstract).
- **Assumptions and setting:** The field is the sum of `f(e^{τ_j}t+v_j)` over the first `n` points, where `τ_j` are rate-1 Poisson arrival times and `v_j` are iid uniform on `[0,1)`; `f` is centered, analytic, and 1-periodic.
- **Caveat:** The analogous asymptotics for characteristic polynomials of random permutation matrices and sparse random matrices are conjectured/expected by the authors, not proved here.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 7. [Dimension drop for superlevel sets of the uniform Littlewood constant](https://arxiv.org/abs/2611.17189)
- **Abstract:** Although the set where the uniform Littlewood constant is positive has full Hausdorff dimension, the authors prove every fixed positive superlevel set has dimension strictly below two and polynomially decaying finite-scale measure.
- **Authors:** Shahriar Mirzadeh
- **arXiv:** `2611.17189v1` (published 2026-11-12 17:54:36 UTC; categories: `math.DS`, `math.NT`)
- **Evidence for ranking:** The paper bridges Diophantine approximation and homogeneous dynamics, giving both a Hausdorff-dimension drop and a quantitative Lebesgue-measure bound. Semantic Scholar reports 0 current citations and 0 influential citations; exact-title searches surfaced the arXiv record but no independent expert discussion.
- **Claimed result:** For every fixed `c>0`, the set `{L≥c}` has Hausdorff dimension strictly less than two, and the measure of `{(x,y)∈[0,1]²:F_Q(x,y)≥c}` is `O_c(Q^−κ(c))` for some `κ(c)>0` and all `Q≥2` (arXiv abstract).
- **Assumptions and setting:** `F_Q(x,y)=Q min_{1≤q≤Q}||qx||||qy||` and `L=limsup_{Q→∞}F_Q`; the result is for each fixed positive threshold `c`.
- **Caveat:** The abstract gives no explicit value for `κ(c)` or exact dimension of the superlevel set; its strict upper bound is not a complete dimension classification.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

## Trending Research Themes

- **Arithmetic obstructions and extremal behavior (two distinct signals):** the subset-sum paper resolves an irregularity problem through the least non-divisor of `n`, while the Littlewood paper uses Diophantine structure and dynamics to force dimension drop at every fixed positive threshold. Their techniques differ; this is an intersection of questions, not evidence of one shared method.
- **Rigidity assertions under smoothness or fixed-profile constraints:** the surface paper gives smooth isometric nonrigidity where analytic rigidity holds; the wave-equation paper invalidates one precise fixed-profile resolution statement while preserving the possibility of sequence-dependent decompositions. Both are author-claimed counterexamples to constrained rigidity principles, in different settings.
- **Regularity and asymptotic structure in analytic/probabilistic models:** the self-similar-measure paper upgrades absolute continuity to some `L^p` regularity and explicit continuous-density examples; the Poissonian-field paper derives a maximum law with random-time and logarithmic terms. These are separate results rather than a common technique.
- **Archive context:** the full batch contains 774 entries across many areas. Parsed primary-category labels were highest in combinatorics (76), probability (59), analysis of PDEs (55), optimization and control (50), and numerical analysis (44); 771 entries had a parsed primary label. The selected set is deliberately cross-field and is not a claim that these areas are shifting archive-wide.

## Open Problems and Research Directions

- **Author-stated open problem:** For the subset-sum function, determine behavior along arithmetic classes whose least non-divisor is outside the paper’s eligible set `Q(c)`; the authors specifically warn that the stated class limits cannot simply be extended to all `q` (2611.17205, Section 9). A follow-up could test boundary cases near the condition `2^(q−2) min(c,1−c)≤1` and compare extremal constructions across excluded classes.
- **Author-stated question:** The smooth tight surfaces are not known by the authors to be flexible (2611.17269, Introduction). A concrete direction is to determine whether their construction can be connected by a continuous path of noncongruent isometric embeddings while preserving tightness.
- **Author-proposed extension:** The Poissonian-field authors conjecture analogous maximum asymptotics for random-permutation characteristic polynomials and expect the mechanism in sparse random-matrix fields (2611.17236, Abstract). Testing the random-time fluctuation and logarithmic correction in those models would probe the scope of their mechanism.

Takeaway — This batch’s clearest mathematical signals are precise counterexamples and arithmetic-sensitive asymptotics, alongside sharp regularity and probability results. The selection is evidence-led but not popularity-measured: these papers are exceptionally new, citation counts are tiny, and the theorem claims remain preprints pending broader expert scrutiny.

Method and sources — Daily window: 2026-11-13 through 2026-11-13; selected batch: Friday 13 November 2026, the latest announcement batch available at the 2026-11-14 17:17:55 UTC snapshot (Saturday had no newer batch in the listing). Scope: arXiv Mathematics (`math`), all subfields; traversed the full recent listing showing all 774 entries in this announcement batch, then checked each selected abstract page and the introductions/main results for the top three. Candidate selection is a transparent evidence hierarchy of named/open-problem results, concrete theorem/counterexample claims, cross-list relevance, author-linked formal proof artifact, and current Semantic Scholar citation/influential-citation totals; totals are current counts, not gains during the window. Recent citation counts are too sparse to establish popularity; ordering is therefore a notable-paper judgment, not a trend score or “most read/downloaded” list. Exact-title searches were used for independent discussion; none that met an expert/seminar standard was found for this set. Sources: https://arxiv.org/list/math/recent ; selected arXiv abstract pages linked above; arXiv HTML for 2611.17291, 2611.17205, and 2611.17269; Semantic Scholar Graph API batch metadata (citationCount, influentialCitationCount); and the author-linked Lean repository https://github.com/matejasevick/erdos361. A date-bounded arXiv API query did not return entries, so batch completeness was verified by the full arXiv listing rather than API results.