# Mathematics on arXiv — rolling 30-day report

## Headline

Mathematics · latest announcement batch 2026-09-29 · 8,897 unique arXiv records in the month-window pool; 9 notable papers highlighted here. A striking pattern in this selection is exact classification: long-standing conjectures are resolved, bounded, or given explicit counterexamples. Spoken agenda: graph spectra, restarted algorithms, quantum graph coloring, sharp PDE regularity, then combinatorics and functional analysis. There is no official arXiv trending chart; this is an inferred notable-paper selection, not a readership ranking, and citation evidence for these recent papers is sparse.

Snapshot: 2026-09-30 10:43:14 UTC. Archive-date window queried: 2026-08-31 through 2026-09-30 UTC; the latest records returned were announced 2026-09-29, so no 2026-09-30 batch was present at snapshot time. The query includes the whole UTC start date, so it can include submissions earlier than the exact 30×24-hour cutoff by up to 10h 43m.[1]

## Top papers (ranked)

### 1. [The maximum relaxation time of a random walk on regular graphs](https://arxiv.org/abs/2609.06818v2)
- **Abstract:** The paper gives sharp quadratic extremal bounds for random-walk relaxation time on connected regular graphs and reports resolutions of several associated graph-spectral conjectures.[2]
- **Authors:** Haoran Zhu.[2]
- **arXiv:** `2609.06818v2` (published 2026-09-06T20:27:47Z; categories: `math.PR`).[2]
- **Evidence for ranking:** The abstract names the Aldous–Fill spectral-gap conjecture and several structural/uniqueness conjectures; the current version is explicitly described as substantially expanded. This is a concrete-result signal, not readership evidence.[2]
- **Claimed result:** The author claims leading relaxation-time constants 3/(2π²) for even and 1/π² for odd graph orders, and identifies the extremizing regular-graph chains for sufficiently large order; the paper also reports sharp algebraic-connectivity, stability, hitting-time, and commute-time results.[2]
- **Assumptions and setting:** Finite, simple, undirected connected graphs; relaxation-time extremal statements concern regular graphs, while other theorems impose their stated minimum-degree or fixed-degree conditions.[2]
- **Caveat:** The abstract's unique-extremizer statement is for sufficiently large order; the several subsidiary sharp bounds have their own hypotheses and should not be read as one uniform theorem.[2]
- **Announcement type:** revision, announcement-batch date 2026-09-23.[2]
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics.

### 2. [A Complete Resolution of Forsythe's Conjecture for Restarted Conjugate Gradients](https://arxiv.org/abs/2609.04659v2)
- **Abstract:** For exact restarted conjugate gradients on real symmetric positive-definite systems, the authors classify precisely which restart lengths force even/odd residual-direction convergence and construct counterexamples above the threshold.[3]
- **Authors:** Matthew J. Colbrook, George Stepaniants, Alex Townsend.[3]
- **arXiv:** `2609.04659v2` (published 2026-09-04T02:46:48Z; categories: `math.NA`, `math.DS`, `math.OC`).[3]
- **Evidence for ranking:** The paper gives a sharp all-restart-length classification, spans three mathematical categories, and reports a Lean formalization of the classification.[3]
- **Claimed result:** In exact arithmetic, restart lengths 2 and 3 either terminate or have convergent even and odd normalized residual directions; for every restart length s≥4, a nonterminating diagonal positive-definite counterexample exists in dimension s+4. Together with the s=1 theorem, the universal claim holds exactly for s∈{1,2,3}.[3]
- **Assumptions and setting:** Finite-dimensional real symmetric positive-definite matrices, arbitrary initial data, and exact arithmetic; the counterexamples are diagonal.[3]
- **Caveat:** This is an asymptotic direction result, not a finite-precision guarantee or a convergence-rate estimate for practical solver implementations.[3]
- **Announcement type:** revision, announcement-batch date 2026-09-07.[3]
- **Themes:** Numerical analysis & computation; Optimization & control.

### 3. [A counterexample to the quantum Hedetniemi conjecture](https://arxiv.org/abs/2609.20690v1)
- **Abstract:** Explicit finite graphs violate the conjectured equality between the quantum chromatic number of a categorical product and the smaller quantum chromatic number of its factors.[4]
- **Authors:** Julius A. Zeiss.[4]
- **arXiv:** `2609.20690v1` (published 2026-09-17T16:57:12Z; categories: `math.CO`, `quant-ph`).[4]
- **Evidence for ranking:** The paper supplies a numerical gap between product and factor bounds, is cross-listed in combinatorics and quantum physics, and says its graph constructions and projective-formulation counterexamples are formalized in Lean 4.[4]
- **Claimed result:** The authors construct G,H with χ(G×H)≤1538 while min(χq(G),χq(H))≥1539, disproving the conjecture and extending the failure to spatial, approximate, commuting-operator, and C*-algebraic variants.[4]
- **Assumptions and setting:** Finite simple graphs and the quantum-coloring models defined in the paper; the displayed construction is explicit but very large.[4]
- **Caveat:** The result is a counterexample to a specific product identity, not a general formula for quantum chromatic numbers; the headline construction uses graphs with over a million vertices.[4]
- **Announcement type:** new submission, announcement-batch date 2026-09-17.[4]
- **Themes:** Combinatorics & discrete mathematics; Mathematical physics.

### 4. [Sharp Hessian integrability for fully nonlinear elliptic supersolutions in low dimensions](https://arxiv.org/abs/2609.06817v1)
- **Abstract:** The authors settle the planar sharp Hessian-integrability conjecture and obtain the matching three-dimensional exponent for ellipticity ratios from 1 through 4.[5]
- **Authors:** Thialita M. Nascimento, Eduardo V. Teixeira.[5]
- **arXiv:** `2609.06817v1` (published 2026-09-06T20:19:50Z; categories: `math.AP`).[5]
- **Evidence for ranking:** The abstract gives an explicit optimal exponent and identifies the exact parameter range reached in dimension three, a sharply checkable resolution rather than a vague improvement claim.[5]
- **Claimed result:** For viscosity supersolutions of fully nonlinear uniformly elliptic equations, the authors claim ε₂(κ)=2/(κ+1) in dimension two and ε₃(κ)=3/(2κ+1) in dimension three for 1≤κ≤4, where κ=Λ/λ.[5]
- **Assumptions and setting:** The setting is the W²,ε regularity theory for viscosity supersolutions of fully nonlinear uniformly elliptic equations, with ellipticity ratio κ=Λ/λ.[5]
- **Caveat:** In dimension three, the abstract says that for κ>4 the paper gives a lower bound and identifies a remaining gap; it does not claim the optimal exponent is settled there.[5]
- **Announcement type:** new submission, announcement-batch date 2026-09-06.[5]
- **Themes:** Analysis & PDE.

### 5. [Sign patterns of real powers of infinite products: resolution of four conjectures of Schlosser and Zhou](https://arxiv.org/abs/2609.22324v1)
- **Abstract:** The paper resolves four conjectures on coefficient-sign patterns for specified powers of four q-products, including precise parameter intervals where several conjectures fail.[6]
- **Authors:** Jaideep Sai Padhi.[6]
- **arXiv:** `2609.22324v1` (published 2026-09-16T03:59:42Z; categories: `math.CO`).[6]
- **Evidence for ranking:** It settles four named conjectures, pinpoints exact failure intervals and thresholds, and reports code plus certificates for its computational components.[6]
- **Claimed result:** The author claims one conjecture is true and three fail on explicitly specified intervals; the proof combines exact cusp analysis and explicit Hardy–Ramanujan–Rademacher expansions with certified exact/ball-arithmetic checks on finite and degenerate cases.[6]
- **Assumptions and setting:** The results concern coefficient signs of powers of four specified Goellnitz–Gordon/Borwein infinite products, for the parameter ranges stated in the paper.[6]
- **Caveat:** The conclusions cover these four products and conjectures, not sign patterns for arbitrary infinite products; some finite-range claims depend on certified computation.[6]
- **Announcement type:** new submission, announcement-batch date 2026-09-16.[6]
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics.

### 6. [Nonmaximal sums of maximally monotone operators under Rockafellar's constraint qualification](https://arxiv.org/abs/2609.10487v4)
- **Abstract:** The author constructs maximally monotone operator pairs satisfying an interior-domain condition whose sum is not maximally monotone, and develops constructions that transfer the counterexamples across Banach spaces.[7]
- **Authors:** Weifeng Yang.[7]
- **arXiv:** `2609.10487v4` (published 2026-09-09T17:26:26Z; categories: `cs.LG`, `math.FA`).[7]
- **Evidence for ranking:** The latest version is a substantial reorganization around a general construction and pullback theorem; it directly addresses a named sum conjecture and is cross-listed in functional analysis and machine learning.[7]
- **Claimed result:** The author claims a complete disproof of Rockafellar's sum conjecture under the stated interior-domain condition, along with a general construction theorem and counterexample families on Banach spaces containing or admitting suitable c₀/ℓ¹ subspaces or quotients.[7]
- **Assumptions and setting:** Pairs of maximally monotone operators on Banach spaces satisfying the paper's interior-domain condition; the Banach-space transfer results have additional subspace/quotient hypotheses.[7]
- **Caveat:** This refutes the stated condition's sufficiency; it does not imply that every stronger sum theorem or constraint qualification fails.[7]
- **Announcement type:** revision, announcement-batch date 2026-09-24.[7]
- **Themes:** Analysis & PDE; Optimization & control.

### 7. [Sharp connectivity thresholds for mixed rigidity packings and improved bounds for highly connected orientations of graphs](https://arxiv.org/abs/2609.24463v1)
- **Abstract:** A unified connectivity theorem packs edge-disjoint rigid spanning subgraphs at a sharp threshold in the stated range and improves quadratic upper bounds for highly connected graph orientations.[8]
- **Authors:** Hanzhi Bai, Jørgen Bang-Jensen, Jin Yan.[8]
- **arXiv:** `2609.24463v1` (published 2026-09-21T12:06:44Z; categories: `math.CO`).[8]
- **Evidence for ranking:** The authors claim to settle two sharp packing conjectures, prove a general mixed-dimension theorem, and reduce the leading coefficient in a related orientation bound from 320 to 25/2 (and to 8 asymptotically).[8]
- **Claimed result:** Every graph with connectivity at least Σᵢdᵢ(dᵢ+1) contains pairwise edge-disjoint spanning dᵢ-rigid subgraphs; the bound is sharp when the sum is at least 4. The paper also gives the stated improved orientation bounds.[8]
- **Assumptions and setting:** Positive integers d₁,…,dₛ and finite graphs satisfying the specified vertex-connectivity threshold; sharpness is claimed when Σᵢdᵢ(dᵢ+1)≥4.[8]
- **Caveat:** Sharpness is not asserted in the abstract for the smaller-sum cases; the orientation statements are upper bounds, not a complete determination of the optimal function.[8]
- **Announcement type:** new submission, announcement-batch date 2026-09-21.[8]
- **Themes:** Combinatorics & discrete mathematics.

### 8. [A weak Hellinger inequality for noisy Boolean channels](https://arxiv.org/abs/2609.28534v2)
- **Abstract:** For the binary symmetric channel, the authors prove a weak Hellinger-conjecture form in which dictators maximize Hellinger Φ-entropy among Boolean inputs and one-bit noisy-output statistics.[9]
- **Authors:** Polona Durcik, Marco Fraccaroli, Joris Roos.[9]
- **arXiv:** `2609.28534v2` (published 2026-09-22T19:50:58Z; categories: `cs.IT`, `math.CO`).[9]
- **Evidence for ranking:** It is cross-listed in information theory and combinatorics, has a substantive v2 revision, and the paper reports computer-assisted positivity checks plus a Lean 4 formalization.[9]
- **Claimed result:** The authors prove the stated weak form using an explicit three-parameter inequality, polynomial approximations, and computer-assisted positivity checks; they report formal verification in Lean 4.[9]
- **Assumptions and setting:** The result is for the binary symmetric channel, Boolean input functions, and one-bit statistics of the noisy output.[9]
- **Caveat:** The result is explicitly a weak form for a restricted channel/statistic setting; it should not be described as settling the full Hellinger conjecture.[9]
- **Announcement type:** revision, announcement-batch date 2026-09-29.[9]
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics.

### 9. [Maker Breaker Games on a Budget](https://arxiv.org/abs/2609.38138v1)
- **Abstract:** In a budget-enabled version of the Maker–Breaker triangle game, the authors determine the exact threshold bias and give an asymptotic threshold when accumulated budget cannot be spent on threats.[10]
- **Authors:** Sebastian Lüderssen, Fabien Nießen, Silas Rathke.[10]
- **arXiv:** `2609.38138v1` (published 2026-09-29T17:55:08Z; categories: `math.CO`).[10]
- **Evidence for ranking:** The abstract identifies an exact threshold matching the known lower bound in the new budget variant and adds a threat-restricted asymptotic result; this is a concrete combinatorial advance in the latest batch.[10]
- **Claimed result:** In the budget version, the triangle-game threshold is exactly ⌈√(2n−2)−3/2⌉; without spending budget on threats it is (√2+o(1))√n. The paper also gives first explicit bounds for the K₄ game.[10]
- **Assumptions and setting:** Maker claims one edge per round in Kₙ and Breaker's bias is q; the exact formula applies to the newly defined budget game, with a distinct result for the threat-restricted rule.[10]
- **Caveat:** The exact threshold is for the budget variant; the original triangle-game threshold remains open in the abstract's stated context.[10]
- **Announcement type:** new submission, announcement-batch date 2026-09-29.[10]
- **Themes:** Combinatorics & discrete mathematics.

## Trending Research Themes

- **Extremal graph structure and exact thresholds:** The random-walk paper relates small spectral gaps to chain-like extremizers and stability; the rigidity-packing paper gives sharp connectivity thresholds; and the Maker–Breaker paper isolates how allowing a stored budget changes the threshold. These are distinct problems, but each makes extremal structure or threshold behavior explicit.[2][8][10]
- **Conjecture closure by classification or counterexample:** The restarted-CG paper finds a sharp restart-length boundary, while the quantum Hedetniemi and Rockafellar papers give counterexamples.[3][4][7]
- **Exact parameter boundaries:** The q-product paper separates true and false parameter intervals, while the elliptic-regularity paper identifies exact exponents in its stated ranges.[5][6]
- **Formal verification:** Lean formalization is reported for restarted CG, quantum graph coloring, and the weak Hellinger inequality.[3][4][9]
- **Certified computation:** The q-product work reports exact and ball-arithmetic checks for finite regimes. These are examples within this selection, not evidence of a field-wide shift.[6]

## Open Problems and Research Directions

- **Author-stated gap:** The original Maker–Breaker triangle-game threshold is not determined by the exact result for the budget variant; the paper gives the old-game bounds in its abstract. Determining the original threshold remains open there.[10]
- **Author-stated gap:** For the sharp Hessian-integrability problem in three dimensions, the abstract reports a remaining gap beyond ellipticity ratio κ=4. Closing or disproving sharpness of the proposed exponent in that regime is a direct follow-up.[5]
- **Author-stated boundary:** The Hellinger result covers a weak form for the binary symmetric channel and one-bit statistics. Testing which parts extend to stronger conjecture formulations or broader channel/statistic classes is a proposed research direction, not a claim made by the paper.[9]
- **Synthesis:** The regular-graph extremizer classification is stated for sufficiently large order, while the paper gives a separate all-n quartic uniqueness result. Identifying any remaining finite-order exceptions for the broader extremal problem would sharpen the boundary of the asymptotic classification.[2]
- **Synthesis:** The q-product sign results are exact for four named products, with certified computations in finite ranges. Applying the same cusp-amplitude/secondary-term analysis to other modular products could test how broadly that mechanism predicts sign changes.[6]

## Takeaway

This window's strongest mathematical signals are precise boundaries: a restart-length cutoff, explicit counterexamples to conjectured identities, optimal regularity exponents in specified dimensions, and sharp graph thresholds. The spread across probability, numerical analysis, PDE, functional analysis, and combinatorics makes this a useful set of notable papers, but the sparse attention data does not support calling it a measured popularity ranking.

## Method and sources

- **Window and snapshot:** Rolling 30-day request translated to an archive-date query covering 2026-08-31 through 2026-09-30; snapshot at 2026-09-30 10:43:14 UTC. The exact 30×24-hour cutoff is 2026-08-31 10:43:14 UTC, while the date-granularity archive query included all of 2026-08-31.[1]
- **Corpus:** Full arXiv API searches for `math.*` by submitted date and last-updated date were traversed and deduplicated by versionless ID. Each returned 8,897 unique records and the same ID set; no earlier first-submission IDs were added by the updated-date query. The latest returned announcement was 2026-09-29. The largest primary-category counts in the pool were math.CO (956), math.AP (952), math.NT (618), and math.OC (601); selection was not weighted by category volume.[1][11]
- **Selection and ranking:** Since arXiv has no official trending/readership chart and citation evidence was too sparse to rank papers by attention, these are “notable recent papers,” ordered by concrete claimed results, conjecture resolution/counterexamples, cross-subfield relevance, and revision/formalization signals—not by downloads or popularity. Semantic Scholar produced records for only 2 of 14 candidate lookups; both showed 0 current citations, so citation counts were not used to rank.[12][13]
- **Reading and verification:** arXiv abstracts and metadata were checked for all nine entries; the introductions/main-results statements were also inspected for the top three. The mathematical claims remain attributed preprint claims; no proof was independently verified here.
- **Primary corpus endpoint:** arXiv API date-filtered Mathematics archive search.[1]

## Sources

[1] https://export.arxiv.org/api/query?search_query=cat%3Amath.%2A%20AND%20submittedDate%3A%5B%32%30%32%36%30%38%33%31%30%30%30%30%20TO%20%32%30%32%36%30%39%33%30%32%33%35%39%5D&start=0&max_results=30000&sortBy=submittedDate&sortOrder=descending
[2] https://arxiv.org/abs/2609.06818v2
[3] https://arxiv.org/abs/2609.04659v2
[4] https://arxiv.org/abs/2609.20690v1
[5] https://arxiv.org/abs/2609.06817v1
[6] https://arxiv.org/abs/2609.22324v1
[7] https://arxiv.org/abs/2609.10487v4
[8] https://arxiv.org/abs/2609.24463v1
[9] https://arxiv.org/abs/2609.28534v2
[10] https://arxiv.org/abs/2609.38138v1
[11] https://export.arxiv.org/api/query?search_query=cat%3Amath.%2A%20AND%20lastUpdatedDate%3A%5B%32%30%32%36%30%38%33%31%30%30%30%30%20TO%20%32%30%32%36%30%39%33%30%32%33%35%39%5D&start=0&max_results=30000&sortBy=lastUpdatedDate&sortOrder=descending
[12] https://api.semanticscholar.org/graph/v1/paper/arXiv:2609.20690?fields=title%2CcitationCount%2CinfluentialCitationCount
[13] https://api.semanticscholar.org/graph/v1/paper/arXiv:2609.04659?fields=title%2CcitationCount%2CinfluentialCitationCount
