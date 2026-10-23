# arXiv Mathematics — weekly notable papers, 17–23 October 2026

Eight notable new submissions from the week. A recurring pattern is authors claiming resolutions of long-standing conjectures, especially in extremal combinatorics; a separate thread is mathematicians explaining AI-attributed proof claims. I’ll focus on what each paper actually asserts, its hypotheses, and the limits still visible from the sources. Global caveat: arXiv publishes no official trending chart, so this ordering is inferred; citation evidence is sparse for papers only days old.

## Top papers (ranked)

### 1. [Proof of the Erdős-Szemerédi sunflower conjecture](https://arxiv.org/abs/2610.26686)
- **Abstract:** The authors prove that for every fixed integer k ≥ 3, families of subsets of [n] containing no k-sunflower have size at most c_k^n for some c_k < 2.
- **Authors:** Matija Bucić, Fankang He, Hyunwoo Lee
- **arXiv:** `2610.26686v1` (published 2026-10-19 16:32:32 UTC; categories: `math.CO`)
- **Evidence for ranking:** Besides the explicit conjecture-resolution claim, the work has an announced IBS seminar by coauthor Hyunwoo Lee and a public Lean formalization linked to the paper; these are checkable independent engagement signals, not citation counts. [IBS seminar](https://dimag.ibs.re.kr/event/2026-10-28/) · [Lean formalization](https://github.com/mbucic4/erdos-szemeredi-sunflowers)
- **Claimed result:** The authors' main theorem gives an exponential upper bound with base strictly below 2 for every k ≥ 3; the paper develops a vector-sunflower bound and transfers it to set families.
- **Assumptions and setting:** Fixed k ≥ 3; a family is a subset of the power set of [n] and is assumed to contain no k sets whose pairwise intersections all coincide.
- **Caveat:** The paper notes that the best known lower construction remains close to the upper bound for large k, so the exponential base is not established as optimal.
- **Announcement type:** new submission, 2026-10-19
- **Themes:** Combinatorics & discrete mathematics

### 2. [On OpenAI's proof of the Nagata conjecture](https://arxiv.org/abs/2610.30050)
- **Abstract:** Jenia Tevelev's expository notes explain a claimed proof of Nagata's conjecture by reducing interpolation for fat points to a lattice-triangle problem, and also derive cones for certain weighted blow-ups.
- **Authors:** Jenia Tevelev
- **arXiv:** `2610.30050v1` (published 2026-10-21 17:10:57 UTC; categories: `math.AG`)
- **Evidence for ranking:** The preprint follows a UMass Amherst research talk on the same claim, and the university's event page independently documents that talk; the mathematical claim is high-profile, but this is attention to the claim rather than evidence that the proof has been independently certified. [UMass event](https://www.umass.edu/mathematics-statistics/events/jenia-tevelev-umass-what-nagata-conjecture-and-how-did-ai-prove-it-last-week)
- **Claimed result:** In the author's account of the OpenAI proof, for r ≥ 10 very general points of the complex projective plane, every nonzero degree-d curve vanishing to order at least m at all points satisfies d > m√r; the notes also determine nef and pseudoeffective cones for a stated class of weighted blow-ups.
- **Assumptions and setting:** The Nagata statement is over ℂ, for r ≥ 10 very general points in P² and integer multiplicity m ≥ 1; “very general” excludes a countable union of proper algebraic subsets.
- **Caveat:** These are explicitly expository notes, not the original proof; Tevelev says they are not a definitive account and claims no originality. The underlying proof claim has not been independently assessed here.
- **Announcement type:** new submission, 2026-10-21
- **Themes:** Geometry & topology

### 3. [A Solution to the Kohayakawa-Prömel-Rödl Conjecture](https://arxiv.org/abs/2610.27478)
- **Abstract:** The authors prove a polynomial upper bound for the induced Ramsey number r_ind(G,H), namely at most t^(60k²+3) when G and H have k and t vertices, respectively.
- **Authors:** Chuang Zhong, Masaki Kashima, Yaping Mao
- **arXiv:** `2610.27478v1` (published 2026-10-20 01:44:36 UTC; categories: `math.CO`)
- **Evidence for ranking:** The paper gives a concrete resolution of a 1998 conjecture with an explicit bound; Wolfram MathWorld independently added a reference describing the claimed polynomial bound and resolution. [Wolfram MathWorld](https://mathworld.wolfram.com/Kohayakawa-Promel-RodlConjecture.html)
- **Claimed result:** The authors state that for finite simple graphs G,H with k=|V(G)| ≥ 2 and t=|V(H)| ≥ 2, r_ind(G,H) ≤ t^(60k²+3), establishing the conjectured polynomial dependence on t for each fixed G.
- **Assumptions and setting:** The induced Ramsey number is the minimum order of a host graph in which every red/blue edge-colouring yields a red induced G or blue induced H; the theorem concerns arbitrary finite simple G,H in the stated size range.
- **Caveat:** The exponent is large and the paper does not claim it is sharp; substantially improving the dependence on k or the exponent remains open-ended.
- **Announcement type:** new submission, 2026-10-20
- **Themes:** Combinatorics & discrete mathematics

### 4. [On the proof of the Kozma-Nitzan conjecture](https://arxiv.org/abs/2610.30063)
- **Abstract:** Jean-Baptiste Gouéré's short note presents an exposition of a recent proof of the Kozma-Nitzan conjecture attributed to OpenAI.
- **Authors:** Jean-Baptiste Gouéré
- **arXiv:** `2610.30063v1` (published 2026-10-21 17:23:22 UTC; categories: `math.PR`)
- **Evidence for ranking:** The note addresses a widely discussed critical-percolation claim: independent discussion by Gil Kalai and a MathDB problem page describes the underlying result and its relation to the Kozma-Nitzan conjecture. This is topical attention to the underlying claim, not evidence of citations to this new note. [Gil Kalai's discussion](https://gilkalai.wordpress.com/2026/09/03/amazing-there-is-no-percolation-at-the-critical-probability-in-all-dimensions-solved-by-ai-via-a-conjecture-of-gady-kozma-and-shahaf-nitzan/) · [MathDB](https://mathdb.com/p/408931/kozma-nitzan-conjecture)
- **Claimed result:** The paper claims to explain the proof, not to establish a new theorem; the abstract identifies the proof as one provided by OpenAI.
- **Assumptions and setting:** The abstract does not restate the conjecture's precise hypotheses; it is an expository note on a separate proof concerning percolation.
- **Caveat:** This is a commentary/exposition rather than the primary proof, and the abstract alone does not specify the theorem statement or permit assessment of that proof.
- **Announcement type:** new submission, 2026-10-21
- **Themes:** Probability & statistics

### 5. [A proof of Ward's conjecture on Griesmer codes](https://arxiv.org/abs/2610.29275)
- **Abstract:** For a q-ary Griesmer code with q=p^f and e the p-adic valuation of its minimum distance, the authors claim divisibility by p^max(0,e−f+1), proving Ward's conjecture.
- **Authors:** Haihua Deng, Weiye Zhang
- **arXiv:** `2610.29275v1` (published 2026-10-21 06:26:54 UTC; categories: `math.CO` (primary), `cs.IT` (cross-list))
- **Evidence for ranking:** A precise proof claim resolves a stated conjecture and the paper is cross-listed between combinatorics and information theory; no independent discussion surfaced in the sources checked.
- **Claimed result:** The authors prove every [n,k,d]_q Griesmer code is p^max(0,e−f+1)-divisible when q=p^f and e=ν_p(d).
- **Assumptions and setting:** The code must attain the Griesmer bound, over a finite field of characteristic p; e is the p-adic valuation of its minimum distance d.
- **Caveat:** The divisibility theorem is specific to Griesmer codes and does not assert the same conclusion for arbitrary linear codes.
- **Announcement type:** new submission, 2026-10-21
- **Themes:** Combinatorics & discrete mathematics

### 6. [A proof of the Baranov--Bessonov--Kapustin conjecture](https://arxiv.org/abs/2610.26232)
- **Abstract:** The authors claim that for a nonconstant inner function θ, every bounded truncated Toeplitz operator on the model space K_θ has a bounded symbol exactly when θ is one-component.
- **Authors:** Carlo Bellavita, Jani A. Virtanen
- **arXiv:** `2610.26232v1` (published 2026-10-19 11:59:41 UTC; categories: `math.FA` (primary), `math.CV` (cross-list))
- **Evidence for ranking:** The paper claims a resolution of a conjecture formulated in operator theory, with cross-listing in functional analysis and complex variables; MathDB's conjecture entry documents the historical open direction. [MathDB](https://mathdb.com/p/408811/baranov-bessonov-kapustin-conjecture)
- **Claimed result:** The authors state the conjectured if-and-only-if characterization of when all bounded truncated Toeplitz operators on K_θ admit bounded symbols.
- **Assumptions and setting:** θ is a nonconstant inner function; K_θ is its associated model space, and the operators are bounded truncated Toeplitz operators.
- **Caveat:** The abstract gives an existence criterion for bounded symbols, not a quantitative norm-control estimate.
- **Announcement type:** new submission, 2026-10-19
- **Themes:** Analysis & PDE

### 7. [Sharp Bounds for Nodal Sets of Steklov Eigenfunctions on Smooth Surfaces](https://arxiv.org/abs/2610.28391)
- **Abstract:** The authors prove sharp linear upper bounds for Steklov nodal lengths and counts on smooth compact surfaces with boundary, while showing that interior nodal length can grow beyond log λ arbitrarily slowly.
- **Authors:** Guiyu Xie, Cheng Zhang
- **arXiv:** `2610.28391v1` (published 2026-10-20 15:40:07 UTC; categories: `math.AP` (primary), `math.CA`, `math.DG`, `math.SP` (cross-lists))
- **Evidence for ranking:** Four-way mathematical cross-listing and a sharp upper bound tied to the two-dimensional Steklov analogue of Yau's conjecture make this a strong cross-field result; independent attention signals were not found in the sources checked.
- **Claimed result:** The authors establish a sharp linear upper bound on interior nodal length and sharp linear bounds on boundary zeros and nodal-domain counts; they also show the interior nodal length divided by log λ tends to infinity, with examples permitting arbitrarily slow divergence.
- **Assumptions and setting:** Steklov eigenfunctions on a fixed smooth compact Riemannian surface with boundary; the asymptotic statements concern large eigenvalues.
- **Caveat:** The lower-growth conclusion is only ω(log λ), and the examples rule out a universal positive-power lower bound; stronger lower rates require extra hypotheses.
- **Announcement type:** new submission, 2026-10-20
- **Themes:** Analysis & PDE; Geometry & topology

### 8. [Sprinkling for random regular graphs and Kim-Vu's sandwich conjecture](https://arxiv.org/abs/2610.28395)
- **Abstract:** For even n and diverging degree d ≤ n^(1/10), the author proves that a uniform random d-regular graph is asymptotically close in total variation to a union of d uniformly random edge-disjoint perfect matchings, yielding two conjecture-related consequences.
- **Authors:** Julien Portier
- **arXiv:** `2610.28395v1` (published 2026-10-20 15:41:44 UTC; categories: `math.CO`)
- **Evidence for ranking:** The single theorem yields implications for sprinkling in random regular graphs and the sparse-regime upper side of Kim-Vu's sandwich conjecture; this is a concrete multi-consequence result, though no independent attention signal was found in the sources checked.
- **Claimed result:** The author proves the total-variation approximation in the stated degree range, confirming the cited random-regular-graph conjecture there, and derives the stated sprinkling and sparse-regime sandwich consequences.
- **Assumptions and setting:** Uniform simple d-regular graphs on even n vertices; d=ω(1) and d≤n^(1/10).
- **Caveat:** The theorem is restricted to this sparse degree window and does not address bounded d or degrees above n^(1/10).
- **Announcement type:** new submission, 2026-10-20
- **Themes:** Probability & statistics; Combinatorics & discrete mathematics

## Trending Research Themes

- **Conjecture resolutions in extremal combinatorics:** The sunflower bound and the induced Ramsey bound both turn structural avoidance conditions into global exponential or polynomial size controls, but use different arguments; the papers do not establish a shared method. [Sunflower](https://arxiv.org/abs/2610.26686) · [Induced Ramsey](https://arxiv.org/abs/2610.27478)
- **AI-attributed proof claims are prompting expository work:** Tevelev's Nagata notes and Gouéré's Kozma-Nitzan note document two distinct proof claims; these are not themselves independent validation of the original proof manuscripts. [Nagata notes](https://arxiv.org/abs/2610.30050) · [Kozma-Nitzan note](https://arxiv.org/abs/2610.30063)
- **Sharp bounds with carefully described boundary behavior:** The Steklov paper pairs an optimal linear upper bound with a lower-growth obstruction; Portier's random-regular-graph approximation likewise states a precise sparse parameter range. These are isolated examples, not evidence of a field-wide shift. [Steklov](https://arxiv.org/abs/2610.28391) · [Random regular graphs](https://arxiv.org/abs/2610.28395)
- **Cross-subfield bridges:** Coding theory links combinatorics and information theory in Ward's conjecture; truncated Toeplitz operators bridge functional analysis and complex variables in the Baranov-Bessonov-Kapustin result. [Ward](https://arxiv.org/abs/2610.29275) · [Baranov--Bessonov--Kapustin](https://arxiv.org/abs/2610.26232)

## Open Problems and Research Directions

- **Open problem — author-stated:** The sunflower paper records a remaining gap between its upper bound and known lower constructions, especially for large k. A concrete direction is to improve either side and compare the bases as k varies. [2610.26686](https://arxiv.org/abs/2610.26686)
- **Research direction — synthesis:** The induced Ramsey theorem proves polynomial dependence but gives exponent 60k²+3. Seek sharper dependence on k, or constructions showing which part of that exponent is necessary. [2610.27478](https://arxiv.org/abs/2610.27478)
- **Open problem — author-reported limitation:** The Steklov examples permit arbitrarily slow divergence above log λ, while excluding every universal positive-power lower bound. Characterizing which divergence rates can occur, and what geometric assumptions force stronger growth, is a natural next test. [2610.28391](https://arxiv.org/abs/2610.28391)
- **Research direction — synthesis:** Portier's total-variation approximation is proved only for d=ω(1) up to n^(1/10); investigate whether related couplings or sprinkling conclusions persist at higher degrees or near the sparse boundary. [2610.28395](https://arxiv.org/abs/2610.28395)
- **Research direction — synthesis, not a claim that the result is open:** Independent line-by-line checking or formalization of the original arguments would make the Nagata and Kozma-Nitzan proof claims easier for specialists to assess; the selected papers are expositions, not independent proof certification. [2610.30050](https://arxiv.org/abs/2610.30050) · [2610.30063](https://arxiv.org/abs/2610.30063)

## Takeaway

This week’s most conspicuous pattern is a cluster of claimed conjecture resolutions, alongside highly specific sharp bounds and parameter-limited results. The selection is useful for tracking claims and techniques, but the evidence supports “notable recent papers,” not a measured popularity ranking or a verdict on the AI-attributed proofs.

## Method and sources

- **Window:** weekly, 2026-10-17 through 2026-10-23 inclusive (UTC). Snapshot: 2026-10-23 01:14:35 UTC. The latest available Mathematics announcement batch was Thu 2026-10-22; no Oct 23 batch was shown at snapshot time. Available full new-submission batches in the window were Oct 19–22; the recent Mathematics listing showed 359, 777, 437, and 382 entries respectively (1,955 total). Weekend dates Oct 17–18 had no separate batch in the listing.
- **Coverage:** arXiv Mathematics archive and its math.* subfields, retaining each paper's specific arXiv primary and cross-list categories. Eight v1 papers were selected; each abstract page was checked. For the top three, the arXiv HTML text was also inspected for introductions and main-result statements. No proof was independently verified.
- **Inference:** arXiv provides no official trending or readership ranking. The ordering prioritizes corroborated independent discussion where found, then concrete potentially significant claims and cross-subfield relevance, with recency as a tie-breaker. Semantic Scholar citation totals could not be retrieved at snapshot time, so they were not used as period gains or ranking inputs.
- **Revision coverage limitation:** the current arXiv `new` page showed Oct 22 new submissions, cross-lists, and replacements, but historical replacement listings for the earlier dates were not accessible during this check. Thus this is a notable selection from verified new submissions, not a complete accounting of revision-only papers in the full weekly window.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent), [arXiv Mathematics new listings](https://arxiv.org/list/math/new), each linked arXiv abstract/HTML page above, and the independent event, problem, and formalization references linked in individual entries.
