# Giant Watch Summary - Daily - 2026-10-24

## Headline

Kimi K3.1 Pro's launch puts a 3T-class open-weight model within a point of Claude Opus 5.5 on Terminal-Bench 4.0, while Meta's Muse monetization plan signals agents moving toward transaction revenue. The day's episode is open-weight labs closing the agentic-coding gap while platform owners experiment with non-advertising business models.

## Top Developments

### 1. Moonshot releases Kimi K3.1 Pro, a 3T-class open-weight model with 1M-token context (Kimi)
Moonshot AI launched Kimi K3.1 Pro, described as its most capable 3T-class open-weight model with a 1-million-token context window, alongside a Highspeed variant claimed at 2-3x output speed. It is available on Kimi.ai, Kimi App, Kimi Work, Kimi Code and the Kimi API, with full weights promised by Nov 4. Moonshot reports Terminal-Bench 4.0 at 65.7% versus GPT-6 Astra at 58.2% and Claude Opus 5.5 at 66.4%, and Kimi Code Bench 3.0 Long-horizon at 61.2% versus K3's 55.95%. The company also cites OfficeQA Pro v2 at 64.4 and a drop in claim-level hallucination rate on its internal Kimi Hallu Bench Hard from 23.4% to 8.3%.
Why it matters: The strongest single release in the window: an open-weight model positioned at near-parity with leading proprietary coding agents, with weights pending rather than shipped.
Refs: https://www.kimi.ai/blog/kimi-k3-1-pro?utm_source=diginews_johandenoyer&utm_medium=referral&utm_campaign=diginews_referral, https://tech.ifeng.com/c/8xTWmzaVbfg, https://www.sohu.com/a/1091986421_114960?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smpc.channel_248.block3_308_NDdFbm_1_fd.1.1792801193544AAUThF6, https://inews.hket.com/article/4213932, https://app.qudong.com/article/527221.html

### 2. Meta outlines Muse monetization: no ads, paid enterprise tiers, agent shopping commissions (Meta)
Meta chief AI officer Alexandr Wang told Nikkei that the personal AI agent Muse will stay ad-free and free for ordinary users, with paid tiers for heavy users and enterprise services, plus planned commissions on shopping transactions completed through the agent. Muse debuted in Japan on Oct 23; the report says it launched in North America on Sept 8 and reached 10 million app downloads in six weeks. Wang cited Meta's own infrastructure, safety systems and data centers as a differentiator. The same coverage notes Meta's 2026 capex guidance of $135-145 billion and roughly $810 billion in lease and irrevocable contract commitments as of end-September.
Why it matters: A concrete signal that a major platform is testing transaction and enterprise revenue for agents rather than advertising, with pricing and commission terms still undisclosed.
Refs: https://awtmt.com/articles/3784364, https://fund.eastmoney.com/a/202610243906836171.html

### 3. DeepSeek open-sources inference framework DeepInfer plus Search/Fetch and recipe components (DeepSeek)
DeepSeek open-sourced DeepInfer, the inference framework it uses in production, under Apache 2.0 with support for Nvidia and domestic compute platforms, and released Search and Fetch JSON interfaces plus a deepseek-recipe component for prompt/format translation. Search and Fetch are free until Nov 1, 2026, then priced at 5 yuan per 1,000 successful requests, and are callable from DeepSeek Harness, Claude Code and Codex. DeepSeek also published deployment economics, including 155 trillion tokens per day of throughput per cluster and average revenue of $38 per GPU-hour at off-peak pricing. 360 founder Zhou Hongyi framed the release as a 'sovereign AI' signal and said 360 has deployed its own sovereign AI operating system with some government and enterprise customers.
Why it matters: Publishes both the serving stack and unit economics that proprietary labs typically keep private, and pushes DeepSeek's interfaces into third-party agent harnesses.
Refs: https://www.163.com/dy/article/L9VJHF2F0519E3QB.html?referFrom=, http://news.cyol.com/gb/keji/articles/2026-10/24/content_3nXnaVuwy3.html

### 4. Meta and Carnegie Mellon study finds RL-trained 8B model beats Llama-4-Maverick at tool selection (Meta, Qwen)
A Meta and Carnegie Mellon study reports that an 8B model trained with reinforcement learning to decompose requests and pick tools from a catalog of over 10,000 options reached 41.5% accuracy in tool selection, versus 30.6% best performance for the 402B Llama-4-Maverick. The paper fine-tunes Qwen3 variants with supervised learning followed by RL on a plan-retrieve-select workflow and reports generalization across tool benchmarks without further training.
Why it matters: A direct small-versus-large comparison on agent tool selection, with Meta's own flagship used as the underperforming baseline.
Refs: https://emeraldforce.com/meta-carnegie-mellon-study-shows-rl-trained-models-outperform-llama-4-maverick-in-tool-selection/

### 5. Qwen3.6-27B dense model resurfaces after being listed on an LLM aggregation gateway (Qwen)
A report says Alibaba's Qwen team open-sourced Qwen3.6-27B, a 27B dense multimodal model, on April 22, 2026 under Apache 2.0, and that it was added to the LLM Gateway aggregation platform on Oct 21. The report claims it beats the prior Qwen3.5-397B-A17B mixture-of-experts flagship on coding benchmarks, including SWE-bench Verified 77.2 versus 76.2 and Terminal-Bench 2.0 59.3 versus 52.5, and that quantized versions fit on a single 24GB consumer GPU. Community quantizations are said to exceed 78 variants across llama.cpp, LM Studio, Jan and Ollama.
Why it matters: The in-window hook is the Oct 21 gateway listing; the underlying release dates to April, so this is a distribution and tooling story rather than a new model launch.
Refs: https://doitnews.cn/a/qwen3-6-27b-release/

### 6. OpenAI ChatGPT Edu product page surfaces in the window (OpenAI)
A ChatGPT Edu page describes an education offering for universities with higher message limits than free ChatGPT, GPT-5 as the flagship model, SAML SSO and domain verification, custom data retention, SOC 2 Type 2 and ISO 27001/27017/27018/27701 certifications, SCIM and admin controls, and a commitment not to train on customer data or conversations. The page carries a window-dated timestamp but reads as standing product documentation; the fetch of the page returned a 404.
Why it matters: Included only because it is the sole OpenAI signal in the window; it documents an existing education offering rather than a new event.
Refs: https://chatgpt.com/zh-Hans-CN/business/education/?openaicom_referred=true

## Cross-Org Themes

- Agentic tool use and coding benchmarks are the shared competitive yardstick across Kimi, Meta, Qwen and DeepSeek
- Open-weight releases paired with serving or interface tooling (DeepInfer, recipe, quantizations, gateways) as a distribution strategy
- Monetization experiments around agents: enterprise tiers and transaction commissions versus API and per-request pricing

## Rumors and Unverified Claims

The Qwen3.6-27B item is a single secondary report whose in-window hook is an Oct 21 gateway listing; its benchmark figures and April release date are not corroborated by other supplied sources. The ChatGPT Edu page is undated product documentation with a window timestamp and failed to fetch (404). A Meta Llama 3 item from a low-credibility repost site describes an older release and was not selected.

## Takeaway

Watch whether Kimi actually ships the promised full weights by Nov 4 and whether Meta discloses Muse pricing or commission terms; both would convert announcements into verifiable commitments. The Qwen and OpenAI items need primary-source confirmation before being treated as events.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
