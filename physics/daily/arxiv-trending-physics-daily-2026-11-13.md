# arXiv physics daily — Fri, 13 Nov 2026

10 notable new papers; the strongest pattern is quantum systems moving from controlled demonstrations toward deployed networks, alongside fresh measurements and analysis methods in nuclear and gravitational-wave physics. Spoken agenda: two QKD field deployments, one quantum-memory experiment, then collider, hadron, and gravitational-wave results. This is an inferred ranking, not an official arXiv trending chart; the papers are less than a day old at snapshot, so citation evidence is sparse and the list should be read as notable work rather than measured popularity.

## Top papers (ranked)

### 1. [Observation of the $\Lambda(1520)$ suppression in Pb-Pb collisions at $\sqrt{s_{\rm NN}} = 5.02$ TeV](https://arxiv.org/abs/2611.17010)
- **Abstract:** ALICE measures a 6.8σ central-to-peripheral suppression of the $\Lambda(1520)/\Lambda$ yield ratio in Pb-Pb collisions and compares the centrality trend with hadronic-transport and statistical-hadronization models.
- **Authors:** ALICE Collaboration
- **arXiv:** `2611.17010v1` (published 2026-11-12 16:07:03 UTC; categories: `nucl-ex`)
- **Evidence for ranking:** A quantitative 6.8σ measurement, six centrality classes, a model comparison that separates late hadronic transport from freeze-out-only predictions, and a comment that the paper is submitted to PRL make this a strong direct-result candidate.
- **Claimed result:** The authors report a suppression fraction of $0.589 \pm 0.015_{stat} \pm 0.086_{syst}$ (about 59%; equivalent central/peripheral ratio 0.411) and find MUSIC coupled to the SMASH hadronic afterburner reproduces the centrality dependence.
- **Evidence type:** experimental; ALICE Pb-Pb collision data at $\sqrt{s_{NN}}=5.02$ TeV, measured across six centrality classes, with hydrodynamic/transport comparisons.
- **Caveat:** The attribution to late-stage rescattering is supported by model comparison rather than isolated experimentally; the models still differ in peripheral collisions.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

### 2. [Inter-city 18.9 km free-space QKD over a dense urban corridor](https://arxiv.org/abs/2611.16774)
- **Abstract:** A decoy-state BB84 system is field-tested across an 18.9 km urban Barcelona free-space link, with measured channel parameters implying a finite-size key rate above 11 kbit/s.
- **Authors:** Ignacio H. López Grande, Nicolas Linale, Giacomo Paganini, Achraf El Bouazzaoui, Adrián S. Blanca, et al.
- **arXiv:** `2611.16774v1` (published 2026-11-12 13:20:16 UTC; categories: `quant-ph`)
- **Evidence for ranking:** The field deployment has independent coverage by [QubitWire](https://qubitwire.com/articles/barcelona-urban-quantum-link-room-temperature-detectors), in addition to concrete link length, measured error/attenuation, and an explicitly estimated finite-size key rate.
- **Claimed result:** The authors report a 40-minute run with mean QBER 1.31% and approximately 19 dB average attenuation; from those measured parameters they estimate a finite-size secret-key rate exceeding 11 kbit/s.
- **Evidence type:** experimental; 785 nm decoy-state BB84 over a Barcelona metropolitan free-space link using room-temperature single-photon detectors and no receiver adaptive optics.
- **Caveat:** The secret-key rate is an estimate from measured channel parameters, not demonstrated sustained fresh-key delivery; the paper identifies long-term, unattended and day/night operation as future work.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Quantum information; Instrumentation & detectors

### 3. [A deployed four-city entanglement-based QKD network with real-time key delivery, benchmarked against finite-key security bounds](https://arxiv.org/abs/2611.17265)
- **Abstract:** The authors describe a deployed entanglement-based fiber QKD segment connecting four Slovak cities and report real-time post-processed keys on simultaneously operated links.
- **Authors:** Gilberto Borges, Saeid Salari, Ekta Panwar, Samgeeth Puliyil, Kartik Kakade, et al.
- **arXiv:** `2611.17265v1` (published 2026-11-12 18:45:08 UTC; categories: `quant-ph`, `physics.optics`)
- **Evidence for ranking:** This is a deployed multi-city network rather than a laboratory-only link; reported rates follow the complete post-processing chain, keys are delivered using ETSI GS QKD 014, and the work benchmarks the implementation against finite-key bounds.
- **Claimed result:** The authors report 13.5 bit/s over 109 km and 4.3 bit/s over 32.1 dB loss, and estimate error correction could improve finite-key rates by 4.1–6.6 times.
- **Evidence type:** experimental; entangled photons routed over deployed Slovak telecommunication fiber, with real-time key delivery and finite-key analysis.
- **Caveat:** The authors find the implemented heuristic privacy amplification can exceed the finite-key bound; the reported rates depend on the security analysis and post-processing choices.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Quantum information; Instrumentation & detectors

### 4. [Observation of Genuine Multi-Time Quantum Memory](https://arxiv.org/abs/2611.17268)
- **Abstract:** The authors derive a three-time witness for quantum memory that evades pairwise tests and demonstrate the resulting hierarchy in a time-continuous superconducting-qubit experiment.
- **Authors:** Konstantin Beyer, Valentin Link, Surihan Sean Borjigin, Qian Cao, Orion Lee, et al.
- **arXiv:** `2611.17268v1` (published 2026-11-12 18:46:04 UTC; categories: `quant-ph`)
- **Evidence for ranking:** The paper combines a new analytical witness with a physical-platform demonstration, and its counterexample directly distinguishes quantum memory from classical-memory explanations that pass all pairwise tests.
- **Claimed result:** The authors certify a strict hierarchy: a three-time joint test detects quantum memory in a minimal qubit example where every pair of times admits a classical-memory explanation.
- **Evidence type:** experimental and theoretical; analytical witness plus a time-continuous superconducting-qubit realization with time-independent couplings.
- **Caveat:** The demonstration is a minimal qubit implementation; broader robustness and scaling to more complex environments are not established by the abstract.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Quantum information

### 5. [Lurkers at the Threshold: GWTC-4.0's near-threshold events](https://arxiv.org/abs/2611.16985)
- **Abstract:** The authors reanalyse 42 GWTC-4.0 candidates below the catalogue's parameter-estimation threshold, validate 29, and release posterior results for possible astrophysical candidates.
- **Authors:** Daniel Williams, Michael Williams
- **arXiv:** `2611.16985v1` (published 2026-11-12 15:50:43 UTC; categories: `gr-qc`, `astro-ph.HE`)
- **Evidence for ranking:** It adds a reproducible public-data analysis and a compatible data release to a catalogue population often omitted from parameter estimation, with explicit validation and rejection accounting.
- **Claimed result:** Of 42 candidates, 29 pass the authors' validation; six of those have interpretable indications of interest, but inferred spin parameters are generally weakly constrained.
- **Evidence type:** computational; catalogue-style parameter estimation on publicly available GWTC-4.0 strain data with automated posterior validation.
- **Caveat:** Several candidates are consistent with noise or affected by instrumental artifacts, and the reported spin/precession hints need further analysis to establish robustness.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Cosmology & gravitation; Astrophysics; Computational & data methods

### 6. [New measurement of BR$(K^+\rightarrow\pi^+\nu\bar\nu)$ at the NA62 experiment](https://arxiv.org/abs/2611.16530)
- **Abstract:** NA62 presents an updated $K^+\to\pi^+\nu\bar\nu$ branching-ratio analysis based on its 2023–2024 data, which doubles the total dataset and is expected to reach 5σ sensitivity to the Standard Model process.
- **Authors:** Silvia Martellotti on behalf of NA62 Collaboration, A. T. Akmete, R. Aliberti, S. Alibocus, F. Ambrosino, et al.
- **arXiv:** `2611.16530v1` (published 2026-11-12 09:29:12 UTC; categories: `hep-ex`)
- **Evidence for ranking:** The rare-decay channel is a high-precision probe of short-distance physics, and this conference contribution reports a dataset twice the previous total with an explicit expected-sensitivity milestone.
- **Claimed result:** The authors say the 2023–2024 data double NA62's total dataset and provide an expected 5σ sensitivity for the Standard Model process; the abstract does not give a measured branching-ratio value.
- **Evidence type:** experimental; NA62 data collected at the CERN SPS, presented as a conference contribution.
- **Caveat:** The arXiv abstract supplies no branching-ratio central value, uncertainty, or observed significance; the 5σ statement is expected sensitivity, not a claimed discovery or completed 5σ observation.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Instrumentation & detectors

### 7. [Three-body dynamics of the Roper resonance](https://arxiv.org/abs/2611.17139)
- **Abstract:** A unitary coupled-channel amplitude that includes $\pi\pi N$ dynamics is used to determine the Roper resonance poles near the complex $\pi\Delta$ threshold.
- **Authors:** Jinzi Wu, Michael Döring, Maxim Mai
- **arXiv:** `2611.17139v1` (published 2026-11-12 17:29:13 UTC; categories: `nucl-th`, `hep-lat`, `hep-ph`, `nucl-ex`)
- **Evidence for ranking:** It bridges four nuclear/high-energy archives, introduces explicit three-body dynamics relevant to lattice-QCD extraction, and quantifies parametrization-dependent systematic uncertainties in a pole result.
- **Claimed result:** Fitting the $P_{11}$ amplitude to SAID data with strict two- and three-body unitarity, the authors report a Roper pole at $\sqrt{s_R}=1346\pm2^{+6}_{-3}-i(81\pm2^{+7}_{-8})$ MeV.
- **Evidence type:** theoretical; unitary coupled-channel amplitude fitted to experimental two-body amplitudes and the SAID $P_{11}$ amplitude.
- **Caveat:** The pole remains dependent on amplitude parametrization; the authors present it as an input for future lattice-QCD determinations, not a direct lattice observation.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

### 8. [$N\Omega$ Dibaryon near Unitarity from Physical-Point Lattice QCD](https://arxiv.org/abs/2611.16989)
- **Abstract:** A physical-point lattice-QCD calculation finds an attractive $N\Omega$ interaction compatible with a shallow near-unitary dibaryon state and estimates its binding energy.
- **Authors:** Liang Zhang, Yan Lyu, Sinya Aoki, Takumi Doi, Tetsuo Hatsuda, et al.
- **arXiv:** `2611.16989v1` (published 2026-11-12 15:55:38 UTC; categories: `hep-lat`)
- **Evidence for ranking:** The calculation uses physical quark masses and a direct $T$-matrix pole analysis, giving a quantitative first-principles benchmark for proposed femtoscopy and dibaryon searches.
- **Claimed result:** With the HAL QCD method, the authors infer $B_{n\Omega}=0.61$ MeV with two reported uncertainty components; including finite-size Coulomb attraction gives $B_{p\Omega}=1.25$ MeV, also with two uncertainty components.
- **Evidence type:** computational; (2+1)-flavor lattice QCD at physical quark masses ($m_\pi\simeq137$ MeV) using the HAL QCD method.
- **Caveat:** The shallow binding estimates have substantial statistical/systematic uncertainty and depend on the lattice interaction extraction; the authors call for future femtoscopy and dibaryon searches.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

### 9. [Rapid Multiparameter Gravitational-Wave Tests of General Relativity with Neural Posterior Estimation](https://arxiv.org/abs/2611.17038)
- **Abstract:** DINGO-TGR combines neural posterior estimation, importance sampling, and principal-component analysis to accelerate joint inference of binary parameters and six post-Newtonian deviations in GR tests.
- **Authors:** Hong Su, Tao Yang, He Wang
- **arXiv:** `2611.17038v1` (published 2026-11-12 16:22:58 UTC; categories: `gr-qc`, `astro-ph.IM`)
- **Evidence for ranking:** The method is checked on GR and beyond-GR injections, agrees with an independent `bilby-tgr` analysis for two events, and reports a large runtime reduction plus a dedicated null-model significance test.
- **Claimed result:** For GW150914, the leading-mode offset has an empirical upper-tail p-value of 11.5% in the authors' 1,000 GR-like simulations; it does not reject the adopted GR null at 5% significance.
- **Evidence type:** computational; IMRPhenomXPHM waveform inference, injection validation, and GW150914/GW250114 analyses.
- **Caveat:** The significance calibration uses Gaussian-noise realizations and fixed detector power spectral densities, so robustness to broader noise and waveform systematics remains open.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Cosmology & gravitation; Computational & data methods

### 10. [Efficient Standard Siren Cosmological Inference with Posterior Reuse](https://arxiv.org/abs/2611.16697)
- **Abstract:** ASPIRE reuses posterior samples to update dark-siren cosmology and population inferences under changed assumptions, recovering nested-sampling-consistent posteriors with reported 6–28× speedups.
- **Authors:** Alexander Papadopoulos, Michael J. Williams, Christian E. A. Chapman-Bird, Rachel Gray, Christopher Messenger
- **arXiv:** `2611.16697v1` (published 2026-11-12 12:13:17 UTC; categories: `astro-ph.CO`, `astro-ph.HE`, `gr-qc`)
- **Evidence for ranking:** It links cosmological and source-population inference across three physics categories, tests against nested sampling on GWTC-5 cases, and reports a practical speedup for repeated analyses.
- **Claimed result:** The authors report ASPIRE posterior agreement with nested sampling and a 6–28× performance improvement when reusing an existing posterior.
- **Evidence type:** computational; normalizing flows plus sequential Monte Carlo applied to dark-siren analyses with GWTC-5.0.
- **Caveat:** Standard-siren results still depend on source-population, galaxy-catalogue, and detection-selection assumptions; posterior reuse accelerates their comparison but does not remove them.
- **Announcement type:** new submission, Fri, 13 Nov 2026 announcement batch
- **Themes:** Cosmology & gravitation; Astrophysics; Computational & data methods

## Trending Research Themes

- **Field-ready quantum communication:** The Barcelona free-space BB84 demonstration (#2) and the Slovak deployed entanglement-based fiber network (#3) both move QKD into operational urban infrastructure, but they are complementary demonstrations—not independent replications of one shared result. One reports a finite-size key rate inferred from a field test; the other reports keys delivered after full post-processing.
- **Quantum information in time and networks:** The superconducting-qubit multi-time witness (#4) extends how memory in an environment is certified, while #2–3 explore distributing cryptographic keys over real channels. These are distinct routes from quantum principles toward usable systems.
- **Strong-interaction physics from collisions to lattice and amplitude methods:** ALICE's $\Lambda(1520)$ result (#1) constrains late hadronic rescattering; NA62's enlarged rare-kaon dataset (#6) targets a clean flavor observable; the Roper amplitude (#7) and physical-point $N\Omega$ lattice calculation (#8) address hadronic structure with complementary amplitude and first-principles approaches.
- **Gravitational-wave catalogues as reusable analysis infrastructure:** The sub-threshold GWTC-4.0 study and data release (#5), neural multiparameter GR test (#9), and posterior-reuse standard-siren analysis (#10) all use public or catalogue-scale data to improve what can be inferred and how quickly. Their shared GW data ecosystem is not independent observational confirmation of the same event or result.

## Open Problems and Research Directions

- **Urban free-space QKD — author-stated limitation:** The Barcelona paper says long-term attenuation statistics, pointing-error/QBER correlations, and unattended day/night operation remain to be characterized (#2). **Research direction (synthesis):** run continuous multi-day and seasonal tests with logged pointing, weather, and key-management outputs; separately verify sustained fresh-key delivery rather than extrapolating from a short channel characterization.
- **Finite-key operation — author-stated issue:** In the Slovak network, the paper says its heuristic privacy amplification can exceed the finite-key bound and finds that error correction could improve rates; one 142.9 km link has no positive finite-key rate under the implemented scheme (#3). **Research direction (synthesis):** implement and independently audit the suggested error-correction path, then measure the end-to-end finite-key rate on the long link.
- **Late-stage heavy-ion dynamics — paper-reported model gap:** MUSIC+SMASH reproduces the centrality trend within uncertainties, but the paper reports residual peripheral discrepancies and statistical-hadronization models overpredict the central ratio (#1). **Research direction (synthesis):** compare additional resonance species and energies with transport calculations while varying rescattering/regeneration inputs to test whether one hadronic-stage description explains them consistently.
- **Marginal gravitational-wave candidates — paper-reported limitation:** Thirteen of the 42 GWTC-4.0 candidates fail validation or cannot be reliably interpreted, while spin constraints are generally weak (#5). **Research direction (synthesis):** stress-test the released posteriors against alternative noise/artifact treatments and independent parameter-estimation pipelines before promoting candidate-level interpretations.
- **Roper and $N\Omega$ — author-stated next tests:** The Roper pole has parametrization-dependent systematic uncertainty and is intended to support future lattice extraction (#7); the shallow $N\Omega$ state is offered as a benchmark for future femtoscopy and dibaryon searches (#8). **Research direction (synthesis):** compare finite-volume lattice spectra against the unitary amplitude and seek $N\Omega$ femtoscopic constraints capable of discriminating a shallow bound state from near-threshold attraction.
- **GR tests and standard sirens — model/noise dependence:** The DINGO-TGR null test uses fixed detector PSDs and Gaussian-noise realizations (#9), while standard-siren inference depends on source populations, galaxy catalogues, and selection functions (#10). **Research direction (synthesis):** extend the GR calibration across realistic non-Gaussian noise and waveform systematics, and use posterior reuse to systematically vary catalogue completeness and population assumptions.
- **Rare-kaon measurement — missing reported observable:** The NA62 abstract describes a doubled dataset and expected 5σ sensitivity but gives no measured branching ratio or uncertainty (#6). **Research direction (synthesis):** assess the full analysis once the measured value, backgrounds, and systematic budget are reported; do not treat the sensitivity projection as a detection.

## Takeaway

This announcement is especially strong in practical quantum-network demonstrations, with an independent report on the Barcelona link and a separate deployed fiber QKD network. The most concrete physics result is ALICE's high-significance resonance suppression, while the GW and hadron papers broaden catalogue reuse and multi-body theory. Because all candidates are extremely fresh and citation evidence is limited, this is a transparent shortlist of notable papers—not a measured popularity ranking.

## Method and sources

- **Window:** Daily; the current arXiv announcement batch dated Fri, 13 Nov 2026. The API candidate records have first-submission timestamps from 2026-11-12 00:11:03 through 18:59:55 UTC; all 167 records fall on that submission date. This is today's batch, not a prior-batch fallback.
- **Snapshot:** 2026-11-13 17:20:42 UTC.
- **Coverage:** Checked arXiv recent pages for `physics`, `astro-ph`, `cond-mat`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`; queried the combined arXiv API pool across those archives for the daily submitted-date window. The pool contained 167 unique works; 106 have multiple category tags, and `quant-ph` is the primary category for 59. Candidates were deduplicated by versionless ID. Verified the abstract pages for all ten selected papers and inspected arXiv HTML full text for the top three entries.
- **Inference:** No official arXiv trending chart exists. The ordering favors a checkable independent report, direct experimental measurements, public-data/reproducible artifacts, cross-subfield relevance, and clearly quantified results; recency is only a tie-breaker. Semantic Scholar citation evidence was not available for this just-announced set at snapshot, so citation counts did not rank the papers. The independent coverage signal for #2 is [QubitWire](https://qubitwire.com/articles/barcelona-urban-quantum-link-room-temperature-detectors); primary sources are the linked arXiv abstract pages and HTML full texts.
- **Sources:** [arXiv Physics recent](https://arxiv.org/list/physics/recent); [arXiv archive recent pages](https://arxiv.org/list/astro-ph/recent), [cond-mat](https://arxiv.org/list/cond-mat/recent), [gr-qc](https://arxiv.org/list/gr-qc/recent), [hep-ex](https://arxiv.org/list/hep-ex/recent), [hep-lat](https://arxiv.org/list/hep-lat/recent), [hep-ph](https://arxiv.org/list/hep-ph/recent), [hep-th](https://arxiv.org/list/hep-th/recent), [nucl-ex](https://arxiv.org/list/nucl-ex/recent), [nucl-th](https://arxiv.org/list/nucl-th/recent), [quant-ph](https://arxiv.org/list/quant-ph/recent); Semantic Scholar Graph data unavailable for these newly announced records at the snapshot.
