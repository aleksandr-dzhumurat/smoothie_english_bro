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
| **Think Deeper** | Decisions by logic and evidence, find the root cause | Recall@5 investigation (un-authorized users, Kafka); metrics drop by `app_version`; Kafka vs ClickHouse row count; the nightly challenge-share step (timezone train/serve bug) |
| **Get It Done** | Grit, urgency, full ownership, contingency plans | Elasticsearch assistant under a tight deadline; pre-configured report instead of a web app; ownership of the incident-ranking service; the nightly challenge-share incident response |
| **Deliver WOW** | Simple, high-quality products that make others' work easier | RAG shopping assistant demo; Metabase self-serve reports; LLM standup automation; ranking service that saves incident managers' time |

