# arXiv Physics — 14 October 2026 batch: eight notable papers

The batch's strongest pattern is experimental control: new quantum devices isolate individual excitations or prepare multipartite states, while JWST and nuclear measurements add spatial or angular resolution. I’ll cover those results, then the computational methods tying together radio astronomy, quantum matter, and quantum communication. This is an inferred selection, not an arXiv trending chart: arXiv publishes no official popularity ranking, and citations are too sparse for these just-announced papers to establish momentum.

## Top papers (ranked)

### 1. [Single anyons and anyon binding in a quantum Hall dot](https://arxiv.org/abs/2610.18817)
- **Abstract:** The authors use a graphene quantum Hall dot to trap and tune down to a single fractional quasiparticle, and report charge-addition patterns consistent with an anyon-binding energy comparable to the charging energy.[1]
- **Authors:** Marco Valentini, Will Wang, Amir Shapour Mohammadi, Noah Samuelson, Chengxuan Li, et al.
- **arXiv:** `2610.18817v1` (published 2026-10-13 17:50:04 UTC; categories: `cond-mat.mes-hall`)
- **Evidence for ranking:** A direct, controlled quantum Hall device result with single-quasiparticle tuning and a distinct paired-charge signature; this is a concrete experimental advance rather than a proposal.[1][9]
- **Claimed result:** The authors report resonances consistent with e/3 charge transport and suppression of alternating charge sectors, which they interpret as attractive inter-anyon interactions and an anyon binding energy at least as large as the charging energy.[1][9]
- **Evidence type:** Experimental; graphene quantum Hall dot transport and charge-addition measurements, compared with DMRG calculations.[1]
- **Caveat:** The binding interpretation combines transport/charge-addition signatures with modeling; the authors say large-quasiparticle-number wavefunctions are not known precisely. This is not a direct braiding-statistics measurement.[9]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Condensed matter & materials

### 2. [Deterministic and programmable generation of mechanical multipartite entangled states](https://arxiv.org/abs/2610.18778)
- **Abstract:** The authors prepare and characterize W, GHZ, and cluster states in mechanical resonator modes, certify genuine multipartite entanglement among as many as four modes, and use the states to bound collective dephasing.[2]
- **Authors:** Isabelle Franzen, Max-Emanuel Kern, Q. Rumman Rahman, Igor Kladarić, Stefano Marti, et al.
- **arXiv:** `2610.18778v1` (published 2026-10-13 17:32:44 UTC; categories: `quant-ph`)
- **Evidence for ranking:** The paper reports an implemented state-preparation protocol, tomography, multipartite-entanglement certification, and a sensing demonstration in one mechanical platform.[2][10]
- **Claimed result:** The authors use optimal-control pulses between a superconducting transmon and successive modes of a high-overtone bulk acoustic wave resonator to prepare bond-dimension-two matrix-product states, certifying genuine multipartite entanglement through four modes.[2][10]
- **Evidence type:** Experimental; transmon-coupled acoustic resonator, quantum-state tomography, and correlated-noise sensing.[2]
- **Caveat:** Certification is currently limited to four modes; the authors identify decoherence, preparation errors, and the duration of sequential tomography as scaling limits.[10]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Quantum information

### 3. [A Spatial Map of the Atmospheric Limb of a Hot Jupiter](https://arxiv.org/abs/2610.18806)
- **Abstract:** Applying transmission-string mapping to JWST observations of WASP-17b, the authors resolve temperature variation around the planet's transmitting limb and report an approximately 650 K morning–evening contrast.[3]
- **Authors:** Lili Alderson, Hannah R. Wakeford, David Grant, Nikole K. Lewis, Avinash Verma, et al.
- **arXiv:** `2610.18806v1` (published 2026-10-13 17:46:20 UTC; categories: `astro-ph.EP`)
- **Evidence for ranking:** The preprint is accepted for Nature Astronomy, and its JWST mapping result received separate science coverage; it presents a new spatially resolved observational result, not just a forecast.[3][12]
- **Claimed result:** The authors map WASP-17b from 0.6–12 μm using JWST NIRISS, NIRSpec, and MIRI data, finding a hotter evening limb and constraining H₂O and CO₂ abundances around the limb.[3][11]
- **Evidence type:** Observational; JWST transit spectroscopy with NIRISS/SOSS, NIRSpec/G395H, and MIRI/LRS.[11]
- **Caveat:** This is one planet, and the morning-side temperature has broad uncertainties (858 K with +434/−233 K). Independent coverage notes that the analysis assumes the planet's northern and southern halves match.[3][12]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Astrophysics

### 4. [The 3He(α,γ)7Be γ-ray angular distribution: measured, and calculated by effective field theory](https://arxiv.org/abs/2610.17770)
- **Abstract:** The authors report the first comprehensive angular distribution measurement for this astrophysically important reaction, using 22 high-purity germanium detectors and comparing the data with an EFT-based calculation.[4]
- **Authors:** S. Turkat, P. Hempel, X. Zhang, S. Akhmadaliev, D. Bemmerer, et al.
- **arXiv:** `2610.17770v1` (published 2026-10-13 05:56:12 UTC; categories: `nucl-ex`)
- **Evidence for ranking:** A new multi-angle nuclear measurement is paired with a specific theory comparison and bears on solar-neutrino production and primordial lithium synthesis.[4]
- **Claimed result:** The authors measured γ-ray angular distributions from 27° to 145° over 442–1213 keV center-of-mass energies; they report agreement with a hybrid EFT treatment when E1, M1, and E2 interference is included.[4]
- **Evidence type:** Experimental; 22 high-purity germanium detectors, plus one activation-method astrophysical S-factor point, compared with EFT calculations.[4]
- **Caveat:** The activation method contributes only one S-factor point; the angular measurement covers the stated energy interval, so broader extrapolation still depends on the reaction model.[4]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Particle, nuclear & high-energy physics

### 5. [Evidence for Distinct One-Off and Repeating Subpopulations in CHIME/FRB Catalog 2](https://arxiv.org/abs/2610.18710)
- **Abstract:** Using simulation-based inference on CHIME/FRB Catalog 2, the authors find that models with a truly one-off FRB subpopulation fit better than single-population alternatives, with a random-forest analysis as a second check.[6]
- **Authors:** Sloane Sirota, Duncan R. Lorimer
- **arXiv:** `2610.18710v1` (published 2026-10-13 16:54:53 UTC; categories: `astro-ph.HE`)
- **Evidence for ranking:** The work analyzes a 3,641-burst catalog, compares eight population models, and reports a separate classifier cross-check; it is submitted to ApJ.[6]
- **Claimed result:** The authors say the catalog favors models containing a one-off population and predict the repeater fraction will fall below 2% within five years, eventually reaching about 0.5% as the catalog saturates.[6]
- **Evidence type:** Computational; simulation-based inference and random-forest analysis of CHIME/FRB Catalog 2.[6]
- **Caveat:** This is population-model inference, not a direct identification of intrinsically non-repeating individual sources; the forward predictions remain to be tested against later catalogs.[6]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Astrophysics; Computational & data methods

### 6. [Energy, vertex, and time response of a LiquidO detector with an opaque-scintillator target to Compton-tagged electrons](https://arxiv.org/abs/2610.18849)
- **Abstract:** A 4-liter LiquidO prototype was calibrated with Compton-tagged electrons; the collaboration reports a linear light yield, energy resolution, position localization, and a lower bound on start-time response.[5]
- **Authors:** LiquidO Collaboration: S. Katz, J. T. Moffatt, G. Wendel, D. F. Cowen, I. Jovanovic, et al.
- **arXiv:** `2610.18849v1` (published 2026-10-13 17:58:14 UTC; categories: `physics.ins-det`)
- **Evidence for ranking:** A calibrated prototype measurement with event-by-event energy ground truth provides quantitative detector-performance benchmarks; the manuscript is submitted to Nuclear Instruments and Methods A.[5]
- **Claimed result:** The collaboration reports 48.3 ± 1.5 photoelectrons/MeV across four operating points, (23.4 ± 0.4)% energy resolution, localization bounded by the 20 mm beam spot, and a ≥1.5 ns lower bound on single-scatter start time.[5]
- **Evidence type:** Experimental; 4-liter opaque-scintillator prototype, Compton-coincidence calibration, and tagged ¹³⁷Cs/⁶⁰Co γ-ray sources.[5]
- **Caveat:** These are prototype-scale results; the higher 108–124 photoelectrons/MeV yield is an estimate for changed fiber collection and sensor configurations, not a measured result from this setup.[5]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Instrumentation & detectors

### 7. [A hierarchy of exact lower bounds on the Laughlin spectral gap](https://arxiv.org/abs/2610.18854)
- **Abstract:** The authors combine analytic bounds with finite semidefinite programs to derive lower bounds for the first Haldane pseudopotential's Laughlin gap, including a thermodynamic-limit argument.[7]
- **Authors:** Michael G. Scheer, Eslam Khalaf
- **arXiv:** `2610.18854v1` (published 2026-10-13 17:59:10 UTC; categories: `cond-mat.str-el`)
- **Evidence for ranking:** It offers an explicit computational-to-rigorous-proof workflow and a proposed extension to other model-state pseudopotentials, making the method itself a notable theoretical result.[7]
- **Claimed result:** The authors present a cutoff-sized SDP whose dependence on flux is parametric, plus an algorithm to produce nearly optimal exact feasible points and certify rank stability in the thermodynamic limit.[7]
- **Evidence type:** Theoretical; analytic inequalities and semidefinite-program bounds, with exact certificates subject to the stated solver/feasibility procedure.[7]
- **Caveat:** The demonstrated target is the first Haldane pseudopotential on the sphere; extension to Moore–Read and Read–Rezayi pseudopotentials is described as possible, not established here.[7]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Condensed matter & materials

### 8. [Gaussian entanglement and quantum communication: geodesic optimization and multimode bounds](https://arxiv.org/abs/2610.18827)
- **Abstract:** The authors develop a convex-optimization framework for Gaussian-restricted entanglement measures and use it to bound two-way assisted quantum and private communication under input-energy constraints.[8]
- **Authors:** Hemant K. Mishra, Mark M. Wilde
- **arXiv:** `2610.18827v1` (published 2026-10-13 17:53:59 UTC; categories: `quant-ph`, `cs.IT`)
- **Evidence for ranking:** The paper combines a convergence-guaranteed algorithm, explicit bit-complexity analysis, multimode examples, and openly listed code files; its cross-list links quantum physics and information theory.[8]
- **Claimed result:** The authors derive additive Gaussian-restricted entanglement quantities, prove a geometric convergence rate, and obtain communication bounds that match pure-loss benchmarks in selected two- and three-mode examples.[8]
- **Evidence type:** Computational; convex optimization, controlled numerical integration, and two-/three-mode examples.[8]
- **Caveat:** Gaussian-restricted entanglement quantities need not equal unrestricted ones; the authors treat the latter separately through a photon-number truncation method with controlled error.[8]
- **Announcement type:** new submission, 14 October 2026 announcement batch
- **Themes:** Quantum information; Computational & data methods

## Trending Research Themes

- **Control and measurement of quantum degrees of freedom:** The quantum Hall dot resolves single-charge addition and binding signatures, the acoustic resonator generates multipartite mechanical states, and LiquidO measures the response to tagged electron recoils. These are distinct advances in experimentally isolating signals, not independent confirmations of one another.[1][2][5]
- **Sharper views of astrophysical systems:** JWST's WASP-17b limb map adds spatially differentiated atmosphere constraints, while the CHIME analysis uses catalog-level inference to distinguish possible FRB populations.[3][6]
- **Tools connecting computation and physics:** Simulation-based inference and classifier checks appear in the FRB analysis; semidefinite programming is used for Laughlin-gap bounds; and convex optimization provides Gaussian communication bounds.[6][7][8]
- **Quantum information meets matter:** The mechanical-state experiment and single-anyon device span hardware and correlated phases.[1][2]
- The Laughlin-gap and Gaussian-channel studies add theory linking correlated matter and quantum communication.[7][8]

## Open Problems and Research Directions

- **Open problem (authors):** The anyon paper says large-quasiparticle-number wavefunctions are not known precisely and calls for further experiments on the relation between binding and pairing-like behavior. **Research direction (informed synthesis):** vary confinement and quasiparticle number while measuring addition spectra, and pursue the authors' proposed fractional-charge-pump or single-non-Abelian-anyon extensions.[9]
- **Open problem (authors):** Mechanical-state certification is limited by decoherence, preparation error, and sequential tomography duration. **Research direction (authors):** increase qubit–phonon coupling and coherence, speed readout, and use partial-information characterization to test entanglement across more modes.[10]
- **Open problem (reported uncertainty):** WASP-17b's morning-side temperature remains weakly constrained, and the result comes from one target; independent coverage also notes a north–south symmetry assumption. **Research direction (informed synthesis):** apply the mapping to other planets and test whether relaxing that symmetry changes the inferred limb contrast.[3][12]

## Takeaway

- The strongest experimental signals are single-anyon charging and mechanical entanglement, complemented by JWST atmospheric mapping.[1][2][3]
- The nuclear angular result and CHIME population inference add more targeted constraints.[4][6]
- The Laughlin-gap and Gaussian-channel papers contribute mathematical and computational tools whose extensions remain open.[7][8]

## Method and sources

- **Window:** daily; the latest available arXiv announcement batch was Wednesday, 14 October 2026. Thursday, 15 October had no newer batch at the snapshot time, 2026-10-15 00:26:36 UTC.
- **Coverage:** the recent listings were checked across all 11 configured physics archive groups. The 14 October batch contained 1,392 category-list entries in aggregate (cross-lists can appear in multiple archives; this is not a unique-paper count). The groups checked were physics, astro-ph, cond-mat, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, nucl-ex, nucl-th, and quant-ph.
- The `physics`, `astro-ph`, and `cond-mat` recent listings showed 304, 208, and 324 entries for the 14 October batch.[13][14][15]
- The `gr-qc`, `hep-ex`, and `hep-lat` listings showed 75, 42, and 8 entries.[16][17][18]
- The `hep-ph`, `hep-th`, and `nucl-ex` listings showed 89, 87, and 11 entries.[19][20][21]
- The `nucl-th` and `quant-ph` listings showed 26 and 218 entries.[22][23]
- Eight papers were selected and deduplicated by versionless arXiv ID. Metadata and abstracts for papers 1–3 were checked on arXiv.[1][2][3]
- Metadata and abstracts for papers 4–6 were checked on arXiv.[4][5][6]
- The same metadata and abstract checks were completed for papers 7 and 8.[7][8]
- Full-text HTML was inspected for the first three papers.[9][10][11]
- Ordering is an editorial inference based on concrete result, evidence type, cross-field relevance, journal status where available, and independent coverage where found. No numeric trend score was computed; this is not a measured popularity or readership ranking.

## Sources

[1] https://arxiv.org/abs/2610.18817 — arXiv 2610.18817: Single anyons and anyon binding
[2] https://arxiv.org/abs/2610.18778 — arXiv 2610.18778: Mechanical multipartite entanglement
[3] https://arxiv.org/abs/2610.18806 — arXiv 2610.18806: WASP-17b atmospheric limb
[4] https://arxiv.org/abs/2610.17770 — arXiv 2610.17770: 3He alpha capture angular distribution
[5] https://arxiv.org/abs/2610.18849 — arXiv 2610.18849: LiquidO detector response
[6] https://arxiv.org/abs/2610.18710 — arXiv 2610.18710: CHIME FRB populations
[7] https://arxiv.org/abs/2610.18854 — arXiv 2610.18854: Laughlin spectral gap bounds
[8] https://arxiv.org/abs/2610.18827 — arXiv 2610.18827: Gaussian entanglement and communication
[9] https://arxiv.org/html/2610.18817 — Full text: Single anyons and anyon binding
[10] https://arxiv.org/html/2610.18778 — Full text: Mechanical multipartite entanglement
[11] https://arxiv.org/html/2610.18806 — Full text: WASP-17b atmospheric limb
[12] https://sciquest.org/wasp-17b-hot-jupiter-atmosphere-shape-jwst — SciQuest coverage of WASP-17b mapping
[13] https://arxiv.org/list/physics/recent?show=2000 — arXiv physics recent listings
[14] https://arxiv.org/list/astro-ph/recent?show=2000 — arXiv astrophysics recent listings
[15] https://arxiv.org/list/cond-mat/recent?show=2000 — arXiv condensed matter recent listings
[16] https://arxiv.org/list/gr-qc/recent?show=2000 — arXiv relativity recent listings
[17] https://arxiv.org/list/hep-ex/recent?show=2000 — arXiv high-energy experiment recent listings
[18] https://arxiv.org/list/hep-lat/recent?show=2000 — arXiv high-energy lattice recent listings
[19] https://arxiv.org/list/hep-ph/recent?show=2000 — arXiv high-energy phenomenology recent listings
[20] https://arxiv.org/list/hep-th/recent?show=2000 — arXiv high-energy theory recent listings
[21] https://arxiv.org/list/nucl-ex/recent?show=2000 — arXiv nuclear experiment recent listings
[22] https://arxiv.org/list/nucl-th/recent?show=2000 — arXiv nuclear theory recent listings
[23] https://arxiv.org/list/quant-ph/recent?show=2000 — arXiv quantum physics recent listings
