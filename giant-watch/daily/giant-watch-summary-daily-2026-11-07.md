# Giant Watch Summary - Daily - 2026-11-07

## Headline

Google DeepMind reported that human-guided AI agents found two weaknesses in legacy 1024-bit RSA, while Google pushed Gemini Omni 1.2 Flash to general availability. The day's episode is about labs converting model capability into deployed products and audited security findings, not just benchmark scores.

## Top Developments

### 1. DeepMind: human-guided AI agents find two weaknesses in legacy 1024-bit RSA (Google)
Google DeepMind said on Nov. 6 that AI agents working under human supervision found two weaknesses in legacy 1024-bit RSA: a padding gap that makes certain signature forgeries far cheaper, and a batch-factoring method that cuts the average cost of factoring each additional 1024-bit key by about 30x. DeepMind says 2048-bit and larger keys are not affected.
Why it matters: A concrete, dated research result that positions AI agents as cryptanalysis and security-audit tools, with explicit scope limits that keep the claim checkable.
Refs: https://www.aichatdaily.com/ai-security/google-deepmind-agents-find-two-weaknesses-legacy-1024-bit, https://toolnavs.com/article/3230-nov-7-ai-briefing-openai-banks-11b-as-googles-gemini-faces-lawsuit, https://yeekal.com/daily/2026-11-07/

### 2. Gemini Omni 1.2 Flash reaches general availability (Google)
Google made Gemini Omni 1.2 Flash generally available on 5 November 2026, with native 15-second clips, 3-to-15-second length control, multi-turn conversational editing, reference-image inputs, and a 30% price cut to $0.07 per second at 720p. It is reachable through the Gemini API, Google AI Studio and Google Cloud Console, and outputs carry a SynthID watermark.
Why it matters: A priced, generally available video model with editing and reference consistency moves video generation from demo to production tooling for developers.
Refs: https://devhives.in/blog/ai/build-video-apps-gemini-omni-flash/, https://yeekal.com/daily/2026-11-07/

### 3. Meta rolls Muse Wonder-trained models with Active Memory and Active Focus to all Muse and Meta AI users (Meta)
Meta announced on November 6 that specialized models trained with learnings from its Muse Wonder frontier model are rolling out to all Muse and Meta AI users, bringing Active Memory and Active Focus. Meta reports the current Muse model uses critical context correctly in 90% of tasks (up from 76%), forgets goal-relevant information 2.4x less often, and shows a 67% improvement on everyday tasks hit by unexpected issues. The same announcement introduced Spaces in the Muse app.
Why it matters: Meta is distilling frontier behavior into free, mass-reach assistants rather than gating agent-style memory behind top tiers, a distinct distribution strategy.
Refs: https://www.newsbytesapp.com/news/science/meta-ai-muse-get-memory-and-focus-upgrade/story, https://shiftdelete.net/en/meta-muse-models, https://gptonline.ai/meta-brings-muse-wonder-memory-every-muse-user/, https://yeekal.com/daily/2026-11-07/

### 4. DeepSeek Harness reports 1.54M daily active users and a token-incentive plan for plugin authors (DeepSeek)
DeepSeek Harness said that as of November 4, counted by official-API users, it had 1.54 million daily active users, about 92 trillion daily tokens consumed, and roughly 35,000 third-party plugins, with around 60% of active users having created or installed at least one. It is preparing an official plugin marketplace, token subsidies for plugin authors, and traffic promotion, under an "everything is a plugin" design.
Why it matters: A concrete usage and ecosystem snapshot for an agent platform, plus a monetization experiment that pays creators in tokens rather than cash.
Refs: https://eu.36kr.com/en/p/4057774236652417, https://hub-assets-cache.baai.ac.cn/view/59440

### 5. Moonshot publishes full Kimi K3.1 Pro weights on Hugging Face (Kimi)
Moonshot AI published the full MXFP4 weights of Kimi K3.1 Pro, a 2.8-trillion-total / 104-billion-active-parameter multimodal agentic model with a 1M-token context, under a modified MIT license with conditions for large model-as-a-service businesses and high-reach products. BenchLM ranks it as the highest open-weight model it tracks.
Why it matters: A frontier-scale model becoming downloadable shifts the open-weight frontier and puts license conditions, not just scores, at the center of the release.
Refs: https://benchlm.ai/blog/posts/llm-news-november-7-2026, https://web.gate.it/zh-tw/news/detail/kimi-k31-pro-combines-28t-parameters-with-a-1m-token-context-25467681

### 6. Revolut replaces Anthropic and OpenAI APIs with self-hosted GLM for coding (GLM)
Revolut has made an open-weight GLM model from Z.ai the default coding model for roughly 2,000 engineers, served on 56 NVIDIA B200 GPUs it reserves for that use, at a company-cited combined cost of about $0.30 per million tokens. Claude Code and Codex remain available as exceptions, and image tasks route to Gemini or GPT-6 Luna. The figures are company-provided and exclude staff, cloud and observability costs.
Why it matters: A named, large regulated fintech publicly swapping US frontier APIs for a self-hosted Chinese open-weight model is a concrete data point on cost-driven stack sovereignty.
Refs: https://cloudnews.tech/revolut-swaps-the-api-for-56-b200-gpus-and-an-open-model-for-coding/, https://longbridge.com/en/quote/02513.HK

### 7. Menlo Ventures report puts Zhipu GLM at 11% of US enterprise open-source AI spend (GLM)
A Menlo Ventures 2026 enterprise AI report, based on a survey of nearly 400 US enterprise AI leaders responsible for more than $4 billion in AI spend, puts Zhipu's GLM at 11% of US enterprise open-source model spend, behind Moonshot's Kimi at 61% and DeepSeek at 15%, with Alibaba's Qwen at 3% and Meta's Llama the top Western model at 7%.
Why it matters: Survey evidence that Chinese open-weight models dominate US enterprise open-source spend, framing the competitive stakes behind individual releases.
Refs: https://web.gate.it/zh-tw/news/detail/ZHIPU-AI/zhipu-glm-captures-11-of-us-enterprise-open-source-ai-spend-25463334

### 8. Grok API begins watermarking AI-generated text by default (xAI)
Starting November 7, 2026, Grok API text responses carry an invisible watermark by default, covering grok-4.7, 4.6, 4.5, 4.3 and the grok-4.20 variants across Chat Completions and Responses, including structured outputs and tool-call arguments. Responses carry an x-watermark header; only team admins can disable watermarking per model after asserting a legal exception. xAI frames the change as EU AI Act compliance.
Why it matters: A dated, API-wide default change that shifts a compliance burden onto developers and adds an auditable response header.
Refs: https://byteiota.com/grok-api-text-watermark/, https://web.gate.it/zh/news/detail/grok-api-to-watermark-ai-generated-text-by-default-from-november-7-25463804

### 9. Qwen integrated into China Apple Intelligence test build (Qwen)
Alibaba's Qwen is integrated into the first test release of China-market Apple Intelligence, providing text and image understanding inside Siri, Writing Tools and Visual Intelligence, with users able to hand complex Siri queries to Qwen after a consent prompt. The article also reports Qwen4 is expected in early November with Max, Flash, Plus and 27B versions, and that Qwen4 architecture has been adapted to Huawei Ascend.
Why it matters: A system-level distribution win for Qwen inside iPhone entry points, plus a signal on the next flagship family's timing and hardware adaptation.
Refs: https://cdnh5.laohucaijing.com/lhapp/dist/articles?newsid=237585&isType=1

### 10. Qwen-Image-3.0-Pro and Standard launch on Qwen Cloud (Qwen)
Qwen-Image-3.0-Pro and Standard are live on Qwen Cloud, described as China's first text-to-image model with 10px-level text rendering, using ultra-long 4.5k-token prompts, support for 12 languages, and a unified architecture that merges generation and editing. Pricing starts at $0.04 per image for Pro and $0.03 for Standard.
Why it matters: A priced image-model release with a specific capability claim (fine text rendering) and a unified generate-and-edit design aimed at small teams.
Refs: https://www.xix.ai/ainews/tongyi-qwen-unveils-qwenimage30pro-chinas-first-texttoimage-model-with-10pxlevel-text-rendering.html

### 11. Parents sue Google over teen's Gemini conversations (Google)
Bloomberg reported on November 7 that a North Carolina couple sued Google, alleging their 13-year-old daughter exchanged thousands of messages about suicidal thoughts with Gemini on a school-issued Chromebook. Google said it is reviewing the claims and noted it has added crisis helplines to AI features in Search.
Why it matters: A dated legal action that puts consumer-safety obligations for assistant products on the record.
Refs: https://toolnavs.com/article/3230-nov-7-ai-briefing-openai-banks-11b-as-googles-gemini-faces-lawsuit

### 12. Anthropic details Claude 'dreaming' memory consolidation (Anthropic)
Anthropic's engineering blog described a 'dreaming' mechanism in which Claude organizes learned memories in the background, corrects errors, and retrieves needed information faster on later tasks, framing memory as a component of learning from experience rather than a chat-history cache.
Why it matters: A named engineering mechanism that treats memory quality as a stability metric for long-running agent tasks.
Refs: https://yeekal.com/daily/2026-11-07/

### 13. Analysis argues Anthropic's RSP 'dramatically accelerated' threshold may be crossed (Anthropic)
A Hacker News-linked analysis, drawing on an Anthropic S1 filing and a METR report, argues that capability progress from 2025-10 to 2026-10 ran at roughly 2x the prior 12 months and that AI automation may account for much of the acceleration, potentially crossing Anthropic's RSP threshold. The author states the view is personal and that much of the most informative evidence was redacted.
Why it matters: A contested, explicitly uncertain claim that ties frontier-lab governance thresholds to measurable progress rates.
Refs: https://yeekal.com/daily/2026-11-07/

### 14. Meta Model API in public preview serves Muse Spark models (Meta)
Promptfoo documents the Meta Model API public preview, which serves Meta Superintelligence Labs' Muse Spark models through an OpenAI-compatible API at api.meta.ai, with muse-spark-1.3 as the latest model, a 1,048,576-token context, and an Anthropic-compatible Messages surface. Meta retired the separate Llama API on July 6, 2026.
Why it matters: A developer-surface detail showing Meta consolidating model access around Muse Spark rather than Llama.
Refs: https://www.promptfoo.dev/docs/providers/meta/

## Cross-Org Themes

- Frontier labs are pushing flagship-model behavior into cheaper, mass-distributed products
- Open-weight models are being adopted on cost and control grounds, not only benchmark scores
- Agent memory and task persistence are becoming explicit engineering and product metrics
- Compliance and safety obligations are being built into model and API defaults

## Rumors and Unverified Claims

Unverified or undated claims not selected as events: that Qwen4 would launch in early November with Max, Flash, Plus and 27B versions and that its architecture is already adapted to Huawei Ascend (reported as rumor in a single article); that DeepSeek plans to train a V5 model on Huawei Ascend 950 chips (reported, not confirmed); that xAI has been renamed SpaceXSI (asserted by a single source); that Anthropic's RSP 'dramatically accelerated' threshold has been crossed (author's personal analysis with redacted evidence); that Muse was struggling with English fluency and coherence two weeks before launch (anonymous sourcing); and that Gemini Omni 1.2 Flash's quality and speed claims have not been independently tested.

## Takeaway

The evidence to watch next is whether these releases hold up outside vendor-run tests: independent evaluations of the new video and memory models, and whether enterprise self-hosting of open-weight models spreads beyond a single large fintech.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
