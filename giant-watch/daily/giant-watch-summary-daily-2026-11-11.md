# Giant Watch Summary - Daily - 2026-11-11

## Headline

Google's Gemini 4 Carbon and Anthropic's Claude Fable 5.2 / Mythos 5.2 both went into broad release on November 10-11, pushing frontier models toward long-horizon agentic and scientific work. The episode's throughline is that capability gains are now being packaged with explicit access tiers and safety guardrails.

## Top Developments

### 1. Google DeepMind opens Gemini 4 Carbon to developers, enterprises, scientists and consumers (Google)
Google DeepMind released Gemini 4 Carbon, described as its strongest model for cybersecurity and long-horizon agentic workflows across knowledge work, software engineering and scientific reasoning. It is available through the Gemini API in Google AI Studio and Gemini for Business for paying developers and enterprises, with rollout to Google AI Ultra subscribers via Antigravity, the Gemini app and AI Mode in Search. Introductory pricing matches Gemini 4 Argon at $2 per million input tokens and $10 per million output tokens, rising to $4/$20 after November 30. Google also previewed a /swarm feature in Antigravity for coordinating multiple agents.
Why it matters: The broadest frontier-model release of the window, and the clearest example of a lab shipping a high-reasoning model with tiered access and a multi-agent orchestration layer.
Refs: https://china.googleblog.com/2026/11/, https://www.ifanr.com/1688883?utm_source=rss&utm_medium=rss&utm_campaign=, https://www.sohu.com/a/1099901388_114760?scm=10008.1478_13-1478_13-70_70.0-3231002.0-1-0-0-0.0&spm=smpc.content.fd-link.2.1794354821653KUnv7nf, https://newsable.asianetnews.com/business/google-deepmind-launches-gemini-4-carbon-model-for-complex-ai-tasks-articleshow-n2oz7rl, https://github.com/dboeter/daily-diff/issues/227

### 2. Anthropic launches Claude Fable 5.2 and Claude Mythos 5.2 with split access and safety tiers (Anthropic)
Anthropic released Claude Fable 5.2, a frontier model for technical work open to general users, and Claude Mythos 5.2, a model for cybersecurity and life-sciences research available only through Anthropic's verification programs. Fable 5.2 intercepts most bio and cyber requests and falls back to older Opus models; Mythos 5.2 removes those restrictions for vetted researchers. Both are priced at $8 per million input tokens and $40 per million output tokens, 20% below the prior generation, with a high-performance mode up to 2.5x faster at double the cost. Reported benchmarks include a 74.6% score on Terminal-Bench-Science 0.1 for Fable 5.2 and accurate modeling of 28 of 34 AAV capsid samples for Mythos 5.2.
Why it matters: A direct frontier release that makes access control and safety classification part of the product architecture rather than an afterthought.
Refs: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html, https://www.digitaltoday.co.kr/cn/view/123947/anthropic-unveils-fable-5-2-mythos-5-2-to-boost-life-science-and-coding-performance, https://www.eet-china.com/mp/a538468.html, https://www.nananobanana.com/zh/blogs/cmwbgnqw71a1sl4fskuzdihmj

### 3. Alibaba releases Qwen4-Max preview through Token Plan and multiple Qwen apps (Qwen)
Alibaba announced the fourth-generation Qwen flagship and opened a preview of Qwen4-Max (model ID qwen4-max-preview) through its Token Plan subscription, also wiring it into Qwen Office, Qoder, the Qwen app and QwenStudio. The preview runs from November 11 10:00 to November 25 24:00 UTC+8, after which the model identifier goes offline. Alibaba describes upgrades in knowledge understanding, world perception, coding and agentic capability, with support for text, image and video input and a 1M-token context window per platform documentation. Official benchmark scores, parameter counts and open-source plans were not disclosed.
Why it matters: A major Chinese lab moving its flagship into real billing and application channels before a formal launch, shifting evaluation earlier in the release cycle.
Refs: https://developer.aliyun.com/article/1782099, https://developer.aliyun.com/article/1782128, https://www.cnstock.com/commonDetail/826985, https://www.163.com/dy/article/LBERCM340511B8LM.html, https://news.qiniu.com/archives/1794366632000

### 4. Musk says Grok 4.8 will trail Claude Opus 5.5, flags limited rollout this week (xAI)
Elon Musk said on X that xAI's next model, Grok 4.8, will perform 'not as good' as Anthropic's Claude Opus 5.5, which he called a masterpiece. He said Grok 4.8 has finished pre-training and is in reinforcement learning, with supervised fine-tuning data overhauled, and that a limited soft rollout to some bot users is planned as early as later this week. Musk also said xAI is discontinuing JAX and SGLang and rewriting its inference and reinforcement-learning systems in C and C++, and that Grok 5 should exceed Opus 5.5 in two to three months.
Why it matters: A rare public concession from a frontier lab founder, paired with disclosure of a full stack rewrite and a near-term rollout timeline.
Refs: https://www.digitaltoday.co.kr/en/view/124180/musk-calls-claude-opus-5-5-a-masterpiece-says-grok-4-8-wont-beat-it

### 5. Google DeepMind introduces Gemini Robotics 2.5 with improved dexterity (Google)
Google DeepMind introduced Gemini Robotics 2.5, an updated vision-language-action model it said approaches human-level performance on some real-world robotic tasks. The model was evaluated across more than 200 activities, including serving food with tongs and using a pipette, and was demonstrated on Apptronik's Apollo 2 humanoid tying a bow with five-fingered hands. Google said robots using Gemini Robotics have performed work at Mercedes-Benz factories and that it is preparing an open-source safety benchmark called ASIMOV-jailbreak.
Why it matters: Extends the Gemini platform from software agents into embodied manipulation, a distinct frontier from the coding and research releases.
Refs: https://dataconomy.com/2026/11/11/google-unveils-gemini-robotics-25-as-ai-nears-human-level/

### 6. QuestMobile data shows DeepSeek monthly actives down 15.2% despite model reputation (DeepSeek)
A 36Kr analysis citing QuestMobile's autumn 2026 report put AI-native app monthly actives at 420 million for Doubao, 158 million for Qwen, 123 million for DeepSeek and 37.33 million for Yuanbao, with year-on-year growth of +143.6%, +5076.6%, -15.2% and +13.6% respectively. The piece notes DeepSeek has the strongest model reputation and the lowest prices among them, and that it cut V4-Pro input pricing from 10 yuan to 1 yuan and output from 20 yuan to 2 yuan in April. It argues retention depends on high-frequency use scenarios rather than model capability or price.
Why it matters: A counterpoint to the release cycle: distribution and usage frequency, not benchmark leadership, are framed as the durable advantage.
Refs: https://eu.36kr.com/en/p/4064866450003849, https://36kr.com/p/4064866450003849?ref=aididai.cn

## Cross-Org Themes

- Frontier releases are being paired with explicit access tiers and safety guardrails rather than uniform public availability.
- Long-horizon agentic and multi-agent orchestration is the shared capability target across Google, Anthropic and Alibaba releases.
- Pricing and packaging, including introductory rates and subscription plans, are being used as launch levers alongside capability claims.

## Rumors and Unverified Claims

Anthropic was reported to have launched an IPO roadshow for 825 million Class A shares at $70-$78, targeting a Nasdaq listing under 'ANT' at a reported $1.3 trillion valuation (daily-diff digest). A GLM-5.5 model was discussed in a comparison article, but the same article states no such model exists in Z.ai's release log or pricing page. Qwen4-Max context-window and parameter figures circulating online were explicitly flagged as unconfirmed by Alibaba's own documentation summaries.

## Takeaway

The next evidence to watch is whether the guarded and preview-tier releases convert into sustained usage, and whether xAI's rewritten stack produces a Grok 4.8 result that closes the gap its founder has already conceded.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
