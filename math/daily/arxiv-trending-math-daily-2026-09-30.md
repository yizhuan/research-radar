# arXiv Mathematics — notable papers in the 30 September 2026 batch

## Headline

The latest batch available at the 1 October 2026 snapshot is the 30 September announcement batch: 480 entries, of which 419 carried at least one `math.*` subject tag. The selected papers feature a negative resolution of both parts of Erdős Problem #786, near-linear paths in vertex-transitive graphs, and exact asymptotics in sparse hypergraph Turán theory. Agenda: start with those three combinatorics results, then look at two number-theory conjecture advances and a sharper Latin-square completion bound. This is an inferred shortlist, not a popularity chart: arXiv has no official trending ranking, and same-day citation/attention evidence is too sparse to measure what is actually hottest.[1]

## Top papers (ranked)

### 1. [A negative answer to Erdős Problem #786](https://arxiv.org/abs/2609.37471)
- **Abstract:** Shows that admissible subsets of `[1,N]` cannot have density arbitrarily close to one, and gives a logarithmic reciprocal-sum bound, answering both distinct-product questions negatively.[2]
- **Authors:** Shisheng Li
- **arXiv:** `2609.37471v1` (published 2026-09-28 08:15:28 UTC; categories: `math.NT`)[2]
- **Evidence for ranking:** The paper closes two explicitly stated open questions and gives both a reciprocal-sum theorem and a positive density deficit; its introduction states the main bounds and relates them to the prior `7/8` density result.[2]
- **Claimed result:** The author proves `Σ(1/a) ≤ (1/2) log N + (log log N + 2)^2` for every admissible `A ⊆ [1,N]`, and proves `|A| < (1−η)N` for all sufficiently large `N`, for an absolute `η>0`. The paper also reports Lean 4 formal verification against the Formal Conjectures statements.[2]
- **Assumptions and setting:** “Admissible” means that any equality between products of distinct elements of `A` has equally many factors on both sides; the cardinality result is asymptotic in `N`.[2]
- **Caveat:** The explicit density deficit is extremely small (`η=e^-5000` is one allowed value); the paper does not determine the optimal deficit, which its introduction conjecturally relates to `0.1715…`.[2]
- **Announcement type:** new submission, 2026-09-30 announcement batch (v1 submitted 2026-09-28)
- **Themes:** Algebra & number theory

### 2. [A nearly linear bound for the Lovász conjecture](https://arxiv.org/abs/2609.38135)
- **Abstract:** Improves the known guaranteed cycle length in an `n`-vertex connected vertex-transitive graph from `n^(2/3−o(1))` to `n^(1−o(1))`.[3]
- **Authors:** Bowen Li, Abhishek Methuku
- **arXiv:** `2609.38135v1` (published 2026-09-29 17:54:33 UTC; categories: `math.CO`)[3]
- **Evidence for ranking:** The abstract identifies a substantial exponent improvement on a well-known Hamiltonicity problem and gives a concrete proof architecture (structural partition, random path joining, and nilpotent Cayley-graph reduction). The Semantic Scholar record checked at snapshot listed 0 citations, so that metric supplies no positive momentum signal.[3][9]
- **Claimed result:** The authors prove that every connected vertex-transitive graph on `n` vertices contains a cycle of length `n^(1−o(1))`; the paper’s abstract contrasts this with the previous `n^(2/3−o(1))` bound.[3]
- **Assumptions and setting:** Finite, undirected, connected vertex-transitive graphs; the bound is asymptotic and is not a Hamiltonicity theorem.[3]
- **Caveat:** The result still falls short of a Hamiltonian path or cycle through all vertices, so Lovász’s original conjecture remains unresolved.[3]
- **Announcement type:** new submission, 2026-09-30 announcement batch (v1 submitted 2026-09-29)
- **Themes:** Combinatorics & discrete mathematics

### 3. [Asymptotics of the Brown–Erdős–Sós problem at integer exponents](https://arxiv.org/abs/2609.38115)
- **Abstract:** Determines the leading asymptotic coefficient for a broad integer-exponent family in sparse hypergraph Turán theory, with one even-parameter family left open.[4]
- **Authors:** Ting-Wei Chao, Xinqi Huang, Hong Liu
- **arXiv:** `2609.38115v1` (published 2026-09-29 17:50:05 UTC; categories: `math.CO`)[4]
- **Evidence for ranking:** The authors give explicit constants for general `r>t≥2` and nearly all `k`, resolving a leading-coefficient question beyond the previously known exponent order `Θ(n^t)`; they also derive consequences for generalized Ramsey cases.[4]
- **Claimed result:** For `f^(r)(n;(r−t)k+t,k)`, the authors establish the limit coefficient for every `r>t≥2`, except `(r,t)=(3,2)` with even `k≥4`. For odd `k` it is `2/[t!(2·binom(r,t)−1)]`; for even `k` and `r≥4` it is `1/[t!·binom(r,t)]`. In the excluded family they prove the coefficient exceeds `1/6`.[4]
- **Assumptions and setting:** Fixed integers `r,k≥2`, `r>t≥2`, in the extremal problem for `r`-uniform hypergraphs avoiding `k` edges spanning at most `(r−t)k+t` vertices.[4]
- **Caveat:** The exact coefficient remains unresolved when `(r,t)=(3,2)` and `k≥4` is even; the paper only supplies a strict lower bound there.[4]
- **Announcement type:** new submission, 2026-09-30 announcement batch (v1 submitted 2026-09-29)
- **Themes:** Combinatorics & discrete mathematics

### 4. [Proof of Fishburn’s latent-subset conjecture](https://arxiv.org/abs/2609.35920)
- **Abstract:** Proves Fishburn’s conjecture that every dual intersecting family has an index whose latent-subset family is at least as large as its corresponding star.[5]
- **Authors:** Yuxian Dong, Jianxi Mao
- **arXiv:** `2609.35920v1` (published 2026-09-28 10:58:05 UTC; categories: `math.CO`)[5]
- **Evidence for ranking:** A direct resolution of a conjecture proposed in 1987; the abstract identifies the recent weighted star inequality of Chang, Liu, and Liu as the proof’s key input.[5]
- **Claimed result:** The authors prove that for every dual intersecting `F ⊆ 2^[n]`, some `i∈[n]` satisfies `|F^L(i)| ≥ |F(i)|`.[5]
- **Assumptions and setting:** The statement is for dual intersecting set families; `F^L` is the family of subsets of members of `F` that are not themselves in `F`.[5]
- **Caveat:** The proof depends on the weighted star inequality named by the authors; this summary has not independently checked that argument or its use.[5]
- **Announcement type:** new submission, 2026-09-30 announcement batch (v1 submitted 2026-09-28)
- **Themes:** Combinatorics & discrete mathematics

### 5. [Smyth’s Conjecture on the Mahler Measure of non-reciprocal trinomials of height 1](https://arxiv.org/abs/2609.37886)
- **Abstract:** Establishes Smyth’s conjectural threshold for Mahler measures of non-reciprocal trinomials of height 1 around `ρ=M(x+y+1)=1.381356…`.[6]
- **Authors:** Paul M Voutier
- **arXiv:** `2609.37886v1` (published 2026-09-29 15:55:24 UTC; categories: `math.NT`)[6]
- **Evidence for ranking:** The author claims a precise classification relative to the proposed smallest limit point `ρ`; the checked Semantic Scholar record listed 0 citations, so ranking rests on the stated result rather than citation momentum.[6][10]
- **Claimed result:** The author determines exactly when the Mahler measure of a non-reciprocal height-1 trinomial is above or below `ρ`.[6]
- **Assumptions and setting:** Non-reciprocal trinomials of height 1; the paper’s abstract does not extend the proved classification beyond that family.[6]
- **Caveat:** The abstract says the result conjecturally gives the full spectrum below `ρ` for all non-reciprocal polynomials; that broader conclusion remains conjectural, not proved here.[6]
- **Announcement type:** new submission, 2026-09-30 announcement batch (v1 submitted 2026-09-29)
- **Themes:** Algebra & number theory

### 6. [An infinite family of counterexamples to Goss’s conjecture on L-functions of cyclotomic function fields](https://arxiv.org/abs/2609.37466)
- **Abstract:** Constructs infinitely many counterexamples to Goss’s degree bound, with counterexample degrees growing as large as `p−2`.[7]
- **Authors:** David Niedbala Giraudin
- **arXiv:** `2609.37466v1` (published 2026-09-26 13:04:50 UTC; categories: `math.NT`)[7]
- **Evidence for ranking:** The abstract does more than give an isolated exception: it supplies a family indexed by a prime and a parameter, and states that the violation is unbounded as the prime grows.[7]
- **Claimed result:** For `q=p`, `A=F_p[T]`, and `P_a=T^p−T−a` with `a∈F_p*`, the author proves an exact congruence yielding `deg_X g(X,ω_P^i)=n−1` for `i=p^n−1`; for `p≥5` and `3≤n≤p−1`, this contradicts Goss’s conjectured bound, reaching degree `p−2`.[7]
- **Assumptions and setting:** Cyclotomic function fields over `F_p(T)` with prime field size `q=p`; the construction uses the specified irreducible polynomials and q-magic indices.[7]
- **Caveat:** The counterexamples are in the stated prime-field setting and do not, by themselves, settle analogous formulations for general prime powers `q`.[7]
- **Announcement type:** new submission, 2026-09-30 announcement batch (v1 submitted 2026-09-26)
- **Themes:** Algebra & number theory

### 7. [Improved bounds on completion of partial Latin squares](https://arxiv.org/abs/2609.37877)
- **Abstract:** Raises the guaranteed completion threshold for partial Latin squares from a previous `0.08n` bound to `0.231n` filled cells per row, column, and symbol.[8]
- **Authors:** Jack Allsop, Candida Bowtell, Thomas Lesgourgues, Kalina Petrova
- **arXiv:** `2609.37877v1` (published 2026-09-29 15:51:48 UTC; categories: `math.CO`)[8]
- **Evidence for ranking:** A clear quantitative improvement on a named completion conjecture, with the abstract identifying a discharging argument adapted to the partite setting as the new ingredient.[8]
- **Claimed result:** The authors prove that a partial Latin square of order `n` can be completed when each row, column, and symbol occurs at most `0.231n` times.[8]
- **Assumptions and setting:** The partial Latin square uses at most `n` symbols and has at most `0.231n` filled cells of each symbol in each row and column; the result is a sufficient condition, not a characterization.[8]
- **Caveat:** The `n/4` Daykin–Häggkvist conjectured threshold remains out of reach; `0.231n` is the proven sufficient bound reported in the abstract.[8]
- **Announcement type:** new submission, 2026-09-30 announcement batch (v1 submitted 2026-09-29)
- **Themes:** Combinatorics & discrete mathematics

## Trending Research Themes

- **Combinatorial extremal bounds and completion thresholds:** the Brown–Erdős–Sós paper determines asymptotic constants, while the Latin-square paper pushes a completion threshold closer to its conjectured `n/4` limit.[4][8]
- **Conjecture resolution and counterexamples:** Fishburn’s conjecture is proved, while the number-theory papers answer Erdős Problem #786 negatively and construct counterexamples to Goss’s conjecture; these are distinct results, not evidence of a shared technique.[2][5][7]
- **Graph symmetry and long structures:** the Lovász-related paper improves the guaranteed cycle length in connected vertex-transitive graphs, but does not establish Hamiltonicity.[3]
- **Batch composition:** among 419 entries with a `math.*` subject tag, `math.CO` was the most frequent tag (63), followed by `math.OC` (59) and `math.AP` (51). Tags can overlap, so these are non-exclusive counts, not a partition or an attention measure.[1]

## Open Problems and Research Directions

- **Erdős #786 — author-stated direction:** the introduction suggests that the optimal density deficit may be about `0.1715…`; sharpening the explicit `η` bound toward that scale would test this conjectural picture.[2]
- **Lovász — open problem:** the original Hamiltonian-path conjecture remains open. A natural next step is to improve the `n^(1−o(1))` guarantee or identify additional structure that forces a spanning path.[3]
- **Brown–Erdős–Sós — open case:** determine the asymptotic coefficient for `(r,t)=(3,2)` and even `k≥4`, where the paper only proves it exceeds `1/6`.[4]
- **Smyth — author-qualified extension:** the abstract says the height-1 trinomial result may describe the full sub-`ρ` spectrum for all non-reciprocal polynomials; testing higher-term or higher-height families would probe that conjectural extension.[6]
- **Goss — scope extension:** the paper’s counterexamples use `q=p`; investigate whether comparable degree violations occur over `F_q` for non-prime prime powers.[7]
- **Latin squares — open threshold:** improve the `0.231n` sufficient condition toward the Daykin–Häggkvist `n/4` conjecture, or determine whether a larger threshold fails.[8]

## Takeaway

The most compelling mathematical signals in this batch are concrete improvements or resolutions: an explicit negative answer to both parts of Erdős #786, a near-linear cycle bound for vertex-transitive graphs, and broad asymptotic constants for sparse hypergraphs. Treat this as a guide to notable new claims, not a measured popularity ranking; the items are preprints and their proofs have not been independently assessed here.

## Method and sources

- **Window:** daily; latest arXiv Mathematics announcement batch available at the snapshot was 2026-09-30. This is the prior-day batch relative to the 2026-10-01 snapshot; no 1 October batch was present on the listing at that time.[1]
- **Snapshot:** 2026-10-01T00:15:01Z.
- **Coverage:** traversed all 480 entries in the announcement batch and found 419 with at least one `math.*` subject tag.[1]
- Checked the top three arXiv abstracts, version histories, introductions, and main-results sections.[2][3][4]
- Checked abstracts and version histories for two of the other four selected papers.[5][6]
- Checked the remaining two selected papers’ abstracts and version histories.[7][8]
- This is a curated shortlist, not a complete review of all 419 math-tagged entries.[1]
- **Ranking:** inferred from explicit theorem/conjecture claims, quantitative improvement, breadth of stated scope, and recency—not readership or downloads. Semantic Scholar returned 0 current citations for two checked records; the rest did not yield a complete citation sample, and no independent expert discussion surfaced in the exact-title searches checked.[9][10]
- **Caveat:** arXiv publishes no official trending chart. Citation totals are not period gains, and the ranking should not be read as “most read” or “most downloaded.”

## Sources

[1] https://arxiv.org/list/math/recent
[2] https://arxiv.org/abs/2609.37471
[3] https://arxiv.org/abs/2609.38135
[4] https://arxiv.org/abs/2609.38115
[5] https://arxiv.org/abs/2609.35920
[6] https://arxiv.org/abs/2609.37886
[7] https://arxiv.org/abs/2609.37466
[8] https://arxiv.org/abs/2609.37877
[9] https://api.semanticscholar.org/graph/v1/paper/arXiv:2609.38135?fields=title%2Cauthors%2Cyear%2CcitationCount%2CinfluentialCitationCount%2CreferenceCount%2CpublicationTypes%2CfieldsOfStudy%2CexternalIds
[10] https://api.semanticscholar.org/graph/v1/paper/arXiv:2609.37886?fields=title%2Cauthors%2Cyear%2CcitationCount%2CinfluentialCitationCount%2CreferenceCount%2CpublicationTypes%2CfieldsOfStudy%2CexternalIds
