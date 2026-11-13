# arXiv Mathematics — daily report

## Headline

Latest available announcement batch: Wednesday, 2026-11-11; 7 papers ranked. The selected set is unusually rich in explicit conjecture resolutions and sharp structural bounds, spanning quasiperiodic spectra, Diophantine approximation, hypergraph coloring, algebraic geometry, and topology. Agenda: the supercritical Ten Martini result, two number-theory breakthroughs, then exact classifications and the questions they leave open. This is an inferred notable-paper ordering, not an official arXiv trending chart; citation evidence is limited for papers only days old, so the order is not a popularity measure.

## Top papers (ranked)

### 1. [The Supercritical Ten Martini Problem](https://arxiv.org/abs/2611.13068)
- **Abstract:** The authors prove that for every nonconstant real-analytic one-frequency Schrödinger operator, the part of the spectrum with positive Lyapunov exponent is a Cantor set, using a higher-dimensional extension of a Kotani–almost-reducibility strategy.
- **Authors:** Lingrui Ge, Svetlana Jitomirskaya, Jiangong You
- **arXiv:** `2611.13068v1` (published 2026-11-09 18:55:42 UTC; categories: `math-ph` (primary), `math.DS`, `math.SP`)
- **Evidence for ranking:** The arXiv introduction identifies this as proving You’s supercritical Cantor-spectrum conjecture, and Theorem 1.1 states the exact spectral scope; [Wolfram MathWorld](https://mathworld.wolfram.com/SupercriticalTenMartiniProblem.html) independently summarizes the result. This is the strongest combination here of a substantial theorem and outside mathematical attention.
- **Claimed result:** The authors’ Theorem 1.1 says that for nonconstant real-analytic `v` and irrational frequency `α`, `Σ(v,α) ∩ closure({E : L(E)>0})` is a Cantor set, when nonempty; the whole spectrum is Cantor if `L(E)>0` throughout it.
- **Assumptions and setting:** One-frequency Schrödinger operators on `ℓ²(ℤ)`, with a nonconstant real-analytic potential and irrational frequency; the primary conclusion concerns the positive-Lyapunov part of the spectrum.
- **Caveat:** It is not an unconditional Cantor-spectrum theorem for all energies: zero-Lyapunov portions are outside the main conclusion, and the paper notes that subcritical examples can have spectral intervals.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Mathematical physics

### 2. [A counterexample to the Erdős--Mahler conjecture](https://arxiv.org/abs/2611.13604)
- **Abstract:** For every real `τ ≥ 4`, the author constructs a Cantor set of numbers with irrationality exponent `τ` and infinitely many regular continued-fraction convergents whose numerators and denominators are powers of 2 and 3, respectively.
- **Authors:** Diego Marques
- **arXiv:** `2611.13604v1` (published 2026-11-10 05:31:31 UTC; categories: `math.NT` (primary))
- **Evidence for ranking:** The paper claims a counterexample to a 1939 conjecture, gives a precise construction, and includes a [Lean 4 formalization](https://github.com/DiegoMarquesMath/Erdos-Mahler); [Wolfram MathWorld](https://mathworld.wolfram.com/Erdos-MahlerConjecture.html) now cites the claimed counterexample. Those are concrete corroboration signals, not citation-growth data.
- **Claimed result:** The author’s main theorem constructs, for each real `τ ≥ 4`, a Cantor set `Kτ ⊂ (1,2)` whose members have irrationality exponent `τ` and infinitely many convergents of the form `2ᵃ/3ᵇ`, thereby contradicting the stated conjecture.
- **Assumptions and setting:** Regular continued fractions of irrational real numbers; the construction prescribes convergents with numerator a power of 2 and denominator a power of 3, and applies to finite exponents `τ ≥ 4`.
- **Caveat:** The stated construction covers `τ ≥ 4`; it does not settle whether analogous sets exist for every finite exponent below 4.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Algebra & number theory

### 3. [The Proof of the Alon--Kim Conjecture](https://arxiv.org/abs/2611.13698)
- **Abstract:** For fixed integers `k ≥ t ≥ 1` and `ε > 0`, the authors prove that every `k`-uniform multihypergraph whose distinct edges intersect in at most `t` vertices has edge-chromatic number at most `(t−1+1/t+ε)Δ` once its maximum degree `Δ` is sufficiently large.
- **Authors:** Chengshuo Qiao, Zhijun Lu, Huimin Song
- **arXiv:** `2611.13698v1` (published 2026-11-10 07:44:41 UTC; categories: `math.CO` (primary))
- **Evidence for ranking:** The abstract states a resolution of the Alon–Kim asymptotic edge-coloring conjecture with its quantifiers and bound, and identifies a combination of finite-dimensional convex optimization and probabilistic methods. The result’s specificity and breadth within hypergraph coloring drive its placement; no citation-growth claim is used.
- **Claimed result:** The authors claim that for every fixed `k,t,ε` in the stated range there is a sufficiently large degree threshold above which the conjectured edge-coloring inequality holds for all such multihypergraphs.
- **Assumptions and setting:** Finite `k`-uniform multihypergraphs; any two distinct edges meet in at most `t` vertices; `k,t` and positive `ε` are fixed while `Δ` is sufficiently large.
- **Caveat:** This is asymptotic in maximum degree, not an exact bound for all finite degrees; the abstract does not give an explicit threshold in `Δ`.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Combinatorics & discrete mathematics

### 4. [The closure of the nonreal roots of bounded-height polynomials is connected exactly at pronic heights](https://arxiv.org/abs/2611.14517)
- **Abstract:** For the closure `Cₕ` of nonreal roots of integer polynomials with coefficient modulus at most `h`, the author proves that `Cₕ` is connected exactly when `h=q(q−1)` is pronic, and has at least five components otherwise.
- **Authors:** Bernat Espigule
- **arXiv:** `2611.14517v1` (published 2026-11-10 18:58:59 UTC; categories: `math.CV` (primary), `math.NT`)
- **Evidence for ranking:** The paper gives an exact if-and-only-if arithmetic classification, links complex-variable and number-theoretic settings, and the announcement lists a substantial [Zenodo computational companion](https://doi.org/10.5281/zenodo.24117729). The abstract also connects the height-two case with an older numerical observation.
- **Claimed result:** The author claims connectedness precisely at pronic heights `2, 6, 12, 20, …`; at every other height there are at least five components, with further infinite-component results for specified height ranges.
- **Assumptions and setting:** `Cₕ` is the closure of the nonreal roots of integer polynomials whose coefficients have modulus at most the positive integer height `h`; the statement excludes nonzero real roots from the set being closed.
- **Caveat:** The general nonpronic conclusion gives a lower bound on the number of components, not an exact component count at every height; the abstract gives detailed infinite-component statements only for specified ranges and exceptions.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Algebra & number theory

### 5. [No 13-vertex triangulation of the three-torus](https://arxiv.org/abs/2611.14367)
- **Abstract:** The author rules out a 13-vertex simplicial triangulation of the three-torus, narrowing its minimum vertex count to 14 or 15.
- **Authors:** Geunho Lim
- **arXiv:** `2611.14367v1` (published 2026-11-10 17:23:48 UTC; categories: `math.GT` (primary), `math.CO`)
- **Evidence for ranking:** This excludes the first case left unresolved by the standard lower bound, using a `g₂` inequality, fundamental-group analysis, and Alexander duality; [Wolfram MathWorld’s three-torus entry](https://mathworld.wolfram.com/Three-Torus.html) independently notes the result and its consequence for the minimum.
- **Claimed result:** The author’s Theorem 1.1 proves that no simplicial triangulation of `T³` has 13 vertices; together with existing bounds and a 15-vertex construction, the minimum lies between 14 and 15.
- **Assumptions and setting:** Finite simplicial triangulations of the three-torus; the obstruction uses the `g₂` lower bound and properties of fundamental groups of small simplicial complexes.
- **Caveat:** The result does not decide whether a 14-vertex triangulation exists, so it does not yet establish that the known 15-vertex triangulation is vertex-minimal.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Geometry & topology; Combinatorics & discrete mathematics

### 6. [On the stable birational type of Fano threefolds](https://arxiv.org/abs/2611.14417)
- **Abstract:** For a very general cubic threefold `X`, the author claims that every smooth cubic threefold stably birational to `X` is isomorphic to `X`, and says the method also applies to a sextic double solid and a quartic threefold.
- **Authors:** Claire Voisin
- **arXiv:** `2611.14417v1` (published 2026-11-10 17:57:27 UTC; categories: `math.AG` (primary))
- **Evidence for ranking:** The abstract states a rigidity result for stable birational equivalence and identifies applications to multiple Fano threefold families; the scope is concrete and theorem-like, but the paper has no cross-listing signal in the checked metadata.
- **Claimed result:** The author claims stable birational rigidity within the smooth cubic threefolds for a very general cubic, with analogous applications to the named Fano threefolds and discussion of higher dimensions.
- **Assumptions and setting:** The reference cubic is very general; the comparison is with smooth cubic threefolds stably birational to it. Other Fano cases and higher-dimensional questions are treated as applications or discussion.
- **Caveat:** The stated cubic result is for a very general reference variety, not every cubic threefold, and the abstract does not spell out the precise higher-dimensional conclusions.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Geometry & topology

### 7. [The Q-gonality of X₁(42) is 12](https://arxiv.org/abs/2611.13155)
- **Abstract:** The author proves that both the `𝔽₅`-gonality and `ℚ`-gonality of `X₁(42)` are 12, improving the previous lower bound of 10, and deduces the least degree supporting infinitely many rational points.
- **Authors:** Sourajyoti Maiti
- **arXiv:** `2611.13155v1` (published 2026-11-09 19:40:36 UTC; categories: `math.NT` (primary), `math.AG`)
- **Evidence for ranking:** The paper claims an exact invariant, improves a published lower bound, and reports a reproducible lower-bound computation over 743,231 Riemann–Roch spaces; the abstract notes an earlier search using reductions from van Hoeij’s code with the same outcome.
- **Claimed result:** The author claims `gon_{𝔽₅}(X₁(42)) = gon_{ℚ}(X₁(42)) = 12`; since `J₁(42)(ℚ)` is finite, 12 is the least degree in which `X₁(42)` has infinitely many rational points.
- **Assumptions and setting:** The modular curve is `X₁(42)`; the claim concerns gonality over `𝔽₅` and `ℚ`, and uses finiteness of `J₁(42)(ℚ)` for the rational-point consequence.
- **Caveat:** The lower bound relies on an exhaustive Riemann–Roch computation and its reductions; the author records data for reproduction, but this report has not independently rerun the computation.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Algebra & number theory; Geometry & topology

## Trending Research Themes

- **Conjectures sharpened or settled by explicit bounds:** The Supercritical Ten Martini paper proves a Cantor-spectrum conjecture on the positive-Lyapunov region; Marques constructs counterexamples to Erdős–Mahler; and Qiao, Lu, and Song prove the Alon–Kim asymptotic edge-coloring bound. These are separate problems, not evidence of a single shared technique.
- **Exact arithmetic structure meets classification:** Espigule’s pronic-height criterion, Maiti’s exact modular-curve gonalities, and Marques’s restricted continued-fraction convergents all turn arithmetic constraints into precise structural conclusions, using different methods.
- **Topology through small-complex obstructions:** Lim combines a face-number inequality, small-group classification, and Alexander duality to exclude 13 vertices; this intersects combinatorics and geometric topology. The remaining 14-vertex case is still live.
- **Geometry and spectral theory connect distinct languages:** The Ten Martini proof extends a Kotani/almost-reducibility method to higher-dimensional symplectic centers, while Voisin’s Fano result concerns stable birational invariants. These are isolated signals within this batch, not a broad shift.

## Open Problems and Research Directions

- **Paper-stated open case — three-torus:** Lim’s result leaves the minimum at 14 or 15. A direct construction or exclusion of a 14-vertex triangulation would settle whether the known 15-vertex example is minimal. [2611.14367](https://arxiv.org/abs/2611.14367)
- **Boundary of the spectral theorem — synthesis:** Ge, Jitomirskaya, and You prove the Cantor property on the positive-Lyapunov part, while noting that subcritical examples may contain intervals. A useful next step is to identify additional hypotheses that distinguish zero-Lyapunov regimes with Cantor spectrum from those with intervals. [2611.13068](https://arxiv.org/abs/2611.13068)
- **Exponent range — synthesis:** Marques’s Cantor-set construction covers finite irrationality exponents `τ ≥ 4`. Investigating whether the restricted-convergent construction extends to `2 ≤ τ < 4` would test the boundary of the method; the paper’s reported theorem does not settle that range. [2611.13604](https://arxiv.org/abs/2611.13604)
- **Component counts beyond connectedness — synthesis:** Espigule classifies exactly when `Cₕ` is connected and proves lower bounds or infinite-component results in several nonpronic ranges. Determining exact component counts, especially at the exceptional heights singled out in the abstract, is a concrete continuation. [2611.14517](https://arxiv.org/abs/2611.14517)
- **Quantitative and neighboring coloring questions — synthesis:** The Alon–Kim theorem is asymptotic for fixed `k,t,ε`; extracting explicit degree thresholds or testing analogous bounds for list edge-coloring would probe how far the method extends beyond the stated setting. [2611.13698](https://arxiv.org/abs/2611.13698)

## Takeaway

This batch’s clearest signals are ambitious theorem claims with carefully bounded scope: a spectral conjecture in the positive-Lyapunov regime, a continued-fraction counterexample, and an asymptotic hypergraph-coloring theorem. The ordering reflects mathematical claims and a few checkable corroboration signals, not measured readership; all are new preprints and the proofs still warrant specialist review.

## Method and sources

- **Window:** Daily, announcement batch 2026-11-11 (the latest batch shown on arXiv as of the snapshot); the batch’s selected records were first submitted on 2026-11-09 or 2026-11-10. This is a prior batch relative to the 2026-11-13 snapshot. Batch start/end: 2026-11-11 through 2026-11-11. Snapshot: 2026-11-13 01:27:24 UTC.
- **Coverage:** The arXiv Mathematics recent listing was traversed with all 452 records for the 2026-11-11 announcement group loaded; each selected abstract and version history was checked. Seven v1 new submissions are included. The top three papers’ arXiv HTML introductions and main-result statements were also inspected; this is not proof verification.
- **Inference:** arXiv publishes no official trending chart. Ranking used theorem specificity and potential mathematical significance, independent mathematical summaries where found, cross-listing, and proof/reproducibility artifacts; recency only broke ties. Semantic Scholar citation metadata was not available from the sources checked, so no citation counts or citation momentum were used. Because attention evidence is sparse, this is a notable-recent-paper ranking rather than a measured popularity ranking.
- **Primary sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); the seven linked arXiv abstract pages above; full text for the top three via their arXiv HTML pages: [2611.13068](https://arxiv.org/html/2611.13068v1), [2611.13604](https://arxiv.org/html/2611.13604v1), and [2611.13698](https://arxiv.org/html/2611.13698v1).
- **Independent/reproducibility sources:** [MathWorld — Supercritical Ten Martini Problem](https://mathworld.wolfram.com/SupercriticalTenMartiniProblem.html); [MathWorld — Erdős–Mahler Conjecture](https://mathworld.wolfram.com/Erdos-MahlerConjecture.html); [MathWorld — Three-Torus](https://mathworld.wolfram.com/Three-Torus.html); the Lean 4 formalization and Zenodo artifact linked in the relevant entries.
