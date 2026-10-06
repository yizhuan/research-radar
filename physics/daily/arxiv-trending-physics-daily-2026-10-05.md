# Physics on arXiv — Monday, 5 October 2026: 8 notable papers

The batch’s strongest pattern is precision and reliability: new analysis tools for neutrino, cosmological, collider, and lattice-QCD measurements sit alongside ambitious fault-tolerant quantum-computing designs. I’ll cover the standout experimental signal, then the methods and theory results that could sharpen what experiments can infer. This is an inferred selection, not an official arXiv trending chart; citations are too sparse or unavailable for most just-announced papers, so the ordering is not a popularity ranking.

Daily window: Monday, 5 October 2026 arXiv announcement batch (the latest batch available at the snapshot). Snapshot: 2026-10-06 00:17:15 UTC.

## Top papers (ranked)

### 1. [First observation of electron antineutrinos from nuclear reactors at Super-Kamiokande](https://arxiv.org/abs/2610.03143)
- **Abstract:** Using 411.52 live days of gadolinium-enhanced Super-Kamiokande data, the collaboration reports a reactor-antineutrino signal at about 6σ and fits solar-neutrino oscillation parameters jointly with the reactor sample.
- **Authors:** K. Abe, Y. Asaoka, M. Harada, Y. Hayato, K. Hiraide et al. (Super-Kamiokande Collaboration; 149 additional authors)
- **arXiv:** `2610.03143v1` (published 2026-10-02 11:08:41 UTC; categories: `hep-ex`)
- **Evidence for ranking:** A concrete detector-level observation with a reported ~6σ signal and oscillation fit; the paper was also independently surfaced in a researcher’s 5 October arXiv-picks list. That supports notice, not a measured readership lead.
- **Claimed result:** The authors disfavor the no-reactor hypothesis at approximately 6σ and report a combined solar-plus-reactor fit of sin²θ₁₂ = 0.332 (+0.028/−0.026) and Δm²₂₁ = (8.94 ± about 0.47) × 10⁻⁵ eV².
- **Evidence type:** Experimental; 411.52 live days from Super-Kamiokande’s SK-Gd phase, with accidental, geoneutrino, and spallation backgrounds considered.
- **Caveat:** The reactor-only and solar-neutrino samples are statistically compatible at only 1.9σ in the paper’s comparison, and the reported exposure is finite; the result is a preprint submitted to Physical Review Letters.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 2 October 2026).
- **Themes:** Particle, nuclear & high-energy physics; Instrumentation & detectors

### 2. [Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules](https://arxiv.org/abs/2610.03682)
- **Abstract:** The authors propose modular hyperbolic surface and color codes using sparse static connections between planar processor modules, with circuit-level simulations indicating much lower physical-qubit overhead than surface-code memories.
- **Authors:** Oscar Higgott, Hasan Sayginel, Francisco J. H. Heras, Zhiyang He, Tomas Jochym-O’Connor et al.
- **arXiv:** `2610.03682v1` (published 2026-10-02 17:48:44 UTC; categories: `quant-ph`)
- **Evidence for ranking:** The paper reports quantitative circuit-level simulation results (10× or greater overhead reduction, and a projected >30× reduction for larger codes) on a central fault-tolerance bottleneck; this is a technical-significance signal, not evidence of readership.
- **Claimed result:** The authors say their modular memory design can lower qubit overhead while maintaining fault tolerance, and give projected code parameters including encoding rate k/n = 1/16 and distance d ≥ 22.
- **Evidence type:** Computational; circuit-level simulations using modular syndrome extraction plus neural-network and matching decoders.
- **Caveat:** The headline resource gains are simulation results and larger-system projections, not a demonstrated hardware implementation; performance depends on the modeled inter-module seam errors and decoder assumptions.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 2 October 2026).
- **Themes:** Quantum information; Computational & data methods

### 3. [Multi-Band Constraints on Cosmic Strings: Unifying Harmonic and Burst Spectra](https://arxiv.org/abs/2610.02590)
- **Abstract:** The authors unify two descriptions of gravitational waves from cosmic-string loops and use joint PTA and LVK data to constrain string tension and loop-model parameters.
- **Authors:** Hansong Zhang, Huai-Ke Guo, Mairi Sakellariadou, Fengwei Yang, Yue Zhao
- **arXiv:** `2610.02590v1` (published 2026-10-01 23:39:02 UTC; categories: `gr-qc`, `astro-ph.CO`, `hep-ph`)
- **Evidence for ranking:** It connects three physics archives and combines NANOGrav, EPTA, and LIGO–Virgo–KAGRA data; the report number includes LIGO-P2600521-v1. This cross-field, data-linked result is stronger evidence of scientific relevance than recency alone.
- **Claimed result:** Across four representative loop-distribution models, the authors find that a harmonic treatment strengthens LVK bounds by 21–31% in three models, which then cannot explain the PTA common signal; one model remains viable under their joint analysis.
- **Evidence type:** Observational-data analysis and theoretical modeling; joint Bayesian inference using NANOGrav, EPTA, and LVK datasets with four loop-distribution models.
- **Caveat:** Conclusions depend on the assumed cosmic-string loop distributions and radiation parameters; the authors explicitly find different model outcomes, so the PTA signal is not established as cosmic-string evidence.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 1 October 2026).
- **Themes:** Cosmology & gravitation; Astrophysics

### 4. [Dark Energy Survey Year 6 Results: fast and interpretable posterior predictive checks for correlated cosmic probes](https://arxiv.org/abs/2610.03447)
- **Abstract:** The DES collaboration introduces a fast posterior-predictive consistency diagnostic for correlated cosmological probes, tests it on DES Year 3 data and simulations, and describes its role in DES Year 6 validation.
- **Authors:** C. Doux, J. Muir, A. Ferté, M. Raveri, D. Sanchez Cid et al. (DES Collaboration)
- **arXiv:** `2610.03447v1` (published 2026-10-02 15:28:00 UTC; categories: `astro-ph.CO`)
- **Evidence for ranking:** A major survey collaboration’s validation method has public code and is listed on the DES Year 6 cosmology-results page; the abstract reports tests against published DES Year 3 tension results and simulated Year 6 analyses.
- **Claimed result:** The authors’ scalar ΔPPD statistic reproduces the same inter-probe tensions identified by calibrated DES Year 3 tests, runs in minutes per test, and responds to injected inconsistency in simulated Year 6 analyses.
- **Evidence type:** Computational; Gaussian-mixture approximation, DES Year 3 measurements, toy models, and simulated DES Year 6 noise realizations.
- **Caveat:** Nuisance-parameter shifts can hide tensions, while weakly constrained parameter directions can create apparent tension between otherwise consistent probes; the authors advise using ΔPPD alongside other checks.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 2 October 2026).
- **Themes:** Cosmology & gravitation; Computational & data methods

### 5. [Third-Order Logarithmic Resummation for Jet-Vetoed Higgs Production](https://arxiv.org/abs/2610.03687)
- **Abstract:** The authors present a third-logarithmic-order QCD prediction for jet-vetoed Higgs production, combining a next-to-next-to-next-to-leading-order calculation with next-to-next-to-next-to-leading-logarithmic resummation.
- **Authors:** Samuel Abreu, Jonathan R. Gaunt, Pier Francesco Monni, Luca Rottoli, Robert Szafron
- **arXiv:** `2610.03687v1` (published 2026-10-02 17:51:35 UTC; categories: `hep-ph`, `hep-ex`)
- **Evidence for ranking:** It claims a first-in-class precision calculation for a standard LHC Higgs observable and is cross-listed between phenomenology and experiment; the CERN report number is CERN-TH-2026-173.
- **Claimed result:** At representative veto scales near 30 GeV and jet radius R = 0.4, the authors report an approximately 3% increase over the fixed-order prediction and residual perturbative uncertainty of about 3% after resummation.
- **Evidence type:** Theoretical; high-order perturbative QCD calculation and logarithmic resummation for LHC Higgs production.
- **Caveat:** The quoted uncertainty is residual perturbative uncertainty, not the total experimental or modeling uncertainty; the prediction remains tied to the specified veto scale and jet definition.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 2 October 2026).
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

### 6. [Complex-momentum form factors from lattice QCD](https://arxiv.org/abs/2610.03553)
- **Abstract:** The authors propose obtaining form factors at complex momenta directly from Euclidean position-space correlators using a bilateral Laplace transform, and test the method in a two-dimensional O(3) model.
- **Authors:** Maxwell T. Hansen, Gurtej Kanwar
- **arXiv:** `2610.03553v1` (published 2026-10-02 16:34:05 UTC; categories: `hep-lat`, `hep-th`)
- **Evidence for ranking:** The method addresses analytic continuation and inverse-problem difficulties, cross-lists lattice and theoretical high-energy physics, and includes a Monte Carlo test in a field theory.
- **Claimed result:** For the pion form factor, the authors derive access to complex Q² where Re(Q²) > −4m_π² without analytically continuing the correlator or solving an inverse problem.
- **Evidence type:** Theoretical and computational; derivation for infinite-volume correlators, proposed finite-volume estimators, and Monte Carlo tests in the two-dimensional O(3) nonlinear sigma model.
- **Caveat:** The numerical test is in the O(3) model, not a realistic finite-volume QCD calculation; the paper discusses but does not establish which finite-volume estimator will work best in production lattice studies.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 2 October 2026).
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

### 7. [Guide field effects on particle acceleration in three-dimensional relativistic magnetic reconnection](https://arxiv.org/abs/2610.03427)
- **Abstract:** Three-dimensional pair-plasma simulations indicate that the fast particle-acceleration channel persists as guide fields strengthen, but involves fewer particles and yields steeper spectra and lower maximum energies.
- **Authors:** Despina Karavola, Lorenzo Sironi, Maria Petropoulou
- **arXiv:** `2610.03427v1` (published 2026-10-02 15:11:45 UTC; categories: `astro-ph.HE`, `physics.plasm-ph`)
- **Evidence for ranking:** The study cross-lists astrophysics and plasma physics and compares 3D with 2D simulations across guide-field strengths, testing the robustness of an acceleration mechanism relevant to high-energy astrophysical plasmas.
- **Claimed result:** The authors find the fast acceleration channel absent in 2D but persistent in their 3D runs across the guide fields studied; increasing the guide field reduces the accelerated fraction, steepens spectra, and lowers maximum Lorentz factors.
- **Evidence type:** Computational; 3D relativistic pair-plasma particle-in-cell simulations, complemented by 2D runs with open outflow boundaries.
- **Caveat:** This is a simulation result for the modeled pair-plasma setup, not a direct measurement of astrophysical particle spectra; extrapolation depends on how well the simulated regime represents real sources.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 2 October 2026).
- **Themes:** Astrophysics; Plasma & fluid physics; Computational & data methods

### 8. [Higgsino dark matter compatible with the LUX-ZEPLIN high-energy nuclear-recoil event and IceCube constraints](https://arxiv.org/abs/2610.03692)
- **Abstract:** The authors test whether inelastic Higgsino dark matter can explain an LZ high-energy recoil event while remaining consistent with IceCube limits, finding allowed regions that vary strongly with astrophysical and solar-cooling assumptions.
- **Authors:** Katherine Freese, Dionysios P. Theodosopoulos
- **arXiv:** `2610.03692v1` (published 2026-10-02 17:52:54 UTC; categories: `hep-ph`, `astro-ph.CO`, `hep-th`)
- **Evidence for ranking:** The paper directly connects a reported LZ event to IceCube constraints and cross-lists particle phenomenology, cosmology, and theory. Its placement reflects a timely, testable interpretation, not evidence that the event is a dark-matter detection.
- **Claimed result:** Under selected halo, solar-cooling, and sideband assumptions, the authors find Higgsino parameter regions compatible with the LZ event and IceCube null searches, spanning roughly 2 TeV to hundreds of TeV or more.
- **Evidence type:** Theoretical; likelihood analysis of the LZ event and IceCube constraints under alternative halo and solar-cooling assumptions.
- **Caveat:** This is a proposed explanation of a single event, not a detection; compatibility changes with the high-speed halo tail, solar cooling model, and whether the LZ sideband constraint is included.
- **Announcement type:** new submission, 5 October 2026 announcement batch (submitted 2 October 2026).
- **Themes:** Particle, nuclear & high-energy physics; Cosmology & gravitation

## Trending Research Themes

- **Precision tests and inference from large datasets:** Super-Kamiokande’s reactor-antineutrino analysis, DES’s posterior-predictive checks, and the cosmic-string multi-band fit all show how background treatment, consistency tests, and model assumptions shape interpretation (2610.03143, 2610.03447, 2610.02590). These are complementary analyses, not independent confirmations of a shared physical signal.
- **Fault tolerance moves from code theory toward architecture:** Two new quantum-computing papers in the batch develop resource-saving code constructions—modular memories and SpiderCSS state preparation (2610.03682, 2610.03714). Their reported gains are simulation-based; neither entry establishes a hardware demonstration.
- **High-precision theory and computation as experimental infrastructure:** The jet-veto calculation and lattice-QCD complex-momentum method target precision observables, while reconnection simulations test acceleration physics in extreme plasmas (2610.03687, 2610.03553, 2610.03427). This is a methods-oriented pattern, not a measured readership trend.
- **New-particle explanations remain conditional:** The Higgsino study maps one LZ event against IceCube limits, but multiple astrophysical assumptions change the compatible region (2610.03692); it should be read as a phenomenological scenario, not an experimental result.

## Open Problems and Research Directions

- **Neutrino precision:** The Super-Kamiokande paper reports a finite 411.52-live-day exposure and 1.9σ compatibility between its reactor-only and solar samples. Longer SK-Gd exposure and independent reactor-sensitive measurements could test the stability of the oscillation fit (2610.03143).
- **Cosmic-string interpretation:** The joint constraints vary across loop-distribution models, and three of four considered models cannot explain the PTA common signal under the paper’s analysis. Better-motivated loop distributions and coordinated PTA/LVK analyses could determine whether any model survives robustly (2610.02590).
- **Quantum-memory practicality:** The modular-code resource projections have not yet been demonstrated in hardware. Experiments should measure seam-error behavior and decoder performance in connected planar modules at increasing code distances (2610.03682); state-preparation circuits likewise need implementation-level validation beyond Monte Carlo studies (2610.03714).
- **Cosmological consistency diagnostics:** The DES authors identify nuisance-parameter absorption and projection effects as failure modes. Further tests on realistic, varied Stage-IV survey simulations should quantify false-positive and missed-tension rates before relying on ΔPPD alone (2610.03447).
- **Dark-matter event interpretation:** The Higgsino explanation depends on solar cooling, halo high-speed populations, and the LZ sideband. Follow-up recoil data and independent constraints on those assumptions are needed to distinguish a dark-matter interpretation from backgrounds or fluctuations (2610.03692).

## Takeaway

The batch is led by a concrete reactor-antineutrino signal at Super-Kamiokande, while much of the other notable work improves the tools used to extract physics from difficult datasets or to build fault-tolerant quantum systems. Several headline conclusions remain model- or simulation-dependent; the most useful follow-up is experimental validation and robustness testing, not treating these preprints as settled results.

## Method and sources

- **Window:** Daily; latest arXiv announcement batch dated Monday, 5 October 2026. Snapshot time: 2026-10-06 00:17:15 UTC. Individual arXiv v1 submission timestamps are shown in each entry; the batch date is not the same as the original submission date.
- **Archive coverage:** Checked the latest pages for physics, astro-ph, cond-mat, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, nucl-ex, nucl-th, and quant-ph. The latest listing on each showed the Monday, 5 October batch. The selected papers are a cross-archive subset, not a complete digest of all submissions.
- **Inference:** arXiv has no official trending chart. The ordered selection prioritizes reported concrete results, cross-subfield relevance, collaboration/dataset or code signals, and the limited independent discussion found; recency is only a tie-breaker. Citation counts were not used. A Semantic Scholar citation lookup was rate-limited, so no citation metrics are asserted. The Super-Kamiokande paper appeared in a researcher’s daily arXiv picks; the DES paper is listed on the survey’s Year 6 results page. Most selected papers had no independent attention signal in sources checked.
- **Sources:** [arXiv recent listings](https://arxiv.org/list/physics/recent) and the corresponding category listings; each paper’s linked arXiv abstract page and its submission history. Additional checks: [researcher’s 5 October picks](https://mbustamante.net/my-daily-arxiv-picks/) and [DES Year 6 cosmology papers](https://www.darkenergysurvey.org/des-y6-cosmology-results-papers/).
