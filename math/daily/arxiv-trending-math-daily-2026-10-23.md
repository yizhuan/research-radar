# arXiv Mathematics daily — Friday, 2026-10-23 batch — 8 notable papers

The latest Mathematics announcement batch is Friday, 23 October: eight selected papers span a striking set of counterexamples, sharp bounds, classifications and critical-limit constructions, with a notable bridge between discrete mathematics and probability. Spoken agenda: a claimed disproof of a spectral conjecture, a new thrackle bound, exotic positive-curvature spheres, then critical stochastic limits and several tightly scoped classification theorems. arXiv provides no official trending chart; this is an inferred ranking, and measurable citation evidence is unavailable for this newly announced batch, so read it as notable recent work rather than measured popularity.

## Top papers (ranked)

### 1. [Lenses make many points: Pure point spectrum disproves Simon's $L^2$ conjecture](https://arxiv.org/abs/2610.31637)
- **Abstract:** For every $d\ge2$ and $0\le\sigma<1/3$, the authors construct with LLM assistance a smooth bounded nonnegative potential, arbitrarily small in a specified supremum-plus-weighted-$L^2$ norm, for which $-\Delta+V$ has pure point spectrum throughout positive energies, contradicting Simon's conjecture.
- **Authors:** Simon Becker, Mengxuan Yang
- **arXiv:** `2610.31637v1` (published 2026-10-22 17:52:23 UTC; categories: `math.SP`, `math-ph`)
- **Evidence for ranking:** The claimed counterexample addresses a named spectral conjecture in every dimension $d\ge2$ and is cross-listed in spectral theory and mathematical physics. A math.SP account repeated the announcement, and MathWorld's Simon-conjecture entry cites the 2026 result—early external visibility, not independent validation.
- **Claimed result:** The authors claim that for each $d\ge2$, $0\le\sigma<1/3$, and $\delta>0$, there is smooth bounded $V\ge0$ with $\|V\|_\infty+\mathcal I_{d,0}(V)+\mathcal I_{d,\sigma}(V)<\delta$ such that $-\Delta+V$ has spectrum $[0,\infty)$ and no continuous spectral component; positive spectrum is pure point.
- **Assumptions and setting:** Schrödinger operator on $\mathbb R^d$, $d\ge2$; the weighted integral is $\mathcal I_{d,\sigma}(V)=\int_{\mathbb R^d}|x|^{1-d+\sigma}|V(x)|^2\,dx$, with $0\le\sigma<1/3$.
- **Caveat:** This is an unrefereed preprint; its delicate multiscale construction has not been independently proof-checked here. The authors disclose extensive LLM assistance and state that they take responsibility for the mathematics.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Analysis & PDE; Mathematical physics

### 2. [Conway's thrackle conjecture: a new upper bound of $\frac43n$](https://arxiv.org/abs/2610.31589)
- **Abstract:** For a planar thrackle, where each pair of edges meets exactly once, the author proves that a thrackle on $n\ge4$ vertices has at most $\lfloor4(n-1)/3\rfloor$ edges, using a computer-assisted small-case result and a discharging argument.
- **Authors:** Dániel Gábor Simon
- **arXiv:** `2610.31589v1` (published 2026-10-22 17:23:50 UTC; categories: `math.CO`, `math.GN`, `math.GT`)
- **Evidence for ranking:** A concrete bound on a long-standing extremal conjecture, cross-listed in combinatorics and two geometry/topology categories. The introduction compares it with the previously cited $18(n-1)/13$ bound; the announced $4(n-1)/3$ bound is sharper. No independent expert discussion was found in the sources checked.
- **Claimed result:** The author proves $m\le\lfloor4(n-1)/3\rfloor$ for every thrackleable graph on $n\ge4$ vertices.
- **Assumptions and setting:** A thrackle is a plane graph drawing in which every pair of edges meets exactly once, either at a shared endpoint or a proper crossing; the theorem concerns finite simple graphs and $n\ge4$.
- **Caveat:** This improves but does not prove Conway's conjectured $m\le n$ bound. The discharging proof uses a computer-assisted verification for graphs with at most twelve vertices.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Combinatorics & discrete mathematics; Geometry & topology

### 3. [Positive sectional curvature on exotic spheres in infinitely many dimensions](https://arxiv.org/abs/2610.31528)
- **Abstract:** The author constructs exotic spheres admitting strictly positive sectional curvature in every dimension $n\equiv3\pmod4$, $n\ge11$, except the residue class $n\equiv255\pmod{256}$; finite computations also supply examples in that excluded class below $2^{16}$.
- **Authors:** Fernando Galaz-García
- **arXiv:** `2610.31528v1` (published 2026-10-22 16:36:34 UTC; categories: `math.DG`)
- **Evidence for ranking:** The result claims examples in infinitely many dimensions in a setting where the paper says known simply connected examples above dimension 24 were diffeomorphic to compact rank-one symmetric spaces. The paper links archived programs and outputs with a Zenodo DOI, giving a checkable computational artifact.
- **Claimed result:** For the specified quotients of special $S^3$–$S^3$ bundles, the author computes the Eells–Kuiper invariant and shows it is nonzero for a suitable map in each $b\ge2$ with $b\not\equiv63\pmod{64}$, yielding exotic positively curved spheres in dimensions $4b+3$; additional computations cover some excluded-residue dimensions below $2^{16}$.
- **Assumptions and setting:** Homotopy spheres $\Sigma_{\rho_b,\beta}$ of dimension $4b+3$, with the stated $S^3$ representation and equivariant map; positivity uses recent metric constructions for this family.
- **Caveat:** The general theorem leaves dimensions $n\equiv255\pmod{256}$ outside its proved range; only a finite range of those cases is supplied computationally. The construction also depends on prior positive-curvature metric results for the family.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Geometry & topology

### 4. [The Critical 2D KPZ Process](https://arxiv.org/abs/2610.31614)
- **Abstract:** The authors construct a non-Gaussian, distribution-valued critical two-dimensional KPZ process as a scaling limit of centered log partition functions for critical Gaussian directed polymers and via a renormalized Cole–Hopf transform of the critical stochastic heat flow.
- **Authors:** Quentin Berger, Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, et al.
- **arXiv:** `2610.31614v1` (published 2026-10-22 17:40:36 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** It connects a singular stochastic PDE to directed polymers and a stochastic heat flow, and is cross-listed in probability and mathematical physics. A public Lean 4 formalization project cites the preprint; that is a checkable follow-on artifact, not a verification of the analytic proof.
- **Claimed result:** The authors claim convergence in law to a nontrivial critical KPZ process, measurable from the critical stochastic heat flow after renormalized Cole–Hopf transformation; they report non-Gaussianity, logarithmic-logarithmic covariance blow-up near the diagonal, and Gaussian fluctuations after averaging on shrinking scales.
- **Assumptions and setting:** Two-dimensional critical KPZ, interpreted through centered log partition functions of Gaussian directed polymers and a mollified stochastic heat flow; the paper's specific renormalization and scaling are essential.
- **Caveat:** This is an 84-page preprint whose authors report extensive generative-AI interactions in developing the results; the mathematical claims require specialist scrutiny and are not independently validated here.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Probability & statistics; Mathematical physics

### 5. [Hydrodynamic and Stochastic Limits of Space-Time Hawkes Processes](https://arxiv.org/abs/2610.31604)
- **Abstract:** For critical and nearly critical space-time Hawkes processes started from a Poisson field of past events, the authors identify high-density deterministic, threshold stochastic, and sparse locally vanishing limits, with altered fractional-diffusion behavior for heavy-tailed delays.
- **Authors:** Fuqing Gao, Yingli Wang, Lingjiong Zhu
- **arXiv:** `2610.31604v1` (published 2026-10-22 17:35:45 UTC; categories: `math.PR`)
- **Evidence for ranking:** The abstract gives a three-regime limit theorem and distinguishes finite-mean from heavy-tailed reproduction delays; this is a substantial probability result, though it has no cross-list or independent attention signal in the sources checked.
- **Claimed result:** The authors derive deterministic diffusion, measure-valued branching limits, and locally vanishing event measures according to the initial Poisson density. Heavy-tailed delays produce fractional diffusion and a superprocess occupation-measure limit with memory terms.
- **Assumptions and setting:** Critical or nearly critical space-time Hawkes processes with a prescribed Poisson past; initial profiles may be bounded with infinite total mass, and the limit depends on the reproduction-delay tail and matched observation scales.
- **Caveat:** The limit descriptions are tied to these initial conditions and scaling regimes; they do not directly characterize arbitrary Hawkes processes or delay laws.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Probability & statistics

### 6. [A semiampleness result for hyperkähler fourfolds and smoothings of Lagrangian subvarieties](https://arxiv.org/abs/2610.31497)
- **Abstract:** For a smooth hyperkähler fourfold whose Picard group is generated by a nef, nontrivial, non-big line bundle of nonnegative Kodaira dimension, the authors prove that a positive multiple defines a Lagrangian fibration.
- **Authors:** Andreas Höring, Vladimir Lazić, Christian Lehn
- **arXiv:** `2610.31497v1` (published 2026-10-22 16:14:52 UTC; categories: `math.AG`, `math.CV`, `math.DG`)
- **Evidence for ranking:** A substantive semiampleness/fibration theorem cross-listed in algebraic, complex and differential geometry; the authors also identify unobstructedness and smoothing results as independently useful tools. No independent expert discussion was found in the sources checked.
- **Claimed result:** If $X$ is a smooth hyperkähler fourfold, $\operatorname{Pic}(X)=\mathbb Z[L]$, and $L$ is nef, nontrivial, not big, with $\kappa(L)\ge0$, then some positive multiple of $L$ defines a Lagrangian fibration.
- **Assumptions and setting:** Smooth hyperkähler fourfold; Picard group generated by $L$; $L$ nef, nontrivial, not big, and of nonnegative Kodaira dimension.
- **Caveat:** Both the Picard-rank-one condition and $\kappa(L)\ge0$ are hypotheses; the result is not a general semiampleness theorem for higher-dimensional hyperkähler manifolds.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Geometry & topology

### 7. [Deep holes of full-length Reed--Solomon codes: uniform bounds and exact classifications](https://arxiv.org/abs/2610.31460)
- **Abstract:** For full-length Reed–Solomon codes, the author classifies all deep holes at interpolation degrees $k+m$ over every finite field for $m=3,4,5,6,7$, and proves further uniform bounds and large-field classifications for all $m\ge3$.
- **Authors:** Xiang Fan
- **arXiv:** `2610.31460v1` (published 2026-10-22 15:53:11 UTC; categories: `cs.IT`, `math.CO`, `math.NT`)
- **Evidence for ranking:** Exact classifications across five excess degrees plus uniform bounds, with cross-listing across information theory, combinatorics and number theory. The author reports finite computations with certificates and deterministic verification programs.
- **Claimed result:** For $m=3,\ldots,7$, no deep holes occur for odd $m$; for $m=4,6$, the only exceptions are respectively the Segre sextic and Frobenius-power families, only in dimension two over characteristic-two fields. General $m\ge3$ results impose explicit field-size bounds.
- **Assumptions and setting:** Full-length $\operatorname{RS}_q(k)$ over $\mathbb F_q$, with interpolation degree $k+m$; unconditional classification is for $m=3,\ldots,7$, while the broader results require the stated lower bounds on $q$.
- **Caveat:** The unconditional classification does not cover all $m$; the paper's uniform large-field hypotheses and remaining finite cases matter, and the author notes independent parallel work.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 8. [Improved Bounds for the Entropic Central Limit Theorem in the Log-Concave Case](https://arxiv.org/abs/2610.31493)
- **Abstract:** For an isotropic log-concave probability measure $\mu$ on $\mathbb R^d$, the author proves an entropic central-limit bound of order $1/n$ whose dimension dependence is the minimum of a polylogarithmic term and $d$.
- **Authors:** Tom Maitre (LMA (Poitiers))
- **arXiv:** `2610.31493v1` (published 2026-10-22 16:13:24 UTC; categories: `cs.IT`, `math.PR`)
- **Evidence for ranking:** The stated bound replaces a polynomial dimension dependence in the previous best bound with polylogarithmic dependence in one regime, and the paper bridges probability with information theory. No independent expert discussion was found in the sources checked.
- **Claimed result:** The author proves $H(\mu^n\mid\gamma)\le \frac{C}{n}\min\{1+\log(ed)^2H(\mu\mid\gamma),d\}$, where $\mu^n$ is the law of the normalized sum of $n$ independent samples from $\mu$ and $\gamma$ is the standard Gaussian.
- **Assumptions and setting:** Isotropic log-concave probability measure on $\mathbb R^d$; relative entropy to the standard Gaussian, for normalized sums of independent identically distributed vectors.
- **Caveat:** The result assumes log-concavity and isotropy; the abstract does not claim the same dimension improvement for arbitrary input distributions.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Probability & statistics; Machine learning theory

## Trending Research Themes

- **Counterexamples and sharpened boundaries:** Becker–Yang claim to overturn Simon's spectral conjecture, while Simon narrows the thrackle edge bound without settling Conway's conjecture. These are isolated developments, not evidence of a broad field-wide turn.
- **Probability across criticality and scaling:** The Critical 2D KPZ Process and the space-time Hawkes paper both build limit objects from interacting random systems, but their models and techniques differ. Maitre's entropic CLT result adds a distinct information-theoretic measure of convergence to Gaussian behavior.
- **Classification through geometric or algebraic invariants:** Galaz-García uses the Eells–Kuiper invariant to distinguish exotic spheres; Fan classifies code-theoretic deep holes using finite-field structure; Höring–Lazić–Lehn derive a fibration from positivity and Picard-group hypotheses. These are parallel styles of reducing existence questions to computable or structural criteria, not a shared method.
- **Bridges are concrete rather than evidence of a trend by themselves:** The selected papers cross-list spectral theory with mathematical physics (Becker–Yang), probability with mathematical physics (KPZ), information theory with combinatorics and number theory (Reed–Solomon), and probability with information theory (entropic CLT).

## Open Problems and Research Directions

- **Open problem (explicitly unresolved):** Conway's conjectured $m\le n$ edge bound remains open after the new $\lfloor4(n-1)/3\rfloor$ estimate. A natural follow-up is to reduce the constant toward $1$ and understand whether the small-case computer verification can be replaced by a more structural argument (Simon, [2610.31589](https://arxiv.org/abs/2610.31589)).
- **Open scope (from the theorem's stated range):** Becker–Yang give counterexamples for $0\le\sigma<1/3$. A concrete synthesis direction is to test what additional decay, sign, or regularity assumptions could restore absolutely continuous spectrum, particularly at or beyond the endpoint not covered by their construction (Becker–Yang, [2610.31637](https://arxiv.org/abs/2610.31637)).
- **Open scope (from the stated exception):** The exotic-sphere result leaves dimensions $n\equiv255\pmod{256}$ outside its general theorem, with only finite computational examples there. Extending the invariant calculation or metric construction to all such dimensions would test that boundary (Galaz-García, [2610.31528](https://arxiv.org/abs/2610.31528)).
- **Open scope (author-stated classification range):** Fan's unconditional deep-hole classification stops at $m=7$; the all-$m$ conclusions require field-size bounds. Extending the exact range or tightening those bounds is a direct next step, with independent parallel work accounted for (Fan, [2610.31460](https://arxiv.org/abs/2610.31460)).
- **Research direction (synthesis):** Test whether the KPZ scaling limit and its covariance behavior persist for other disorder distributions or nearby critical scalings; the present preprint treats the specified Gaussian-polymer setting (Berger et al., [2610.31614](https://arxiv.org/abs/2610.31614)).
- **Open scope (theorem hypotheses):** The hyperkähler fibration theorem assumes a fourfold and a Picard group generated by $L$. Studying which parts survive at higher Picard rank or in higher dimensions would probe the role of those assumptions (Höring, Lazić & Lehn, [2610.31497](https://arxiv.org/abs/2610.31497)).

## Takeaway

The batch's strongest signals are precise theorem claims with narrow, consequential hypotheses: a spectral counterexample, a tighter classical extremal bound, new positive-curvature examples, and limit/classification results across probability and geometry. The ordering is qualitative, not a popularity measurement, and several of the most striking claims are fresh preprints that still need expert scrutiny.

## Method and sources

- **Window:** daily; selected announcement batch 2026-10-23, with exact window 2026-10-23 through 2026-10-23. The run was on 2026-10-26; the Mathematics recent listing showed Friday 23 October as its latest batch, so this is a prior batch.
- **Snapshot:** 2026-10-26 01:27:17 UTC.
- **Coverage:** Traversed the complete arXiv Mathematics recent listing for 2026-10-23; arXiv displayed 392 entries for that date. The eight selected entries' abstract pages were checked for version, UTC submission timestamp, authors, categories and abstracts. HTML introductions/main-result text was inspected for the top three (2610.31637, 2610.31589, 2610.31528); no proof was independently checked.
- **Selection and ranking:** arXiv supplies no official trending chart. The Semantic Scholar citation lookup was throttled, and web searches found little independent expert discussion for this very new batch; therefore the list is explicitly ranked as notable recent papers, using paper-specific theorem claims, cross-listing, reproducible artifacts and the limited external visibility signals available. No numeric score or citation totals are asserted.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent); the individual arXiv abstract and HTML pages linked above; [MathWorld entry on Simon's $L^2$ conjecture](https://mathworld.wolfram.com/SimonsL2Conjecture.html); [math.SP announcement on X](https://x.com/mathSPb/status/2113505725603340388); [Lean 4 formalization project citing the KPZ preprint](https://github.com/scottnarmstrong/Critical2DKPZ); [Zenodo archive for the exotic-sphere computations](https://doi.org/10.5281/zenodo.23571372). A structured JSON sidecar accompanies this report.
