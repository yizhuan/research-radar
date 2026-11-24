# Giant Watch Summary - Daily - 2026-11-24

## Headline

OpenAI pushed GPT-6.2 Sol into ChatGPT's main chat tab and set GPT-5.6 Sol and Terra for December 23 retirement, while Google answered with Gemini 4 Neon's launch. The day's episode is a frontier-model refresh race in which vendors compete on cost-per-task and agentic reliability rather than raw parameter counts.

## Top Developments

### 1. OpenAI rolls out GPT-6.2 Sol to ChatGPT chat tab and schedules GPT-5.6 Sol/Terra retirement (OpenAI)
OpenAI began rolling out a version of GPT-6.2 Sol in the ChatGPT chat tab on November 23, optimized for everyday conversation and available to Plus, Pro, Business and Enterprise users. The company said the model handles complex requests and web search better, reads finer image details, and offers more relevant follow-ups. OpenAI also said GPT-5.6 Sol will be retired from Chat, Work and Codex on December 23, with GPT-5.6 Terra leaving Work and Codex the same day, as part of a practice of retiring models two generations back to free compute.
Why it matters: The flagship consumer surface gets a new default model while two prior-generation models are put on a dated retirement clock, compressing the model lifecycle and shifting compute toward newer models.
Refs: https://m.ithome.com/html/1031271.htm, https://news.qq.com/rain/a/20261124A03QEY00, https://www.chinaz.com/2026/1124/1790167.shtml, https://www.chinaz.com/ainews/32482.shtml, https://dataist.ai/news/openai-updates-chatgpt-for-complex-questions-web-search-and-images/

### 2. Google launches Gemini 4 Neon across AI Studio, Gemini Enterprise and Antigravity (Google)
Google DeepMind introduced Gemini 4 Neon, positioned for complex software engineering, knowledge work and scientific research workflows, with a 1M-token context window and pricing of $3 per million input tokens ($0.15 cached) and $15 per million output tokens. Google said Neon scored 61 on the Artificial Analysis intelligence index in xhigh thinking mode, ranked second on the Vals Index and second on a new Agent Arena index, and reported leading results on several benchmarks including Legal Research Bench, Tax Agent Bench and Terminal-Bench Science. It is available via the Gemini API in AI Studio, Gemini Enterprise, and for AI Pro/Ultra subscribers in Antigravity and the Gemini app; a cyber-focused variant is to reach trusted defenders through the Fairwind program.
Why it matters: A new mid-tier frontier model explicitly framed around cost-per-task and agentic controllability, with published head-to-head comparisons against Claude Opus 5.5 and GPT-6.2 Sol.
Refs: https://m.elecfans.com/article/8969546.html

### 3. DeepMind reports Gemini 4 agent teams cutting quantum circuit costs, verified in Lean (Google)
Google DeepMind and Google Quantum AI published results in which teams of Gemini 4 agents proposed cheaper quantum circuits, with each result checked in the Lean theorem prover against frozen specifications. Reported improvements include an arcsin state-preparation routine cut by more than 290x in estimated space-time cost, an 11.8x reduction for a fusion fuel simulation (qubits falling from 5,650 to 4,338), about 8x for photochemistry and 2.5x for a cytochrome P450 enzyme simulation. DeepMind open-sourced its Lean library, problem specs and verified solutions; the work is resource estimation only and no circuit ran on hardware.
Why it matters: A concrete demonstration of the 'human writes spec, agents search, proof checker gates' pattern applied to a domain where circuits cannot be simulated, with open formal artifacts others can inspect.
Refs: https://aiweekly.co/alerts/deepminds-gemini-4-agents-cut-quantum-arithmetic-subroutines-290x-with-lean, https://juejin.cn/post/7711261382734774287, https://www.parasmadan.in/blog/deepmind-gemini-4-quantum-lean-proof-vs-speedup, https://aidr.today/74d51a78?lang=en

### 4. Z.ai releases GLM-5.4, its first looped-transformer flagship, with vision and 1M context (GLM)
Z.ai (Zhipu AI) released GLM-5.4, which runs 28 layers of the GLM-5 base twice per token at roughly 750B scale, adds vision input (video, image, text, file), keeps a 1M-token context with 128K output, and targets what Z.ai calls Generalized Coding. Z.ai claims performance comparable to 2T-3T parameter models but published no benchmark table, only an internal win-rate chart (51.1% wins vs GLM-5.3) and a 30B ablation; it also flags a tendency toward overly long 'marathon thinking'. Access is limited to Z.ai Chat, ZCode and partner coding tools, with API access pending a security assessment and open weights planned without a date. Z.ai hinted its next model would be significantly larger and ready soon.
Why it matters: The first disclosed looped-transformer flagship from a Chinese lab, an efficiency-over-parameters bet whose headline claims remain unverified by public benchmarks.
Refs: https://www.scmp.com/tech/big-tech/article/3375517/chinas-zai-aggressively-using-looped-transformer-method-improve-ai-models?module=top_story&pgtype=section, https://venturebeat.com/technology/z-ais-glm-5-4-aims-to-match-models-up-to-four-times-its-size-by-running-28-layers-twice, https://glm5.app/blog/what-is-glm-5-4, https://simonwillison.net/2026/Nov/23/glm-54/, https://glm5.app/blog/glm-5-4-vs-glm-5-3

### 5. Virginia and Oregon sue Musk companies over Grok-generated sexualized imagery (xAI)
Democratic attorneys general in Virginia and Oregon filed separate lawsuits on Monday under state consumer protection statutes, naming SpaceX, X and SpaceX Super Intelligence (formerly xAI) and alleging the companies stripped out safeguards and marketed Grok's 'spicy mode', leading to proliferation of child sexual abuse material and nonconsensual intimate imagery. Virginia seeks $2,500 per willful violation and both seek injunctions and disgorgement. SpaceXSI said sexual content involving minors is abhorrent, that it acts against users who break safeguards, and that it has sued abusers; the filings cite CCDH estimates of roughly 3 million sexualized images posted to X in a ten-day window, about 23,000 depicting children.
Why it matters: State-level consumer-protection litigation turns AI content-safety failures into direct legal exposure for a frontier lab and its parent platform, with a template other states could follow.
Refs: https://www.scmp.com/news/world/united-states-canada/article/3375532/us-states-sue-musk-companies-over-flood-sexualised-images-made-ai-chatbot-grok, https://www.manilatimes.net/2026/11/24/world/americas-emea/states-sue-musk-companies-over-flood-of-sexualized-images-made-with-ai-chatbot-grok/2476692, https://www.wtnh.com/news/national/oregon-and-virginia-sue-spacex-claiming-xs-ai-creates-sexualized-photos-of-children/, https://katu.com/news/local/oregon-sues-musk-companies-over-flood-of-sexualized-images-made-with-ai-chatbot-grok?teaserSource=databricks

### 6. Alibaba developer posts detail Qwen4-Max preview capabilities, pricing and November 25 preview cutoff (Qwen)
Alibaba Cloud developer articles published November 24 describe the Qwen4-Max preview (qwen4-max-preview), a 2.4T-parameter MoE flagship with about 71B activated parameters, native vision, a 1M-token context and a Live Delivery progressive-delivery mechanism. The posts report Terminal-Bench 4.0 at 48.5 with per-attempt token use falling from 289K to 151K and average per-task cost down about 58%, and state the preview is subscription-only via Token Plan, with the preview model ID going offline at the end of November 25 (UTC+8) and a formal version to follow under a new name. The articles note official parameter scale, full benchmarks and open-source plans had not been disclosed.
Why it matters: Signals Alibaba's flagship positioning around long-horizon agentic tasks and cost reduction, but the material is vendor-authored explainer content rather than a dated launch announcement.
Refs: https://developer.aliyun.com/article/1788038, https://developer.aliyun.com/article/1788196, https://developer.aliyun.com/article/1788200

## Cross-Org Themes

- Frontier vendors are competing on cost-per-task and agentic reliability rather than parameter counts, as seen in Gemini 4 Neon's pricing and efficiency framing, Qwen4-Max's token and cost reductions, and GLM-5.4's looped-depth efficiency claim.
- Model lifecycles are compressing: OpenAI set a dated retirement for two prior generations while Z.ai restricted a new flagship to first-party surfaces pending safety hardening and API access.

## Rumors and Unverified Claims

Z.ai's claim that GLM-5.4 matches 2T-3T parameter models rests on an internal win-rate chart and a 30B ablation, with no public benchmark table, API price or open weights. A JPMorgan note cited by SCMP, reportedly based on a Z.ai internal road map, points to a 3-trillion-parameter release by year-end. Alibaba's Qwen4-Max figures (2.4T parameters, 71B activation, benchmark scores, ~58% cost reduction) come from vendor-authored developer articles that state official specs and benchmarks were not fully disclosed. Kimi K3.1 Pro benchmark comparisons and hands-on impressions come from a single outlet's real-world testing rather than a new dated release.

## Takeaway

The competitive axis has moved to delivered cost and agentic reliability, so the next evidence to watch is independent benchmarking of GLM-5.4 and Qwen4-Max and whether OpenAI's December 23 retirement proceeds on schedule. The Grok litigation will also test whether state consumer-protection statutes become a durable channel for AI safety enforcement.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
