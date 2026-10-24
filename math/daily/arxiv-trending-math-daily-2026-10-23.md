# arXiv Mathematics — notable papers from the Fri 23 Oct 2026 batch

Six selected papers; the batch's strongest shared pattern is boundary-testing mathematics: counterexamples to expected principles, sharper bounds, and rigidity or uniqueness thresholds. Spoken agenda: randomized query composition and spectral conjectures, then a graph bound, a finite-group tiling result, and two sharp PDE/geometry statements. This is an inferred shortlist, not an official arXiv trending chart; the very recent papers have little citation evidence (Semantic Scholar currently reports zero citations for each selected paper), so the ordering is not a measured popularity ranking.

Today is Sat 24 Oct and the latest batch available is Fri 23 Oct 2026; this daily report therefore uses the prior announcement batch. The six are selected highlights, not a claim to cover all mathematics submissions.

## Top papers (ranked)

### 1. [No Perfect Randomized Composition](https://arxiv.org/abs/2610.31638)
- **Abstract:** The paper constructs total Boolean functions whose randomized query complexity under composition is smaller than the product of the two component complexities by a logarithmic factor, and develops related separations among query-complexity measures.
- **Authors:** Alexander Meiburg
- **arXiv:** `2610.31638v1` (published 2026-10-22 17:52:26 UTC; categories: `cs.CC`, `math.CO`)
- **Evidence for ranking:** Ranked first for the concrete counterexample to a standard composition principle, cross-listing between computational complexity and combinatorics, and a same-day item in the Theory of Computing Report; the abstract also reports a Lean formalization of the total-function separation.
- **Claimed result:** The author constructs total Boolean functions with `R(f∘g) = Θ(R(f)R(g)/log R(g))`, refuting a constant-factor product lower bound for total-function composition; the paper also gives further separations among related query measures.
- **Assumptions and setting:** Bounded-error randomized query complexity of block compositions of total Boolean functions; the exhibited separation is logarithmic and uses carefully coupled input sizes.
- **Caveat:** The author explicitly notes that this does not refute composition up to polylogarithmic factors; the large separation depends on the construction's scale relationship.
- **Announcement type:** new submission, Fri 23 Oct 2026
- **Themes:** Combinatorics & discrete mathematics

### 2. [Lenses make many points: Pure point spectrum disproves Simon's $L^2$ conjecture](https://arxiv.org/abs/2610.31637)
- **Abstract:** For every dimension `d ≥ 2` and `0 ≤ σ < 1/3`, the authors construct smooth, bounded, nonnegative potentials with arbitrarily small stated weighted norms for which the Schrödinger operator has pure point spectrum throughout positive energies.
- **Authors:** Simon Becker, Mengxuan Yang
- **arXiv:** `2610.31637v1` (published 2026-10-22 17:52:23 UTC; categories: `math.SP`, `math-ph`)
- **Evidence for ranking:** A striking explicit counterexample to a named spectral conjecture, cross-listed in spectral theory and mathematical physics, and surfaced in a same-day spectral-theory research feed; a MathWorld entry also appeared for the conjecture/result.
- **Claimed result:** Becker and Yang claim that their potentials have no continuous spectral component on `[0,∞)`, disproving the stated Simon conjecture; the paper's Theorem 1.1 gives the construction under the stronger weighted condition for every `σ < 1/3`.
- **Assumptions and setting:** Schrödinger operators `−Δ+V` on `R^d`, `d ≥ 2`; `V` is smooth, bounded and nonnegative, with both the unweighted and additional `|x|^σ`-weighted radial `L²` quantities arbitrarily small.
- **Caveat:** The weight range stops below `σ = 1/3`; the paper also discloses LLM assistance in developing the construction, making independent scrutiny of the full proof especially important. This report has not checked the proof.
- **Announcement type:** new submission, Fri 23 Oct 2026
- **Themes:** Analysis & PDE; Mathematical physics

### 3. [Conway's thrackle conjecture: a new upper bound of $\frac43n$](https://arxiv.org/abs/2610.31589)
- **Abstract:** The author proves that a thrackleable graph with `n ≥ 4` vertices has at most `⌊4(n−1)/3⌋` edges, combining a finite computer-assisted result with discharging arguments in plane and projective-plane embeddings.
- **Authors:** Dániel Gábor Simon
- **arXiv:** `2610.31589v1` (published 2026-10-22 17:23:50 UTC; categories: `math.CO`, `math.GN`, `math.GT`)
- **Evidence for ranking:** A sharper explicit bound on a long-standing conjecture, cross-listed across combinatorics, general mathematics, and geometric topology; the introduction compares it with the preceding `18/13`-type bound, so the improvement is checkable from the paper itself.
- **Claimed result:** Simon proves `m ≤ ⌊4(n−1)/3⌋` for every thrackleable graph on `n ≥ 4` vertices.
- **Assumptions and setting:** Finite simple graphs admitting a plane drawing in which each pair of edges meets exactly once, either at a shared endpoint or a proper crossing; the proof combines discharging with verification of the conjectured bound for graphs up to 12 vertices.
- **Caveat:** The new upper bound remains above Conway's conjectured `m ≤ n`, so the conjecture is not settled; the proof relies on the cited computer-assisted finite verification.
- **Announcement type:** new submission, Fri 23 Oct 2026
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 4. [Fuglede's conjecture holds in $\mathbb{F}_{p}^{d}$ for $p=2,\,d=8$ and $p=11,\,d=3$](https://arxiv.org/abs/2610.30712)
- **Abstract:** The authors prove the finite-group tile/spectral equivalence in `F₂⁸` and `F₁₁³`, and give substantial additional structure and reductions for spectral sets in `F₂⁹`.
- **Authors:** Samuel J. Ferguson, Joshua Iosevich
- **arXiv:** `2610.30712v1` (published 2026-10-22 04:30:10 UTC; categories: `math.CO`)
- **Evidence for ranking:** It resolves two specific cases of a central harmonic-analysis conjecture, contributes reductions in a neighboring dimension, and provides described computational verification programs among its ancillary materials.
- **Claimed result:** Ferguson and Iosevich prove Fuglede's conjecture for `F₂⁸` and `F₁₁³`; for `F₂⁹` they show every tile is spectral, every spectral set has power-of-two size, and all spectral cardinalities other than 64 tile.
- **Assumptions and setting:** Nonempty subsets of finite vector spaces `F_p^d`; “spectral” means admitting an orthogonal character spectrum, while “tiles” means tiling the group by translations.
- **Caveat:** These are finite-group results, not a resolution of Fuglede's conjecture in general; the abstract leaves the cardinality-64 case in `F₂⁹` for further work.
- **Announcement type:** new submission, Fri 23 Oct 2026
- **Themes:** Combinatorics & discrete mathematics

### 5. [Non-uniqueness for the forced one-dimensional Vlasov-Poisson equation](https://arxiv.org/abs/2610.31629)
- **Abstract:** For every finite `p`, the author constructs two distinct distributional solutions with the same zero initial data for a forced one-dimensional Vlasov–Poisson problem, while proving uniqueness in the stated Lipschitz-field class when the spatial density is bounded.
- **Authors:** Mikaela Iacobelli
- **arXiv:** `2610.31629v1` (published 2026-10-22 17:47:45 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract states a sharp contrast between nonuniqueness for every finite `L^p` density bound and uniqueness for bounded density, a precise well-posedness threshold rather than a qualitative example.
- **Claimed result:** Iacobelli constructs a nonnegative source and two nonnegative solutions in `C([0,1];L¹(R²))` with the same zero data and uniformly `L^p(R)` spatial densities for every finite `p`; in the Lipschitz-electric-field class, bounded spatial density restores uniqueness.
- **Assumptions and setting:** Forced one-dimensional Vlasov–Poisson equation on the whole space; the source is continuous in time with values in `L¹(R²)` and vanishes initially, and the ion density is smooth for positive times.
- **Caveat:** The result is for a forced one-dimensional problem with the constructed source; it does not assert nonuniqueness for the unforced equation or higher-dimensional settings.
- **Announcement type:** new submission, Fri 23 Oct 2026
- **Themes:** Analysis & PDE

### 6. [Collapsed translating solitons with planar wings](https://arxiv.org/abs/2610.31669)
- **Abstract:** For complete embedded translators in `R³` with finite genus and finite entropy, the authors prove that a collapsed translator with all wings of planar type must be a vertical plane, and classify the collapsed finite-genus case below entropy 3.
- **Authors:** Eddygledson Souza Gama, Francisco Martín, Niels Martin Møller
- **arXiv:** `2610.31669v1` (published 2026-10-22 17:59:50 UTC; categories: `math.DG`)
- **Evidence for ranking:** A rigidity theorem with a stated classification corollary, including a sharp exterior decay estimate as a named technical ingredient; ranked after the broader conjecture and bound results because the available independent attention evidence is thinner.
- **Claimed result:** Gama, Martín, and Møller claim planar-wing rigidity for collapsed translators and a full classification of collapsed embedded finite-genus translators with entropy `λ < 3`.
- **Assumptions and setting:** Complete embedded translating solitons in `R³`, finite genus and finite entropy; the rigidity statement additionally assumes collapsed ends whose wings are all planar in the authors' weak topological sense.
- **Caveat:** The rigidity hypothesis restricts the geometry of the ends, and the stated classification is limited to entropy below 3; it does not classify all translating solitons.
- **Announcement type:** new submission, Fri 23 Oct 2026
- **Themes:** Geometry & topology; Analysis & PDE

## Trending Research Themes

- **Testing where broad principles fail:** Meiburg gives a total-function counterexample to constant-factor randomized composition; Becker and Yang give a spectral counterexample; Iacobelli constructs nonuniqueness below an `L∞` density threshold. These are distinct techniques and fields, but together make boundary and hypothesis sensitivity a recurring pattern in this selected batch.
- **Combinatorial structure paired with explicit bounds or finite checks:** Simon's thrackle bound uses structural embeddings, discharging, and a small-graph verification; Ferguson and Iosevich use Fourier structure, incidence methods, and exact computations in finite groups. This is a shared flavor in two selected combinatorics papers, not evidence of an archive-wide shift.
- **Rigidity and threshold statements:** Iacobelli's bounded-density uniqueness criterion and Gama–Martín–Møller's planar-wing rigidity both identify restrictive conditions under which behavior becomes rigid, though one is kinetic PDE and the other geometric analysis.

## Open Problems and Research Directions

- **Open problem (reported in the paper):** Conway's `m ≤ n` thrackle conjecture remains open after the new `4(n−1)/3` upper bound. **Follow-up direction (synthesis):** test whether stronger structural exclusions in plane/projective-plane embeddings can tighten the discharging argument, beyond the finite verification used here. [Simon, arXiv:2610.31589]
- **Open case (reported in the abstract):** In `F₂⁹`, the paper leaves spectral sets of cardinality 64 as the remaining tile question. **Follow-up direction (synthesis):** combine the Fourier-support plane criterion with the paper's classified Hadamard/code reductions to isolate whether size-64 spectral sets must tile. [Ferguson–Iosevich, arXiv:2610.30712]
- **Boundary question (from the stated range):** Becker and Yang's counterexample reaches every weight exponent below `1/3`; the endpoint and stronger decay regime are not settled by this theorem. **Follow-up direction (synthesis):** investigate whether endpoint assumptions at `σ = 1/3`, or additional regularity/decay, force any continuous spectral component. [Becker–Yang, arXiv:2610.31637]
- **Generalization suggested by a limitation:** Meiburg's construction loses only a logarithmic factor and does not rule out polylogarithmic composition bounds. **Follow-up direction (synthesis):** determine whether total Boolean functions can yield larger separations, or prove a robust polylogarithmic lower bound under the same hypotheses. [Meiburg, arXiv:2610.31638]
- **Threshold extension (synthesis from the theorem):** Iacobelli separates every finite-`p` density bound from bounded density in the stated Lipschitz-field setting. It would be useful to test intermediate Lorentz/Orlicz controls or additional source regularity to locate finer uniqueness thresholds. [Iacobelli, arXiv:2610.31629]

## Takeaway

The best-supported story in this batch is not a measurable popularity surge but a cluster of unusually sharp statements: counterexamples to expected principles, a substantial improvement to a graph bound, and exact finite cases or regularity thresholds. These are fresh preprints with little citation history; their mathematical claims, especially the AI-assisted spectral construction, still need independent expert review.

## Method and sources

- **Window:** daily; selected arXiv announcement batch Friday 2026-10-23. Today is Saturday 2026-10-24, so this is the latest prior batch. The selected papers were first submitted on 2026-10-22; their arXiv v1 timestamps are recorded above. Snapshot: 2026-10-24 00:24 UTC.
- **Coverage:** the arXiv Mathematics archive (`math.*`), including the papers' specific primary and cross-list categories. Candidate discovery used the arXiv API's `cat:math.*` submitted-date query for 2026-10-22 through 2026-10-23, which returned 263 records across the surrounding two-day bracket; six selected abstract pages were then verified. Search results identified Fri 23 Oct as the latest announcement batch. The arXiv recent/new list endpoint was rate-limited during this run, so complete traversal of every entry in the batch could not be independently confirmed; this is a selected shortlist and may omit other strong papers.
- **Inference:** arXiv publishes no official trending chart. Ordering is inferred from concrete mathematical claims, cross-listing, independently discoverable same-day research coverage where found, and the paper's own stated technical contribution; recency is a tie-breaker. Semantic Scholar Graph API current citation totals were zero for all six selected papers, so citation momentum is too sparse to measure. No citation count is presented as a gain during the window.
- **Reading:** all six arXiv abstract pages were checked; introductions and main-result statements were inspected for the top three. No proof was independently verified.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); individual arXiv abstract pages linked in each entry; [Theory of Computing Report item on Meiburg's paper](https://theory.report/); [MathWorld entry on Simon's $L^2$ conjecture](https://mathworld.wolfram.com/SimonsL2Conjecture.html); Semantic Scholar Graph records queried by arXiv ID.
