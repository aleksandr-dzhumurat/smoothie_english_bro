# Behavioral Interview Answers


## Walk me through your background (60–90 seconds)

### Hint
ML career → safety leadership → GenAI and fincrime.

### Ideal answer

Let me walk you through it in about a minute. I'm a machine learning engineer with over five years of experience across online cinema, entertainment, e-commerce and ride-hailing, from early-stage startups to global companies. My main areas are recommender systems and safety scoring. My strength is owning the whole cycle: framing the problem with product, preparing the data, modeling in Python and SQL, deploying the service and running the experiment. I've also led cross-functional teams of three to eleven people, with responsibility for hiring, mentoring, stakeholder communication and planning.

Right now I lead the Safety AI team at inDrive, a global ride-hailing platform, similar to Uber, with three machine learning engineers whom I hired. I'd like to highlight one thing: we built a model that scores a trip for risk *before* it starts; if the score is high, the driver or passenger gets an additional check. We went from idea to experiment in two quarters, and in the Peru pilot incidents went down by 20 percents. We're now scaling it to the whole network. I also built a computer vision based liveness detection service and an incident-ranking service that lets incident managers review the most serious cases first.

Most of my production work is classical ML. On the GenAI side I've built a PydanticAI multi-agent assistant that creates delivery orders in WhatsApp, a RAG shopping assistant, and LLM-based Jira standup automation. I also recently completed a Data Engineering course to strengthen my pipeline skills. This Applied AI role brings together my product, ML and leadership experience in a domain like fincrime, where ML reduces real harm. I'm excited to keep growing technically, mentor colleagues and take on broader responsibility. That's all from my side; happy to go deeper on any part.

## Tell me about the project with the biggest business impact: problem, solution, impact

### Hint
Pre-trip risk scoring → extra checks → Peru pilot.

### Ideal answer

In LATAM, serious incidents (robbery, assault attempts) happen during trips, and support could only react after the fact. I led the team to detect risky trips *before* they start. I framed the problem with product, built the data pipeline and the model that scores each trip, defined what happens at a high score (extra check for the driver or passenger), deployed the service on live traffic, and designed the A/B experiment in Peru.

The experiment finished last month with positive results: incidents went down by 20 percents. What's important here is not just the headline number: all guardrail metrics stayed green. Fewer incidents also mean lower insurance and legal costs, although I don't have the exact savings figures. We're now scaling to the whole network.

## Tell me about the project with the biggest business impact: problem, solution, impact

### Hint
Safety-appeal queue → severity ranking → offline vs. live metrics.

### Ideal answer

InDrive gets a large flow of safety appeals, and incident managers review them manually. Serious cases (robbery, violence) waited in the same queue as minor ones, which means slower response and higher insurance and legal cost. The task was to prioritize the queue so managers see the most serious incidents first. My team and I built a ranking service that scores every appeal by severity; I designed the data preparation pipeline and the inference service, and agreed the API contract with the backend team.

Offline, the model reaches recall of about 0.8 on serious incidents within the top 20 percents of the queue, versus about 5 percents if managers review in chronological order. The A/B test is running; the key metrics are time-to-review for serious cases and handling cost. I'll share the online numbers as soon as the experiment finishes; so far everything is on track.

## How did the idea originate? Did it come from product, or from you?

### Hint
PM surfaced the pain → I led discovery → ranking over classification.

### Ideal answer

I would answer the question in two parts. The PM raised the pain point: the incident queue was not prioritized. Then I took the lead on discovery. I ran kickoffs with the PM and the incident managers to understand how they judge severity, turned that into features, and proposed *ranking* instead of classification, because the managers' capacity is fixed. I defined the success metric, built the pipeline and the service, and agreed the contract with backend. In this role I want to do the same from the very start, including finding the opportunity myself.

## Why are you looking outside your current company, and what do you want in the new place?

### Hint
Broader ownership, fincrime impact, relocation.

### Ideal answer

I'm proud of what we built at inDrive, and I want the next step. I'd like to highlight three things. First, scope: I want to own the whole product cycle, from finding the opportunity to the pitch, and use GenAI/LLMs to move core metrics. Second, domain: safety work showed me I do my best work where ML directly reduces harm, and fraud and financial crime at Revolut is the same logic at a larger scale, with rich transaction data. Third, relocation: inDrive supports relocation only to Cyprus or Serbia, while a hub like the UAE or London fits my plans.

## Tell me about your management experience

### Hint
IC to lead → hired three → two products in experiment.

### Ideal answer

For the first two quarters at inDrive I was an individual contributor, then I became the lead of three machine learning engineers, and I hired the whole team. I set priorities and the roadmap together with product, review designs, mentor, and stay hands-on. Under this setup we shipped two products to experiment within 5 months. Earlier I led teams of 3 to 11 people, including hiring, offboarding, and quarterly planning.

## Do you have any questions for us? (never answer "no")

### Hint
Verticals, six-month expectations, LLM stack, relocation.

### Ideal answer

I do have a couple of questions
- Which business verticals are open for this role right now, and how is the vertical chosen?
- What does success look like in the first 6 months? How many POCs usually reach leadership buy-in?
- What is the LLM stack and tooling the team uses (models, evals, infra budget)?
- What do visa and relocation support look like for the UAE / UK?
- Any tips for the business problem-solving and ML fundamentals rounds?

Thank you, that's all from my side.

## What are your salary expectations?

### Hint
UK market benchmark, total package, ask for range.

### Ideal answer

Based on the market for this level in UK I'm targeting 100k. I'm flexible depending on the total package. Could you share the range for this role? *Research the range first; don't give a number you haven't checked.*

## Are you interviewing with other companies?

### Hint
Other conversations, Revolut fit, one-month notice.

### Ideal answer

I'm talking to a few companies, but Revolut is a top choice for me because of the ownership model and the fincrime domain. I can move fast: my notice period is one month.

## Last time the case round didn't go well. What's different now?

### Hint
Own the setback → structured practice → value before building.

### Ideal answer

Let's be honest: last time the format was new to me, and it showed. It was a minor setback, and I treated it that way. Since then I've practiced the case with a clear structure: clarify the goal, size the opportunity, ask for the data, build the solution, check unit economics, and name risks. I've also run more business-impact projects at work, where I had to estimate the value before building. So I'm not just saying I'll do better; I've put the work in.

## What GenAI / LLM experience do you have?

### Hint
Shopping RAG, WhatsApp orders, Jira standup; evals and cost per task.

### Ideal answer

I've built three things. First, a RAG shopping assistant at Sweed that helps customers fill their carts, prototyped with scraped competitor product data when our own catalog lacked rich descriptions; the demo led to a catalog enrichment initiative. Second, a PydanticAI multi-agent framework that creates delivery orders from WhatsApp chats. Third, an LLM-based Jira analysis that automates our daily standup. My evaluation approach is to test representative and edge-case conversations, check whether the assistant completes the task correctly, and track failures and response time. For cost, I would log input and output token usage for every model call, including retries, and calculate the total cost per successfully completed task using the model's token prices. I'd use failed cases to improve prompts, retrieval, and validation, then rerun the same test set to check for regressions. My production ML is mostly classical, so GenAI is where I'm growing fastest, and this role is the way to apply it at scale.

---

## Tell me about a time you owned a product from idea to production, almost alone

### Hint
Safety scoring → pipeline, model, deployment → Peru A/B test.

### Ideal answer

At inDrive, I took safety risk scoring from a research idea to a production system on live traffic. The problem was that we could only react to serious incidents after they happened. I worked with product to frame the problem: identify risky trips before they start and trigger an extra check for the driver or passenger.

I owned most of the technical work: building the data pipeline, developing the model, and deploying the scoring service. I also designed the A/B experiment in Peru and coordinated the rollout with the backend and support teams. We went from idea to experiment in two quarters. Incidents in the pilot went down by 20 percents, all guardrail metrics stayed green, and we're now scaling the system to the whole network.

A few things took longer than expected, but the delays were mostly predictable. If I did it again, I'd involve backend and support earlier and set guardrail metrics from day one. It's good that we found the edge cases early; it helped us avoid a much bigger problem at scale.

## Tell me about a time you built a POC with minimal resources and pitched it

### Hint
Solo shopping RAG prototype → catalog gap → stakeholder demo.

### Ideal answer

At Sweed we wanted a conversational shopping assistant, but our product catalog had no rich text descriptions. I built a RAG prototype in [X weeks] alone, and to prove the full experience I used scraped competitor data strictly for prototyping. The demo impressed stakeholders and started a discussion on systematically enriching our own catalog. "It was still small, still incubation, but worth looking at. Prove value cheaply, then ask for resources. Crawl first, then walk, then run."


## How do you validate an AI idea with unit economics?

### Hint
Unit value × volume × lift − cost; sensitivity and kill criteria.

### Ideal answer

Let me walk you through it. I use four lines: value per case × volume × expected lift − cost = monthly value, then payback time.
- Value per case: cost of an incident, a fraud loss, an analyst hour, a support contact.
- Volume: cases per day in the chosen vertical.
- Lift: how much better than today's process (get a baseline first; assume a range, not a point).
- Cost: LLM tokens (tokens per request × price × requests), infra, human review for edge cases, maintenance.

Then I test the sensitivity (what if lift is half?), define kill criteria, and build the cheapest POC that can measure the lift. For incident ranking, I would estimate how many serious incidents we could handle faster each day and how much that faster response could reduce insurance and legal costs. I would then compare those savings with the cost of running and maintaining the service.

## Tell me about a time you pitched an idea to senior leadership and got buy-in

### Hint
Jira-to-Slack demo → managers review exceptions, not every task.

### Ideal answer

At inDrive, I noticed that managers spent time before every standup reading Jira tasks, checking progress, and chasing people for missing updates. Much of this was routine work, so I proposed a chatbot that would prepare the updates and highlight only the tasks that needed attention.

I built a working prototype and used it to make the idea concrete for leadership. The bot pulled active tasks from Jira, grouped them by assignee, and posted a daily summary in Slack. It also used an LLM to check whether each task had a clear current state, target state, and action plan, and flagged missing information or progress updates.

My pitch focused on the managers' time: instead of checking every task manually, they could review the exceptions and spend the standup discussing blockers and decisions. The bot worked with the Jira and Slack workflow the team already used, and I kept the running cost low by choosing an inexpensive model. Managers could review its feedback and decide what action to take.

Showing a working chatbot made the value easier to explain and helped me get buy-in. It took over routine preparation and follow-up work, giving managers more time to support the team. I don't have an exact measurement of the time saved, but the practical benefit was less manual checking and chasing updates.

## Tell me about a time you went above and beyond. (Bar Raiser)

### Hint
BigQuery feature discovery → reusable agent skill → analysts take ownership.

### Ideal answer

While working on the safety risk-scoring model at inDrive, I noticed that feature engineering was a bottleneck. BigQuery contained a huge number of tables, but there was no semantic layer to explain what the data meant or how the tables connected. Finding the right data and validating a potential feature could take an experienced data scientist up to a week.

Instead of only researching features for my own model, I took the initiative to make the process reusable. I built an AI agent skill that used our existing BigQuery connectors to research candidate features and guide their validation. I documented the investigation steps and the validation procedure, including ablation tests to check whether a feature actually improved the model, time-based splits to test performance on future data, and geographic splits to check whether the improvement held across locations.

The skill gave product analysts a structured way to investigate features and gather evidence before involving a data scientist. This allowed us to move feature discovery from data scientists to product analysts and substantially speed up the discovery stage. Data scientists could then focus more on modeling and deeper technical work.

For me, going above and beyond meant addressing the bottleneck for the whole team, rather than just getting my next feature into the model. I turned a process that depended on individual expertise into a repeatable workflow that more people could use.

## Tell me about a time a model looked good offline but disappointed in production

### Hint
Recall@5 drop → guest cohort → missing Kafka likes.

### Ideal answer

Offline metrics were fine, but production Recall@5 was lower. I segmented by user cohort, found un-authorized users with very low metrics, traced it to feedback (likes) not being sent to Kafka for them, so their likes were missing from the recommendation pipeline and their recommendations were not personalized, wrote a bug report, and the fix restored performance. "It's good that we found it early. Now I define online metrics and segment checks *before* launch, so a temporary bump doesn't turn into a quarter-long problem."

## Tell me about a time you diagnosed a production incident under time pressure. (Think Deeper / Get It Done)

### Hint
Nightly verification spike → timezone mismatch → rate control before model fix.

### Ideal answer

Our risk-scoring model flags risky ride-hailing passengers, and a flagged order is held until the passenger passes a liveness selfie check through Sumsub (a "challenge"). Every night at exactly 07:00 UTC (02:00 local), the challenge share in Colombia, Peru and Ecuador roughly doubled. On 1 Nov the step took it from 10% to 21%, Sumsub traffic jumped from 9 to 40 req/s past its 30 req/s rate limit, Sumsub started returning HTTP 429, retries piled more load on top, and up to 48K passengers could not start verification. The incident (INCIDENT-13657) was raised to P1, and engineering asked DS whether the step was intended or an artifact, with an answer needed before the post-mortem the next day.

My task was to explain the step quickly and propose measures that would actually prevent a repeat. I also had to make sure the team did not treat a model change as the incident fix when it wasn't one.

I worked with a teammate to trace the sudden increase in checks to how the model used the time of day. Comparing countries helped us see the pattern: the jump happened at the same local hour. We also found that the model had been trained using a different timezone from the live service.

I explained why retraining alone would not solve the problem. Even with the timezone corrected, the model could still suddenly send too many passengers for verification and overload the provider. We needed to control the volume of checks immediately, while improving the model separately. I helped split those two workstreams, with clear owners and timelines.

As a result:
- Verification errors fell to near zero after we controlled the volume of checks.
- We corrected the timezone mismatch and made the model's risk scores change gradually, avoiding sudden spikes.

The key lesson: time features always carry an explicit timezone, and incident fixes are tracked separately from model improvements.

## How do you handle the trade-off between catching fraud/risk and hurting good users? (false positives)

### Hint
Extra check, not a ban; threshold costs and conversion guardrails.

### Ideal answer

In safety scoring the action at a high score is an *additional check*, not a ban, so a false positive costs friction instead of a lost customer. I pick the threshold by comparing the cost of friction with the cost of a missed incident, track guardrail metrics (conversion, share of trips with checks, complaint rate), keep humans in the loop for the highest-impact decisions, and monitor drift by segment. We flag up to 1,000 rides per hour. The same logic applies to fincrime alerts.

## Tell me about how you hired your team. What do you look for? (Dream Team)

### Hint
Hired three for fundamentals, ownership, and communication.

### Ideal answer

I hired all three engineers on my team. I started by defining the skills we needed to take safety models from research to production. During interviews, I focused on technical fundamentals, ownership, and communication: could the candidate explain their decisions, take responsibility for a result, and work effectively with product and backend engineers? I wanted to build a team that could own the whole delivery process, rather than rely on me for every decision. Under this setup, we shipped two products to experiment within five months. I give the team a lot of credit for that result: my role was to set clear priorities and support them, while giving them room to own their work.

## Tell me about a time you gave candid, difficult feedback. (Dream Team)

### Hint
Unclear Jira updates → private feedback → clearer next steps.

### Ideal answer

As a team lead, I sometimes need to give feedback that is uncomfortable. One example was when an engineer's Jira tasks did not have clear progress updates or next steps. That made it difficult to understand whether the work was on track, and I had to chase updates before planning discussions.

I spoke with him privately and focused on the behavior and its impact. I said, "When a task has no recent update or clear next step, I can't tell whether you're making progress or need help. It also makes it harder for the team to plan around your work." I asked what was getting in the way and explained that I needed visibility into progress and blockers.

We agreed on a simple expectation: keep the current state and next step clear in Jira, and raise blockers early. In the following sprint, his updates became clearer and I needed fewer follow-ups. I also made a point of recognizing the improvement in front of the team. I'm deliberately working on giving positive feedback as consistently as I give corrective feedback.

## Tell me about a time you were not satisfied with a "good enough" result. (Never Settle)

### Hint
Batch risk scores → real-time Kafka features → fresher decisions.

### Ideal answer

While working on safety risk scoring at inDrive, batch inference would have been enough for an initial solution. We could calculate risk scores on a schedule and use them until the next update. That was a reasonable starting point, but it meant recent activity would not affect the score until the next batch run.

I wanted the model to respond to what was happening now. I pushed to add real-time features based on events from Kafka, so new activity could inform the risk assessment before a trip started. This meant going beyond the batch pipeline and building a way to keep those features up to date as events arrived.

The result was a system that could use recent behavior rather than rely only on the last scheduled update. Batch inference gave us a workable baseline, but real-time features made the information behind each decision fresher. For me, going beyond "good enough" meant identifying where that freshness mattered for safety and improving that part of the system.

## Where could LLMs create leverage in fincrime? (case prep, role-specific)

### Hint
Alert triage, queue ranking, analyst copilot; baseline and unit economics.

### Ideal answer

1. Alert triage and summarization: an LLM summarizes the case and evidence for an analyst; metric: handling time per alert. This mirrors your incident-ranking service (prioritize first, then speed up the review).
2. Prioritization of alert queues: the same ranking idea as incident moderation; metric: share of serious cases found in the top 20 percents of the queue.
3. Analyst copilot: for investigation notes and SAR/report drafting; metric: hours saved per case, quality checked by sampling.

For each: first ask for the baseline (volume, cost per case, current false-positive rate), then run the unit-economics test above.


## Main Achievements
### Hint
Safety scoring, liveness, queue ranking, hiring, LLM automation.

### Ideal answer

I currently work as a Safety AI Tech Lead at inDrive. My team builds ML solutions for trip monitoring, safety scoring, and liveness checks, with the overarching goal of reducing safety incidents on the platform.

As a hands-on tech lead:
*   Turned safety risk scoring from a research idea into a production-ready system that handles live traffic. It scores a trip for risk before it starts; the Peru pilot reduced incidents by 20 percents and it is now being scaled to the whole network.
*   Built a computer vision based liveness detection service.
*   Built an incident-ranking service that puts serious appeals (robbery, violence) at the top of the incident managers' queue (offline recall about 0.8; online experiment running).
*   Hired the whole team of three machine learning engineers.

As an individual contributor:
*   Designed a PydanticAI-based multi-agent framework that automates delivery order creation via WhatsApp chat.
*   Automated the daily standup routine with LLM-based Jira task analysis.

## Previous Experience

### Hint
ivi analytics → FunCorp recommendations → inDrive matching → Sweed → Safety AI.

### Ideal answer

**ivi (Online Cinema)**
I started out as a data analyst at an online cinema called ivi, which is similar to the Russian version of Netflix. That role helped me gain hands-on experience with visualization, data cleansing, and BI tools like Tableau and PowerBI. I provided actionable insights to the business based on my analysis. Although my background is in data analysis, I've always had a strong interest in data science and machine learning. As I took on more responsibility, I was promoted to Senior machine learning engineer.

**FunCorp (Entertainment)**
At FunCorp, I led a team of four ML engineers building a personalized feed of funny videos and images. I collaborated closely with the Chief Product Officer and Chief Analyst. One of our main achievements was building and launching a classic two-stage recommender system.

**inDrive (Ride-Hailing)**
After FunCorp, I worked as a data scientist at inDrive, a global ride-hailing company, where I gathered, analyzed, and interpreted driver-rider matching data to support product owners in improving the dispatch algorithm. I was part of a product team of four, with a primary focus on optimizing the marketplace. My main responsibility was managing the entire data preparation pipeline. The ML launch led to an impressive 7% improvement in our North Star metric.

I built a driver-rider matching model using CatBoost, added location-based features, and developed the data and training pipeline with BigQuery and Kubeflow on Google Cloud.

**Sweed (E-commerce)**
After inDrive, I joined Sweed, a small e-commerce technology company, as a Staff ML engineer. In this role, I implemented models for inventory management, an AI shopping assistant, and a churn prediction classifier. I then returned to inDrive to lead the Safety AI direction.

## Strengths
### Hint
Initiative, experiments, cross-functional work, end-to-end ownership.

### Ideal answer

*   Proactivity & Innovation
*   Experimentation & Metrics-Driven Approach
*   Cross-Functional Collaboration & Communication
*   Strong ML/AI Expertise
*   End-to-end Ownership (idea → pipeline → service → experiment → business case)

## Weaknesses
### Hint
Deepen LLM fundamentals; recognize teammates’ wins more often.

### Ideal answer

*   Depth in deep learning / LLM internals: Most of my production work is classical ML, although I've also shipped a computer vision based liveness service and LLM agents. I'm deepening the foundations (LLM evaluation, fine-tuning) through hands-on projects, and for an Applied AI role I treat it as my main growth area.
*   Giving Feedback: Another area I'm working on is giving positive feedback to colleagues. While I naturally focus on problem-solving and areas for improvement, I've realized the importance of recognizing what's going well. I'm becoming more intentional about expressing appreciation.

---

## Personal Behavioral Answers: Give an example of a challenging project

### Hint
Shopping assistant → thin catalog → prototype sparks catalog enrichment.

### Ideal answer

One of the most challenging projects I worked on was building an AI-powered shopping assistant. AI assistant was designed to help customers fill their carts through a conversational interface. My goal was to implement a solution that could understand user intent and suggest relevant products in real-time, effectively simulating a human-like shopping experience. I decided to use a Retrieval-Augmented Generation (RAG) architecture for the assistant. However, I quickly ran into a major roadblock: our internal product database lacked rich text descriptions, which are essential for generating meaningful, context-aware chatbot responses. To work around this, I proposed and implemented a solution to scrape product data from a competitor's site — strictly for prototyping purposes. This gave us access to richer content that I could use to power the assistant and demonstrate the full potential of the experience. The prototype was a success and impressed our stakeholders during the demo. As a result, we began broader discussions on how to systematically enrich our own product catalog to support future ML and conversational use cases. It turned a technical challenge into an opportunity for long-term product improvement.

## Personal Behavioral Answers: Describe a time when you had to solve a complex technical problem

### Hint
Pipeline memory failures → micro-batches and Polars → faster processing.

### Ideal answer

While working on a data pipeline, I noticed a sudden spike in job failures, impacting downstream analytics. I needed to diagnose and fix the issue quickly to restore data flow. I analyzed logs, identified a memory leak due to unoptimized batch processing, and rewrote the job to use micro-batches and replace Pandas with Polars with better memory management. Failures dropped to zero, processing time improved by 40%, and I documented the fix to prevent recurrence.

## Personal Behavioral Answers: What is your greatest strength?

### Hint
Clarify requirements, build an MVP, iterate on feedback.

### Ideal answer

One of my greatest strengths is my ability to quickly gather business requirements and deliver working solutions fast. I focus on understanding the core problem and avoid over-engineering, which helps me move quickly and iterate based on real feedback. I follow a 'fail fast' mindset — getting something functional out early allows me to validate assumptions, adjust course if needed, and ultimately deliver better results in less time.

## Personal Behavioral Answers: What's your greatest weakness?

### Hint
Task switching → Pomodoro → protect focus.

### Ideal answer

One area I've been working on is improving my concentration when handling multiple tasks. I've noticed that when I have several things on my plate, I sometimes switch between them too frequently, which affects my focus. To manage this, I've started using the Pomodoro technique — it helps me stay locked in on one task at a time and maintain better productivity throughout the day.

## Personal Behavioral Answers: Team work: Tell me about a time when you faced a problem you couldn't solve yourself

### Hint
ClickHouse/Kafka row gap → data engineering help → unregistered users.

### Ideal answer

Early in my career, I encountered a complex data quality issue that was affecting our training pipeline. The training dataset prepared from ClickHouse has fewer rows per day than the Kafka data source, indicating a bug in our Kafka data preparation pipeline. Despite multiple attempts, I couldn't identify the root cause alone. I realized that support from a data engineering team was necessary, so I approached senior team members and proposed forming a cross-functional task force to investigate further. By leveraging their expertise and collaborative problem-solving, we were able to uncover a system integration issue that was corrupting our data. This experience taught me the value of teamwork and diverse perspectives in overcoming challenges. The root cause was related to how we handled unregistered users.

## Personal Behavioral Answers: Communication: Tell me about a time when it was hard to communicate the importance of the task to the tech team?

### Hint
Data governance resistance → one-on-ones → connect standards to team needs.

### Ideal answer

In a past role as a data team product owner, I was responsible for setting up new data governance rules. To make it work, I needed support from the tech team to follow data rules and standards. Initially, I faced resistance as the tech team prioritized other pressing issues. To communicate the importance effectively, I scheduled a series of one-on-one meetings with key stakeholders from the tech team. During these meetings, I emphasized how improved data governance would streamline workflows and enhance data reliability for their projects. By demonstrating empathy and aligning the benefits with their goals, I successfully gained their support and cooperation.

## Personal Behavioral Answers: Handling Negative Feedback: Tell me about a time when you got negative feedback

### Hint
Unclear visualizations → ask stakeholders → revise the design.

### Ideal answer

During a project presentation, I received constructive feedback from stakeholders regarding the visual clarity of our data visualizations. Initially, I felt disappointed as I had put significant effort into the design. However, I recognized the opportunity to improve. I scheduled a follow-up meeting with the stakeholders to delve deeper into their expectations and preferences. I then revised the visualizations accordingly, incorporating their feedback. This experience reinforced my belief in the value of iterative improvement and listening actively to stakeholder needs.

## Personal Behavioral Answers: Anticipating Problems: Tell me about a time when you anticipated potential problems and developed steps to avoid them

### Hint
Legacy migration → profile data → validation and fallbacks.

### Ideal answer

In a data migration project, I proactively anticipated potential data integrity issues due to the complexity of merging legacy databases. To mitigate risks, I conducted thorough data profiling and developed a comprehensive data validation plan before initiating the migration. This involved running extensive data quality checks and creating fallback strategies in case of discrepancies. As a result, we successfully completed the migration within the timeline and minimized disruptions to business operations.

## Personal Behavioral Answers: Challenging situation: metrics drop investigation

### Hint
Recommended views fell → segment by app version → release issue.

### Ideal answer

In my previous role as a data analyst, we noticed a significant drop in our metric for recommended item views. Upon investigation, we found that this decline was specifically associated with certain dates. I started by grouping the data by 'app_version' attribute and discovered a pattern — the metrics dropped on specific dates that coincided with the release of new application versions. We then worked closely with the application development team to identify and rectify the issues within the new releases. After rectifying the issues, our metrics showed a significant recovery. This incident highlighted the importance of thorough checks and test runs before releasing any new application versions.

## Personal Behavioral Answers: Challenging situation: Recall@5 metric investigation

### Hint
Production Recall@5 → anonymous users → fix missing likes events.

### Ideal answer

I was responsible for developing and monitoring the performance of a recommendation system in a production environment. Upon deployment, the Recall@5 metric in production was showing lower values than expected. I investigated and identified a specific cohort of users — un-authorized users — experiencing low metrics. Further analysis revealed that for this cohort, feedback data (content likes) was not being sent to Kafka, causing the recommendation system to perform poorly for these users. I documented my findings and wrote a detailed bug report. The development team implemented a fix, ensuring that the feedback data for un-authorized users was correctly sent to Kafka, leading to improved performance.

## Personal Behavioral Answers: Tell me about a time you failed and what you learned from it

### Hint
Two leads, unclear remit → leave → verify ownership before accepting.

### Ideal answer

Let's be honest, this one was a setback. I joined the company as the ML team lead; during hiring I was told the current lead would move up a grade. When I started, the promotion didn't materialize, and we were effectively two leads on one team. I took a step back and looked at what I actually wanted: people management plus hands-on work. Staying meant neither. I didn't have a crystal ball, but I decided it was a one-way door for my growth, so I left and found a role where I could own both the technical and the leadership side. What I learned: check the setup before accepting, not after, and ask the uncomfortable question early.

## Personal Behavioral Answers: Adapting to Changing Requirements

### Hint
Frontend engineer left → replace inventory app with a report.

### Ideal answer

In a previous role as a product manager, I faced a tight deadline when a client requested a tool to monitor out-of-stock inventory items. Unfortunately, our frontend engineer left the company just as the deadline was approaching. To meet the client's needs, I proposed an alternative solution. Instead of developing a full web application, I offered a pre-configured report with the necessary columns. This allowed us to deliver the core functionality without the complexity of building an interface from scratch, and we met the deadline.

## Personal Behavioral Answers: Give an example of how you handled tight deadlines

### Hint
Reuse Elasticsearch → lightweight query layer instead of an ML model.

### Ideal answer

In one of my projects, I was expected to deliver a machine learning–based assistant that could suggest relevant items to users. The timeline was very tight. Instead of going the ML route right away, I assessed the available tools and realized we already had a well-structured ElasticSearch setup in place. I decided to reuse it and built a lightweight layer that translated user input into search queries. By tuning the query scoring and leveraging full-text search with filters, I was able to get relevant results without building a model. I delivered a fully working assistant ahead of the deadline.

## Personal Behavioral Answers: Tell me about a time when you had to deliver a project under a tight deadline

### Hint
One week → essential scope, feature flags, parallel QA.

### Ideal answer

A product team needed a last-minute feature for a major launch, but we had only a week to implement it. I collaborated with stakeholders to prioritize essential functionality, used feature flags to roll out changes incrementally, and worked with QA to parallelize testing. The feature launched on time with no critical bugs, and the approach became a template for future urgent tasks.

## Personal Behavioral Answers: Give an example of a time you had to troubleshoot a production issue

### Hint
Empty recommendations → index/query mismatch → hotfix and CI checks.

### Ideal answer

A real-time recommendation engine started returning empty results, impacting user engagement. I traced logs, found a mismatch between the indexing process and the query format, and deployed a hotfix while reindexing the data. The system recovered within an hour, and I later improved our CI/CD pipeline to catch such issues earlier.

## Personal Behavioral Answers: Describe a time when you had to manage a difficult stakeholder

### Hint
Unrealistic feature request → explain impact → agree on phased MVP.

### Ideal answer

A client insisted on an unrealistic feature that would have delayed the project significantly. I presented alternative approaches, backed by impact analysis, and proposed a phased rollout with incremental improvements. The client agreed to a compromise, and we delivered an MVP on time while planning further enhancements.

## Personal Behavioral Answers: Learning a New Technology Quickly

### Hint
Learn Polars → migrate a pandas pipeline → lower memory pressure.

### Ideal answer

Our analytics team adopted Polars, but no one had prior experience. I had to quickly get up to speed and help the team integrate it. I used Claude to rewrite current pandas pipeline using polars. We successfully deployed our first Polars pipeline, reducing memory pressure by 60%.

## Personal Behavioral Answers: Describe a time when you had to mediate a conflict between team members

### Hint
Airflow vs. Dagster → compare benchmarks → agree on simplicity.

### Ideal answer

Two engineers disagreed on whether to use Airflow or Dagster for a new data ingestion pipeline. I organized a structured debate, gathered performance benchmarks, and facilitated consensus-building. We chose Dagster for simplicity, and the decision process improved team collaboration.

## Personal Behavioral Answers: Have you ever optimized a system for better performance?

### Hint
12-hour batch job → parallelism and query tuning → two hours.

### Ideal answer

A batch job processing user transactions was taking over 12 hours to complete. I identified bottlenecks, parallelized processing, and optimized database queries. Processing time dropped to 2 hours, improving data freshness for stakeholders.

## Personal Behavioral Answers: Have you ever dealt with a security vulnerability?

### Hint
S3 exposure → restrict access, rotate credentials, automate scanning.

### Ideal answer

A routine audit uncovered a misconfigured S3 bucket exposing user data. I restricted access, rotated credentials, and implemented automated security scanning. No data was compromised, and security audits became part of our development lifecycle.

## Personal Behavioral Answers: Have you ever improved a process in your workplace?

### Hint
Custom reporting bottleneck → Metabase MVP → self-service dashboards.

### Ideal answer

We had a custom reporting system, and every new report request created a heavy workload for both designers and front-end developers. I proposed building an MVP version of the reports using Metabase, an open-source analytics tool. This allowed us to quickly generate visualizations and dashboards without involving design or front-end teams. Stakeholders were able to explore data on their own, it reduced custom report requests, and gave the team more time for higher-impact work.

## Personal Behavioral Answers: Why did you leave your previous job?

### Hint
Wanted ML closer to business outcomes → moved into Safety AI.

### Ideal answer

I left my previous role because machine learning was not the core of the product there, and ML tasks were often de-prioritized in favor of other initiatives. I wanted an environment where ML directly drives business outcomes, and that's what I found in the Safety AI direction.

## Personal Behavioral Answers: Describe a situation where you had to work with a difficult coworker

### Hint
Last-minute meetings → private conversation → agenda and notice.

### Ideal answer

In my previous role, I worked with a colleague who frequently scheduled same-day meetings without prior notice. This made it challenging to prepare and often disrupted focused work. I initiated a one-on-one conversation and explained that having a clear agenda and at least a day's notice would help make our meetings more productive. We agreed on communication guidelines, and our collaboration became much smoother.

## Personal Behavioral Answers: What's your leadership style?

### Hint
Measurable outcomes, autonomy, hands-on support.

### Ideal answer

I would describe my leadership style as results-oriented. I believe that effort is important, but ultimately it's the outcomes that matter. I focus on empowering team members to make decisions within their areas of expertise while providing clear guidance and support. I emphasize setting measurable goals and regularly tracking progress. I hired my whole team of 3, and I stay hands-on enough to review designs and code while owning priorities and the roadmap together with product.

## Personal Behavioral Answers: How do you stay updated with industry trends?

### Hint
Newsletters, communities, courses, automated weekly reading digest.

### Ideal answer

I stay updated by following thought leaders on LinkedIn and subscribing to several high-quality Substack newsletters covering AI, data science, and product strategy. I'm also active in professional communities. Additionally, I take online courses and certifications — especially in the GenAI space. I also built a chatbot that curates interesting posts from technical blogs and runs on a weekly schedule, so a fresh reading digest reaches me automatically.

## Personal Behavioral Answers: Why do you want to work here?

### Hint
Full-cycle AI ownership, fincrime impact, Revolut values.

### Ideal answer

Three reasons. First, the role: owning the product cycle from discovery to a pitch, with GenAI/LLMs and unit economics, is exactly the next step after leading a team and shipping ML products. Second, the domain: my safety work showed me I do my best work where ML reduces real harm, and fincrime at Revolut is the same logic at a larger scale, with rich transaction data. Third, the standard: your values (Never Settle, Get It Done) match how I work, and the relocation to a hub like the UAE or London fits my plans.

I want to work here because I admire your focus on innovation and making a difference. I've heard great things about how you support employee growth, which fits well with my career goals. [Add 1–2 company-specific facts.]

## Personal Behavioral Answers: What is your preferred work style?

### Hint
Prototype independently; collaborate to reach production.

### Ideal answer

I'm mostly a team player. I believe teamwork brings more value than working alone. My approach is to build an MVP on my own first, and then collaborate closely with the team to bring it to production.

## Personal Behavioral Answers: How do you handle ambiguity and uncertainty in a project?

### Hint
Break down the problem, gather evidence, consult the team, adapt.

### Ideal answer

I thrive in ambiguous situations by breaking down complex problems into smaller, manageable tasks. I do thorough research and consult with team members to gather insights and make informed decisions. My ability to stay adaptable and calm under uncertainty has helped me navigate challenging projects successfully.

## Personal Behavioral Answers: Describe a situation where you had to persuade a team to adopt your idea

### Hint
SQL files over notebooks → demo and migration plan.

### Ideal answer

In a previous role, I proposed a new way to store SQL templates for research purposes — storing them in SQL files instead of Jupyter notebooks. I prepared a demo to highlight the benefits, presented a clear plan for updating the entire codebase, and encouraged team members to share their input. We made our research repo more organized and structured.

## Personal Behavioral Answers: How do you prioritize tasks when you have multiple deadlines?

### Hint
Urgency vs. importance → align, delegate, check progress.

### Ideal answer

I prioritize by evaluating urgency and importance. I create a task list, set deadlines, and break larger projects into smaller steps. I confirm my priorities with stakeholders, delegate when possible, and conduct regular progress checks.

## Personal Behavioral Answers: Can you discuss a time when you had to make a difficult decision at work?

### Hint
A/B platform: adapt vs. build; upfront cost vs. ongoing support.

### Ideal answer

I was once tasked with deciding how to run an A/B testing system: either adapt an existing solution or develop our own. After conducting a thorough analysis, I made the tough decision to adopt the existing solution, even though it required more upfront costs. In the end, the project was successfully launched, and we saved significant engineering hours on ongoing support.

## Personal Behavioral Answers: How do you handle a team member who is not meeting their goals?

### Hint
Private discussion → support and expectations → improvement plan if needed.

### Ideal answer

I take a proactive approach. I initiate a private conversation to understand their challenges, offer support, and set clear expectations. If the issues persist, I work with them to develop an improvement plan and provide ongoing feedback and coaching.

## Personal Behavioral Answers: What do you consider your most significant professional achievement?

### Hint
Lead with Peru safety pilot; matching and data product as backups.

### Ideal answer

1. Safety risk scoring (most recent): took a research idea to a production system on live traffic; the Peru experiment showed incidents going down by 20 percents, and it's now being scaled globally.
2. Driver-rider matching at inDrive: the ML launch improved our North Star metric by 7%.
3. Product-owner story (older): led a cross-functional team to launch a data product that reduced time to market by 30%. We were slightly behind schedule since it was my first product, but the impact was strong. Use it only if asked about product ownership.

## Personal Behavioral Answers: What's your approach to setting and achieving career goals?

### Hint
SMART goals, small steps, progress checks, mentorship.

### Ideal answer

I set SMART goals — Specific, Measurable, Achievable, Relevant, and Time-bound. I break big goals into smaller, actionable steps and regularly check my progress. I also look for mentorship and learning opportunities.

## Personal Behavioral Answers: Can you provide an example of leading a team through a crisis?

### Hint
Unexpected leave → reassign work → reset expectations → deliver on time.

### Ideal answer

I once led a team through a crisis when a key team member had to take unexpected medical leave during a critical project phase. I quickly reassigned tasks, adjusted timelines, and kept stakeholders informed. By staying focused and leveraging the team's strengths, we delivered the project on time.

## Personal Behavioral Answers: How do you stay organized and manage your time?

### Hint
Calendar, priorities, time blocks, Pomodoro.

### Ideal answer

I use a mix of digital tools and time management strategies. I keep a detailed calendar, set clear priorities, and block time for specific tasks. I also use the Pomodoro Technique to stay focused.

## Personal Behavioral Answers: How do you handle a situation where you disagree with your supervisor?

### Hint
Understand their view → present evidence → distinguish reversible decisions.

### Ideal answer

I handle it with respect and professionalism. I first try to understand their perspective by asking for clarification. Then I say "I would answer the question differently" and share my viewpoint with supporting evidence and alternatives. If the decision is a one-way door, I push harder and ask for more time or data; if it's reversible, I say "let's try it and see", disagree and commit, and revisit it with the results.

## Personal Behavioral Answers: How do you handle a situation where a project is falling behind schedule?

### Hint
Identify dependency owner → rescope parallel work → revised plan and checkpoints.

### Ideal answer

When a project falls behind because we depend on another team, I first speak with their owner to understand the blocker and agree on a realistic delivery date. I make clear what we need from them and how the delay affects our launch. Then I work with my team to find what we can deliver independently, whether through a temporary workaround, a smaller scope or a different order of tasks. If priorities conflict, I bring the relevant leads together to agree on a decision. I keep stakeholders informed about the dependency, its impact and our revised plan, and follow up with clear owners and checkpoints.

## Personal Behavioral Answers: How do you handle high-pressure situations?

### Hint
Stay calm, prioritize, break down tasks, keep the team aligned.

### Ideal answer

I stay calm and focused by prioritizing tasks and breaking them into manageable steps. I communicate clearly with the team to keep everyone aligned, and I rely on my problem-solving skills and experience to make quick, informed decisions.

## Personal Behavioral Answers: Can you discuss working on a project with limited resources?

### Hint
One engineer → narrow RAG prototype → prove value before scaling.

### Ideal answer

At Sweed, I built the first version of a RAG shopping assistant on my own. Instead of building a full ML platform, I focused on a working prototype that could demonstrate the customer experience. Our catalog lacked rich product descriptions, so I used scraped competitor data strictly for prototyping. This kept the scope manageable for one engineer and avoided investing in a larger platform before validating the idea. The prototype impressed stakeholders during the demo and started a discussion about enriching our own catalog. This is the same lean approach I'd use in the Applied AI role: prove value with a small working version, then use the evidence to ask for resources.

## Case 1: Disappointing Results (Process Monitoring Tool)

### Hint
Procurement expected 10 variants → found over 100 and off-process orders.

### Ideal answer

"I must admit it's hard to remember something like that. But I think there is one case I can share."

On my previous project I was involved in creating a tool to monitor business process performance for the procurement department of a manufacturing company. First, we needed to gather the requirements and information about the current state of things. So what we did was we studied the documentation and conducted a series of interviews.

While talking to the stakeholders, we found out that they didn't really have a lot of requirements apart from a consistent process with only about 10 broad variants. As it turned out, they didn't see much value in introducing a monitoring tool. But in my experience this practice could bring really interesting and helpful insights. So I pointed out that seeing every system entry can uncover some unexpected findings.

Then I did the primary modelling and analyzed the results. Through my analysis it became clear that there were over 100 process variants in just over a year. Some steps were skipped or done against the procedure. Besides, a lot of orders were hanging in the system without being processed. I knew that the business team wouldn't be happy about that, so when we met, I started with positive news — most of the scenarios they expected to see were indeed in use. However, the processing of around 20% of the orders didn't go according to the existing standards.

As I expected, the stakeholders were shocked by that data. But I highlighted that further tool development would allow us to dive deeper into it and see the causes of such problems. Eventually the team saw the benefits of monitoring and appreciated my efforts in persuading them.

## Case 2: Historical Master Data Issue (Dashboard)

### Hint
Dashboard lost history → refactor fell short → recover from historical logs.

### Ideal answer

Last year I was working on a dashboard to monitor the performance of my company's marketing campaigns. At some point I noticed that, with every weekly refresh, some pieces of historical master data stopped appearing in the dashboard.

That was a bit of a problem as I needed to have all the data in place to get on with the task. When I looked into the data table, I saw that some product and campaign information was missing. My preliminary research showed that refactoring the data source was the right way to address the issue.

What happened next:
- First attempt: so, I told the stakeholder and the data team about the situation and we planned the refactoring. I also told the users that I expected to finish working on the dashboard within a month. During the refactoring we managed to restore some data, and by the time it became available, I'd already prepared the dashboard to fit the new data schema. Much to my surprise, I found out that the data coverage only increased by 10% and some data was still missing. The month was over and some of the key stakeholders seemed rather dissatisfied with the results.
- Root cause: so, I apologized for the inconvenience and asked for some time to figure out the root cause of the problem. Talking with one of the dashboard users, I learned that they could delete and recreate campaigns instead of cloning or versioning them. And I realized that the data engineering pipeline was linked to the active campaign directory, and figured that connecting it to historical log data would be a simple and elegant solution.

The data team helped to recreate and test the target data source and we had the dashboard up and running by the end of the week. Although we missed the initial deadline, the stakeholder appreciated the way we handled the situation.

## Why should we hire you?
### Hint
Measured safety impact, lean RAG prototype, team leadership and LLMs.

### Ideal answer

You should hire me because I combine three things this role needs. First, I own the full cycle: at inDrive I took safety scoring from an idea to live traffic and a measured result (20 percents fewer incidents in the pilot). Second, I work lean: I build a prototype alone first, then ask for resources (for example, the RAG shopping assistant demo at Sweed). Third, I think in business terms and leadership terms: I led and hired a team, and I already build LLM agents. I want to bring that to fincrime.

## Where do you see yourself in 5 years?
### Hint
Scale Applied AI products, own high-stakes work, grow a team.

### Ideal answer

In five years I see myself as a senior Applied AI engineer or lead who has taken several AI products from idea to scale in one business vertical, and who is growing a small team around them. I want to be the person leadership trusts with a new high-stakes problem. I'm dedicated to continuous growth.

## What do you know about our company?
### Hint
Revolut products, transaction data, Applied AI verticals, values.

### Ideal answer

I've researched Revolut and am impressed by the range of products you've built. Revolut is a global fintech that keeps expanding its product lines, and it works with a large volume of transaction data, which is exactly where ML and now LLMs can move core metrics. The Applied AI role puts engineers next to business verticals (fincrime, business, retail, CX) and lets them own a product from discovery to a pitch. I also read your five values (Never Settle, Dream Team, Think Deeper, Get It Done, Deliver WOW) and recognize my way of working in them.

## What motivates you in your career?
### Hint
Real-world ML impact, ownership, continuous learning.

### Ideal answer

What motivates me is working on problems where ML has a visible effect on real people and the business, like reducing safety incidents, and continually learning while doing it. I thrive when I can tackle new challenges, own the result, and expand my skill set.

## How do you handle constructive criticism?
### Hint
Listen, clarify, thank them, use the feedback.

### Ideal answer

I welcome constructive criticism as an opportunity for growth. I actively listen, ask clarifying questions, and express gratitude for the input.

## Can you describe a time you had to adapt to a change at work?
### Hint
Software migration → learn, help colleagues, share feedback.

### Ideal answer

Our company underwent a significant software migration project. I embraced this change by proactively seeking training, assisting colleagues in the transition, and providing feedback to improve the process.

## What role do ethics and integrity play in your work?
### Hint
Honesty, respect, standards, and company policies.

### Ideal answer

Ethics and integrity are fundamental. I believe in conducting business honestly, treating all stakeholders with respect, and adhering to ethical standards and company policies.

## How do you handle feedback from peers or subordinates?
### Hint
Listen actively, evaluate objectively, thank them.

### Ideal answer

I value feedback as an opportunity for growth. I actively listen, consider the feedback objectively, and express gratitude for the insights.

## Can you discuss navigating a project with a diverse, multicultural team?
### Hint
Cultural sensitivity, open communication, individual strengths.

### Ideal answer

I promoted cultural sensitivity, encouraged open communication, and leveraged each team member's unique strengths. This approach led to a successful project outcome and enhanced team cohesion.

## What's the most innovative idea you've implemented?
### Hint
Automated analysis, Jira standup, or WhatsApp order creation.

### Ideal answer

I introduced an automated data analysis tool that significantly reduced manual data entry and processing time, improving efficiency by 40%.

I automated our daily standup with LLM-based Jira task analysis, and I built a PydanticAI multi-agent framework that creates delivery orders from WhatsApp chats. Result: 90 minutes saved.

## What role do mentorship and professional development play in your career?
### Hint
Seek experienced mentors and keep investing in learning.

### Ideal answer

Mentorship and professional development are vital. I actively seek mentorship from experienced professionals and continually invest in professional development opportunities.

## How do you ensure your work aligns with the company's mission?
### Hint
Use the mission and values to guide project decisions.

### Ideal answer

I regularly refer to the company's mission and values as guiding principles. I ensure my actions, decisions, and projects align with these values.

## Have you been in a hiring process with us before?

### Hint
Previous AI PM interview → tech lead delivery → better Applied AI fit.

### Ideal answer

Yes, about 4–5 months ago, for an AI project management role. Since then I've moved into a tech lead position and delivered several ML products end-to-end (safety scoring, liveness detection, incident prioritization), so this hands-on Applied AI role is a much better fit for me.

## Does the Applied AI role sound interesting to you?

### Hint
Incident ranking → earlier discovery, unit economics, leadership pitch.

### Ideal answer

Very much. What attracts me is the full-cycle ownership. At inDrive, a PM brought the incident prioritization problem, and I turned it into a data pipeline, an inference service and a backend contract with a small team. I'd like to go one step earlier and own the discovery and the unit economics too. I also like the idea of pitching a prototype to leadership to unlock resources, because that is how I already work: prove value cheaply first, then scale.

## Where are you based, and would you relocate to the UAE, UK or Cyprus?

### Hint
Prefer UAE or UK; previously lived in Cyprus.

### Ideal answer

UAE and the UK are my preferred options. I've already lived in Cyprus for two years, so I'd rather explore a new hub. I'm ready to relocate.

## Citizenship, work permit and visa

### Hint
State citizenship; ask about UAE/UK sponsorship and timeline.

### Ideal answer

I hold Russian citizenship only. Could you tell me how Revolut handles visa and relocation support for the UAE and the UK, and what the usual timeline is?

## What is your notice period?

### Hint
One month, clean handover, flexible start date.

### Ideal answer

One month. I'd use it for a clean handover of my team's projects, and I'm happy to align on a start date that works for you.
