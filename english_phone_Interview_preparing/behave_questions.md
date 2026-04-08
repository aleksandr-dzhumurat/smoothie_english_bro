# Behave questions

## STAR technique

- situation
- task
- action
- results

## Give an example of a challenging project.

One of the most challenging projects I worked on was building an AI-powered shopping assistant. AI assistant was designed to help customers fill their carts through a conversational interface. My goal was to implement a solution that could understand user intent and suggest relevant products in real-time, effectively simulating a human-like shopping experience. I decided to use a Retrieval-Augmented Generation (RAG) architecture for the assistant. However, I quickly ran into a major roadblock: our internal product database lacked rich text descriptions, which are essential for generating meaningful, context-aware chatbot responses. To work around this, I proposed and implemented a solution to scrape product data from a competitor’s site—strictly for prototyping purposes. This gave us access to richer content that I could use to power the assistant and demonstrate the full potential of the experience. The prototype was a success and impressed our stakeholders during the demo. As a result, we began broader discussions on how to systematically enrich our own product catalog to support future ML and conversational use cases. It turned a technical challenge into an opportunity for long-term product improvement.

## Describe a time when you had to solve a complex technical problem.

While working on a data pipeline, I noticed a sudden spike in job failures, impacting downstream analytics. I needed to diagnose and fix the issue quickly to restore data flow. I analyzed logs, identified a memory leak due to unoptimized batch processing, and rewrote the job to use micro-batches and replace Pandas with Polars with better memory management. Failures dropped to zero, processing time improved by 40%, and I documented the fix to prevent recurrence.

## What is your greatest strength?

One of my greatest strengths is my ability to quickly gather business requirements and deliver working solutions fast. I focus on understanding the core problem and avoid over-engineering, which helps me move quickly and iterate based on real feedback. I follow a 'fail fast' mindset—getting something functional out early allows me to validate assumptions, adjust course if needed, and ultimately deliver better results in less time.

## What's your greatest weakness?

One area I’ve been working on is improving my concentration when handling multiple tasks. I’ve noticed that when I have several things on my plate, I sometimes switch between them too frequently, which affects my focus. To manage this, I’ve started using the Pomodoro technique—it helps me stay locked in on one task at a time and maintain better productivity throughout the day.

## Team work: Tell me about a time when you faced a problem you couldn’t solve yourself.

Early in my career, I encountered a complex data quality issue that was affecting our training pipeline. The training dataset prepared from ClickHouse has fewer rows per day than the Kafka data source, indicating a bug in our Kafka data preparation pipeline. Despite multiple attempts, I couldn't identify the root cause alone. I realized that support from a data engineering team was necessary, so I approached senior team members and proposed forming a cross-functional task force to investigate further. By leveraging their expertise and collaborative problem-solving, we were able to uncover a system integration issue that was corrupting our data. This experience taught me the value of teamwork and diverse perspectives in overcoming challenges. The root cause was related to how we handled unregistered users.

## Communication Tell me about a time when it was hard to communicate the importance of the task to the tech team?

In a past role as a data team product owner, I was responsible for setting up a new data governance rules. To make it work, I needed support from the tech team to follow data rules and standards. Initially, I faced resistance as the tech team prioritized other pressing issues. To communicate the importance effectively, I scheduled a series of one-on-one meetings with key stakeholders from the tech team. During these meetings, I emphasized how improved data governance would streamline workflows and enhance data reliability for their projects. By demonstrating empathy and aligning the benefits with their goals, I successfully gained their support and cooperation.

## Handling Negative Feedback Tell me about a time when you got negative feedback.

How did you deal with it? During a project presentation, I received constructive feedback from stakeholders regarding the visual clarity of our data visualizations. Initially, I felt disappointed as I had put significant effort into the design. However, I recognized the opportunity to improve. I scheduled a follow-up meeting with the stakeholders to delve deeper into their expectations and preferences. I then revised the visualizations accordingly, incorporating their feedback. This experience reinforced my belief in the value of iterative improvement and listening actively to stakeholder needs.

## Anticipating Problems tell me about a time when you anticipated potential problems and developed steps to avoid them.

In a data migration project, I proactively anticipated potential data integrity issues due to the complexity of merging legacy databases. To mitigate risks, I conducted thorough data profiling and developed a comprehensive data validation plan before initiating the migration. This involved running extensive data quality checks and creating fallback strategies in case of discrepancies. As a result, we successfully completed the migration within the timeline and minimized disruptions to business operations. This experience underscored the importance of foresight and meticulous planning in mitigating project risks.

## Can you describe a challenging situation you faced at work and how you handled it?

In my previous role as a data analyst, we noticed a significant drop in our metric for recommended item views. Upon investigation, we found that this decline was not random, but rather specifically associated with certain dates. As a data analyst, my task was to identify the cause of this issue, rectify it, and ensure the recovery of our metrics. I started by grouping the data by 'app_version' attribute and discovered a pattern - the metrics dropped on specific dates that coincided with the release of new application versions. This led us to believe that the issue was tied to the new releases. We then worked closely with the application development team to identify and rectify the issues within the new releases. After rectifying the issues in the new application versions, our metrics for recommended item views showed a significant recovery. This incident not only improved our metrics but also highlighted the importance of thorough checks and test runs before releasing any new application versions. It was a valuable learning experience for the entire team about the potential impact of application updates on user metrics.

## Can you describe a challenging situation you faced at work and how you handled it?

I was responsible for developing and monitoring the performance of a recommendation system in a production environment. The Recall@5 metric was implemented to evaluate the effectiveness of the recommendation system. The task was to ensure that the Recall@5 metric reflected the system's performance accurately. However, upon deployment, it was observed that the metric in production was showing lower values than expected. I investigated the issue and identified a specific cohort of users who were experiencing low Recall@5 metrics. Further analysis revealed that this cohort consisted of un-authorized users. Upon closer examination, I discovered that for this particular cohort, feedback data (content likes) was not being sent to Kafka, causing the recommendation system to perform poorly for these users. I took immediate action and documented my findings to provide clear insights into the issue. By identifying the root cause of the low Recall@5 metric, which was the lack of feedback data for the un-authorized user cohort, I could effectively communicate the issue to the development team. I wrote a detailed bug report outlining the specific problem and provided recommendations for addressing the issue in the codebase. The development team used the information provided to implement a fix, ensuring that the feedback data for un-authorized users was correctly sent to Kafka. As a result, the recommendation system's performance improved for this cohort, leading to an increase in the Recall@5 metric in production.

## Tell me about a time you failed and what you learned from it.

I joined the company as the ML team lead, having been informed during the hiring process that the current lead would receive a promotion to the next grade. The task was to assume the role of ML team lead and oversee the team's projects, meetings, and backlogs effectively. However, upon starting the role, I discovered that the promised promotion for the current lead did not materialize, and they continued with daily responsibilities such as attending meetings and managing backlogs. I assessed my career goals and ambitions, considering the option to become a senior engineer instead of staying in a leadership role without the promised promotion. Recognizing my desire for people management and the potential limitations of my current position, I made the decision to leave the company. Leaving the company was a strategic decision aligned with my career aspirations and the pursuit of a role that allowed more focus on people management. This choice allowed me to explore opportunities elsewhere where I could contribute to both technical and leadership aspects, aligning with my career goals.

## Adapting to Changing Requirements.

In a previous role as a product manager, I faced a tight deadline when a client requested a tool to monitor out-of-stock inventory items. Unfortunately, our frontend engineer left the company just as the deadline was approaching. To meet the client's needs while working within the constraints, I proposed an alternative solution. Instead of developing a full web application, I offered a pre-configured report with the necessary columns that the client required. This allowed us to deliver the core functionality they needed, without the complexity of building an interface from scratch, and we were able to meet the deadline.

## Give an example of how you handled tight deadlines.

In one of my projects, I was expected to deliver a machine learning–based assistant that could suggest relevant items to users based on their input. The timeline was very tight, and there wasn’t enough time to design, train, and integrate a fully working ML model from scratch. My task was to deliver a working prototype of this assistant under a tight deadline, while ensuring that the suggestions it provided were accurate and helpful to the users. Instead of going the ML route right away, I assessed the available tools and realized we already had a well-structured ElasticSearch setup in place. I decided to reuse it and built a lightweight layer that translated user input into search queries. By tuning the query scoring and leveraging full-text search with filters, I was able to get relevant results without building a model. As a result, I delivered a fully working assistant ahead of the deadline. It met the key business needs, was easy to iterate on, and gave us more time to explore ML-based improvements later on. The team was impressed by how quickly we had something useful in production.

## Tell me about a time when you had to deliver a project under a tight deadline.

A product team needed a last-minute feature for a major launch, but we had only a week to implement it. I had to design and deliver the feature without compromising code quality. I collaborated with stakeholders to prioritize essential functionality, used feature flags to roll out changes incrementally, and worked with QA to parallelize testing.The feature launched on time with no critical bugs, and the approach became a template for future urgent tasks.

## Give an example of a time you had to troubleshoot a production issue.

A real-time recommendation engine started returning empty results, impacting user engagement. I needed to identify and resolve the issue quickly. I traced logs, found a mismatch between the indexing process and the query format, and deployed a hotfix while reindexing the data. The system recovered within an hour, and I later improved our CI/CD pipeline to catch such issues earlier.

## Describe a time when you had to manage a difficult stakeholder.

A client insisted on an unrealistic feature that would have delayed the project significantly. I had to manage expectations and find a viable solution. I presented alternative approaches, backed by impact analysis, and proposed a phased rollout with incremental improvements. The client agreed to a compromise, and we delivered an MVP on time while planning further enhancements.

## Learning a New Technology Quickly.

you ever had to learn a new technology on the job? Our analytics team adopted Polars, but no one had prior experience. I had to quickly get up to speed and help the team integrate it. Use claude to rewrite current pandas pipeline using polars. We successfully deployed our first Polars pipeline, reducing memory pressure by 60%.

## Describe a time when you had to mediate a conflict between team members.

Two engineers disagreed on whether to use Airflow or Dagster for a new data ingestion pipeline. I needed to ensure the team made a decision based on technical merit.  I organized a structured debate, gathered performance benchmarks, and facilitated consensus-building. We chose Dagster for simplicity, and the decision process improved team collaboration.

## Have you ever optimized a system for better performance?

A batch job processing user transactions was taking over 12 hours to complete. I needed to reduce processing time to meet SLA requirements. I identified bottlenecks, parallelized processing, and optimized database queries.Processing time dropped to 2 hours, improving data freshness for stakeholders.

## Have you ever dealt with a security vulnerability?

A routine audit uncovered a misconfigured S3 bucket exposing user data.  I had to mitigate the issue immediately and prevent future risks.  I restricted access, rotated credentials, and implemented automated security scanning. No data was compromised, and security audits became part of our development lifecycle.

## Have you ever improved a process in your workplace?

We had a custom reporting system, and every new report request created a heavy workload for both designers and front-end developers. Each iteration required a lot of time and manual effort. My goal was to reduce the overhead of building custom reports while still giving stakeholders the insights they needed. I proposed building an MVP version of the reports using Metabase, an open-source analytics tool. This allowed us to quickly generate visualizations and dashboards based on existing data without involving design or front-end teams. This approach significantly sped up the reporting process. Stakeholders were able to explore data on their own and better understand the available metrics. It reduced the number of custom report requests and gave the team more time to focus on higher-impact work.

## Why did you leave your last job?

I decided to leave my previous role because it wasn’t an ML-first environment—machine learning tasks were often de-prioritized in favor of other initiatives. My goal is to join a company where machine learning is a core part of the product and directly contributes to business outcomes, ideally with models that drive a measurable portion of the company’s revenue.

## Describe a situation where you had to work with a difficult coworker.

In my previous role, I worked with a colleague who frequently scheduled same-day meetings without prior notice. This made it challenging to prepare and often disrupted focused work. To address the issue, I initiated a one-on-one conversation and explained that having a clear agenda and at least a day’s notice would help make our meetings more productive. We agreed on some simple communication guidelines, and as a result, our collaboration became much smoother and more efficient, which also had a positive impact on the broader team dynamic.

## What's your leadership style?

I would describe my leadership style as results-oriented. I believe that effort is important, but ultimately it's the outcomes that matter. I focus on empowering team members to make decisions within their areas of expertise while providing clear guidance and support when needed. I also emphasize setting measurable goals and regularly tracking progress to ensure we stay aligned and on target. This approach helps the team stay focused, accountable, and motivated to deliver impact.

## How do you stay updated with industry trends and developments?

I stay updated with industry trends by following thought leaders on LinkedIn and subscribing to several high-quality Substack newsletters that cover topics like AI, data science, and product strategy. I’m also active in professional communities, where I engage in discussions and learn from peers. Additionally, I make it a priority to take online courses and certifications—especially in the GenAI space—to stay current with the latest tools and developments.

## Why do you want to work here?

I want to work here because I admire your focus on innovation and making a difference in the world. I’ve heard great things about how you support employee growth, which fits well with my career goals. I'm excited to use my skills and be part of a motivated team.

## What is your preferred work style: working independently or in a team?

I’m mostly a team player. I believe teamwork brings more value than working alone. My approach is to build an MVP on my own first, and then collaborate closely with the team to bring it to production.

## How do you handle ambiguity and uncertainty in a project?

I thrive in ambiguous situations by breaking down complex problems into smaller, manageable tasks. I make sure to do thorough research and consult with team members to gather insights and make informed decisions. My ability to stay adaptable and calm under uncertainty has helped me navigate challenging projects successfully.

## Describe a situation where you had to persuade a team to adopt your idea.

In a previous role, I proposed a new way to store SQL templates for research purposes. Instead of keeping them in Jupyter notebooks, I suggested storing them in SQL files. To persuade the team, I prepared a demo to highlight the benefits, presented a clear plan for updating the entire codebase with the new approach, and encouraged team members to share their input. By addressing concerns and demonstrating the positive impact, we were able to make our research repo more organized and structured.

## How do you prioritize tasks when you have multiple deadlines?

I prioritize tasks by evaluating their urgency and importance. I create a task list, set deadlines, and break larger projects into smaller, manageable steps. I confirm my priorities with stakeholders, delegate when possible, and conduct regular progress checks to ensure all deadlines are met.

## Can you discuss a situation where you had to make a difficult decision at work?

I was once tasked with deciding how to run an A/B testing system: either adapt an existing solution or develop our own. After conducting a thorough analysis, I made the tough decision to adopt the existing solution, even though it required more upfront costs for the team. In the end, the project was successfully launched, and we saved a significant amount of engineering hours on ongoing support.

## How do you handle a team member who is not meeting their goals or expectations?

When faced with a team member who is struggling, I take a proactive approach. I initiate a private conversation to understand their challenges, offer support, and set clear expectations. If the issues persist, I work with them to develop an improvement plan and provide ongoing feedback and coaching.

## What do you consider your most significant professional achievement?

My most significant professional achievement was leading a cross-functional team as a product owner to successfully launch a data product that reduced time to market by 30%. Although we were slightly behind schedule since it was my first product, the project still had a strong positive impact on the organization. It highlighted my leadership and project management skills and taught me valuable lessons for future launches.

## What's your approach to setting and achieving career goals?

My approach to career goals is to set SMART goals—Specific, Measurable, Achievable, Relevant, and Time-bound. I break big goals into smaller, actionable steps and regularly check my progress. I also look for mentorship and learning opportunities to stay on track and keep growing professionally.

## Can you provide an example of a time you had to lead a team through a crisis?

I once led a team through a crisis when a key team member had to take unexpected medical leave during a critical phase of a project. I quickly reassigned tasks, adjusted the timelines, and kept stakeholders informed about the situation. By staying focused and making the most of the team’s strengths, we were able to manage the crisis effectively and deliver the project on time.

## How do you stay organized and manage your time effectively?

I stay organized by using a mix of digital tools and time management strategies. I keep a detailed calendar, set clear priorities, and block time for specific tasks. I also use the Pomodoro Technique to stay focused and maintain productivity throughout the day.

## How do you handle a situation where you disagree with your supervisor's decision?

When I disagree with a supervisor’s decision, I handle it with respect and professionalism. I first try to understand their perspective by asking for clarification. Then, I share my viewpoint along with any supporting evidence and suggest alternatives if appropriate. In the end, I respect their final decision and continue working as a supportive team member.

## How do you handle a situation where a project is falling behind schedule?

When a project is falling behind schedule, I act quickly to understand the root causes of the delay. I reassess priorities, reallocate resources if needed, and create a clear recovery plan. I also keep stakeholders informed with honest updates and explain the steps we’re taking to get the project back on track.

## How do you handle high-pressure situations, such as tight deadlines or unexpected crises?

In high-pressure situations, I stay calm and focused by prioritizing tasks and breaking them into manageable steps. I communicate clearly with the team to keep everyone aligned, and I rely on my problem-solving skills and experience to make quick, informed decisions.

## Can you discuss a time when you had to work on a project with limited resources?

In a previous role, we had a project with only one ML engineer available. To make the most of our limited resources, I decided to postpone building a full ML platform and instead focused on using our existing infrastructure. By aligning the project scope with available skills and tools, we were able to deliver a successful outcome within the constraints.

