# Behavioral Interview Answers

*Merged from: behave_questions.md, behavioral_interview_70_questions.md, self-intro.md, critical_thinking.md. Updated after the Revolut Applied AI recruiter screen (Oct 28, 2026): new Revolut section added, generic answers tailored.*

---

## STAR Technique

- **S**ituation
- **T**ask
- **A**ction
- **R**esults

Give specific examples and describe how you gathered, analyzed, prioritized, and communicated information. The STAR framework gives your answer structure and makes it easier for the interviewer to follow your story.

---

## Resources

*   [Yuriy Kashnitskiy: behavioral questions](https://www.linkedin.com/feed/update/urn:li:activity:7210627927418245120/)
*   [Behavioral Interview Post](https://www.linkedin.com/feed/update/urn:li:activity:7067921863519129601)
*   [Revolut — Our culture (5 values)](https://www.revolut.com/our-culture)

---

## Revolut — Applied AI Engineer: Interview Q&A

### Recruiter screen — questions and model answers (continued)

#### Walk me through your background (60–90 seconds)

I'm an ML engineer with 5+ years of experience in entertainment, e-commerce and ride-hailing, in startups and in large companies. My strength is owning the whole cycle: framing the problem with product, building the data pipeline, modeling in Python and SQL, deploying the service and running the experiment.

Now I lead the Safety AI team at inDrive, a global ride-hailing platform, similar to Uber, with 3 ML engineers whom I hired. We built a model that scores a trip for risk *before* it starts: if the score is high, the driver or passenger gets an additional check. We went from idea to experiment in two quarters, and in the Peru pilot incidents went down by [X%]. Now we're scaling it to the whole network. I also built a CV-based liveness detection service and an incident-ranking service that lets incident managers review the most serious cases first.

Most of my production work is classical ML. On the GenAI side I've built [a PydanticAI multi-agent assistant that creates delivery orders in WhatsApp, a RAG shopping assistant, and LLM-based Jira standup automation]. That's why Applied AI fits me: product thinking plus hands-on building, in a domain like fincrime where ML reduces real harm.

*Tips:* define the product in one clause ("ride-hailing, like Uber") so the recruiter doesn't have to ask. Finish with the link to the role. Keep sentences short.

#### Tell me about the project with the biggest business impact: problem, solution, impact.

**Option A (stronger: it has finished experiment results) — Safety risk scoring**
- **Situation:** in LATAM, serious incidents (robbery, assault attempts) happen during trips, and support could only react after the fact.
- **Task:** I led the team to detect risky trips *before* they start.
- **Action:** framed the problem with product, built the data pipeline and the model that scores each trip, defined what happens at a high score (extra check for the driver or passenger), deployed the service on live traffic, and designed the A/B experiment in Peru.
- **Result:** the experiment finished last month with positive results: incidents went down by [X%], with [guardrail, e.g. share of trips getting extra checks / conversion impact: X%]. The estimated saving is roughly [X] per month in insurance and legal costs. We're now scaling to the whole network.

**Option B — Incident moderation (ranking) service**
- **Situation:** inDrive gets a large flow of safety appeals, and incident managers review them manually. Serious cases (robbery, violence) waited in the same queue as minor ones, which means slower response and higher insurance and legal cost.
- **Task:** prioritize the queue so managers see the most serious incidents first.
- **Action:** my team and I built a ranking service that scores every appeal by severity; I designed the data preparation pipeline and the inference service, and agreed the API contract with the backend team.
- **Result:** offline, the model reaches recall of about 0.8 on serious incidents within the top [X%] of the queue, versus about [baseline] if managers review in chronological order. That means the same coverage with [X%] fewer reviews, roughly [X] hours saved. The A/B test is running; the key metrics are time-to-review for serious cases and handling cost.

*Avoid:* "give me a second", and giving recall without baseline, volume or business meaning.

#### Do you have specific business metrics, like revenue generated or cost saved?

The experiment for the ranking service is still running, so I can't share final online numbers. But I built the business case with a back-of-the-envelope model: [appeals per day] × [share of serious incidents] × [average cost of a serious incident: insurance, legal] × [share we now handle faster]. That gives roughly [X] per month, plus about [X] reviewer hours saved. For the safety scoring project, incidents in the Peru pilot went down by [X%].

*Avoid:* "I don't have any specific numbers". For a role built on unit economics this is the most damaging answer. An approximate, labeled estimate is far better than none.

#### How did the idea originate? Did it come from product, or from you?

The PM raised the pain point: the incident queue was not prioritized. Then I took the lead on discovery. I ran kickoffs with the PM and the incident managers to understand how they judge severity, turned that into features, and proposed *ranking* instead of classification, because the managers' capacity is fixed. I defined the success metric, built the pipeline and the service, and agreed the contract with backend. In this role I want to do the same from the very start, including finding the opportunity myself.

#### Why are you looking outside your current company, and what do you want in the new place?

I'm proud of what we built at inDrive, and I want the next step. First, scope: I want to own the whole product cycle, from finding the opportunity to the pitch, and use GenAI/LLMs to move core metrics. Second, domain: safety work showed me I do my best work where ML directly reduces harm, and fraud and financial crime at Revolut is the same logic at a larger scale, with rich transaction data. Third, relocation: inDrive supports relocation only to Cyprus or Serbia, while a hub like the UAE or London fits my plans.

*Avoid:* calling your previous work (the recommender system) unimportant. Say "this work has a more direct impact" instead.

#### Tell me about your management experience.

For the first two quarters at inDrive I was an individual contributor, then I became the lead of 3 ML engineers, and I hired the whole team. I set priorities and the roadmap together with product, review designs, mentor, and stay hands-on. Under this setup we shipped [two] products to experiment within [X months]. Earlier I led teams of 3 to 11 people, including hiring, offboarding, and quarterly planning.

#### Do you have any questions for us? (never answer "no")

Pick 2–3:
- Which business verticals are open for this role right now, and how is the vertical chosen?
- What does success look like in the first 6 months? How many POCs usually reach leadership buy-in?
- What is the LLM stack and tooling the team uses (models, evals, infra budget)?
- What do visa and relocation support look like for the UAE / UK?
- Any tips for the business problem-solving and ML fundamentals rounds?

#### What are your salary expectations?

*(Likely asked in a later call; recruiter said they'd "catch up on other details later".)* Based on the market for this level in [UAE/UK] I'm targeting [range]. I'm flexible depending on the total package. Could you share the range for this role? *Research the range first; don't give a number you haven't checked.*

#### Are you interviewing with other companies?

I'm talking to a few companies, but Revolut is a top choice for me because of the ownership model and the fincrime domain. I can move fast: my notice period is one month.

*(Say this only if it's true.)*

#### Last time the case round didn't go well. What's different now?

Last time the format was new to me. Since then I've practiced it with a clear structure: clarify the goal, size the opportunity, ask for the data, build the solution, check unit economics, and name risks. I've also run more business-impact projects at work, where I had to estimate the value before building.

#### What GenAI / LLM experience do you have?

I've built three things. First, a RAG shopping assistant at Sweed that helps customers fill their carts, prototyped with scraped competitor product data when our own catalog lacked rich descriptions; the demo led to a catalog enrichment initiative. Second, a PydanticAI multi-agent framework that creates delivery orders from WhatsApp chats. Third, an LLM-based Jira analysis that automates our daily standup. [Add: how you evaluated quality, cost per request, and what you'd improve.] My production ML is mostly classical, so GenAI is where I'm growing fastest, and this role is the way to apply it at scale.

---

### Applied AI role — additional behavioral questions

#### Tell me about a time you owned a product from idea to production, almost alone.

*Use the safety risk scoring story:* the research idea became a system on live traffic. Highlight what *you* personally did: problem framing with product, data pipeline, model, service, experiment design, rollout. Close with the result [X%] and what you'd do differently (for example: involve backend and support earlier, set guardrail metrics from day one).

#### Tell me about a time you built a POC with minimal resources and pitched it.

- **Situation:** at Sweed we wanted a conversational shopping assistant, but our product catalog had no rich text descriptions.
- **Action:** I built a RAG prototype in [X weeks] alone, and to prove the full experience I used scraped competitor data strictly for prototyping.
- **Result:** the demo impressed stakeholders and started a discussion on systematically enriching our own catalog. Close with the lesson: prove value cheaply, then ask for resources.

*Optional:* add one line on the cost of the prototype (for example, LLM cost per conversation of [X]) to show the unit-economics mindset.

#### How do you validate an AI idea with unit economics?

I use four lines: **value per case × volume × expected lift − cost = monthly value**, then payback time.
- *Value per case:* cost of an incident, a fraud loss, an analyst hour, a support contact.
- *Volume:* cases per day in the chosen vertical.
- *Lift:* how much better than today's process (get a baseline first; assume a range, not a point).
- *Cost:* LLM tokens (tokens per request × price × requests), infra, human review for edge cases, maintenance.

Then I test the sensitivity (what if lift is half?), define kill criteria, and build the cheapest POC that can measure the lift. Example: for incident ranking, [appeals/day] × [share of serious] × [cost per serious incident] × [share handled faster] − [infra + maintenance].

#### Tell me about a time you pitched an idea to senior leadership and got buy-in.

*Use the scaling of safety scoring from the Peru pilot to the whole network.* Structure of the pitch: problem and metric → prototype or experiment result → unit economics → risks and guardrails → the ask (people, budget, timeline). Mention what leadership challenged and how you answered it. [Add a real example of the questions they asked.]

#### Tell me about a time you went above and beyond. (Bar Raiser)

*Story: the daily standup bot (details in product_idea.md).*

- **Situation:** our daily standups started with people reading through Jira and reporting status by hand. Task descriptions were often incomplete (no current state, target state or action plan), and the team lead had to chase people for updates. It was not my job as an ML tech lead, and nobody asked me to fix it.
- **Task:** remove this routine and make task quality visible, without adding a new tool or a new process for people.
- **Action:** on my own initiative, I built a bot that runs on schedule every weekday (skips weekends). It:
  - fetches the active tasks from a configured Jira filter, excluding epics;
  - posts the standup reminder to the team's Slack channel, with tasks grouped by assignee and people mentioned by Slack ID;
  - analyzes each task with an LLM (Gemini via Vertex AI, temperature 0.1, structured output with a Pydantic schema): is the current state, target state and action plan complete, is there recent activity and comment progress;
  - posts feedback in a thread, with a ready-to-send message to the assignee, only for tasks that need action;
  - posts an "all clear" message that mentions the team lead when everything is fine.
  
  I used structured JSON output (decision, findings, required actions, `is_action_required`) so the reports are consistent and easy to check, plus retries with exponential backoff for reliability. I built it with a cheap model and in my spare time, so the running cost is very low [add: about $X per month].
- **Result:** [X minutes saved per person per day / X% of tasks now with a complete plan / the team lead no longer chases updates / the team adopted it]. It became a reusable pattern for [other teams / other Jira filters], because the filter and the channel are configurable.
- **Lesson:** look for leverage beyond my own task list, start with a small working version, and use LLMs where the work is repetitive and judgment is simple.

*Why it fits Revolut:* it shows ownership without being asked (Get It Done), a simple product that makes colleagues' work easier (Deliver WOW), and a lean GenAI POC that solved a real process problem. *Be ready for follow-ups:* how you evaluated the LLM's decisions (false alarms vs missed tasks), how you chose the model and the cost per run, and what you'd improve next (for example, an eval set with human labels).

*Alternative (shorter, if the interviewer wants a second example):* the PydanticAI multi-agent framework that creates delivery orders from WhatsApp chats.

#### Tell me about a time a model looked good offline but disappointed in production.

*Use the Recall@5 story:* offline metrics were fine, but production Recall@5 was lower. I segmented by user cohort, found un-authorized users with very low metrics, traced it to feedback (likes) not being sent to Kafka for them, wrote a bug report, and the fix restored performance. Lesson (relevant to the ranking service, which has offline metrics only): define online metrics and segment checks *before* launch.

#### How do you handle the trade-off between catching fraud/risk and hurting good users? (false positives)

In safety scoring the action at a high score is an *additional check*, not a ban, so a false positive costs friction instead of a lost customer. I pick the threshold by comparing the cost of friction with the cost of a missed incident, track guardrail metrics (conversion, share of trips with checks, complaint rate), keep humans in the loop for the highest-impact decisions, and monitor drift by segment. [Add a real number: share of trips checked, or conversion impact.] The same logic applies to fincrime alerts.

#### Tell me about how you hired your team. What do you look for? (Dream Team)

I hired all 3 engineers on my team. *(Adjust to what you really did.)* I defined the profile first (what the team lacked), used [take-home / technical / system design / behavioral stages], and looked for three things: [solid fundamentals, ownership, communication]. I held the bar even when it slowed hiring, because [one sentence on what it gave you: for example, the team shipped X without hand-holding].

#### Tell me about a time you gave candid, difficult feedback. (Dream Team)

Use the SBI structure: **S**ituation (specific moment), **B**ehavior (what you saw, no judgement), **I**mpact (effect on team or product), then agree the next step. [Add a real example with the result.] Also show you recognize good work: you are deliberately working on giving positive feedback too.

#### Tell me about a time you were not satisfied with a "good enough" result. (Never Settle)

We could have stopped with an offline model for safety scoring. I pushed to deploy it on live traffic, run a real experiment in Peru, measure incidents instead of proxy metrics, and then scale it to the whole network. [Add one detail on what you improved after the first results.]

#### Where could LLMs create leverage in fincrime? (case prep, role-specific)

Present these as *hypotheses to validate*, not facts:
1. **Alert triage and summarization:** an LLM summarizes the case and evidence for an analyst; metric: handling time per alert. This mirrors your incident-ranking service (prioritize first, then speed up the review).
2. **Prioritization of alert queues:** the same ranking idea as incident moderation; metric: share of serious cases found in the top [X%] of the queue.
3. **Analyst copilot** for investigation notes and SAR/report drafting; metric: hours saved per case, quality checked by sampling.

For each: first ask for the baseline (volume, cost per case, current false-positive rate), then run the unit-economics test above.

---

### Mistakes from the Oct 28 screen — don't repeat

1. No numbers for business impact. Always bring a figure or a labeled estimate.
2. Not one mention of GenAI/LLMs, which is the core of the role. Mention it in the intro and in "why this role".
3. Negatives: "I really don't want to go back to Cyprus", "last time I failed", calling your previous project unimportant.
4. No questions at the end. Always ask 2–3.
5. Filler and long explanations ("how to say", "give me a second", explaining what ride-hailing is). Use short sentences and structure answers in 3 parts: situation → what I did → result.
6. Receiving the idea instead of originating it. Stress discovery, framing and ownership.

---

## Self-Introduction — Experience Overview

I am a machine learning engineer with over 5 years of experience. I have worked on a wide range of projects across various industries — including online cinema, entertainment, ride-hailing, and e-commerce — and within companies of all sizes, from early-stage startups to global enterprises. I've gained valuable experience in machine learning engineering, particularly in recommender systems and safety scoring models. I have a strong understanding of machine learning algorithms and hands-on experience with SQL and Python. I'm also skilled in data cleaning and transformation. On the GenAI side I've built LLM-based agents and a RAG assistant (see below), and I like owning a product from the first idea to production.

I used to lead cross-functional teams ranging from 3 to 11 contributors. I've been responsible for hiring and offboarding team members, as well as mentoring them to support their growth and career development. I was also responsible for stakeholder management and for preparing annual and quarterly plans for my team, aligning them with company-wide quarterly goals.

### Current Role
I currently work as a Safety AI Tech Lead at inDrive. My team builds ML solutions for trip monitoring, safety scoring, and liveness checks, with the overarching goal of reducing safety incidents on the platform.

As a hands-on tech lead:
*   Turned safety risk scoring from a research idea into a production-ready system that handles live traffic. It scores a trip for risk before it starts; the Peru pilot reduced incidents by [X%] and it is now being scaled to the whole network.
*   Built a CV-based liveness detection service.
*   Built an incident-ranking service that puts serious appeals (robbery, violence) at the top of the incident managers' queue (offline recall about 0.8; online experiment running).
*   Hired the whole team of 3 ML engineers.

As an individual contributor:
*   Designed a PydanticAI-based multi-agent framework that automates delivery order creation via WhatsApp chat.
*   Automated the daily standup routine with LLM-based Jira task analysis.

### Previous Experience

**ivi (Online Cinema)**
I started out as a data analyst at an online cinema called ivi, which is similar to the Russian version of Netflix. That role helped me gain hands-on experience with visualization, data cleansing, and BI tools like Tableau and PowerBI. I provided actionable insights to the business based on my analysis. Although my background is in data analysis, I've always had a strong interest in data science and machine learning. As I took on more responsibility, I was promoted to Senior machine learning engineer.

**FunCorp (Entertainment)**
At FunCorp, I led a team of four ML engineers building a personalized feed of funny videos and images. I collaborated closely with the Chief Product Officer and Chief Analyst. One of our main achievements was building and launching a classic two-stage recommender system.

**inDrive (Ride-Hailing)**
After FunCorp, I worked as a data scientist at inDrive, a global ride-hailing company, where I gathered, analyzed, and interpreted driver-rider matching data to support product owners in improving the dispatch algorithm. I was part of a product team of four, with a primary focus on optimizing the marketplace. My main responsibility was managing the entire data preparation pipeline. The ML launch led to an impressive 7% improvement in our North Star metric.

I worked with Google Cloud Platform, particularly leveraging tools like KubeFlow and BigQuery. A significant project I undertook was the development of a driver-rider matching algorithm. I also worked on enhancing a CatBoost model by introducing new features based on geo-points, designing and implementing a Kubeflow pipeline.

**Sweed (E-commerce)**
After inDrive, I joined Sweed, a small e-commerce technology company, as a Staff ML engineer. In this role, I implemented models for inventory management, an AI shopping assistant, and a churn prediction classifier. I then returned to inDrive to lead the Safety AI direction.

### Strengths
*   Proactivity & Innovation
*   Experimentation & Metrics-Driven Approach
*   Cross-Functional Collaboration & Communication
*   Strong ML/AI Expertise
*   End-to-end Ownership (idea → pipeline → service → experiment → business case)

### Weaknesses
*   **Depth in deep learning / LLM internals:** Most of my production work is classical ML, although I've also shipped a CV-based liveness service and LLM agents. I'm deepening the foundations (LLM evaluation, fine-tuning, [what you are studying now]) through hands-on projects, and for an Applied AI role I treat it as my main growth area.
*   **Giving Feedback:** Another area I'm working on is giving positive feedback to colleagues. While I naturally focus on problem-solving and areas for improvement, I've realized the importance of recognizing what's going well. I'm becoming more intentional about expressing appreciation.

### Closing Statements
*   I think my skills and experience make me a good fit for the job.
*   Recently I took a course on Data Engineering, which I found really useful.
*   I am excited about this new position which lets me blend all of my previous experience and grow as a machine learning engineer.
*   I hope to see myself progressing to a senior role where I can mentor colleagues, have a greater impact, and continue to grow professionally.

---

## Personal Behavioral Answers

### Give an example of a challenging project.

One of the most challenging projects I worked on was building an AI-powered shopping assistant. AI assistant was designed to help customers fill their carts through a conversational interface. My goal was to implement a solution that could understand user intent and suggest relevant products in real-time, effectively simulating a human-like shopping experience. I decided to use a Retrieval-Augmented Generation (RAG) architecture for the assistant. However, I quickly ran into a major roadblock: our internal product database lacked rich text descriptions, which are essential for generating meaningful, context-aware chatbot responses. To work around this, I proposed and implemented a solution to scrape product data from a competitor's site — strictly for prototyping purposes. This gave us access to richer content that I could use to power the assistant and demonstrate the full potential of the experience. The prototype was a success and impressed our stakeholders during the demo. As a result, we began broader discussions on how to systematically enrich our own product catalog to support future ML and conversational use cases. It turned a technical challenge into an opportunity for long-term product improvement.

### Describe a time when you had to solve a complex technical problem.

While working on a data pipeline, I noticed a sudden spike in job failures, impacting downstream analytics. I needed to diagnose and fix the issue quickly to restore data flow. I analyzed logs, identified a memory leak due to unoptimized batch processing, and rewrote the job to use micro-batches and replace Pandas with Polars with better memory management. Failures dropped to zero, processing time improved by 40%, and I documented the fix to prevent recurrence.

### What is your greatest strength?

One of my greatest strengths is my ability to quickly gather business requirements and deliver working solutions fast. I focus on understanding the core problem and avoid over-engineering, which helps me move quickly and iterate based on real feedback. I follow a 'fail fast' mindset — getting something functional out early allows me to validate assumptions, adjust course if needed, and ultimately deliver better results in less time.

### What's your greatest weakness?

One area I've been working on is improving my concentration when handling multiple tasks. I've noticed that when I have several things on my plate, I sometimes switch between them too frequently, which affects my focus. To manage this, I've started using the Pomodoro technique — it helps me stay locked in on one task at a time and maintain better productivity throughout the day.

### Team work: Tell me about a time when you faced a problem you couldn't solve yourself.

Early in my career, I encountered a complex data quality issue that was affecting our training pipeline. The training dataset prepared from ClickHouse has fewer rows per day than the Kafka data source, indicating a bug in our Kafka data preparation pipeline. Despite multiple attempts, I couldn't identify the root cause alone. I realized that support from a data engineering team was necessary, so I approached senior team members and proposed forming a cross-functional task force to investigate further. By leveraging their expertise and collaborative problem-solving, we were able to uncover a system integration issue that was corrupting our data. This experience taught me the value of teamwork and diverse perspectives in overcoming challenges. The root cause was related to how we handled unregistered users.

### Communication: Tell me about a time when it was hard to communicate the importance of the task to the tech team?

In a past role as a data team product owner, I was responsible for setting up new data governance rules. To make it work, I needed support from the tech team to follow data rules and standards. Initially, I faced resistance as the tech team prioritized other pressing issues. To communicate the importance effectively, I scheduled a series of one-on-one meetings with key stakeholders from the tech team. During these meetings, I emphasized how improved data governance would streamline workflows and enhance data reliability for their projects. By demonstrating empathy and aligning the benefits with their goals, I successfully gained their support and cooperation.

### Handling Negative Feedback: Tell me about a time when you got negative feedback.

During a project presentation, I received constructive feedback from stakeholders regarding the visual clarity of our data visualizations. Initially, I felt disappointed as I had put significant effort into the design. However, I recognized the opportunity to improve. I scheduled a follow-up meeting with the stakeholders to delve deeper into their expectations and preferences. I then revised the visualizations accordingly, incorporating their feedback. This experience reinforced my belief in the value of iterative improvement and listening actively to stakeholder needs.

### Anticipating Problems: Tell me about a time when you anticipated potential problems and developed steps to avoid them.

In a data migration project, I proactively anticipated potential data integrity issues due to the complexity of merging legacy databases. To mitigate risks, I conducted thorough data profiling and developed a comprehensive data validation plan before initiating the migration. This involved running extensive data quality checks and creating fallback strategies in case of discrepancies. As a result, we successfully completed the migration within the timeline and minimized disruptions to business operations.

### Challenging situation: metrics drop investigation

In my previous role as a data analyst, we noticed a significant drop in our metric for recommended item views. Upon investigation, we found that this decline was specifically associated with certain dates. I started by grouping the data by 'app_version' attribute and discovered a pattern — the metrics dropped on specific dates that coincided with the release of new application versions. We then worked closely with the application development team to identify and rectify the issues within the new releases. After rectifying the issues, our metrics showed a significant recovery. This incident highlighted the importance of thorough checks and test runs before releasing any new application versions.

### Challenging situation: Recall@5 metric investigation

I was responsible for developing and monitoring the performance of a recommendation system in a production environment. Upon deployment, the Recall@5 metric in production was showing lower values than expected. I investigated and identified a specific cohort of users — un-authorized users — experiencing low metrics. Further analysis revealed that for this cohort, feedback data (content likes) was not being sent to Kafka, causing the recommendation system to perform poorly for these users. I documented my findings and wrote a detailed bug report. The development team implemented a fix, ensuring that the feedback data for un-authorized users was correctly sent to Kafka, leading to improved performance.

### Tell me about a time you failed and what you learned from it.

I joined the company as the ML team lead, having been informed during the hiring process that the current lead would receive a promotion to the next grade. However, upon starting the role, I discovered that the promised promotion for the current lead did not materialize, and they continued with daily responsibilities. I assessed my career goals and ambitions, considering the option to become a senior engineer instead of staying in a leadership role without the promised promotion. Recognizing my desire for people management and the potential limitations of my current position, I made the decision to leave the company. This choice allowed me to explore opportunities elsewhere where I could contribute to both technical and leadership aspects, aligning with my career goals.

### Adapting to Changing Requirements.

In a previous role as a product manager, I faced a tight deadline when a client requested a tool to monitor out-of-stock inventory items. Unfortunately, our frontend engineer left the company just as the deadline was approaching. To meet the client's needs, I proposed an alternative solution. Instead of developing a full web application, I offered a pre-configured report with the necessary columns. This allowed us to deliver the core functionality without the complexity of building an interface from scratch, and we met the deadline.

### Give an example of how you handled tight deadlines.

In one of my projects, I was expected to deliver a machine learning–based assistant that could suggest relevant items to users. The timeline was very tight. Instead of going the ML route right away, I assessed the available tools and realized we already had a well-structured ElasticSearch setup in place. I decided to reuse it and built a lightweight layer that translated user input into search queries. By tuning the query scoring and leveraging full-text search with filters, I was able to get relevant results without building a model. I delivered a fully working assistant ahead of the deadline.

### Tell me about a time when you had to deliver a project under a tight deadline.

A product team needed a last-minute feature for a major launch, but we had only a week to implement it. I collaborated with stakeholders to prioritize essential functionality, used feature flags to roll out changes incrementally, and worked with QA to parallelize testing. The feature launched on time with no critical bugs, and the approach became a template for future urgent tasks.

### Give an example of a time you had to troubleshoot a production issue.

A real-time recommendation engine started returning empty results, impacting user engagement. I traced logs, found a mismatch between the indexing process and the query format, and deployed a hotfix while reindexing the data. The system recovered within an hour, and I later improved our CI/CD pipeline to catch such issues earlier.

### Describe a time when you had to manage a difficult stakeholder.

A client insisted on an unrealistic feature that would have delayed the project significantly. I presented alternative approaches, backed by impact analysis, and proposed a phased rollout with incremental improvements. The client agreed to a compromise, and we delivered an MVP on time while planning further enhancements.

### Learning a New Technology Quickly.

Our analytics team adopted Polars, but no one had prior experience. I had to quickly get up to speed and help the team integrate it. I used Claude to rewrite current pandas pipeline using polars. We successfully deployed our first Polars pipeline, reducing memory pressure by 60%.

### Describe a time when you had to mediate a conflict between team members.

Two engineers disagreed on whether to use Airflow or Dagster for a new data ingestion pipeline. I organized a structured debate, gathered performance benchmarks, and facilitated consensus-building. We chose Dagster for simplicity, and the decision process improved team collaboration.

### Have you ever optimized a system for better performance?

A batch job processing user transactions was taking over 12 hours to complete. I identified bottlenecks, parallelized processing, and optimized database queries. Processing time dropped to 2 hours, improving data freshness for stakeholders.

### Have you ever dealt with a security vulnerability?

A routine audit uncovered a misconfigured S3 bucket exposing user data. I restricted access, rotated credentials, and implemented automated security scanning. No data was compromised, and security audits became part of our development lifecycle.

### Have you ever improved a process in your workplace?

We had a custom reporting system, and every new report request created a heavy workload for both designers and front-end developers. I proposed building an MVP version of the reports using Metabase, an open-source analytics tool. This allowed us to quickly generate visualizations and dashboards without involving design or front-end teams. Stakeholders were able to explore data on their own, it reduced custom report requests, and gave the team more time for higher-impact work.

### Why did you leave your previous job?

I left my previous role because machine learning was not the core of the product there, and ML tasks were often de-prioritized in favor of other initiatives. I wanted an environment where ML directly drives business outcomes, and that's what I found in the Safety AI direction.

*For "why are you leaving inDrive now", use the answer in the Revolut section above.*

### Describe a situation where you had to work with a difficult coworker.

In my previous role, I worked with a colleague who frequently scheduled same-day meetings without prior notice. This made it challenging to prepare and often disrupted focused work. I initiated a one-on-one conversation and explained that having a clear agenda and at least a day's notice would help make our meetings more productive. We agreed on communication guidelines, and our collaboration became much smoother.

### What's your leadership style?

I would describe my leadership style as results-oriented. I believe that effort is important, but ultimately it's the outcomes that matter. I focus on empowering team members to make decisions within their areas of expertise while providing clear guidance and support. I emphasize setting measurable goals and regularly tracking progress. I hired my whole team of 3, and I stay hands-on enough to review designs and code while owning priorities and the roadmap together with product.

### How do you stay updated with industry trends?

I stay updated by following thought leaders on LinkedIn and subscribing to several high-quality Substack newsletters covering AI, data science, and product strategy. I'm also active in professional communities. Additionally, I take online courses and certifications — especially in the GenAI space.

### Why do you want to work here?

*Revolut version:* Three reasons. First, the role: owning the product cycle from discovery to a pitch, with GenAI/LLMs and unit economics, is exactly the next step after leading a team and shipping ML products. Second, the domain: my safety work showed me I do my best work where ML reduces real harm, and fincrime at Revolut is the same logic at a larger scale, with rich transaction data. Third, the standard: your values (Never Settle, Get It Done) match how I work, and the relocation to a hub like the UAE or London fits my plans.

*Generic version (other companies):* I want to work here because I admire your focus on innovation and making a difference. I've heard great things about how you support employee growth, which fits well with my career goals. [Add 1–2 company-specific facts.]

### What is your preferred work style?

I'm mostly a team player. I believe teamwork brings more value than working alone. My approach is to build an MVP on my own first, and then collaborate closely with the team to bring it to production.

### How do you handle ambiguity and uncertainty in a project?

I thrive in ambiguous situations by breaking down complex problems into smaller, manageable tasks. I do thorough research and consult with team members to gather insights and make informed decisions. My ability to stay adaptable and calm under uncertainty has helped me navigate challenging projects successfully.

### Describe a situation where you had to persuade a team to adopt your idea.

In a previous role, I proposed a new way to store SQL templates for research purposes — storing them in SQL files instead of Jupyter notebooks. I prepared a demo to highlight the benefits, presented a clear plan for updating the entire codebase, and encouraged team members to share their input. We made our research repo more organized and structured.

### How do you prioritize tasks when you have multiple deadlines?

I prioritize by evaluating urgency and importance. I create a task list, set deadlines, and break larger projects into smaller steps. I confirm my priorities with stakeholders, delegate when possible, and conduct regular progress checks.

### Can you discuss a time when you had to make a difficult decision at work?

I was once tasked with deciding how to run an A/B testing system: either adapt an existing solution or develop our own. After conducting a thorough analysis, I made the tough decision to adopt the existing solution, even though it required more upfront costs. In the end, the project was successfully launched, and we saved significant engineering hours on ongoing support.

### How do you handle a team member who is not meeting their goals?

I take a proactive approach. I initiate a private conversation to understand their challenges, offer support, and set clear expectations. If the issues persist, I work with them to develop an improvement plan and provide ongoing feedback and coaching.

### What do you consider your most significant professional achievement?

Pick by the question:

1. **Safety risk scoring (most recent):** took a research idea to a production system on live traffic; the Peru experiment showed incidents going down by [X%], and it's now being scaled globally.
2. **Driver-rider matching at inDrive:** the ML launch improved our North Star metric by 7%.
3. **Product-owner story (older):** led a cross-functional team to launch a data product that reduced time to market by 30%. We were slightly behind schedule since it was my first product, but the impact was strong. Use it only if asked about product ownership.

### What's your approach to setting and achieving career goals?

I set SMART goals — Specific, Measurable, Achievable, Relevant, and Time-bound. I break big goals into smaller, actionable steps and regularly check my progress. I also look for mentorship and learning opportunities.

### Can you provide an example of leading a team through a crisis?

I once led a team through a crisis when a key team member had to take unexpected medical leave during a critical project phase. I quickly reassigned tasks, adjusted timelines, and kept stakeholders informed. By staying focused and leveraging the team's strengths, we delivered the project on time.

### How do you stay organized and manage your time?

I use a mix of digital tools and time management strategies. I keep a detailed calendar, set clear priorities, and block time for specific tasks. I also use the Pomodoro Technique to stay focused.

### How do you handle a situation where you disagree with your supervisor?

I handle it with respect and professionalism. I first try to understand their perspective by asking for clarification. Then, I share my viewpoint along with supporting evidence and suggest alternatives. In the end, I respect their final decision and continue working as a supportive team member.

### How do you handle a situation where a project is falling behind schedule?

I act quickly to understand the root causes of the delay. I reassess priorities, reallocate resources if needed, and create a clear recovery plan. I also keep stakeholders informed with honest updates.

### How do you handle high-pressure situations?

I stay calm and focused by prioritizing tasks and breaking them into manageable steps. I communicate clearly with the team to keep everyone aligned, and I rely on my problem-solving skills and experience to make quick, informed decisions.

### Can you discuss working on a project with limited resources?

In a previous role, we had a project with only one ML engineer available. I decided to postpone building a full ML platform and instead focused on using our existing infrastructure. By aligning the project scope with available skills and tools, we delivered a successful outcome within the constraints. Result: [time to first working version], [cost], used by [X]. This is the same lean approach I'd use in the Applied AI role: prove value cheaply with a POC, then ask for resources.

---

## Critical Thinking — Practical Cases & Useful Language

Critical thinking skills include things like identifying other people's needs, convincing others, recognizing and building arguments, or evaluating different aspects of a solution.

### Synonyms & Rephrasing Drills

*   *I highlighted the need for some improvements* ➞ I emphasized that it was necessary to improve some things.
*   *Through my analysis, it became clear that some users didn't see the button.* ➞ My analysis showed that some users didn't notice the button.
*   *I think that's basically it* ➞ I guess these are the main points of my story.
*   *As it turned out, most people chose the cheapest subscription.* ➞ We discovered that most people preferred the cheapest plan.
*   *I must admit I haven't had a lot of situations like that.* ➞ I have to say that I've rarely found myself in such situations.
*   *While analyzing the logs, I discovered a data error.* ➞ I found an error in data when I was analyzing the logs.
*   *What I did was I created another query.* ➞ I wrote another query — that's what I did.

### Useful Language

*   **have a bit of a problem** = have a small problem
*   **get on with something** = continue doing something
*   **address something** = try to deal with something
*   **dissatisfied with something** = unhappy with something
*   **figure something out** = find the solution or understand something
*   **miss the deadline** = fail to finish work before the planned date
*   **experience delays** = be forced to wait because of problems
*   **handle something** = take necessary actions to deal with something

### Case 1: Disappointing Results (Process Monitoring Tool)

> I must admit it's hard to remember something like that. But I think there is one case I can share. On my previous project I was involved in creating a tool to monitor business process performance for the procurement department of a manufacturing company. First, we needed to gather the requirements and information about the current state of things. So what we did was we studied the documentation and conducted a series of interviews.
>
> While talking to the stakeholders, we found out that they didn't really have a lot of requirements apart from a consistent process with only about 10 broad variants. As it turned out, they didn't see much value in introducing a monitoring tool. But in my experience this practice could bring really interesting and helpful insights. So I pointed out that seeing every system entry can uncover some unexpected findings.
>
> Then I did the primary modelling and analyzed the results. Through my analysis it became clear that there were over 100 process variants in just over a year. Some steps were skipped or done against the procedure. Besides, a lot of orders were hanging in the system without being processed. I knew that the business team wouldn't be happy about that, so when we met, I started with positive news — most of the scenarios they expected to see were indeed in use. However, the processing of around 20% of the orders didn't go according to the existing standards.
>
> As I expected, the stakeholders were shocked by that data. But I highlighted that further tool development would allow us to dive deeper into it and see the causes of such problems. Eventually the team saw the benefits of monitoring and appreciated my efforts in persuading them.

### Case 2: Historical Master Data Issue (Dashboard)

> Last year I was working on a dashboard to monitor the performance of my company's marketing campaigns. At some point I noticed that, with every weekly refresh, some pieces of historical master data stopped appearing in the dashboard. That was a bit of a problem as I needed to have all the data in place to get on with the task. When I looked into the data table, I saw that some product and campaign information was missing. My preliminary research showed that refactoring the data source was the right way to address the issue.
>
> So, I told the stakeholder and the data team about the situation and we planned the refactoring. I also told the users that I expected to finish working on the dashboard within a month. During the refactoring we managed to restore some data, and by the time it became available, I'd already prepared the dashboard to fit the new data schema. Much to my surprise, I found out that the data coverage only increased by 10% and some data was still missing. The month was over and some of the key stakeholders seemed rather dissatisfied with the results.
>
> So, I apologized for the inconvenience and asked for some time to figure out the root cause of the problem. Talking with one of the dashboard users, I learned that they could delete and recreate campaigns instead of cloning or versioning them. And I realized that the data engineering pipeline was linked to the active campaign directory, and figured that connecting it to historical log data would be a simple and elegant solution.
>
> The data team helped to recreate and test the target data source and we had the dashboard up and running by the end of the week. Although we missed the initial deadline, the stakeholder appreciated the way we handled the situation.

---

## Reference: Additional Behavioral Questions

*(Generic template answers from "70 Toughest Interview Questions")*

### Why should we hire you?
You should hire me because I combine three things this role needs. First, I own the full cycle: at inDrive I took safety scoring from an idea to live traffic and a measured result ([X%] fewer incidents in the pilot). Second, I work lean: I build a prototype alone first, then ask for resources (for example, the RAG shopping assistant demo at Sweed). Third, I think in business terms and leadership terms: I led and hired a team, and I already build LLM agents. I want to bring that to fincrime.

### Where do you see yourself in 5 years?
In five years I see myself as a senior Applied AI engineer or lead who has taken several AI products from idea to scale in one business vertical, and who is growing a small team around them. I want to be the person leadership trusts with a new high-stakes problem. I'm dedicated to continuous growth.

### What do you know about our company?
*Revolut version:* Revolut is a global fintech that keeps expanding its product lines, and it works with a large volume of transaction data, which is exactly where ML and now LLMs can move core metrics. The Applied AI role puts engineers next to business verticals (fincrime, business, retail, CX) and lets them own a product from discovery to a pitch. I also read your five values (Never Settle, Dream Team, Think Deeper, Get It Done, Deliver WOW) and recognize my way of working in them. [Add 1–2 recent facts or product launches you checked on revolut.com or the Revolut blog.]

*Generic version:* I've thoroughly researched your company and am impressed by your innovative products. [Add 1–2 specific facts.]

### What motivates you in your career?
What motivates me is working on problems where ML has a visible effect on real people and the business, like reducing safety incidents, and continually learning while doing it. I thrive when I can tackle new challenges, own the result, and expand my skill set.

### How do you handle constructive criticism?
I welcome constructive criticism as an opportunity for growth. I actively listen, ask clarifying questions, and express gratitude for the input.

### Can you describe a time you had to adapt to a change at work?
Our company underwent a significant software migration project. I embraced this change by proactively seeking training, assisting colleagues in the transition, and providing feedback to improve the process.

### What role do ethics and integrity play in your work?
Ethics and integrity are fundamental. I believe in conducting business honestly, treating all stakeholders with respect, and adhering to ethical standards and company policies.

### How do you handle feedback from peers or subordinates?
I value feedback as an opportunity for growth. I actively listen, consider the feedback objectively, and express gratitude for the insights.

### Can you discuss navigating a project with a diverse, multicultural team?
I promoted cultural sensitivity, encouraged open communication, and leveraged each team member's unique strengths. This approach led to a successful project outcome and enhanced team cohesion.

### What's the most innovative idea you've implemented?
I introduced an automated data analysis tool that significantly reduced manual data entry and processing time, improving efficiency by 40%.

*More recent (GenAI) example:* I automated our daily standup with LLM-based Jira task analysis, and I built a PydanticAI multi-agent framework that creates delivery orders from WhatsApp chats. Result: [minutes saved per person per day / orders handled without a human].

### What role do mentorship and professional development play in your career?
Mentorship and professional development are vital. I actively seek mentorship from experienced professionals and continually invest in professional development opportunities.

### How do you ensure your work aligns with the company's mission?
I regularly refer to the company's mission and values as guiding principles. I ensure my actions, decisions, and projects align with these values.

---

## Revolut — Applied AI Engineer: Process, Values, Screen Q&A

*Added after the Oct 28 recruiter screen. `[X]` = insert your real number. Never invent one; if you have no exact figure, give a clearly labeled estimate ("roughly", "back-of-the-envelope").*

### Role in one sentence

Applied AI Engineer = solo owner of the whole product cycle: pick a high-stakes business vertical (fincrime, business, retail, CX…) → run discovery → validate with unit economics → build a POC/prototype alone in the first couple of months → pitch to senior leadership → if approved, get resources and a team. Focus: aggressively using GenAI/LLMs to move core business metrics, with minimal resources at the start.

### Hiring process (as described by the recruiter)

| # | Round | What to expect | Prep |
|---|-------|----------------|------|
| 1 | Recruiter screen | Done (Oct 28) | — |
| 2 | ML fundamentals | Theory: statistics, maths, probability, A/B testing, "dates back to uni time" | Study from prep materials; it is nearly impossible to pass without them |
| 3 | System design | Map out an end-to-end solution from scratch for a given scenario | Practice ML + LLM system design (data, model, serving, monitoring, cost) |
| 4 | Business problem-solving case | With a senior leader; gather data and insights to crack a business case | Weak spot last time. Drill the framework below |
| 5 | Bar Raiser (behavioral) | Past projects, strong deliverables, going above and beyond, matched to the 5 values | Use this file; map stories to values |
| 6 | Team fit | With a specific business vertical | Prepare domain questions (fincrime etc.) |

**Case framework (round 4):** clarify the goal and the metric → size the opportunity → list data you need and ask for it → segment and find the biggest driver → propose a solution (start with the simplest) → unit economics (value per case × volume × lift − cost) → risks and guardrails → next steps. Think out loud and ask for data instead of guessing.

### Revolut values → which story to use

Source: [Revolut — Our culture](https://www.revolut.com/our-culture)

| Value | What they look for | Your story from this file |
|-------|-------------------|---------------------------|
| **Never Settle** | Excellence, pushing beyond current results | Safety risk scoring: from research idea to live traffic, then a real experiment, then global scaling |
| **Dream Team** | High bar for talent, candid and direct feedback | You hired the whole team of 3; feedback story below |
| **Think Deeper** | Decisions by logic and evidence, find the root cause | Recall@5 investigation (un-authorized users, Kafka); metrics drop by `app_version`; Kafka vs ClickHouse row count |
| **Get It Done** | Grit, urgency, full ownership, contingency plans | Elasticsearch assistant under a tight deadline; pre-configured report instead of a web app; ownership of the incident-ranking service |
| **Deliver WOW** | Simple, high-quality products that make others' work easier | RAG shopping assistant demo; Metabase self-serve reports; LLM standup automation; ranking service that saves incident managers' time |

---

### Recruiter screen — questions and model answers

#### Have you been in a hiring process with us before?

Yes, about 4–5 months ago, for an AI project management role. Since then I've moved into a tech lead position and delivered several ML products end-to-end (safety scoring, liveness detection, incident prioritization), so this hands-on Applied AI role is a much better fit for me.

*Avoid:* "Last time I failed this round." Say instead: "I've prepared specifically for the business case round since then."

#### Does the Applied AI role sound interesting to you?

Very much. What attracts me is the full-cycle ownership. At inDrive, a PM brought the incident prioritization problem, and I turned it into a data pipeline, an inference service and a backend contract with a small team. I'd like to go one step earlier and own the discovery and the unit economics too. I also like the idea of pitching a prototype to leadership to unlock resources, because that is how I already work: prove value cheaply first, then scale.

*Avoid:* only saying "I like working with product and lean resources". Name the specifics: ownership, POC, pitch, unit economics, GenAI.

#### Where are you based, and would you relocate to the UAE, UK or Cyprus?

UAE and the UK are my preferred options. I've already lived in Cyprus for two years, so I'd rather explore a new hub. I'm ready to relocate.

*Avoid:* negative tone about a location ("I really don't want to go back"), and irrelevant details like the Serbian work permit.

#### Citizenship, work permit and visa

I hold Russian citizenship only. Could you tell me how Revolut handles visa and relocation support for the UAE and the UK, and what the usual timeline is?

*Why:* this is your biggest practical risk, so ask early instead of waiting.

#### What is your notice period?

One month. I'd use it for a clean handover of my team's projects, and I'm happy to align on a start date that works for you.
