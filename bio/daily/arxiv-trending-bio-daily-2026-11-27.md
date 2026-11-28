# Biology & biomedicine on arXiv — latest available batch, 27 November 2026

Five notable papers from the latest official Quantitative Biology listing currently visible on arXiv, labeled Thursday 26 November and announced 27 November at 01:00 UTC. The selected work spans RNA inverse design, spatial cell-state inference, molecular binding models, and interpretable medical-image classification. This is a relevance-ranked fallback, not a “hottest” ranking: the supplied 27 November signal pool is empty, arXiv has no official trending chart, and its preprint listings cover only part of biomedical research. The five records below predate the supplied signal window and are clearly identified as the prior available listing.

## Notable recent papers (relevance-ranked)

### 1. [KnitNet: Learning to Search at Inference Time for Exact RNA Inverse Design](https://arxiv.org/abs/2611.33812)
- **Abstract:** KnitNet uses verifier feedback to iteratively repair candidate RNA sequences toward exact computational fold-back matches, with reported gains on five secondary-structure benchmarks and improved 3D structural self-consistency.
- **Authors:** Antonia Panescu, Xin Wang, Haoran Xu, Qingyu Chen, Carlos Oliver, Rex Ying
- **arXiv:** `2611.33812v1` (published 2026-11-25 05:42:56 UTC; categories: `q-bio.BM` (primary), `cs.AI`, `cs.LG`)
- **Evidence for ranking:** No candidate-level signal or score was available for this paper; selected for direct RNA-design relevance and quantified benchmark results, not measured popularity.
- **Claimed contribution:** The authors report an average 21-percentage-point increase in exact solves versus continued sampling with 70% less time-to-solve across five secondary-structure benchmarks; they also report higher 3D self-consistency and faster inference than per-target reinforcement learning.
- **Caveat:** These are computational folding and benchmark results; the paper does not establish experimental folding or biological function.
- **Announcement type:** New submission; latest available listing dated 2026-11-26, announced 2026-11-27.
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 2. [Resolving cell states in spatial transcriptomics with SCATTER](https://arxiv.org/abs/2611.34798)
- **Abstract:** SCATTER estimates cell-type proportions and within-cell-type expression at spatial transcriptomic spots using spatial context and annotated single-cell reference profiles.
- **Authors:** Lei Huang, Yun Gong, Weiqiang Lin, Lindong Jiang, Hui Shen, Chaoyang Zhang, Hong-Wen Deng
- **arXiv:** `2611.34798v1` (published 2026-11-25 17:50:26 UTC; categories: `q-bio.QM` (primary))
- **Evidence for ranking:** No candidate-level HF/HN score was supplied; Semantic Scholar returned 0 citations and 0 influential citations at retrieval. Selected for direct spatial-omics relevance, not popularity.
- **Claimed contribution:** Across five pseudo-spot benchmarks, the authors report higher cross-spot correlations than three comparators for 82.8–99.8% of evaluated gene–cell-type pairs, plus computational analyses of breast cancer, multiple-sclerosis, and colorectal-cancer tissue data.
- **Caveat:** Much of the quantitative comparison uses pseudo-spots; the tissue applications are computational analyses and do not independently establish biological validation.
- **Announcement type:** New submission; latest available listing dated 2026-11-26, announced 2026-11-27.
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Bioinformatics & sequence analysis

### 3. [Exclusion and internal structure in the association/dissociation kinetics of DNA-binding proteins in the fast diffusion limit](https://arxiv.org/abs/2611.33740)
- **Abstract:** The paper develops a coarse-grained stochastic model for DNA-binding proteins that combines footprint exclusion, diffusion, and conformational switching, and fits it to previously measured RPA–ssDNA dynamics.
- **Authors:** Xiangting Li, Tom Chou
- **arXiv:** `2611.33740v1` (published 2026-11-25 04:01:12 UTC; categories: `q-bio.BM` (primary), `cond-mat.soft`, `cond-mat.stat-mech`, `q-bio.QM`)
- **Evidence for ranking:** No candidate-level score was available; selected for direct molecular-biophysics relevance and reported comparison with simulations and prior RPA measurements, not popularity.
- **Claimed contribution:** The authors derive an effective Markov model and mean-field approximation for fast-diffusing proteins, then use multisegment binding states to represent facilitated exchange and the balance between affinity and remodeling.
- **Caveat:** The model relies on a fast-diffusion assumption and is fitted to previously measured RPA dynamics; this is not a new binding experiment, and applicability to other proteins remains to be tested.
- **Announcement type:** New submission; latest available listing dated 2026-11-26, announced 2026-11-27.
- **Themes:** DNA & genomics; Biochemistry & proteins; Quantitative methods

### 4. [From the Deterministic Hook Effect to Stochastic Reliability in Ternary Complex Formation](https://arxiv.org/abs/2611.33753)
- **Abstract:** Deterministic equations and stochastic simulations examine how mediator dose, reaction volume, and copy-number thresholds affect reliable ternary-complex formation in a minimal binding model.
- **Authors:** Deepak K. Agrawal
- **arXiv:** `2611.33753v1` (published 2026-11-25 04:12:08 UTC; categories: `math.DS` (primary), `q-bio.BM`, `q-bio.MN`)
- **Evidence for ranking:** No candidate-level score was available; selected for direct relevance to molecular binding and its explicit stochastic-versus-deterministic comparison, not popularity.
- **Claimed contribution:** In exact stochastic simulations, the author reports that small modeled volumes can fail to accumulate enough complexes despite a favorable deterministic response; volume, thresholds, completion rates, and breakup rates change the modeled reliability range.
- **Caveat:** The results concern a minimal mathematical model and catalytic extension; no experimental system or clinical outcomes are reported.
- **Announcement type:** New submission, cross-listed; latest available listing dated 2026-11-26, announced 2026-11-27.
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 5. [DDxBasis: Explaining Frozen Foundation Encoder-based Medical Classification by Exact Differential Diagnosis](https://arxiv.org/abs/2611.33358)
- **Abstract:** DDxBasis represents frozen-image-encoder classifications as differential-diagnosis-style contrasts and evaluates them across five medical-image datasets.
- **Authors:** Luojie Huang, Gregory N. McKay, Nicholas J. Durr
- **arXiv:** `2611.33358v1` (published 2026-11-24 19:46:14 UTC; categories: `cs.CV` (primary), `q-bio.QM`)
- **Evidence for ranking:** No candidate-level score was available; selected as a biomedical methods paper cross-listed to quantitative biology, not as a popularity leader.
- **Claimed contribution:** The authors report exact concept-level decomposition of model decisions and performance competitive with published domain-specific methods across five datasets; they also report analyses of recovered structure and shortcut features.
- **Caveat:** These are retrospective model and dataset results, not evidence of clinical utility or prospective performance; external-site validation remains necessary.
- **Announcement type:** New submission, cross-listed; latest available listing dated 2026-11-26, announced 2026-11-27.
- **Themes:** Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- **Computational molecular design and interaction models:** KnitNet searches RNA sequence space using folding-verifier feedback; Li and Chou model DNA–protein occupancy and exchange; Agrawal models stochastic ternary-complex reliability. The common thread in this selected set is explicit modeling of molecular constraints, not a demonstrated field-wide shift or experimental convergence.
- **Spatial cell-state inference:** SCATTER separates changes in cell-type proportions from within-cell-type expression in spatial spots. It is the sole selected spatial-omics paper, so it is a notable method, not evidence of a broad trend.
- **Interpretable biomedical prediction:** DDxBasis structures image-classifier explanations as diagnosis contrasts. It is also a single-paper signal and remains a retrospective computational evaluation.

## Open Problems and Research Directions

These are follow-up proposals grounded in the selected papers, not claims that the authors established novelty or clinical readiness.

- **RNA design to function (KnitNet):** Synthesize a preregistered subset of designed sequences, measure structure with an orthogonal assay, and compare intended function with matched controls, including pseudoknotted targets.
- **Spatial-expression validation (SCATTER):** Test on independent, multi-platform tissues with cell-type-specific measurements not used to construct pseudo-spots; quantify calibration and failure under reference-cell mismatch.
- **Binding-model generalization (Li & Chou; Agrawal):** Measure exchange and complex-formation distributions across protein footprints, concentrations, and reaction volumes, then test model predictions beyond fitted RPA data and idealized networks.
- **Explanation robustness (DDxBasis):** Evaluate faithfulness and expert agreement on external-site image cohorts with acquisition and prevalence shifts; this is a research direction, not clinical guidance.

## Takeaway

The latest available official listing is dated 26 November, announced on 27 November; its selected work is strongest in computational RNA design and molecular-interaction modeling, with one spatial-omics method and one medical-image explanation method. The supplied 27 November candidate pool is empty, so this is a relevance-ranked fallback rather than a measured popularity list, and none of these five records falls within the manifest's stated submission interval.

## Method and sources

- **Window and snapshot:** Daily signal window 2026-11-25 19:00:00–2026-11-26 19:00:00 UTC; snapshot 2026-11-28 03:14:59 UTC. The supplied manifest says it was announced 2026-11-27 01:00:00 UTC. The latest official `q-bio/new` listing currently visible is labeled Thursday, 26 November 2026; it is the prior available listing, not a new 27 November list.
- **Window/listing discrepancy:** A category-restricted arXiv API query for the exact manifest interval returned 0 records. The latest 200-result broad query for the configured categories had no record later than 2026-11-25 17:50:26 UTC, before the interval began. The five selected papers appear on the latest official Quantitative Biology listing, but their original published timestamps precede 2026-11-25 19:00 UTC. They are included only because the daily procedure falls back to the most recent available announcement listing; they are not represented as new in the manifest interval.
- **Candidate and attention signals:** Supplied file `/home/yizhuan/.research/bio/daily/arxiv-trending-bio-daily-2026-11-27.signals.json`: `arxiv.status=ok,count=0`; `pool_size=0`; `with_attention=0`; Hugging Face `status=ok,count=141`; Hacker News `status=ok,count=23`; arXiv lookup `status=ok,count=163`; Semantic Scholar `status=ok,count=0`. Those are collector-level source counts, not paper-level values. Since `candidates` is empty, no per-paper HF upvotes, HN points/comments, signal scores, or cross-list score values can be cited. A zero or missing score is not evidence of low scientific importance. Signal weights were HF upvotes 3.0, HN points 1.5, HN comments 1.0, citations 2.0, influential citations 1.0, code stars 0.5, and cross-lists 0.25; no numeric ranking score was calculated.
- **Corroboration:** The Semantic Scholar Graph API returned 0 citation and 0 influential-citation counts for SCATTER. Requests for the other four selected IDs were rate-limited (HTTP 429), so Semantic Scholar citation data is unavailable for them. No paper-level HF/HN attention signal was available. Ranking is by direct relevance and specificity of reported methods/evidence, not attention.
- **Coverage and selection:** Candidates were checked against the latest official Quantitative Biology listing and each selected arXiv abstract page. The top three were checked in full-text HTML where available (KnitNet and the DNA-binding model); SCATTER's full-text HTML was unavailable, so its abstract page supports the summary. The arXiv API query used `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`; no pagination was needed after the initial 200 results because the newest returned result was already older than the requested start date.
- **Primary sources:** [Latest Quantitative Biology listing](https://arxiv.org/list/q-bio/new); the five verified arXiv abstract pages are linked in their titles. This report covers arXiv only, not bioRxiv, medRxiv, or biomedical research as a whole.
