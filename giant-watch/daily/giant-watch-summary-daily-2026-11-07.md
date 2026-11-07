# Giant Watch Summary - Daily - 2026-11-07

## Headline

Google DeepMind moved Gemini Omni 1.2 Flash to general availability at a 30% lower 720p price, while Anthropic disclosed a "dreaming" mechanism that reorganizes Claude's agent memory in the background. The day's throughline is vendors competing on cost-per-output and memory quality rather than raw capability alone.

## Top Developments

### 1. Google DeepMind takes Gemini Omni 1.2 Flash to GA with 30% cheaper 720p pricing (Google)
Google DeepMind released Gemini Omni 1.2 Flash to general availability as a faster, cheaper video generation and editing model for developers, enterprises and creators. It produces native 15-second video in 1-second increments from 3 to 15 seconds, supports multi-turn conversational editing, and can combine people, products, style images, motion clips up to 3 seconds and audio prompts while emphasizing consistency of characters, objects, scenes and first/last frames. Workflows can draft at 360p/720p, refine through edits, then upscale to 1080p/4K. 720p pricing is $0.07 per second, 30% below version 1.1, available via Gemini API and Gemini for business/Cloud with Provisioned Throughput, and outputs carry SynthID watermarks. Google says fast motion, rapid script changes and complex physics are still being improved, and demos are vendor-supplied with no independent evaluation.
Why it matters: A GA release with a double-digit price cut on the flagship video model sets a new cost benchmark for generative video and pressures rivals on per-second pricing.
Refs: https://yeekal.com/daily/2026-11-07/

### 2. Anthropic details Claude "dreaming" for background memory consolidation (Anthropic)
Anthropic's engineering blog described a "dreaming" mechanism in which Claude reorganizes memories it has already learned in the background, corrects errors, and retrieves needed information faster on later tasks. Anthropic frames memory as a key component of learning from experience rather than a mere cache of conversation history, and the post breaks down the components of agent memory.
Why it matters: Moves agent memory from an external retrieval add-on toward background consolidation and error correction, making memory quality an engineering metric for long-running task stability.
Refs: https://yeekal.com/daily/2026-11-07/

### 3. Meta ships Wonder-trained specialized models to Muse and Meta AI users (Meta)
Meta began giving users of its Muse agent and Meta AI new "specialized" models on Friday, November 6, which it says were trained using its frontier Muse Wonder model; the models are unnamed and reach a free consumer tier plus Meta AI inside WhatsApp, Instagram, Facebook and Messenger, while Wonder itself stays with paying subscribers for harder tasks. The models carry Active Memory, which Meta says lets them distinguish temporary from permanent and stale from relevant information, and Active Focus, aimed at keeping tasks on track when they break down. Meta reports critical context used correctly in 90% of tasks versus 76% for the previous model, and a 67% improvement in finishing routine tasks that hit unexpected problems, though it did not share that baseline. Meta has not detailed the training method.
Why it matters: Distilling a frontier model into free, high-distribution consumer surfaces is a cheaper path to scale than serving the frontier model directly, and it raises the bar for memory and task-persistence in assistants.
Refs: https://pivotnews.ai/five/meta-ships-wonder-trained-models-to-muse-and-meta-ai-users, https://yeekal.com/daily/2026-11-07/

### 4. DeepSeek Harness reports 1.54M daily active users and token grants to plugin developers (DeepSeek)
DeepSeek Harness announced on the evening of November 5 that, as of November 4 and counted by users of the official API, daily active users reached 1.54 million with roughly 92 trillion tokens consumed daily. Third-party plugins grew to about 35,000, and around 60% of active users have created or installed at least one. DeepSeek positions Harness as an operating system for the agent era under an "Everything is a Plugin" design, with professional and industry needs left to developers. The report also documents friction: users describe infinite loops, context overflow and sharply higher token consumption as plugin counts grow, and one Windows user lost 32 configured plugin entries upgrading from v0.2.1-rc.5 to v0.2.2-rc.1, with no automatic config backup or rollback and about five hours of manual repair.
Why it matters: A concrete scale datapoint for an open agent platform, paired with evidence that plugin sprawl and upgrade safety are becoming the binding constraints on agent usability.
Refs: https://eu.36kr.com/en/p/4057774236652417

### 5. Moonshot AI builds Kimi Hosted Agent on Tencent Cloud sandbox runtime (Kimi)
Moonshot AI deployed Kimi Hosted Agent on a Tencent Cloud sandbox, letting enterprises call a managed Harness runtime directly while writing their own Skills; the announcement came at the 2026 Tencent Global Digital Ecosystem Conference, where Tencent Cloud published an enterprise AI agent whitepaper covering more than 30 companies. Moonshot's enterprise lead said the period needed for a model's reliable working duration to double has shortened from seven months to four, while the Harness layer updates every three months, making it hard for enterprises to keep pace — hence the hosted approach.
Why it matters: Shows agent vendors shifting from shipping runtimes to operating them as managed services, with update cadence as the stated commercial rationale.
Refs: https://miniapp.gate.com/zh/news/detail/kimi-hosted-agent-runs-on-tencent-clouds-managed-sandbox-25463820, https://www.gatewebsite.com/zh-tw/news/detail/kimi-hosted-agent-runs-on-tencent-clouds-managed-sandbox-25463820

### 6. Grok API to watermark AI-generated text by default from November 7 (xAI)
Starting November 7, 2026, Grok models will embed an invisible watermark in text generated through the API by default, covering Grok 4.7, 4.6, 4.5, 4.3 and 4.20 in the SpaceXSI API; the source also states xAI is now named SpaceXSI. The watermark works by subtly steering word choice rather than adding visible marks, and the provider says text quality and generation speed are unaffected. Each response carries an x-watermark header, detection returns watermarked, unwatermarked or indeterminate with longer text giving clearer results, and detection is limited to approved applicants. Only team administrators can disable watermarking per model after confirming a legal exception, and the provider cites EU AI Act compliance as the rationale.
Why it matters: A default-on provenance control across an entire model family turns AI Act compliance into a product default that enterprise customers must audit before the effective date.
Refs: https://web.gate.it/zh/news/detail/grok-api-to-watermark-ai-generated-text-by-default-from-november-7-25463804, https://www.gateweb3.net/zh-tw/news/detail/grok-api-to-watermark-ai-generated-text-by-default-from-november-7-25463804

## Cross-Org Themes

- Agent memory and task persistence are being productized as named features (Anthropic's dreaming, Meta's Active Memory and Active Focus) rather than left to retrieval add-ons
- Agent runtimes are consolidating into managed or plugin-based platforms (DeepSeek Harness, Kimi Hosted Agent), with update cadence and configuration safety as the emerging pain points

## Rumors and Unverified Claims

Menlo Ventures' 2026 enterprise AI report, as relayed by Gate, is said to show Chinese open models taking 89% of US enterprise open-source AI spend, with Kimi at 61%, DeepSeek at 15%, GLM at 11%, Qwen at 3% and Meta's Llama at 7% as the top Western model; the figures come from a survey of nearly 400 US enterprise AI leaders and were not independently confirmed in the supplied material. A separate report says Coforge joined the SpaceX Super Intelligence partner network as a transformation partner to deploy the Grok portfolio in enterprise workflows.

## Takeaway

The competitive axis this cycle is cost per unit of output and reliability of long-running agents, not headline capability. Watch whether the Grok watermark default holds up in enterprise audits and whether plugin and runtime governance keeps pace with the user growth vendors are now reporting.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
