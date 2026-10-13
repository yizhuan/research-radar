# arXiv physics — daily notable papers, Monday 12 October 2026

Eight selected papers from the latest announcement batch, with a strong experimental thread running from quantum hardware and magnetic materials to JWST surveys and cosmological distance measurements. I’ll cover the measurements first, then the computational/theoretical work and the questions still open. arXiv has no official trending chart; this is an inferred, evidence-led selection, not a readership ranking. At the 2026-10-13 00:22 UTC snapshot, Semantic Scholar listed zero citations and zero influential citations for all eight, so popularity evidence is limited and the ordering is best read as notable recent work.

## Top papers (ranked)

### 1. [Evolution and breakdown of chiral anomaly in Weyl semiconductor tellurium](https://arxiv.org/abs/2610.13084)
- **Abstract:** The authors report tunable negative longitudinal magnetoresistance in doped tellurium, its persistence to ambient temperature, and a reversal under extreme quantum-limit conditions that may indicate an interaction-driven phase transition.
- **Authors:** Zhifeng Xue, Jiaji Zhao, Yi Ji, Fuyang Chen, Nannan Tang, et al.
- **arXiv:** `2610.13084v1` (published 2026-10-09 06:38:52 UTC; categories: `cond-mat.mtrl-sci`, `physics.app-ph`, `quant-ph`)
- **Evidence for ranking:** The authors list a 2026 *Communications Physics* journal reference (DOI: 10.1038/s42005-026-02901-3); the work is also cross-listed across materials physics, applied physics, and quantum physics. This is a concrete transport result rather than a popularity signal.
- **Claimed result:** The authors attribute the enhanced negative magnetoresistance to chiral anomaly as the Fermi level approaches the Weyl point; they describe the low-temperature sign reversal beyond the quantum limit as a possible field-induced collective state, not an established phase transition.
- **Evidence type:** Experimental; magnetotransport in doped tellurium under varied Fermi-level and magnetic-field conditions.
- **Caveat:** The proposed collective-state interpretation of the extreme-field reversal is tentative; the abstract does not identify a definitive phase diagnosis.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Condensed matter & materials

### 2. [An entangling Hubbard quasiparticle collider on a digital quantum processor](https://arxiv.org/abs/2610.13946)
- **Abstract:** The authors collide a doublon and holon in a 21-site Fermi–Hubbard chain encoded on 42 qubits, measure quasiparticle transmission consistent with the Bethe-ansatz result, and infer collision-generated number entanglement.
- **Authors:** Chan Bin Bark, Hanbyul Kim, Yoonil Koo, SeungBeom Hong, Seik Pak, et al.
- **arXiv:** `2610.13946v1` (published 2026-10-09 17:59:06 UTC; categories: `quant-ph`, `cond-mat.str-el`)
- **Evidence for ranking:** The paper reports a direct, 42-qubit hardware scattering experiment and is cross-listed between quantum physics and strongly correlated electrons; its measured transmission agrees with an exact Bethe-ansatz benchmark without fitted parameters.
- **Claimed result:** Authors report the first hardware measurement of Hubbard-model quasiparticle transmission and use particle-number fluctuations to infer entanglement between transmitted and reflected components.
- **Evidence type:** Experimental; 21-site/42-qubit Fermi–Hubbard simulation on the `ibm_boston` processor, compared with the Bethe-ansatz scattering matrix.
- **Caveat:** The measured number fluctuations show the component weights but do not directly establish coherence between the transmitted and reflected branches; the authors say a later interference measurement could test that coherence.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Quantum information; Condensed matter & materials; Computational & data methods

### 3. [A Comprehensive JWST Slitless Spectroscopic Census of ∼12,000 Emission-Line Galaxies at Redshift 0∼9 in COSMOS](https://arxiv.org/abs/2610.13920)
- **Abstract:** Using JWST/NIRCam wide-field slitless spectroscopy across 0.33 square degrees, the authors assemble 12,275 emission-line galaxy spectra over redshifts 0–9, with line fluxes, redshifts, and derived properties.
- **Authors:** Shuqi Fu, Zijian Zhang, Danyang Jiang, Jie Chen, Linhua Jiang, et al.
- **arXiv:** `2610.13920v1` (published 2026-10-09 17:53:18 UTC; categories: `astro-ph.GA`)
- **Evidence for ranking:** This is a large, reusable JWST spectroscopic catalogue with a stated 3σ line-flux limit and composite spectra spanning cosmic time; the authors say it is submitted to *ApJS*.
- **Claimed result:** The authors report a homogeneous sample of 12,275 objects and composite spectra revealing faint hydrogen-recombination, CO-absorption, and Fe II features.
- **Evidence type:** Observational; JWST/NIRCam COSMOS-3D F444W grism data over 3.9–5.1 μm, combined with multi-band imaging; reported typical 3σ line-flux limit is 3.2×10⁻¹⁸ erg s⁻¹ cm⁻².
- **Caveat:** Slitless-source overlap and many single-line spectra create line-identification/redshift ambiguities; the paper says some contamination requires additional inspection.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Astrophysics; Computational & data methods

### 4. [Magnetic-field-induced detwinning of orientational domains in altermagnet α-MnTe: A single-crystal neutron diffraction study](https://arxiv.org/abs/2610.13444)
- **Abstract:** Single-crystal neutron diffraction shows that an in-plane field near 2 T prepares α-MnTe in a nearly single-orientation magnetic-domain state, with a refined domain population of 0.97:0.03:0.
- **Authors:** Feihao Pan, Yishui Zhou, Sabreen Hammouda, Yinghao Zhu, Soohyeon Shin, et al.
- **arXiv:** `2610.13444v1` (published 2026-10-09 11:45:01 UTC; categories: `cond-mat.mtrl-sci`, `cond-mat.str-el`)
- **Evidence for ranking:** The authors provide a quantitative neutron-diffraction refinement using 61 nuclear and magnetic reflections, a measured field scale, and a nearly complete domain-population estimate; the result addresses domain averaging in a candidate altermagnet.
- **Claimed result:** The authors find field-induced selection of a common Néel-vector orientation in α-MnTe and report an ordered Mn moment of 4.62(8) μB at 2 K and 2 T.
- **Evidence type:** Experimental; single-crystal neutron diffraction at 2 K and 2 T, with refinement of 61 reflections.
- **Caveat:** Unpolarized diffraction cannot distinguish domain repopulation from continuous Néel-vector rotation or resolve time-reversal antiphase domains; the authors therefore call it a near-single-orientation, not a true single-domain, state.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Condensed matter & materials

### 5. [Nailing down the Hubble constant value through time delay cosmography: A 3% measurement from SN Refsdal](https://arxiv.org/abs/2610.12595)
- **Abstract:** The authors infer H₀ = 65.0⁺²·⁰₋₁·⁸ km/s/Mpc from strongly lensed supernova Refsdal, reporting 3.0% precision after adding the host galaxy’s extended surface-brightness data to a cluster-lens model.
- **Authors:** S. Schuldt, C. Grillo, S. H. Suyu, A. Acebron, L. Bazzanini, et al.
- **arXiv:** `2610.12595v1` (published 2026-10-08 18:18:16 UTC; categories: `astro-ph.CO`)
- **Evidence for ranking:** The work reports a quantitative 3% constraint from a single strongly lensed supernova, compares four mass-model realizations, and is submitted to *Astronomy & Astrophysics*; it adds an independent time-delay-cosmography approach to H₀ inference.
- **Claimed result:** Within flat ΛCDM, the authors obtain H₀ = 65.0⁺²·⁰₋₁·⁸ km/s/Mpc and Ωm = 0.30⁺⁰·⁰⁸₋₀·⁰⁹, with the H₀ result agreeing with earlier lensed-supernova estimates.
- **Evidence type:** Observational; SN Refsdal time delays and 77,000 HST host-galaxy pixels, interpreted through cluster-lens mass models.
- **Caveat:** The cluster’s total-mass parameterization is deliberately held fixed to enable comparison with the earlier point-image model; the authors identify lens-mass and time-delay uncertainties as comparable remaining contributors.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Cosmology & gravitation; Astrophysics

### 6. [Determination of U-spin breaking parameters with an amplitude analysis of the decay D⁰→K⁰S,Lπ⁺π⁻](https://arxiv.org/abs/2610.13101)
- **Abstract:** A BESIII simultaneous amplitude analysis of D⁰→K⁰Sπ⁺π⁻ and D⁰→K⁰Lπ⁺π⁻ measures complex U-spin-breaking parameters using 20.3 fb⁻¹ of e⁺e⁻ collision data at 3.773 GeV.
- **Authors:** BESIII Collaboration: M. Ablikim, M. N. Achasov, P. Adlarson, X. C. Ai, C. S. Akondi, et al.
- **arXiv:** `2610.13101v1` (published 2026-10-09 06:55:58 UTC; categories: `hep-ex`)
- **Evidence for ranking:** A large BESIII collaboration and a 20.3 fb⁻¹ sample underpin a simultaneous analysis of both neutral-kaon final states; the authors describe the dataset as significantly larger than in earlier work.
- **Claimed result:** The authors report fitted U-spin-breaking parameter magnitudes from 0.62 to 4.45 and provide resonant fit fractions plus model predictions for average strong-phase parameters.
- **Evidence type:** Experimental; BESIII e⁺e⁻ data collected at √s = 3.773 GeV, analyzed with a simultaneous amplitude fit.
- **Caveat:** The average strong-phase parameters are model predictions from the amplitude analysis; interpretation of resonance-specific quantities depends on that model.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics

### 7. [Impact of ab initio E1 strength on neutron capture rates along the nickel isotopic chain](https://arxiv.org/abs/2610.13868)
- **Abstract:** Ab initio electric-dipole strength calculations for nickel isotopes predict enhanced neutron-capture rates relevant to r-process simulations, with the size of the enhancement varying across isotopes and temperature.
- **Authors:** Francesca Bonaiti, Joanna E. Sobczyk
- **arXiv:** `2610.13868v1` (published 2026-10-09 17:18:37 UTC; categories: `nucl-th`, `astro-ph.HE`, `nucl-ex`)
- **Evidence for ranking:** The work connects nuclear theory, nuclear experiment, and high-energy astrophysics; it benchmarks against measured ⁵⁸Ni photoabsorption and ⁶⁸Ni E1 strength, and explicitly identifies the dominant transform-inversion uncertainty.
- **Claimed result:** Authors report low-lying E1 strength above neutron threshold that grows with neutron number and raises calculated capture rates for ⁶⁸–⁷⁸Ni by factors whose effects increase with temperature and neutron number; for ⁸⁰Ni the enhancement begins near 0.5 GK.
- **Evidence type:** Theoretical and computational; Lorentz-integral-transform coupled-cluster calculations with chiral two- and three-nucleon interactions, propagated into TALYS reaction-rate calculations.
- **Caveat:** The uncertainty is dominated by inversion of the integral transform, and most neutron-rich isotopes considered are beyond experimental reach.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Astrophysics; Computational & data methods

### 8. [Evidence of Taste-Symmetry restoration for Kähler-Dirac fermions on Euclidean Dynamical Triangulations](https://arxiv.org/abs/2610.13791)
- **Abstract:** In quenched Euclidean Dynamical Triangulations, the authors find that Kähler–Dirac fermion mass splittings appear to shrink with lattice spacing, suggesting restoration of the relevant taste symmetry toward the continuum limit.
- **Authors:** Mingwei Dai, Walter Freeman, Mason Grieb, Jack Laiho, Marc Schiffer, Judah Unmuth-Yockey
- **arXiv:** `2610.13791v1` (published 2026-10-09 16:05:04 UTC; categories: `hep-lat`, `hep-th`)
- **Evidence for ranking:** The paper is cross-listed between lattice and theoretical high-energy physics and tests a concrete continuum-limit property using fluctuating geometries; the authors compare the scale of symmetry breaking with the emergent de Sitter and Planck scales.
- **Claimed result:** The authors find that unprotected bound-state mass splittings scale in a way that decreases as the lattice spacing is reduced, suggesting an analogy with staggered fermions in flat-space lattice theories.
- **Evidence type:** Computational; two-particle bound-state spectra in quenched Euclidean Dynamical Triangulations.
- **Caveat:** The quenched approximation omits matter back-reaction on geometry, and the continuum-restoration conclusion is an extrapolative interpretation of the observed lattice-spacing dependence.
- **Announcement type:** new submission, 12 October 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics; Cosmology & gravitation; Computational & data methods

## Trending Research Themes

- **Controlled quantum and magnetic responses:** The digital Hubbard collider changes transmission with interaction strength and infers number entanglement (2610.13946); α-MnTe’s field-prepared domain populations address domain averaging (2610.13444); doped tellurium’s magnetoresistance varies with Fermi level and field (2610.13084). These are separate systems, not independent replications of a shared result.
- **Survey-scale astronomy and precision cosmology:** JWST/COSMOS-3D supplies a 12,275-object emission-line sample across z≈0–9 (2610.13920), while SN Refsdal’s surface-brightness lens reconstruction yields a 3% single-lens H₀ constraint (2610.12595). Both lean on richer image/spectral data to improve inference, but address different scales and systematics.
- **Theory tied to observables:** The nickel-chain E1 calculation is benchmarked to stable/near-stable nickel data before extrapolating capture rates (2610.13868); the Kähler–Dirac study tracks lattice-spacing dependence in a gravity simulation (2610.13791). These are isolated examples in this small curated set, not evidence of a field-wide shift.

## Open Problems and Research Directions

- **Quantum-collider coherence (author-stated limitation):** Number fluctuations reveal the weights of transmitted and reflected components but do not directly confirm their coherence (2610.13946). An interferometric readout after the collision, at longer accessible evolution times, would test that interpretation.
- **Magnetic-domain mechanism (author-stated limitation):** The neutron data do not separate domain repopulation from continuous Néel-vector rotation or resolve time-reversal domains (2610.13444). Polarized diffraction and field-angle/temperature-dependent measurements could distinguish these mechanisms.
- **JWST line identification (author-stated limitation):** Overlapping traces and frequent single-line detections can leave source and redshift ambiguities (2610.13920). Independent redshift confirmation and quantified completeness/contamination tests would strengthen uses of the catalogue, especially at the highest redshifts.
- **H₀ systematics (author-stated limitation):** The cluster total-mass parameterization remains fixed and lens-mass uncertainty is still important (2610.12595). Repeating the surface-brightness reconstruction across more flexible mass profiles and improving time-delay precision are direct follow-ups.
- **Extrapolations beyond measured nuclei:** The neutron-capture predictions concern isotopes that are difficult or impossible to measure directly, with integral-transform inversion dominating uncertainty (2610.13868). Further benchmarks on accessible isotopes and independent rate-model sensitivity studies would test the reliability of the extrapolation.

## Takeaway

The batch is strongest where authors turn hard-to-access physics into controlled or reusable evidence: tunable transport, quasiparticle scattering on a processor, and a broad JWST spectroscopic catalogue. Several claims remain preprint-level or model-dependent, and even the sharpest numbers—especially the 3% H₀ precision and the extreme-field tellurium interpretation—need their stated systematics and assumptions kept in view.

## Method and sources

- **Window:** daily; latest arXiv announcement batch dated Monday, 12 October 2026. Snapshot: 2026-10-13 00:22:35 UTC. The run was early on Tuesday UTC, so the report uses the latest available prior batch, not an October 13 batch.
- **Coverage:** checked the current `recent` pages for all 11 configured physics archives: `physics`, `astro-ph`, `cond-mat`, `gr-qc`, `hep-ex`, `hep-lat`, `hep-ph`, `hep-th`, `nucl-ex`, `nucl-th`, and `quant-ph`. The daily pages contained 493 archive-category appearances before cross-list deduplication; the report selects eight version-distinct papers. Each selected arXiv abstract page and metadata was checked.
- **Ranking:** arXiv provides no official trending chart. Semantic Scholar Graph API returned 0 citations and 0 influential citations for each of the eight at the snapshot; these near-new papers therefore cannot be separated by meaningful citation momentum. The ordering emphasizes checkable cross-field relevance, concrete measurements/datasets, journal or submission status where stated, and explicit scientific results; it is a notable-paper selection, not a popularity ranking.
- **Sources:** [arXiv Physics recent](https://arxiv.org/list/physics/recent), [Astrophysics recent](https://arxiv.org/list/astro-ph/recent), [Condensed Matter recent](https://arxiv.org/list/cond-mat/recent), [General Relativity recent](https://arxiv.org/list/gr-qc/recent), [HEP-Experiment recent](https://arxiv.org/list/hep-ex/recent), [HEP-Lattice recent](https://arxiv.org/list/hep-lat/recent), [HEP-Phenomenology recent](https://arxiv.org/list/hep-ph/recent), [HEP-Theory recent](https://arxiv.org/list/hep-th/recent), [Nuclear Experiment recent](https://arxiv.org/list/nucl-ex/recent), [Nuclear Theory recent](https://arxiv.org/list/nucl-th/recent), [Quantum Physics recent](https://arxiv.org/list/quant-ph/recent); selected canonical arXiv abstracts linked above; Semantic Scholar Graph API; [Communications Physics article record for the tellurium paper](https://www.nature.com/articles/s42005-026-02901-3).
