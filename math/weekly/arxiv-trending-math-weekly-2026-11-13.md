# Mathematics (math.*) weekly — 7 notable papers; latest announcement batch 11 November 2026 (window 7–13 November)

The strongest mathematical pattern in this week's selected papers is explicit structural resolution: counterexamples to broad conjectures, exact classifications, and a new complexity boundary. The short agenda is group cohomology, higher Teichmüller geometry, triangulated manifolds, arithmetic curves, optimization, and polynomial-root loci. ArXiv publishes no official trending chart, so this is an inferred ranking of notable recent papers, not a popularity list; citation evidence for preprints this new is limited.

## Top papers (ranked)

### 1. [The cohomology of finite simple groups is unbounded](https://arxiv.org/abs/2611.11677)
- **Abstract:** The authors show that in each fixed positive degree the cohomology dimensions of finite simple groups, algebraic groups, and quantum groups with simple-module coefficients are unbounded, thereby disproving Guralnick's conjecture.
- **Authors:** Chris Bowman, Damian de la Fuente, Nicolas Libedinsky, David Plaza
- **arXiv:** `2611.11677v1` (published 2026-11-08 23:04:40 UTC; categories: `math.GR`, `math.CO`, `math.RT`)
- **Evidence for ranking:** The paper states an explicit unbounded family and a resolution of a long-standing uniform-boundedness conjecture; its result crosses finite-group cohomology, representation theory, and combinatorics.
- **Claimed result:** The authors construct, for every fixed positive degree, faithful absolutely irreducible modules for finite simple groups whose cohomology dimensions grow without bound; their introduction gives an exact first-cohomology family for sufficiently large primes.
- **Assumptions and setting:** The finite-group constructions use groups of type `PSL` over sufficiently large prime-power fields and faithful absolutely irreducible coefficients; the bounds are not uniform in a fixed characteristic.
- **Caveat:** The fixed-characteristic version remains open in the paper: it asks whether bounds may exist when the characteristic is fixed.
- **Announcement type:** new submission, announcement batch 10 November 2026
- **Themes:** Algebra & number theory; Combinatorics & discrete mathematics

### 2. [A counterexample on the main flatness conjecture for SL_n(C)-Fock bundles](https://arxiv.org/abs/2611.14847)
- **Abstract:** Using cyclic Higgs bundles, the author disproves the conjecture that every SL_n(C)-Fock bundle has a unique strongly positive flat compatible Hermitian metric for every rank n ≥ 3.
- **Authors:** Sotiria Chatzimarkou
- **arXiv:** `2611.14847v1` (published 2026-11-10 23:56:08 UTC; categories: `math.DG`, `math.AG`, `math.GT`)
- **Evidence for ranking:** The preprint gives a rank-uniform counterexample to a named conjecture and connects differential geometry, algebraic geometry, and geometric topology.
- **Claimed result:** The author proves that at each rank n ≥ 3, universal existence and uniqueness cannot both hold: at a positivity wall either the required metric does not exist or nearby fields admit two distinct such metrics.
- **Assumptions and setting:** The construction uses cyclic Higgs bundles on closed oriented surfaces of genus at least two and the associated Fock fields and harmonic metrics.
- **Caveat:** The theorem establishes a disjunction—failure of existence at the wall or failure of uniqueness just before it—rather than identifying which failure occurs in every instance.
- **Announcement type:** new submission, announcement batch 11 November 2026
- **Themes:** Geometry & topology

### 3. [No 13-vertex triangulation of the three-torus](https://arxiv.org/abs/2611.14367)
- **Abstract:** The author rules out a 13-vertex simplicial triangulation of the three-torus using a g₂ lower bound, a reduction to a small simplicial complex, and fundamental-group and Alexander-duality arguments.
- **Authors:** Geunho Lim
- **arXiv:** `2611.14367v1` (published 2026-11-10 17:23:48 UTC; categories: `math.GT`, `math.CO`)
- **Evidence for ranking:** It settles the first unresolved vertex count in a classical minimal-triangulation problem and combines geometric topology with combinatorial and group-theoretic constraints.
- **Claimed result:** The author proves that no simplicial triangulation of T³ has 13 vertices; together with known bounds this leaves the minimum between 14 and 15.
- **Assumptions and setting:** The result concerns finite simplicial triangulations of the topological three-torus; the argument uses the Novik–Swartz g₂ inequality and a classification of fundamental groups of complexes on at most eight vertices.
- **Caveat:** It does not decide whether a 14-vertex triangulation exists, nor prove that the known 15-vertex construction is minimal.
- **Announcement type:** new submission, announcement batch 11 November 2026
- **Themes:** Geometry & topology; Combinatorics & discrete mathematics

### 4. [A Complete Classification of Maximal Hyperelliptic Curves Related to Chebyshev Polynomials](https://arxiv.org/abs/2611.14198)
- **Abstract:** For curves y² = φ_d(x) built from Chebyshev polynomials, the authors classify the prime-characteristic pairs and finite fields over which the curves are maximal, including a criterion for supersingularity in the case p ≡ 1 mod 4.
- **Authors:** Saeed Tafazolian, Jaap Top
- **arXiv:** `2611.14198v1` (published 2026-11-10 15:21:08 UTC; categories: `math.NT`, `math.AG`)
- **Evidence for ranking:** The authors present a complete classification in a concrete arithmetic-geometric family and connect finite-field maximality, Jacobian supersingularity, Frobenius, and Dirichlet L-values.
- **Claimed result:** For p not dividing 2d they determine all pairs (d,p) for which H_d is maximal over a finite extension of F_p, together with the fields; for odd d and p ≡ 1 mod 4, supersingularity is equivalent to maximality over an extension and occurs precisely for d = ℓⁿ with ℓ ≡ 1 mod 4 prime and p a generator modulo ℓⁿ.
- **Assumptions and setting:** H_d is the hyperelliptic curve y² = φ_d(x), with φ_d(t+t⁻¹)=tᵈ+t⁻ᵈ; the stated classification excludes characteristics p dividing 2d.
- **Caveat:** The stated hypotheses exclude the ramified characteristics p | 2d; those cases are outside this classification.
- **Announcement type:** new submission, announcement batch 11 November 2026
- **Themes:** Algebra & number theory; Geometry & topology

### 5. [Two-Stage Mixed-Integer Quadratic Programming in Polynomial Time](https://arxiv.org/abs/2611.14837)
- **Abstract:** The author gives a polynomial-time algorithm for two-stage mixed-integer quadratic programs with an arbitrary quadratic objective when the number of linking variables and each continuous block size are fixed, even as the number of blocks grows.
- **Authors:** Alberto Del Pia
- **arXiv:** `2611.14837v1` (published 2026-11-10 23:39:39 UTC; categories: `math.OC`, `cs.CC`, `cs.DS`)
- **Evidence for ranking:** The result gives a concrete tractability boundary for a central structured optimization model and is cross-listed with computational complexity and algorithms.
- **Claimed result:** The author proves polynomial-time solvability under fixed linking-variable count and fixed block size, with arbitrarily many continuous blocks and an arbitrary quadratic objective.
- **Assumptions and setting:** All integer variables must be among the linking variables; continuous blocks interact only through those variables; linking-variable count and block size are fixed. The paper states that none of these structural conditions can be dropped without complexity consequences.
- **Caveat:** The polynomial-time guarantee is parameter-restricted; the author states the running-time exponent must depend on both fixed structural parameters unless FPT = W[1].
- **Announcement type:** new submission, announcement batch 11 November 2026
- **Themes:** Optimization & control; Combinatorics & discrete mathematics

### 6. [The closure of the nonreal roots of bounded-height polynomials is connected exactly at pronic heights](https://arxiv.org/abs/2611.14517)
- **Abstract:** For the closure C_h of nonreal roots of integer polynomials whose coefficients have modulus at most h, the author proves that C_h is connected exactly when h is pronic and gives detailed component results at other heights.
- **Authors:** Bernat Espigule
- **arXiv:** `2611.14517v1` (published 2026-11-10 18:58:59 UTC; categories: `math.CV`, `math.NT`)
- **Evidence for ranking:** The paper gives an exact arithmetic criterion for a global topological property, addresses earlier conjectures and numerical observations, and includes a computational companion archived at Zenodo.
- **Claimed result:** The author proves C_h is connected iff h=q(q−1); at every other height it has at least five components, with further theorems showing infinitely many components for broad ranges of nonpronic heights.
- **Assumptions and setting:** C_h is formed from the nonreal roots of integer polynomials with coefficient modulus at most h; the connectivity statement changes if nonzero real roots are included.
- **Caveat:** Several explicitly listed small nonpronic heights are exceptions to the paper's general claim of infinitely many components, so component-count refinements depend on the particular height.
- **Announcement type:** new submission, announcement batch 11 November 2026
- **Themes:** Algebra & number theory; Geometry & topology

### 7. [Positivity in symplectic groups and electrical networks](https://arxiv.org/abs/2611.15043)
- **Abstract:** The authors show that electrical positivity for circular planar networks and total positivity of associated symplectic matrices do not coincide, while deriving rational factorization-recovery formulas with uniqueness under nonvanishing conditions.
- **Authors:** V. Gorbounov, A. Kazakov
- **arXiv:** `2611.15043v1` (published 2026-11-11 05:09:49 UTC; categories: `math.CO`, `math.GR`, `math.SG`)
- **Evidence for ranking:** The paper identifies a precise mismatch between two positivity notions and supplies constructive recovery formulas, bridging graph/network combinatorics, group theory, and symplectic geometry.
- **Claimed result:** The authors prove that the two specified notions of positivity do not coincide and give explicit rational formulas recovering factorization parameters from matrix entries and minors, with uniqueness under stated nonvanishing conditions.
- **Assumptions and setting:** The setting is symplectic matrices arising from circular planar electrical networks and the associated positive Lagrangian Grassmannian construction.
- **Caveat:** The uniqueness statement is conditional on explicit nonvanishing requirements; the abstract does not claim a general factorization-recovery result outside those conditions.
- **Announcement type:** new submission, announcement batch 11 November 2026
- **Themes:** Geometry & topology; Combinatorics & discrete mathematics

## Trending Research Themes

- **Counterexamples and structural limits:** Three papers establish sharp boundaries rather than universal positive results: unbounded cohomology refutes a uniform bound (#1), the Fock-bundle paper breaks a universal existence/uniqueness conjecture (#2), and the MIQP paper identifies assumptions essential to polynomial-time solvability (#5).
- **Finite, explicit classification and obstruction:** The hyperelliptic-curve paper classifies a family over finite fields (#4), the three-torus paper excludes a specific minimal-size case (#3), and the bounded-height-root paper gives an exact arithmetic criterion for connectedness (#6). These are parallel styles of resolution, not evidence of a field-wide shift.
- **Algebraic structure meets geometry:** Group and representation-theoretic constructions (#1), cyclic Higgs bundles (#2), finite-field curves (#4), and symplectic positivity from networks (#7) make algebraic structure do geometric work; the methods and objects remain distinct across these papers.
- **Combinatorial certificates as mathematical leverage:** A small-complex fundamental-group classification helps exclude a triangulation (#3), while network factorization and block decomposition turn structural information into explicit statements (#5, #7). This is a limited cross-paper connection, not a shared single technique.

## Open Problems and Research Directions

- **Author-stated open question:** Does a cohomology bound survive when the characteristic is fixed, with constants allowed to depend on that characteristic? This is the fixed-characteristic question posed by Bowman et al. (#1). **Research direction (synthesis):** test whether their Kazhdan–Lusztig construction can be replaced or adapted using the more difficult p-canonical data they identify as relevant.
- **Author-stated gap:** The minimum number of vertices for a triangulation of T³ remains either 14 or 15 (#3). **Research direction (synthesis):** search systematically for a 14-vertex complex satisfying manifold and homology constraints, or derive an obstruction that closes the remaining gap.
- **Author-stated unresolved status:** The Fock-bundle counterexample disproves the main flatness conjecture in ranks n ≥ 3 but leaves open which branch of its existence/uniqueness failure is realized in particular examples (#2). **Research direction (synthesis):** make the positivity-wall alternatives constructive and determine whether higher-complex-structure correspondences can hold by a route not requiring the disproved conjecture.
- **Research direction (synthesis):** The hyperelliptic classification assumes p ∤ 2d (#4); analyze the excluded characteristics separately, where the curve or its reduction may be singular.
- **Author-stated complexity boundary:** Del Pia's polynomial-time theorem requires fixed linking dimension and block size, and notes parameterized-hardness constraints (#5). **Research direction (synthesis):** identify natural restricted subclasses with limited block interaction or integer variables inside blocks, and determine whether tractability survives there.
- **Research direction (synthesis):** The root-locus paper singles out exceptional nonpronic heights (#6); investigate whether the stated upper bound on heights with only finitely many components is sharp and classify the remaining exceptions.
- **Research direction (synthesis):** For the network/symplectic factorization formulas, study what fails when the nonvanishing hypotheses degenerate and characterize the overlap between the two positivity notions (#7).

## Takeaway

This is a theorem-oriented slice of the week's mathematics: several preprints turn open conjectures or unresolved boundary cases into explicit counterexamples, classifications, or complexity limits. These are author-reported preprint results, and they still warrant expert review.

## Method and sources

- **Window:** 2026-11-07 through 2026-11-13 UTC, inclusive (the last seven calendar dates, with the current-day window observed only through the snapshot).
- **Snapshot:** 2026-11-13 02:24:31 UTC. The live arXiv mathematics listing showed announcement batches through Wednesday 11 November 2026; no later batch was present at snapshot time.
- **Coverage:** arXiv Mathematics (`math.*`) and mathematically central cross-lists; 1,167 first-submission records returned for the window by the arXiv API, sorted by submission date. Candidate metadata and abstracts were checked against the arXiv pages for all seven selected entries. All selected entries are new submissions; no revisions are ranked here.
- **Inference:** Selection and ordering use explicitly stated author results, category cross-listing, direct relevance to named conjectures or open boundary cases, and the extra full-text checks for the top three. Independent expert/seminar discussion was not corroborated in the searches performed; Semantic Scholar returned no indexed records for these newly posted preprints at snapshot time.
- **Revision coverage:** The arXiv API query returned 1,167 records based on first-submission dates. A separate prior-submission revision query did not yield a reliable candidate set, so this report ranks only new submissions and does not claim comprehensive revision coverage.
- **Full-text checks:** The introductions and main-result statements were inspected for papers #1–#3. The report attributes all mathematical claims to the preprint authors; no proof has been independently verified.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent), [arXiv API](https://export.arxiv.org/api/query), and the seven linked arXiv abstract pages above. For #1–#3, the arXiv HTML full texts were also inspected.
