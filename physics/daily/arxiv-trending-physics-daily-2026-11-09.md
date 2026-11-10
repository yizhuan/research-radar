# arXiv physics daily — 9 November 2026

This batch contains **8 ranked papers**. The strongest pattern is formal methods being used both to discover quantum programs and to establish quantum-query results, alongside new state-resolved measurements in superconductors, neutron optics and molecular spectroscopy. We’ll begin with the quantum algorithm work, then move to direct measurements and finish with a dark-matter sensitivity study and a soft-matter result. arXiv publishes no official trending chart; this ordering is an inferred notable-paper ranking, not a readership or download measure, and citation evidence is sparse for papers this new.

## Top papers (ranked)

### 1. [Discovering formally verified quantum programs with AI](https://arxiv.org/abs/2611.09822)
- **Abstract:** The authors use LLM-agent teams and Lean formal specifications to discover quantum programs with machine-checked correctness and resource-cost improvements over prior baselines.
- **Authors:** Sergey Shirobokov, Ben Jaderberg, Katerina Hristova, George Tsoukalas, Johannes Bausch, et al.
- **arXiv:** `2611.09822v1` (published 2026-11-06T18:08:06Z; categories: `quant-ph`, `cs.AI`, `cs.PL`)
- **Evidence for ranking:** QubitWire independently discussed the work; the arXiv record cross-lists quantum information with AI and programming languages; the paper supplies explicit formally checked algorithmic cost comparisons. [Independent discussion](https://qubitwire.com/articles/ai-quantum-programs-formal-proof-hardware-gap).
- **Claimed result:** The authors report verified improvements including up to 1.4× fewer expected rounds for parallel search, a 290× spacetime-cost reduction for fixed-point arcsin, and 10.9×, 8.08× and 2.49× lower resource costs for simulations relevant to fusion, photochemistry and drug metabolism.
- **Evidence type:** computational; Lean-verified quantum-program synthesis and resource accounting against prior algorithmic baselines, not a hardware demonstration.
- **Caveat:** The gains depend on human-written formal specifications, chosen baselines and resource metrics; the paper says the verification library and solutions will be open-sourced, so independent reproduction remains pending.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Quantum information, Computational & data methods

### 2. [A proof of the Aaronson-Ambainis conjecture](https://arxiv.org/abs/2611.09773)
- **Abstract:** The author proves the Aaronson–Ambainis influence conjecture for bounded low-degree functions on the Boolean cube and derives a consequence for quantum query algorithms.
- **Authors:** David Turturean
- **arXiv:** `2611.09773v1` (published 2026-11-06T17:36:58Z; categories: `cs.CC`, `quant-ph`)
- **Evidence for ranking:** The author links a Lean 4 formalization and reproducibility materials, and the work is cross-listed in quantum information; its theorem addresses a longstanding question with a direct implication for quantum query complexity. [Formalization and materials](https://github.com/physical-superintelligence/aaronson-ambainis).
- **Claimed result:** For degree-at-most-d functions f:{−1,1}ⁿ→[−1,1], the paper proves that some variable has influence at least c Var(f)^(5/2)/d⁶; in the original normalization this yields (ε/d)^7, supporting the claim that superpolynomial query-model speedups require input structure.
- **Evidence type:** theoretical; mathematical proof on bounded low-degree functions over the discrete cube, with a Lean 4 formalization.
- **Caveat:** The explicit lower bound is quantitatively weak in the original normalization, and the conclusion concerns the query model rather than end-to-end speedups on physical quantum hardware.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Quantum information, Computational & data methods

### 3. [Probing Dark Matter via the Migdal Effect in LUX-ZEPLIN Data](https://arxiv.org/abs/2611.09106)
- **Abstract:** The authors use LUX-ZEPLIN data templates to project how the Migdal effect could constrain sub-GeV dark matter through electronic-recoil signals.
- **Authors:** Yang Yu, Lei Feng
- **arXiv:** `2611.09106v1` (published 2026-11-06T07:38:27Z; categories: `astro-ph.HE`)
- **Evidence for ranking:** An external Cosmos News digest flags the work as an LZ Migdal reinterpretation and explicitly distinguishes it from a new experimental release; the site describes its digest as AI-written, so I use it as a traceable mention rather than expert validation. The paper uses LZ’s 4.2 tonne-year exposure and reports a mass-dependent sensitivity projection. [Cosmos News](https://home.ba.infn.it/~marrone/Cosmos-News.html).
- **Claimed result:** The authors project 90% upper limits from 6.5×10⁻³⁷ to 9.6×10⁻⁴² cm² for dark-matter masses of 0.35–10 GeV and derive light-mediator coupling constraints near α≈10⁻¹²; these are their sensitivity estimates, not an official LZ collaboration limit.
- **Evidence type:** forecast/proposal; Asimov expected-count analysis using LUX-ZEPLIN 4.2 tonne-year templates, a Bayesian posterior and a standard-halo velocity model.
- **Caveat:** The result depends on Migdal ionization probabilities, xenon response and calibration, detection efficiency, background spectra and the assumed halo; the authors note low-mass limits can shift by O(10–100%) under velocity-distribution changes.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Astrophysics, Particle, nuclear & high-energy physics

### 4. [Energy- and momentum-resolved Cooper-pair emission from a cuprate superconductor](https://arxiv.org/abs/2611.09857)
- **Abstract:** Using two-electron ARPES, the authors report a zero-momentum, zero-pair-binding-energy emission peak in an optimally doped cuprate below its superconducting transition that disappears in the normal state.
- **Authors:** Henry Amir, Jack Zwettler, Ka Ho Wong, Genda Gu, Rafael M. Fernandes, et al.
- **arXiv:** `2611.09857v1` (published 2026-11-06T18:41:10Z; categories: `cond-mat.supr-con`, `cond-mat.mtrl-sci`, `cond-mat.str-el`)
- **Evidence for ranking:** A concrete two-electron spectroscopic signature appears only below the superconducting transition, while the anomalous relative-energy broadening adds a second reported observable; the paper spans superconductivity, materials and many-body dynamics.
- **Claimed result:** The authors identify the peak as Cooper-pair emission and report that its relative-energy width grows on cooling while total-energy width stays nearly constant; they argue this behavior points to scattering involving collective excitations.
- **Evidence type:** experimental; two-electron angle-resolved photoemission (2e-ARPES) on optimally doped Bi₂Sr₂CaCu₂O₈₊δ (Bi-2212).
- **Caveat:** The measurement is on one cuprate system, and the proposed collective-excitation explanation for the broadening is interpretive; the paper says data are available from the corresponding author upon reasonable request.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Condensed matter & materials

### 5. [Spin to Orbital Angular Momentum Conversion in the Neutron Nucleus Weak Interaction](https://arxiv.org/abs/2611.09677)
- **Abstract:** The authors combine neutron-beam measurements and theory to argue that parity-violating neutron–nucleus spin rotation is accompanied by orbital angular momentum generation, conserving total angular momentum.
- **Authors:** Niels Geerits, Stephan Sponar, Hartmut Lemmel, Andrea Piovano, Kyle Steffen, William Michael Snow
- **arXiv:** `2611.09677v1` (published 2026-11-06T16:27:15Z; categories: `physics.app-ph`, `nucl-ex`, `quant-ph`)
- **Evidence for ranking:** An experimental result is cross-listed in applied physics, nuclear experiment and quantum physics; the authors report an observable beam-image rotation from a spin-textured neutron beam through ¹³⁹La at the ILL.
- **Claimed result:** Using a magnetic-quadrupole spin texture and a ¹³⁹La sample, the authors report an image rotation associated with parity-violating spin rotation and total-angular-momentum conservation within statistical error.
- **Evidence type:** experimental; thermal-neutron beam with a magnetic quadrupole and 5 cm ¹³⁹La sample at the ILL IN3 instrument.
- **Caveat:** The abstract quotes a maximum rotary power of 2.2×10⁻³ rad cm⁻¹, while the PDF conclusion reports (2.2±0.5)×10⁻⁴ rad cm⁻¹ for the measured rotation; this internal numerical discrepancy needs clarification before quantitative reuse.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Particle, nuclear & high-energy physics, Quantum information, Instrumentation & detectors

### 6. [Classical control of quantum-state relaxation in confined molecular hydrogen](https://arxiv.org/abs/2611.09850)
- **Abstract:** Rotationally resolved infrared measurements and simulations show that increasing H₂ loading suppresses ortho–para nuclear-spin conversion in crystalline molecular hosts at 10 K.
- **Authors:** Nathan McLane, Richard C. Remsing, Leah G. Dodson
- **arXiv:** `2611.09850v1` (published 2026-11-06T18:34:06Z; categories: `physics.chem-ph`, `quant-ph`)
- **Evidence for ranking:** The paper combines direct state-resolved infrared measurements in two host solids with molecular-dynamics and Monte Carlo analysis, and is cross-listed in chemical physics and quantum physics.
- **Claimed result:** The authors find that increasing H₂ concentration suppresses conversion by nearly an order of magnitude, reaching complete suppression at 20% loading; simulations attribute the trend to changes in phonon modes and strain-driven H₂ clustering.
- **Evidence type:** experimental; rotationally resolved infrared spectroscopy of H₂ in crystalline CO₂ and N₂O at 10 K, supplemented by molecular-dynamics and Monte Carlo simulations.
- **Caveat:** The proposed mechanisms partly depend on simulations and the host-crystal environment; the measurements cover two matrices at one temperature, so generality across hosts and conditions remains open.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Atomic, molecular & optical physics, Condensed matter & materials, Quantum information

### 7. [Time-gated optical-parametric-amplification and field-resolved detection of mid-infrared free-induction decay signals](https://arxiv.org/abs/2611.09783)
- **Abstract:** The authors demonstrate time-gated optical parametric amplification for mid-infrared free-induction-decay detection, extending the observable vibrational window in an isopropyl-alcohol test.
- **Authors:** Sergio Revuelta, Gerard Faustino, Ka Fai Mak, Ferenc Krausz, Nicholas Karpowicz
- **arXiv:** `2611.09783v1` (published 2026-11-06T17:43:49Z; categories: `physics.optics`, `physics.chem-ph`)
- **Evidence for ranking:** The experiment reports quantified improvements in signal field, dynamic range, signal-to-noise and observable lifetime using a specified laser–crystal system, providing a checkable instrumentation advance.
- **Claimed result:** With a Cr:ZnS laser and ZnGeP₂ nonlinear crystal, the authors report a 10× signal-field increase, 100× dynamic-range enhancement, 2× signal-to-noise improvement and an observable-window extension up to 72% in isopropyl alcohol.
- **Evidence type:** experimental; time-gated optical parametric amplification and field-resolved mid-IR detection using a Cr:ZnS laser, ZnGeP₂ crystal and isopropyl alcohol.
- **Caveat:** The demonstration uses one model molecule; performance and spectral-resolution gains across more complex molecules and other experimental conditions remain to be established.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Atomic, molecular & optical physics, Instrumentation & detectors

### 8. [Increased Crystal Nucleation in the Glassy State of a Polymer/Water Mixture](https://arxiv.org/abs/2611.09456)
- **Abstract:** Experiments on a PMEA/water mixture find a strong increase in crystal nuclei below the glass-transition temperature, with a nucleation-rate maximum around 10 K below it.
- **Authors:** Mika Kobayashi, Shingo Kobayashi, Kazuyoshi Shiga, Hiroaki Yamada, Masaru Tanaka
- **arXiv:** `2611.09456v1` (published 2026-11-06T13:27:13Z; categories: `physics.chem-ph`, `cond-mat.soft`)
- **Evidence for ranking:** The authors report a material-specific experimental result that challenges the usual classical-nucleation expectation and support its link to cold crystallization with calorimetry; it is cross-listed in chemical physics and soft condensed matter.
- **Claimed result:** In hydrated poly(2-methoxyethyl acrylate), the authors report a nucleation-rate maximum near T_g−10 K and use temperature-history-dependent calorimetry to connect the enhanced sub-T_g nucleation to cold crystallization on heating.
- **Evidence type:** experimental; crystallization and calorimetric measurements of a hydrated PMEA polymer/water mixture.
- **Caveat:** The result is established for one polymer/water mixture; the suggested relevance to other glass-forming liquids remains a hypothesis until tested in additional materials.
- **Announcement type:** new submission, announcement batch 2026-11-09
- **Themes:** Biophysics & soft matter, Condensed matter & materials

## Trending Research Themes

- **Formal tools are moving into quantum algorithm discovery:** Two selected papers turn formal guarantees into a central scientific tool: LLM-agent synthesis is checked against Lean specifications in Shirobokov et al., while Turturean proves an influence theorem relevant to quantum query algorithms and supplies Lean materials. Their claims are different—resource optimization versus a mathematical theorem—but both make verification part of the result. ([arXiv:2611.09822](https://arxiv.org/abs/2611.09822)) ([arXiv:2611.09773](https://arxiv.org/abs/2611.09773))
- **State-resolved probes reach beyond single-particle or ensemble signals:** Amir et al. use 2e-ARPES to resolve a pair-emission signature in Bi-2212; McLane et al. use rotationally resolved IR to follow ortho–para H₂ conversion in two crystalline hosts; Geerits et al. use neutron spin textures and image rotation to study angular-momentum transfer. These are distinct experiments, not independent confirmations of one phenomenon. ([arXiv:2611.09857](https://arxiv.org/abs/2611.09857)) ([arXiv:2611.09850](https://arxiv.org/abs/2611.09850)) ([arXiv:2611.09677](https://arxiv.org/abs/2611.09677))
- **Instrument design and signal processing widen measurable windows:** Revuelta et al. use time-gated amplification to improve weak mid-IR free-induction-decay readout, while the 2e-ARPES work provides access to correlated two-electron emission; these are complementary measurement strategies, not a shared facility or dataset. ([arXiv:2611.09783](https://arxiv.org/abs/2611.09783)) ([arXiv:2611.09857](https://arxiv.org/abs/2611.09857))
- **Dark-matter constraints are being extended through signal reinterpretation (isolated signal):** Yu and Feng apply the Migdal electronic-recoil channel to LZ exposure templates to project low-mass sensitivity. This is a single selected-paper signal and a forecast, not a new LZ detection or collaboration-published limit. ([arXiv:2611.09106](https://arxiv.org/abs/2611.09106))
- **Sub-glass-transition crystallization is a material-specific signal:** Kobayashi et al. report a nucleation-rate maximum below T_g in hydrated PMEA; the proposed connection to broader glass-forming liquids remains untested in this selected corpus. ([arXiv:2611.09456](https://arxiv.org/abs/2611.09456))

## Open Problems and Research Directions

- **Formal quantum-program discovery:** Open problem (paper-stated/synthesis): Shirobokov et al. rely on human-written specifications and compare costs against selected baselines; the manuscript says its Lean library and solutions will be open-sourced. Direction (synthesis): independently audit the released specification and verifier, then test new chemistry or plasma tasks with common resource metrics and third-party baselines. ([arXiv:2611.09822](https://arxiv.org/abs/2611.09822))
- **Strength and implications of the quantum-query theorem:** Open problem (synthesis from the bound): Turturean’s original-normalization guarantee scales as (ε/d)^7, leaving room to sharpen degree/variance dependence. Direction: seek stronger bounds and test how they change concrete query-complexity separations; do not assume direct consequences for hardware advantage. ([arXiv:2611.09773](https://arxiv.org/abs/2611.09773))
- **LZ Migdal projection uncertainties:** Open problem (authors): Migdal probabilities, xenon response, calibration, efficiency, background shape and halo velocities control the projected limits. Direction (synthesis): compare alternative atomic calculations and halo models, and validate the response/background treatment against collaboration-level likelihoods before treating the projection as an experimental constraint. ([arXiv:2611.09106](https://arxiv.org/abs/2611.09106))
- **Pair-emission broadening and neutron result consistency:** Open problem (authors/synthesis): Amir et al. leave the temperature dependence of the relative-energy broadening mechanism unresolved; Geerits et al.’s abstract and PDF conclusion quote rotary-power values differing by a factor of ten. Direction: measure pair-emission widths across doping and temperature, and reconcile the neutron paper’s abstract/text values before follow-up quantitative comparisons. ([arXiv:2611.09857](https://arxiv.org/abs/2611.09857)) ([arXiv:2611.09677](https://arxiv.org/abs/2611.09677))
- **Environmental control and sub-T_g nucleation:** Open problem (authors/synthesis): the H₂ mechanism is inferred partly from simulations in two hosts at 10 K, and the enhanced nucleation result is demonstrated in one PMEA/water system. Direction: vary host, temperature and concentration for H₂, and repeat sub-T_g nucleation measurements in independent glass-forming mixtures to test transferability. ([arXiv:2611.09850](https://arxiv.org/abs/2611.09850)) ([arXiv:2611.09456](https://arxiv.org/abs/2611.09456))

## Takeaway

The batch’s clearest direction is a push toward stronger formal and measurement tools: machine-checked quantum algorithms, direct access to paired or spin-orbit observables, and more sensitive molecular spectroscopy. The most eye-catching claims remain preprint-level: the algorithmic gains depend on formal specifications, the LZ result is a projection rather than a collaboration limit, and the neutron paper contains a numerical inconsistency that should be resolved.

## Method and sources

- **Window:** daily batch date 2026-11-09–2026-11-09; arXiv recent-list pages show the latest batch as Monday, 9 November 2026. This is the current latest batch, not a prior-batch fallback. Snapshot: 2026-11-10T01:35:12Z.
- **Coverage:** arXiv recent pages were checked for physics, astro-ph, cond-mat, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, nucl-ex, nucl-th and quant-ph. Category-list entries in the batch: physics 105, astro-ph 80, cond-mat 97, gr-qc 31, hep-ex 12, hep-lat 5, hep-ph 39, hep-th 47, nucl-ex 6, nucl-th 14, quant-ph 83 (total 519); after versionless-ID deduplication, 390 distinct papers remained.
- **Verification:** arXiv API metadata supplied versions, submission timestamps and categories; every selected arXiv abstract page was fetched and title-matched. PDF text was inspected for the three highest-ranked papers, including the LZ sensitivity analysis; the neutron paper’s abstract/conclusion discrepancy is flagged above.
- **Inference:** there is no official arXiv trending chart. Ranking prioritizes checkable external mentions where found (QubitWire coverage; an AI-written Cosmos News digest entry for the LZ reinterpretation), an author-linked Lean formalization for the theorem, then specific measurement/theory results and cross-listing. Recency is a tie-breaker; no numeric trend score is used.
- **Citation signal:** Semantic Scholar Graph batch requests were rate-limited during this run, so no citation totals are reported; citations were not treated as gains during the batch.
- **Sources:** [arXiv:paper-1](https://arxiv.org/abs/2611.09822), [arXiv:paper-2](https://arxiv.org/abs/2611.09773), [arXiv:paper-3](https://arxiv.org/abs/2611.09106), [arXiv:paper-4](https://arxiv.org/abs/2611.09857), [arXiv:paper-5](https://arxiv.org/abs/2611.09677), [arXiv:paper-6](https://arxiv.org/abs/2611.09850), [arXiv:paper-7](https://arxiv.org/abs/2611.09783), [arXiv:paper-8](https://arxiv.org/abs/2611.09456). External context: [QubitWire coverage](https://qubitwire.com/articles/ai-quantum-programs-formal-proof-hardware-gap), [Cosmos News](https://home.ba.infn.it/~marrone/Cosmos-News.html), [Aaronson–Ambainis Lean repository](https://github.com/physical-superintelligence/aaronson-ambainis).
