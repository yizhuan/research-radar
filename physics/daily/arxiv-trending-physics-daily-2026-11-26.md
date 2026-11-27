# arXiv physics daily — 26 November 2026 announcement batch

Five notable papers from the latest available arXiv Physics batch span mathematical physics, quantum many-body dynamics, stochastic ecology, and computational relativity. Brief agenda: a spin-DFT error bound, a knot-theory/topological-recursion proof, demographic extinction, quantum-scar preparation, and a PINN method for photon orbits. This is an editorial shortlist, not a measured popularity ranking: arXiv has no official trending chart, the supplied current-window signals contain no candidate-level scores, and very recent papers have limited citation evidence.

## Top papers (ranked)

### 1. [The transverse spin-gradient approximation in noncollinear spin density functional theory](https://arxiv.org/abs/2611.34301)
- **Abstract:** The authors prove a quantitative error bound for a fixed-axis transverse spin-gradient approximation to noncollinear spin density functional theory using a spin-spiral reference.
- **Authors:** Mihály A. Csirik
- **arXiv:** `2611.34301v1` (published 2026-11-25 12:53:36 UTC; categories: `math-ph`, `cond-mat.mtrl-sci`, `cond-mat.quant-gas`, `cond-mat.stat-mech`, `quant-ph`)
- **Evidence for ranking:** No candidate score was present in the supplied signal file; included for a rigorous quantitative bound and cross-listing across mathematical physics, condensed matter, and quantum physics.
- **Claimed result:** Csirik proves an O(N^(5/6)) error for an energy of order N under stated slow-variation and regularity assumptions, and recovers the noncollinear local spin-density approximation when the spiral phase is set to zero.
- **Evidence type:** Theoretical; an analytic bound for the thermodynamic-limit electron gas with a spin-spiral-wave local reference.
- **Caveat:** The bound is for a fixed-axis variant and depends on smooth, slowly varying rotating-frame density and local wavevector; it is not an empirical accuracy benchmark for general materials.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Condensed matter & materials

### 2. [Colored Jones polynomial of figure eight knot and non-perturbative topological recursion](https://arxiv.org/abs/2611.34110)
- **Abstract:** The authors prove that the asymptotic expansion of the figure-eight knot's colored Jones polynomial is connected to non-perturbative topological recursion on its elliptic spectral curve.
- **Authors:** Alexander Hock, Sergey Shadrin
- **arXiv:** `2611.34110v1` (published 2026-11-25 10:13:46 UTC; categories: `math-ph`, `hep-th`, `math.AG`, `math.GT`, `nlin.SI`)
- **Evidence for ranking:** No candidate score was present; included for a detailed proof linking a knot invariant to topological recursion and cross-listing into high-energy theory and mathematical physics.
- **Claimed result:** Hock and Shadrin identify the asymptotic Jones-polynomial wave function with recurrence and normalized non-perturbative wave functions for the figure-eight-knot spectral curve, proving the proposed connection in this case.
- **Evidence type:** Theoretical; analysis of the colored-Jones recurrence, spectral curve, and topological-recursion equations.
- **Caveat:** The proof is specific to the figure-eight knot and the colored Jones polynomial; extension to other knots is a follow-up question, not established here.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Particle, nuclear & high-energy physics

### 3. [Noise-induced Extinction in Hierarchical Food Webs](https://arxiv.org/abs/2611.33569)
- **Abstract:** The authors develop a large-deviation account of demographic-noise-driven extinctions in hierarchical food webs, deriving an extinction network and recursion for mean extinction times.
- **Authors:** Varun Nevash, Eric Forgoston, M. Ani Hsieh
- **arXiv:** `2611.33569v1` (published 2026-11-25 00:32:11 UTC; categories: `q-bio.PE`, `cond-mat.stat-mech`, `math.DS`, `math.PR`, `nlin.AO`)
- **Evidence for ranking:** No candidate score was present; included for its explicit large-deviation treatment of rare events, cross-listing with statistical mechanics, and stochastic simulation check of the three-species example.
- **Claimed result:** Under unit conversion efficiency and self-limitation only at the basal species, the authors show coexistence is the sole stable mean-field state and derive a 3^(N−1)-transition extinction network; the three-species instanton route is checked against stochastic simulations.
- **Evidence type:** Theoretical and computational; WKB analysis of the master equation, numerical instantons for a three-species omnivory model, and stochastic simulations.
- **Caveat:** General results rely on an idealized hierarchical interaction structure and restrictive ecological assumptions; direct simulation checks cover the three-species example, not arbitrary food webs.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Biophysics & soft matter

### 4. [Unified preparation of exact and asymptotic quantum many-body scars from Dicke states](https://arxiv.org/abs/2611.33987)
- **Abstract:** The authors propose a unified algorithm that prepares exact and asymptotic quantum many-body scar states by mapping them to Dicke states and ferromagnetic-chain magnons.
- **Authors:** Yuki Asari, Masaya Kunimi, Tetsuro Nikuni
- **arXiv:** `2611.33987v1` (published 2026-11-25 08:44:47 UTC; categories: `quant-ph`, `cond-mat.quant-gas`, `cond-mat.stat-mech`, `cond-mat.str-el`)
- **Evidence for ranking:** No candidate score was present; included for a concrete state-preparation algorithm and resource argument connecting quantum information with condensed-matter scar models.
- **Claimed result:** Asari, Kunimi, and Nikuni show that at fixed target fidelity the block-encoding success probability has a positive lower bound independent of system size and scar index, so only a constant number of amplitude-amplification rounds is needed.
- **Evidence type:** Theoretical; quantum-algorithm construction and resource analysis for three scar models.
- **Caveat:** This is an algorithmic proposal for idealized programmable simulators; the abstract does not demonstrate preparation on hardware or quantify noise and gate costs.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Quantum information; Condensed matter & materials

### 5. [PINN-Slicer: Exploiting Rotational Symmetry to Solve the Photon Orbit Equation Around a Black Hole](https://arxiv.org/abs/2611.33953)
- **Abstract:** The authors introduce a slice-by-slice physics-informed neural-network method for long-domain autonomous ODEs and demonstrate it on the photon-orbit equation around a black hole.
- **Authors:** Claire David, Tlotlo Oepeng, Harrison B. Prosper
- **arXiv:** `2611.33953v1` (published 2026-11-25 08:13:49 UTC; categories: `cs.CL`, `astro-ph.IM`, `gr-qc`, `physics.comp-ph`)
- **Evidence for ranking:** No candidate score was present; included for a quantified numerical benchmark, code availability noted on the arXiv record, and cross-listing into general relativity and computational physics.
- **Claimed result:** David, Oepeng, and Prosper report pointwise RMSE below 10^-3 in inverse radius relative to a finite-difference reference, with one trained network generalizing across initial conditions in its training range.
- **Evidence type:** Computational; a PINN benchmarked against a finite-difference solution of the Schwarzschild photon-orbit ODE.
- **Caveat:** Validation is one ODE problem and uses a numerical reference solution; generalization beyond the trained initial-condition range and to other physical systems remains untested.
- **Announcement type:** new submission, 2026-11-26 announcement batch
- **Themes:** Computational & data methods; Cosmology & gravitation

## Trending Research Themes

- **Formal methods crossing physics boundaries:** The spin-DFT bound (2611.34301) and the figure-eight recursion proof (2611.34110) are mathematical results cross-listed into physics, while the food-web paper (2611.33569) applies large-deviation theory to population dynamics. This is a small shortlist, not a corpus-frequency estimate.
- **Quantum resources and non-equilibrium structure:** The scar-state preparation algorithm (2611.33987) focuses on efficient preparation of nonergodic states; it remains theoretical, unlike an experimental hardware demonstration.
- **Scientific computing for long-time or rare-event questions:** PINN-Slicer (2611.33953) targets long-domain ODE integration; the food-web work (2611.33569) derives rare extinction paths and checks a small module by stochastic simulation. The methods address different systems and are not independent confirmation of one phenomenon.

## Open Problems and Research Directions

- **Open problem (author-stated assumptions):** The spin-DFT error estimate assumes slow variation and a fixed spin axis (2611.34301). **Research direction (synthesis):** benchmark it against established calculations on noncollinear materials where magnetization rotates rapidly or the preferred axis varies.
- **Open problem (author-stated scope):** The topological-recursion proof is for the figure-eight knot; the paper discusses extension beyond that case (2611.34110). **Research direction (synthesis):** test the construction on other hyperbolic knots and determine when recursion descends to the relevant quotient curve.
- **Open problem (author-stated model limits):** The food-web theory assumes unit conversion efficiency and basal-only self-limitation; detailed instanton checks cover a three-species module (2611.33569). **Research direction (synthesis):** relax those assumptions and compare extinction-time distributions with stochastic simulations and calibrated interaction data.
- **Open problem (evidence gap):** The scar algorithm and PINN-Slicer are not demonstrated on physical hardware or across a broad set of systems (2611.33987, 2611.33953). **Research direction (synthesis):** estimate gate-depth/noise tolerance for the quantum algorithm and test PINN-Slicer on additional physical ODEs and out-of-range initial conditions.

## Takeaway

The batch combines rigorous mathematical results with algorithmic methods for many-body quantum states, ecological rare events, and relativistic trajectories. The claims are promising but conditional: most need broader model tests, hardware realization, or application to physical systems beyond the proof or benchmark cases.

## Method and sources

- **Window:** daily; the latest arXiv new-listing page available at the snapshot was dated Thursday, 2026-11-26. Its batch corresponds to the 2026-11-24 19:00:00–2026-11-25 19:00:00 UTC submission window and was announced 2026-11-26 at 01:00 UTC. The current-window signals file covers 2026-11-25 19:00:00–2026-11-26 19:00:00 UTC, with announcement time 2026-11-27 01:00:00 UTC; it had no arXiv candidates, so the prior available batch is used. Snapshot: 2026-11-27 03:22 UTC.
- **Archive coverage:** checked the new-listing pages for `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`; the latest page date was 2026-11-26. Cross-listed papers were treated as one work.
- **Signal evidence:** supplied file `/home/yizhuan/.research/physics/daily/arxiv-trending-physics-daily-2026-11-27.signals.json` reports `pool_size: 0`, `with_attention: 0`, and an empty `candidates` array. Source statuses/counts are arXiv `ok` (0), Hugging Face `ok` (126), Hacker News `ok` (16), arXiv lookup `ok` (141), and Semantic Scholar `ok` (0). Thus no paper-level score or attention values were available to rank the selected records. A zero score would not mean a paper is unimportant; in this file there are no candidate scores at all. No source is marked `error`.
- **Selection and verification:** this is an editorial shortlist, not a popularity ordering; selection emphasizes specific physical results, evidence type, model scope, and physics cross-listing. All five arXiv abstract pages and version histories were verified. Full-text HTML for the first three papers was inspected for introduction, methods, results, and caveats. No prior-window trend comparison is made.
- **Sources:** [arXiv 2611.34301](https://arxiv.org/abs/2611.34301), [2611.34110](https://arxiv.org/abs/2611.34110), [2611.33569](https://arxiv.org/abs/2611.33569), [2611.33987](https://arxiv.org/abs/2611.33987), [2611.33953](https://arxiv.org/abs/2611.33953); listings: [physics](https://arxiv.org/list/physics/new), [astro-ph](https://arxiv.org/list/astro-ph/new), [cond-mat](https://arxiv.org/list/cond-mat/new), [gr-qc](https://arxiv.org/list/gr-qc/new), [hep-ex](https://arxiv.org/list/hep-ex/new), [hep-lat](https://arxiv.org/list/hep-lat/new), [hep-ph](https://arxiv.org/list/hep-ph/new), [hep-th](https://arxiv.org/list/hep-th/new), [nucl-ex](https://arxiv.org/list/nucl-ex/new), [nucl-th](https://arxiv.org/list/nucl-th/new), and [quant-ph](https://arxiv.org/list/quant-ph/new).
