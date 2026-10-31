# Giant Watch Summary - Daily - 2026-10-31

## Headline

Alibaba's Qwen lands inside Apple Intelligence for China, the day's most consequential distribution deal, while Google DeepMind's Gemini 4 Carbon pushes frontier capability further behind a defenders-first gate. The episode's through-line is agents and access: who gets frontier models, on whose platform, and under what safeguards.

## Top Developments

### 1. Alibaba and Apple partner to bring Qwen into Apple Intelligence in China (Qwen)
Alibaba announced a partnership with Apple to integrate its Qwen model into Apple Intelligence, letting users in China call Qwen's text and image understanding and content generation through Siri, Apple's system writing tools (as 'Compose with Qwen') and Visual Intelligence. Developer beta testing was slated to begin November 4, with a consumer rollout alongside iOS 27.3 in December, limited to iPhones purchased in China or with device region and Apple Account set to China. Users must opt in, and Alibaba said requests and responses will not be used for model training.
Why it matters: Puts a Chinese frontier model inside the default assistant of Apple's second-largest market, a distribution win that reframes Qwen's competitive position beyond benchmarks.
Refs: https://hznews.hangzhou.com.cn/jingji/content/2026-10/31/content_9362286.htm, https://baijiahao.baidu.com/s?id=1880528673045100174&wfr=spider&for=pc, https://news.qq.com/rain/a/20261031A03O2300, https://news.dayoo.com/finance/202610/31/171077_55018814.htm, https://www.scmp.com/tech/big-tech/article/3372831/apple-intelligence-roll-out-iphones-china-december-alibaba-backing?module=top_story&pgtype=section

### 2. Google DeepMind unveils Gemini 4 Carbon, gated first to cyber defenders (Google)
Google DeepMind announced Gemini 4 Carbon on October 28, 2026, describing it as its strongest model for cybersecurity and long-horizon work and reporting top placement on the Artificial Analysis Intelligence Index v5.0. Reported security scores include 88.2% on SEC-bench Pro, 71% on CWE-bench and 54.8% on ExploitGym, with Terminal-Bench 4.0 at 65.2% and OSWorld-2.1 at 81.5% in Google's own comparison tables. Pricing was announced at $2/$10 per million tokens introductory, rising to $4/$20 later, but access is staged: a limited set of cybersecurity specialists first, then vetted partners via the Fairwind program, with no general-availability date.
Why it matters: A frontier release whose defining feature is restricted, defender-first access rather than open availability, setting a possible template for how top-tier capability ships.
Refs: https://startuphub.today/en/editorial/3868/googles-gemini-4-carbon-ai-model-poised-to-slash-startup-costs, https://dev.to/neuraitool/gemini-4-carbon-googles-1-ai-model-and-the-release-strategy-that-matters-more-than-the-score-55oh, https://dev.to/felipe0liveira/the-frontier-keeps-climbing-but-the-open-weight-gap-is-closing-fast-2k41

### 3. DeepSeek open-sources Super-agent architecture for always-on, multi-task agents (DeepSeek)
DeepSeek's Harness team published a technical article and open prototype (dsh-superagent-prototype) describing a 'Super-agent' design: a two-layer Router/Worker architecture, event-driven triggers, asynchronous multi-channel interaction, separation of compute, state and execution environment, and an external Watchdog for recovery. The team reported an internal instance carrying one task from an IM group chat through GitHub pull-request review, and preliminary experiments on a simulated environment of roughly 300 messages and 20 work requests showing median task completion of 12.4 minutes and 95th percentile of 15.7 minutes, versus 29.5 minutes at the 95th percentile for a single-session-plus-subagent baseline. The team noted token overhead rises without event pass-through and that results come from synthetic, simplified settings.
Why it matters: Moves agent design from single-session chat toward persistent, proactive systems, and releases the architecture openly rather than as a product.
Refs: https://www.sohu.com/a/1095500579_120988576?scm=10001.7746_13-119000.0.0-0-0-0-0.0&spm=smpc.channel_354.block3_32_P7Ovbu_1_fd.12.1793462121955JFhMGrJ_7746, https://www.qbitai.com/2026/10/506904.html, https://www.zhidx.com/p/606311.html

### 4. Epoch AI reports GLM 5.3 autonomously exploited six Firefox releases (GLM)
Epoch AI published an October 30 report saying Zhipu's open-weight GLM 5.3 autonomously wrote attack code against all six stable Firefox releases shipped between September 17 and October 26, 2026, exploiting the 'patch gap' between public security fixes and stable releases. The experiment modeled a low-resource attacker with only public information, capped each attempt at 48 hours (fastest success about 12 hours), and cost more than $100,000 in API fees overall, roughly $1,000 per version once the environment was built. Epoch said no provider safeguards or refusals were triggered, including at Z.ai, and noted the same approach did not succeed against Chrome; all tests ran in an offline simulation. The report did not mention any response from Zhipu.
Why it matters: A concrete demonstration that downloadable open weights can be used for offensive security work beyond provider-level guardrails, sharpening the open-weight safety debate.
Refs: https://news.cocoloop.cn/en/2026/10/glm-53-firefox-patch-gap/, https://aistop.watch/p/one-nation-under-grok?utm_source=%2Finbox&utm_medium=reader2

### 5. Amazon Bedrock adds Kimi K3 and GLM 5.3 open models (Kimi, GLM)
Amazon CEO Andy Jassy said on the October 29 earnings call that Bedrock now offers open-model versions from Chinese developers Kimi and GLM alongside OpenAI and SpaceXAI models, according to call transcripts cited in coverage. Reporting said the open models on Bedrock include Moonshot's Kimi K3 and Z.ai's GLM 5.3, with GLM 5.3 arriving in early October aimed at agentic coding and complex software engineering. Jassy said he expects six to eight models to be roughly comparable over time and that Bedrock input and output are not shared with model providers or used to train foundation models.
Why it matters: Puts Chinese open-weight models into a major Western cloud catalog, a distribution channel that also raises data-handling and provenance questions for enterprise buyers.
Refs: https://www.toutiao.com/article/7702731290101121572/?wid=1793435512785

### 6. Moonshot launches Kimi K3.1 Pro with weights promised by November 4 (Kimi)
Moonshot AI unveiled Kimi K3.1 Pro with a 1-million-token context window, saying it is its most capable 3T-class open-weight release and that full weights would be released by November 4. The model is live across Kimi.ai, Kimi Work, Kimi Code and the Kimi API, with a high-speed variant offering 2-3x faster responses. Moonshot claimed 65.7% on Terminal-Bench 4.0, ahead of GPT-6 Astra's 58.2% and near Claude Opus 5.5's 66.4%, and a Kimi Code Bench 3.0 long-horizon score of 61.2% versus 55.95% for K3. A separate account said Moonshot issued an apology to subscribers on October 26 and granted a 25% monthly quota top-up after complaints about fast quota burn and long execution times, and that the weights had not yet been released as of October 31.
Why it matters: A near-frontier Chinese model whose competitive claim depends on a weight release still pending, with early user friction over quota consumption.
Refs: https://adalytica.com/news/moonshot-ai-kimi-k31-pro-0c93eaff, https://www.ai345.info/post/post-1793422164330, https://dev.to/felipe0liveira/the-frontier-keeps-climbing-but-the-open-weight-gap-is-closing-fast-2k41

### 7. Report alleges DeepSeek and Moonshot used GPT-6 Astra distillation (Kimi, DeepSeek, OpenAI)
The Information reported on October 28, citing people with direct knowledge, that DeepSeek and Moonshot AI leaned heavily on GPT-6 Astra distillation to train their newest models, naming Moonshot's Kimi K3.1 Pro (released October 23) and DeepSeek's upgraded V4.1-Flash 1017 (launched October 17). None of the three companies confirmed the claim, and no logs, account details or data volumes were made public. The report builds on a September 30 OpenAI blog post saying it disrupted a campaign to extract protected reasoning from its models and attributed a core cluster of the activity to individuals associated with Moonshot AI; Moonshot has previously denied that its earlier Kimi K3 was built through distillation.
Why it matters: Turns benchmark competition into a provenance dispute, with commercial and policy stakes for both labs and for OpenAI's lead narrative.
Refs: https://en.shiftdelete.net/gpt-6-astra-distillation/

### 8. OpenAI releases GPT-6.1 Terra for fast, low-cost computer use (OpenAI)
OpenAI released GPT-6.1 Terra, a fast, cost-efficient multimodal model replacing GPT-5.6 Terra, with API prices cut by 50% versus its predecessor and positioned below GPT-6.1 Sol. Coverage reports it is optimized for computer use, visual reasoning and office tasks, scoring about 15 points higher than GPT-5.6 on the Agents' Last Exam benchmark at roughly a third of the cost, matching GPT-6 Astra's computer-use quality at about a tenth of the price per token, and running more than three times faster than Sol and Astra. Reported internal tests cut basic-reasoning error rates from 53.6% to 16.7%, and TerminalBench 4.0 rose from 21.5% to 50.3% at maximum reasoning effort. It is available to Plus, Pro, Enterprise and Edu users via Codex and ChatGPT Work and via the API as gpt-6.1-terra.
Why it matters: Pushes high-volume computer-use automation down the price curve, intensifying cost competition with Anthropic and Google's agentic tiers.
Refs: https://mundobytes.com/en/OpenAI-launches-GPT-6.1-Terra-for-desktop-automation/, https://dev.to/felipe0liveira/the-frontier-keeps-climbing-but-the-open-weight-gap-is-closing-fast-2k41

### 9. OpenAI says ChatGPT will auto-terminate conversations showing violent fixation (OpenAI)
OpenAI said ChatGPT will automatically terminate conversations that exhibit violent fixation, and that if multiple conversations are terminated, an account may be temporarily suspended. The same source's related briefs also describe a community safety report and expanded protections for teens, and a commitment to public safety reporting for teen protection.
Why it matters: A concrete product-level safety intervention with account consequences, extending OpenAI's teen-safety posture into enforcement mechanics.
Refs: https://app.dahecube.com/nweb/pc/spiderdetail.html?spidid=885321?recid=1, https://thewire.ink/sources/openai

### 10. Ex-Meta researcher testified he torrented Books3 and deleted his copy (Meta)
In a joint status report filed with Meta in California federal court, rightsholders said former Meta researcher Stephen Roller admitted in a deposition that he torrented the pirated Books3 dataset and knowingly distributed it while working at Meta between 2017 and 2023, and later deleted his copy 'due to all this litigation.' The plaintiffs also seek an internal 'ML Books' Google Drive folder and records of a Meta book club that may have used shadow-library books, and say Meta has not produced all command-history files from its torrenting servers. Meta disputes the significance, saying Roller did not testify the download was for or at Meta and that the deleted copy was on his personal computer; Meta says it is investigating the folder and has produced substantial logs. The court previously ruled training Llama on books was fair use, leaving the BitTorrent downloads as the main open issue; Entrepreneur's case is set for trial in spring 2027.
Why it matters: Puts the acquisition method, not just the training use, at the center of Meta's copyright exposure, with discovery disputes that could affect its fair-use defense.
Refs: https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/, https://times.hntrends.net/story/50316760?view=reader#discussion, https://news.lavx.hu/zh-Hans/article/qian-meta-yan-jiu-yuan-cheng-ren-tong-guo-zhong-zi-xia-zai-books3-bing-zai-su-song-qi-jian-shan-chu-le-fu-ben

### 11. OpenAI commits to honoring robots.txt AI training signals (OpenAI)
OpenAI said it will honor robots.txt AI training signals, enabling websites to opt out of data collection for model training. The commitment appears alongside other OpenAI policy posts on fair use and an updated Model Spec.
Why it matters: A voluntary crawling concession that shifts some control over training data to publishers without resolving the underlying legal fights.
Refs: https://thewire.ink/sources/openai

### 12. Grok Bot daily actives pass 600,000 after 16 straight days of growth (xAI)
Reports citing Similarweb and other third-party data said Grok Bot's daily active users rose for 16 consecutive days, the longest streak since launch, passing 600,000 by October 26 from under 100,000 in early September and about 155,000 on September 20. The product launched in beta on August 11, 2026 as a task-executing agent rather than a chatbot, with interactive shopping cards, subscription templates and persistent project workspaces. It has no free tier; since October 12 new users could subscribe via X at $30, $100 and $200 monthly tiers. SpaceX president and COO Gwynne Shotwell was cited saying paid weekly active users reached 800,000 by early October, more than double the prior month.
Why it matters: Evidence that a paid-only agent product can scale quickly, a data point for agent monetization amid free-tier competition.
Refs: https://www.ithome.com/1/020/468.htm, https://app.qudong.com/article/528102.html

### 13. xAI to watermark Grok text output for EU AI Act compliance (xAI)
xAI's developer documentation says text responses from supported Grok models will include an invisible watermark starting November 7, 2026, applied during generation by shaping token choices, with no request parameter and an x-watermark response header for checking. The company says it watermarks to comply with the EU AI Act, applies it on every API endpoint, and lets team admins opt out per model in the console, with opt-outs requiring confirmation that a legal exception applies and being recorded in the audit log. Covered models include grok-4.7, grok-4.6, grok-4.5, grok-4.3 and the grok-4.20 variants.
Why it matters: A concrete compliance implementation for AI-content marking, and a test of how much opt-out flexibility regulators will tolerate.
Refs: https://docs.x.ai/developers/advanced-api-usage/watermarking

### 14. DeepMind trains Gemini 3.1 Flash-Lite on simulated patients for psychiatric intake (Google)
A Google DeepMind preprint published October 29, 2026 (arXiv:2610.40476) applied multi-turn reinforcement learning to Gemini 3.1 Flash-Lite using simulated patients, extending the ResidencyRL framework to psychiatry. In a randomized, double-blind crossover OSCE, 32 board-certified psychiatrists preferred the trained agent in 76.7% of paired comparisons (p<0.0001), with alliance and communication at 82.0% versus 65.2% and diagnostic appropriateness at 68.3% versus 33.3%; rubric scores rose from 0.379 to 0.706 across 127 validated scenarios. In 256 adversarial safety scenarios, the share of acute risks the model failed to escalate fell from 30.5% to 12.9% (p<0.0001). The work is a preprint, tested in simulated and examination settings rather than with real patients.
Why it matters: Shows reinforcement learning from simulated interaction improving both clinical performance and a safety metric in a lightweight model, with clear caveats about real-world deployment.
Refs: https://cryptobriefing.com/google-deepmind-gemini-psychiatric-intake-rl/, https://www.bitmart.com/zh-CN/news/detail/deepmind-gemini-3-1-flash-lite-30-5-12-9-163655?slug=latest

## Cross-Org Themes

- Agentic capability is the shared competitive axis: DeepSeek's Super-agent architecture, OpenAI's Terra computer-use model, xAI's Grok Bot and Google's long-horizon Carbon all target sustained autonomous work.
- Access and gating are being renegotiated: Google restricts Carbon to defenders, Amazon Bedrock shelves Chinese open models, and Alibaba puts Qwen inside Apple's China stack.
- Open-weight releases carry unresolved safety and provenance questions, from GLM 5.3's autonomous exploits to Kimi's pending weight drop and distillation allegations.

## Rumors and Unverified Claims

The Information's report that DeepSeek and Moonshot used GPT-6 Astra distillation for V4.1-Flash 1017 and Kimi K3.1 Pro rests on anonymous sources and was not confirmed by OpenAI, DeepSeek or Moonshot. Separately, a social post claimed Anthropic released two new models, Fable 5.5 and a next-generation Opus, into early testing ahead of an IPO, with no official timing or parameters disclosed.

## Takeaway

The decisive variable this cycle is not raw benchmark rank but who can actually use a model and under what conditions, so watch whether Kimi ships its promised weights, whether Google widens Carbon access, and whether Apple's China rollout proceeds on schedule. Provenance and safety claims, including the distillation allegations and the Firefox exploit findings, still need independent confirmation.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
