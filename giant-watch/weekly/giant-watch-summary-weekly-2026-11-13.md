# Giant Watch Summary - Weekly - 2026-11-13

## Headline

Google's Gemini 4 Carbon rollout and Anthropic's Claude Fable 5.2 launch anchor a week in which frontier vendors pushed long-horizon agentic models into paying developer and enterprise channels. The episode's throughline is the shift from chat capability to task completion, with vendors pairing new flagships with agent orchestration tooling and tiered access.

## Top Developments

### 1. Google opens Gemini 4 Carbon to developers, enterprises, scientists and consumers (Google)
Google DeepMind made Gemini 4 Carbon generally available on November 10, 2026, positioning it as its strongest model for cybersecurity and long-horizon agentic workflows across software engineering, scientific reasoning and knowledge work. Access runs through the Gemini API in Google AI Studio and Gemini for business for paying developers and enterprises, with Google AI Ultra subscribers reaching it via Google Antigravity, the Gemini app and AI Mode in Search. Introductory API pricing matches Gemini 4 Argon at $2 per million input tokens and $10 per million output tokens through November 30, 2026, rising to $4 and $20 afterward. Google also previewed a /swarm feature in Antigravity for coordinating multiple agents on one task.
Why it matters: The broadest simultaneous release of the week, spanning paid API, enterprise and consumer tiers, and the clearest statement that frontier capability is now sold on long-horizon agentic work rather than chat quality.
Refs: https://newsable.asianetnews.com/business/google-deepmind-launches-gemini-4-carbon-model-for-complex-ai-tasks-articleshow-n2oz7rl, https://www.sohu.com/a/1099901388_114760?scm=10008.1478_13-1478_13-70_70.0-3231002.0-1-0-0-0.0&spm=smpc.content.fd-link.2.1794354821653KUnv7nf, https://shattered.io/gemini-4-carbon-access-signal-libsignal-alphaproof-code-6-5m-lean-proofs-2026/, https://www.dtinsight.com.cn/sys-nd/4377.html

### 2. Anthropic releases Claude Fable 5.2 with a gated Mythos 5.2 sibling (Anthropic)
Anthropic's Claude Fable 5.2 shipped on November 9, 2026, built for demanding reasoning and long-horizon agentic work such as multi-hour agent sessions and multistep deep research. It carries a 1M-token context window, 128K max output, adaptive always-on thinking and $8/$40 per-million-token pricing, with a knowledge cutoff of June 2026 and retirement no sooner than November 9, 2027. Claude Mythos 5.2 shares its specifications and pricing but is restricted to organizations verified through Anthropic programs such as the Cyber Verification Program. Fable 5.2 requires 30-day data retention and is unavailable under zero data retention unless expressly authorized. The model appeared across Amazon Bedrock, Google Cloud and Microsoft Foundry documentation in the same window.
Why it matters: Anthropic's first frontier release since its CEO publicly called for slowing frontier development, and a notable split between an open commercial model and a verification-gated sibling for cyber and life-sciences work.
Refs: https://platform.claude.com/docs/en/models/fable-5-2/overview, https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html, https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/fable-5-2, https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models, https://www.sohu.com/a/1099752356_122512986?scm=10001.7746_13-119000.0.0-0-0-0-0.0&spm=smpc.channel_354.block3_32_P7Ovbu_1_fd.28.1794308716442BiCDPaV_7746

### 3. Anthropic extends Claude into spreadsheets, meetings and whiteboards (Anthropic)
On November 10, 2026, Anthropic announced Claude Sheets, Claude Whiteboards and Claude Meetings, and formally launched Claude Data (renamed from Claude Dashboards). Claude Sheets builds spreadsheets from plain language and can edit individual cells with change tracking, exporting to Excel or CSV, though Anthropic says it is not yet suited to complex financial models. Claude Meetings is being tested with Team and Enterprise customers on Google Meet, and Claude Whiteboards turns discussion into visual plans with owners and deadlines. Coverage frames the move as Anthropic competing with Microsoft and Google for office work.
Why it matters: Marks Anthropic's shift from a developer-facing tool toward a broader professional platform, putting it in direct competition with Microsoft 365 Copilot and Google Workspace.
Refs: https://www.vietnam.vn/en/anthropic-mo-rong-claude-thanh-bo-cong-cu-van-phong-ai

### 4. Alibaba releases Qwen4-Max preview through a subscription-only Token Plan (Qwen)
Alibaba released the Qwen4-Max preview on November 11, 2026, as the flagship of its fourth-generation Qwen family, with a 1M-token context window and text, image and video input. It is available only through the Token Plan subscription rather than pay-as-you-go, with a preview window running November 11 to November 25, after which the model identifier is retired and a formal version ships under a new name. Alibaba has not disclosed parameter count, benchmark scores or official unit pricing. The preview is also reachable through Qwen Office, Qoder, the Qwen app and QwenStudio.
Why it matters: An unusual go-to-market: a flagship model released first into a metered subscription and multiple consumer surfaces rather than a standard API, with capability claims left unquantified.
Refs: https://developer.aliyun.com/article/1782441, https://developer.aliyun.com/article/1782099

### 5. DeepSeek V4 family lands on Amazon SageMaker JumpStart (DeepSeek)
AWS announced on November 11, 2026 that DeepSeek-V4-Pro, DeepSeek-V4-Flash and DeepSeek-V4.1-Flash are available on Amazon SageMaker JumpStart. The three open-weight Mixture-of-Experts models are released under the MIT license. V4-Pro is a 1.6T-parameter model activating 49B parameters per token with a 1M-token context window; V4-Flash is a 284B-parameter model activating 13B; V4.1-Flash uses a Causal Encoder-Decoder architecture with a 552B backbone and adds native multimodal support.
Why it matters: Puts DeepSeek's flagship open-weight family into a major Western cloud's one-click deployment catalog, widening enterprise reach for Chinese open models.
Refs: https://aws.amazon.com/cn/about-aws/whats-new/2026/01/deepseek-v4-pro-v4-flash-v4.1-flash-on-sagemaker-jumpstart/, https://www.alibabacloud.com/help/en/model-studio/deepseek-v4-pro

### 6. DeepSeek says its Harness agent framework passed 1.54 million daily users (DeepSeek)
DeepSeek said its Harness agent framework reached 1.54 million daily active users less than three months after launching on August 13, 2026, with a desktop app following on September 29. Users through the official API were consuming roughly 92 trillion tokens a day as of November 4, and third-party plug-ins had grown to about 35,000, with around 60 percent of active users having built or installed at least one. DeepSeek said it plans a plug-in marketplace and a developer support program, and has set up its first product division.
Why it matters: The most concrete usage metric of the week for an agent harness, and a direct challenge to OpenAI's Codex and Anthropic's Claude Code in the agent-tooling layer.
Refs: https://www.scmp.com/tech/big-tech/article/3373757/can-deepseek-challenge-openai-anthropic-ai-agents-harness-adoption-takes?module=Big%20Tech&pgtype=section

### 7. GLM-5.3 arrives on SambaCloud with open-weight agentic and security claims (GLM)
SambaNova said GLM-5.3, Z.ai's flagship for complex software engineering and long-horizon agent tasks, is now available on SambaCloud at over 200 tokens per second. The post cites 28.3 on Terminal-Bench 3.0 and 66.9 on DeepSWE v1.1, described as state of the art among open-weight models, and an internal Code Bench score of 31.4 percent at around 50K output tokens per task versus Claude Opus 4.8 at 29.5 percent with 120K tokens. It also cites the best published score on CyberGym and a US Center for AI Standards and Innovation rating as the most advanced open-weight model for cybersecurity. Z.ai's own release notes describe GLM-5.3 as improving 50 percent over GLM-5.2 on its internal Z.ai Code Bench and reaching open-source SOTA on Terminal Bench 3.0.
Why it matters: A strong open-weight claim in exactly the agentic-coding and defensive-security categories where closed frontier labs are competing, delivered through a third-party inference provider.
Refs: https://sambanova.ai/blog/glm-5.3-now-running-on-sambacloud, https://docs.bigmodel.cn/cn/update/new-releases

### 8. Moonshot launches Kimi K3.1 Pro with 1M context and always-on reasoning (Kimi)
Kimi's API platform now lists Kimi K3.1 Pro and K3.1 Pro Highspeed as available, described as Moonshot's most capable flagship with a 1M-token context window and native visual understanding, with improvements in coding, 3D creation, financial research and modeling. Reasoning and Preserved Thinking are always on, with reasoning effort set via a top-level field accepting low, high or max (default max). Runpod's endpoint documentation describes K3.1 Pro as a 3T-class open-weight model priced at $2 per million input and $10 per million output tokens, with the Highspeed variant at $4 and $20.
Why it matters: Adds another 1M-context, always-reasoning flagship to the market, and the open-weight framing puts it in direct comparison with GLM-5.3 and DeepSeek's V4 family.
Refs: https://platform.kimi.ai/docs/get-your-api-key, https://platform.kimi.com/docs/get-api-key, https://platform.kimi.ai/docs/guide/use-thinking-models, https://docs.runpod.io/public-endpoints/models/moonshot-kimi

### 9. Musk announces Grok 4.8 with a from-scratch C/C++ RL and inference stack (xAI)
Elon Musk announced Grok 4.8, saying xAI abandoned JAX and SGLang and rewrote its entire reinforcement-learning and inference stack in C/C++, which he said took extra time. In his posts he said pre-training is complete after cleanup of supervised fine-tuning data, that 4.8 is now in RL with evaluations climbing, and that a soft rollout to Grok Bot users would follow later in the week. The report says the model is promised to bear no similarity to version 4.7.
Why it matters: A rare public disclosure of infrastructure re-architecture at a frontier lab, and an unusually explicit statement that a model is mid-training rather than shipped.
Refs: https://www.thenews.com.pk/amp/1423133-elon-musk-announces-grok-48-featuring-a-full-c-stack-rewrite-what-to-know

### 10. Google lists Gemini 4 Hydrogen as generally available (Google)
Google Cloud documentation lists Gemini 4 Hydrogen as a generally available short-term release with a release date of November 12, 2026, subject to a minimum 45-day retirement notice policy. It uses a unified 1,048,576-token limit covering both input and output, with a single foreground segment generating up to 65,536 output tokens and long decodes extending output to the full window. It supports thinking levels LOW, MEDIUM, HIGH (default) and XHIGH, accepts Microsoft Office and OpenDocument files alongside PDFs and text, and supports implicit context caching only.
Why it matters: A second Google flagship in the same week, notable for a unified input-output token budget and Office document ingestion rather than a separate model tier.
Refs: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-hydrogen

## Cross-Org Themes

- Frontier releases are being framed around long-horizon agentic work rather than chat quality
- Multiple labs shipped 1M-token context windows as a baseline expectation
- Agent harnesses and orchestration tooling are becoming the competitive layer above the model
- Open-weight Chinese models are being distributed through Western cloud and inference providers

## Rumors and Unverified Claims

Coverage of Anthropic's Claude Fable 5.2 release states the company is preparing for an IPO and that this was its first frontier model since CEO Dario Amodei called for slowing frontier AI development in September; the IPO framing is not corroborated by the supplied Anthropic documentation. A Chinese-language analysis of Qwen4-Max cites third-party GameFeel Bench scores for unreleased Qwen4 family models and describes architecture details from community posts, both explicitly flagged in the source as unofficial and not confirmed by Alibaba. A Databricks report quotes CEO Ali Ghodsi saying he uses Genie instead of OpenClaw, Instinct and Muse, which he described as having questionable security; that characterization is an executive's opinion, not a verified finding.

## Takeaway

The decisive question this week is whether agentic capability claims survive contact with paying customers: watch whether Google's November 30 price step changes Carbon adoption, whether Qwen4-Max ships a formal version with disclosed benchmarks after its November 25 preview ends, and whether DeepSeek's Harness usage figures hold as OpenAI and Anthropic push their own harnesses.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
