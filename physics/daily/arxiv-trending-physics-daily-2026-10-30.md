# arXiv Physics Daily — Friday, 30 October 2026

Snapshot: 2026-11-02 01:27:20 UTC. The latest available announcement batch was Friday 30 October; no Monday 2 November batch had appeared by the snapshot. This report selects five notable papers from that batch. The strongest shared pattern is quantum-computing scale-up, spanning fault-tolerant algorithm resource estimates and cryogenic atom-array gates. Agenda: the hardware-cost estimate, the new gate experiment, then a Hubbard-model superconductivity result, a CMB clustering analysis, and neutrino constraints from XENONnT. Global caveat: arXiv publishes no official trending chart; this ordering is inferred from limited community-attention and curation signals plus paper-specific results, with little usable citation evidence for such recent submissions—it is not a readership or download ranking.

## Top papers (ranked)

### 1. [Shor's algorithm compiled on cat qubits: 22 593 qubits for RSA-2048 in 3.14 days](https://arxiv.org/abs/2610.37839)
- **Abstract:** The authors give end-to-end physical-resource estimates for compiling Shor's algorithm onto two superconducting cat-qubit architectures, including layouts and schedules for RSA-2048 and related discrete-log benchmarks.
- **Authors:** Axel Pappalardo, Dahmun Goudarzi, Victor Hertz, Hugo Jacinto, Larissa Kroell et al.
- **arXiv:** `2610.37839v1` (published 2026-10-27 18:52:22 UTC; categories: `quant-ph`)
- **Evidence for ranking:** SciRate's “Top arXiv papers” feed surfaced it among its leading entries at the snapshot, a qualitative community-attention signal; no numerical score is used.
- **Claimed result:** The authors estimate RSA-2048 factoring at 22,593 cat qubits and 3.14 days under their stated hardware and noise assumptions; the RSA circuit is compiled in full, while related estimates reuse its operations.
- **Evidence type:** computational; circuit compilation, error-correction resource modeling, physical-qubit layouts, and schedules.
- **Caveat:** The headline estimate assumes a 1 μs error-correction cycle, 10 μs decoder reaction, phase-flip probability 5×10⁻⁴, and no bit flips—roughly a 100-year bit-flip time. The authors give a higher-cost alternative when bit flips are included; this is a resource estimate, not a demonstration of a working machine.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Quantum information; Computational & data methods

### 2. [High-Fidelity Universal Quantum Gates in a Cryogenic Atom Array](https://arxiv.org/abs/2610.40329)
- **Abstract:** The authors demonstrate a universal gate set in a cryogenic ¹³³Cs tweezer array, reporting 99.970(2)% single-qubit fidelity and 99.76(8)% raw two-qubit entangling-gate fidelity using direct single-photon Rydberg excitation.
- **Authors:** Junlan Jin, Donghyuk Seo, Yue Shi, Yukai Lu, Jeff D. Thompson, Waseem S. Bakr
- **arXiv:** `2610.40329v1` (published 2026-10-29 15:57:06 UTC; categories: `physics.atom-ph`, `quant-ph`)
- **Evidence for ranking:** A community-maintained quantum-experiment index opened a paper-addition issue on 30 October; the paper is also cross-listed between atomic physics and quantum physics, and reports measured gate benchmarks.
- **Claimed result:** The authors report a complete universal gate set in a cryogenic atom array; their error analysis attributes most measured two-qubit infidelity to atomic motion, with the Rydberg-decay contribution below 3×10⁻⁴.
- **Evidence type:** experimental; cryogenic optical-tweezer array of ¹³³Cs atoms, with single- and two-qubit gate benchmarking.
- **Caveat:** Atomic motion remains the dominant error in the measured gate, so the higher fidelities projected from suppressing Rydberg decay require improved cooling and further experimental validation.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Quantum information; Atomic, molecular & optical physics

### 3. [A $B_{1g}$ phonon unlocks $d$-wave superconductivity in the repulsive Hubbard model](https://arxiv.org/abs/2610.37746)
- **Abstract:** Finite-temperature quantum Monte Carlo calculations find a $d$-wave superconducting dome when a $B_{1g}$ phonon couples to the doped repulsive $t$-$t'$ Hubbard model, with the authors reporting cooperative enhancement beyond either interaction alone.
- **Authors:** Wen O. Wang, Tianshu Li, Xiaoyue Ma, Rong Zhang, Lei Zhang et al.
- **arXiv:** `2610.37746v1` (published 2026-10-27 18:00:00 UTC; categories: `cond-mat.supr-con`, `cond-mat.str-el`)
- **Evidence for ranking:** Its cross-listing links superconductivity and strongly correlated electrons, and the paper reports finite-temperature numerical evidence for a concrete pairing mechanism. No paper-specific citation or independent discussion signal was found in the sources checked, so its placement reflects the result rather than measured attention.
- **Claimed result:** The authors infer a transition scale near $T_c/t≈0.04$ at $U/t=1$ and density 0.8, with a doping dome; this establishes a result in the simulated model, not in a material sample.
- **Evidence type:** computational; numerically exact determinant quantum Monte Carlo on doped Hubbard-model lattices.
- **Caveat:** The fermion sign problem limits access to lower temperatures at stronger repulsion and prevents equally direct checks on the largest lattices; finite-size and extrapolation limits therefore remain relevant.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Condensed matter & materials

### 4. [Disentangling constraints on $S_8$ from the high and low redshift CMB](https://arxiv.org/abs/2610.37752)
- **Abstract:** A principal-component analysis separates primordial-CMB and CMB-lensing contributions to clustering constraints, finding a primordial-CMB $S_8$ value compatible with DES while the lensing-inferred clustering is higher.
- **Authors:** Joann Jones, Ualype de Andrade Uchôa, Scott Dodelson
- **arXiv:** `2610.37752v1` (published 2026-10-27 18:00:00 UTC; categories: `astro-ph.CO`)
- **Evidence for ranking:** The work appears in multiple third-party daily arXiv listings, including DailyArXiV and Academus, and combines Planck, ACT, and SPT data with an explicit comparison to DES.
- **Claimed result:** The authors obtain $S_8=0.795±0.022$ from the primordial CMB, consistent with their cited DES value of $0.789±0.012$; the size of the lensing excess and the comparison depend on the prior for summed neutrino mass.
- **Evidence type:** observational; reanalysis of Planck 2018, ACT DR6, and SPT-3G D1 CMB data, compared with Dark Energy Survey results.
- **Caveat:** This is a data-analysis separation, not evidence that a cosmological tension is resolved; the authors report sensitivity to the neutrino-mass prior and lensing treatment.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Cosmology & gravitation; Computational & data methods

### 5. [Neutrino electromagnetic properties after the first $pp$ solar neutrino observation at XENONnT](https://arxiv.org/abs/2610.38734)
- **Abstract:** The authors analyze XENONnT's reported low-energy solar-neutrino scattering data to infer the $pp$ flux and low-momentum-transfer weak mixing angle, and to constrain several neutrino electromagnetic interactions.
- **Authors:** Valentina De Romeri, Dimitrios K. Papoulias, Federica Pompa, Christoph A. Ternes
- **arXiv:** `2610.38734v1` (published 2026-10-28 19:27:50 UTC; categories: `hep-ph`)
- **Evidence for ranking:** A curated 30 October neutrino/particle-physics arXiv digest selected the work; it links a newly available low-energy detector data set to several beyond-Standard-Model constraints.
- **Claimed result:** The authors derive bounds on neutrino charge radii, magnetic moments, millicharges, and a sterile-neutrino dipole portal from the published XENONnT data; they specifically test how the mild $pp$-flux excess is affected by the $^{14}$C background.
- **Evidence type:** observational; phenomenological fit to the XENONnT collaboration's reported neutrino-electron scattering result, not a new detector measurement.
- **Caveat:** The mild flux excess and the $^{14}$C background treatment affect the fitted quantities, so the inferred constraints depend on the background model and data interpretation.
- **Announcement type:** new submission, 2026-10-30 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Instrumentation & detectors

## Trending Research Themes

- **Quantum-computing scale-up (two-paper pattern):** Pappalardo et al. estimate the physical resources and schedules for fault-tolerant Shor computation on cat qubits, while Jin et al. experimentally benchmark a universal gate set in a cryogenic neutral-atom array. These address complementary layers—logical resource accounting and physical gate performance—not a shared platform or a demonstrated end-to-end computer.
- **Correlated-electron pairing (isolated signal):** Wang et al. use determinant QMC to test cooperation between a symmetry-specific phonon and Hubbard repulsion. The shared scientific thread is an interaction mechanism for $d$-wave pairing; the result remains model-based rather than a measurement of a cuprate.
- **Precision inference from existing data (two distinct isolated signals):** Jones et al. separate primordial and lensing contributions in CMB constraints using Planck/ACT/SPT, while De Romeri et al. reinterpret XENONnT's low-energy solar-neutrino data. These are complementary analysis strategies, not independent confirmations of one another or of a new detection.

## Open Problems and Research Directions

- **Realistic fault-tolerant resource assumptions — paper 1 (authors' stated assumption):** The no-bit-flip baseline requires an approximately century-long bit-flip time. A useful next step is a full resource sweep using measured, correlated error channels and decoder latency from a specified device, comparing the paper's concatenated-code alternative with the baseline.
- **Cryogenic gate infidelity — paper 2 (authors' error budget):** Atomic motion dominates the measured error. Improved cooling and repeated benchmarking across atom-pair geometries could test how much of the projected fidelity gain survives in a larger, repeatedly operated array.
- **Finite-temperature limits on the pairing result — paper 3 (authors' stated limitation):** The sign problem restricts stronger-coupling, low-temperature simulations and the largest-lattice checks. Follow-up work could improve controlled thermodynamic extrapolations or use complementary unbiased methods, then compare the predicted phonon-frequency and doping dependence with spectroscopy and pairing measurements in candidate materials.
- **CMB lensing and neutrino-prior dependence — paper 4 (authors' stated model dependence):** Independent likelihood analyses that vary neutrino-mass priors and lensing systematics, and add newer CMB/lensing data, could determine which part of the inferred $S_8$ difference is robust to those choices.
- **XENONnT $^{14}$C-background sensitivity — paper 5 (authors' stated issue):** Refit the solar-neutrino spectrum with independently constrained $^{14}$C contamination and additional exposure, then propagate that background uncertainty through the electromagnetic-property limits. This would test the robustness of the interpretation without treating the mild excess as a discovery.

## Takeaway

The most visible signal in this batch is a two-sided push on quantum computing: realistic algorithm-level resource accounting and improved physical gate benchmarks. Alongside it, a numerical superconductivity result and two data-reanalysis papers offer testable leads, but they remain conditional on model, noise, prior, or background assumptions; none alone establishes broad consensus or a new discovery.

## Method and sources

- **Window:** daily, 2026-10-30 through 2026-10-30. Snapshot: 2026-11-02 01:27:20 UTC. Because no 2 November announcement was available at the snapshot, the report uses the preceding Friday batch. All selected papers were new submissions in that batch, not revisions.
- **Archive coverage:** checked the official arXiv “new” pages for `physics`, `astro-ph`, `cond-mat`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`, including cross-submission sections. The pages contained 830 new-submission placements and 348 cross-list placements; after deduplication, 894 versionless IDs remained. Replacement entries were excluded. Category pages: [physics](https://arxiv.org/list/physics/new), [astro-ph](https://arxiv.org/list/astro-ph/new), [cond-mat](https://arxiv.org/list/cond-mat/new), [gr-qc](https://arxiv.org/list/gr-qc/new), [hep-ex](https://arxiv.org/list/hep-ex/new), [hep-lat](https://arxiv.org/list/hep-lat/new), [hep-ph](https://arxiv.org/list/hep-ph/new), [hep-th](https://arxiv.org/list/hep-th/new), [nucl-ex](https://arxiv.org/list/nucl-ex/new), [nucl-th](https://arxiv.org/list/nucl-th/new), [quant-ph](https://arxiv.org/list/quant-ph/new).
- **Verification and ranking:** selected IDs, v1 versions, UTC timestamps, categories, authors, abstracts, and canonical links were checked against arXiv's Atom API and each official abstract page. The top three papers' full text was inspected where practical: the 128-page Shor paper via PDF text extraction, and the cryogenic-gate and Hubbard papers via arXiv HTML. Ranking signals were the SciRate community listing, a GitHub experiment-index addition, third-party daily arXiv curation, cross-listing, and concrete result types. No citation totals are reported; a usable Semantic Scholar citation snapshot was unavailable, so citation momentum did not influence the order. `web_extract` was unavailable in this runtime; direct official arXiv pages/API and full-text routes were used instead.
- **Attention and curation sources:** [SciRate Top arXiv papers](https://scirate.com/); [quantum-experiment index issue #590](https://github.com/francois-marie/awesome-quantum-computing-experiments/issues/590); [DailyArXiV, 30 October](https://rhysyt.github.io/DailyArXiV/Main.html); [Academus astrophysics listings](https://academ.us/list/astro-ph/); [Antonio Marrone's 30 October neutrino digest](https://home.ba.infn.it/~marrone/highlights/2026-10-30.html).
- **Selected arXiv records:** [2610.37839](https://arxiv.org/abs/2610.37839), [2610.40329](https://arxiv.org/abs/2610.40329), [2610.37746](https://arxiv.org/abs/2610.37746), [2610.37752](https://arxiv.org/abs/2610.37752), [2610.38734](https://arxiv.org/abs/2610.38734).
- **Interpretation:** “Notable recent papers” is more accurate than a measured popularity ranking for most entries. The external lists and digest are evidence of curation, not independent scientific validation. The date labels in the arXiv API are first-submission timestamps; the batch date comes from the official `new` listings.
