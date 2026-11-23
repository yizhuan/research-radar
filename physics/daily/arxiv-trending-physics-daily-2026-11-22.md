# Physics on arXiv | 22 November 2026 announcement batch | 6 notable papers

Today's selected set leans toward model-guided physics: authors use numerical or analytical frameworks to separate mechanisms, optimize measurement, and assess computational methods. The agenda: fracture and electrolyte physics, cold-atom thermometry, Rydberg sensing, quantum simulation, and topological solitons. This is an inferred ranking, not an official arXiv trending chart; the candidate pool registered no external-attention matches, and citation evidence is limited for papers only days old, so treat these as notable recent papers rather than a popularity list.

## Top papers (ranked)

### 1. [Disentangling Lengthscales in Disordered Fracture](https://arxiv.org/abs/2611.27581)
- **Abstract:** The authors use a two-dimensional random fuse model to distinguish the disorder-dependent screening length of crack-tip damage from the length in Bažant's size-effect law, and propose pre-failure microfracture percolation as a possible origin of the latter.
- **Authors:** Matthaios Chouzouris, Marcelo A. Dias
- **arXiv:** `2611.27581v1` (published 2026-11-20 13:14:40 UTC; categories: `cond-mat.soft`, `cond-mat.dis-nn`, `cond-mat.other`, `cond-mat.stat-mech`, `physics.app-ph`)
- **Evidence for ranking:** Candidate-pool score 1.00, the highest among selected papers, entirely from four cross-lists (4 × 0.25); the score is not an attention measure.
- **Claimed result:** In simulations, the statistical fracture-process-zone length scales approximately as disorder strength to the first power, while the size-effect-law length and crack extension scale near disorder strength to the 1.34 power; the authors suggest percolation of microfractures may explain the latter.
- **Evidence type:** computational; two-dimensional Weibull-disordered random fuse simulations (L=128, 2,000 runs for each notch/disorder pair) with a coarse-grained load-redistribution model.
- **Caveat:** This is an idealized 2D model, not a measurement on real materials; the authors note that the origins and scaling of damage zones, particularly in more brittle regimes, remain open.
- **Announcement type:** new submission, 22 November 2026 announcement batch
- **Themes:** Condensed matter & materials; Computational & data methods

### 2. [Bayesian Quantum Thermometry of Ultracold Gases with Non-Equilibrium Single-Atom Probes](https://arxiv.org/abs/2611.27584)
- **Abstract:** The authors experimentally infer an ultracold bath's temperature from non-equilibrium spin-exchange dynamics of single-atom probes and find that adaptive Bayesian measurement reaches a prescribed precision with 2.5 times fewer measurements than an unoptimized protocol.
- **Authors:** Julian Feß, Luca Granert, Sabrina Burgardt, Silvia Hiebel, Alexander Guthmann, Mohammad Mehboudi, Martí Perarnau-Llobet, Artur Widera
- **arXiv:** `2611.27584v1` (published 2026-11-20 13:16:04 UTC; categories: `cond-mat.quant-gas`, `cond-mat.stat-mech`, `physics.data-an`, `quant-ph`)
- **Evidence for ranking:** Candidate-pool score 0.75 from three cross-lists; the paper also links an openly available supporting-data deposit (Zenodo DOI 10.5281/zenodo.24390998), which is context rather than a component of that score.
- **Claimed result:** The authors report that adaptive expected-information-gain measurements reduce the number of measurements needed for a target precision by a factor of 2.5 versus the unoptimized protocol, with estimates compared against time-of-flight references.
- **Evidence type:** experimental; individually measured 133Cs probe atoms in a thermal 87Rb bath, with Bayesian inference on spin populations and independent time-of-flight reference thermometry.
- **Caveat:** The inference uses an independently measured bath atom number and a model of spin-exchange rates; the authors note a trade-off between information efficiency and setup-specific control/measurement overhead.
- **Announcement type:** new submission, 22 November 2026 announcement batch
- **Themes:** Quantum information; Atomic, molecular & optical physics; Computational & data methods

### 3. [Molecular structure breaks universality in screening behavior of electrolyte solutions](https://arxiv.org/abs/2611.27955)
- **Abstract:** Using machine-learned classical density functional theory, the authors find that solvent polarity, solvent attraction, and ionic structure change screening modes and exponents, challenging a universal scaling law across concentrated electrolyte models.
- **Authors:** Anna T. Bui, Connie J. Fairchild, Dominic P. W. Thomas, Stephen J. Cox
- **arXiv:** `2611.27955v1` (published 2026-11-20 18:27:33 UTC; categories: `cond-mat.stat-mech`, `cond-mat.soft`, `physics.chem-ph`, `physics.comp-ph`)
- **Evidence for ranking:** Candidate-pool score 0.75 from three cross-lists; the work addresses a live disagreement over concentrated-electrolyte screening with a systematic hierarchy of model complexity.
- **Claimed result:** The authors report that solvent attraction can introduce a monotonic decay mode, solvent polarity can produce re-entrant screening, and ionic structure can alter screening exponents; they conclude no single scaling law applies across their molecularly distinct models.
- **Evidence type:** computational; machine-learned classical density functional theory applied to electrolyte models with increasing solvent and ionic detail.
- **Caveat:** These are model-based calculations, not a new measurement of electrolyte screening; the correspondence between the model hierarchy and specific real solutions needs experimental testing.
- **Announcement type:** new submission, 22 November 2026 announcement batch
- **Themes:** Condensed matter & materials; Computational & data methods

### 4. [A Microwave-Photonics Formulation of the Rydberg-Atom Receiver](https://arxiv.org/abs/2611.27942)
- **Abstract:** The author formulates a warm-vapor Rydberg receiver as an intensity-modulated optical link and derives its RF link-budget metrics from a velocity-averaged four-level atomic response, while finding its noise figure limits general antenna replacement.
- **Authors:** David Rosser
- **arXiv:** `2611.27942v1` (published 2026-11-20 18:16:06 UTC; categories: `quant-ph`, `eess.SP`, `physics.app-ph`, `physics.atom-ph`)
- **Evidence for ranking:** Candidate-pool score 0.75 from three cross-lists; the paper supplies checkable quantitative model comparisons for a cross-field sensing device.
- **Claimed result:** For a rubidium transition at 17.04 GHz, closed-form estimates agree with a velocity-resolved density-matrix model to 1% for slope and intercepts and 10% for bandwidth; they underestimate group delay by about one-third.
- **Evidence type:** theoretical; closed-form warm-vapor response compared with a velocity-resolved density-matrix model.
- **Caveat:** The paper's own analysis says the warm-vapor noise figure rules out the receiver as a general substitute for a conventional antenna and low-noise amplifier.
- **Announcement type:** new submission, 22 November 2026 announcement batch
- **Themes:** Atomic, molecular & optical physics; Instrumentation & detectors; Quantum information

### 5. [Optimised 8th-Order Trotter-Suzuki Schemes for Quantum Simulation](https://arxiv.org/abs/2611.27896)
- **Abstract:** The authors construct optimized general eighth-order product formulas for quantum dynamics, benchmark them on a Heisenberg XZ chain, and simulate noisy circuits to assess when the schemes could outperform lower-order alternatives.
- **Authors:** Marko Maležič, Johann Ostmeyer
- **arXiv:** `2611.27896v1` (published 2026-11-20 17:36:11 UTC; categories: `quant-ph`, `cond-mat.stat-mech`, `cond-mat.str-el`, `hep-lat`)
- **Evidence for ranking:** Candidate-pool score 0.75 from three cross-lists; the paper adds an explicit many-body benchmark and a noisy-circuit comparison rather than a formal construction alone.
- **Claimed result:** The authors report improved theoretical efficiency over prior state-of-the-art schemes and find their recommended formulas become competitive as hardware noise falls toward fault-tolerant levels.
- **Evidence type:** computational; product-formula analysis, Heisenberg XZ-chain simulations, and simulated noisy circuits using the qiskit-omelyan plugin.
- **Caveat:** At the noise levels modeled as current, the paper finds the Leapfrog scheme remains the best choice; the proposed gains are not demonstrated on quantum hardware.
- **Announcement type:** new submission, 22 November 2026 announcement batch
- **Themes:** Quantum information; Condensed matter & materials; Computational & data methods

### 6. [Neural variational Skyrmions as a topological benchmark: emergent symmetry, precision energies and KAN--MLP comparison](https://arxiv.org/abs/2611.27411)
- **Abstract:** Neural variational optimization produces three-dimensional Skyrmions with charges 1–4 without a symmetry ansatz, recovers familiar shapes, and compares Kolmogorov–Arnold networks with multilayer perceptrons across more than a thousand training runs.
- **Authors:** Koji Hashimoto, Masaki Murata, Gakuto Ogiwara
- **arXiv:** `2611.27411v1` (published 2026-11-20 10:16:13 UTC; categories: `hep-th`, `cs.LG`, `nucl-th`, `physics.comp-ph`)
- **Evidence for ranking:** Candidate-pool score 0.75 from three cross-lists; the authors also provide code and data (Zenodo DOI 10.5281/zenodo.24390286), a reproducibility signal not included in the score.
- **Claimed result:** The authors report spontaneous emergence of toroidal, tetrahedral, and cubic solutions, topological-charge errors at most 10^-6 in their highest-precision solutions, and a KAN parameter-efficiency advantage that largely disappears against tuned MLPs.
- **Evidence type:** computational; neural variational solutions of the three-dimensional Skyrme model, checked against physical constraints, independent quadratures, resolution sweeps, and over 1,000 network-training runs.
- **Caveat:** Results cover charges 1–4 in this model; the apparent KAN advantage depends on the comparison protocol, since tuned MLPs perform at least as well at fixed wall-clock time.
- **Announcement type:** new submission, 22 November 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

## Trending Research Themes

- **Physics through computational models.** Several papers use model construction and controlled numerical comparison to expose mechanisms or algorithmic limits: a coarse-grained fracture model and fuse simulations (Chouzouris & Dias), machine-learned density functional theory for electrolyte screening (Bui et al.), product-formula/noise simulations (Maležič & Ostmeyer), and variational soliton computation (Hashimoto et al.). These are distinct applications, not independent confirmations of one result.
- **Quantum measurement and sensing.** The cold-atom thermometry experiment (Feß et al.) turns probe spin dynamics into adaptive temperature estimates; the Rydberg receiver analysis (Rosser) translates atomic response into RF link-budget metrics. One is an experiment and the other a theoretical device analysis, so they do not independently validate a shared performance claim.
- **Cross-archive physics methods.** The selected corpus spans condensed matter, atomic physics, quantum information, and high-energy/nuclear theory, with computational methods serving as a bridge. Cross-listing contributes to the candidate scores, but does not by itself establish readership or scientific influence.

## Open Problems and Research Directions

- **Fracture length scales — open problem (authors):** The relation between the statistical fracture-process zone, the equiprobable damage zone, and the size-effect-law length remains unresolved, especially at low disorder and in more brittle materials (Chouzouris & Dias). **Research direction (synthesis):** test the proposed microfracture-percolation interpretation across lattice sizes, disorder distributions, three-dimensional models, and laboratory fracture data.
- **Probe calibration and practical cost — open problem (authors):** The thermometry analysis currently treats bath atom number as an independently measured input; the authors suggest joint temperature/atom-number estimation and note that laboratory time and adaptive-control overhead can change which protocol is preferable (Feß et al.). **Research direction (synthesis):** compare joint inference and protocol wall-clock cost across wider temperature intervals and independently calibrated baths.
- **Concentrated-electrolyte screening — open problem (authors):** Whether a universal screening law exists at high ionic strength remains unsettled, and extracting asymptotic decay lengths is difficult in simulation because of long-range tails and finite-size effects (Bui et al.). **Research direction (synthesis):** measure matched electrolyte compositions while comparing explicit-solvent simulations and the paper's cDFT model hierarchy, with finite-size and nonequilibrium controls.

## Takeaway

The most coherent pattern in this batch is not a single discovery but a set of tools that connect microscopic models to measurable or computationally testable quantities. The clearest near-term experimental signal is adaptive single-atom thermometry; the fracture and electrolyte results are promising mechanisms from models, and should not be mistaken for validation in real materials or solutions.

## Method and sources

- **Window:** daily arXiv announcement batch covering first submissions or revisions from 2026-11-19 19:00 UTC through 2026-11-20 19:00 UTC; announced 2026-11-23 01:00 UTC as the 2026-11-22 batch. Snapshot: 2026-11-23 17:18 UTC.
- **Coverage:** the supplied signal pool covers `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`; it reports 363 arXiv candidates. All six selected IDs were checked against their arXiv abstract pages and version/category metadata; full HTML was inspected for the top three.
- **Inference:** the provided signal file is the primary attention source. It reports zero candidates with external attention (`with_attention: 0`); these six therefore are described as notable recent papers, not measured popular papers. Selected scores are 1.00 (four cross-lists) and 0.75 (three cross-lists), using the file's 0.25-per-cross-list weight. Ranking ties were ordered using checkable result/resource context, not a claim of measured attention. Zero score or no external signal is not evidence of low scientific importance.
- **Unavailable signal:** Semantic Scholar citation and influential-citation data were unavailable for this run; Hugging Face and Hacker News source collections themselves completed, but the candidate pool had no attention matches. No citation totals are inferred or represented as period gains.
- **Sources:** arXiv abstract/full-text pages for each linked paper; supplied `arxiv-trending-physics-daily-2026-11-22.signals.json` (arXiv candidate pool, cross-list counts and scores; Hugging Face/Hacker News matching; Semantic Scholar status); linked Zenodo deposits for Feß et al. and Hashimoto et al.
