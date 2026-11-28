# Physics on arXiv — 26 November 2026

Eight notable recent papers from the latest available announcement batch, spanning quantum hardware and information, lattice methods, cosmological inference, satellite galaxies, neutrino phenomenology, and heavy-ion measurements. The leading pattern is tighter empirical or computational tests of difficult signals: hardware witnesses, replica-exchange efficiency, multi-probe cosmology, and complementary collision systems. Spoken agenda: what was actually measured, what remains a forecast or mathematical result, and which follow-ups would sharpen the claims. Global caveat: arXiv supplies no official trending chart; this ordering is inferred from the papers' concrete results and cross-field relevance, while citation evidence for this very recent batch is limited.

The provided attention-signal file targets the 27 November batch but contains no candidates. The most recent batch visible across the arXiv archive listings is dated 26 November, so this report uses that prior batch and labels the papers “notable recent” rather than treating them as measured popularity leaders.

## Top papers (ranked)

### 1. [Experimental Quantum Hardware Benchmarks of Flat Non-Clifford Hypergraph States, Antipodal Obstructions, and Nonlocal Games on IBM Heron r2](https://arxiv.org/abs/2611.34683)
- **Abstract:** The authors test non-Clifford hypergraph-state structure and contextuality-style games on two IBM Heron r2 processors, reporting hardware benchmarks across 3–50 qubits.
- **Authors:** Filipe Martins Vono, Valéria Gonzaga Santos, André Oliveira Naufel de Toledo
- **arXiv:** `2611.34683v1` (published 2026-11-25 16:45:22 UTC; categories: `quant-ph`)
- **Evidence for ranking:** No per-paper attention values were present in the supplied signal file; it had no candidate records. Included for direct hardware evidence across two processors, auditable jobs, and a connection between non-Clifford witnesses and quantum nonlocality tests.
- **Claimed result:** The authors report non-Clifford coherence and multiple game/witness violations on IBM Heron r2, including a 96.85% raw Mermin–Peres win rate on one backend and parity-game violations up to 30 qubits.
- **Evidence type:** experimental; 11 IBM Heron r2 jobs on `ibm_fez` and `ibm_kingston`, using 4,096 shots per circuit.
- **Caveat:** The authors say the single-chip runs do not close the relativistic locality loophole; finite shots and routing/depth limitations constrain some higher-qubit tests.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Quantum information; Instrumentation & detectors

### 2. [Unfreezing topology using out-of-equilibrium replica exchanges](https://arxiv.org/abs/2611.34367)
- **Abstract:** The authors introduce a gradual, out-of-equilibrium replica-exchange method for mitigating topological freezing and test it in a two-dimensional CP^{N−1} lattice model.
- **Authors:** Claudio Bonanno, Andrea Bulgarelli, Elia Cellini, Raffaele Dionisio, Andrea Nada et al.
- **arXiv:** `2611.34367v1` (published 2026-11-25 13:30:59 UTC; categories: `hep-lat`, `cond-mat.stat-mech`)
- **Evidence for ranking:** No per-paper attention values were available in the supplied signal file. Cross-listed between lattice field theory and statistical mechanics, the work derives an acceptance/cost model and checks it against simulations rather than presenting only a proposed algorithm.
- **Claimed result:** For the tested N=21 model, authors report at least about 40% lower computational cost at fixed statistical precision than standard parallel tempering on boundary conditions, across five lattice spacings.
- **Evidence type:** computational; simulations of the two-dimensional CP^{N−1} model with N=21, compared with standard replica exchange.
- **Caveat:** The quantitative demonstration is restricted to this model and setup; the paper frames extension to four-dimensional gauge theories as future work.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Particle, nuclear & high-energy physics; Computational & data methods

### 3. [Bound Entanglement with Negative Partial Transpose Exists](https://arxiv.org/abs/2611.34921)
- **Abstract:** The author gives an explicit Werner state on C^8 ⊗ C^8 that is negative under partial transpose yet nondistillable by LOCC, with a further fidelity bound under separable operations.
- **Authors:** Islam Faisal
- **arXiv:** `2611.34921v1` (published 2026-11-25 18:58:48 UTC; categories: `quant-ph`, `cond-mat.other`, `cs.CC`, `cs.IT`)
- **Evidence for ranking:** No per-paper attention values were emitted for this item. Its four-way cross-list and explicit finite-dimensional theorem make it a concrete connection across quantum information, condensed matter, complexity, and information theory.
- **Claimed result:** The author proves that the specified state is NPT and bound entangled, and that separable operations cannot produce a two-qubit Bell-state fidelity above (1+√2)/4 ≈ 0.604.
- **Evidence type:** theoretical; exact analysis of a specified 8×8 Werner state, with a computer-assisted search used to find a proof certificate that the paper then checks exactly.
- **Caveat:** This is a mathematical existence result for a particular state, not an experimental preparation or a general classification of NPT states.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Quantum information

### 4. [Probing Dynamical Dark Energy with Hyper Suprime-Cam Year 3 Cosmic Shear](https://arxiv.org/abs/2611.34650)
- **Abstract:** The authors combine HSC Year 3 cosmic shear with distance probes to test constant and time-varying dark-energy models, finding a 2.4σ preference for evolution in the latter parameterization.
- **Authors:** Shreya Mukherjee, Surhud More
- **arXiv:** `2611.34650v1` (published 2026-11-25 16:25:50 UTC; categories: `astro-ph.CO`)
- **Evidence for ranking:** No per-paper attention record was available. Included for a reported measurement using over 25 million galaxies across 416 deg² and an explicit comparison of weak-lensing constraints with external distance data.
- **Claimed result:** In the authors' joint w0waCDM analysis, w0=−0.832^{+0.071}_{−0.059} and wa=−1.23^{+0.66}_{−0.44}, a 2.4σ preference for dynamical dark energy; the reported S8 constraint remains consistent with their baseline HSC ΛCDM result.
- **Evidence type:** observational; HSC-Y3 real-space cosmic-shear correlations with DESI DR2 BAO, DES five-year supernova data, and BBN priors.
- **Caveat:** The authors say the dynamical-dark-energy preference is driven primarily by the geometric distance probes, not by the lensing amplitude alone; it is not a discovery-level result.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Cosmology & gravitation

### 5. [State of the UNIONS: Four Milky Way companions discovered in a systematic search for northern Local Group satellites](https://arxiv.org/abs/2611.34775)
- **Abstract:** A systematic search of UNIONS g,r,i imaging identifies four faint Milky Way satellite systems, two of which are candidate ultra-faint dwarf galaxies.
- **Authors:** Simon E. T. Smith, Alan W. McConnachie, Thomas de Boer, Ken C. Chambers, Stephen Gwyn et al.
- **arXiv:** `2611.34775v1` (published 2026-11-25 17:37:22 UTC; categories: `astro-ph.GA`)
- **Evidence for ranking:** No candidate-level attention values were available. Included for four survey discoveries with measured luminosity/size estimates and a clear distinction between candidate galaxies and unclassified faint systems.
- **Claimed result:** The authors identify Boötes VI and Draco III as likely ultra-faint dwarf galaxies and report two still fainter, compact systems named UNIONS 2 and UNIONS 3.
- **Evidence type:** observational; systematic search of Ultraviolet Near-Infrared Optical Northern Survey (UNIONS) imaging.
- **Caveat:** Boötes VI and Draco III still need chemodynamical confirmation; morphology alone cannot determine whether UNIONS 2 and 3 are dark-matter-dominated galaxies.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Astrophysics

### 6. [Measuring the flavor composition of high-energy neutrinos from the Milky Way](https://arxiv.org/abs/2611.34797)
- **Abstract:** The author forecasts that IceCube and KM3NeT may resolve the flavor composition of Galactic high-energy neutrinos in roughly a decade, potentially distinguishing source and propagation scenarios.
- **Authors:** Mauricio Bustamante
- **arXiv:** `2611.34797v1` (published 2026-11-25 17:50:14 UTC; categories: `astro-ph.HE`, `hep-ex`, `hep-ph`, `hep-th`)
- **Evidence for ranking:** No per-paper attention record was emitted. The four-archive cross-list and a quantitative forecast connect Galactic astrophysics with neutrino detection and particle phenomenology.
- **Claimed result:** The author estimates future telescopes could infer the source νe fraction to within 27%; a comparison of Galactic and extragalactic flavor compositions could test strong source magnetic fields or neutrino decay.
- **Evidence type:** forecast/proposal; projected sensitivity for IceCube and KM3NeT, which view the inner Galaxy from complementary hemispheres.
- **Caveat:** This is a forecast, not a flavor measurement; the timeline and precision depend on future exposure and source/propagation assumptions.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Astrophysics; Particle, nuclear & high-energy physics; Instrumentation & detectors

### 7. [Signals from the early Universe: primordial features from the full-shape analysis of BOSS galaxies and eBOSS quasars in combination with Planck](https://arxiv.org/abs/2611.34672)
- **Abstract:** The authors search for oscillatory primordial features in Planck CMB and BOSS/eBOSS large-scale-structure data using multiple templates and find no statistically significant evidence.
- **Authors:** Mario Ballardini, Nicola Barbieri, Antonio Raffaelli, Chiara Moretti, Oliver H. E. Philcox et al.
- **arXiv:** `2611.34672v1` (published 2026-11-25 16:37:25 UTC; categories: `astro-ph.CO`)
- **Evidence for ranking:** No per-paper attention values were available. Included for a joint CMB/galaxy/quasar analysis using full-shape power-spectrum multipoles and an explicit look-elsewhere-adjusted assessment of candidate features.
- **Claimed result:** The authors report no significant detection: the best LSS fits improve χ² by about 6–10 but reach at most 1.6σ global significance after the look-elsewhere correction; the strongest CMB-only feature is about 2.6σ.
- **Evidence type:** observational; Planck PR4, BOSS galaxy clustering, and eBOSS quasar clustering analyzed with one-loop effective field theory of large-scale structure.
- **Caveat:** The LSS amplitude bounds are 1.4–3 times weaker than Planck's over the tested frequencies, and the combined constraints do not strengthen the CMB result because the preferred frequencies do not align.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Cosmology & gravitation; Computational & data methods

### 8. [Nuclear Modification of π⁰ Production in pO and OO Collisions with ALICE](https://arxiv.org/abs/2611.34503)
- **Abstract:** The contribution reports neutral-pion nuclear-modification measurements in proton–oxygen and oxygen–oxygen collisions, intended to separate cold- and hot-nuclear-matter effects.
- **Authors:** Nicolas Strangmann
- **arXiv:** `2611.34503v1` (published 2026-11-25 14:55:18 UTC; categories: `nucl-ex`)
- **Evidence for ranking:** No per-paper attention values were available. Included as an experimental measurement in newly relevant pO/OO systems, comparing their spectra with pp data and with models containing cold and hot matter effects.
- **Claimed result:** The author reports presenting R_pO and R_OO measurements at √sNN=9.62 TeV and 5.36 TeV respectively, using ALICE π⁰ transverse-momentum spectra.
- **Evidence type:** experimental; ALICE electromagnetic-calorimeter π⁰ spectra in pO, OO, and pp collisions.
- **Caveat:** The abstract does not provide numerical modification-factor values or uncertainties, so the magnitude of the reported effects cannot be assessed from the abstract alone.
- **Announcement type:** new submission, 2026-11-26 announcement batch.
- **Themes:** Particle, nuclear & high-energy physics; Instrumentation & detectors

## Trending Research Themes

- **Quantum information reaches both hardware and theorem:** the Heron r2 experiments test non-Clifford witnesses on real processors (paper 1), while paper 3 gives a rigorous NPT bound-entanglement example. These are complementary experimental and theoretical contributions, not independent confirmation of one result.
- **Numerical tools are being treated as part of the physics result:** O-REX links fluctuation relations to measurable algorithmic cost in lattice simulations (paper 2); the primordial-feature study uses full-shape large-scale-structure modeling and look-elsewhere correction to interpret cosmological data (paper 7). Their numerical methods address different systems, not a shared dataset.
- **Cosmology is leaning on multi-probe consistency rather than a single anomaly:** the HSC cosmic-shear analysis combines lensing with distance probes (paper 4), while the primordial-feature search compares CMB constraints with BOSS/eBOSS clustering (paper 7). Both report limits on stronger interpretations: a 2.4σ parameter preference in one case and no significant feature in the other.
- **Complementary channels help separate source physics from backgrounds:** ALICE's pO/OO/pp comparison targets cold versus hot nuclear matter (paper 8), while the Galactic-neutrino forecast uses flavor composition and hemisphere-complementary observatories to distinguish production/propagation scenarios (paper 6). These are isolated signals in distinct fields, not a single shared trend dataset.

## Open Problems and Research Directions

- **Quantum hardware — author-stated:** paper 1 notes that finite shots and routing/depth limits constrain some witnesses, and that its single-chip runs do not close the locality loophole. **Research direction (synthesis):** repeat the open benchmark suite on all-to-all hardware and at larger connected hypergraph sizes, reporting raw rates separately from SPAM diagnostics.
- **Lattice topology — author-stated:** paper 2 demonstrates O-REX in the two-dimensional CP^{N−1}, N=21 model and points to four-dimensional gauge-theory applications. **Research direction (synthesis):** test the predicted acceptance/cost scaling in additional lattice gauge theories and check whether the reported cost advantage survives realistic update costs and continuum extrapolations.
- **Dynamical dark energy — author-stated:** paper 4 says its 2.4σ preference is primarily driven by geometric distance probes. **Research direction (synthesis):** use independent Stage-IV lensing and distance datasets with matched nuisance/systematics treatment to test whether the preference persists without being dominated by the distance ladder.
- **Faint satellites — author-stated:** paper 5 says chemodynamics are required to secure Boötes VI and Draco III classifications and morphology is insufficient for UNIONS 2/3. **Research direction (synthesis):** obtain deeper follow-up imaging and spectroscopy to constrain stellar populations, velocities, and dark-matter content.
- **Primordial features — author-stated:** paper 7 finds LSS bounds weaker than Planck and no frequency agreement that improves the joint constraints. **Research direction (synthesis):** improve large-scale-structure precision and test matched feature templates/frequency ranges against future CMB and galaxy-survey data with look-elsewhere effects handled consistently.
- **Galactic neutrinos — author-stated:** paper 6's flavor discrimination is prospective and needs future exposure. **Research direction (synthesis):** update the decade-scale sensitivity forecast as IceCube and KM3NeT accumulate data, and compare Galactic and extragalactic samples under explicit source and propagation models.
- **Small-system nuclear matter — evidence gap:** paper 8's abstract gives no numerical R_pO/R_OO values or uncertainties. **Research direction (synthesis):** consult the full proceedings/results and report the measured factors, correlated uncertainties, and model comparisons before drawing conclusions about energy loss in OO collisions.

## Takeaway

This batch mixes concrete hardware and simulation results with observational analyses and forward-looking sensitivity forecasts. The most useful common signal is methodological discipline: each paper pairs a difficult physical question with a stronger discriminator, while several authors explicitly delimit what their current data or model can establish.

## Method and sources

- **Window used:** daily, latest available announcement batch dated 2026-11-26; submissions in the 2026-11-24 19:00:00 UTC to 2026-11-25 19:00:00 UTC window. The snapshot was taken 2026-11-28 03:28:52 UTC. The batch is prior to the current date because the checked arXiv recent pages had no newer batch dated 2026-11-27.
- **Archive coverage:** checked the recent listings for `physics.*`, `astro-ph.*`, `cond-mat.*`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`. Those pages contained 635 category-list appearances for the 26 November batch, representing 499 unique arXiv IDs after deduplication; 111 IDs appeared in more than one checked category listing. Each of the eight selected entries was verified against its arXiv abstract page for title, authors, version, submission timestamp, abstract, and categories. The top three papers were also inspected in their arXiv HTML full text for methods/results and limitations.
- **Attention signals:** the supplied file `/home/yizhuan/.research/physics/daily/arxiv-trending-physics-daily-2026-11-27.signals.json` refers to the next window (2026-11-25 19:00 to 2026-11-26 19:00 UTC; announcement date 2026-11-27) and has `pool_size=0`, `with_attention=0`, and an empty candidate list. Its source counts were arXiv 0, Hugging Face 141, Hacker News 23, arXiv lookup 163, and Semantic Scholar 0; all sources were marked `ok`, but no paper-level matches or scores were available to apply to the prior 26 November batch. Thus no zero score is assigned to any selected paper and the ordering is a notable-paper ordering, not a per-paper popularity ranking.
- **Primary sources:** [arXiv recent physics listing](https://arxiv.org/list/physics/recent), [astro-ph](https://arxiv.org/list/astro-ph/recent), [cond-mat](https://arxiv.org/list/cond-mat/recent), [gr-qc](https://arxiv.org/list/gr-qc/recent), [hep-ex](https://arxiv.org/list/hep-ex/recent), [hep-lat](https://arxiv.org/list/hep-lat/recent), [hep-ph](https://arxiv.org/list/hep-ph/recent), [hep-th](https://arxiv.org/list/hep-th/recent), [nucl-ex](https://arxiv.org/list/nucl-ex/recent), [nucl-th](https://arxiv.org/list/nucl-th/recent), [quant-ph](https://arxiv.org/list/quant-ph/recent), and the eight linked abstract pages above. Full-text inspection used arXiv HTML for papers 1–3.
