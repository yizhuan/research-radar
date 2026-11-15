Headline — Mathematics, latest announcement batch Friday 13 November 2026: six notable papers selected from the 774-entry math listing. This Sunday, 15 November, has no newer batch in the recent listing. The strongest pattern is rigorous constructions/counterexamples alongside stochastic scaling-limit results. Agenda: Ising interfaces, nonlocal PDEs, certified geometry, then additive combinatorics, nonlinear waves and field theory. This is an inferred significance-weighted selection, not an official arXiv trending chart; these same-batch papers are too new for citation evidence to support a popularity ranking.

## Top papers (ranked)

### 1. [GFF for 3D Ising interfaces in three moves of Tetris](https://arxiv.org/abs/2611.16943)
- **Abstract:** The authors prove that, at sufficiently low temperature and positive interface slopes, the three-dimensional Ising interface has a Gaussian free field scaling limit, using mappings to SOS, half-monotone SOS and dimer surfaces.
- **Authors:** Benoît Laslier, Eyal Lubetzky
- **arXiv:** `2611.16943v1` (published 2026-11-12 15:23:54 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** The paper states a scaling-limit theorem for four related surface/interface models and an improved renormalization result for interacting dimers; its probability and mathematical-physics cross-listing reflects the bridge in the work. Placement is based on scope and concreteness, not measured readership.
- **Claimed result:** The authors' Theorem 1 proves local gradient convergence and convergence of centered rescaled height fields (modulo constants) to a linearly transformed GFF for the 3D Ising interface, SOS, HMSOS and bubble-free Ising interface.
- **Assumptions and setting:** Tilted tori with both limiting slopes positive; inverse temperature `β ≥ β₀`. The limiting amplitude and linear map depend on temperature and slope.
- **Caveat:** The authors state that extending the 3D Ising conclusion to every `β > βc` remains open; degenerate slopes such as `(θ₁, 0)` also remain unresolved, including the order of the positive-temperature height variance.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

### 2. [The coercivity conjecture for nonlocal energies](https://arxiv.org/abs/2611.16682)
- **Abstract:** The authors show that uniform ellipticity alone does not ensure fractional Sobolev coercivity for broad classes of symmetric nonlocal kernels, while identifying cancellation conditions that recover coercivity and regularity in important cases.
- **Authors:** Linus Behn, Roberto Colombo, Xavier Fernández-Real, Florian Grube, Harsh Prasad, Xavier Ros-Oton
- **arXiv:** `2611.16682v1` (published 2026-11-12 11:56:48 UTC; categories: `math.AP`)
- **Evidence for ranking:** The authors give counterexamples to a named coercivity conjecture and a positive annular-cancellation criterion, with applications to variable stable kernels and non-cutoff Boltzmann kernels. This combines a sharp negative result with a structural positive theory; placement is significance-based, not an attention measure.
- **Claimed result:** Theorem 1.1 gives failure of a uniform `H^s` coercivity bound when `n > 2s`, including bounded discontinuous weak solutions. The paper also proves coercivity for specified kernel classes under extra cancellation/symmetry assumptions, and for `n = 1`, `s > 1/2` under its stated hypotheses.
- **Assumptions and setting:** Symmetric measurable nonlocal kernels of order `2s`, with `0 < s < 1` and the paper's uniform ellipticity/moment bounds. Positive results require additional structure or special kernel classes.
- **Caveat:** Uniform ellipticity is not enough in the counterexample regime; positive conclusions depend on the extra structure and hypotheses of the relevant theorems.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Analysis & PDE

### 3. [A constructive computer-assisted existence proof for a Calabi--Yau metric](https://arxiv.org/abs/2611.16908)
- **Abstract:** The authors rigorously construct a Ricci-flat Kähler metric on the Fermat quartic using numerical approximation, a fixed-point argument and verified numerical bounds, and provide an explicit analytic approximation.
- **Authors:** Michael R. Douglas, Javier Gómez-Serrano, Fabian Lehmann, Daniel Platt, Yidi Qi
- **arXiv:** `2611.16908v1` (published 2026-11-12 15:02:05 UTC; categories: `math.DG`, `hep-th`)
- **Evidence for ranking:** A constructive, computer-assisted existence result in differential geometry with a high-energy-theory cross-list; Theorem 1.1 supplies explicit norm bounds for the correction to the computed metric. This unusual proof artifact supports inclusion, not popularity.
- **Claimed result:** The authors' Theorem 1.1 proves that a specified approximate Kähler form on the Fermat quartic can be corrected to a Calabi–Yau metric, with `‖u‖𝒳 ≤ 1.551 × 10⁻⁴` and `‖i∂∂̄u‖C⁰ ≤ 1.553 × 10⁻⁴` in the stated norms.
- **Assumptions and setting:** The certified construction concerns the Fermat quartic and the explicitly computed Kähler form/metric in the paper; verified bounds support the fixed-point argument.
- **Caveat:** The proof constructs this particular metric; adapting the rigorous numerical bounds and analysis to other manifolds remains a computational and mathematical task discussed by the authors.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Geometry & topology; Mathematical physics

### 4. [Forbidden subset sums in a linear range: an inverse theorem and the Erdős-Graham irregularity problem](https://arxiv.org/abs/2611.17205)
- **Abstract:** The authors determine the extremal subset-sum function for `c ≥ 1`, prove multiple limit points for `0 < c < 1` (with an exact answer at `c = 1/2`), and establish an inverse theorem for dense sets with a prescribed subset sum.
- **Authors:** Mateo Matijasevick
- **arXiv:** `2611.17205v1` (published 2026-11-12 18:05:45 UTC; categories: `math.CO`, `math.NT`)
- **Evidence for ranking:** The abstract reports explicit results on Erdős Problem #361 and an inverse theorem; selected results are machine-checked in Lean 4, and the paper is cross-listed in combinatorics and number theory. These are mathematical/formalization signals, not evidence of popularity.
- **Claimed result:** For `c ≥ 1`, `f_c(n) = ⌊cn⌋ − ⌈n/2⌉`; for `0 < c < 1`, the authors prove `limsup f_c(n)/n = c/2` and nonconvergence, with exactly `{1/6, 1/4}` as limit points when `c = 1/2`. Their inverse theorem says that, for `q` the least positive integer not dividing `s`, `|A| ≥ E/q + εT` forces a subset of `A ⊆ {1,…,E}` summing to `sT` for sufficiently large `T` and `2^(q−2)E ≤ sT`.
- **Assumptions and setting:** `f_c(n)` maximizes the size of a subset of `{1,…,⌊cn⌋}` avoiding `n` as a distinct-element subset sum. The inverse theorem has the stated size/range condition and sufficiently large `T`; only specified portions of the results are reported as Lean-formalized.
- **Caveat:** For general `0 < c < 1`, the abstract gives multiple limit points and formulas along specified arithmetic subsequences, not every limit point for every `c`.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 5. [A counterexample to fixed-profile soliton resolution for the three-dimensional quintic wave equation](https://arxiv.org/abs/2611.17291)
- **Abstract:** For the three-dimensional focusing energy-critical wave equation, the authors construct a bounded global solution whose core approaches distinct stationary profiles along different limits, contradicting a fixed-profile soliton-resolution description.
- **Authors:** Xuwen Chen, Justin Holmer, Shunlin Shen
- **arXiv:** `2611.17291v1` (published 2026-11-12 18:53:35 UTC; categories: `math.AP`)
- **Evidence for ranking:** The abstract states a concrete counterexample to a fixed-profile formulation of a major asymptotic principle and reports a computer-assisted certificate for the stationary state and its complete odd energy kernel. It is a high-specificity result, though not cross-listed.
- **Claimed result:** The authors construct a bounded forward-global solution asymptotic to a varying stationary profile plus one free wave; two limits of its core lie in distinct similarity orbits, ruling out the competing fixed-profile list described in the paper.
- **Assumptions and setting:** Three-dimensional focusing energy-critical (quintic) wave equation; the construction starts arbitrarily close to a particular sign-changing stationary state and uses a certified construction.
- **Caveat:** The result refutes the specified fixed-profile formulation through one constructed solution; it does not settle every broader or suitably generalized version of soliton resolution.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Analysis & PDE

### 6. [Mass gap for the fractional $Φ^4_2$ model](https://arxiv.org/abs/2611.17119)
- **Abstract:** The authors introduce a stochastic-quantisation method for mass gaps in a high-temperature regime and apply it to prove exponential spatial-correlation decay for the fractional `Φ⁴` model on the plane in the Wick-ordering regime.
- **Authors:** Paweł Duch, Massimiliano Gubinelli
- **arXiv:** `2611.17119v1` (published 2026-11-12 17:11:56 UTC; categories: `math.PR`, `math-ph`)
- **Evidence for ranking:** This probability/mathematical-physics cross-listed paper gives a correlation-decay theorem and a proof strategy based on stochastic quantisation, perturbation propagation and a variational formula. Its placement follows the stated result and field bridge, not citation data.
- **Claimed result:** The authors establish exponential decay of spatial correlations for the fractional `Φ⁴` model on the plane in the Wick-ordering regime, using an auxiliary random walk to control propagation and dissipative estimates plus the Boué–Dupuis formula to control the renormalised nonlinearity.
- **Assumptions and setting:** Euclidean quantum field theory in a high-temperature regime; the application is the fractional `Φ⁴` model on the plane in the Wick-ordering regime.
- **Caveat:** The abstract's application is restricted to that model and regime and gives no quantitative parameter range or mass-gap result for all couplings or temperatures.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Probability & statistics; Mathematical physics

## Trending Research Themes

- **Proof and computation:** Verified numerical bounds certify the Fermat-quartic metric (paper 3), a computer-assisted certificate supports the stationary state in the wave-equation construction (paper 5), and Lean formalizes selected subset-sum results (paper 4). These are distinct validation strategies, not one shared method or evidence of a field-wide shift.
- **Stochastic large-scale behavior:** The Ising-interface paper proves a GFF scaling limit under low-temperature, positive-slope hypotheses (paper 1), while the fractional `Φ⁴` work proves exponential correlation decay in a Wick-ordering regime (paper 6). Different models and analytic machinery.
- **PDE theorem boundaries:** The nonlocal-energy paper identifies failure of ellipticity-only coercivity and recovery under additional structure (paper 2); the wave-equation paper breaks a fixed-profile asymptotic description (paper 5). The shared signal is sharpening theorem boundaries, not a shared technique.

## Open Problems and Research Directions

- **Author-stated — Ising interfaces:** Extend the 3D Ising GFF conclusion from sufficiently large `β` to every `β > βc` at each fixed positive slope. The authors also ask for the fluctuation scale and limit at degenerate slopes such as `(θ₁, 0)`; even the order of the positive-temperature variance is open. (Paper 1.)
- **Author-stated question and proposed follow-up — nonlocal coercivity:** The authors ask what additional kernel structure restores coercivity and whether it occurs in motivating classes. A concrete follow-up is to test the critical boundary `n = 2s` and compare cancellation conditions there with regimes already settled by the paper; the boundary proposal is synthesis. (Paper 2.)
- **Author-discussed extension — certified geometry:** Apply the verified-numerics/fixed-point pipeline to other Calabi–Yau manifolds and determine which geometric bounds dominate computation; the authors discuss computational issues in extending the method. (Paper 3.)
- **Proposed direction — subset sums:** For each `0 < c < 1`, seek a complete description of the limit-point set of `f_c(n)/n`, beyond the subsequences and special `c` values in the preprint. (Paper 4.)
- **Proposed direction — soliton resolution:** Determine which non-fixed-profile asymptotic formulations remain viable in view of the constructed solution, and whether related mechanisms occur for other stationary states or dimensions. (Paper 5.)
- **Proposed direction — mass gap:** Test how far the stochastic-quantisation argument extends beyond the fractional `Φ⁴` plane model and the stated Wick-ordering/high-temperature regime. (Paper 6.)

Takeaway — This batch’s clearest mathematical signals are sharply delimited theorems: a GFF limit for tilted Ising interfaces, counterexamples and recovery criteria for nonlocal coercivity, and a computer-certified metric construction. Other entries address a named subset-sum problem and limits of fixed-profile wave asymptotics. These are promising preprints, but a same-batch snapshot cannot establish popularity or independent validation of the proofs.

Method and sources — Daily window: announcement batch 2026-11-13 through 2026-11-13; arXiv recent listing labels the batch Friday, 13 November. The selected papers' v1 submissions are timestamped 2026-11-12 UTC. Since the run is Sunday, 15 November 2026, this is the latest prior batch, not a Sunday batch. Snapshot: 2026-11-15 01:25:58 UTC. Scope: arXiv Mathematics (`math`), all subfields; listing showed 774 batch entries. Six abstracts and latest v1 metadata were checked on arXiv; introductions/main results were inspected for the first three. arXiv supplies no official trending chart. As these are new v1 submissions, citation history is too short for meaningful momentum comparisons; a Semantic Scholar citation-count request was rate-limited, so citation and influential-citation metrics are not used. Ordering is a transparent significance/cross-field selection, not measured popularity; independent attention evidence was sparse. Sources: https://arxiv.org/list/math/recent; linked arXiv abstracts and v1 HTML pages; exact-title searches for independent discussion.
