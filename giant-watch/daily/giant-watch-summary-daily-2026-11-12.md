# Giant Watch Summary - Daily - 2026-11-12

## Headline

Anthropic released Claude Fable 5.2 and Claude Mythos 5.2 with a 20% cut to standard API pricing, while Google DeepMind's Gemini 4 Carbon launch and Gemini Robotics 2.5 rollout made the day a frontier-model race. The episode's throughline is labs pushing flagship capability into longer, multi-agent work and pricing it aggressively.

## Top Developments

### 1. Anthropic launches Claude Fable 5.2 and Claude Mythos 5.2 with lower API pricing (Anthropic)
Anthropic released Claude Fable 5.2 and Claude Mythos 5.2, which it says improve on complex software engineering, long-running tasks and multi-agent collaboration, with output up to 30% faster than 5.1. Standard API pricing is $8 per million input tokens and $40 per million output tokens, 20% below the prior generation, with a 1M-token context and 128K max output. Fable is offered to general users; Mythos is gated to verified cybersecurity and life-sciences organizations.
Why it matters: A flagship model refresh paired with a price cut is the strongest single signal of the day, and the gated Mythos tier shows labs segmenting access by risk domain.
Refs: https://www.exmoo.com/article/267953.html

### 2. Google DeepMind releases Gemini 4 Carbon to developers, enterprises and consumers (Google)
Google DeepMind made Gemini 4 Carbon generally available to developers, enterprises, researchers and consumers, positioning it for complex coding, cybersecurity, scientific reasoning and long-running multi-agent tasks. The report cites first-place results on CursorBench 4.0, Perplexity WANDR and Zapier AutomationBench, with API pricing of $2 per million input and $10 per million output tokens until December 1, when it rises to $4 and $20. Google also previewed a /swarm feature in Antigravity for coordinating multiple agents.
Why it matters: A broad flagship release with benchmark claims and a time-limited promotional price directly competes with Anthropic's same-day model launch.
Refs: https://www.dtinsight.com.cn/sys-nd/4377.html

### 3. Google DeepMind unveils Gemini Robotics 2.5 with a Mercedes-Benz production-line pilot (Google)
Google DeepMind released Gemini Robotics 2.5, which it calls its most capable vision-language-action model, evaluated on more than 200 tasks with success rates 30% to 100% higher and completion times 20% to 30% faster than the previous version. In a proof of concept on active Mercedes-Benz production lines, an Apptronik Apollo 2 humanoid reached a 96% success rate sorting automotive parts. DeepMind also introduced the ASIMOV-Jailbreak benchmark and released AlphaGenome 2, a gene-prediction model not approved for clinical use.
Why it matters: The Mercedes pilot is a concrete real-world deployment datapoint for embodied AI, though the sources stress it is a proof of concept rather than commercial results.
Refs: https://www.digitaltoday.co.kr/en/view/124565/google-deepmind-launches-gemini-robotics-2-5, https://www.digitaltoday.co.kr/cn/view/124587/google-deepmind-launches-gemini-robotics-2-5, https://www.gatenode.irish/zh-tw/news/detail/GOOGL/google-deepmind-releases-gemini-robotics-25-and-alphagenome-2-ai-models-25567838, https://xiaohu.ai/en/article/gemini-robotics-2-5/

### 4. Security researchers find Grok Build apps exposing confidential data, including SpaceXSI's own (xAI)
Security firm Claroc reported that Grok Build's link-sharing design lets outsiders enumerate thousands of published apps, with roughly 650 to 800 estimated to contain private data. Exposed material reportedly includes SpaceXSI and X internal sales tools and onboarding plans, a Tesla service-center scorecard, a naval contractor personnel list and patient records. Claroc says the publishing panel pre-selects 'anyone with the link'; SpaceXSI said apps are private before sharing and took its 24 apps offline after press inquiries.
Why it matters: A named security incident with a documented default-permissions dispute is the day's most consequential negative signal and a test case for agent-built app platforms.
Refs: https://www.zhiding.cn/network_security/2026/1112/3205666.shtml, https://eu.36kr.com/en/p/4066243326579591

### 5. xAI releases Grok Bot 1.0 with shared Team Bots (xAI)
xAI launched Grok Bot 1.0, upgrading the beta from a personal assistant to shared Team Bots that can be added to Slack, Microsoft Teams and video meetings, track ongoing projects and proactively take on work. The release adds permission-respecting access, confirmation before sensitive actions and admin controls, plus improved browser operation and document generation. Team Bots are limited to Team and Enterprise plans; meeting features cover Team, Enterprise and Ultra.
Why it matters: A direct move into the collaborative 'AI coworker' category, competing with office-suite agents from Anthropic, Google and Microsoft.
Refs: https://www.jiqizhixin.com/articles/2026-11-12-11

### 6. Anthropic expands Claude into an office suite with Sheets, Whiteboards, Meetings and Data (Anthropic)
Anthropic announced Claude Sheets, Claude Whiteboards and Claude Meetings, and formally launched Claude Data (renamed from Claude Dashboards). Sheets builds spreadsheets from plain language and exports to Excel or CSV but is described as not yet suited to complex financial models; Meetings is in testing with Team and Enterprise customers on Google Meet. Claude also added connections to Adobe, Atlassian and HubSpot.
Why it matters: Moves Claude from a developer tool toward a broad professional platform, putting Anthropic in direct competition with Microsoft 365 and Google Workspace.
Refs: https://www.vietnam.vn/en/anthropic-mo-rong-claude-thanh-bo-cong-cu-van-phong-ai

### 7. Alibaba releases Qwen4-Max preview with a Token Plan subscription (Qwen)
Alibaba released the Qwen4-Max preview, its fourth-generation flagship, with a 1M-token context and text, image and video input, aimed at complex coding, long agentic tasks and professional office work. It is available only through the new Token Plan subscription, not pay-as-you-go, with a preview window from November 11 to November 25 after which the model identifier is retired. Parameter counts, benchmark scores and final pricing were not disclosed.
Why it matters: A flagship Chinese model launch with an unusual subscription-only access model and a short preview window that forces integrators to plan migrations.
Refs: https://developer.aliyun.com/article/1782441, https://www.163.com/dy/article/LBHGOS0C05568W0A.html?spss=dy_author

### 8. DeepSeek Harness adds AgentTeam in a v0.2.2 preview (DeepSeek)
DeepSeek's Harness shipped a v0.2.2-rc.2 preview that lets users enable AgentTeam per session, view team members and tasks in one panel, and let sub-agents be named and organized hierarchically. A DeepSeek product team member described a two-layer Router/Worker architecture and said cross-session long-term memory is not yet built in but may be close. The Super-agent work is described as still in prototype exploration, running only in a small internal trusted environment.
Why it matters: Shows a Chinese lab iterating on multi-agent orchestration tooling, though the headline capability remains a prototype.
Refs: https://aiorang.com/article/kamOhBw.html

### 9. HSBC cuts Z.AI target price, tying upside to the next GLM release (GLM)
HSBC lowered its Z.AI target price from HK$1,375 to HK$500 and kept a Hold rating, cutting 2027-2028 ARR and revenue forecasts by 7% to 27% and non-IFRS operating margin forecasts by 15 to 19 points. The note attributes pressure to intensifying competition including price cuts from Anthropic and OpenAI, rising R&D costs and longer model cycles at Chinese labs, and says ARR upside depends on the expected November GLM-5.5 release. It also cites a HK$4 billion buyback announced November 10 and a November 6 partnership with China Mobile.
Why it matters: An analyst view that explicitly links a Chinese lab's growth to competitive pricing pressure from US frontier labs.
Refs: https://news.futunn.com/post/1004283187/zai-2513-hk-hold-upside-to-growth-hinges-on-the, https://news.futunn.com/hk/post/1004283187/zai-2513-hk-hold-upside-to-growth-hinges-on-the?level=0&global_content=%7B%22promote_content%22%3A%22nn%3A1004283187%22%7D

## Cross-Org Themes

- Flagship model refreshes paired with aggressive or promotional pricing
- Push from single-turn assistants toward multi-agent, long-running work
- AI moving into shared team and office workflows

## Rumors and Unverified Claims

A Hugging Face page describes a community 'no-refusal' derivative of DeepSeek-V4.1-Flash-1017 with self-reported benchmark and refusal figures; it is an unofficial third-party release, not a DeepSeek announcement. A FourWeekMBA article about 'Deletion Tuning' on Meta's Llama 3 8B is an NYU and University of Calgary paper, and the article states the paper does not say whether Meta uses the method. A Vercel AI Gateway report and a Langfuse report contain adoption and spend statistics that are third-party analyses rather than company announcements.

## Takeaway

The competitive axis this week is less raw capability than price and access terms, so watch whether Google's December 1 price increase and Qwen's November 25 preview retirement hold, and whether the Grok Build default-permission dispute produces platform changes.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
