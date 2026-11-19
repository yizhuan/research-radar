# arXiv physics daily — 18 November 2026

The latest arXiv Physics announcement batch is Wednesday, 18 November 2026. This inferred shortlist contains 7 papers; the main pattern is quantum-hardware work spanning AI-assisted coherence control, logical magic-state preparation, and nanophotonic interfaces, alongside a large JWST catalog and a cross-field kinetic simulation method. Spoken agenda: quantum devices first, then new astronomy data and simulation tools. arXiv has no official trending chart, and this ordering is inferred; citation evidence is especially limited for papers less than a day old. Snapshot: 2026-11-19 01:35 UTC. The latest available batch is 18 November (not a 19 November batch).

## Top papers (ranked)

### 1. [AI Scientist Discovered Robust Quantum Control](https://arxiv.org/abs/2611.21765)
- **Abstract:** The authors introduce QORA, a human-supervised multi-agent system that discovers dynamical-decoupling sequences which nearly double measured coherence in a spin-1 diamond NV ensemble compared with a leading human-designed sequence.
- **Authors:** Jiahao Yan, Xuanying Lai, Xiaoshui Lin, Yizhou Wang, Changyu Yao et al.
- **arXiv:** `2611.21765v1` (published 2026-11-16 19:01:34 UTC; categories: `quant-ph`)
- **Evidence for ranking:** Early paper discussion and indexing surfaced on INSPIRE and specialist paper-summary sites; the paper also reports a direct experimental comparison, with T₂ = 18.6 ± 0.7 μs versus 9.8 ± 1.1 μs for DROID-C3PO. The external material is early discussion, not independent replication.
- **Claimed result:** The authors report that QORA-discovered AID-ROD-1 nearly doubles measured coherence in their NV ensemble, and attribute the improvement to suppression of onsite disorder, drive-amplitude errors, and dipolar interactions.
- **Evidence type:** experimental; closed-loop optical and microwave control and coherence measurements on a dense spin-1 nitrogen-vacancy ensemble, with sequence simulations and human physical interpretation.
- **Caveat:** This is a single platform/ensemble demonstration; transfer to other Hamiltonians and higher-dimensional systems remains untested, and human researchers supplied the physical interpretation.
- **Announcement type:** new submission, 18 November 2026 batch.
- **Themes:** Quantum information; Atomic, molecular & optical physics; Computational & data methods

### 2. [Magic state cultivation with lattice-surgery escape on superconducting hardware](https://arxiv.org/abs/2611.22035)
- **Abstract:** The authors implement and compare two magic-state cultivation escape protocols on IBM Nighthawk, reporting high-fidelity transfer of a cultivated T state into a distance-5 surface code using lattice surgery.
- **Authors:** Haoran Liao, Michael Schutzman, William Munizzi, Pranav Mundada, Gavin Hartnett, Yuval Baum
- **arXiv:** `2611.22035v1` (published 2026-11-17 00:56:04 UTC; categories: `quant-ph`)
- **Evidence for ranking:** Quantum Zeitgeist and Quantum.world covered the experiment soon after release; the Q-CTRL post is a primary-source company account, not independent coverage. The paper reports a first hardware demonstration of lattice-surgery escape and a matched comparison against grafting.
- **Claimed result:** The authors report a cultivated-state logical error probability of 2×10⁻⁵ before escape and fidelity 0.991(2) after ten surface-code rounds at 4.6% shot retainment; the reported per-round logical error is about 0.14%.
- **Evidence type:** experimental; distance-5 code execution on a publicly accessible IBM Nighthawk processor, with hardware-calibrated decoding and postselection.
- **Caveat:** The demonstration stops at distance 5 rather than the larger code distance envisaged for a complete protocol; after ten rounds the cited fidelity uses only 4.6% retainment, and the authors note calibrated-noise simulations underestimate absolute error rates.
- **Announcement type:** new submission, 18 November 2026 batch.
- **Themes:** Quantum information; Instrumentation & detectors

### 3. [oMEGACat-JWST I.: Project description and photometric data release](https://arxiv.org/abs/2611.23150)
- **Abstract:** The authors release a near-infrared photometric and astrometric catalog of about 677,000 sources in Omega Centauri, including more than 86,000 sources below the earlier HST detection limit.
- **Authors:** Maximilian Häberle, Callie Clontz, Massimo Griggio, Mattia Libralato, Isabella Carlton et al.
- **arXiv:** `2611.23150v1` (published 2026-11-17 18:03:37 UTC; categories: `astro-ph.GA`, `astro-ph.SR`)
- **Evidence for ranking:** A substantial catalog/data release from three JWST programs, cross-listed across two astrophysics subfields, with a submission to Astronomy & Astrophysics noted by the authors; early astronomy coverage also appeared.
- **Claimed result:** The authors report >90% recovery of overlapping HST sources, >86,000 additional faint sources, and single-image astrometric precision of 0.15 mas at F115W=18 and about 1 mas at F115W=23.
- **Evidence type:** observational; custom reductions of JWST NIRCam and NIRISS imaging, compared with the prior HST-based catalog.
- **Caveat:** The catalog covers Omega Centauri and its immediate surroundings; this first monitoring epoch does not yet support the planned search for astrometric accelerations, which are needed to constrain orbits of the central fast-moving stars.
- **Announcement type:** new submission, 18 November 2026 batch.
- **Themes:** Astrophysics; Instrumentation & detectors; Computational & data methods

### 4. [An Efficient Method for Directly Integrating the Vlasov Equation in Collisionless and Weakly-Collisional Simulations](https://arxiv.org/abs/2611.23084)
- **Abstract:** The author presents a conservative Lagrangian phase-space method for evolving distribution functions across collisionality regimes, with a public GIZMO implementation and a suite of test problems.
- **Authors:** Philip F. Hopkins
- **arXiv:** `2611.23084v1` (published 2026-11-17 17:09:37 UTC; categories: `astro-ph.CO`, `astro-ph.HE`, `astro-ph.IM`, `physics.plasm-ph`)
- **Evidence for ranking:** Four-way cross-listing connects cosmology, high-energy astrophysics, instrumentation/methods, and plasma physics; the author identifies a public GIZMO implementation and reports validation tests. It is submitted to the Open Journal of Astrophysics.
- **Claimed result:** The author reports a 6+1-dimensional distribution-function scheme that conserves mass, momentum, and energy, represents multi-stream and collisional distributions, and has computational cost described as a modest multiplier of particle-based methods.
- **Evidence type:** computational; numerical test problems and implementation in the GIZMO code, not a new astrophysical observation.
- **Caveat:** The abstract's broad applications to dark matter, plasma, and transport are prospective; the reported validation is a set of test problems rather than production-scale demonstrations across those application areas.
- **Announcement type:** new submission, 18 November 2026 batch.
- **Themes:** Computational & data methods; Astrophysics; Plasma & fluid physics

### 5. [Frequency Multiplexing of Purcell-Enhanced Optically Coherent NV Centers](https://arxiv.org/abs/2611.23046)
- **Abstract:** The authors integrate multiple optically coherent diamond NV centers into one photonic-crystal cavity, report linewidths down to 19 MHz, and demonstrate frequency multiplexing with cavity-enhanced emission.
- **Authors:** Alok Gokhale, Marco E. Stucki, Malo Bezard, Maarten H. van der Hoeven, Kilian Unterguggenberger et al.
- **arXiv:** `2611.23046v1` (published 2026-11-17 16:44:46 UTC; categories: `quant-ph`, `physics.optics`)
- **Evidence for ranking:** The paper links quantum information and optics through measurements on a shared nanophotonic platform, reports a 19 MHz linewidth and multi-emitter frequency multiplexing, and includes finite-element modeling of the cavity response.
- **Claimed result:** The authors report near-lifetime-limited optical coherence and charge-state stability over minutes; cavity tuning increased zero-phonon-line photoluminescence by 16.8(1.4)%, consistent with their Purcell-enhancement model.
- **Evidence type:** experimental; photoluminescence and photoluminescence-excitation measurements of NV centers in a Sawfish diamond cavity at about 5 K, supported by finite-element simulations.
- **Caveat:** The measured emission increase is an ensemble result and the authors expect it to be dominated by a favorable subset of emitters; photon extraction remains a stated engineering step.
- **Announcement type:** new submission, 18 November 2026 batch.
- **Themes:** Quantum information; Atomic, molecular & optical physics; Instrumentation & detectors

### 6. [Atomic-scale Imaging of Time Reversal Breaking Supercurrents in Bi₂Sr₂CaCu₂O₈](https://arxiv.org/abs/2611.23060)
- **Abstract:** Using energy-resolved electronic-state images and a dual neural-network method, the authors infer repeatable supercurrent-flow networks in a disordered cuprate over hole densities p=0.17–0.22.
- **Authors:** Bin Hu, Catherine Dawson, Shuqiu Wang, Siyuan Wan, Huiyu Zhao et al.
- **arXiv:** `2611.23060v1` (published 2026-11-17 16:53:28 UTC; categories: `cond-mat.supr-con`)
- **Evidence for ranking:** The paper makes a concrete experimental claim on a long-standing cuprate question and joins atomic-scale spectroscopy with neural-network inference; this is a notable scientific signal, not corroborated evidence of broad popularity.
- **Claimed result:** The authors infer current loops whose junctions satisfy Kirchhoff's law and report inferred speeds of 1,250–4,000 m/s, consistent with theoretical predictions and reported field amplitudes.
- **Evidence type:** experimental; energy-resolved electronic density-of-states imaging interpreted with the authors' dual-ANN VMAP method and checked against theoretical predictions.
- **Caveat:** Current maps are inferred through a model mapping spectra to flow rather than measured as a direct current image; the reported claim is limited to the stated material and doping range and merits independent, complementary validation.
- **Announcement type:** new submission, 18 November 2026 batch.
- **Themes:** Condensed matter & materials; Computational & data methods

### 7. [Demonstration of a Qubit Control Scheme Compatible with Superconducting Digital Signals](https://arxiv.org/abs/2611.22166)
- **Abstract:** The authors demonstrate common-clock encoded bipolar pulse control for superconducting single- and two-qubit gates, reporting XEB-estimated fidelities of 99.94% and 99.63%, respectively.
- **Authors:** Chenyin Sun, Yu Xu, Zihua Chen, Dayu Li, Tianzuo Sun et al.
- **arXiv:** `2611.22166v1` (published 2026-11-17 03:58:03 UTC; categories: `quant-ph`)
- **Evidence for ranking:** Concrete single- and two-qubit gate measurements add an experimental control-system result to the batch; the paper's relevance to scalable cryogenic digital control is a stated target, not a demonstrated full SFQ deployment.
- **Claimed result:** The authors report 40 ns single-qubit gates at 99.94% average fidelity and 120 ns controlled-Z gates at 99.63%, using a common-clock pulse scheme.
- **Evidence type:** experimental; 25 GSa/s arbitrary-waveform-generator pulses and cross-entropy benchmarking, with separate numerical gate-fidelity estimates.
- **Caveat:** The experiment uses an arbitrary waveform generator to produce the pulse sequences; integration with cryogenic single-flux-quantum hardware remains prospective.
- **Announcement type:** new submission, 18 November 2026 batch.
- **Themes:** Quantum information; Instrumentation & detectors

## Trending Research Themes

- Quantum hardware is being optimized at several layers, not by one shared experiment: QORA (2611.21765) uses a closed-loop AI/human workflow to improve ensemble coherence; the IBM Nighthawk study (2611.22035) tackles logical non-Clifford resource preparation; the gate-control study (2611.22166) explores common-clock pulse delivery; and the NV cavity paper (2611.23046) targets optical interconnects. These papers are distinct demonstrations, not mutual replications.
- Data-driven inference and release recur across fields: the cuprate paper (2611.23060) maps spectroscopic data to inferred current networks, while oMEGACat-JWST (2611.23150) releases a large source catalog and astrometry. They share a high-volume-data/methods pattern, not a common physical result.
- Methods for difficult distribution functions cross astrophysics and plasma physics in the Vlasov work (2611.23084), whose four categories and GIZMO implementation bridge numerical methods and multiple physical applications. Its claims are computational validation, not observational evidence.

## Open Problems and Research Directions

- Open problem (authors state): QORA's approach has so far been shown on a spin-1 NV ensemble; the authors call for extensions to higher-dimensional systems and for AI agents to reason about physical mechanisms. Research direction (synthesis): test on a second platform with independently calibrated noise channels and compare whether the discovered pulse structures transfer (2611.21765).
- Open problem (authors state): magic-state cultivation remains at code distance 5; the authors identify larger-distance expansion, unexplained noise/model mismatch, and low-latency feed-forward as follow-up needs. Research direction (synthesis): test lattice-surgery escape at larger distance while reporting fidelity and retainment together and characterizing leakage, crosstalk, and coherent errors (2611.22035).
- Open problem (authors state): the NV nanocavity study names photon extraction as a next step. Research direction (synthesis): integrate an evanescent fiber interface and measure extraction efficiency alongside linewidth and multi-emitter coherence (2611.23046).
- Open problem (authors state): orbital constraints for Omega Centauri's central fast-moving stars require future monitoring. Research direction (synthesis): combine repeated JWST astrometry with the existing HST baseline and quantify proper-motion systematics at the faint end (2611.23150).
- Open problem (synthesis): the cuprate current map depends on a neural-network translation from spectral data to flow. Complementary probes or blinded validation on independent samples and doping points would test whether the inferred networks are robust (2611.23060).
- Open problem (synthesis): the Vlasov method is validated on test problems while its broad application range is proposed. Benchmark against established particle and kinetic solvers on representative production problems across collisionality regimes (2611.23084).

## Takeaway

The clearest near-term cluster is quantum hardware engineering: coherence protection, magic-state preparation, control electronics, and optical interfaces are being advanced through different experimental routes. The JWST catalog and Vlasov implementation add unusually reusable data and computational infrastructure, while the cuprate current-network claim is potentially consequential but model-dependent and still preliminary.

## Method and sources

- Window: daily arXiv announcement batch dated 2026-11-18; submission interval queried was 2026-11-16 19:00 UTC through 2026-11-17 19:00 UTC. Snapshot: 2026-11-19 01:35 UTC. The most recent batch was used because no 19 November batch was available at snapshot time.
- Coverage: checked the recent listings and arXiv API for physics.*, astro-ph.*, cond-mat.*, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, nucl-ex, nucl-th, and quant-ph. The API queries returned 605 category hits (including cross-lists); deduplication by versionless arXiv ID left 456 unique papers in the batch pool. Seven are selected here, so this is not comprehensive coverage of physics.
- Inference: arXiv publishes no trending ranking. The shortlist uses reported experimental/observational or computational results, cross-listing, code/data release, early independent discussion, and journal/submission signals; recency is only a tie-breaker. Recent papers have little time to accumulate citations. No numerical trend score is claimed.
- Sources: arXiv recent Physics listing (https://arxiv.org/list/physics/recent); arXiv API records and verified abstracts linked above; full text for the three leading papers via arXiv HTML. Early outside discussion checked at INSPIRE (https://inspirehep.net/literature/3230218), Qubitsok (https://qubitsok.com/papers/2611.21765) and Pith (https://pith.science/paper/2611.21765); Quantum Zeitgeist (https://quantumzeitgeist.com/q-ctrl-magic-states-ibm-quantum/), Quantum.world (https://quantum.world/news/q-ctrl-magic-states-ibm-nighthawk), and an early Omega Centauri catalog news item (https://www.bioscience.com.pk/en/subject/astronomy/omegacat-jwst-i-project-description-and-photometric-data-release).
- Retrieval note: the Semantic Scholar Graph API was rate-limited at this snapshot, so citation and influential-citation totals could not be checked and are not reported. The configured web-extraction backend was unavailable; selected abstracts were verified directly on arXiv abstract pages instead.
