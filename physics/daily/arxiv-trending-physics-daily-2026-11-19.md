# arXiv Physics — Daily notable papers, 19 November 2026

## Headline

For the supplied 19 November 2026 arXiv window, 10 papers are selected. The strongest repeated pattern is quantum-information methods crossing into many-body simulation, error correction, dark-matter detection proposals, and formal complexity theory; computational tools also connect astrophysics, fluid physics, and gravity. Spoken agenda: quantum algorithms and detectors, then a gamma-ray pulsar result, followed by topology, atmospheric dynamics, and accelerator physics. This is an inferred ordering, not an official arXiv trending chart; the selected papers have only one or two Semantic Scholar citations each and no matching Hugging Face or Hacker News signals, so popularity evidence is limited. This follows the supplied 19 November signals file; a separate report for the newer 20 November batch already exists.

Window: 2026-11-18T19:00:00Z to 2026-11-19T19:00:00Z; announcement batch date 2026-11-19, announced 2026-11-20T01:00:00Z. This is a prior batch relative to the snapshot.

## Top papers (ranked)

### 1. [High-Accuracy Neural-Network Quantum States via Randomized Real-Time Dynamics](https://arxiv.org/abs/2611.26587)
- **Abstract:** Dynamical averaging evolves a neural-network quantum state or observable in real time to suppress ground-state observable errors quadratically in the state error, demonstrated on non-integrable spin models.
- **Authors:** John M. Martyn, Rod Rofougaran, Samuel Stein, Di Luo
- **arXiv:** `2611.26587v1` (published 2026-11-19T18:45:45Z; categories: `quant-ph` (primary), `cond-mat.dis-nn`, `cond-mat.str-el`, `physics.comp-ph`)
- **Evidence for ranking:** Collector score 2.947; Semantic Scholar current citations 2 (score component 2.197), 3 cross-lists (component 0.750); no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The authors prove up-to-quadratic suppression of errors in arbitrary ground-state observables and demonstrate faster convergence and lower correlation-function and magnetization errors in 1D and 2D non-integrable spin models.
- **Evidence type:** computational; theoretical error analysis and numerical non-integrable spin-model tests.
- **Caveat:** The Schrödinger-picture method requires real-time state evolution, which can be costly; the cheaper Heisenberg approximation assumes support predominantly on a few low-energy eigenstates and can incur additional errors or instabilities when that assumption fails.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Quantum information; Condensed matter & materials; Computational & data methods

### 2. [Numerical Implementation and Tests of the Quadratic Effective Action for Lorentzian Spinfoam Amplitudes](https://arxiv.org/abs/2611.25031)
- **Abstract:** The authors implement and numerically test a quadratic effective-action approximation for Lorentzian EPRL spinfoam amplitudes on several triangulations, including a 24-simplex hypercube.
- **Authors:** Dongxue Qu, Sean Tobin, Hongguang Liu, Muxin Han
- **arXiv:** `2611.25031v1` (published 2026-11-18T19:00:03Z; categories: `gr-qc` (primary), `hep-th`)
- **Evidence for ranking:** Collector score 2.329; Semantic Scholar current citations 1 (component 1.386), 1 influential citation (component 0.693), and 1 cross-list (component 0.250); no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The authors report that the quadratic action reproduces the Regge action and its curvature correction in the tested cases, and matches the nonlinear complex-critical-point action through cubic-order remainders for finite edge-length perturbations.
- **Evidence type:** computational; Julia implementations tested on double-Δ3 and 1–5 Pachner complexes, a refinement, and a 24-simplex hypercube.
- **Caveat:** The results are a local perturbative expansion around one flat real critical point; other critical points and integration-domain boundary contributions are neglected, as are subleading 1/J terms.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Cosmology & gravitation; Computational & data methods

### 3. [Theory of Particle Scattering on Superconducting Qubits: From Single Devices to Quantum Arrays](https://arxiv.org/abs/2611.25013)
- **Abstract:** The authors model finite-momentum particle scattering from superconducting qubits and project sensitivity to eV–keV bosonic dark matter, including possible collective enhancement in coherent qubit arrays.
- **Authors:** Doojin Kim, Kyoungchul Kong, Myeonghun Park
- **arXiv:** `2611.25013v1` (published 2026-11-18T19:00:00Z; categories: `hep-ph` (primary), `quant-ph`)
- **Evidence for ranking:** Collector score 2.329; Semantic Scholar current citations 1 (component 1.386), 1 influential citation (component 0.693), and 1 cross-list (component 0.250); no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** For a modeled Xmon transmon, the authors find improved projected low-mass sensitivity; independent qubits give a rate proportional to N, while suitably prepared spatially coherent Dicke states can approach N² scaling.
- **Evidence type:** theoretical; device-response calculation for a planar Xmon-style transmon and dark-matter sensitivity projections.
- **Caveat:** The sensitivity is projected, not an observed signal; it depends on the modeled device response, and the near-N² collective enhancement requires maintained spatial coherence and suitable Dicke-state preparation.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Particle, nuclear & high-energy physics; Quantum information

### 4. [Evolving Decoding Algorithms for Quantum Error Correction](https://arxiv.org/abs/2611.25880)
- **Abstract:** Grammatical evolution over a decoder-specific language finds quantum LDPC belief-propagation decoders with improved time–logical-error trade-offs.
- **Authors:** Eduardo Dueñez, Edgar Said Hernandez Sanchez, Edgar A. Duéñez-Guzmán, Suzanne Sadedin
- **arXiv:** `2611.25880v1` (published 2026-11-19T10:36:21Z; categories: `quant-ph` (primary), `cs.AI`, `cs.MA`, `cs.NE`)
- **Evidence for ranking:** Collector score 2.136; Semantic Scholar current citations 1 (component 1.386), 3 cross-lists (component 0.750); the arXiv comment notes NeurIPS 2026 EvoRobust Workshop acceptance; no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The authors report evolved decoders that reduce logical errors or runtime relative to specified BP+OSD baselines and generalize across tested noise levels, code sizes, and round counts.
- **Evidence type:** computational; decoder simulations on quantum low-density-parity-check codes using a DSL and grammatical evolution.
- **Caveat:** The reported gains are benchmark results in the tested code and noise settings; the preprint does not demonstrate real-time deployment on a quantum processor.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Quantum information; Computational & data methods

### 5. [Physics-Informed Deep Learning for Shear Wave Speed Estimation in MR Elastography](https://arxiv.org/abs/2611.26111)
- **Abstract:** An end-to-end physics-informed neural reconstruction and inversion method estimates tissue shear-wave speed directly from undersampled MR elastography k-space data.
- **Authors:** Stefan Martin, Jakob Schattenfroh, Patrick Schuenke, Felix Frederik Zimmermann, Ingolf Sack, et al.
- **arXiv:** `2611.26111v1` (published 2026-11-19T13:39:46Z; categories: `eess.IV` (primary), `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** Collector score 1.886; Semantic Scholar current citations 1 (component 1.386), 2 cross-lists (component 0.500); the arXiv comment gives a journal DOI and public code; no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The authors report a 30% lower NRMSE than total-variation minimization and accurate SWS mapping at acceleration factors up to 19, with evaluation on retrospective brain data and in-vivo data.
- **Evidence type:** computational; retrospective highly undersampled brain MR elastography data, comparison with total-variation minimization, and in-vivo evaluation.
- **Caveat:** The reported comparison is tied to the studied data and reconstruction setup; broader prospective and multi-site validation is not established in the abstract.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Instrumentation & detectors; Computational & data methods

### 6. [Gamma-Ray Pulsar Discovery Using a Lattice-Based Method](https://arxiv.org/abs/2611.26425)
- **Abstract:** A lattice-based search of 15 years of Fermi-LAT data finds the isolated 261-Hz gamma-ray pulsar PSR J1622−7204 using about ten CPU hours.
- **Authors:** Daniel Pook-Kolb, Dotan Gazith, Colin J. Clark, Erik Agrell, Barak Zackay, Bruce Allen
- **arXiv:** `2611.26425v1` (published 2026-11-19T17:03:45Z; categories: `astro-ph.HE` (primary), `astro-ph.IM`)
- **Evidence for ranking:** Collector score 1.636; Semantic Scholar current citations 1 (component 1.386) and 1 cross-list (component 0.250); the paper has a Physical Review Letters reference and DOI; no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The authors report the first gamma-ray pulsar discovery using their lattice-based method and contrast its roughly ten CPU hours with about 600 CPU-years spent by an earlier semicoherent search that did not find the source.
- **Evidence type:** observational; computational lattice search of Fermi-LAT Pass 8 photon-arrival data and source-probability weights.
- **Caveat:** The authors estimate success in only about 1% of random 80-photon subsets; the demonstrated search assumes an isolated pulsar and a simplified pulse profile, while binary-pulsar searches remain prospective.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Astrophysics; Computational & data methods; Instrumentation & detectors

### 7. [Classical Oracle Separation of QMA from the QCMA Hierarchy and Quantum Cryptography Even When P = QCMA](https://arxiv.org/abs/2611.26574)
- **Abstract:** In the query-complexity model, a new codeword-hash-pairs-in-noise problem yields a classical-oracle separation of QMA from the QCMA hierarchy and enables quantum cryptographic primitives in a relativized setting.
- **Authors:** Alper Cakan
- **arXiv:** `2611.26574v1` (published 2026-11-19T18:40:14Z; categories: `quant-ph` (primary), `cs.CR`)
- **Evidence for ranking:** Collector score 1.636; Semantic Scholar current citations 1 (component 1.386) and 1 cross-list (component 0.250); the arXiv comment notes submission to STOC’27; no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The author proves an oracle-relative separation in which P, BQP, QCMA, and the QCMA hierarchy coincide while QMA is strictly stronger, and constructs specified quantum cryptographic primitives relative to such an oracle.
- **Evidence type:** theoretical; query-complexity proofs in a classical-oracle model.
- **Caveat:** These are relativized complexity-theory results; an oracle separation does not by itself establish the corresponding unrelativized separation or practical cryptographic construction.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Quantum information; Computational & data methods

### 8. [Multi-scale dynamics of deep convective self-aggregation. Part II: scale-by-scale budget and mesoscale self-similarity](https://arxiv.org/abs/2611.25829)
- **Abstract:** A scale-by-scale analysis of deep convective self-aggregation finds an inverse energy cascade mediated by mesoscale circulations and a self-similar frozen-moist-static-energy variance scaling.
- **Authors:** Lorenzo Silvestri, Paolina Bongioannini Cerlini, Andrea Cimarelli
- **arXiv:** `2611.25829v1` (published 2026-11-19T09:44:28Z; categories: `physics.ao-ph` (primary), `physics.flu-dyn`)
- **Evidence for ranking:** Collector score 1.636; Semantic Scholar current citations 1 (component 1.386) and 1 cross-list (component 0.250); no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The authors derive a generalized Yaglom relation and report FMSE variance scaling approximately as r^(6/5), with departures below 100 km and below 750 m elevation; horizontal-velocity scaling retains height dependence.
- **Evidence type:** theoretical; generalized structure-function and scale-dependent budget analysis of deep convective self-aggregation.
- **Caveat:** The reported power laws break down at small horizontal scales below 100 km and below 750 m, and the velocity scaling retains residual height dependence.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Plasma & fluid physics; Computational & data methods

### 9. [Topological (in)equivalence encoded in zeros of wavefunction overlaps](https://arxiv.org/abs/2611.25037)
- **Abstract:** The authors encode relative topology of two-dimensional gapped band structures in phase-winding charges at zeros of the determinant of occupied-state overlaps.
- **Authors:** Carolina Paiva, Bruno Mera, Roni Ilan, Raquel Queiroz
- **arXiv:** `2611.25037v1` (published 2026-11-18T19:00:05Z; categories: `cond-mat.mes-hall` (primary), `math-ph`)
- **Evidence for ranking:** Collector score 1.636; Semantic Scholar current citations 1 (component 1.386) and 1 cross-list (component 0.250); no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** For class A, the total zero charge equals the Chern-number difference; for class AII, the parity of charge in half the Brillouin zone gives the relative Z2 invariant, illustrated in Haldane, Kane–Mele, and Qi–Wu–Zhang models.
- **Evidence type:** theoretical; topological band-theory derivation and model examples.
- **Caveat:** The construction is developed for gapped band structures in specified symmetry classes; it is a theoretical classification framework, not an experimental measurement of a material.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Condensed matter & materials

### 10. [Hydrodynamic modeling of liquid metal field emitter deformation under combined RF and DC magnetic fields](https://arxiv.org/abs/2611.26518)
- **Abstract:** Hydrodynamic and magnetohydrodynamic simulations examine how combined RF and DC magnetic fields deform a liquid-copper field emitter in accelerator cavities.
- **Authors:** Yuan-Zhi Lim, Juliette Plouin, Guillaume Ferrand
- **arXiv:** `2611.26518v1` (published 2026-11-19T17:59:22Z; categories: `physics.acc-ph` (primary))
- **Evidence for ranking:** Collector score 1.386; Semantic Scholar current citations 1 (score component 1.386); the arXiv comment says the work was submitted to Physical Review Accelerators and Beams; no matching Hugging Face upvote or Hacker News discussion signal.
- **Claimed result:** The authors find in their simulations that sufficiently high local RF electric fields can deform the emitter and potentially eject hot copper droplets into the cavity, a proposed contributor to RF breakdown.
- **Evidence type:** computational; COMSOL Navier–Stokes, electromagnetic-field, and level-set simulations of a liquid-copper emitter.
- **Caveat:** The proposed droplet-emission mechanism is simulation-based and has not been established here by direct observation in an operating RF cavity.
- **Announcement type:** new submission, 2026-11-19 announcement batch.
- **Themes:** Instrumentation & detectors; Plasma & fluid physics

## Trending Research Themes

- **Quantum information as a bridge:** dynamical averaging for neural-network quantum states (#1), evolved qLDPC decoders (#4), superconducting-qubit scattering targets (#3), and oracle-based complexity results (#7) span simulation, fault tolerance, sensing, and theory. These are distinct contributions, not evidence of one shared platform.
- **Physics gains from computational methods:** numerical spinfoam tests (#2), a lattice-based Fermi-LAT search (#6), neural MRE inversion (#5), and COMSOL field-emitter simulations (#10) turn difficult inference or modeling problems into concrete workflows; their validation bases differ substantially.
- **Topology and multiscale structure:** the overlap-zero construction links Chern and Z2 band invariants (#9), while the convection paper derives scale-dependent energy and moisture-transport relations (#8). These are separate theoretical results, not a common dataset or independent confirmation.
- **Isolated signal in observational astrophysics:** the Fermi-LAT pulsar search (#6) is the selected corpus’s direct astrophysical discovery; no second selected paper uses the same instrument or source, so it should not be read as an instrument-wide trend.

## Open Problems and Research Directions

- **Author-stated limitation — NQS averaging:** the cheaper Heisenberg-picture approximation relies on low-energy support and may become unstable when that assumption fails (#1). **Research direction (synthesis):** test operator-evolution approximations on larger spin systems and excited-state or tensor-network ansätze, measuring accuracy against computational cost.
- **Author-stated limitation — spinfoam expansion:** the numerical study neglects other critical points, boundary contributions, and subleading 1/J terms (#2). **Research direction (synthesis):** extend to refinement sequences at fixed physical geometry and include multiple saddles and subleading corrections, as the paper identifies as follow-up work.
- **Open problem — dark-matter qubit targets:** the reported sensitivity is projected, with collective gains requiring spatial coherence (#3). **Research direction (synthesis):** measure finite-momentum transition response and background rates in realistic devices, then test whether coherence and frequency multiplexing survive in arrays.
- **Author-stated limitation — gamma-ray pulsar search:** success was estimated at about 1% per random 80-photon subset; binary systems and more complex profiles remain future targets (#6). **Research direction (synthesis):** validate success rates across additional Fermi-LAT sources and develop orbital-parameter searches before treating binary sensitivity as demonstrated.
- **Observed scale break — deep convection:** the FMSE scaling fails below 100 km and below 750 m, and velocity increments retain height dependence (#8). **Research direction (synthesis):** compare simulations and observations across those transition scales to determine how boundary-layer stratification sets the break.

## Takeaway

Across this batch, concrete outcomes range from a reported gamma-ray pulsar and decoder benchmarks to theoretical tools for quantum simulation, scattering, and gravity; several promising results remain model- or simulation-dependent.

## Method and sources

- **Window:** The supplied signals file covers 2026-11-18T19:00:00Z–2026-11-19T19:00:00Z, labels the batch 2026-11-19, and gives announcement time 2026-11-20T01:00:00Z. Snapshot time is recorded in the JSON sidecar. This is a prior batch relative to the snapshot. A newer report for the 20 November batch exists; this file intentionally follows the supplied 19 November signals rather than silently substituting another window.
- **Coverage:** The supplied pool contains 444 papers across `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`. All configured archives are represented in the collector's category query; the signal metadata reports 444 arXiv listings, 444 Semantic Scholar lookups, 175 arXiv metadata lookups, 141 Hugging Face matches, and 35 Hacker News matches. All five sources report status `ok`. The ten selected papers are v1 submissions in the supplied window; all ten arXiv records were verified through the official arXiv API, including ID, version, title, authors, abstract, dates, and categories. The top three full texts were checked in arXiv HTML for introduction, methods, results, and limitations.
- **Inference:** Scores and score components are taken from the supplied deterministic signals file. The selected papers have one or two current Semantic Scholar citations each (totals, not gains during the window); none had a matched Hugging Face upvote or Hacker News discussion. Scores rely on citation and cross-list components, with journal/publication or concrete-result signals used to break ties. Missing social matches are not evidence of unimportance. No independent external coverage signal was used for ranking.
- **Sources:** [arXiv physics](https://arxiv.org/list/physics/recent), [astro-ph](https://arxiv.org/list/astro-ph/recent), [cond-mat](https://arxiv.org/list/cond-mat/recent), [gr-qc](https://arxiv.org/list/gr-qc/recent), [hep-ex](https://arxiv.org/list/hep-ex/recent), [hep-lat](https://arxiv.org/list/hep-lat/recent), [hep-ph](https://arxiv.org/list/hep-ph/recent), [hep-th](https://arxiv.org/list/hep-th/recent), [nucl-ex](https://arxiv.org/list/nucl-ex/recent), [nucl-th](https://arxiv.org/list/nucl-th/recent), and [quant-ph](https://arxiv.org/list/quant-ph/recent); supplied signal file `arxiv-trending-physics-daily-2026-11-19.signals.json`; primary arXiv records linked above.
