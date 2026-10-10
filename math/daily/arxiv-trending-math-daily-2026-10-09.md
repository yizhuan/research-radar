# arXiv Mathematics — notable papers from the Fri, 9 Oct 2026 announcement batch (8 papers)

The strongest pattern today is boundary-setting mathematics: sharp constants and sample thresholds, explicit classifications, and undecidability. I’ll cover computability, random media, sharp estimates, and geometric structure. This is an inferred selection, not an official arXiv trending chart; very recent papers have little citation evidence, so the ordering is not a popularity ranking.[1]

Window: latest daily batch, 2026-10-09; snapshot: 2026-10-10 00:18:55 UTC. Saturday 10 Oct has no newer batch listed, so this uses Friday’s announcement.

## Top papers (ranked)

### 1. [Global asymptotic stability of homogeneous polynomial vector fields is undecidable](https://arxiv.org/abs/2610.12434v1)
- **Abstract:** For rational homogeneous polynomial vector fields, the authors reduce stability questions to cubic fields and prove global asymptotic stability is undecidable in every odd degree at sufficiently large fixed dimension.[2][3]
- **Authors:** Ivan O. Shevchenko, Jun Liu, Xinzhi Liu
- **arXiv:** `2610.12434v1` (published 2026-10-08 17:57:15 UTC; categories: `math.DS`, `math.CA`, `math.LO`)[2]
- **Evidence for ranking:** A concrete many-one-completeness result across dynamics, analysis, and logic; the introduction explains how it advances prior stability undecidability results.[3]
- **Claimed result:** The authors prove GAS is many-one complete for every odd degree ≥3 and all dimensions above a fixed threshold, hence cubic GAS is undecidable in some fixed dimension.[2][3]
- **Assumptions and setting:** Inputs are rational-coefficient homogeneous polynomial vector fields on real Euclidean space; the dimension threshold is sufficiently large, not arbitrary.[2][3]
- **Caveat:** The paper says its fixed dimension threshold is not computed; the result does not identify the smallest dimension where undecidability begins.[3]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Logic & foundations; Optimization & control

### 2. [Anomalous scaling limit of a Brownian particle in a log-correlated potential](https://arxiv.org/abs/2610.12335v1)
- **Abstract:** At weak disorder, the authors establish a scaling limit for a diffusion in a log-correlated Gaussian potential, with a singular path law and Gaussian-multiplicative-chaos reversible measure; in dimension two they compute the scaling exponent exactly.[4][5]
- **Authors:** Scott Armstrong, Ahmed Bou-Rabee, Tuomo Kuusi
- **arXiv:** `2610.12335v1` (published 2026-10-08 17:12:29 UTC; categories: `math.PR`, `math-ph`, `math.AP`)[4]
- **Evidence for ranking:** The paper addresses a scaling-limit problem noted in its introduction, connects probability, PDE, and mathematical physics, and links a Lean formalization.[5]
- **Claimed result:** Under the paper’s assumptions and sufficiently weak disorder, the authors prove convergence to a continuous strong Markov process with singular reversible measure and anomalous scaling.[4][5]
- **Assumptions and setting:** Dimension `d≥2`; the random environment satisfies the paper’s stationarity, dependence, symmetry, and regularity hypotheses, with disorder below a dimension-dependent threshold.[5]
- **Caveat:** The theorem is for weak disorder and this structured class of random fields; it does not establish the same behavior at strong disorder or for every log-correlated potential.[5]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Probability & statistics; Analysis & PDE; Mathematical physics

### 3. [Subspace Uncertainty and Sharp Sampling Thresholds on the Boolean Cube](https://arxiv.org/abs/2610.12358v1)
- **Abstract:** For Gaussian regression on a known subspace of low-degree functions on the Boolean cube, the paper gives an exponential worst-case sample threshold and sharpens an uncertainty bound, with an Airy-kernel construction showing the `k^(1/3)` remainder is generally unavoidable.[6]
- **Authors:** Thomas Weinberger
- **arXiv:** `2610.12358v1` (published 2026-10-08 17:23:25 UTC; categories: `math.PR`, `cs.IT`, `cs.LG`, `math.CO`)[6]
- **Evidence for ranking:** A precise threshold theorem spans probability, information theory, learning theory, and combinatorics; the abstract supplies both upper and conditional matching lower bounds.[6]
- **Claimed result:** For fixed `q₀<1/2` and `1≤k≤q₀d`, the worst-subspace sample threshold is `(m+t) exp{d Ψ(k/d)+O(k^(1/3))}`; the paper also proves a matching lower bound in specified regimes.[6]
- **Assumptions and setting:** Squared population `L₂` loss, Gaussian regression, known `m`-dimensional subspace of degree-at-most-`k` functions on the `d`-dimensional Boolean cube; the lower bound requires `m≤binom(d, floor(k^(1/3)))` or `t≥m`.[6]
- **Caveat:** The matching lower bound is not asserted for every feasible `m,t`; the theorem’s stated asymptotic regime and confidence conditions matter.[6]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics; Machine learning theory

### 4. [Directed fractal percolation and non-Lipschitz variants](https://arxiv.org/abs/2610.12366v1)
- **Abstract:** In Mandelbrot fractal percolation, the authors quantify last-passage growth and construct directed paths through open sites when paths may move exponentially fast in space, defining an unrectifiable directed-percolation variant.[12]
- **Authors:** Shirshendu Ganguly, Victor Ginsburg, Kaihao Jing
- **arXiv:** `2610.12366v1` (published 2026-10-08 17:27:33 UTC; categories: `math.PR`, `math-ph`, `math.CA`, `math.MG`)[12]
- **Evidence for ranking:** Four-way mathematical cross-listing and two concrete claims: an almost-polynomial gap from linear passage-time growth, and a new non-Lipschitz path model.[12]
- **Claimed result:** The authors show high last-passage values are obstructed for Lipschitz paths, while allowing exponentially fast spatial motion yields directed paths through open sites.[12]
- **Assumptions and setting:** The model is Mandelbrot’s scale-by-scale fractal percolation, not a theorem for general random media or Liouville quantum gravity.[12]
- **Caveat:** The proposed non-Lipschitz variant changes the path constraint; it does not overturn the known absence of ordinary directed percolation in the basic model.[12]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Probability & statistics; Mathematical physics; Analysis & PDE

### 5. [The sharp `L²`-Michael–Simon inequality](https://arxiv.org/abs/2610.12309v1)
- **Abstract:** For isometric immersions of `n`-manifolds into Euclidean space with `n≥3`, the authors prove the sharp Michael–Simon Sobolev constant, characterize equality, and extend the argument to conformal ambient settings.[7][8]
- **Authors:** Jeffrey S. Case, Dawit Mengesha
- **arXiv:** `2610.12309v1` (published 2026-10-08 16:58:54 UTC; categories: `math.DG`, `math.AP`)[7]
- **Evidence for ranking:** The full introduction states the sharp constant and equality characterization, and the result connects differential geometry with PDE/Sobolev analysis.[8]
- **Claimed result:** For `n≥3`, the coefficient is the Aubin–Talenti constant `n(n−2) Vol(Sⁿ)^(2/n)/4`, independent of codimension; the authors characterize equality cases.[7][8]
- **Assumptions and setting:** An isometric immersion `j:(Σⁿ,g)→Rᴺ` and test functions in `W^{1,2}(Σ)`; the paper takes manifolds to be connected.[8]
- **Caveat:** The sharp theorem is stated for `n≥3`; equality has a specific conformal/capacity condition and is not simply a claim that every immersion attains equality.[8]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Geometry & topology; Analysis & PDE

### 6. [The moduli space of curves of genus 16 is uniruled](https://arxiv.org/abs/2610.12364v1)
- **Abstract:** Using non-abelian Brill–Noether theory, the authors claim that the moduli space of curves of genus 16 is uniruled, the highest genus for which they say this is known.[9]
- **Authors:** Gavril Farkas, Alessandro Verra
- **arXiv:** `2610.12364v1` (published 2026-10-08 17:27:14 UTC; categories: `math.AG`)[9]
- **Evidence for ranking:** The preprint claims a record genus for uniruledness and reports a new use of non-abelian Brill–Noether theory.[9]
- **Claimed result:** The authors prove `M₁₆` is uniruled.[9]
- **Assumptions and setting:** The statement concerns the moduli space of curves of genus 16; the abstract does not give further technical hypotheses.[9]
- **Caveat:** The record claim and proof details come from a new preprint; its short abstract alone does not expose the construction or establish independent expert validation.[9]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Geometry & topology

### 7. [Ordinary `G`-permutable subgroups of finite simple groups](https://arxiv.org/abs/2610.12329v1)
- **Abstract:** The paper classifies nontrivial proper ordinary `G`-permutable subgroups of finite non-abelian simple groups and claims to solve part (a) of Problem 17.112 in the Kourovka Notebook.[10]
- **Authors:** Shengmin Zhang
- **arXiv:** `2610.12329v1` (published 2026-10-08 17:08:32 UTC; categories: `math.GR`)[10]
- **Evidence for ranking:** It reports a complete classification resolving a named open problem; Semantic Scholar currently lists one citation, a very early total rather than evidence of period growth.[10][16]
- **Claimed result:** Such subgroups occur exactly for the listed families `PSL₂(q)`, `²B₂(2^(2a+1))`, `J₁`, `Sp₄(4)`, and `PSp₄(p)` with the stated congruence restrictions; the paper also classifies them.[10]
- **Assumptions and setting:** Finite non-abelian simple groups; “ordinary `G`-permutable” and proper, nontrivial subgroups are the specific notion and scope.[10]
- **Caveat:** This is not a classification of every broader notion of permutability or of subgroups in arbitrary finite groups.[10]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Algebra & number theory

### 8. [Prevalence of sparsity for negatively curved metrics](https://arxiv.org/abs/2610.12351v1)
- **Abstract:** On a closed manifold of any dimension, the authors prove that negatively curved `Cᵏ` metrics with exponentially sparse length spectra form a prevalent, hence dense, family for sufficiently large `k`.[11]
- **Authors:** Kostiantyn Drach, Vadim Kaloshin
- **arXiv:** `2610.12351v1` (published 2026-10-08 17:20:13 UTC; categories: `math.DG`, `math.DS`)[11]
- **Evidence for ranking:** A prevalence-and-density theorem in differential geometry and dynamics, with a stated sublinear-in-`k` growth rate for the exponent in the sparsity bound.[11]
- **Claimed result:** The authors establish exponential sparsity of distinct closed-geodesic lengths for a prevalent set of negatively curved metrics, with an exponent growing sublinearly in regularity `k`.[11]
- **Assumptions and setting:** Closed manifolds of arbitrary dimension and negatively curved `Cᵏ` metrics, for sufficiently large `k`.[11]
- **Caveat:** Prevalence and density do not mean every negatively curved metric has this property; the theorem requires sufficiently high regularity.[11]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Geometry & topology

## Trending Research Themes

- **Multiscale random geometry (two related but distinct papers):** the Brownian-potential result uses renormalization across scales, while the fractal-percolation paper develops a multiscale framework for passage times. They share a scale-dependent random setting, not an asserted common proof technique.[5][12]
- **Sharp quantitative boundaries:** the Boolean-cube paper pins down an exponential sampling threshold and its remainder, while the Michael–Simon paper identifies an optimal geometric Sobolev constant and equality cases.[6][8]
- **Isolated boundary results, not a field-wide shift:** the undecidability theorem settles a computability question for stability, and the finite-group paper gives a classification for one named problem; their mathematical mechanisms are different.[3][10]
- **Geometry of families:** the genus-16 moduli result and prevalent sparse-length-spectrum theorem each make strong structural claims in different geometric settings; this small sample is not evidence of a broader shift.[9][11]

## Open Problems and Research Directions

- **Author-reported limitation:** the stability paper’s fixed dimension threshold is not computed. A follow-up could make the reduction quantitative and test whether smaller dimensions or degrees are decidable.[3]
- **Author-reported context; proposed extension:** the Brownian paper identifies an earlier open scaling-limit problem for diffusion in a smoothed planar Gaussian free field and proves a weak-disorder result under its hypotheses. Test how far the convergence and singularity conclusions extend toward stronger disorder or broader environments.[5]
- **Gap in stated theorem:** the Boolean-cube upper bound applies to every feasible subspace dimension, but the matching lower bound is limited to stated regimes. Establishing matching lower bounds beyond those regimes would sharpen the sample-complexity picture.[6]
- **Synthesis:** since genus 16 is reported as the highest genus with known uniruledness, investigate what happens in higher genus to locate where the birational behavior changes.[9]

## Takeaway

This batch is unusually rich in sharp structural claims: an undecidability theorem, a new stochastic scaling limit, optimal constants and sample thresholds, and several classifications or genericity results. These are preprint claims from a single announcement day; the ordering signals mathematical substance and cross-field reach, not measured reader attention.

## Method and sources

Daily window: arXiv’s latest Mathematics announcement batch, Friday 2026-10-09 (the request date, Saturday 2026-10-10, has no newer batch listed); snapshot at 2026-10-10 00:18:55 UTC.

The full batch listing reported 504 entries; candidates were taken from `math.*` and retained only when mathematics was a primary or cross-listed category.[1]

Abstract pages for ranks 1–3 were checked on arXiv.[2][4][6]

Abstract pages for ranks 4–6 were also checked.[7][9][12]

Pages for ranks 7–8 were checked as well.[10][11]

The introductions and main-result statements of the first three ranked papers were inspected in their HTML full texts.[3][5][8]

Semantic Scholar currently returns zero citations for the checked genus-16, length-spectrum, and fractal-percolation records.[13][14][15]

The checked finite-group record currently returns one citation; these early totals are too sparse for popularity ranking.[16]

The ranking is an evidence-informed editorial selection based on the specificity of claimed results, stated assumptions, cross-list relevance, and named problems or sharp bounds.

## Sources

[1] https://arxiv.org/list/math/recent — arXiv Mathematics recent submissions listing
[2] https://arxiv.org/abs/2610.12434v1 — Global asymptotic stability is undecidable
[3] https://arxiv.org/html/2610.12434v1 — Global asymptotic stability paper full text
[4] https://arxiv.org/abs/2610.12335v1 — Anomalous scaling limit of Brownian particle
[5] https://arxiv.org/html/2610.12335v1 — Anomalous scaling limit paper full text
[6] https://arxiv.org/abs/2610.12358v1 — Subspace uncertainty and sharp sampling thresholds
[7] https://arxiv.org/abs/2610.12309v1 — Sharp L2 Michael-Simon inequality
[8] https://arxiv.org/html/2610.12309v1 — Sharp L2 Michael-Simon paper full text
[9] https://arxiv.org/abs/2610.12364v1 — Moduli space of curves of genus 16
[10] https://arxiv.org/abs/2610.12329v1 — Ordinary G-permutable subgroups
[11] https://arxiv.org/abs/2610.12351v1 — Prevalence of sparsity for negatively curved metrics
[12] https://arxiv.org/abs/2610.12366v1 — Directed fractal percolation and non-Lipschitz variants
[13] https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.12364?fields=title,citationCount,influentialCitationCount,referenceCount — Semantic Scholar record for arXiv:2610.12364
[14] https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.12351?fields=title,citationCount,influentialCitationCount,referenceCount — Semantic Scholar record for arXiv:2610.12351
[15] https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.12366?fields=title,citationCount,influentialCitationCount,referenceCount — Semantic Scholar record for arXiv:2610.12366
[16] https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.12329?fields=title,citationCount,influentialCitationCount,referenceCount — Semantic Scholar record for arXiv:2610.12329
