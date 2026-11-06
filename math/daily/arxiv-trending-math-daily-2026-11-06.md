# arXiv Mathematics — daily notable papers, 6 November 2026

Latest announcement batch: Friday, 2026-11-06. Nine papers highlighted from a 409-entry Mathematics recent listing. The strongest shared pattern is sharp resolution of long-standing bounds, uniqueness questions, and classification problems, usually within carefully delimited settings. Spoken agenda: discrepancy and geometry first, then stochastic uniqueness, number theory, and nonlinear PDE. Caveat: arXiv has no official trending chart; this is an inferred notable-paper ordering, not a readership ranking, and citation evidence for papers this new is limited.

## Top papers (ranked)

### 1. [Tusnády's problem and online two-sample thinning](https://arxiv.org/abs/2611.08455)
- **Abstract:** The paper establishes sharp discrepancy orders for Tusnády's problem in every fixed dimension at least two, then applies them to online two-sample thinning, obtaining sharp prefix bounds and a one-dimensional terminal order.
- **Authors:** Yuhao Lei
- **arXiv:** `2611.08455v1` (published 2026-11-05T18:47:43Z; categories: `math.CO`, `cs.DS`, `math.PR`)
- **Evidence for ranking:** Cross-listed across combinatorics, algorithms, and probability; the paper matches Nikolov's upper bound with a sharp fixed-dimension order and connects that result to minimax online-thinning bounds. These are concrete, cross-field mathematical signals, not measured readership.
- **Claimed result:** The author proves the largest box discrepancy is Θ_d((log N)^(d−1/2)) for each fixed d≥2, and gives a Θ_{k,ρ}((log n)^(k+1/2)) minimax expected prefix discrepancy for fixed k≥1 and 0<ρ<2; in one dimension the terminal order is Θ_ρ((log log n)^(3/2)).
- **Assumptions and setting:** Dimensions are fixed as N or n grows; the online model uses two independent samples from a common unknown Borel distribution and an expected deletion budget ρn, with 0<ρ<2.
- **Caveat:** For k≥2, the paper's terminal online-thinning lower and upper bounds still differ by a factor of log n; the author identifies closing this gap as open.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 2. [Hyperpolarity of polar foliations of codimension two](https://arxiv.org/abs/2611.08480)
- **Abstract:** For compact simply connected irreducible symmetric spaces of rank at least two, the author proves codimension-two polar foliations are hyperpolar and identifies the exceptional Cayley-plane cases.
- **Authors:** Stephan Wiesendorf
- **arXiv:** `2611.08480v1` (published 2026-11-05T18:59:13Z; categories: `math.DG`)
- **Evidence for ranking:** The introduction identifies codimension two as the remaining open case of a named hyperpolarity problem and says the result settles it without a homogeneity assumption; the paper also gives a precise rigidity classification for the Cayley-plane exception.
- **Claimed result:** The author proves every codimension-two polar singular Riemannian foliation on a compact simply connected symmetric space of rank at least two is hyperpolar. For the specified irreducible spherical Coxeter quotients on the Cayley plane, every foliation is congruent to one of two known homogeneous models.
- **Assumptions and setting:** The main theorem assumes a compact, simply connected, irreducible symmetric space of rank at least two and a codimension-two polar singular Riemannian foliation.
- **Caveat:** This closes the codimension-two case in the stated compact symmetric-space setting; it is not a classification of polar foliations on arbitrary ambient manifolds.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Geometry & topology

### 3. [Weak uniqueness for the stochastic heat equation with nondegenerate diffusion: the full Hölder regime](https://arxiv.org/abs/2611.07310)
- **Abstract:** The author proves weak well-posedness for a scalar stochastic heat equation on the one-dimensional torus with uniformly nondegenerate diffusion coefficients of every positive Hölder order, and extends the result to specified measurable drifts.
- **Authors:** Yi Han
- **arXiv:** `2611.07310v1` (published 2026-11-05T01:55:58Z; categories: `math.PR`)
- **Evidence for ranking:** The author states the result resolves the full positive-Hölder weak-uniqueness range beyond the author's previous exponent-above-two-thirds result; the arXiv comment links a Lean formalization, a checkable proof artifact.
- **Claimed result:** The author proves existence and uniqueness in law for the scalar equation with uniformly nondegenerate, bounded Hölder diffusion of any positive order, and gives further uniqueness results for unbounded diffusion with bounded initial data and for measurable drifts of linear growth under the stated hypotheses.
- **Assumptions and setting:** The core theorem concerns the scalar stochastic heat equation driven by space-time white noise on the one-dimensional torus, deterministic L² initial data, and a uniformly nondegenerate bounded diffusion coefficient that is Hölder continuous with some exponent β>0.
- **Caveat:** The paper proves weak uniqueness, not pathwise uniqueness. Its unbounded-diffusion extension assumes bounded initial data; the author says relaxing this to L² initial data may require a finer near-time-zero argument.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Probability & statistics; Analysis & PDE

### 4. [On a problem due to Erdős concerning w₁(n)](https://arxiv.org/abs/2611.07617)
- **Abstract:** For the function w defined from the prime-power factorization of n, the author answers Erdős's question about the number V(x) of distinct values w(n) for n≤x by proving its lower density is positive in the liminf sense.
- **Authors:** John M. Campbell
- **arXiv:** `2611.07617v1` (published 2026-11-05T08:01:07Z; categories: `math.NT`)
- **Evidence for ranking:** The abstract directly identifies the question as an Erdős problem left open in a 1980 source and says it also appears in Guy's unsolved-problems book; the claimed positive-liminf bound is stronger than merely disproving V(x)=o(x).
- **Claimed result:** The author proves liminf_{x→∞} V(x)/x > 0, where V(x)=|{w(n):1≤n≤x}| and w(n)=Σ_{p^α∥n} n/p^α for n>1, with w(1)=0.
- **Assumptions and setting:** The setting is the specified arithmetic function on positive integers and the count of its distinct values up to x.
- **Caveat:** The abstract establishes a positive lower density in liminf, but does not state an exact limiting density or a full asymptotic formula for V(x).
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Algebra & number theory

### 5. [On do Carmo's Question: The Properly Embedded Case](https://arxiv.org/abs/2611.08454)
- **Abstract:** The author proves that every complete noncompact, two-sided, properly embedded constant-mean-curvature hypersurface of finite Morse index in Euclidean space is minimal, in every dimension and without curvature or volume-growth bounds.
- **Authors:** Gongping Niu
- **arXiv:** `2611.08454v1` (published 2026-11-05T18:47:40Z; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** The result is cross-listed in geometry and analysis, resolves the properly embedded case of a named finite-index question, and retains the conclusion without imposing curvature or volume-growth bounds.
- **Claimed result:** The author proves the stated hypersurface must be minimal; the abstract outlines a weighted-volume argument combined with stability outside a compact set.
- **Assumptions and setting:** The hypersurface is complete, noncompact, two-sided, properly embedded, has constant mean curvature, and has finite Morse index in Euclidean space.
- **Caveat:** The theorem is specifically for properly embedded hypersurfaces; the abstract does not claim the corresponding result for general immersed or nonproper hypersurfaces.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Geometry & topology; Analysis & PDE

### 6. [Necessary and sufficient conditions for the self-normalized central limit theorem for independent triangular arrays](https://arxiv.org/abs/2611.08137)
- **Abstract:** For rowwise independent triangular arrays, the authors derive consequences of a self-normalized normal limit and, combined with earlier work, obtain necessary and sufficient conditions for the self-normalized central limit theorem, resolving a conjecture for independent sequences.
- **Authors:** Xiang Li, Song-Hao Liu, Qi-Man Shao, Hao Shi, Jing-Yu Xu
- **arXiv:** `2611.08137v1` (published 2026-11-05T15:01:50Z; categories: `math.PR`)
- **Evidence for ranking:** The abstract gives an explicit necessary-and-sufficient characterization and says it resolves Shao's conjecture for independent sequences; it also states two quantitative-in-probability consequences of the self-normalized normal limit.
- **Claimed result:** The authors show that S_n/V_n converging in distribution to N(0,1) forces max_i |X_{n,i}|/V_n to converge to zero in probability and V_n²/b_n² to converge to one for any median b_n² of V_n²; together with Shao (2018), this yields the stated characterization.
- **Assumptions and setting:** The array is rowwise independent, S_n is the row sum, and V_n² is the sum of squared entries; the characterization is for independent sequences, not general dependence.
- **Caveat:** Dependence across entries is not covered by the stated result, and the abstract's characterization relies in part on Shao's earlier theorem.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Probability & statistics

### 7. [Classification of cohomogeneity one steady gradient Ricci solitons in dimension four and five](https://arxiv.org/abs/2611.08206)
- **Abstract:** The authors prove a uniqueness conjecture for an Appleton soliton and classify non-Ricci-flat κ-noncollapsed cohomogeneity-one steady gradient Ricci solitons in dimensions four and five, up to finite cover.
- **Authors:** Yuxing Deng, Guohao Wang
- **arXiv:** `2611.08206v1` (published 2026-11-05T15:59:38Z; categories: `math.DG`)
- **Evidence for ranking:** The abstract combines a named conjecture resolution with a dimension-specific classification into explicit known solitons, a stronger signal than recency alone.
- **Claimed result:** The authors state that in dimension four the soliton must, after a finite cover, be the Bryant soliton or Appleton's noncollapsed four-dimensional steady soliton; in dimension five it must be the Bryant soliton or a soliton constructed by Ivey–Dancer–Wang.
- **Assumptions and setting:** The classification is for non-Ricci-flat, κ-noncollapsed, cohomogeneity-one steady gradient Ricci solitons in dimensions four and five.
- **Caveat:** The result does not purport to classify higher dimensions, other cohomogeneities, or Ricci-flat cases.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Geometry & topology; Analysis & PDE

### 8. [Global well-posedness for the energy-critical focusing NLS on T³](https://arxiv.org/abs/2611.07740)
- **Abstract:** The authors prove global well-posedness for the focusing quintic nonlinear Schrödinger equation on the standard three-dimensional torus for initial data below the mass-corrected energy and Sobolev thresholds determined by the Euclidean ground state.
- **Authors:** Meng Chen, Han Wang
- **arXiv:** `2611.07740v1` (published 2026-11-05T09:49:05Z; categories: `math.AP`)
- **Evidence for ranking:** The paper claims a global result for an energy-critical focusing equation on a compact domain, under explicit ground-state thresholds, and connects periodic profile analysis with a recent Euclidean scattering theorem.
- **Claimed result:** The authors prove global well-posedness below both stated mass-corrected energy and Sobolev-norm thresholds, using an invariant region, a nonnegative energy decomposition, and a contradiction argument for finite-time bounds.
- **Assumptions and setting:** The equation is the focusing quintic NLS on the standard three-dimensional torus, with initial data strictly below the stated Euclidean-ground-state thresholds.
- **Caveat:** The abstract covers the subthreshold regime only; it makes no claim at or above the threshold.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Analysis & PDE; Mathematical physics

### 9. [Butler's conjecture for K3 curves](https://arxiv.org/abs/2611.08333)
- **Abstract:** The authors prove two cases of Butler's conjectures for curves of genus at least eight by establishing the result on curves lying on Picard-rank-one K3 surfaces and using deformation and openness.
- **Authors:** Soheyla Feyzbakhsh, Aliaksandra Novik, Angela Ortega
- **arXiv:** `2611.08333v1` (published 2026-11-05T17:21:35Z; categories: `math.AG`)
- **Evidence for ranking:** The abstract addresses a named conjectural family and combines wall-crossing for coherent systems with a K3-surface construction; the stated theorem treats two mathematically distinct rank/slope regimes.
- **Claimed result:** For g≥8, the authors prove Butler's conjectures in the rank-one case and in the range μ(E)>2g−2, under the stated general-curve and semistability framework.
- **Assumptions and setting:** The proof reduces by deformation and openness to a Brill–Noether–Petri general curve on a K3 surface of Picard rank one; the covered cases are rank one and μ(E)>2g−2.
- **Caveat:** The result covers only the two stated cases for genus at least eight, not the full conjecture for all ranks and slopes.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

## Trending Research Themes

- Sharp bounds are a visible thread across distinct areas: Tusnády discrepancy reaches a sharp fixed-dimension exponent and the online thinning result separates prefix from terminal objectives; the number-theory paper strengthens a qualitative Erdős question to a positive-liminf density statement. These are separate problems, not evidence of a shared technique.
- Several papers push a theorem to the edge of a previously open parameter regime: the stochastic heat equation result reaches every positive Hölder exponent, the self-normalized CLT paper supplies necessary and sufficient conditions for independent sequences, and the K3 paper proves Butler's conjectures in two specified regimes. The scope restrictions differ and should not be conflated.
- Geometry and nonlinear analysis also feature classification and global-control results: the polar-foliation paper closes a codimension-two case, the Ricci-soliton paper classifies the stated four- and five-dimensional families, and the CMC and NLS papers establish rigidity or global behavior under their respective finite-index and subthreshold hypotheses.
- Cross-field links are concrete but selective: Tusnády's result is cross-listed in combinatorics, discrete algorithms, and probability; the properly embedded CMC result is cross-listed in differential geometry and analysis. The other entries remain focused in their listed primary areas.

## Open Problems and Research Directions

- Open problem (author-stated): For online two-sample thinning in dimensions k≥2, the terminal bounds still differ by a factor of log n. The paper explicitly leaves closing that gap open. A follow-up could test whether the lower bound can be strengthened or whether a distribution-free thinning rule can improve the upper bound. [2611.08455]
- Open limitation (author-stated): The stochastic heat equation paper distinguishes weak uniqueness from pathwise uniqueness and says its L²-initial-data extension for unbounded diffusion may need a finer near-time-zero argument. A direct route is to investigate whether the localization can be sharpened to remove the bounded-initial-data condition. [2611.07310]
- Open direction (synthesis): The NLS theorem is strictly subthreshold. Studying the threshold endpoint, and identifying which parts of the invariant-region/profile argument fail above it, would clarify how sharp the stated regime is. This is a proposed extension, not a claim that the paper settles or explicitly formulates that question. [2611.07740]
- Open direction (synthesis): The Erdős-function result proves a positive liminf for V(x)/x but does not give an exact density or asymptotic. Establishing whether the ratio converges, or bounding its liminf more sharply, would refine the answer. [2611.07617]
- Open direction (synthesis): Butler's result covers genus at least eight in two rank/slope cases. Extending the K3 wall-crossing argument to the remaining ranks and slopes, or to lower genus, would test how far the conjectural evaluation-map and kernel-stability conclusions persist. [2611.08333]

## Takeaway

The most compelling items in this batch are not tied to one emerging subfield: they are rigorous-looking preprint claims that close a named gap, sharpen an exponent, or identify a uniqueness/classification regime. Because this is a single fresh batch with limited independent attention and citation evidence, treat the ordering as a reading shortlist rather than a popularity measure; the stated theorems still need expert review.

## Method and sources

- Window: daily announcement batch dated 2026-11-06 (Friday); batch window 2026-11-06 to 2026-11-06. Snapshot time: 2026-11-06 17:24:15 UTC. This uses today's batch, not a prior batch. The 409-entry arXiv Mathematics recent listing was traversed. New-submission timestamps in the batch include 2026-11-04 and 2026-11-05; the listing also contains three revision entries, which were treated as revisions, not new submissions. The nine selected papers below are all new submissions.
- Scope: arXiv Mathematics (`math.*`) as the core corpus, preserving exact primary and cross-list categories. Neighboring classes were retained only when cross-listed in mathematics or when their central contribution was mathematical; unrelated communications and engineering items were not treated as math papers. The candidate listing's entries were de-duplicated by versionless arXiv ID.
- Inference: selected nine notable papers from the batch using explicit results, problem/conjecture status stated in abstracts or introductions, cross-listing, and a linked formalization where present. Recency was a tie-breaker only. No official arXiv trending or readership metric exists. Semantic Scholar citation fields could not be retrieved at this snapshot, so no citation totals or citation momentum were used.
- Sources: [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); [arXiv API](https://export.arxiv.org/api); each linked arXiv abstract page above. For the first three papers, the PDF introductions and main-result statements were inspected. Web extraction was unavailable in this runtime; arXiv records were obtained through its API and the abstract/PDF pages directly.
