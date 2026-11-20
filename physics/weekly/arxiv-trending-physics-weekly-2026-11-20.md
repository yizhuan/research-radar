# arXiv physics weekly: notable recent papers | 14–20 November 2026

Eight papers selected from the physics-group archives show a recurring push toward model-aware inference and benchmarking: from atom-resolved electron microscopy to quantum-device characterization and weather-model ensembles. Brief agenda: the strongest measurements and methods first, then what their shared limitations suggest. This is an inferred ranking, not an official arXiv trending chart; arXiv publishes no such chart, and citation evidence for papers this new is sparse, so the ordering cannot establish popularity.

Window: 2026-11-14 through 2026-11-20 (inclusive); snapshot: 2026-11-20 02:41:21 UTC. At the snapshot, the latest available announcement batch in this window was 2026-11-19; no 2026-11-20 submissions were yet present in the queried API results.

## Top papers (ranked)

### 1. [4D-TEMPO: Differentiable 4D-STEM ptychography via fast Physics Optimizers](https://arxiv.org/abs/2611.24776)
- **Abstract:** The authors introduce a differentiable physical renderer that fits atoms, microscope, and detector directly to 4D-STEM counts, returning per-atom Fisher-information uncertainties and improving tested reconstructions.
- **Authors:** Ramani Duraiswami, Yichao Zhang
- **arXiv:** `2611.24776v1` (published 2026-11-18T17:23:50Z; categories: `physics.ins-det`, `cond-mat.mtrl-sci`, `cs.CV`, `math-ph`, `physics.comp-ph`)
- **Evidence for ranking:** Five category listings span instrumentation, materials, computer vision, mathematical physics, and computational physics; the paper benchmarks against existing codes on simulated and experimental 4D-STEM data and reports held-out prediction and runtime comparisons.
- **Claimed result:** The authors report improved atomic-position errors on simulated WSe₂, better held-out-pattern prediction on experimental WSe₂, and faster benchmark runs, with model-conditional per-atom error bars.
- **Evidence type:** computational; multislice/Poisson-likelihood analysis of simulated WSe₂ and experimental WSe₂ and PrScO₃ 4D-STEM data.
- **Caveat:** The authors say model error can exceed nominal shot-noise ellipses; on real data, individual atoms within one layer are not resolved in depth, and the error bars are conditional on the physical model.
- **Announcement type:** new submission, announcement batch 2026-11-18.
- **Themes:** Instrumentation & detectors; Condensed matter & materials; Computational & data methods

### 2. [Measurements of inclusive J/ψ production in Au+Au collisions at √sNN = 14.6, 17.3, 19.6, and 27 GeV with the STAR experiment](https://arxiv.org/abs/2611.25487)
- **Abstract:** The STAR Collaboration measures mid-rapidity inclusive J/ψ production at four RHIC collision energies and reports centrality and transverse-momentum trends in the nuclear modification factor.
- **Authors:** The STAR Collaboration
- **arXiv:** `2611.25487v1` (published 2026-11-19T04:21:38Z; categories: `nucl-ex`, `hep-ex`)
- **Evidence for ranking:** A new four-energy measurement from RHIC directly fills an energy-coverage gap between earlier lower- and higher-energy results; it is cross-listed across nuclear and high-energy experimental physics.
- **Claimed result:** The authors report RAA near 0.5 in the 0–20% centrality class, a hint of increasing RAA with pT at 14.6–27 GeV, and no significant integrated central-collision energy dependence within uncertainties.
- **Evidence type:** experimental; STAR dielectron-channel analysis of Au+Au collision data collected at RHIC.
- **Caveat:** Reported per-bin systematic uncertainties span 6.5–20.6%, dominated by tracking efficiency; the comparison uses an interpolated p+p reference, and the low-energy trend is described as a hint.
- **Announcement type:** new submission, announcement batch 2026-11-19.
- **Themes:** Particle, nuclear & high-energy physics; Instrumentation & detectors

### 3. [Certified Discovery of Quantum Phase Diagrams](https://arxiv.org/abs/2611.25064)
- **Abstract:** The authors give quantum and classical algorithms that map phase diagrams of geometrically local Hamiltonian families and provide verifiable certificates for detected transitions, with numerical demonstrations on model systems.
- **Authors:** Yuanxi Liu, John Preskill, Hsin-Yuan Huang
- **arXiv:** `2611.25064v1` (published 2026-11-18T19:09:17Z; categories: `quant-ph`, `cond-mat.stat-mech`, `cond-mat.str-el`, `math-ph`)
- **Evidence for ranking:** Four category listings connect quantum information, condensed matter, and mathematical physics; the contribution is a formal certification method with accompanying numerical experiments rather than an unverified classifier.
- **Claimed result:** The authors prove that, under stated assumptions, a frequency-filtered local probe can certify transitions and a quantum algorithm can recover phase structure to prescribed resolution without supplied order parameters or training labels.
- **Evidence type:** theoretical and computational; algorithmic proofs plus numerical experiments on model quantum systems.
- **Caveat:** The guarantee assumes at least one valid reference-ground-state preparation in each gapped region and finite resolvable gaps; sufficiently small gaps, including some first-order transitions, can evade the detection regime.
- **Announcement type:** new submission, announcement batch 2026-11-18.
- **Themes:** Quantum information; Condensed matter & materials; Computational & data methods

### 4. [Compiling Constraints into Neuromorphic Ising Machines](https://arxiv.org/abs/2611.25352)
- **Abstract:** The authors encode combinatorial constraints as programmable transitions in a neuromorphic Ising machine and report optimization and surface-code-decoding benchmarks, including a real-time FPGA implementation.
- **Authors:** Faiek Ahsan, Shantanu Chakrabartty
- **arXiv:** `2611.25352v1` (published 2026-11-19T01:48:43Z; categories: `cs.ET`, `cond-mat.dis-nn`, `cs.AR`, `cs.NE`, `quant-ph`)
- **Evidence for ranking:** Five cross-list categories bridge neuromorphic hardware, optimization, and quantum information; the abstract reports an FPGA sampler and finite-distance surface-code decoding results, giving a concrete implementation signal.
- **Claimed result:** The authors report fewer iterations than penalty-based machines on third-order graph matching and real-time surface-code decoding on FPGA up to distance 9 under noisy syndrome measurements.
- **Evidence type:** computational; neuromorphic Ising-machine benchmarks and FPGA sampler/decoder implementation.
- **Caveat:** The reported comparisons concern specified optimization and surface-code benchmarks and finite code distances; they do not establish general scaling or broad superiority across problem classes.
- **Announcement type:** new submission, announcement batch 2026-11-19.
- **Themes:** Quantum information; Computational & data methods

### 5. [Characterizing a neutral atom quantum simulator accessible in cloud](https://arxiv.org/abs/2611.25131)
- **Abstract:** The authors experimentally probe Pasqal’s cloud-accessible Fresnel neutral-atom simulator, identify noise sources, and build an effective noisy-dynamics model that reproduces the tested behavior.
- **Authors:** Andrea Muratori, Francesco Minardi, Tommaso Calarco, Felix Motzoi
- **arXiv:** `2611.25131v1` (published 2026-11-18T20:09:08Z; categories: `quant-ph`)
- **Evidence for ranking:** The work reports direct experiments on remotely accessible quantum hardware and an empirically fitted model, complementing algorithm papers with a device-characterization result.
- **Claimed result:** The authors show that an effective model with numerically inferred noise strengths reproduces the simulator’s observed dynamics for the tested pulse sequences and settings.
- **Evidence type:** experimental; cloud-accessed Pasqal Fresnel neutral-atom analog quantum simulator, with numerical noise-model fitting.
- **Caveat:** The fitted noise model is tied to Fresnel and the pulse sequences/settings examined; transfer to other devices or operating regimes is not established by this study.
- **Announcement type:** new submission, announcement batch 2026-11-18.
- **Themes:** Quantum information; Atomic, molecular & optical physics

### 6. [Dark Matter Model Implications of a Candidate Sub-halo Near the Sun, and the Data Needed to Discriminate Among Them](https://arxiv.org/abs/2611.25359)
- **Abstract:** The authors interpret a candidate local mass concentration in pulsar-timing accelerations across several dark-matter models and identify observations that could distinguish the possibilities.
- **Authors:** Stefano Profumo, Sukanya Chakrabarti
- **arXiv:** `2611.25359v1` (published 2026-11-19T01:57:40Z; categories: `astro-ph.GA`, `astro-ph.CO`, `astro-ph.HE`, `hep-ph`)
- **Evidence for ranking:** Four astrophysics/high-energy category listings make this a cross-subfield interpretation; it translates an existing candidate into specific discriminating measurements rather than claiming a new detection.
- **Claimed result:** The authors argue that current accelerations leave the candidate’s internal profile, velocity, and population degenerate, and outline tests using interior accelerations, lensing/accretion, emission morphology, and a comoving stellar population.
- **Evidence type:** theoretical; phenomenological analysis of existing pulsar-timing acceleration claims and proposed observational tests.
- **Caveat:** The paper treats the sub-halo as a candidate, not an established detection; the existing acceleration measurements lie outside the tidal radius and cannot determine the inner mass profile.
- **Announcement type:** new submission, announcement batch 2026-11-19.
- **Themes:** Astrophysics; Cosmology & gravitation; Particle, nuclear & high-energy physics

### 7. [Orbital differentiation in a rare earth ion near half filling](https://arxiv.org/abs/2611.22462)
- **Abstract:** Using full-multiplet calculations for SmN, the authors report distinct orbital-stiffness subspaces in the ground-state manifold and compare calculated observables with magnetic-susceptibility, neutron-scattering, and DFT results.
- **Authors:** D. W. Tam, Ø. S. Fjellvåg, B. Gonano, E. X. M. Trewick, M. Månsson
- **arXiv:** `2611.22462v1` (published 2026-11-17T09:23:36Z; categories: `cond-mat.str-el`, `cond-mat.mtrl-sci`, `cond-mat.supr-con`, `physics.chem-ph`, `physics.comp-ph`)
- **Evidence for ranking:** Five category listings span correlated electrons, materials, superconductivity, chemical physics, and computation; the model is checked against measured magnetic susceptibility and inelastic neutron scattering.
- **Claimed result:** The authors find orbital differentiation within the SmN ground J=5/2 manifold and suggest it may support a proposed unconventional triplet-superconductivity interpretation.
- **Evidence type:** computational; full-multiplet crystal-field calculations with Quanty, compared with susceptibility and inelastic-neutron data and DFT spin-density predictions.
- **Caveat:** The superconductivity connection is suggestive rather than demonstrated, and the inferred orbital structure depends on the crystal-field model and parameter choices.
- **Announcement type:** new submission, announcement batch 2026-11-17.
- **Themes:** Condensed matter & materials; Computational & data methods

### 8. [Run it Back: Autoregression vs. Video Diffusion for Final-Conditioned Weather Trajectories](https://arxiv.org/abs/2611.21521)
- **Abstract:** The revised paper compares a backward autoregressive climate emulator with video diffusion for final-conditioned trajectories of three extreme-weather cases and reports improved variance and physical consistency alongside rollout instability.
- **Authors:** Jerry Lin, Elizabeth A. Barnes
- **arXiv:** `2611.21521v2` (published 2026-11-16T18:13:42Z; revised 2026-11-19T04:38:11Z; categories: `physics.ao-ph`)
- **Evidence for ranking:** A substantive v2 revision falls inside the requested week; the authors compare methods on three named observed events and report ERA5-based checks. The arXiv comment states acceptance at a NeurIPS 2026 climate-ML workshop.
- **Claimed result:** The authors report that Rewind-AR better captures leading precursor variability and heatwave intensification than the earlier diffusion approach for the examined cases, without the same near-conditioning geostrophic inconsistency.
- **Evidence type:** computational; Rewind-AR/FourCastNet 3 ensembles evaluated against ERA5 for the 2021 Pacific Northwest heatwave, Hurricane Ian, and Superstorm Sandy.
- **Caveat:** Up to 22% of generated members become numerically unstable within 66 hours, and the evaluation is based on three cases rather than a broad extreme-event sample.
- **Announcement type:** revision, announcement batch 2026-11-19.
- **Themes:** Plasma & fluid physics; Computational & data methods

## Trending Research Themes

- **Model-aware inference and uncertainty are becoming part of the result, not just post-processing.** 4D-TEMPO fits the microscope and atoms jointly and exposes model-conditional errors; the STAR analysis quantifies tracking-driven systematics; and Rewind-AR tests physical consistency and ensemble spread against ERA5 (2611.24776, 2611.25487, 2611.21521).
- **Quantum-computing claims increasingly pair algorithms with verification or device characterization.** Certified phase-diagram discovery supplies transition certificates, the Fresnel study fits an explicit hardware-noise model, and the neuromorphic Ising work reports an FPGA decoder (2611.25064, 2611.25131, 2611.25352). These are distinct methods and platforms, not independent confirmations of one result.
- **Bridging measurements and microscopic interpretation remains a cross-field pattern.** STAR compares multi-energy heavy-ion data with transport models; the SmN calculation checks against susceptibility and neutron-scattering observations; the local-subhalo analysis lays out which new observations could break model degeneracies (2611.25487, 2611.22462, 2611.25359).

## Open Problems and Research Directions

- **Author-stated uncertainty — STAR tracking and reference inputs:** The STAR paper reports 6.5–20.6% per-bin systematic uncertainty, with tracking efficiency dominant, and uses an interpolated p+p reference. Follow-up work could improve tracking calibration and tighten the reference while extending the collision-energy scan (2611.25487).
- **Author-stated model limits — atomic-scale imaging:** 4D-TEMPO says diffuse scattering/coherence modeling still limits uncertainty calibration and real-data depth resolution. Better forward models and event-driven detectors that capture drift and dynamics could test whether per-atom errors remain calibrated at low dose (2611.24776).
- **Author-stated assumptions — certified phase boundaries:** The phase-diagram guarantee needs a valid reference state in each gapped region and resolvable gap behavior; some very small-gap transitions may be missed. Testing on larger quantum-simulator Hamiltonian families, including difficult first-order cases, would probe the practical boundary of the certification method (2611.25064).
- **Authors’ proposed discriminants — candidate local sub-halo:** Current accelerations do not resolve the interior profile or object motion. Measurements inside the candidate, lensing/accretion constraints, emission morphology, and searches for comoving stars are the paper’s proposed routes to distinguish dark-matter and compact-object interpretations (2611.25359).
- **Author-stated limitation — weather rollouts:** Rewind-AR has unstable members within a 66-hour horizon. Longer-horizon stability tests and broader, held-out extreme-event sets could determine whether its improved physical consistency generalizes beyond the three examined cases (2611.21521).

## Takeaway

The clearest shared pattern this week is not one new physical discovery but tighter coupling between measurements, physical models, and explicit uncertainty or verification: from STAR’s collision-energy scan to atom-by-atom microscopy and quantum-device benchmarks. Several results are promising but conditional—on detector systematics, model fidelity, reference-state assumptions, or limited test sets—so follow-up measurement and out-of-sample validation matter more than the ranking order.

## Method and sources

- **Window and snapshot:** 2026-11-14–2026-11-20 inclusive; snapshot 2026-11-20 02:41:21 UTC. This weekly window is based on submissions and revisions dated in the interval; no 2026-11-20 records appeared in the API result at the snapshot, so the newest available batch was 2026-11-19.
- **Archive coverage:** A combined arXiv API query checked the configured physics scope: `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`, retaining cross-listed papers. It returned 1,732 unique eligible records for the window; cross-list entries were deduplicated by versionless arXiv ID. This is a candidate pool, not an exhaustive account of research quality.
- **Selection and inference:** Eight entries are labeled “notable recent papers,” not measured popularity. Ranking weighs cross-subfield listings, concrete measurements or methods, validation/benchmark evidence, and substantive revisions; recency is secondary. There is no official arXiv trending chart. Semantic Scholar Graph returned current citation metadata for only two selected papers; each listed zero citations and zero influential citations at lookup time. Citation totals are not gains during this week. No independent paper-specific news/expert-discussion signal is credited in the ordering; targeted exact-title searches covered only several candidates, not the entire pool.
- **Verification and reading:** Each selected arXiv abstract page was checked for title, authors, version/date, and categories. The PDFs of the top three were inspected for introduction, methods/results, and limitations/systematics; the rest are summarized from their arXiv abstracts and comments.
- **Sources:** Individual arXiv abstract links are attached to each title. Candidate discovery used the arXiv API; paper text used arXiv PDFs; citation metadata used Semantic Scholar Graph API (`arXiv:<id>`). Targeted independent web searches covered several candidates; no corroborating paper-specific signal is credited here.
