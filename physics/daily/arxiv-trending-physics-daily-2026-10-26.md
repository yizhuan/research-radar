# arXiv Physics — Daily brief, Monday 26 October 2026

Six notable recent papers show a strong mix of instrument-led astronomy, model-based inference, and quantum error correction. This brief covers logical-qubit operations, the new GWTC-5 black-hole population analysis, an extensive 3I/ATLAS monitoring campaign, JWST's early-galaxy luminosity functions, simulated explanations of the Galactic-center gamma-ray excess, and twisted graphene spectroscopy. The ordering is inferred: arXiv publishes no official trending chart, and citation evidence is limited for these very recent papers.

Today is Tuesday, 27 October 2026. At the 01:24:54 UTC snapshot, the latest available announcement batch was Monday, 26 October. The daily window is exactly 2026-10-26 through 2026-10-26; it uses the prior batch because no Tuesday batch had appeared by the snapshot.

## Top papers (ranked)

### 1. [Entangled logical qubits on a superconducting quantum processor](https://arxiv.org/abs/2610.32347)
- **Abstract:** The authors demonstrate logical surface-code operations, entanglement, and teleportation on a 120-qubit superconducting processor using lattice surgery, fast reset, and noise-informed decoding.
- **Authors:** Robin Harper, Xanda C. Kolesnikow, Campbell K. McLauchlan, Georgia M. Nixon, Stephen D. Bartlett, Benjamin J. Brown
- **arXiv:** `2610.32347v1` (published 2026-10-23 08:40:47 UTC; categories: `quant-ph`)
- **Evidence for ranking:** A direct hardware demonstration extends beyond logical memory to two-logical-qubit Bell-state entanglement and three-logical-qubit teleportation on a named processor, with quantitative fidelities reported.
- **Claimed result:** The authors report logical Bell-state fidelities above 93%, teleportation fidelities of 78%–93%, and sub-1% logical error per round for distance-3 and distance-5 surface codes.
- **Evidence type:** experimental; 120 coupled superconducting qubits on IBM's `ibm_phoenix` processor, using surface codes and lattice surgery.
- **Caveat:** Results rely on excluding underperforming components and noise-informed decoding on this particular device; they are not yet a demonstration of a scalable, general-purpose fault-tolerant computer.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Quantum information; Instrumentation & detectors

### 2. [Three subpopulations of binary black holes in mass, spin magnitudes and tilts following GWTC-5](https://arxiv.org/abs/2610.32935)
- **Abstract:** Using 259 binary black holes in the fifth LIGO–Virgo–KAGRA catalog, the authors infer three mass-dependent subpopulations with distinct spin and mass-ratio distributions.
- **Authors:** Asad Hussain, Maximiliano Isi, Aaron Zimmerman
- **arXiv:** `2610.32935v1` (published 2026-10-23 17:31:43 UTC; categories: `astro-ph.HE`)
- **Evidence for ranking:** The analysis uses the new 259-event GWTC-5 catalog, reports a three-component population result, and introduces variance control for resolving concentrated spin features.
- **Claimed result:** The authors infer low-, medium-, and high-spin populations whose relative contributions vary with primary mass; the high-spin component dominates above roughly 60 solar masses.
- **Evidence type:** observational; hierarchical population inference from the LIGO–Virgo–KAGRA GWTC-5 catalog.
- **Caveat:** Population structure and component assignments depend on the chosen mixture model; a fourth component does not resolve into a distinct distribution, and the inferred groups do not by themselves identify unique formation channels.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Astrophysics; Cosmology & gravitation

### 3. [Comprehensive Visible and Near-infrared Keck and Gemini Monitoring and Characterization of Interstellar Comet 3I/ATLAS during its Encounter with the Solar System](https://arxiv.org/abs/2610.32972)
- **Abstract:** The authors report a multi-epoch optical and near-infrared observing record of interstellar comet 3I/ATLAS, tracing its dust activity, colours, gas ratios, and infrared spectrum from 2025 July to 2026 May.
- **Authors:** Bryce T. Bolin, Jeffrey Cooke, Brian C. Lemaux, Marco Micheli, Davide Farnocchia, et al.
- **arXiv:** `2610.32972v1` (published 2026-10-23 17:58:04 UTC; categories: `astro-ph.EP`, `astro-ph.GA`)
- **Evidence for ranking:** An unusually broad Keck/Gemini time series combines optical imaging and spectroscopy with near-infrared imaging and spectroscopy; it also connects planetary and galactic astrophysics.
- **Claimed result:** The authors find different inbound and outbound dust-activity trends and report no water-ice absorption robust to their tested continuum and calibration choices.
- **Evidence type:** observational; Keck/LRIS and MOSFIRE, Gemini/GMOS, Flamingos-2 and GNIRS observations.
- **Caveat:** Dust-loss estimates assume grain sizes of 1 μm–1 mm and a nucleus model; the ice non-detection is conditional on the tested spectral-continuum and calibration treatments.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Astrophysics; Instrumentation & detectors

### 4. [Galaxy Luminosity Functions at z~7-10 from Four Years of JWST Observations](https://arxiv.org/abs/2610.32307)
- **Abstract:** From four years of public JWST NIRCam imaging across nine fields, the authors estimate galaxy luminosity functions near redshifts 7.4 and 10, using NIRSpec confirmations to help quantify candidate contamination.
- **Authors:** Bangzheng Sun, Haojing Yan
- **arXiv:** `2610.32307v1` (published 2026-10-23 08:06:31 UTC; categories: `astro-ph.GA`)
- **Evidence for ranking:** The analysis combines nine JWST fields spanning about 1,045 square arcminutes with thousands of dropout candidates and hundreds of secure NIRSpec redshifts; the preprint says it was submitted to MNRAS.
- **Claimed result:** The authors report a Schechter-like z≈7.4 luminosity function with faint-end slope −1.70±0.16, while the z≈10 sample is better fit by a power law with slope −2.36±0.16.
- **Evidence type:** observational; JWST public NIRCam imaging and NIRSpec spectroscopic redshifts, with statistical incompleteness and contamination corrections.
- **Caveat:** The authors call for deeper imaging and spectroscopy near 30th magnitude to check the faint end and more bright-end spectroscopy (≲26th magnitude) to strengthen the z≈10 result.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Astrophysics; Instrumentation & detectors

### 5. [The Galactic Center Gamma-Ray Excess and the Look-Elsewhere Effect](https://arxiv.org/abs/2610.32845)
- **Abstract:** Time-dependent cosmic-ray transport in simulated Milky Way analogues produces transient diffuse gamma-ray residuals that can resemble the spectrum and morphology of the Fermi-LAT Galactic Center Excess.
- **Authors:** Isabel S. Sands, Philip F. Hopkins
- **arXiv:** `2610.32845v1` (published 2026-10-23 16:19:38 UTC; categories: `astro-ph.HE`, `astro-ph.CO`, `hep-ph`)
- **Evidence for ranking:** The work links high-energy astrophysics, cosmology, and particle phenomenology, replacing steady-state and axisymmetric simplifications with time-dependent, spectrally resolved cosmic-ray transport in full-MHD galaxy simulations.
- **Claimed result:** The authors find simulated residuals several times larger than the Fermi excess in some snapshots and suggest that a transient stellar-source fluctuation could mimic it.
- **Evidence type:** computational; full magnetohydrodynamic simulations of Milky Way analogues with time-dependent cosmic-ray transport.
- **Caveat:** This is a simulation-based interpretation, not a new Fermi-LAT detection or a demonstrated explanation of the excess; it depends on the simulated galaxy and cosmic-ray transport assumptions.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Astrophysics; Particle, nuclear & high-energy physics; Computational & data methods

### 6. [Nano-ARPES observation of a flat band at the M point in 2.4° twisted bilayer graphene](https://arxiv.org/abs/2610.32714)
- **Abstract:** Nano-ARPES measurements reveal a flat band near the M point, away from the usual K-point focus, in a 2.4° twisted bilayer graphene sample.
- **Authors:** Giovanna Feraco, Przemysław Przybysz, Oreste De Luca, Ying Wang, Pavel Dudin, et al.
- **arXiv:** `2610.32714v1` (published 2026-10-23 14:35:25 UTC; categories: `cond-mat.mes-hall`, `cond-mat.mtrl-sci`)
- **Evidence for ranking:** A direct spectroscopic observation reports an unexpected band location and motivates measurements across the Brillouin zone; the paper cross-lists mesoscopic physics and materials science.
- **Claimed result:** The authors report the first observation, in twisted bilayer graphene, of a flat band away from the K point, at M and far from the Fermi level.
- **Evidence type:** experimental; nano-focused angle-resolved photoemission spectroscopy (nano-ARPES) on 2.4° twisted bilayer graphene.
- **Caveat:** The reported feature is from a particular twist angle and does not itself establish a superconducting or other correlated phase; replication across samples and angles is needed to assess its generality.
- **Announcement type:** new submission, announcement-batch date 2026-10-26
- **Themes:** Condensed matter & materials; Instrumentation & detectors

## Trending Research Themes

- **Multi-instrument observations and large samples:** Keck/Gemini track 3I/ATLAS over many epochs, JWST combines nine fields and spectroscopic checks for early-galaxy luminosity functions, and GWTC-5 supports a 259-event black-hole population analysis. These are different targets and data products, not independent confirmations of one result.
- **Forward models for interpretation:** The Galactic-center excess paper compares time-variable simulated gamma-ray emission with Fermi-LAT residuals, while the GWTC-5 study uses flexible population mixtures and likelihood-variance control. These methods address distinct questions and systematics.
- **Logical quantum operations:** The superconducting-processor paper demonstrates lattice-surgery entanglement and teleportation beyond memory benchmarks. This is an isolated signal in this batch, not a cross-paper trend.
- **Spectroscopy beyond conventional targets:** 3I/ATLAS is characterized across optical and near-IR bands, while nano-ARPES maps a flat band at M in twisted graphene. These are separate applications of complementary instruments, not evidence for a shared mechanism.

## Open Problems and Research Directions

- **Author-stated open problem — 3I/ATLAS:** The water-ice feature is not robust to the tested continuum/calibration choices, and dust-loss conversion depends on grain and nucleus assumptions. **Follow-up synthesis:** repeat calibrated near-IR spectroscopy and multi-band monitoring, and test the inferred mass loss under alternative grain-size and nucleus models. [2610.32972]
- **Author-stated open problem — GWTC-5:** The number and properties of inferred subpopulations are sensitive to modeling choices, while an added fourth component is degenerate. **Follow-up synthesis:** compare alternative mixture structures and selection-function treatments as additional LVK events accumulate, rather than equating current components with formation channels. [2610.32935]
- **Author-stated open problem — JWST:** The authors request deeper imaging/spectroscopy near 30 mag and more spectroscopy at the bright end (≲26 mag). **Follow-up:** test the reported z≈7.4 faint-end slope and z≈10 bright-end behavior with those data. [2610.32307]
- **Author-stated open problem — Galactic-center excess:** Current diffuse-emission templates may miss time-dependent cosmic-ray transport. **Follow-up synthesis:** build time-dependent Fermi-LAT templates and test whether the simulated spectral and spatial residuals remain consistent across independent Milky Way analogues. This would test a proposal, not assume the excess is explained. [2610.32845]
- **Research-direction synthesis — logical qubits and twisted graphene:** Test logical Bell-state and teleportation performance across less selectively configured devices and larger code distances [2610.32347]; map twisted graphene across more angles and the full Brillouin zone to determine whether the M-point band is reproducible and how it evolves [2610.32714].

## Takeaway

The strongest signals in this batch are data-rich observations and experiments probing beyond established measurement baselines. The results remain constrained by model choices, calibration and sample dependence, and follow-up measurements; none should be read as a settled explanation of the Galactic-center excess, a confirmed early-universe luminosity-function shape, or scalable fault-tolerant quantum computing.

## Method and sources

- **Window:** daily; 2026-10-26 through 2026-10-26, the Monday announcement batch only. Snapshot: 2026-10-27 01:24:54 UTC. Because the run was early Tuesday and no Tuesday batch had appeared, the prior batch was used.
- **Archive coverage:** checked the latest pages for `physics`, `astro-ph`, `cond-mat`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`. The pages showed 458 category entries; deduplication by versionless arXiv ID yielded 348 distinct entries. Counts by archive were physics 86, astro-ph 75, cond-mat 97, gr-qc 32, hep-ex 13, hep-lat 5, hep-ph 23, hep-th 38, nucl-ex 7, nucl-th 10, and quant-ph 72. The six selected abstracts and version histories were checked on arXiv; HTML full text was inspected for the leading qubit, GWTC-5, and 3I/ATLAS papers.
- **Inference:** these six are presented as notable recent papers, not measured popularity. Placement prioritizes concrete datasets or instrument demonstrations, cross-subfield relevance, and reported results. No numeric trend score is used.
- **Attention evidence:** a Semantic Scholar Graph citation lookup was rate-limited (HTTP 429), so citation counts and momentum are not reported. Web search did not provide reliable independent coverage sufficient to establish a popularity ranking. Retrieval limitations are noted here, not treated as evidence for placement.
- **Sources:** [arXiv physics recent](https://arxiv.org/list/physics/recent), [astro-ph recent](https://arxiv.org/list/astro-ph/recent), [cond-mat recent](https://arxiv.org/list/cond-mat/recent), [gr-qc recent](https://arxiv.org/list/gr-qc/recent), [hep-ex recent](https://arxiv.org/list/hep-ex/recent), [hep-lat recent](https://arxiv.org/list/hep-lat/recent), [hep-ph recent](https://arxiv.org/list/hep-ph/recent), [hep-th recent](https://arxiv.org/list/hep-th/recent), [nucl-ex recent](https://arxiv.org/list/nucl-ex/recent), [nucl-th recent](https://arxiv.org/list/nucl-th/recent), [quant-ph recent](https://arxiv.org/list/quant-ph/recent). Paper-specific sources are linked in each title; HTML full text was inspected at [2610.32347](https://arxiv.org/html/2610.32347), [2610.32935](https://arxiv.org/html/2610.32935), and [2610.32972](https://arxiv.org/html/2610.32972).
