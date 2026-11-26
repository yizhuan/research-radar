# arXiv physics daily — 2026-11-26 announcement batch

Nine notable recent papers from today's batch lean toward rigorous theoretical tools, quantum dynamics, and measurement design. Brief agenda: a new spin-DFT error bound, a knot-theory/topological-recursion proof, rare extinction dynamics, quantum algorithms and sensing, and two astrophysical instrument concepts. This is an inferred ordering, not an official arXiv trending chart; the signal file contains no measured engagement for these papers, and citation evidence is limited because Semantic Scholar was unavailable.

## Top papers (ranked)

### 1. [The transverse spin-gradient approximation in noncollinear spin density functional theory](https://arxiv.org/abs/2611.34301)
- **Abstract:** The authors prove a quantitative error bound for a fixed-axis transverse spin-gradient approximation to noncollinear spin density functional theory using a spin-spiral reference.
- **Authors:** Mihály A. Csirik
- **arXiv:** `2611.34301v1` (published 2026-11-25 12:53:36 UTC; categories: `math-ph`, `cond-mat.mtrl-sci`, `cond-mat.quant-gas`, `cond-mat.stat-mech`, `quant-ph`)
- **Evidence for ranking:** Collector score 1.00, entirely from 4 cross-lists × 0.25; newest in the retained four-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** Csirik proves an O(N^(5/6)) error for an energy of order N under stated slow-variation and regularity assumptions, and recovers the noncollinear local spin-density approximation when the spiral phase is set to zero.
- **Evidence type:** Theoretical; an analytic bound for the thermodynamic-limit electron gas with a spin-spiral-wave local reference.
- **Caveat:** The bound is for a fixed-axis variant and depends on smooth, slowly varying rotating-frame density and local wavevector; it is not an empirical accuracy benchmark for general materials.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Condensed matter & materials

### 2. [Colored Jones polynomial of figure eight knot and non-perturbative topological recursion](https://arxiv.org/abs/2611.34110)
- **Abstract:** The authors prove that the asymptotic expansion of the figure-eight knot's colored Jones polynomial is connected to non-perturbative topological recursion on its elliptic spectral curve.
- **Authors:** Alexander Hock, Sergey Shadrin
- **arXiv:** `2611.34110v1` (published 2026-11-25 10:13:46 UTC; categories: `math-ph`, `hep-th`, `math.AG`, `math.GT`, `nlin.SI`)
- **Evidence for ranking:** Collector score 1.00, entirely from 4 cross-lists × 0.25; second by submission time in the retained four-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** Hock and Shadrin identify the asymptotic Jones-polynomial wave function with the recurrence and normalized non-perturbative wave functions for the figure-eight-knot spectral curve, proving the proposed connection in this case.
- **Evidence type:** Theoretical; analysis of the colored-Jones recurrence, spectral curve, and topological-recursion equations.
- **Caveat:** The proof is specific to the figure-eight knot and the colored Jones polynomial; extension to other knots is posed as a follow-up question, not established here.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Particle, nuclear & high-energy physics

### 3. [Noise-induced Extinction in Hierarchical Food Webs](https://arxiv.org/abs/2611.33569)
- **Abstract:** The authors develop a large-deviation account of demographic-noise-driven extinctions in hierarchical food webs, deriving an extinction network and recursion for mean extinction times.
- **Authors:** Varun Nevash, Eric Forgoston, M. Ani Hsieh
- **arXiv:** `2611.33569v1` (published 2026-11-25 00:32:11 UTC; categories: `q-bio.PE`, `cond-mat.stat-mech`, `math.DS`, `math.PR`, `nlin.AO`)
- **Evidence for ranking:** Collector score 1.00, entirely from 4 cross-lists × 0.25; third by submission time in the retained four-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** Under unit conversion efficiency and self-limitation only at the basal species, the authors show coexistence is the sole stable mean-field state and derive a 3^(N−1)-transition extinction network; their three-species instanton route is checked against stochastic simulations.
- **Evidence type:** Theoretical and computational; WKB analysis of the master equation, numerical instantons for a three-species omnivory model, and stochastic simulations.
- **Caveat:** The general results rely on an idealized hierarchical interaction structure and restrictive ecological assumptions; direct simulation checks cover the three-species example, not arbitrary food webs.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Biophysics & soft matter

### 4. [Unified preparation of exact and asymptotic quantum many-body scars from Dicke states](https://arxiv.org/abs/2611.33987)
- **Abstract:** The authors propose a unified algorithm that prepares exact and asymptotic quantum many-body scar states by mapping them to Dicke states and ferromagnetic-chain magnons.
- **Authors:** Yuki Asari, Masaya Kunimi, Tetsuro Nikuni
- **arXiv:** `2611.33987v1` (published 2026-11-25 08:44:47 UTC; categories: `quant-ph`, `cond-mat.quant-gas`, `cond-mat.stat-mech`, `cond-mat.str-el`)
- **Evidence for ranking:** Collector score 0.75, entirely from 3 cross-lists × 0.25; newest in the retained three-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** Asari, Kunimi, and Nikuni show that at fixed target fidelity the block-encoding success probability has a positive lower bound independent of system size and scar index, so only a constant number of amplitude-amplification rounds is needed.
- **Evidence type:** Theoretical; quantum-algorithm construction and resource analysis for three scar models.
- **Caveat:** This is an algorithmic proposal for idealized programmable simulators; the abstract does not demonstrate preparation on hardware or quantify noise and gate costs.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Quantum information; Condensed matter & materials

### 5. [PINN-Slicer: Exploiting Rotational Symmetry to Solve the Photon Orbit Equation Around a Black Hole](https://arxiv.org/abs/2611.33953)
- **Abstract:** The authors introduce a slice-by-slice physics-informed neural-network method for long-domain autonomous ODEs and demonstrate it on the photon-orbit equation around a black hole.
- **Authors:** Claire David, Tlotlo Oepeng, Harrison B. Prosper
- **arXiv:** `2611.33953v1` (published 2026-11-25 08:13:49 UTC; categories: `cs.CL`, `astro-ph.IM`, `gr-qc`, `physics.comp-ph`)
- **Evidence for ranking:** Collector score 0.75, entirely from 3 cross-lists × 0.25; second by submission time in the retained three-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** David, Oepeng, and Prosper report pointwise RMSE below 10^-3 in inverse radius relative to a finite-difference reference, with one trained network generalizing across initial conditions in its training range; the arXiv comment notes code availability and workshop acceptance.
- **Evidence type:** Computational; a PINN benchmarked against a finite-difference solution of the Schwarzschild photon-orbit ODE.
- **Caveat:** The validation is one ODE problem and uses a numerical reference solution; generalization beyond the trained initial-condition range and to other physical systems remains untested in the abstract.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Computational & data methods; Cosmology & gravitation

### 6. [Moon Radio Interferometer for Science and Exploration (MoonRISE): A Mission Concept for a Low-Frequency Radio Interferometer on the Lunar Farside](https://arxiv.org/abs/2611.33534)
- **Abstract:** The authors present MoonRISE, a proposed lunar-farside, all-sky radio interferometer operating from 100 kHz to 30 MHz, with heliophysics, lunar-ionosphere, and planetary-radio science goals.
- **Authors:** Saptarshi Bandyopadhyay, Marin Anderson, Alexander Hegedus, Kalind Carpenter, Jack Burns, et al.
- **arXiv:** `2611.33534v1` (published 2026-11-24 23:22:25 UTC; categories: `astro-ph.IM`, `astro-ph.CO`, `astro-ph.EP`, `astro-ph.SR`)
- **Evidence for ranking:** Collector score 0.75, entirely from 3 cross-lists × 0.25; third by submission time in the retained three-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** Bandyopadhyay et al. describe a nine-dipole, 1.5-km optical-fibre-tether concept intended to measure type-III burst scattering, the lunar ionosphere, and Uranian kilometric radiation if the mission is realized.
- **Evidence type:** Forecast/proposal; mission and payload concept, not an operating instrument or observational result.
- **Caveat:** The proposed science depends on mission selection, deployment, radio-frequency cleanliness, and technology maturity; none is demonstrated by this concept paper.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Astrophysics; Instrumentation & detectors; Plasma & fluid physics

### 7. [Quantum Noise-Limited Terahertz Interferometry for Distinguishing Ultra-Compact Supermassive Galactic Objects](https://arxiv.org/abs/2611.33488)
- **Abstract:** The authors model whether high-sensitivity terahertz interferometric visibilities could distinguish a Schwarzschild black hole from a JMN-1 naked-singularity model for Sgr A*.
- **Authors:** Vishwas Patel, Pankaj S. Joshi, Swalih A. Valiyakath, Munn V. Shukla, Mehul R. Pandya
- **arXiv:** `2611.33488v1` (published 2026-11-24 22:08:54 UTC; categories: `astro-ph.HE`, `astro-ph.IM`, `gr-qc`, `physics.ins-det`)
- **Evidence for ranking:** Collector score 0.75, entirely from 3 cross-lists × 0.25; fourth by submission time in the retained three-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** For optically thin spherical accretion onto Sgr A*, Patel et al. calculate separable visibility windows at specified baselines and flux errors, about 28 times below the 2017 EHT statistical uncertainty, and argue that minutes-long coherent integration would be needed.
- **Evidence type:** Computational; modeled gravitational-lensing images and interferometric visibilities under an accretion and noise model.
- **Caveat:** The discrimination forecast depends on spherical, optically thin accretion and demanding sensitivity assumptions; it is not an observation of a naked singularity or evidence against an event horizon.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Astrophysics; Cosmology & gravitation; Instrumentation & detectors

### 8. [Infrared-absorption magnetometry in a diamond nanocavity: demonstration and limits at the nanoscale](https://arxiv.org/abs/2611.33481)
- **Abstract:** The authors demonstrate cavity-enhanced magnetometry by measuring spin-dependent infrared absorption at the NV-centre singlet transition in a spin-dense diamond nanocavity.
- **Authors:** Nicholas J. Sorensen, Elham Zohari, Chris Coutts, Sean McNaney, Matteo Feder, et al.
- **arXiv:** `2611.33481v1` (published 2026-11-24 21:58:08 UTC; categories: `quant-ph`, `cond-mat.mes-hall`, `physics.app-ph`, `physics.optics`)
- **Evidence for ranking:** Collector score 0.75, entirely from 3 cross-lists × 0.25; fifth by submission time in the retained three-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** Sorensen et al. observe spin-dependent cavity transmission near 1042 nm, demonstrate cavity-enhanced magnetic-field sensing, and experimentally validate a model of the cavity response.
- **Evidence type:** Experimental; spin-dense diamond nanocavities probing the NV singlet transition, with a validated response model.
- **Caveat:** This establishes a readout method in the demonstrated nanocavity configuration, not a deployed sensor network or a general sensitivity advantage across all sensor geometries.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Quantum information; Atomic, molecular & optical physics; Instrumentation & detectors

### 9. [Chiral Domain-Wall Modes in Topological Adaptive Quantum Dynamics](https://arxiv.org/abs/2611.33328)
- **Abstract:** The authors study measurement-and-feedback adaptive circuits and find chiral dynamical topological domain-wall modes with long-time scaling consistent with a chiral free-fermion conformal field theory.
- **Authors:** Asadullah Bhuiyan, Haining Pan, Chao-Ming Jian
- **arXiv:** `2611.33328v1` (published 2026-11-24 19:17:32 UTC; categories: `quant-ph`, `cond-mat.dis-nn`, `cond-mat.stat-mech`, `cond-mat.str-el`)
- **Evidence for ranking:** Collector score 0.75, entirely from 3 cross-lists × 0.25; oldest by submission time in the retained three-cross-list tier. No HF/HN engagement or code-star value was recorded for this candidate.
- **Claimed result:** Bhuiyan, Pan, and Jian report chiral modes localized at domain walls in a 2+1D charge-conserving free-fermion adaptive-circuit model, with logarithmic entanglement and charge-variance scaling and algebraically decaying density correlations.
- **Evidence type:** Theoretical; free-fermion circuit model with measurement, feedforward, and quantum-trajectory analysis.
- **Caveat:** The result is established in a specific free-fermion model; robustness to interactions, hardware noise, and experimental implementation is not shown.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Quantum information; Condensed matter & materials

## Trending Research Themes

- **Quantum dynamics and usable quantum resources:** The many-body-scar preparation algorithm (2611.33987) and adaptive-circuit domain-wall modes (2611.33328) address coherent control and non-equilibrium structure theoretically, while the diamond-nanocavity study (2611.33481) reports an experimental sensing/readout advance. These are related by quantum control and measurement, not by a shared experimental result.
- **Instrumentation across very different frequency and scale regimes:** MoonRISE proposes lunar-farside observations below 30 MHz (2611.33534); a separate paper forecasts terahertz interferometric requirements for Sgr A* (2611.33488); the diamond study demonstrates infrared cavity readout at 1042 nm (2611.33481). The first is a mission concept, the second a model-based forecast, and the third a laboratory demonstration—not independent confirmations of one phenomenon.
- **Sharper mathematical and computational tools:** A quantitative noncollinear spin-DFT bound (2611.34301), a numerical PINN strategy for photon-orbit ODEs (2611.33953), and a proof linking the figure-eight colored Jones expansion to topological recursion (2611.34110) each provide a method or formal guarantee in a distinct setting. The food-web paper (2611.33569) is a further, isolated application of large-deviation methods to rare extinction events.

## Open Problems and Research Directions

- **Open problem (paper-stated):** The spin-DFT error estimate assumes slow variation and a fixed spin axis (2611.34301). **Direction (synthesis):** Benchmark the approximation against established calculations on noncollinear materials, especially where magnetization rotates rapidly or the preferred axis varies.
- **Open problem (paper-stated):** The topological-recursion proof is for the figure-eight knot; the authors explicitly raise extension to other hyperbolic knots and higher-genus curves (2611.34110). **Direction (synthesis):** Test the quotient-curve construction on hyperbolic twist knots and identify conditions under which recursion descends.
- **Open problem (paper-stated):** The food-web theory assumes unit conversion efficiency and basal-only self-limitation, while detailed instanton checks are for a three-species module (2611.33569). **Direction (synthesis):** Relax these assumptions and compare predicted extinction-time distributions with stochastic simulations and calibrated ecological interaction data.
- **Open problem (synthesis):** The scar algorithm and adaptive-circuit modes are theoretical, with no hardware evidence in the abstracts (2611.33987, 2611.33328). **Direction (synthesis):** Estimate gate depth and noise tolerance, then test finite-size scaling and mode lifetimes on programmable quantum simulators.
- **Open problem (paper-stated):** MoonRISE's proposed science depends on a lunar-farside payload and deployment, and the THz visibility separation requires stringent sensitivity and coherent integration (2611.33534, 2611.33488). **Direction (synthesis):** Validate the instrument/noise assumptions through end-to-end simulations and technology demonstrations, including realistic RFI, non-spherical accretion, and calibration errors.
- **Open problem (paper-stated):** The diamond paper identifies practical limits among optically detected resonance modalities (2611.33481). **Direction (synthesis):** Compare cavity-enhanced singlet absorption with photoluminescence readout under matched NV density, optical power, bandwidth, and nanoscale sensing conditions.

## Takeaway

The batch offers solid theoretical frameworks, algorithmic proposals, a laboratory sensing demonstration, and ambitious observing concepts. Its most useful near-term signal is methodological breadth; the mission and black-hole interferometry claims remain proposals or model-dependent forecasts, not detections.

## Method and sources

- **Window:** Daily arXiv announcement batch, submissions from 2026-11-24 19:00:00 UTC through 2026-11-25 19:00:00 UTC; announced 2026-11-26 at 01:00 UTC. This is today's batch, not a prior batch. Signal snapshot generated 2026-11-26T03:16:54Z.
- **Scope and coverage:** Physics group and major physics archives: `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`. Recent listings for all 11 archive groups were checked; the candidate pool was the provided signal file (273 arXiv records; 150 candidate records), and each retained paper's arXiv abstract page was checked. The top three full-text HTML versions were also inspected for methods/results and caveats.
- **Inference:** The signal file reported 0 candidates with external attention. For these selected records, scores consisted only of cross-listing (weight 0.25 per cross-list): 4 cross-lists = 1.00, and 3 = 0.75. HF/HN engagement and code-star signals were not recorded for these candidates; a zero external-attention score is not evidence of low scientific value. Within score tiers, ties were ordered by submission time. This is therefore a notable-paper list, not a measured popularity chart.
- **Filtering:** The score-1 robotics record `2611.33702` was left out because its full text identifies a prior publication in Proceedings of SPIE 7679 (2010); it is an older work newly present in this batch, not a newly produced result.
- **Sources:** Provided signal file `/home/yizhuan/.research/physics/daily/arxiv-trending-physics-daily-2026-11-26.signals.json` (arXiv collection status ok, 273; Hugging Face ok, 134; Hacker News ok, 15; arXiv lookup ok, 147). Semantic Scholar was unavailable (HTTP 429), so citation totals and influential-citation counts could not be corroborated and were not used. Primary sources: the nine linked arXiv abstract pages; full-text HTML was additionally reviewed for `2611.34301`, `2611.34110`, and `2611.33569`.
