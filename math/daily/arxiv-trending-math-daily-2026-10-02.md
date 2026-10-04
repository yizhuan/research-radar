# arXiv Mathematics — Friday, 2 October 2026

Six notable papers from the latest Math listing, with a notable cluster in spin-glass probability and further results in metric geometry, reinforced walks, and graph theory. I’ll focus on what each claims, the hypotheses that matter, and what remains open. This is an inferred ordering, not an arXiv popularity chart: arXiv publishes no official trending ranking, and Semantic Scholar currently indexes zero citations for all six, so popularity evidence is especially thin.[1][8]

Window: daily; latest Math announcement listing dated 2 October 2026.
Snapshot: 2026-10-04 00:12:27 UTC.
These records appear under the Math page’s “New submissions” section for 2 October.[1]
Their individual histories instead report first-posted dates before that batch: 9 July, 9 September, and 19 September for the first three records.[2][3][4]
The remaining histories report dates from 7–10 September.[5][6][7]
I preserve each record’s history date rather than presenting these as papers first submitted on 2 October.[1][2][3]

## Top papers (ranked)

### 1. [Parisi measure of the Sherrington-Kirkpatrick model with external field](https://arxiv.org/abs/2610.00127)
- **Abstract:** The author proves that the Parisi measure has connected support for every positive temperature and positive external field; in the replica-symmetry-breaking regime, its interior has a smooth, strictly positive density and its endpoints carry atoms.[2]
- **Authors:** Patrick Lopatto[2]
- **arXiv:** `2610.00127v1` (published 2026-09-09 17:37:09 UTC; categories: `math.PR`)[2]
- **Evidence for ranking:** Concrete structural theorem about the support of the central order parameter in the SK model; the paper is in the broad probability corpus. Semantic Scholar reports 0 citations and 0 influential citations at this snapshot, so this placement reflects mathematical scope and the claimed result, not observed citation momentum.[2][8]
- **Claimed result:** The author states that support gaps are excluded and that the density is strictly positive up to both endpoints; the same estimates recover the zero-field support description and bound the upper atom’s mass.[2]
- **Assumptions and setting:** Sherrington-Kirkpatrick model at positive temperature and positive external field. The interval-and-density description is specified for replica-symmetry breaking; endpoints carry atoms.[2]
- **Caveat:** This is an author-claimed preprint result, not an independently assessed proof; the stated positive-field theorem does not itself cover zero temperature.[2]
- **Announcement type:** New submission (v1 in the Math “New submissions” section for 2 October; arXiv history says first posted 9 September 2026)[1][2]
- **Themes:** Probability & statistics; Mathematical physics[2]

### 2. [Critical Free-Energy Variance in the Sherrington-Kirkpatrick Model](https://arxiv.org/abs/2610.00011)
- **Abstract:** The author derives an exact finite-size variance identity for normalized SK free energy at criticality and relates its leading variance to the logarithm of the spin-glass susceptibility.[3]
- **Authors:** Miguel Tierz[3]
- **arXiv:** `2610.00011v1` (published 2026-07-09 17:33:48 UTC; categories: `math.PR`, `cond-mat.dis-nn`)[3]
- **Evidence for ranking:** A sharp critical-regime identity with a cross-list into disordered systems/neural networks, plus a direct connection to overlap-susceptibility scaling. Semantic Scholar reports 0 citations and 0 influential citations at the snapshot; this is therefore a significance-led, not attention-measured, placement.[3][8]
- **Claimed result:** The author claims `Var F_N(1) = (1/(2N²)) log χ_SG(N) + O(N⁻²)`. Combining this with the cited critical scaling `χ_SG(N) ≍ N^(1/3)` gives the coefficient `1/6` for `(log N)/N²`; the paper attributes that scaling result to Du and Huang.[3]
- **Assumptions and setting:** The equality is for the normalized free energy of the SK model at `(β,h)=(1,0)`; the `1/6` coefficient depends on the cited critical susceptibility scaling. The paper also treats fixed `β<1`.[3]
- **Caveat:** The sharp numerical coefficient is conditional on the cited susceptibility-scaling theorem; the paper’s identity is the author’s own preprint claim and should not be mistaken for independent verification of that input.[3]
- **Announcement type:** New submission (v1 in the Math “New submissions” section for 2 October; arXiv history says first posted 9 July 2026)[1][3]
- **Themes:** Probability & statistics; Mathematical physics[3]

### 3. [A question of Ulam and a theorem of de Rham](https://arxiv.org/abs/2610.00200)
- **Abstract:** The author extends de Rham-style factorization to proper metric spaces, proving a unique decomposition into a Euclidean factor and a finite or countable pointed ℓ²-product of irreducible non-Euclidean factors.[4]
- **Authors:** Alexander Lytchak[4]
- **arXiv:** `2610.00200v1` (published 2026-09-19 13:06:10 UTC; categories: `math.MG`, `math.DG`)[4]
- **Evidence for ranking:** The claimed theorem crosses metric and differential geometry and removes geodesicity, curvature, and dimension restrictions in the proper-space result, according to the paper’s introduction. Semantic Scholar reports 0 citations and 0 influential citations; ranking is based on theorem scope and cross-listing, not measured readership.[4][8]
- **Claimed result:** The author proves existence and uniqueness of the stated decomposition for proper metric spaces and a broader canonical splitting for complete metric spaces; the paper says this partially answers a question of Ulam.[4]
- **Assumptions and setting:** The unique irreducible-factor decomposition is for proper metric spaces. In the complete-space statement, a Hilbert factor, irreducible factors, and a residual factor with no nontrivial irreducible factors are distinguished.[4]
- **Caveat:** The complete-space result is not an unconditional decomposition into irreducibles alone: the residual factor may have no nontrivial irreducible factors.[4]
- **Announcement type:** New submission (v1 in the Math “New submissions” section for 2 October; arXiv history says first posted 19 September 2026)[1][4]
- **Themes:** Geometry & topology[4]

### 4. [Once-reinforced random walk on ℤᵈ has range exponent at least d/(d+1)](https://arxiv.org/abs/2610.00090)
- **Abstract:** For once-reinforced random walk on ℤᵈ, the authors prove that the expected range after `n` steps is at least of order `n^(d/(d+1))` for every `d≥2` and every reinforcement parameter `β≥1`.[5]
- **Authors:** Ahmed Bou-Rabee, Yuval Peres[5]
- **arXiv:** `2610.00090v1` (published 2026-09-07 16:29:50 UTC; categories: `math.PR`)[5]
- **Evidence for ranking:** The theorem establishes a predicted exponent lower bound across every dimension `d≥2` and all allowed reinforcement parameters, rather than only sufficiently strong reinforcement. The abstract also points to a Lean 4 formalization. Semantic Scholar reports 0 citations and 0 influential citations, so neither citation momentum nor popularity is established.[5][8]
- **Claimed result:** The authors prove the lower bound corresponding to the predicted `n^(d/(d+1))` scale for the expected range.[5]
- **Assumptions and setting:** Each edge starts with weight one and receives weight `β≥1` after its first crossing; each step chooses an incident edge proportional to its current weight. The result is for `ℤᵈ`, `d≥2`.[5]
- **Caveat:** The abstract supplies a lower bound, not a matching upper bound or a proof of the full predicted asymptotic order.[5]
- **Announcement type:** New submission (v1 in the Math “New submissions” section for 2 October; arXiv history says first posted 7 September 2026)[1][5]
- **Themes:** Probability & statistics[5]

### 5. [A counterexample to Yau's bounded-mean-curvature embedding question](https://arxiv.org/abs/2610.00153)
- **Abstract:** The author constructs complete metrics on ℝ⁴, and in every dimension at least four, with bounded Ricci curvature and positive injectivity radius but unbounded full curvature, forcing every finite-dimensional Euclidean C² isometric immersion to have unbounded mean curvature.[6]
- **Authors:** Haoxuan Cheng[6]
- **arXiv:** `2610.00153v1` (published 2026-09-10 16:13:51 UTC; categories: `math.DG`)[6]
- **Evidence for ranking:** A direct counterexample to a clearly stated embedding question, with a dimension extension; the differential-geometric result is a strong concrete claim. Semantic Scholar reports 0 citations and 0 influential citations at the snapshot, so its inclusion is result-led rather than evidence of current attention.[6][8]
- **Claimed result:** The author claims that the constructed metric rules out bounded-mean-curvature isometric immersion into any finite-dimensional Euclidean space, using the Gauss equation.[6]
- **Assumptions and setting:** The counterexample uses a smooth complete metric with bounded Ricci curvature and positive injectivity radius; the construction works in dimensions `n≥4`. The paper notes that in dimension four Ricci curvature can tend to zero at infinity.[6]
- **Caveat:** It disproves the universal assertion in dimensions four and higher; it does not settle the analogous question in dimensions below four.[6]
- **Announcement type:** New submission (v1 in the Math “New submissions” section for 2 October; arXiv history says first posted 10 September 2026)[1][6]
- **Themes:** Geometry & topology[6]

### 6. [A Counterexample to Wormald's Conjecture](https://arxiv.org/abs/2610.00086)
- **Abstract:** The author gives a 16-vertex cubic-graph counterexample to Wormald's conjecture, extends it to orders `16+4t`, and reports a Lean formalization without custom axioms.[7]
- **Authors:** James Alexander Schreib[7]
- **arXiv:** `2610.00086v1` (published 2026-09-07 02:53:28 UTC; categories: `math.CO`)[7]
- **Evidence for ranking:** A crisp counterexample with a mechanically formalized proof claim; it is a notable combinatorics result, though the source set checked supplies no measured attention signal. Semantic Scholar reports 0 citations and 0 influential citations at the snapshot.[7][8]
- **Claimed result:** The author constructs a cubic graph with no partition of its edges into two isomorphic spanning linear forests, and obtains counterexamples at every order `16+4t` by adjoining copies of `K₄`.[7]
- **Assumptions and setting:** The stated graph is disconnected: it is the disjoint union of `K₃,₃` and a 10-vertex bridged graph assembled from two subdivided copies of `K₄`.[7]
- **Caveat:** The author explicitly leaves the connected case unresolved; the Lean formalization is reported by the author and was not independently audited here.[7]
- **Announcement type:** New submission (v1 in the Math “New submissions” section for 2 October; arXiv history says first posted 7 September 2026)[1][7]
- **Themes:** Combinatorics & discrete mathematics[7]

## Trending Research Themes

- **Spin-glass structure and fluctuations:** Two selected probability papers study complementary SK questions: one the support geometry of the Parisi order parameter, the other critical finite-size free-energy fluctuations. They share a model, but not a demonstrated common proof technique; the selected set is too small to imply a field-wide trend.[2][3]
- **Geometric structure and obstructions:** The metric-space paper gives a positive factorization theorem under properness, while the embedding paper constructs a counterexample under bounded-Ricci and injectivity-radius assumptions. These are distinct geometric directions, not evidence of one shared trend.[4][6]
- **Sharp probabilistic bounds and formal proof:** The reinforced-walk paper proves a lower bound at a conjectured exponent, while the graph paper uses a parity obstruction and reports Lean verification. Both state a concrete boundary of current knowledge, but concern different objects.[5][7]

## Open Problems and Research Directions

- **Connected Wormald case — author-stated open problem:** The counterexample family is disconnected; the author says the connected case remains unresolved. A direct follow-up is to determine whether a connected cubic counterexample exists or whether connectedness forces such a partition.[7]
- **Matching range asymptotics — synthesis from the stated result:** The reinforced-walk paper proves only the lower bound at exponent `d/(d+1)`. Establishing a matching upper bound, or finding parameter/dimension regimes with a different exponent, would test the predicted order.[5]
- **Factorization beyond proper spaces — synthesis from scope:** The strongest uniqueness theorem is for proper metric spaces, while complete spaces can retain a residual factor without irreducible factors. Characterizing broader classes where that residual disappears, or where factor uniqueness still holds, would extend the reported decomposition results.[4]
- **Boundary dimensions for the embedding question — synthesis from scope:** The counterexample settles the universal claim in dimensions at least four. The corresponding low-dimensional cases remain outside this construction and are a natural test of how much the dimension threshold matters.[6]

## Takeaway

The most substantial signals in this batch are two technically different advances on the SK model, alongside a broad metric-space decomposition theorem and several sharp counterexamples or lower bounds. The ranking is necessarily provisional: the evidence supports mathematical interest, not demonstrated popularity, and the listing/history date mismatch means these should not all be read as first submitted on 2 October.

## Method and sources

Window: daily; arXiv Math latest listing for Friday 2 October 2026, inspected at 2026-10-04 00:12:27 UTC.
The `math/new` page showed 787 total entries, including 438 in its “New submissions” section; the six entries above were selected from that section.[1]
Abstracts, authors, categories, and versions were checked on the individual arXiv pages for the first three entries.[2][3][4]
The same metadata was checked for the remaining three.[5][6][7]
The individual histories show dates earlier than 2 October.[2][3][4]
The remaining records also have earlier dates.[5][6][7]
This report preserves those dates and treats 2 October only as the Math listing batch date.[1][2][3]

Ranking is an informed notable-paper selection, not a popularity chart. It favors concrete theorem/counterexample claims and, secondarily, cross-category relevance; recency was not used to imply attention. A Semantic Scholar Graph batch lookup on the snapshot date returned 0 citation and 0 influential-citation counts for all six. These are current totals, not gains during the selected window.[8]

## Sources

[1] https://arxiv.org/list/math/new
[2] https://arxiv.org/abs/2610.00127
[3] https://arxiv.org/abs/2610.00011
[4] https://arxiv.org/abs/2610.00200
[5] https://arxiv.org/abs/2610.00090
[6] https://arxiv.org/abs/2610.00153
[7] https://arxiv.org/abs/2610.00086
[8] https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,citationCount,influentialCitationCount,referenceCount,fieldsOfStudy,externalIds
