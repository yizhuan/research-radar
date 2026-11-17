# arXiv Physics Daily — 16 November 2026

## Headline

**Physics · announcement batch 2026-11-16 · 303 eligible papers; 8 selected.** This batch is strongest in measurement-to-inference work: a short X-ray transient, a pair of Euclid DR1 analyses, and new tools for many-body spectroscopy, turbulent plasma heating, and cosmological inference. Spoken agenda: one transient, two Euclid results, then quantum, plasma, and model-building advances. **Global caveat:** arXiv publishes no official trending chart, so this is an inferred notable-paper ordering—not a popularity ranking—and citation evidence is limited for papers only days old.

## Top papers (ranked)

### 1. [Discovery of a Short-Duration Fast X-ray Transient Associated with a Short Gamma-Ray Burst](https://arxiv.org/abs/2611.18210)
- **Abstract:** The authors report an approximately 8-second extragalactic fast X-ray transient coincident with short GRB 260411A, whose joint X-ray/gamma-ray properties support a compact-object-merger interpretation.
- **Authors:** Yi-Han Iris Yin, Run-Duo Liang, Hui Sun, Jun Yang, Haiwu Pan, et al.
- **arXiv:** `2611.18210v1` (published 2026-11-13 14:15:29 UTC; categories: `astro-ph.HE`)
- **Evidence for ranking:** A separate report highlighted the Einstein Probe event; Semantic Scholar listed 0 citations and 0 influential citations at the snapshot, so placement rests on the unusual observed event and independent coverage, not citation momentum. [Coverage](https://cosmicherald.com/article/einstein-probe-8-second-x-ray-flash-short-gamma-ray-burst-november-2026).
- **Claimed result:** The authors identify EP260411a in archival Einstein Probe Wide-field X-ray Telescope data, temporally coincident with GRB 260411A; joint EP-WXT/Fermi-GBM spectral fitting and its position in the Type-I GRB relation support, but do not prove, a merger origin.
- **Evidence type:** observational; archival Einstein Probe EP-WXT search, Fermi-GBM gamma-ray data, joint spectral fits, and ZTF follow-up constraints.
- **Caveat:** It is one event; the roughly 3-arcminute localization and incomplete galaxy catalog leave no unique host or precise redshift, limiting the progenitor classification.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Astrophysics; Instrumentation & detectors

### 2. [Euclid Data Release 1 (DR1). Enhancing deep-learning models: the impact of image processing and training data selection for strong-lens detection](https://arxiv.org/abs/2611.17420)
- **Abstract:** The Euclid Collaboration tests how image representation, preprocessing, and training-set composition affect a strong-lens classifier, finding that simulation pre-training, realistic negatives, and ensembling improve high-recall searches on DR1.
- **Authors:** Euclid Collaboration: M. Fogliardi, P. Holloway, S. Schuldt, P. Rosati, S. H. Vincken, et al.
- **arXiv:** `2611.17420v1` (published 2026-11-12 19:00:07 UTC; categories: `astro-ph.CO`, `astro-ph.GA`)
- **Evidence for ranking:** A concrete survey-scale evaluation across about 67 million DR1 cutouts, an official Euclid DR1 release, and an INSPIRE record provide corroborating data-release and research signals; this is a pipeline result, not a lens-discovery count. [Euclid DR1 release](https://euclid-ec.net/) · [INSPIRE record](https://inspirehep.net/literature/3228758).
- **Claimed result:** The authors report that their logit-mean ensemble recovers 11,256 visually graded A/B lens candidates among about 70,000 candidates selected for inspection and reaches about 80% recall at the operational threshold; omitting simulation pre-training sharply reduces high-recall precision.
- **Evidence type:** computational; ConvNeXt-Base ablations using simulated and real Euclid imaging, a fixed test set, and approximately 67 million DR1 cutouts.
- **Caveat:** Visual grades include subjective judgments, and conclusions are established for one fully fine-tuned network architecture; transfer to smaller or different models remains untested.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Astrophysics; Computational & data methods

### 3. [Quantum phase estimation on a Rydberg quantum simulator](https://arxiv.org/abs/2611.18122)
- **Abstract:** The authors reconstruct the phase-sensitive Loschmidt echo on an analog Rydberg simulator and use its Fourier transform to measure absolute ground-state energies, gaps, and spectral-window observables in systems up to 19 atoms.
- **Authors:** Hendrik Timme, Benjamin F. Schiffer, Ohad Lib, Shijia Sun, Maximilian Ammenwerth, Dominik S. Wild, J. Ignacio Cirac, Immanuel Bloch, Johannes Zeiher
- **arXiv:** `2611.18122v1` (published 2026-11-13 12:52:16 UTC; categories: `quant-ph`, `physics.atom-ph`)
- **Evidence for ranking:** A laboratory demonstration of phase-sensitive many-body spectroscopy without auxiliary qubits or controlled evolution, cross-listed in quantum and atomic physics.
- **Claimed result:** The authors demonstrate statistical quantum phase estimation on an analog Rydberg simulator, reconstructing complex return amplitudes and measuring absolute energies and gaps while selecting spectral windows for magnetization observables.
- **Evidence type:** experimental; analog Rydberg-atom simulator with one- and two-dimensional arrays of up to 19 atoms.
- **Caveat:** The demonstration is finite-size; the authors note that Hamiltonian calibration errors shift the energy offset and that this contribution is not included in the reported statistical uncertainties.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Quantum information

### 4. [Turbulence at the Correlation Scale as the Driver of Magnetic Reconnection: In Situ Observations and Kinetic Simulations](https://arxiv.org/abs/2611.17450)
- **Abstract:** Using Magnetospheric Multiscale observations and kinetic particle-in-cell simulations, the authors link upstream reconnecting fields to turbulence at the correlation scale and estimate a substantial reconnection contribution to turbulent heating.
- **Authors:** M. Bilal Khan, Michael A. Shay, Riddhi Bandyopadhyay, Subash Adhikari, William H. Matthaeus, et al.
- **arXiv:** `2611.17450v1` (published 2026-11-12 19:21:07 UTC; categories: `physics.plasm-ph`, `physics.space-ph`)
- **Evidence for ranking:** It combines in-situ MMS measurements with cross-method kinetic-simulation validation and spans plasma and space physics.
- **Claimed result:** The authors find correlation-scale upstream fields predict much higher reconnection rates and heating than estimates based on dissipation-scale amplitudes, and estimate reconnection heating at roughly one-fifth of the turbulence cascade rate.
- **Evidence type:** observational; Magnetospheric Multiscale measurements in the terrestrial magnetosheath, checked with fully kinetic particle-in-cell simulations and a simplified exhaust-heating model.
- **Caveat:** The heating fraction depends on a simplified exhaust model and the sampled plasma conditions; the estimate is not a direct calorimetric measurement of the global turbulent energy budget.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Plasma & fluid physics

### 5. [Full-shape analysis of the Lyman-alpha forest power spectrum and bispectrum: validation on simulations](https://arxiv.org/abs/2611.17405)
- **Abstract:** The authors develop an effective-field-theory model combining Lyman-alpha forest power spectra and bispectra, validate it on AbacusSummit mocks at redshift 2.5, and find that the bispectrum improves simulated constraints on the clustering amplitude.
- **Authors:** Roger de Belsunce, James M. Sullivan, Mikhail M. Ivanov
- **arXiv:** `2611.17405v1` (published 2026-11-12 19:00:01 UTC; categories: `astro-ph.CO`, `hep-th`)
- **Evidence for ranking:** Cross-listing between cosmology and high-energy theory, simulation validation with stated precision gains, and an INSPIRE record support its methodological relevance; the reported constraints are simulation results, not DESI measurements. [INSPIRE record](https://inspirehep.net/literature/3228698).
- **Claimed result:** In idealized fully sampled mocks, the joint full-shape analysis yields unbiased parameters and adding the Lyman-alpha bispectrum improves the simulated constraint on σ₈ by 28%; the authors also report additional gains from quasar clustering statistics.
- **Evidence type:** computational; effective-field-theory modeling validated on large-volume Lyman-alpha mocks painted onto the AbacusSummit N-body simulations at z=2.5.
- **Caveat:** The quoted precision comes from idealized mocks and a fully sampled flux field; observational selection, instrumental effects, and nuisance-systematic control must be tested on DESI data.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Cosmology & gravitation; Computational & data methods

### 6. [Euclid Data Release 1 (DR1): Performance of the redshift measurement and spectroscopic analysis](https://arxiv.org/abs/2611.17960)
- **Abstract:** The Euclid Collaboration describes the DR1 NISP spectroscopic pipeline and validates its redshifts against DESI DR1 and visual inspection in the Euclid Deep Field North.
- **Authors:** Euclid Collaboration: V. Le Brun, M. Moresco, M. Bethermin, S. Quai, N. Borghi, et al.
- **arXiv:** `2611.17960v1` (published 2026-11-13 09:50:42 UTC; categories: `astro-ph.CO`)
- **Evidence for ranking:** It is part of the same major Euclid DR1 release as paper #2, and the Consortium’s DR1 paper index independently identifies the spectroscopy work; the paper reports a direct external redshift comparison. [Euclid DR1 papers](https://www.cosmos.esa.int/en/web/euclid/dr1-papers).
- **Claimed result:** For selected high-quality sources in the Euclid Deep Field North, the authors report 98.5% redshift agreement with DESI DR1, increasing to 98.9% when pipeline probability and reliability estimators are used.
- **Evidence type:** observational; Euclid NISP slitless spectra and SPE processing pipeline, compared with DESI DR1 and visual checks of approximately 4,000 EDF-N sources.
- **Caveat:** The quoted agreement is for selected high-quality EDF-N samples, not a guarantee of accuracy for every source or the full DR1 footprint.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Astrophysics; Instrumentation & detectors

### 7. [Gravitational-wave hierarchical inference from population samples](https://arxiv.org/abs/2611.17428)
- **Abstract:** The authors introduce a gravitational-wave population-inference method that uses samples from astrophysical population models without requiring their probability densities, then test it on GWTC-5.0 detections, simulations, and a grid of population-synthesis models.
- **Authors:** Federico De Santi, Davide Gerosa, Matthew Mould
- **arXiv:** `2611.17428v1` (published 2026-11-12 19:00:53 UTC; categories: `astro-ph.HE`, `gr-qc`)
- **Evidence for ranking:** The sample-only method addresses a concrete obstacle in comparing population-synthesis models with gravitational-wave data, is cross-listed into gravitation, and is indexed by INSPIRE. [INSPIRE record](https://inspirehep.net/literature/3228737).
- **Claimed result:** The authors validate their sample-based method against parametric inference, demonstrate it on simulated hierarchical mergers, and apply it to five formation channels using GWTC-5.0 detections.
- **Evidence type:** computational; gravitational-wave detections, simulated populations, population-synthesis model samples, likelihood and detection-probability surrogates.
- **Caveat:** Population conclusions depend on the accuracy of the single-event likelihood and detection-probability surrogates and on the astrophysical models represented in the tested grid.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Astrophysics; Cosmology & gravitation; Computational & data methods

### 8. [High Entropy Oxides as Room Temperature Anderson Insulators with Colossal Soft Gaps](https://arxiv.org/abs/2611.18433)
- **Abstract:** Combining composition control, angle-resolved photoemission, and transport measurements, the authors argue that a high-entropy oxide hosts interacting Anderson-insulating behavior up to 500 K with a large soft Coulomb gap.
- **Authors:** Elena Salagre, Heather Hare, Eli Rotenberg, Jonathan D. Denlinger, Joshua D. Sugar, et al.
- **arXiv:** `2611.18433v1` (published 2026-11-13 17:12:57 UTC; categories: `cond-mat.mtrl-sci`, `cond-mat.str-el`)
- **Evidence for ranking:** Semantic Scholar listed 0 citations and 0 influential citations at the snapshot; its place is based on complementary ARPES and transport evidence for a tunable correlated-disorder regime, not measured attention.
- **Claimed result:** For the studied La-Sr-Mn-Cr-Fe-Co-Ni oxide series, the authors report localization near the Ioffe-Regel limit and transport consistent with Efros-Shklovskii hopping, with behavior persisting to 500 K at the most disordered composition.
- **Evidence type:** experimental; composition-tuned oxide samples studied with angle-resolved photoemission spectroscopy and electrical transport.
- **Caveat:** The result is specific to the studied oxide series and its transport/spectral interpretation; it does not establish room-temperature Anderson behavior as universal across high-entropy materials.
- **Announcement type:** new submission, announcement batch 2026-11-16.
- **Themes:** Condensed matter & materials

## Trending Research Themes

- **Euclid DR1 as a pipeline-to-catalogue program — papers #2 and #6.** Lens finding focuses on training-set design and candidate ranking across the wide imaging release; spectroscopy tests redshift processing against DESI and EDF-N inspection. They use the same mission release but address different analyses, not independent confirmations of one another’s result.
- **Information-rich inference in complex systems — papers #3, #5, and #7.** The Rydberg experiment extracts phase-sensitive spectral information; the Lyman-alpha work adds bispectrum information to simulated cosmological inference; the gravitational-wave method avoids requiring closed-form population densities. The last two are computational developments, not new observational detections.
- **Cross-scale energy and transient physics — papers #1 and #4.** The transient paper connects an 8-second X-ray event with a short GRB, while the MMS/PIC study connects correlation-scale turbulence to reconnection heating. These are isolated signals from different physical systems, not a shared mechanism.
- **Disorder-driven material response — paper #8 (isolated signal).** The work combines ARPES and transport to probe a composition-dependent insulating regime; further samples and independent replication are needed before generalizing.

## Open Problems and Research Directions

- **Open problem (authors, #1):** The event has no unique host or tight redshift constraint, and one transient cannot establish a population. **Direction (synthesis):** Search additional Einstein Probe/Fermi coincidences and obtain rapid, more precise localizations and multiwavelength follow-up to test the short-duration merger-linked population claim.
- **Open problem (authors, #2):** Visual grades are partly subjective, and the ablations use one ConvNeXt-Base setup. **Direction (synthesis):** Blindly validate a subset with independent lens experts and repeat the selection-function study with alternative architectures as the DR1 footprint expands.
- **Open problem (authors, #3):** The current demonstration is limited to 19 atoms, and calibration uncertainty can shift the reconstructed absolute-energy offset. **Direction (synthesis):** Scale the protocol to larger arrays and report calibration/systematic budgets alongside statistical uncertainties.
- **Open problem (authors, #4):** The inferred heating fraction uses a simplified exhaust model and a limited set of observed/simulated conditions. **Direction (synthesis):** Test the correlation-scale relation across more MMS intervals and plasma regimes, then compare energy budgets in broader kinetic simulations.
- **Open problem (authors, #5–#7):** The Lyman-alpha forecasts rely on idealized mocks, and gravitational-wave population comparisons rely on surrogate accuracy and a finite model grid. **Direction (synthesis):** Validate both pipelines against survey/detection selection effects and systematic variations before using their nominal precision to discriminate cosmological or formation models.
- **Open problem (authors, #6):** The high redshift agreement is reported for selected EDF-N high-quality samples. **Direction (synthesis):** Extend external-catalogue and reliability calibration tests to more source classes and the wider DR1 footprint.
- **Open problem (authors, #8):** The evidence is tied to one composition-tuned oxide family. **Direction (synthesis):** Test further compositions and independent batches with matched spectroscopy and transport to separate disorder, interaction, and sample-quality effects.

## Takeaway

The clearest near-term signal is the shift from instrument data to scalable inference: Euclid DR1 produces large survey-processing tests, while quantum, plasma, and cosmology papers seek more information from measurements and simulations. The most striking observational claim is a single short X-ray transient linked to a short GRB; all eight are new preprints, and the observational, simulation, and model-dependent results still need the follow-up noted above.

## Method and sources

- **Window:** daily; selected arXiv announcement batch **2026-11-16**, the latest posted batch at the **2026-11-17 01:43:46 UTC** snapshot. The current calendar date had no newer batch posted at that time. The batch’s retained first-submission timestamps fall on 2026-11-12 to 2026-11-13 UTC; all 303 eligible records are v1 submissions (none are eligible revisions).
- **Candidate collection:** Retrieved the full recent page (`show=2000`) for each configured archive and checked the batch/date groups. The Mon 16 Nov groups surfaced 118 physics, 98 astro-ph, 108 cond-mat, 19 gr-qc, and 45 hep-th entries; the hep-ex, hep-lat, hep-ph, nucl-ex, nucl-th, and quant-ph recent pages were also checked and had no Mon 16 Nov group. After versionless-ID deduplication this produced 337 IDs; arXiv API metadata/abstract checks verified them, and 34 whose latest version date predated the selected batch were excluded, leaving **303 eligible candidates**. Counts overlap across cross-list pages.
- **Primary-category concentration:** among the 303 eligible candidates, 80 are primarily cond-mat, 78 astro-ph, 55 physics, and 24 hep-th; the other 66 include quant-ph 19, hep-ph 10, CS 10 and smaller gr-qc, math, eess, and nuclear groups. Cross-listed papers are counted once.
- **Ranking:** arXiv provides no popularity ranking. The ordering weighs independent coverage/research indexing where found, concrete new measurements or validated methods, cross-subfield relevance, and survey/data/instrument signals; recency is only a tie-breaker. Semantic Scholar Graph API counts were retrieved for papers #1 and #8 only (both current totals 0 citations and 0 influential citations); other entries have no citation count available here. Because the papers are only days old, no citation gain or age-normalized momentum is inferred. Most ranking weight therefore comes from corroborated scientific evidence, not citation counts.
- **Reading:** arXiv abstract records were checked for all 337 surfaced candidates. The PDFs of the top three (#1–#3) were inspected for introduction, methods/results, and stated limitations where present. Independent corroboration included the linked Euclid/Consortium, INSPIRE, and transient-coverage pages above.
- **Retrieval note:** the configured `web_extract` backend was search-only, so archive pages and abstracts were collected through direct arXiv recent-page HTML and the arXiv Atom API; search was used for corroboration. Citation lookup was rate-limited for most selected entries, and missing citation data were not imputed.
- **Archive pages:** [physics](https://arxiv.org/list/physics/recent?skip=0&show=2000) · [astro-ph](https://arxiv.org/list/astro-ph/recent?skip=0&show=2000) · [cond-mat](https://arxiv.org/list/cond-mat/recent?skip=0&show=2000) · [gr-qc](https://arxiv.org/list/gr-qc/recent?skip=0&show=2000) · [hep-ex](https://arxiv.org/list/hep-ex/recent?skip=0&show=2000) · [hep-lat](https://arxiv.org/list/hep-lat/recent?skip=0&show=2000) · [hep-ph](https://arxiv.org/list/hep-ph/recent?skip=0&show=2000) · [hep-th](https://arxiv.org/list/hep-th/recent?skip=0&show=2000) · [nucl-ex](https://arxiv.org/list/nucl-ex/recent?skip=0&show=2000) · [nucl-th](https://arxiv.org/list/nucl-th/recent?skip=0&show=2000) · [quant-ph](https://arxiv.org/list/quant-ph/recent?skip=0&show=2000)
- **Sources:** [arXiv API](https://export.arxiv.org/api/query), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1), selected arXiv abstract pages, and linked corroborating sources. Snapshot date/time is the UTC value above.
