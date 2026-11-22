# Physics daily — 2026-11-19 announcement batch

Ten notable recent papers, ranked by inferred cross-listing and technical relevance. The dominant pattern is cross-field toolbuilding: better models and inference for quantum many-body systems and gravitational-wave/neutron-star physics, alongside data-driven methods that expose or measure physical structure. Spoken agenda: start with neutron-star and LISA modeling, move to an atomic-superfluid measurement, then cover quantum algorithms and theory constraints. This is an inferred ranking, not an official arXiv trending chart; recent-paper citation evidence is limited, and the ranking should not be read as a measure of readership.

## Top papers (ranked)

### 1. [Nonlinearly Causal General-Relativistic Superfluid Hydrodynamics: Simulating Vortex Dynamics in Neutron-Star Interiors](https://arxiv.org/abs/2611.26547)
- **Abstract:** The authors formulate causal, strongly hyperbolic general-relativistic superfluid hydrodynamics with vortex forces and line energy, and introduce a stable finite-volume method for simulating vortex dynamics in neutron-star interiors.
- **Authors:** Yuan Feng, Elias R. Most, Lorenzo Gavassino
- **arXiv:** `2611.26547v1` (published 2026-11-19T18:20:33Z; categories: `astro-ph.HE`, `astro-ph.SR`, `gr-qc`, `physics.flu-dyn`, `physics.plasm-ph`)
- **Evidence for ranking:** Signal score 1.00, composed of four cross-lists (the highest signal tier in this pool); no positive HF/HN attention signal was recorded, and citation data were unavailable. Its placement at the top of that tied tier reflects the concrete, cross-field numerical framework, not measured popularity.
- **Claimed result:** The authors derive nonlinear-causality and strong-hyperbolicity conditions, show that commonly used force-balanced models without line tension can be ill-posed at short wavelengths, and report the first multidimensional nonlinear simulations of relativistic superfluid vortex dynamics, including a simplified spin-down calculation.
- **Evidence type:** Computational and theoretical; finite-volume simulations validated against an exact relativistic superfluid Riemann solution and Kelvin-wave dispersion, followed by neutron-star equilibrium and spin-down calculations.
- **Caveat:** The neutron-star application uses a simplified, shear-free vortex-array model and prescribed vortex release/repinning; it does not yet model the full microphysics of vortex-lattice elasticity and pinning.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Astrophysics; Plasma & fluid physics; Computational & data methods

### 2. [SlotFlow-GB: A Neural Framework for Trans-Dimensional Inference of Overlapping Galactic Binaries](https://arxiv.org/abs/2611.26057)
- **Abstract:** The authors introduce a neural posterior approximation that jointly infers the number and parameters of overlapping Galactic binaries from simulated LISA data without fixing the source count in advance.
- **Authors:** Niklas Houba, Giovanni Giarda, Davide Piras
- **arXiv:** `2611.26057v1` (published 2026-11-19T13:01:48Z; categories: `astro-ph.IM`, `cs.LG`, `gr-qc`, `physics.data-an`, `physics.ins-det`)
- **Evidence for ranking:** Signal score 1.00, composed of four cross-lists (tied top signal tier). No positive HF/HN attention signal was recorded; citation data were unavailable. Its high placement reflects unusually broad physics/data-method cross-listing and a testable inference result, not a readership claim.
- **Claimed result:** On year-long, high-SNR simulations with up to ten binaries in a 2 μHz interval, the inferred source count is within one of the true count in 94% of cases; inference takes 41 ms per band on an NVIDIA GH200 GPU, according to the authors.
- **Evidence type:** Computational; simulated LISA observations and controlled source-overlap evaluations, with likelihood-based refinement tests.
- **Caveat:** The study uses a restricted high-SNR simulation regime, up to ten binaries, stationary Gaussian noise, and no unresolved Galactic foreground; source-count probabilities are not fully calibrated and cross-source parameter correlations are not explicitly represented.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Astrophysics; Cosmology & gravitation; Computational & data methods

### 3. [Local velocimetry for atomic superfluids: from Riemann rarefaction waves to quantized vortices](https://arxiv.org/abs/2611.26608)
- **Abstract:** The authors demonstrate two-dimensional velocity-field imaging in an atomic superfluid by mapping its wavefunction phase gradient to matter-wave interference fringe displacements, then apply it to rarefaction flows and quantized vortices.
- **Authors:** Yansheng Zhang, Yi Jiang, Feiyang Wang, Louis Depaepe, J. Q. Matthew Chia, et al.
- **arXiv:** `2611.26608v1` (published 2026-11-19T18:56:37Z; categories: `cond-mat.quant-gas`, `physics.atom-ph`, `physics.flu-dyn`, `quant-ph`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. It ranks above other papers in this signal tier because it reports an experimental measurement method and direct demonstrations rather than only a proposed capability.
- **Claimed result:** The authors use Raman–Bragg matter-wave interferometry to observe self-similar 1D Riemann rarefaction flow and map the 2D velocity field around quantized vortices, including quantized circulation.
- **Evidence type:** Experimental; interferometric measurements in a two-dimensional ultracold atomic superfluid.
- **Caveat:** Fringe-phase calibration and interaction-induced phase shifts affect the velocity readout; the supplementary material discusses calibration and an approximately 10% correction associated with finite-duration spin-transfer pulses.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Atomic, molecular & optical physics; Condensed matter & materials; Plasma & fluid physics

### 4. [High-Accuracy Neural-Network Quantum States via Randomized Real-Time Dynamics](https://arxiv.org/abs/2611.26587)
- **Abstract:** The authors propose dynamical averaging, which uses randomized real-time evolution to reduce errors in neural-network quantum-state estimates of ground-state observables without additional energy minimization or model complexity.
- **Authors:** John M. Martyn, Rod Rofougaran, Samuel Stein, Di Luo
- **arXiv:** `2611.26587v1` (published 2026-11-19T18:45:45Z; categories: `quant-ph`, `cond-mat.dis-nn`, `cond-mat.str-el`, `physics.comp-ph`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. The result combines a general error-suppression argument with tests on non-integrable spin models.
- **Claimed result:** The authors prove up-to-quadratic suppression of errors in arbitrary ground-state observables and report accelerated convergence with lower observable errors in non-integrable spin-model demonstrations.
- **Evidence type:** Theoretical and computational; proof plus numerical tests on non-integrable spin models.
- **Caveat:** The numerical demonstration is on the tested spin models; the abstract does not establish performance across other Hamiltonian families or report a universal empirical error reduction.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Quantum information; Condensed matter & materials; Computational & data methods

### 5. [Who Moved My $Z$ Boson? Revealing Resonance Features Inside a Neural Network](https://arxiv.org/abs/2611.26291)
- **Abstract:** The authors identify internal features corresponding to particle resonances in a generative collider model trained on real LHC data, and show that manipulating a selected feature changes the generated Z-boson mass peak.
- **Authors:** Kevin Alberto Urquía Calderón, Midori Kato, Inar Timiryasov, Oleg Ruchayskiy
- **arXiv:** `2611.26291v1` (published 2026-11-19T15:48:04Z; categories: `hep-ph`, `cs.LG`, `hep-ex`, `physics.data-an`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. The placement reflects the concrete model-intervention result and its bridge between collider physics and interpretability methods.
- **Claimed result:** In ShellFlow, the authors report learned features representing the Z, J/ψ, and Υ resonances; altering or removing the Z feature changes its generated mass/peak width while leaving most of the rest of the invariant-mass spectrum largely unchanged.
- **Evidence type:** Computational; mechanistic analysis of a generative model trained on real LHC data.
- **Caveat:** This is an intervention on a model representation, not a new measurement of the Z boson; the conclusion is specific to the trained generator and its feature-selection analysis.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

### 6. [UV Bounds on Inflationary Parity Violation](https://arxiv.org/abs/2611.26594)
- **Abstract:** The authors analyze whether ultraviolet-complete models can generate detectable parity violation in inflationary correlators, finding that existing tensor-scalar-scalar bispectrum bounds strongly constrain that possibility.
- **Authors:** Alexander Cassem, Mark P. Hertzberg
- **arXiv:** `2611.26594v1` (published 2026-11-19T18:51:13Z; categories: `hep-th`, `astro-ph.CO`, `gr-qc`, `hep-ph`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. The paper connects high-energy effective-theory consistency to a potentially observable cosmological signal.
- **Claimed result:** For tensor-to-scalar ratios near current observational limits, the authors find detectable parity-odd trispectrum signals incompatible with or close to the validity boundary of the examined UV completions; smaller ratios remain possible only with a very large TSS vertex enhancement.
- **Evidence type:** Theoretical; analysis of effective-field-theory bounds in fermionic and string-theoretic examples.
- **Caveat:** The result is conditional on the UV completions and parameter regimes examined; it does not rule out every mechanism for cosmological parity violation.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Cosmology & gravitation; Particle, nuclear & high-energy physics

### 7. [Evolving Decoding Algorithms for Quantum Error Correction](https://arxiv.org/abs/2611.25880)
- **Abstract:** The authors encode published belief-propagation decoders in a domain-specific language and use grammatical evolution to search for faster, more accurate decoders for quantum low-density parity-check codes.
- **Authors:** Eduardo Dueñez, Edgar Said Hernandez Sanchez, Edgar A. Duéñez-Guzmán, Suzanne Sadedin
- **arXiv:** `2611.25880v1` (published 2026-11-19T10:36:21Z; categories: `quant-ph`, `cs.AI`, `cs.MA`, `cs.NE`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. Its evidence includes a checkable time/error trade-off and an accepted-workshop comment, alongside the cross-listing.
- **Claimed result:** The authors report an evolved decoder with 23% fewer logical errors than a damped BP+OSD-0 baseline at 0.64 times its runtime, and faster-than-reference decoders across tested noise levels and code settings.
- **Evidence type:** Computational; decoder benchmarks on quantum LDPC-code simulations. The arXiv comment states acceptance at the NeurIPS 2026 EvoRobust Workshop.
- **Caveat:** The reported comparisons are benchmark results for the tested codes, noise models, and decoder implementations; the paper does not report deployment on a live quantum processor.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Quantum information; Computational & data methods

### 8. [Tunable Ground-State Entanglement in Fully Connected Quantum Systems: From Logarithmic to Volume-Law Scaling](https://arxiv.org/abs/2611.26430)
- **Abstract:** The authors construct a fully connected qubit Hamiltonian in which changing only the interaction normalization produces rigorously controlled ground-state entanglement ranging from subextensive scaling to a volume law.
- **Authors:** Donghoon Kim, Tomotaka Kuwahara
- **arXiv:** `2611.26430v1` (published 2026-11-19T17:08:10Z; categories: `quant-ph`, `cond-mat.dis-nn`, `cond-mat.stat-mech`, `math-ph`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. Its placement within the tier reflects a rigorous asymptotic result spanning quantum information and statistical mechanics.
- **Claimed result:** For the constructed all-to-all bipartite model, the authors prove entropy scaling Θ(n^(2−2κ) log n) for 1/2 < κ ≤ 1 and Θ(n) at κ = 1/2; a system-size-independent gap is proved for 3/4 ≤ κ ≤ 1.
- **Evidence type:** Theoretical, with weak-coupling analysis and numerical calculations for part of the parameter range.
- **Caveat:** The gap is rigorously bounded away from zero only for 3/4 ≤ κ ≤ 1; its persistence for 1/2 ≤ κ < 3/4 is suggested by weak-coupling analysis and numerics, not proved in the abstract.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Quantum information; Condensed matter & materials

### 9. [Fast extraction of universal data from temporal spectrum: Applications to Haagerup CFT and monopole scattering](https://arxiv.org/abs/2611.26257)
- **Abstract:** The authors propose extracting conformal-field-theory spectral data from the transfer matrix of an infinite matrix-product state after short imaginary-time evolution, and apply the method to the Haagerup CFT and monopole scattering.
- **Authors:** Tokiro Numasawa, Boris De Vos, Masataka Watanabe, Atsushi Ueda
- **arXiv:** `2611.26257v1` (published 2026-11-19T15:30:45Z; categories: `cond-mat.str-el`, `hep-lat`, `hep-th`, `quant-ph`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. Its placement reflects the cross-field method and the reported numerical CFT estimate, not external readership.
- **Claimed result:** Applying the method, the authors obtain a charge-resolved Haagerup CFT spectrum to higher levels and central charge c = 2.137(27); they also identify the Maldacena–Ludwig monopole boundary with the ground state of the Fidkowski–Kitaev Hamiltonian after space-time rotation.
- **Evidence type:** Computational and theoretical; infinite matrix-product-state transfer spectra and a proposed field-theory/lattice correspondence.
- **Caveat:** The central charge is a numerical extraction; the abstract does not give a systematic-error budget beyond the quoted uncertainty or establish convergence across independent methods.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Condensed matter & materials; Quantum information; Computational & data methods

### 10. [Certified Discovery of Quantum Phase Diagrams](https://arxiv.org/abs/2611.25064)
- **Abstract:** The authors give quantum and classical algorithms for mapping phase diagrams of smooth families of local Hamiltonians, with verifiable certificates for reported transitions under stated reference-state assumptions.
- **Authors:** Yuanxi Liu, John Preskill, Hsin-Yuan Huang
- **arXiv:** `2611.25064v1` (published 2026-11-18T19:09:17Z; categories: `quant-ph`, `cond-mat.stat-mech`, `cond-mat.str-el`, `math-ph`)
- **Evidence for ranking:** Signal score 0.75, from three cross-lists; no positive HF/HN attention signal was recorded; citation data were unavailable. It sits in the same tier as other three-cross-list candidates; selection reflects the verifiable transition-certificate claim and numerical model demonstrations.
- **Claimed result:** The authors prove a polynomial-time quantum algorithm at inverse-polynomial gap resolution and provide a quasipolynomial-time classical algorithm at constant gap resolution; numerical experiments test phase structures in several model systems.
- **Evidence type:** Theoretical and computational; algorithmic proof with numerical experiments on model quantum systems.
- **Caveat:** Success assumes at least one correct reference-ground-state preparation in every gapped region; the algorithms also depend on gap-resolution and smooth-family assumptions and do not remove those input requirements.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Quantum information; Condensed matter & materials; Computational & data methods

## Trending Research Themes

- **Quantum many-body methods span measurement, inference, and mathematical guarantees.** Direct velocity imaging in atomic superfluids (Zhang et al., 2611.26608) sits alongside improved neural quantum-state observables (Martyn et al., 2611.26587), controlled entanglement scaling (Kim & Kuwahara, 2611.26430), a transfer-matrix route to CFT data (Numasawa et al., 2611.26257), and certified phase-diagram algorithms (Liu et al., 2611.25064). These are distinct experiments, algorithms, and proofs—not independent confirmations of one result.
- **Gravitational-wave physics is being pushed toward crowded-source and interior-dynamics regimes.** SlotFlow-GB (Houba et al., 2611.26057) tackles overlapping Galactic-binary inference for LISA simulations, while Feng et al. (2611.26547) develop causal relativistic fluid and vortex evolution for neutron-star interiors. One is a data-analysis method for future observations; the other is a simulation framework, so their shared computational emphasis does not constitute observational corroboration.
- **Machine learning appears as a physics instrument and as an object of inspection.** Neural methods support LISA source inference (2611.26057), quantum-state estimates (2611.26587), and error-correction decoding (2611.25880); the collider study (Urquía Calderón et al., 2611.26291) instead probes how a trained generator encodes resonances. Their validation bases differ—simulations, model demonstrations, and real-data-trained networks—and should not be conflated.
- **Theory papers tie formal consistency to possible observables.** Cassem & Hertzberg (2611.26594) constrain inflationary parity signals using UV-completion bounds, while Feng et al. (2611.26547) connect hyperbolicity and causality to stable neutron-star simulations. The common pattern is checking whether a proposed physical description is both mathematically consistent and practically testable.

## Open Problems and Research Directions

- **Open problem (authors):** SlotFlow-GB’s source-count probabilities are not fully calibrated, its factorized posterior omits cross-binary correlations, and its tests use high-SNR, stationary-noise simulations without an unresolved Galactic foreground. **Research direction (synthesis):** test joint source-count/parameter posteriors with lower-SNR populations, foregrounds, gaps, glitches, and time-varying instrument noise, then compare blind predictions with likelihood-based recovery (2611.26057).
- **Open problem (authors):** The neutron-star formulation omits vortex-lattice shear response, and its spin-down example prescribes vortex release and repinning. **Research direction (synthesis):** incorporate elastic lattice modes and microphysically motivated pinning/unpinning laws, then test how those additions change causality domains, glitch-like dynamics, and spin-down (2611.26547).
- **Open problem (authors/supplement):** Atomic-superfluid velocimetry depends on fringe-phase calibration and has interaction and finite-pulse corrections. **Research direction (synthesis):** quantify those systematics across density and flow regimes, and cross-calibrate against an independent velocity measurement before applying the method to more complex turbulent or vortex-rich states (2611.26608).
- **Open problem (authors):** The entanglement result proves a uniform gap only for 3/4 ≤ κ ≤ 1; the lower-κ gap behavior is supported by weak-coupling analysis and numerics. **Research direction (synthesis):** seek a proof or counterexample below κ = 3/4 and test whether the scaling hierarchy persists under other all-to-all coupling structures (2611.26430).
- **Open problem (authors):** The phase-diagram algorithm requires a correct reference ground-state preparation in each gapped region and finite gap resolution. **Research direction (synthesis):** characterize how reference-state errors and small gaps affect certificate reliability in larger, more complex Hamiltonian families (2611.25064).

## Takeaway

The strongest common signal is methodological: researchers are building ways to measure, infer, or simulate physical structure that was previously difficult to resolve, from local superfluid flow to overlapping gravitational-wave sources and quantum phase diagrams. The candidate pool had no recorded external attention and Semantic Scholar citation data were unavailable, so this is a cross-listing-led selection of notable work—not a defensible measure of what was most read or discussed.

## Method and sources

- **Window:** daily arXiv batch, 2026-11-18 19:00:00Z through 2026-11-19 19:00:00Z; announcement batch dated 2026-11-19 and issued 2026-11-20 01:00:00Z. This report follows the supplied 19 November signal window as requested; a separate report for the newer 20 November batch exists in the archive.
- **Snapshot:** 2026-11-22 17:20:49 UTC. The signal file was generated at 2026-11-22 17:20:30 UTC.
- **Scope:** the configured Physics group and major archives: `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`. The collector reports 444 arXiv records and a 150-paper candidate pool for this daily window; the ten selected entries were deduplicated by versionless arXiv ID. All ten abstract pages were checked against arXiv, and their IDs, versions, authors, dates, abstracts, and categories were cross-checked using one batched arXiv API request. The top two papers were inspected in full arXiv HTML; for the third, the available arXiv HTML included the abstract and supplemental methods, so its caveat is limited to those sources.
- **Inference:** arXiv provides no official trending chart. The signal file reports zero candidates with positive external attention; HF and HN collection completed but no matching positive upvote/point/comment signals were recorded. The selected entries' scores are cross-list-derived (1.00 for four cross-lists; 0.75 for three); score zero would mean no signal was detected, not that a paper is unimportant. Within equal tiers, ordering is editorial and based on the concreteness and cross-field relevance of the claimed result, not arXiv API order. Citation totals and influential citations were not used.
- **Unavailable source:** Semantic Scholar citation/influential-citation data were unavailable in the signal collection, so citation momentum could not be assessed.
- **Sources:** [arXiv signal file](file:///home/yizhuan/.research/physics/daily/arxiv-trending-physics-daily-2026-11-19.signals.json); the ten linked arXiv abstract pages above; arXiv Atom API metadata for the selected IDs. The collector's source-status fields report successful arXiv, Hugging Face, Hacker News, and arXiv lookup collection, with Semantic Scholar unavailable.
