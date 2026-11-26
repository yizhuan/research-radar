# Giant Watch Summary - Daily - 2026-11-26

## Headline

OpenAI's DevDay 2026 reset the developer platform around always-on agents and subscription-funded inference, while its GPT-5.6 retirement fight shows the migration cost of that reset. The episode's throughline is vendors converting model churn into recurring platform lock-in.

## Top Developments

### 1. OpenAI DevDay 2026 launches Dots agents, GPT-6.1 Sol, Ultrafast, and Sign in with ChatGPT (OpenAI)
At DevDay 2026 in San Francisco, OpenAI announced more than 20 items, led by Dots — always-on agents powered by GPT-6 Astra with their own cloud computer and 4,000+ app plugins — plus GPT-6.1 Sol at $2/$10 per million tokens with $0.10 cached input, an Ultrafast tier at up to 300 tokens per second, the Decisions API, Codex cloud and Code Review, the Agents API, Bedrock Managed Agents, and Sign in with ChatGPT with 16 named launch partners.
Why it matters: The most consequential item is Sign in with ChatGPT, which lets a user's subscription pay for inference in partner apps and counts eligible usage toward plan limits — shifting developer economics and dependency onto OpenAI's account system. Dots and the Agents API extend the same platform logic to hosted agent infrastructure.
Refs: https://dev.to/paullovelace/openai-devday-2026-dots-gpt-61-sol-ultrafast-and-sign-in-with-chatgpt-2ggl, https://aiwithghost.com/news/news-openai-devday-2026-dots-gpt-61-sol-ultrafast-and-sign-in-with-chatgpt/

### 2. OpenAI sets December 23 retirement for GPT-5.6 as GPT-6.2 Sol reaches the Chat tab (OpenAI)
OpenAI began offering GPT-6.2 Sol in ChatGPT's Chat tab to Plus, Pro, Business and Enterprise customers and announced that GPT-5.6 Sol will be discontinued from Chat, with GPT-5.6 Sol and GPT-5.6 Terra also removed from Work and Codex, on December 23, 2026. OpenAI said retiring the two-generations-old model frees compute for newer models; some users objected on X and Reddit, citing writing nuance and cybersecurity research, and some threatened to cancel Pro subscriptions.
Why it matters: A concrete test of whether capability gains translate into user retention: OpenAI is forcing a paid base onto a new base model within weeks of launch, and the backlash is over workflow consistency rather than benchmarks.
Refs: https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&chksm=f03129e31341257fd5f57177c8d11938f21090cbb59df53e53cb66ea7502221894a34242d81f&idx=3&mid=2652745240&sn=6db0d8f2621561054778cdef72220067, https://voi.id/en/amp/603962, https://voi.id/zh/amp/603962

### 3. Google DeepMind lets AI agents run some experiments for next-generation Gemini (Google)
DeepMind research vice president Koray Kavukcuoglu said on the company podcast that AI agents control some of the lab's compute to run experiments for future Gemini models, part of a shift away from separate teams per project toward shared general algorithms. He stressed DeepMind is far from full recursive self-improvement, said training does not reward agents' internal chain-of-thought so intentions stay reviewable in natural language, and argued AGI should be judged by whether people trust everyday products enough to delegate decisions.
Why it matters: A stated change in research workflow rather than a capability claim — but the oversight design (no chain-of-thought reward) is a concrete safety position worth tracking as agents take on more of the lab's own experimentation.
Refs: https://www.sohu.com/a/1106585333_115060?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smpc.channel_248.block3_308_NDdFbm_1_fd.1.1795662189241CDGq1Uw_324, https://www.sofarbot.com/news/XIWb5vX5Hacd, https://www.sofarbot.com/zh/news/XIWb5vX5Hacd, https://www.sofarbot.com/zh-TW/news/XIWb5vX5Hacd, https://dayaai.com/news/story/5035

### 4. Alibaba Cloud documents Qwen Realtime API across WebSocket, WebRTC and AOQ (Qwen)
Alibaba Cloud's Model Studio published documentation for the Qwen Realtime API, which supports WebSocket, WebRTC and AOQ (AI over QUIC) for real-time multimodal interaction, speech recognition, speech synthesis, voice dialogue and audio/video translation across six model categories including qwen3.8-omni-flash-realtime, CosyVoice and Qwen-Livetranslate-Realtime. AOQ uses server-side proxy authentication with temporary client tokens and is aimed at weak-network native apps; all three protocols support Token Plan authentication.
Why it matters: A plumbing-level release, but it positions Qwen's realtime stack for mobile and low-bandwidth deployments where WebRTC alone is a poor fit — an infrastructure play rather than a benchmark one.
Refs: https://miniapp.gate.com/zh-tw/news/detail/qwen-realtime-api-supports-websocket-webrtc-aoq-protocols-25862925, https://www.gateweb3.net/zh/news/detail/qwen-realtime-api-supports-websocket-webrtc-aoq-protocols-25862925

### 5. Z.ai releases GLM-5.4 Loop Transformer at ~750B parameters via Coding Plan (GLM)
Z.ai released GLM-5.4, its first Loop Transformer, running 28 shared layers twice at roughly 750 billion parameters, available to subscribers through GLM Coding Plan, ZCode and Z.ai Chat at plans from $18/month. Z.ai's controlled evidence comes from a 30B-parameter ablation (AIME25 19.17 to 30.42, GPQA-Diamond 47.58 to 56.26), and it has not published a benchmark table for the 750B flagship, general per-token API pricing, or downloadable weights.
Why it matters: The pricing model — point multipliers with separate 5-hour and weekly pools, and a Coding Plan key that cannot be used with the standard API — is as much the story as the architecture, and the flagship's coding claims remain unverified at scale.
Refs: https://miniapp.gate.com/zh-tw/news/detail/glm-54-loop-transformer-28-shared-layers-at-750b-scale-25862973

### 6. Kimi K3.1 Pro Uncensored goes live on bf16.ai with 1M context and vision (Kimi)
Third-party host bf16.ai listed moonshotai/kimi-k3.1-pro-uncensored, a 2.8T-parameter multimodal model with a 1,048,576-token input window, 131,072 max output tokens, image and text input, JSON tool calling and selectable reasoning effort, priced at $1.95/$0.28/$6.90 per million input/cached/output tokens. The post recommends routing it to the Opus/Architect slot in Claude Code while running GLM-5.3 Uncensored and DeepSeek V4.1 Flash Uncensored on cheaper tiers.
Why it matters: Evidence that Chinese flagship models are being resold into Western agent toolchains as interchangeable routing slots — a distribution channel that bypasses first-party APIs and their safety filters.
Refs: https://dev.to/bf16ai/running-28t-kimi-k31-pro-uncensored-1m-context-vision-in-claude-code-opencode-and-roo-code-1kn6

### 7. DeepSeek tightens free-tier limits as V4.1 Flash tops OpenRouter weekly token volume (DeepSeek)
DeepSeek adjusted usage quotas on its free web and app products, no longer supporting continuation of long conversations after more than seven days of inactivity and limiting single-input length and daily usage, citing insufficient compute; the platform has had repeated service interruptions since October. On OpenRouter, DeepSeek V4.1 Flash reportedly reached 59.2 trillion tokens in a single week, ranking first globally.
Why it matters: A visible case of demand outrunning compute at a low-cost provider, and a signal that near-free unlimited access is giving way to tiered commercial operation across the sector.
Refs: https://www.fjsen.com/wap/r/2026-11/26/content_32289552.htm

## Cross-Org Themes

- Agent infrastructure is becoming the product layer: OpenAI's Dots and Agents API, DeepMind's agents running its own experiments, and Qwen's realtime multimodal API all push agents into hosted or first-party pipelines.
- Chinese model providers are competing on price and access mechanics — Z.ai's point-based Coding Plan, DeepSeek's tightened free tiers, and Kimi's resale through a third-party host — rather than on headline benchmark wins alone.
- Model churn is now a retention problem: OpenAI's forced GPT-5.6 retirement and DeepSeek's quota cuts both show providers reallocating scarce compute at the expense of existing user workflows.

## Rumors and Unverified Claims

Z.ai's claim that GLM-5.4 is comparable to 2T–3T-parameter models is vendor positioning with no published flagship benchmark table; a reported KingBench 4 result (55.3% of available score, seventh of 19 models, 431 minutes) is secondhand with no linked leaderboard or reproducible evaluation suite. A separate Z.ai item described an open-source GLM-5.2 trained entirely on Huawei Ascend accelerators with MIT-licensed weights and FrontierSWE results near Claude Opus 4.8, but the source page failed to fetch and the claim could not be checked. An OpenAI executive reportedly cited 'over 60 partners' for Sign in with ChatGPT on X, while the official count is 16.

## Takeaway

The competitive axis this cycle is not raw capability but who controls the account, the compute allocation and the routing slot. Watch whether OpenAI's December 23 migration produces measurable churn, and whether Z.ai publishes flagship-scale benchmarks for GLM-5.4.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
