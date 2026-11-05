# arXiv Mathematics — Daily report for 4 November 2026

Seven papers from the latest 423-paper Mathematics announcement batch (Wed 4 Nov 2026), led by new sharp-exponent results and structural bounds across probability, combinatorics, number theory, and PDE. This is the most recent batch at the 5 Nov UTC snapshot. Listen for how spectral operators and random-walk geometry turn hard connectivity questions into quantitative laws. No official arXiv trending chart exists; this is an inferred ranking, and citation evidence is limited for such new papers.

## Top papers (ranked)

### 1. [Monochromatic arm exponents for critical planar percolation](https://arxiv.org/abs/2611.05101)
- **Abstract:** The paper determines the critical planar percolation monochromatic three-arm exponent by an explicit positive-operator spectral threshold and gives spectral characterizations for all monochromatic n-arm exponents with n ≥ 4.
- **Authors:** Gefei Cai
- **arXiv:** `2611.05101v1` (published 2026-11-03 15:56:12 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** The paper gives a precise exponent for a long-standing difficult case, with a reproducible operator characterization and a second result extending the method to n ≥ 4; its math.PR/math-ph cross-list reflects the probability and statistical-physics setting.
- **Claimed result:** The author reports that ξ₃ is the unique spectral threshold of an explicit integral-operator family and numerically evaluates it as 0.76928375…; the paper also characterizes ξₙ spectrally for n ≥ 4. The introduction states the result for critical site percolation on the triangular lattice in the scaling limit.
- **Assumptions and setting:** Critical planar site percolation on the triangular lattice, with three disjoint arms of one color across an annulus; the derivation uses CLE/LQG coupling and a boundary observable retaining past connections.
- **Caveat:** The three-arm value is characterized by an operator and numerical evaluation, not a simple closed form; the n ≥ 4 result is a spectral characterization rather than a list of evaluated constants.
- **Announcement type:** new submission, announcement-batch 2026-11-04
- **Themes:** Probability & statistics; Mathematical physics

### 2. [On the one-arm probability for the metric graph Gaussian free field in high dimensions](https://arxiv.org/abs/2611.05357)
- **Abstract:** For sign clusters of the Gaussian free field on cable systems, the authors establish power-law one-arm bounds from volume-growth and Green-function-decay exponents, including a logarithmic loss in the critical upper bound.
- **Authors:** Pierre-François Rodriguez, Jialu Shi, Wen Zhang
- **arXiv:** `2611.05357v1` (published 2026-11-03 18:53:57 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** The main theorem extends the high-dimensional lattice result to weighted graphs without transitivity, under explicit geometric assumptions, and the paper supplies a short proof strategy using exit times, capacity, and a massive-field comparison.
- **Claimed result:** The authors prove θ(x,R) is bounded above and below by constants times R⁻ᵝ when 2α < 3ν; at 2α = 3ν, the lower bound remains cR⁻ᵝ and the upper bound is CR⁻ᵝ log(1+R). For ℤᵈ, the regimes correspond to d > 6 and d = 6.
- **Assumptions and setting:** A transient, locally finite weighted graph satisfying uniform ellipticity, volume growth V(B(x,R)) ≍ Rᵅ, and Green-function decay g(x,y) ≍ d(x,y)⁻ᵛ; β = α − ν. The equality case has a weaker logarithmic upper estimate.
- **Caveat:** The critical theorem does not give matching bounds up to constants; the paper notes that sharper asymptotics for ℤ⁶ are addressed in forthcoming work, not established by this paper.
- **Announcement type:** new submission, announcement-batch 2026-11-04
- **Themes:** Probability & statistics; Mathematical physics

### 3. [A near-quadratic lower bound for the Brown--Erdős--Sós (9,6)-problem](https://arxiv.org/abs/2611.05261)
- **Abstract:** For a 3-uniform hypergraph avoiding six edges on at most nine vertices, the authors prove a lower bound n² exp(−O((log n)²ᐟ³)), resolving the first unsolved case of a broader conjecture.
- **Authors:** Xiangliang Kong, Chong Shangguan, Xin Wang
- **arXiv:** `2611.05261v1` (published 2026-11-03 17:48:55 UTC; categories: `math.CO`)
- **Evidence for ranking:** The abstract identifies this as the first unsolved case of the fixed-e conjecture and states an explicit near-quadratic bound; this is a concrete resolution claim rather than a recency-only selection.
- **Claimed result:** The authors prove f₃(n,9,6) ≥ n² exp(−O((log n)²ᐟ³)), where f₃(n,e+3,e) is the maximum number of edges in an n-vertex 3-uniform hypergraph with no e distinct edges spanning at most e+3 vertices.
- **Assumptions and setting:** 3-uniform hypergraphs; the result treats the specific parameter pair (e+3,e) = (9,6) and asserts the bound asymptotically in n.
- **Caveat:** The result settles e = 6 only; the conjectured near-quadratic lower bound for every fixed e ≥ 3 remains broader than the case proved here.
- **Announcement type:** new submission, announcement-batch 2026-11-04
- **Themes:** Combinatorics & discrete mathematics

### 4. [On the van der Corput property for cubes](https://arxiv.org/abs/2611.05267)
- **Abstract:** The authors prove a power-saving version of the van der Corput property for cubes and derive a power-saving upper bound for subsets of [N] with no nonzero cube differences.
- **Authors:** Steve Fan, Andrew Lott, Ákos Magyar, Máté Matolcsi, Imre Z. Ruzsa
- **arXiv:** `2611.05267v1` (published 2026-11-03 17:54:46 UTC; categories: `math.NT`, `math.CO`)
- **Evidence for ranking:** It combines an explicit power-saving theorem with a direct consequence for a classical additive-combinatorial extremal problem, and is cross-listed between number theory and combinatorics.
- **Claimed result:** The authors obtain |A| ≪ε N^(59/60+ε) for A ⊆ {1,…,N} containing no nonzero difference that is a cube.
- **Assumptions and setting:** Finite subsets of the first N positive integers; the stated bound is for every ε > 0, with the implicit constant allowed to depend on ε.
- **Caveat:** The abstract establishes this exponent but does not claim it is optimal or characterize extremal cube-difference-free sets.
- **Announcement type:** new submission, announcement-batch 2026-11-04
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 5. [Transfer of Weisfeiler-Leman equivalence under graph operations](https://arxiv.org/abs/2611.05366)
- **Abstract:** The authors determine how much Weisfeiler-Leman equivalence is needed before selected graph operations preserve k-dimensional equivalence, exactly for line graphs and in several generalized line-graph regimes.
- **Authors:** Dmitriy Kunisky, Hamilton Sawczuk
- **arXiv:** `2611.05366v1` (published 2026-11-03 18:56:45 UTC; categories: `math.CO`, `cs.DM`)
- **Evidence for ranking:** The paper gives exact transfer parameters for line graphs, matching upper and lower bounds, and covers generalized (r,S)-line graphs; the math.CO/cs.DM cross-list links structural combinatorics to discrete algorithms.
- **Claimed result:** The authors prove τL(k) = 2k+1 for k ≥ 2 and τL(1) = 1; for (r,S)-line graphs they give τr,S(1) = r−1, exact values rk+r−1 for specified S when k ≥ r, and bounds in the remaining range.
- **Assumptions and setting:** Equivalence is that induced by k-dimensional Weisfeiler-Leman graph-isomorphism tests; results concern line graphs and the stated family of clique-based (r,S)-line graph operations.
- **Caveat:** Exact values are not obtained for every generalized operation and parameter range; the abstract says the remaining range is bounded rather than fully determined.
- **Announcement type:** new submission, announcement-batch 2026-11-04
- **Themes:** Combinatorics & discrete mathematics; Machine learning theory

### 6. [Stable soliton resolution for the corotational Skyrme model](https://arxiv.org/abs/2611.05352)
- **Abstract:** Under corotational symmetry, the author proves uniqueness of stationary Skyrmions in each topological degree, global well-posedness in a nonlinear energy space, and stable soliton resolution for finite-energy solutions.
- **Authors:** Uihyeon Jeong
- **arXiv:** `2611.05352v1` (published 2026-11-03 18:51:51 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract claims a full long-time resolution result together with global well-posedness and uniqueness, and identifies an analytic mechanism—subcritical equivariant Yang-Mills dynamics—that suppresses concentration.
- **Claimed result:** The author states that every finite-energy corotational solution scatters to the Skyrmion of the same topological degree.
- **Assumptions and setting:** The classical Skyrme model restricted to corotational symmetry; initial data have finite energy and are treated in a nonlinear energy space.
- **Caveat:** The result is symmetry-restricted and does not establish soliton resolution for unrestricted Skyrme dynamics.
- **Announcement type:** new submission, announcement-batch 2026-11-04
- **Themes:** Analysis & PDE; Mathematical physics

### 7. [On the abc conjecture](https://arxiv.org/abs/2611.05217)
- **Abstract:** Using adelic intersection theory, the author claims an effective height bound for genus-two curves over number fields and derives a weak abc-type inequality.
- **Authors:** Christophe Soulé
- **arXiv:** `2611.05217v1` (published 2026-11-03 17:03:07 UTC; categories: `math.AG`, `math.NT`)
- **Evidence for ranking:** The abstract makes a concrete arithmetic-geometry claim and cross-lists algebraic geometry with number theory; the paper's introduction states explicit height and abc-type bounds, making the scope checkable rather than relying on its headline.
- **Claimed result:** The author states that for a genus-two curve C over a number field K₀, points P over finite extensions F satisfy h(P) ≤ (12+ε) log|ΔF|/[F:ℚ] + β(ε). The introduction derives c ≤ A(ε) rad(abc)^(24+ε) for coprime positive integers a+b=c.
- **Assumptions and setting:** A smooth, projective, geometrically irreducible genus-two curve over a number field; the stated point-height inequality ranges over finite extensions and points rational over those extensions.
- **Caveat:** The derived exponent 24+ε is much weaker than the classical abc bound with exponent 1+ε; this preprint does not claim to prove the full abc conjecture. Its proof has not been independently assessed here.
- **Announcement type:** new submission, announcement-batch 2026-11-04
- **Themes:** Algebra & number theory

## Trending Research Themes

- **Sharp probabilities and exponent extraction:** The planar-percolation paper turns a monochromatic arm event into a spectral threshold, while the metric-graph GFF paper converts volume growth and Green decay into one-arm exponents. Both make an exponent accessible through a tractable analytic object, but in distinct models and with different hypotheses.
- **Extremal combinatorics and additive structure:** The Brown--Erdős--Sós result proves a near-quadratic lower bound for the first unsolved parameter case; the cube-difference paper gives a power-saving density bound through a van der Corput method. These are related by quantitative avoidance questions, not by a shared proof technique.
- **Structural bounds across discrete mathematics:** The Weisfeiler-Leman paper quantifies how graph transformations change the strength needed for graph equivalence; it complements the extremal papers as another precise bound/classification problem, though the objects and methods differ.
- **Geometry driving long-time behavior:** The Skyrme analysis links emergent Yang--Mills dynamics to suppression of concentration, yielding soliton resolution under symmetry. This is an isolated PDE signal in today's selected set, not evidence of a field-wide shift.
- **Arithmetic geometry and abc-type consequences:** The Soulé preprint connects adelic intersection theory and heights on genus-two curves to a weak abc inequality. The stated exponent is far from the classical conjectural bound, so the headline should not be mistaken for a proof of abc.

## Open Problems and Research Directions

- **Author-stated — Brown--Erdős--Sós for other fixed parameters:** The abstract frames f₃(n,e+3,e) ≥ n^(2−o(1)) for every fixed e ≥ 3 as the broader conjecture; this paper handles e = 6. A natural follow-up is to test whether the construction or estimate extends to the remaining fixed-e cases. [2611.05261]
- **Author-stated — critical one-arm asymptotics:** At 2α = 3ν, the theorem leaves a logarithmic gap between its lower and upper bounds. The introduction points to forthcoming work for sharper ℤ⁶ asymptotics; an evidence-tied extension is to determine whether comparable sharp corrections hold on non-transitive graphs satisfying the same growth assumptions. [2611.05357]
- **Author-stated — higher monochromatic arm exponents:** The percolation paper gives spectral characterizations for n ≥ 4 but numerically evaluates the three-arm case. Computing or rigorously bounding the spectral thresholds for n ≥ 4 would turn those characterizations into quantitative estimates. [2611.05101]
- **Synthesis — strength of cube-difference bounds:** The 59/60+ε exponent is explicit, but the abstract does not claim optimality. Compare it with constructions of large cube-difference-free sets and seek either an improved upper bound or a matching obstruction. [2611.05267]
- **Synthesis — generalized WL transfer parameters:** Exact values are available only for specified (r,S) regimes, with bounds elsewhere. Determining when those upper bounds are sharp is a concrete extension of the paper's classification program. [2611.05366]
- **Synthesis — symmetry boundary in soliton resolution:** Since the Skyrme theorem assumes corotational symmetry, one test of its reach is to identify which parts of the concentration-suppression argument survive under weaker symmetry or perturbations. [2611.05352]
- **Synthesis — scope of the abc-type consequence:** The reported exponent 24+ε is weaker than the classical 1+ε target. A follow-up is to isolate which step in the adelic intersection argument controls that loss and whether additional geometric input improves it. [2611.05217]

## Takeaway

Today's most compelling mathematical signals are precise probability exponents and quantitative extremal bounds, with several substantial results attached to explicit hypotheses. This shortlist identifies potentially important new work, not measured readership; the papers are fresh preprints, and their claims still require specialist verification.

## Method and sources

- **Window:** Daily announcement batch 2026-11-04 (start and end date: 2026-11-04), the latest available batch at the snapshot time 2026-11-05 01:26:25 UTC; it is a prior batch relative to the snapshot date. The arXiv recent listing identifies 423 Mathematics entries in this batch; the selected papers' first-version timestamps are on 2026-11-03 UTC.
- **Coverage:** Full arXiv Mathematics recent listing for the 4 November batch (`math`), including subject classes across the archive. The seven selected papers retain their specific primary and cross-list categories.
- **Selection:** Seven papers ranked by concrete stated results, breadth of setting, cross-list relevance, and clear scope; recency served only as a tie-breaker. No independent expert discussion was verified. Citation and influential-citation totals could not be corroborated from the sources checked, so this is a notable-recent-paper shortlist rather than evidence of readership momentum.
- **Retrieval note:** The configured `web_extract` route did not support URL extraction in this session; the complete listing and selected abstract pages were read in the browser, and the top three introductions/main-result statements were inspected in arXiv HTML. Semantic Scholar citation fields were not available from the sources checked.
- **Sources:** [Full Mathematics recent listing](https://arxiv.org/list/math/recent?skip=0&show=500); selected arXiv abstract pages: [2611.05101](https://arxiv.org/abs/2611.05101), [2611.05357](https://arxiv.org/abs/2611.05357), [2611.05261](https://arxiv.org/abs/2611.05261), [2611.05267](https://arxiv.org/abs/2611.05267), [2611.05366](https://arxiv.org/abs/2611.05366), [2611.05352](https://arxiv.org/abs/2611.05352), [2611.05217](https://arxiv.org/abs/2611.05217). Full text inspected for the top three: [percolation HTML](https://arxiv.org/html/2611.05101v1), [GFF HTML](https://arxiv.org/html/2611.05357v1), [abc HTML](https://arxiv.org/html/2611.05217v1).
