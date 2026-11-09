Mathematics — latest announcement batch: Friday, 6 November 2026

Ten notable papers from the 409-entry Mathematics batch. The loudest mathematical signal is two independent papers claiming the sharp fixed-dimensional order in Tusnády’s discrepancy problem, one of them extending the result to online two-sample thinning. Other standouts close specific gaps in logic, lattice theory, and arithmetic geometry. Spoken agenda: discrepancy first, then logic and discrete structures, followed by geometry, stochastic analysis, optimization, and extremal combinatorics. This is an inferred selection, not an official arXiv trending chart; attention evidence is limited for papers only days old, so this is a result-driven list of notable recent papers, not a measured popularity ranking.

## Top papers (ranked)

### 1. [Tusnády's problem and online two-sample thinning](https://arxiv.org/abs/2611.08455)
- **Abstract:** The author proves the sharp discrepancy order in Tusnády's problem in every fixed dimension, a robust lower bound after limited deletions, and minimax rates for online thinning of two samples, including a sharp one-dimensional terminal rate.
- **Authors:** Yuhao Lei
- **arXiv:** `2611.08455v1` (published 2026-11-05 18:47:43 UTC; categories: `math.CO`, `cs.DS`, `math.PR`)
- **Evidence for ranking:** This is an independent same-batch proof of the sharp Tusnády order for every fixed dimension `d≥2`, alongside new quantitative results for online thinning. The author also identifies a remaining logarithmic gap for terminal discrepancy in dimensions `k≥2`; both the broad theorem and the explicit gap make the result especially informative. No citation-momentum signal is used.
- **Claimed result:** Theorem 1.1 gives `Δ_d(N)=Θ_d((log N)^(d−1/2))` for fixed `d≥2`; Theorem 1.2 gives minimax expected prefix discrepancy `Θ_{k,ρ}((log n)^(k+1/2))` for fixed `k≥1` and `0<ρ<2`. In dimension one, the optimal terminal discrepancy is `Θ_ρ((log log n)^(3/2))`.
- **Assumptions and setting:** The geometry theorem concerns worst-case finite point sets and axis-parallel boxes. Online thinning uses two independent size-`n` samples from an unknown common Borel law; keep/discard decisions are irrevocable and online, with expected deletion budget `ρn`.
- **Caveat:** For `k≥2`, the paper's terminal-thinning upper and lower bounds still differ by a factor of `log n`; the sharp prefix rate does not close that gap.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Probability & statistics

### 2. [Resolving Tusnády's Problem](https://arxiv.org/abs/2611.06998)
- **Abstract:** The author proves a matching lower bound for combinatorial discrepancy of anchored boxes in each fixed dimension at least three; combined with existing bounds, this determines the order for axis-parallel boxes in every fixed dimension at least two.
- **Authors:** Nicola Wengiel
- **arXiv:** `2611.06998v1` (published 2026-11-04 18:58:56 UTC; categories: `math.CA`, `cs.CG`, `cs.DS`, `math.CO`)
- **Evidence for ranking:** Its main theorem closes the remaining logarithmic-factor gap for every fixed `d≥3`; the planar case is combined with Wei's prior lower bound. It is an independent same-batch claim of the full sharp order, corroborating the result pattern in paper 1, but the two papers use distinct arguments.
- **Claimed result:** Theorem 1.1 gives discrepancy at least `c_d(log N)^(d−1/2)` for anchored boxes for each fixed `d≥3`; together with known upper bounds and the planar result, the authors derive `Θ_d((log N)^(d−1/2))` for axis-parallel boxes for all fixed `d≥2`.
- **Assumptions and setting:** `N`-point sets, axis-parallel or anchored boxes, and fixed dimension; constants may depend on the dimension.
- **Caveat:** The paper does not optimize dimension-dependent constants. Its new lower-bound proof treats `d≥3`; the planar lower bound needed for the all-dimensions conclusion is prior work.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 3. [First-Order Model Checking on Monadically Dependent Graph Classes](https://arxiv.org/abs/2611.08143)
- **Abstract:** The authors prove fixed-parameter tractability of first-order model checking on every monadically dependent graph class and, with the known hardness direction, give the conjectured characterization for hereditary classes.
- **Authors:** Jan Dreier, Nikolas Mählmann, Szymon Toruńczyk
- **arXiv:** `2611.08143v1` (published 2026-11-05 15:04:35 UTC; categories: `cs.LO`, `cs.DM`, `cs.DS`, `math.CO`, `math.LO`)
- **Evidence for ranking:** The abstract describes resolution of the tractability direction of a central model-checking conjecture. The result combines structural graph decompositions, locality, and type counting; the paper links a Lean formalization, a checkable proof artifact. These cross-field signals support a high placement, but this is not a readership ranking.
- **Claimed result:** Theorem 1.1 gives an algorithm running in `O_{C,φ,ε}(n^(3+ε))` on `n`-vertex graphs in a monadically dependent class `C`; Theorem 1.2 bounds the number of fixed-rank types over a finite parameter set polynomially in its size.
- **Assumptions and setting:** First-order model checking on graphs in a monadically dependent class; the running-time guarantee depends on the class, formula, and `ε`. The full hereditary-class characterization also uses the previously established hardness direction and the standard `FPT ≠ AW[*]` assumption.
- **Caveat:** The tractability theorem applies when the input graph belongs to a monadically dependent class, and the stated exponent is `3+ε`, not a uniform cubic bound.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Logic & foundations; Combinatorics & discrete mathematics

### 4. [An extremal unimodular lattice of rank 37](https://arxiv.org/abs/2611.07138)
- **Abstract:** The author constructs an extremal unimodular lattice of rank 37 and minimum four, resolving the last undetermined optimal minimum through rank 48; an explicit 4-frame also yields a length-37 self-dual code.
- **Authors:** Eric Kubischta
- **arXiv:** `2611.07138v1` (published 2026-11-04 21:06:40 UTC; categories: `math.CO`, `math.NT`)
- **Evidence for ranking:** The introduction identifies rank 37 as the last unresolved optimal-minimum case among integral unimodular lattices through rank 48. The construction also resolves the corresponding length-37 code case and connects lattice theory with coding theory.
- **Claimed result:** The main theorem constructs an integral unimodular lattice of rank 37 and minimum four, with automorphism group `AGL(1,13)×C6`; an explicit 4-frame yields a Type I self-dual `Z/4Z` code of length 37 and minimum Euclidean weight 16.
- **Assumptions and setting:** Positive-definite integral unimodular lattices; minimum is the smallest squared norm of a nonzero lattice vector. The code conclusion uses a 4-frame in the constructed lattice.
- **Caveat:** The result settles the rank-37 case, not optimal minima in higher ranks; the code conclusion depends on the explicit 4-frame supplied in the paper.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 5. [Pointless K3 surfaces over finite fields](https://arxiv.org/abs/2611.08356)
- **Abstract:** The authors prove that K3 surfaces without rational points over the finite field with `q` elements exist if and only if `q≤11`, using lattice bounds, the Artin–Tate formula, and Niemeier-lattice embeddings.
- **Authors:** Asher Auel, Philip Engel, Kiran S. Kedlaya, Sair Shaikh
- **arXiv:** `2611.08356v1` (published 2026-11-05 17:36:46 UTC; categories: `math.NT`, `math.AG`)
- **Evidence for ranking:** This is a sharp existence/nonexistence cutoff in arithmetic geometry, with a proof route linking finite-field point counts to definite lattices. The paper notes an independent proof of the same classification by Brandhorst and Takada (arXiv:2611.06366), corroborating the result's salience without relying on author reputation.
- **Claimed result:** The authors prove that a K3 surface with no `F_q`-rational point exists exactly when the prime power `q≤11`; they note the bound improves an input to certain threefold rational-point results.
- **Assumptions and setting:** Smooth K3 surfaces over finite fields, with `q` a prime power; the classification concerns existence of at least one rational point over the field of definition.
- **Caveat:** The result is specific to K3 surfaces over finite fields. The authors mention a separate proof; they also note a close relationship between two lattice/Frobenius viewpoints that they have not worked out.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

### 6. [The probabilistic bound for perfect hashing is sharp only for binary alphabets](https://arxiv.org/abs/2611.08230)
- **Abstract:** For perfect `q`-hash codes, the authors prove that the classical probabilistic rate lower bound is attained only at `q=2`, give a strict improvement for every `q≥3`, and establish a larger asymptotic improvement for sufficiently large `q`.
- **Authors:** Shitao Li, Minjia Shi
- **arXiv:** `2611.08230v1` (published 2026-11-05 16:13:19 UTC; categories: `math.CO`, `cs.IT`)
- **Evidence for ranking:** The paper proves the first assertion of the Xing–Yuan conjecture for every `q≥3` and improves the known asymptotic scale of the excess lower bound. Its combinatorics/information-theory cross-list and explicit theorem statements support its placement among this batch's notable results; no citation trend is used.
- **Claimed result:** The authors show `R_q=B_q` iff `q=2`, and for every `η>0`, `R_q ≥ B_q + exp(-(2+η)q)` for all sufficiently large `q`; they also bound what subexponential-length pairwise-uniform inner codes can achieve within the studied concatenation framework.
- **Assumptions and setting:** Asymptotic rate `R_q` of perfect `q`-hash codes as block length tends to infinity with integer alphabet size `q`; the exponential-scale statement has an unspecified threshold `q_0(η)`.
- **Caveat:** These are lower bounds, not an exact determination of `R_q`; the exact exponential order of `R_q−B_q` remains undetermined.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics

### 7. [On do Carmo's Question: The Properly Embedded Case](https://arxiv.org/abs/2611.08454)
- **Abstract:** The author proves that every complete noncompact, two-sided, properly embedded constant-mean-curvature hypersurface of finite Morse index in Euclidean space is minimal, in every dimension, without curvature or volume-growth bounds.
- **Authors:** Gongping Niu
- **arXiv:** `2611.08454v1` (published 2026-11-05 18:47:40 UTC; categories: `math.DG`, `math.AP`)
- **Evidence for ranking:** The stated theorem removes dimension restrictions and curvature/volume-growth bounds for the properly embedded finite-index case; the introduction contrasts it with earlier results requiring bounded curvature or restricted ambient dimensions. The geometry/PDE cross-list is a second checkable scope signal.
- **Claimed result:** Theorem 1 states that a smooth, connected, complete, noncompact, two-sided, properly embedded, boundaryless CMC hypersurface of finite Morse index in `R^(n+1)` has zero mean curvature for every `n≥2`.
- **Assumptions and setting:** Complete, noncompact, two-sided, properly embedded, boundaryless, finite-index hypersurface in Euclidean space; the proof uses an inscribed-radius weight and stability outside a compact set.
- **Caveat:** Proper embeddedness is essential to the presented proof; the result does not cover arbitrary immersed hypersurfaces in every dimension.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Geometry & topology; Analysis & PDE

### 8. [Weak uniqueness for the stochastic heat equation with nondegenerate diffusion: the full Hölder regime](https://arxiv.org/abs/2611.07310)
- **Abstract:** The author proves weak well-posedness for the scalar stochastic heat equation on the one-dimensional torus with uniformly nondegenerate diffusion Hölder continuous at every positive order, extending an earlier result above exponent `2/3`.
- **Authors:** Yi Han
- **arXiv:** `2611.07310v1` (published 2026-11-05 01:55:58 UTC; categories: `math.PR`)
- **Evidence for ranking:** The paper claims the full positive-Hölder range left open by the author's earlier result, and supplies detailed main theorems with distinct bounded- and unbounded-diffusion cases. It is a specific stochastic-analysis advance rather than evidence of broad field-wide attention.
- **Claimed result:** Theorem 1.1 gives weak existence and uniqueness in law for the scalar equation with bounded, uniformly nondegenerate, positively Hölder diffusion and deterministic `L²` initial data. Theorem 1.2 extends to measurable drifts of linear growth and allows unbounded diffusion under a separate initial-data condition.
- **Assumptions and setting:** One-dimensional torus and scalar stochastic heat equation. For Theorem 1.1 the diffusion is bounded, uniformly nondegenerate, and `β`-Hölder for any `β>0`; the unbounded-diffusion extension in Theorem 1.2 assumes bounded initial data.
- **Caveat:** The result is weak well-posedness (uniqueness in law), not pathwise uniqueness. The authors say their localization proof's `L∞` initial-data assumption for unbounded diffusion may be replaceable by `L²` with a finer argument.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Probability & statistics; Analysis & PDE

### 9. [An Accelerated Proximal Gradient Method for Bures-Wasserstein Space](https://arxiv.org/abs/2611.08468)
- **Abstract:** The authors lift a class of composite optimization problems on Gaussian measures in Bures–Wasserstein space to affine transport maps and obtain an accelerated method with an `O(k^-2)` objective gap, including a faster rate for a specified Gaussian variational-inference setting.
- **Authors:** Jakob Nylöf, Sloan Nietert, Julien Pallage, Giancarlo Ferrari-Trecate, Daniel Kuhn, John Lygeros
- **arXiv:** `2611.08468v1` (published 2026-11-05 18:55:10 UTC; categories: `math.OC`)
- **Evidence for ranking:** The abstract states a minimax-optimal `O(k^-2)` rate under explicit lift conditions and an improvement from `O(k^-1)` for its Gaussian variational-inference application. The listing says it was accepted to a NeurIPS 2026 workshop, an external venue signal rather than journal publication.
- **Claimed result:** BW-FISTA achieves objective gap `O(k^-2)` when the smooth and nonsmooth components admit the required convex smooth and convex proximable affine lifts; for log-concave, log-smooth Gaussian variational inference, an entropy term admits an exact proximal step.
- **Assumptions and setting:** Optimization over the Bures–Wasserstein space of Gaussian measures, with the stated affine-lift regularity; the variational-inference result assumes a log-concave, log-smooth target and the paper's conditions on stochastic-gradient noise.
- **Caveat:** The rate guarantee applies to the specified liftable objective class; numerical experiments do not establish performance beyond that setting.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Optimization & control; Numerical analysis & computation

### 10. [An improved minimum degree threshold for fractional clique decompositions in partite graphs](https://arxiv.org/abs/2611.08432)
- **Abstract:** The authors prove a Dirac-type minimum-degree condition sufficient for fractional `K_r`-decompositions of large balanced `r`-partite graphs, yielding an asymptotic threshold bound for ordinary clique decompositions.
- **Authors:** Sean Longbrake, Michael Simkin, Liana Yepremyan, Michael Zheng
- **arXiv:** `2611.08432v1` (published 2026-11-05 18:25:20 UTC; categories: `math.CO`)
- **Evidence for ranking:** The abstract gives a concrete improved degree threshold and a reduction from fractional to ordinary clique decompositions. This is a precise extremal-combinatorics result; no cross-list, citation momentum, or outside attention signal was used.
- **Claimed result:** For sufficiently large `r`-partite graphs with `n` vertices in each part and partite minimum degree at least `(1−1/(30r²))n`, the authors prove a fractional `K_r`-decomposition, subject to necessary divisibility conditions.
- **Assumptions and setting:** Balanced `r`-partite graphs, sufficiently large part size, and divisibility conditions; the stated consequence is an asymptotic upper bound on the minimum-degree threshold for a `K_r`-decomposition.
- **Caveat:** The condition is sufficient and asymptotic; it does not identify the exact threshold for each finite graph size.
- **Announcement type:** new submission, 6 November 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics

## Trending Research Themes

- **Tusnády discrepancy and Gaussian small-ball methods:** Two independent papers, Lei and Wengiel, claim the sharp fixed-dimensional order. Both use Gaussian small-ball ideas in their lower bounds, but Lei adds a robust-deletion theorem and online thinning; these are two corroborating papers, not evidence by themselves of an archive-wide shift.
- **Lattice methods across arithmetic and geometry:** Kubischta uses a Cayley-table construction to settle a rank-37 unimodular-lattice case and derive a self-dual code; Auel, Engel, Kedlaya, and Shaikh use lattice bounds and Niemeier embeddings in the K3 point-classification problem. These distinct results share lattice structure as a bridge between existence and classification.
- **Discrete extremal improvements:** Perfect hashing and fractional clique decomposition both sharpen combinatorial bounds, but address separate objects and use different methods.
- **Logic and algorithmic structure (one focused result):** The model-checking paper turns monadic dependence and polynomial type-counting into tractability across several graph-class notions; it is an isolated, broad result in this batch.
- **Analysis, geometry, and stochastic models:** Niu's CMC theorem and Han's stochastic heat-equation theorem are substantial but separate advances. Bures–Wasserstein optimization is another isolated method result; these do not establish a shared field-wide shift.

## Open Problems and Research Directions

- **Author-stated gap — online terminal thinning:** For dimensions `k≥2`, Lei leaves terminal discrepancy bounds a factor of `log n` apart. Closing that gap under the paper's online, irrevocable decisions and expected deletion-budget assumptions is an explicit next problem. ([Paper 1](https://arxiv.org/abs/2611.08455).)
- **Author-stated limitation — discrepancy constants:** Wengiel does not optimize the dimension-dependent constants or thresholds. Explicit dependence on dimension and sharper finite-`N` bounds would test the strength of the construction. ([Paper 2](https://arxiv.org/abs/2611.06998).)
- **Author-identified connection — K3 lattices:** The K3 paper notes but does not work out the relationship between its Artin–Tate approach and the independent proof's Frobenius/lattice perspective. Making this bridge precise could clarify which parts of the classification depend on each viewpoint. ([Paper 5](https://arxiv.org/abs/2611.08356).)
- **Author-stated scope gap — do Carmo's question:** Niu says proper embeddedness is essential to the proof and points to constructing a suitable weight for general complete immersed CMC hypersurfaces as a route toward the full finite-index question. ([Paper 7](https://arxiv.org/abs/2611.08454).)
- **Author-stated extension — stochastic heat equation:** For the unbounded-diffusion case, Han's localization proof requires `L∞` initial data; the paper suggests a finer near-time-zero argument might reduce this to `L²`. This is a concrete extension, not a claim that the result already holds under that weaker assumption. ([Paper 8](https://arxiv.org/abs/2611.07310).)
- **Result gap — perfect-hash rates:** Li and Shi improve `B_q` for every `q≥3` but do not determine `R_q`; the large-`q` theorem leaves `q_0(η)` unspecified. Sharpening the exponential order of `R_q−B_q`, and exploring constructions beyond the studied concatenation framework, are proposed directions. ([Paper 6](https://arxiv.org/abs/2611.08230).)

## Takeaway

The clearest headline is the pair of independent Tusnády results, with the online-thinning paper adding a second minimax problem and a precise unresolved terminal gap. Elsewhere, papers close specific cases in model checking, unimodular lattices, and K3 arithmetic geometry. The ordering reflects theorem claims and corroboration, not measured readership; these are preprints whose claims still merit expert review.

## Method and sources

- **Window:** Daily, 2026-11-06 through 2026-11-06; the latest Mathematics announcement batch on Monday 2026-11-09 was Friday, 6 November, so this report uses a prior batch.
- **Snapshot:** 2026-11-09 01:24:56 UTC.
- **Coverage:** The complete 409-entry Friday batch in arXiv Mathematics recent listing was traversed; neighboring categories were included only where cross-listed in math or central to a mathematical contribution. Ten papers were selected, deduplicated by versionless arXiv ID, and checked against arXiv metadata and abstract pages. The introductions and main-result statements for the top three were read; the CMC paper's arXiv PDF introduction was used because HTML was unavailable.
- **Inference:** arXiv publishes no official trending chart. Ordering is qualitative and inferred from theorem-level results, cross-listing, independent same-result work, and venue/proof-artifact signals where present. Semantic Scholar citation metadata could not be obtained at this snapshot, so no citation counts or citation-momentum ranking are claimed.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent), the linked arXiv abstract pages above, top-paper HTML/PDF text, and the independent K3 proof at [arXiv:2611.06366](https://arxiv.org/abs/2611.06366). The model-checking paper links its Lean artifact at [LAX archive](https://laxarchive.org/lax-185574/).
