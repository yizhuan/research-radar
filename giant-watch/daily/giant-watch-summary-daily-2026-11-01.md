# Giant Watch Summary - Daily - 2026-11-01

## Headline

DeepSeek open-sourced a Router-Worker "Super-agent" prototype aimed squarely at Anthropic's Claude Code, while OpenAI moved to pool ChatGPT and Codex usage into a single token budget from December. The day's throughline is vendors re-architecting the layer around the model — orchestration, metering and compliance — rather than shipping new flagship weights.

## Top Developments

### 1. DeepSeek Harness team publishes and open-sources Super-agent architecture (DeepSeek)
On the evening of Oct 31 the DeepSeek Harness team published a technical article, "Super-agent design exploration: toward a more autonomous agent system," and released an open-source prototype. The design uses a Router that ingests group chat, GitHub and email channels and dispatches work to Workers that each hold independent context and can call Subagents; event-driven, two-level filtering lets the system spot defects in group chats without being @-mentioned and attempt background reproduction and fixes. DeepSeek says an internal instance already runs in daily R&D, and stresses the post is an engineering architecture discussion, not a description of existing product features.
Why it matters: A Chinese lab publishing a multi-agent orchestration design explicitly framed by coverage as competing with Claude Code and Codex shifts the agent race from model quality to system architecture, and the open prototype gives outside teams something to test against.
Refs: https://finance.sina.com.cn/roll/2026-11-01/doc-inixeyiz3146996.shtml, https://baijiahao.baidu.com/s?id=1880587307431893778&wfr=spider&for=pc, https://www.toutiao.com/article/7703023092108362283/?wid=1793500128269, https://www.scmp.com/tech/article/3372884/deepseek-unveils-ai-super-agent-coding-race-openai-anthropic?module=AI_Recommended_for_you_In-house&pgtype=section, https://www.digitaltoday.co.kr/en/view/122265/deepseek-unveils-super-agent-autonomous-coding-agent-targeting-claude-code

### 2. OpenAI to merge ChatGPT and Codex usage into one token-based allowance from December (OpenAI)
OpenAI's help documentation, as reported Oct 31–Nov 1, says Plus, Pro and Business plans will draw ChatGPT and Codex from a single shared token allowance starting in December, when the agentic features of ChatGPT Work (built on Codex) fold into the main ChatGPT experience. Ordinary chats currently meter by message count per model; after the switch each request is priced by tokens. Instant chat is excluded from the shared pool, and users can view combined remaining allowance and reset time under Settings > Usage. No exact December date is given.
Why it matters: Pooling coding and chat budgets changes the economics for dual-use subscribers and signals that agentic capability is being consolidated into the core product with cost control attached.
Refs: https://airebao.com/item/51636, https://zhuanlan.zhihu.com/p/2100195358156513424

### 3. ChatGPT Pro and Business subscriptions begin bundling monthly OpenAI API credits (OpenAI)
Per a write-up citing OpenAI's Oct 28 release notes and help pages read Nov 1, ChatGPT Pro plans now include monthly API credits equal to plan price ($100/$200/$500), and Business workspaces get $20 per Standard seat and $100 per Premium seat pooled to a $500 monthly cap; annual workspaces get a year up front capped at $6,000. Plus, free trials, Enterprise, Edu and legacy Codex seats are not listed as eligible. Credits do not roll over, do not raise ChatGPT or signed-in Codex limits, and exclude Codex via API keys. The author notes the structure mirrors an Anthropic credits offer launched about three weeks earlier.
Why it matters: Bundling API spend into consumer and SMB subscriptions is a direct bid for builders against Anthropic, and the exclusions define exactly which workloads the credit does not cover.
Refs: https://justinmckelvey.com/blog/openai-api-credits

### 4. Custom GPT retirement set for Dec 11, with custom actions excluded from migration (OpenAI)
A migration runbook published Nov 1, citing OpenAI's retirement FAQ and migration guide, says Custom GPTs become inaccessible on Dec 11, 2026 (Feb 11, 2027 for FedRAMP and approved deferrals), with new GPT creation already ended for affected Enterprise workspaces on Oct 26. Instructions, knowledge files and connected apps move to plugins, but custom actions do not transfer and must be rebuilt on a supported app or custom MCP server; selected model and sharing settings also do not carry over. The article notes OpenAI's help center returned a 403 to a scripted fetch on Nov 1, so dates come from write-ups citing it, and that the FAQ calls dates "subject to change."
Why it matters: For enterprise builders, the forced migration converts working API-connected GPTs into new MCP servers with separate permissions and ownership — a concrete, dated workload with a security-review tail.
Refs: https://www.beri.net/article/custom-gpt-retirement-december-11-plugin-migration-custom-actions-mcp-enterprise-deferral

### 5. Google DeepMind unveils Genie 4 real-time world model with native audio (Google)
DeepMind announced Genie 4, an experimental model that generates and runs interactive worlds in real time, steered by natural-language instructions, combining Gemini models (including Gemini Omni for scene anchoring) with a world simulator. It is described as DeepMind's first real-time world model to generate audio natively, covering ambient sound, music and interactive dialogue. Access is a research preview for trusted testers, with planned availability to Google AI Ultra subscribers via Project Genie and to early-access partners through the Gemini API and AI Studio. DeepMind acknowledges drift in visual detail and object permanence over long sessions and lists physics, audio accuracy and spatial consistency as open problems; outputs carry SynthID.
Why it matters: A restricted but concrete step toward simulation environments usable for agent and robotics training, with explicit limitations disclosed rather than a general-availability launch.
Refs: https://www.innoparkit.com/google-deepmind-unveils-genie-4-real-time-world-model-native-audio

### 6. Gemini-powered PlanAssist expands to 12 more English planning authorities (Google)
Google DeepMind said PlanAssist, a Gemini-built planning-support tool, will be made available to 12 additional local planning authorities in England after early pilots in Barnet, Camden and Dorset. The company reports the tool cut the average time officers spent on householder assessment tasks by up to 58%; the source explicitly notes this measures assessment time, not approval speed. Officers retain final decision-making on every application, and wider-deployment results are not yet established.
Why it matters: A measurable public-sector deployment of Gemini with a named metric and a human-in-the-loop safeguard — the kind of reference case enterprise and government buyers ask for.
Refs: https://aipricedb.com/en/ai-news/google-deepmind-to-expand-gemini-powered-planassist-to-12-more-english-planning-authorities-545c0196?topic=product

### 7. Meta launches Muse Wonder model family, claiming return to the frontier (Meta)
Meta said its Muse Wonder series, including Muse Wonder Full, has frontier capabilities and marks its next step toward "personal superintelligence." The models will be available through the API and Muse Code, with the strongest version powering features including the Muse personal agent. According to the Artificial Analysis Intelligence Index cited in coverage, the largest Muse Wonder version surpasses Anthropic's Claude Fable 5.1 and trails only Claude Opus 5.5; Meta claims wins over OpenAI's GPT-6 Astra and both Claude models on some specialized benchmarks, notably legal documents and software development. New Active Memory and Active Focus features aim to keep agents on goal. Meta did not disclose training details or whether Muse Wonder-driven agents showed misbehavior in testing.
Why it matters: If the cited index placement holds, Meta re-enters the top tier after a stretch of underperforming Llama generations — a competitive reset for the frontier-model ranking.
Refs: https://www.waender.com/news/muse-wonder-puts-meta-back-at-the-ai-frontier-13179/

### 8. Meta AI-training copyright cases get May 3, 2027 trial date; acquisition, not fair use, is the fight (Meta)
A joint case management statement filed Oct 27, 2026 in the Northern District of California sets a May 3, 2027 trial for Kadrey v. Meta and Entrepreneur Media, with three publisher cases queued behind it in filing order. The dispute recorded is about how books were acquired: plaintiffs say a former Meta employee testified he torrented and distributed Books3, while Meta disputes the characterization and says the deleted copy sat on a personal computer years after he left. Entrepreneur Media must file an amended complaint by Nov 6, 2026, expected to add 400+ books and 140+ magazine issues identified from Meta's interrogatory responses and a plaintiffs' expert report. Meta is pressing for registration and chain-of-title documentation for each asserted work.
Why it matters: The case is being decided on provenance, discovery timing and registration paperwork rather than the fair-use merits — a template for how AI-training copyright exposure will actually be litigated.
Refs: https://www.perspireip.com/news/meta-books3-ai-training-copyright-trial-may-2027-kadrey-entrepreneur/

### 9. Z.ai confirms anonymous "Ox Alpha" model as GLM-5.3-Flash, served on 100,000+ domestic chips (GLM)
Z.ai (Zhipu) confirmed that the anonymous model tested on OpenRouter and OpenCode as Ox Alpha is its GLM-5.3-Flash. The company says test-period traffic reached 100 trillion tokens per day, cumulatively over 50 trillion tokens in five days, served by a cluster of more than 100,000 domestic chips, and claims hardware efficiency and per-token cost on par with mainstream Nvidia GPUs. The model is 320B total / 18B active parameters, priced at 0.8 yuan input and 2.8 yuan output per million tokens (half price for the first two weeks), which the report frames as roughly 1/40 the price of Claude Opus 4.8. Z.ai shares reportedly rose over 7% intraday in Hong Kong.
Why it matters: A large-scale inference deployment on non-Nvidia silicon with aggressive pricing is a direct test of whether domestic chip stacks can carry frontier-adjacent serving economics.
Refs: https://blog.9nn.cn/newsflashes/6883.html

### 10. Z.ai co-founder Tang Jie calls recursive self-improvement the main AGI problem, urges shared safety effort (GLM)
Speaking at the World Laureates Forum in Shanghai on Saturday, Tsinghua professor and Z.ai co-founder Tang Jie said recursive self-improvement is "the main research problem" for AGI and represents a new R&D paradigm, while calling for researchers to be "humble" and for the world to organize shared safety guarantees. He did not disclose how much of Z.ai's R&D is AI-performed. Coverage notes Z.ai previously said GLM-5.3 helped optimize its own inference infrastructure for Chinese chips, and that Anthropic reported AI leading 26% of its internal AI R&D in August, up from about 1% in March.
Why it matters: A prominent Chinese lab leader publicly aligning with the RSI framing already used by OpenAI and Anthropic, and attaching a governance ask rather than only a capability claim.
Refs: https://www.scmp.com/tech/tech-trends/article/3372834/self-improving-ai-key-step-towards-agi-safety-key-zai-founder?module=latest&pgtype=homepage

### 11. Alibaba's Qwen3.8 series opens flagship weights for the first time (Qwen)
A Nov 1 roundup says Alibaba released multiple Qwen3.8 models between August and October 2026 across flagship, mid-size dense and lightweight tiers. Qwen3.8-Max is described as a sparse MoE with roughly 2.4 trillion total parameters and about 95 billion active per token, a 1M context window and native multimodality — the first time Qwen has opened flagship-scale weights. Qwen3.8-27B is a dense model under Apache 2.0 aimed at local deployment, and Qwen3.8-Flash is 125B total / 6B active with API pricing cited at 1 yuan input and 3 yuan output per million tokens.
Why it matters: Opening flagship weights changes the self-hosting calculus for teams with data-residency constraints and intensifies the open-weight price competition with Meta and Mistral.
Refs: https://www.exb1.com/news/10503.html

### 12. Alibaba says Qwen will power Apple Intelligence features in China (Qwen)
Alibaba announced on Oct 31 a partnership integrating Qwen into Apple Intelligence for Chinese users, covering Siri, system writing tools and visual intelligence for text and image understanding and generation. The post says features open in iOS developer beta from Nov 4 and ship with iOS 27.3 in December, that Siri seeks user consent before sending content to Qwen, and that requests and responses will not be used by Alibaba for model training. It also states Apple Intelligence passed generative-AI service filing with the Cyberspace Administration of China on July 15.
Why it matters: A system-level placement inside iOS is a distribution win no app-store ranking matches, and it makes Qwen the default Chinese-language intelligence layer on a major global handset.
Refs: https://zhuanlan.zhihu.com/p/2100141645266273073

### 13. Moonshot closes Kimi K2 to new users, plans full retirement by end of December (Kimi)
Moonshot's API docs, per multiple Nov 1 write-ups, state that from Oct 31, 2026 the K2 series (kimi-k2.6, kimi-k2.7-code and its highspeed variant) is unavailable to newly registered users, with existing accounts unaffected, and that all K2 models are planned for retirement by end of December 2026. The named migration target is kimi-k3.1-pro, which has a 1,048,576-token context versus 262,144 for K2. Migration notes flag that K3 fixes several sampling parameters, removes the K2 thinking switch, and adds a reasoning_effort field defaulting to "max," so a bare model-string swap raises cost; third-party pricing lists K3.1 Pro at $2 input / $10 output per million tokens versus $0.95/$4 for K2.7 Code.
Why it matters: A dated deprecation with a cost-changing default is the kind of API churn that forces engineering teams to re-baseline budgets and test suites before year-end.
Refs: https://dev.to/ai_maya_063fc568e157562fd/kimi-k2-closes-in-december-what-moving-to-k31-pro-changes-and-what-the-default-reasoning-effort-fld#comments, https://appauxin.com/kimi-k2-api-retirement-migration/, https://www.wsisp.com/helps/120858.html

### 14. xAI to add invisible watermarks to Grok text output from Nov 7, citing EU AI Act (xAI)
An "Output Watermarking" page on docs.x.ai, last updated Oct 31, 2026, says that from Nov 7 supported Grok models will embed an invisible statistical watermark applied during generation, affecting token selection rather than adding characters or metadata. It covers grok-4.7, grok-4.6, grok-4.5, grok-4.3 and three grok-4.20 variants across all API endpoints, requires no request changes, and adds an x-watermark response header; a separate detection API is available on application. Team admins can opt out per model in the console after confirming a legal exception applies, and opt-outs are logged. The page attributes the change to EU AI Act compliance and uses "SpaceXSI" throughout; xAI's claims that quality and speed are unaffected are not independently verified.
Why it matters: A concrete, dated compliance change from a major API provider that developers can verify themselves via response headers after Nov 7 — and a template for how AI Act transparency obligations reach API surfaces.
Refs: https://hub-assets-cache.baai.ac.cn/view/59240, https://www.ithome.com/1/020/721.htm, https://tech.ifeng.com/c/8xhL6mziJzv

## Cross-Org Themes

- Vendors are competing on the layer around the model — orchestration, metering, migration tooling and compliance — rather than on new flagship weights alone
- Chinese labs are pushing open weights and aggressive pricing (Qwen3.8, GLM-5.3-Flash) while US labs restructure subscriptions and deprecate builder surfaces
- Dated deprecations and forced migrations (Custom GPTs, Kimi K2) are creating near-term engineering work for API and platform customers

## Rumors and Unverified Claims

A Wccftech report relayed by a Nov 1 analysis claims a personality-index comparison links Kimi K3.1 Pro to GPT-6 Astra and GLM-5.3 to Anthropic's Claude 5 series, suggesting distillation; the analysis itself calls this circumstantial and notes no on-record response from OpenAI, DeepSeek, Moonshot, Z.ai or Anthropic. The same report teases an unannounced GPT-6.1 Astra and an internal "GPT-6.2 Betelgeuse" codename with no official OpenAI confirmation. A forum post claims Fable 5.5 and GPT-6.2 Astra are in gray testing and may launch next week. Separately, a report says Meta built a humanoid robot prototype "Max" with China's Fourier using Nvidia Jetson Thor and Muse AI, with a second-generation "Max 2" started in September; Meta's response, as quoted, was that the work is internal research with no plans to sell the units.

## Takeaway

The next evidence to watch is whether these architectural and pricing bets hold up under real usage: DeepSeek's Super-agent prototype under production load, whether OpenAI's shared token pool actually lands in December as described, and whether xAI's watermark header appears as promised on Nov 7.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
