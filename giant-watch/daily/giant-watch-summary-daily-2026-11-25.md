# Giant Watch Summary - Daily - 2026-11-25

## Headline

OpenAI's GPT-6.2 rollout into ChatGPT's main chat tab leads a day defined by frontier labs pushing agentic and coding capability into everyday products. The episode's throughline is the shift from model launches to deployment: labs are shipping variants, quotas, and tooling rather than single flagship announcements.

## Top Developments

### 1. OpenAI expands GPT-6.2 into ChatGPT's general chat tab (OpenAI)
OpenAI said in release notes that GPT-6.2, optimized for ChatGPT's Chat Tab, will roll out sequentially across subscription tiers, starting in professional environments before general users. The version is based on GPT-6.2 Sol, unveiled on the 17th, and follows GPT-6.2 Astra for ChatGPT Work and Codex. OpenAI reported gains in image understanding (71.7% vs 47.4%), complex instruction execution (78.1% vs 62.5%), expert-task internal evaluations (65% vs 52%), and BrowseComp at the Extra High setting (64.5% vs 54.4%), plus safety-policy adherence rising to 91-94% from 77-80%.
Why it matters: The largest consumer-facing deployment in the day's signals, and the clearest example of a lab pushing agent and coding capability into the default chat surface rather than a separate product tier.
Refs: https://en.etnews.com/20261125200003

### 2. Google DeepMind and Google Quantum AI use Gemini 4 agents with Lean proofs to optimize quantum circuits (Google)
Google DeepMind and Google Quantum AI published research showing teams of Gemini 4 agents paired with the Lean theorem prover can synthesize mathematically verified speedups for quantum algorithms. Reported results include an 11.8x reduction in combined computational cost for an inertial confinement fusion calculation (5,650 to 4,338 error-corrected qubits), 2.5x on cytochrome P450 (481 to 333 qubits), roughly 8x on a photochemistry simulation, 2.57x on a Grover's search implementation, and about 290x on an arcsine state-loading routine. The team released a Lean quantum-algorithm library, problem specifications, and verified circuits on GitHub, and noted full scientific simulations still exceed first-generation error-corrected hardware.
Why it matters: A concrete demonstration of agents producing formally verified scientific results, with open-sourced artifacts other researchers can inspect — a stronger claim than benchmark scores alone.
Refs: https://www.toolai.io/zh/info/google-deepmind-uses-gemini-4-agents-and-lean-proofs-to-optimize-quantum-circuits, https://www.toolai.io/zh/info/google-deepmind-%e7%94%a8-gemini-4-%e6%99%ba%e8%83%bd%e4%bd%93%e7%bb%93%e5%90%88-lean-%e5%bd%a2%e5%bc%8f%e5%8c%96%e8%af%81%e6%98%8e%e4%bc%98%e5%8c%96%e9%87%8f%e5%ad%90%e7%ae%97%e6%b3%95, https://sealion-lavender-ar2n.squarespace.com/news/google-deepminds-gemini-agents-cut-estimated-quantum-simulation-costs-by-up-to-118

### 3. Moonshot AI posts Kimi K3.1 Pro open-weight multimodal model on Hugging Face (Kimi)
Moonshot AI released Kimi K3.1 Pro, the first model in the K3.1 series and its largest to date, as an open-weight multimodal model on Hugging Face. It uses a MoE architecture with 2.8 trillion total parameters and 104 billion activated per token, 93 layers, 896 experts with 16 selected per token, a context length of 1,048,576 tokens, and a MoonViT-V2 vision encoder. It is post-trained from Kimi K3 with large-scale joint reinforcement learning across hundreds of downstream domains. Reported scores include Terminal-Bench 4.0 at 65.7, SWE Marathon v1.1 at 51.7, BrowseComp at 92.1, MMMU-Pro with python at 90.0, and GPQA-Diamond at 94.2, while Program Bench at 31.5 and HLE-Diamond at 39.4 trail leading closed models.
Why it matters: Pushes open-weight parameter scale and context length to a new level while using sparse attention to contain long-context inference cost — a direct competitive statement against closed frontier models.
Refs: https://www.readaitime.com/news/2026-11-25/2ncs03rj

### 4. Zhipu AI reportedly releases GLM-5.4 with a Loop Transformer architecture (GLM)
IT Home and Zhidongxi reported that Zhipu AI released GLM-5.4, described as its first flagship using a Loop Transformer architecture, with visual capabilities added and company-claimed speeds of up to 200 tokens per second off-peak and 70-80 at peak. Access was reported through ZCode, Trae, WorkBuddy, Qoder, CatPaw and OpenCode, with GLM Coding Plan V2, V3 and team users getting 1.5x previous quotas. A company evaluation over 200 coding scenarios reportedly showed stronger performance than GLM-5.3, Kimi K3.1 Pro and DeepSeek-V4.1-Flash-1017 on visual coding, visual replication and long-running tasks; weights were reported as planned for release after safety hardening.
Why it matters: A new architecture direction from a major Chinese lab, but the sourcing is single-outlet reporting without company confirmation or independent evaluation, so it carries less evidentiary weight than the day's other releases.
Refs: http://aigc.news/events/it-1124-ceo-39-3399-700-glm-5-4-2026-11-23-a8defa44/, https://www.orcarouter.ai/zh-TW/blog/solar-pro-4-vs-glm-5-5

### 5. Meta announces $700,000 AMET AI Impact Grant and regional AI Impact Hub (Meta)
At the opening of its two-day Africa, Middle East and Türkiye AI and Wearables Summit in Istanbul, Meta announced a $700,000 AMET AI Impact Grant for startups and developers in Nigeria, Egypt, Kenya, Saudi Arabia, South Africa, Türkiye and the UAE, scheduled to launch in 2027. Meta also launched the AMET AI Impact Hub, with AI Academy, AI Literacy and AI for Small and Medium-sized Businesses tracks aimed at reaching more than five million students, developers and entrepreneurs within three years, and introduced the AMET AI Awards 2026 with more than $100,000 across seven categories. Application timelines, individual grant sizes and distribution across markets were not disclosed.
Why it matters: A regional ecosystem play built around Llama adoption rather than a model release, notable for its scale targets and for the absence of concrete application details.
Refs: https://thebusinesstimesng.com/meta-700000-ai-grant-nigeria-startups-developers/, https://www.naijaonpoint.com/meta-announces-%e2%82%a61-billion-ai-grant-opportunity-for-nigerian-startups-and-developers/, https://aibase.ng/ai-news/meta-announces-700000-ai-grant-for-nigeria-and-six-other-countries/

### 6. DeepSeek tightens free-tier limits, capping inactive long conversations and daily quotas (DeepSeek)
A Sina Finance feature reports that since November 15, DeepSeek has shown users a notice that long conversations inactive for more than seven days are no longer supported due to insufficient compute, alongside a single-input cap of roughly 40,000 characters and a daily conversation quota that ends with a server-busy message. The article frames this within a broader 2026 pattern of AI products keeping a free tier while moving high-compute features behind payment, citing Kimi's tier restructuring, Doubao's paid professional tiers, and overseas limits at ChatGPT, Claude and Gemini.
Why it matters: A concrete data point on the economics of free AI access, though the specific limits are reported by a third-party feature rather than DeepSeek's own announcement.
Refs: https://finance.sina.com.cn/jjxw/2026-11-25/doc-inizxaum9659660.shtml

## Cross-Org Themes

- Frontier labs are shipping model variants and tiered rollouts rather than single flagship launches
- Agentic and coding capability is the primary competitive axis across OpenAI, Google DeepMind, Kimi and GLM
- Open-weight releases from Chinese labs are pushing parameter scale and context length against closed frontier models

## Rumors and Unverified Claims

Google DeepMind released Gemini 4 Hydrogen, a model that builds an interactive 3D Earth and converts real-time lightning data into ambient music (Techub News flash, single source). Zhipu AI's GLM-5.5 is described in a JPMorgan research report cited by Chinese and Korean tech media as a roughly 3-trillion-parameter flagship expected around December 2026, with a smaller GLM-5.5 Flash possibly earlier; no model card, pricing, API identifier or weights repository exists as of November 25, and leaked parameter figures have ranged from 1T to 3.5T.

## Takeaway

The day's evidence points to deployment and verification as the real battleground: open artifacts and formal proofs are becoming differentiators, not just benchmark scores. The next checks worth watching are independent evaluations of Kimi K3.1 Pro and GLM-5.4, and whether DeepSeek confirms its free-tier limits directly.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
