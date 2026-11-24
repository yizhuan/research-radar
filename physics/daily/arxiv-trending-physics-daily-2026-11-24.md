# arXiv physics — 24 November 2026: ten notable new papers

Today’s 24 November announcement batch covers 10 notable new papers from 20 November 19:00 through 23 November 19:00 UTC. A visible pattern is physics advancing through more capable computational models and specialized measurement tools, from nanoscale heat transport to astronomy and driven quantum matter. Spoken agenda: start with a differentiable heat-transport solver, move through stellar systems and detector advances, then end with quantum dynamics and dark-matter search strategy. Global caveat: arXiv publishes no official trending chart, so this is an inferred ordering; the available attention scores are cross-listing-only, and citation evidence is unavailable for this snapshot, making this a notable-paper selection rather than a measured popularity ranking.

## Top papers (ranked)

### 1. [JAX-Nano: A GPU-Accelerated Differentiable Phonon Boltzmann Transport Solver for Nanoscale Heat Transfer](https://arxiv.org/abs/2611.28926)
- **Abstract:** The authors introduce a GPU-accelerated, differentiable finite-volume solver for steady and transient phonon Boltzmann transport, validated across transport regimes and applied to 3D FinFETs and inverse parameter identification.
- **Authors:** Bo Zhang, Amy Zhaomei Zhang
- **arXiv:** `2611.28926v1` (published 2026-11-21T16:56:34Z; categories: `physics.comp-ph`, `cs.CE`, `cs.LG`, `math-ph`, `math.NA`)
- **Evidence for ranking:** Signal score 1.00, entirely from 4 cross-lists (weighted component 1.00); this is the highest score in the pool. No external-attention component is recorded for this candidate.
- **Claimed result:** The authors report agreement with analytical and established BTE solvers across diffusive-to-ballistic regimes, and demonstrate automatic-differentiation-based recovery of transport and heat-source parameters.
- **Evidence type:** computational; numerical benchmarks, analytical solutions, established BTE solvers, and simulated FinFET configurations.
- **Caveat:** This is a numerical framework rather than experimental validation of device temperatures; its benchmark speed depends on hardware and workload. The authors identify fuller phonon dispersion/scattering models and memory efficiency as future work.
- **Announcement type:** new submission
- **Themes:** Condensed matter & materials; Computational & data methods

### 2. [Validating Gaia DR3 Astrometric Accelerations with Close Visual Binaries](https://arxiv.org/abs/2611.28969)
- **Abstract:** The authors compare Gaia DR3 acceleration solutions with the gravitational effects and sky directions of known resolved visual-binary companions, finding consistency for a selected subset and identifying likely unresolved perturbers in most cross-matches.
- **Authors:** Qier An, Timothy D. Brandt
- **arXiv:** `2611.28969v1` (published 2026-11-21T18:07:29Z; categories: `astro-ph.SR`, `astro-ph.EP`, `astro-ph.GA`, `astro-ph.IM`)
- **Evidence for ranking:** Signal score 0.75, entirely from 3 cross-lists (weighted component 0.75); tied at this score with several candidates. The physical cross-check and submitted-to-AJ comment support its selection among ties; no external-attention component is recorded.
- **Claimed result:** From 2,466 Gaia–Washington Double Star pairs, the authors find 98.1% of measured accelerations exceed the maximum attributable acceleration from the listed companion by more than a factor of ten; of 13 plausible systems with enough data for a test, 11 statistically accommodate the reported accelerations.
- **Evidence type:** observational; Gaia DR3 and Washington Double Star catalog cross-match, companion-orbit fits, and a direction test.
- **Caveat:** This validates a catalog-matched subset, not all Gaia acceleration solutions. Many plausible pairs lack sufficient resolved astrometry for fitting, and the authors discuss WDS resolution and companion-mass uncertainties.
- **Announcement type:** new submission
- **Themes:** Astrophysics

### 3. [Time-variable tertiary mass transfer in hierarchical triple systems](https://arxiv.org/abs/2611.28537)
- **Abstract:** Three-dimensional hydrodynamic simulations show that the inner binary’s finite separation can change a tertiary donor’s mass-loss variability and mean transfer rate, with implications for whether transferred gas forms a circumbinary disk.
- **Authors:** Alejandra Rosselli-Calderon, Morgan MacLeod, Enrico Ramirez-Ruiz
- **arXiv:** `2611.28537v1` (published 2026-11-21T03:53:59Z; categories: `astro-ph.SR`, `astro-ph.EP`, `astro-ph.GA`, `astro-ph.HE`)
- **Evidence for ranking:** Signal score 0.75 from 3 cross-lists (weighted component 0.75). Its 3D simulations address an explicitly poorly understood phase of triple-star evolution; no external-attention component is recorded.
- **Claimed result:** For the modeled γ=5/3 polytropic donor, the authors find a steep, approximately a_b^(6.1±0.9)-dependent rise in orbit-averaged mass loss as inner-binary separation increases, and a transition between individual and collaborative accretion.
- **Evidence type:** computational; three-dimensional hydrodynamic simulations of a hierarchical triple configuration.
- **Caveat:** The reported scaling is tied to the modeled donor and system assumptions, including equal-mass inner-binary components; grid mapping of the hydrostatic stellar profile is resolution-sensitive and computationally costly.
- **Announcement type:** new submission
- **Themes:** Astrophysics

### 4. [A high-speed and high-resolution 3D velocity map imaging system with a neuromorphic camera](https://arxiv.org/abs/2611.28768)
- **Abstract:** The authors demonstrate a camera-based 3D velocity-map imaging system using an event-driven neuromorphic camera to detect single ions or electrons with microsecond latency.
- **Authors:** Sulaiman Abubakar, Blessed Oguh, Akaninyene Udoikono, Hackim Musah, Suk Kyoung Lee, Wen Li
- **arXiv:** `2611.28768v1` (published 2026-11-21T12:24:15Z; categories: `physics.ins-det`, `cs.CV`, `nucl-ex`, `physics.chem-ph`)
- **Evidence for ranking:** Signal score 0.75 from 3 cross-lists (weighted component 0.75); its detector-method cross-listing spans instrumentation, computer vision, nuclear experiment, and chemical physics. No external-attention component is recorded.
- **Claimed result:** The authors report 2 μs single-particle detection latency and momentum-imaging operation above 100 kHz, compared with a few kHz for their conventional frame-camera reference.
- **Evidence type:** experimental; event-driven camera coupled to a microchannel-plate imaging detector.
- **Caveat:** The abstract establishes a prototype demonstration but does not provide a broad uncertainty budget or performance comparison across other imaging platforms.
- **Announcement type:** new submission
- **Themes:** Instrumentation & detectors

### 5. [The Thue-Morse route to chaos in the open quantum baker map](https://arxiv.org/abs/2611.28242)
- **Abstract:** Numerical resonance spectra of an open quantum baker map track a Thue–Morse sequence of classical survivor cycles as the opening crosses from zero to positive topological entropy.
- **Authors:** Leonardo Ermann
- **arXiv:** `2611.28242v1` (published 2026-11-20T19:17:45Z; categories: `nlin.CD`, `math-ph`, `math.DS`, `quant-ph`)
- **Evidence for ranking:** Signal score 0.75 from 3 cross-lists (weighted component 0.75); it connects nonlinear dynamics, mathematical physics, and quantum physics and includes ancillary verification scripts. No external-attention component is recorded.
- **Claimed result:** The author reports that numerically computed resonances follow the classical Thue–Morse route step by step up to Hilbert-space dimension N=2^25, including the zero-entropy regime.
- **Evidence type:** computational; classical-map analysis and numerical diagonalization/Arnoldi calculations of open quantum-map resonances.
- **Caveat:** At the largest sizes only about four cycle steps are resolved. The paper leaves the asymptotic behavior of the leading resonance and the Fourier-basis fractal-Weyl exponent open.
- **Announcement type:** new submission
- **Themes:** Quantum information; Computational & data methods

### 6. [An all-orders proof of gradient flow for multiscalar φ⁴ theory in four dimensions](https://arxiv.org/abs/2611.28206)
- **Abstract:** The author proves that the perturbative renormalization-group flow of four-dimensional multiscalar φ⁴ theory is a gradient flow to all orders, with a positive-definite metric.
- **Authors:** Marten Reehorst
- **arXiv:** `2611.28206v1` (published 2026-11-20T19:00:01Z; categories: `hep-th`, `cond-mat.stat-mech`, `hep-ph`, `math-ph`)
- **Evidence for ranking:** Signal score 0.75 from 3 cross-lists (weighted component 0.75), placing it among the most cross-listed candidates; its explicit all-orders result and check of five-/six-loop relations distinguish it among ties. No external-attention component is recorded.
- **Claimed result:** The author derives a symmetric positive metric and potential for the flow using Weyl consistency conditions and a Ward identity, and checks the implied five-/six-loop coefficient relations explicitly.
- **Evidence type:** theoretical; perturbative quantum field theory and explicit loop-coefficient calculations.
- **Caveat:** The proof is conditional on stated perturbative assumptions, including finiteness of the generating functional with local couplings and a bounded remainder for the large-momentum Feynman-integral expansion; it is not a nonperturbative result.
- **Announcement type:** new submission
- **Themes:** Particle, nuclear & high-energy physics

### 7. [Observation of nonadiabatic quantum tunneling in a driven correlated insulator](https://arxiv.org/abs/2611.28980)
- **Abstract:** Time-resolved optical spectroscopy of NiPS₃ finds ponderomotively blue-shifted multiphoton-like resonances in a tunneling-dominated absorption channel near the Keldysh crossover.
- **Authors:** Mingyao Guo, Radu Andrei, Jaena Park, Je-Geun Park, Eugene Demler, David Hsieh
- **arXiv:** `2611.28980v1` (published 2026-11-21T18:29:30Z; categories: `cond-mat.str-el`, `cond-mat.mes-hall`, `physics.optics`)
- **Evidence for ranking:** Signal score 0.50 from 2 cross-lists (weighted component 0.50). The experimental spectroscopy plus a qualitative Hubbard-model comparison provide a concrete result among candidates at this score; no external-attention component is recorded.
- **Claimed result:** The authors interpret the blue-shifted resonances observed while varying drive field and frequency as a spectroscopic signature of adiabaticity breakdown in the Keldysh crossover.
- **Evidence type:** experimental; time-resolved optical spectroscopy on NiPS₃, compared with time-dependent Gaussian-variational Hubbard-model simulations.
- **Caveat:** The interpretation is supported by qualitative rather than quantitative agreement with the model simulations, and the abstract reports one correlated-insulator system.
- **Announcement type:** new submission
- **Themes:** Condensed matter & materials

### 8. [Observation of collective flatbands in hybrid Mie-grating THz metasurfaces](https://arxiv.org/abs/2611.28246)
- **Abstract:** Terahertz near-field measurements on free-standing hybrid Mie-resonator/grating metasurfaces reveal quasi-flat magnetic-dipolar bands and long-lived coherent oscillations.
- **Authors:** Jie Ji, Thanh Xuan Hoang, Ayan Nussupbekov, Siyan Zhou, Kehan Wang, Yuri Kivshar, Jaime Gómez Rivas
- **arXiv:** `2611.28246v1` (published 2026-11-20T19:26:08Z; categories: `physics.optics`, `cond-mat.mtrl-sci`, `physics.app-ph`)
- **Evidence for ranking:** Signal score 0.50 from 2 cross-lists (weighted component 0.50). The paper pairs experimental band mapping with a concrete geometry-tuning result; no external-attention component is recorded.
- **Claimed result:** The authors report experimentally observed quasi-flat bands and show that changing grating width tunes resonances and raises Q while retaining quasi-flat dispersion; the Purcell enhancement is calculated.
- **Evidence type:** experimental; terahertz near-field measurements and spatial mapping, supplemented by Bloch-resolved Purcell calculations.
- **Caveat:** The emitter/Purcell response is calculated rather than demonstrated with an emitter, and the reported metasurface behavior does not by itself establish a device-level application.
- **Announcement type:** new submission
- **Themes:** Atomic, molecular & optical physics; Condensed matter & materials

### 9. [State-selective dynamical freezing in driven Rydberg atom chains](https://arxiv.org/abs/2611.28215)
- **Abstract:** Floquet perturbation theory explains how interaction-dependent spin-flip amplitudes determine which initial states in driven Rydberg chains exhibit dynamical freezing.
- **Authors:** Madhumita Sarkar, Sougato Bose, Roopayan Ghosh
- **arXiv:** `2611.28215v1` (published 2026-11-20T19:00:03Z; categories: `quant-ph`, `cond-mat.stat-mech`, `cond-mat.str-el`)
- **Evidence for ranking:** Signal score 0.50 from 2 cross-lists (weighted component 0.50), linking quantum physics and statistical/strongly correlated matter. The ranking reflects cross-listing only; no external-attention component is recorded.
- **Claimed result:** The authors find that a many-body state freezes only when all available spin-flip interference amplitudes vanish, and identify spacing bounds outside which the benefit of two-frequency driving is lost.
- **Evidence type:** theoretical; Floquet perturbation theory for periodically driven interacting Rydberg chains.
- **Caveat:** The conclusions are tied to the model and driving regimes where the perturbative description is controlled; no experimental demonstration is reported in the abstract.
- **Announcement type:** new submission
- **Themes:** Quantum information; Condensed matter & materials

### 10. [Revealing Dark Matter in the Dark-Electron Rate of Xenon Detectors](https://arxiv.org/abs/2611.28211)
- **Abstract:** The authors propose using a much larger fraction of xenon detectors’ single-electron event rate in an annual-modulation search for sub-GeV dark matter and estimate the resulting sensitivity.
- **Authors:** Lillian Santos-Olmsted, Rebecca K. Leane, Carlos Blanco, John F. Beacom
- **arXiv:** `2611.28211v1` (published 2026-11-20T19:00:02Z; categories: `hep-ph`, `astro-ph.HE`, `hep-ex`)
- **Evidence for ranking:** Signal score 0.50 from 2 cross-lists (weighted component 0.50). The detector-data analysis proposal connects phenomenology and experiment; no external-attention component is recorded.
- **Claimed result:** Using measured dark-electron rates, the authors project that annual modulation could improve sensitivity for XENONnT, LZ, PandaX and future xenon detectors; this is a proposed analysis, not a dark-matter detection.
- **Evidence type:** forecast/proposal; sensitivity estimates based on measured single-electron rates from present and planned xenon experiments.
- **Caveat:** The projected gain depends on successfully extracting an annual modulation from backgrounds in the raw single-electron rate; no new signal is reported.
- **Announcement type:** new submission
- **Themes:** Particle, nuclear & high-energy physics; Instrumentation & detectors

## Trending Research Themes

- **Differentiable and numerically controlled physics models:** JAX-Nano embeds automatic differentiation in phonon-BTE simulation; the Thue–Morse baker-map work tests spectral behavior against a classical dynamical structure; and the multiscalar φ⁴ paper turns consistency conditions into an all-orders perturbative flow result. These are distinct applications, not a single shared method.
- **Higher-speed, more informative measurements:** The neuromorphic-camera VMI prototype targets event-level momentum imaging above 100 kHz, while the THz metasurface study combines near-field imaging with tunable collective resonances. The NiPS₃ study uses time-resolved spectroscopy to resolve strong-field carrier-generation dynamics. These are separate experiments rather than independent replications.
- **Non-equilibrium and driven quantum behavior:** NiPS₃ spectroscopy probes a strong-field tunneling/multiphoton crossover; the Rydberg-chain analysis studies drive-frequency-dependent freezing; and the open baker map relates quantum resonances to classical escape and entropy. The shared thread is driven or open-system dynamics, across experiment, many-body theory, and quantum chaos.
- **Astrophysical inference across scales:** Gaia DR3 accelerations are checked against resolved binary companions, whereas the triple-system simulations examine how inner-binary structure regulates mass transfer. One constrains existing catalog measurements; the other models an evolutionary process, so they are complementary rather than confirming one another.

## Open Problems and Research Directions

- **Author-stated — extend transport physics and scale:** JAX-Nano’s authors identify more comprehensive phonon dispersion/scattering and improved memory efficiency as future work. A follow-up could test those additions against independent thermal measurements and larger, experimentally specified device geometries (2611.28926).
- **Author-stated — improve astrometric validation coverage:** The Gaia analysis is limited by systems with too few resolved measurements and WDS resolution/mass uncertainties. New resolved astrometry and independent companion-mass constraints could enlarge orbit-fit validation and test the acceleration/jerk coefficients across more of the DR3 sample (2611.28969).
- **Synthesis — test triple-transfer model dependence:** The reported separation scaling assumes a particular polytropic donor and inner-binary setup, while numerical hydrostatic profiles depend on grid resolution. Simulations that vary donor structure, mass ratio and resolution, followed by searches for the predicted variability or circumbinary-disk signatures, could test how broadly the result applies (2611.28537).
- **Author-stated — establish quantum-map asymptotics:** The baker-map paper leaves the large-N limit of the leading resonance and the Fourier-basis fractal-Weyl exponent unresolved. Larger computations and the proposed extensions to asymmetric or multi-branch maps could determine whether the observed finite-size cascade persists (2611.28242).
- **Synthesis — validate the proposed low-threshold xenon analysis:** The sensitivity forecast relies on exploiting raw single-electron rates and annual modulation. Reanalyses of existing detector data should quantify time-dependent backgrounds and stability before interpreting any modulation as a dark-matter search result (2611.28211).
- **Synthesis — move calculated photonic enhancement toward measurement:** Since the THz paper’s Purcell enhancement is calculated, experiments coupling emitters to the tuned quasi-flat modes could test whether the predicted enhancement survives losses and fabrication tolerances (2611.28246).

## Takeaway

Today’s selected papers show a strong methods-and-measurement thread: differentiable transport solvers, sharper instrumentation, and detailed probes of driven or gravitational systems. The results range from laboratory observations to numerical models and sensitivity proposals; the sparse attention evidence means this report identifies cross-field notable work, not a reliable measure of what is most popular.

## Method and sources

- **Window:** daily arXiv announcement batch; eligible submission window 2026-11-20 19:00:00 UTC through 2026-11-23 19:00:00 UTC; announcement batch 2026-11-24 at 01:00 UTC. This uses today’s batch, not a prior batch.
- **Snapshot:** 2026-11-24 03:16:11 UTC; the supplied signal file was generated at 03:15:55 UTC.
- **Archive scope:** the collector’s configured physics corpus: `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`. Its arXiv source reported 240 records; the candidate file contains 150 entries. This is collector-based coverage, not a claim of a manual census beyond that pool.
- **Inference:** arXiv provides no official trending chart. The supplied deterministic signal file reports no candidates with external-attention signals (`with_attention: 0`); the selected entries’ scores come only from cross-listing at the configured weight 0.25 per cross-list. Score and cross-list counts are given per paper. Zero attention score is not evidence of low scientific importance. Same-score ordering is a qualitative selection based on the concrete result and coverage of distinct physics areas, not an unreported popularity metric. The report therefore calls these “notable recent papers,” not the hottest by measured readership.
- **Sources checked:** supplied signal file `/home/yizhuan/.research/physics/daily/arxiv-trending-physics-daily-2026-11-24.signals.json`; each of the 10 linked arXiv abstract pages was checked for title, authors, version, date, abstract, and categories. The full arXiv HTML was also inspected for the top three where available (JAX-Nano, Gaia validation, and tertiary mass transfer). Signal source statuses: arXiv, Hugging Face and Hacker News were reported `ok`; Semantic Scholar was unavailable in the supplied snapshot, so no citation counts or citation momentum are claimed. The signal file’s source counts and this snapshot do not establish independent expert coverage.
