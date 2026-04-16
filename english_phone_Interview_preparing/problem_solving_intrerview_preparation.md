# References

For start


* [McKinsey Problem Solving](https://www.mckinsey.com/careers/interviewing#)
* [Bain Case Interview](https://www.bain.com/careers/interview-prep/case-interview/)

Recommended videos that are easy to follow and good for multitasking:

* [How to succeed in your problem-solving Interview | Revolut Careers](https://www.youtube.com/watch?v=qX-WFS03kmo)
* [How to structure your answer | Revolut Careers](https://www.youtube.com/watch?v=USGud2cinco)
* [How to think like a consultant | Revolut Careers](https://www.youtube.com/watch?v=J7D04PW0xmk)
* [How to communicate your answer | Revolut Careers](https://www.youtube.com/watch?v=orsNS3YG_KE)

Useful Links: 

* [Bulletproof Problem Solving](https://bulletproofproblemsolving.com/)
* [What is the MECE Principle? Understanding Mutually Exclusive, Collectively Exhaustive](https://strategyu.co/wtf-is-mece-mutually-exclusive-collectively-exhaustive/)
* [MECE Framework McKinsey](https://www.mbacrystalball.com/blog/strategy/mece-framework/)
* [Spotify podcast - Former Head of Recruitment explaining our PS interview](https://open.spotify.com/episode/7yP4IdMFeMe4jr2ZgQg1wO?si=Rm1E7aHySS2ZS9-7oF6EeQ&nd=1&dlsi=5f94721d571e4999)

Not related to problem but also useful

[Product function here at Revolut](https://www.youtube.com/watch?v=-kPpd21bFrE)


# Five-day intensive prep for Revolut's ML/AI problem-solving interview

**A structured case interview has never been your world — but in five days, it can be.** This plan transforms an experienced ML/AI project manager with strong technical skills into a candidate who structures problems with MECE precision, communicates recommendations top-down, and demonstrates the ownership-driven thinking Revolut demands. Each day builds on the last: foundations first, then frameworks, then full-case simulations under time pressure. The plan specifically targets your two weaknesses — problem structuring and recommendation delivery — with daily drills designed to rewire how you think out loud.

Revolut's problem-solving interview borrows heavily from McKinsey and Bain case formats but diverges in critical ways: it's more execution-oriented, obsessed with ownership ("what would you actually do?"), and anchored in fintech/ML contexts rather than abstract business scenarios. The five core Revolut values — Never Settle, Think Deeper, Get It Done, Dream Team, and Deliver WOW — directly shape how interviewers score you.

---

## Day 1: Rewire your thinking with MECE and issue trees

**Morning (2–3 hours): Learn the core structuring frameworks**

Start with the foundation that underpins every consulting-style case: the **MECE principle** (Mutually Exclusive, Collectively Exhaustive), developed by Barbara Minto at McKinsey in the late 1960s. Every bucket in your problem breakdown must have zero overlap (ME) and cover all possibilities (CE). This principle isn't optional at Revolut — candidates who succeed consistently report using MECE as their primary structuring tool.

Learn these six strategies for building MECE structures:

- **Binary split ("X" and "Not X")**: The simplest guaranteed-MECE structure. "Internal factors vs. external factors" or "controllable vs. uncontrollable."
- **Mathematical formulas**: Automatically MECE. Profit = Revenue − Costs. Revenue = Price × Volume. Use these as scaffolding.
- **Process/sequence breakdown**: Stages in a pipeline. For ML: data collection → feature engineering → model training → validation → deployment → monitoring.
- **Segmentation by dimension**: Geography, customer segment, time horizon, product line.
- **Conceptual pairs**: Supply vs. demand, quantitative vs. qualitative, cost vs. benefit.
- **Catch-all "other" bucket**: When you can't fully enumerate, add "other" to guarantee exhaustiveness.

Build your first issue tree. Take the problem "ML model accuracy has dropped 8% in the last quarter" and decompose it:

```
Model accuracy decline
├── Data issues
│   ├── Training data quality degradation
│   ├── Data drift (distribution shift in production)
│   └── Feature pipeline failures
├── Model issues
│   ├── Model staleness (concept drift)
│   ├── Hyperparameter suboptimality
│   └── Architecture limitations for new patterns
└── Infrastructure/deployment issues
    ├── Serving environment changes
    ├── Preprocessing inconsistencies (training-serving skew)
    └── Resource constraints affecting inference
```

**Afternoon (2–3 hours): Learn the Bulletproof 7-step process and hypothesis-driven thinking**

Charles Conn and Robert McLean's *Bulletproof Problem Solving* codifies the McKinsey approach into seven steps. Internalize this sequence — it maps directly to how Revolut's problem-solving interview flows:

**Step 1 — Define** the problem precisely (concrete, measurable, time-bound). Revolut's own culture page states: *"We always start with a problem definition. We always ask: 'What is the exact problem that you are trying to solve?'"* This is not generic advice — it's literally how they think.

**Step 2 — Disaggregate** using logic trees (the MECE work you learned this morning).

**Step 3 — Prioritize** by pruning branches. Apply the **80/20 rule**: which 20% of factors drive 80% of impact? This is where hypothesis-driven thinking enters. Form an educated guess about the root cause, then test it.

**Step 4 — Workplan** what analyses you'd run. In an interview, this means telling the interviewer: "I'd want to look at X first because my hypothesis is Y."

**Steps 5–7 — Analyze, Synthesize, Communicate**. Analysis means running the numbers and interpreting data. Synthesis means connecting individual findings into a coherent story. Communication means leading with your recommendation and supporting it with evidence.

**Hypothesis-driven thinking** is the single biggest mindset shift for technical people. Instead of exhaustively exploring every branch (how engineers think), you form an initial hypothesis and then seek to confirm or refute it. This is faster, more focused, and exactly what interviewers want to see.

**Evening practice exercise (1 hour):**
Write out MECE issue trees for these three problems (spend 3 minutes per tree, then 5 minutes refining each):
1. "Revolut's customer acquisition cost has doubled in the last 6 months"
2. "Our fraud detection model's false positive rate is too high"
3. "ML team velocity has decreased by 30% quarter-over-quarter"

For each tree, write one sentence stating your initial hypothesis about the most likely root cause, and explain which branch you'd investigate first and why.

---

## Day 2: Master communication structures and the top-down recommendation

**Morning (2–3 hours): The Pyramid Principle and top-down communication**

Your biggest weakness is communicating recommendations clearly. Technical people instinctively present information bottom-up: data → analysis → conclusion. Consulting communication inverts this using Barbara Minto's **Pyramid Principle**: conclusion first, then supporting arguments in MECE groups, then evidence.

**The synthesis formula you must memorize and drill:**
1. **Restate the question** (one sentence — proves you understood the problem)
2. **State your recommendation** (one decisive sentence — no hedging)
3. **Support with 2–3 reasons** (each backed by specific evidence from your analysis)
4. **Acknowledge risks and outline next steps** (shows mature, practical thinking)

**Example of what bad looks like** (technical person's default):
*"So I looked at the data pipeline and found some issues with feature freshness, and then I checked the model performance metrics over time, and there was also this thing with the serving infrastructure... so I think maybe we should retrain the model and also fix the pipeline."*

**Example of what good looks like:**
*"I recommend we prioritize fixing the data pipeline before retraining the model, for three reasons. First, our feature freshness has degraded from real-time to 6-hour lag, which directly explains 60% of the accuracy decline based on our feature importance analysis. Second, retraining on stale features would waste 2–3 engineering weeks without addressing the root cause. Third, fixing the pipeline is a 1-week effort that also prevents future recurrences. The main risk is that the remaining 40% accuracy gap may require model architecture changes, so I'd recommend reassessing after the pipeline fix ships."*

**Key communication rules for technical people:**

Signpost every transition. Say "First, I'll look at revenue drivers. Then, I'll examine the cost structure." This simple habit alone dramatically improves perceived structure. **Never go silent** — Bain's explicit advice is that silence is risky in case interviews; narrate your thought process even when uncertain. After every analytical step, answer the **"so what?"** question: what does this number mean for the business decision? McKinsey interviewers say the insight is what gets you hired, not the math itself. Finally, **never say "it depends"** without immediately following it with "but given what we know, I'd recommend X because..."

**Afternoon (2–3 hours): Practice the full case flow end-to-end**

Learn the 5-step case interview flow and practice it with your first ML/AI case:

**Step 1 — Listen and clarify** (2 minutes). Restate the problem. Ask 2–3 targeted questions to bound the problem: What metric defines success? What's the timeline? What constraints exist?

**Step 2 — Present your framework** (2 minutes). Take 60–90 seconds of silence to build your MECE structure. Then present it: "I'd break this into three areas: first, X; second, Y; third, Z. I'd start with X because my hypothesis is..."

**Step 3 — Analyze** (15–20 minutes). Work through the interviewer's questions. Structure math before calculating. Interpret every number.

**Step 4 — Synthesize** (ongoing). After each analysis section, connect findings back to your hypothesis. Refine it as you learn more.

**Step 5 — Recommend** (2 minutes). Use the synthesis formula above.

**Evening practice exercise (1.5 hours): Case #1 — ML model prioritization**

**Case prompt:** *"You're leading Revolut's ML team. You have capacity for 2 projects this quarter but 5 competing proposals: (A) improving fraud detection accuracy by 3%, (B) building a customer churn prediction model, (C) automating KYC document verification, (D) personalizing in-app investment recommendations, (E) deploying an LLM-powered customer support chatbot. How would you prioritize?"*

**Worked solution approach:**

**Clarify:** Ask — What is Revolut's primary business objective this quarter (growth, profitability, compliance)? What is the current team composition (NLP specialists, CV engineers, classical ML)? Are there regulatory deadlines? What's the expected revenue or cost impact of each?

**Framework (MECE):**
```
Prioritization criteria
├── Business impact
│   ├── Revenue uplift potential (quantified)
│   ├── Cost reduction potential (quantified)
│   └── Regulatory/compliance risk mitigation
├── Feasibility
│   ├── Technical complexity and team capability match
│   ├── Data readiness
│   └── Time to production deployment
└── Strategic alignment
    ├── Alignment with quarterly OKRs
    ├── Competitive differentiation
    └── Platform/infrastructure reusability
```

**Hypothesis:** Fraud detection improvement (A) and KYC automation (C) likely rank highest because they directly reduce financial losses and compliance risk — Revolut's most existential concerns as a regulated fintech.

**Analysis:** Score each project on a **2×2 matrix of impact vs. feasibility**. Fraud detection (A): high impact (3% accuracy improvement on a model processing millions of transactions could save £5M+/year), moderate feasibility (model exists, improvement is incremental). KYC automation (C): high impact (reduces manual review costs, speeds onboarding — critical for growth), moderate-high feasibility (document verification is a well-studied CV/NLP problem). Churn prediction (B): moderate impact (retention matters but Revolut is still in growth mode), high feasibility. Recommendations engine (D): moderate impact, moderate feasibility. Chatbot (E): high visibility but high risk (LLM hallucinations in financial context create compliance exposure).

**Recommendation:** *"I recommend prioritizing fraud detection improvement and KYC automation. First, fraud detection directly protects revenue — a 3% accuracy improvement at Revolut's scale could prevent an estimated £5M+ in annual losses. Second, KYC automation accelerates customer onboarding, which is the growth bottleneck for a company expanding into new markets. Third, both projects leverage existing data infrastructure, making them higher-feasibility than greenfield efforts. I'd deprioritize the chatbot despite its visibility because LLM hallucinations in regulated financial contexts create compliance risk that outweighs the support cost savings. As a next step, I'd validate the £5M fraud estimate with the data team and confirm KYC processing time benchmarks."*

---

## Day 3: Deep-dive into Revolut-specific cases and fintech context

**Morning (2–3 hours): How Revolut's interview differs from McKinsey and Bain**

Understanding these differences is critical. Revolut borrows the MECE structuring and hypothesis-driven approach from consulting but applies a fundamentally different lens:

| Dimension | McKinsey/Bain | Revolut |
|---|---|---|
| **Format** | McKinsey: interviewer-led; Bain: shifting to interviewer-led | Interviewer-guided but expects strong candidate initiative |
| **Case context** | Any industry (retail, pharma, energy) | Almost always fintech/banking/payments |
| **Evaluation emphasis** | Structured thinking + analytical elegance | Structured thinking + **execution orientation** |
| **"Right answer"** | Process matters more than answer | Process matters, but **actionable answer matters more** |
| **Recommendation style** | "I recommend the client..." (advisory) | **"I would do..."** (ownership language) |
| **Follow-up pressure** | "What else would you consider?" | "How would you actually implement this Monday morning?" |
| **Cultural signal** | Intellectual polish, hypothesis rigor | **Speed, ownership, bias toward action** |
| **Ethical dimension** | Occasionally tested | Always present (financial regulations, AI ethics, data privacy) |

**The three things Revolut's problem-solving interview tests** that consulting interviews don't emphasize as heavily: **ownership mentality** (full accountability for outcomes, not just process), **speed under pressure** (time-boxed thinking, rapid iteration), and **operational specificity** (they want to hear about implementation, not just strategy).

Reported Revolut case topics from Glassdoor and prep forums include: "Revolut trading platform P&L is going down," "Gross profit of credit card business is declining," and funnel optimization cases. The **ICE framework** (Impact, Confidence, Ease) is frequently used by successful candidates for solution prioritization.

**Study Revolut's product ecosystem.** Download the app if you haven't. Understand the core products: multi-currency accounts, card payments, crypto trading, stock trading, insurance, business banking, Revolut Pay, and premium/metal plans. Know the revenue model: interchange fees, subscription tiers, FX markup on weekends, premium features, and crypto spreads.

**Afternoon (2 hours): Cases #2 and #3**

**Case #2 — ML project behind schedule**

**Prompt:** *"You're managing an ML project to build a real-time transaction risk scoring model for Revolut. The project is 4 weeks behind the 12-week schedule, with 6 weeks remaining until the regulatory deadline. The model's precision is at 0.78 vs. the 0.85 target. The data engineering team is blocked on a schema migration, and two ML engineers just got pulled to support a production incident. What do you do?"*

**Framework:**
```
Project recovery strategy
├── Scope management
│   ├── Minimum viable model (what precision is acceptable for launch?)
│   ├── Feature scope reduction (fewer features, simpler model)
│   └── Phased rollout (shadow mode first, full deployment later)
├── Resource optimization
│   ├── Unblock data engineering (parallel workaround or priority escalation)
│   ├── Temporary resource reallocation (borrow from lower-priority projects)
│   └── External support (contractors, vendor solutions for components)
└── Risk mitigation
    ├── Regulatory communication (can deadline flex? what are consequences?)
    ├── Fallback plan (rules-based system as interim)
    └── Stakeholder alignment (reset expectations with specific timeline)
```

**Recommendation:** *"I'd take three immediate actions. First, reduce scope to a simpler model architecture — likely gradient-boosted trees instead of a deep learning approach — targeting 0.82 precision, which I'd negotiate with compliance as acceptable for initial shadow-mode deployment. Second, I'd escalate the schema migration blocker to the VP of Engineering today, because this is on the critical path and the data team can't unblock themselves. Third, I'd request one ML engineer back from the production incident team within 48 hours, proposing that the remaining incident work be handled by the on-call rotation. The fallback plan if we can't hit 0.82 is a hybrid system: rules-based engine for high-confidence transactions, ML model for the ambiguous middle band. I'd present this recovery plan to stakeholders within 24 hours with revised milestones."*

Notice the **ownership language**: "I'd take," "I'd escalate," "I'd request." Not "the team should consider" or "it might be worth exploring."

**Case #3 — Build vs. buy ML infrastructure**

**Prompt:** *"Revolut's ML team currently uses a patchwork of internal tools for model training, deployment, and monitoring. An ML platform vendor offers an enterprise solution for $2M/year. Your internal platform team estimates building equivalent functionality would take 8 engineers 12 months (~$2.4M fully loaded cost). How would you advise?"*

**Framework:**
```
Build vs. buy decision
├── Cost analysis (TCF: Total Cost over 3 years)
│   ├── Buy: $6M licensing + integration costs + vendor lock-in switching costs
│   ├── Build: $2.4M development + ongoing maintenance (typically 20-30% of build cost/year)
│   └── Hidden costs: training, migration, productivity loss during transition
├── Capability fit
│   ├── Feature coverage (does vendor solve 80% or 100% of needs?)
│   ├── Customization requirements (fintech-specific: compliance logging, audit trails)
│   └── Scalability trajectory (Revolut's growth rate vs. vendor's scaling model)
├── Strategic factors
│   ├── Core competency argument (is ML platform a competitive differentiator?)
│   ├── Speed to value (vendor: 3 months; build: 12 months)
│   └── Talent retention (engineers prefer building to configuring vendor tools)
└── Risk factors
    ├── Vendor reliability and financial stability
    ├── Data sovereignty and regulatory compliance
    └── Migration risk from current patchwork
```

**Recommendation:** *"I recommend a hybrid approach: buy the vendor platform for immediate deployment while building two critical custom components — the compliance audit trail and the real-time feature store — that the vendor doesn't adequately support. Here's why. First, the 9-month speed advantage of buying ($2M) outweighs the cost premium over building ($2.4M), because every month without a proper platform costs productivity — I'd estimate 15-20% of ML team capacity is currently lost to tooling friction, which at $3M annual team cost equals ~$450K in wasted productivity over 9 months. Second, Revolut's regulatory environment requires custom compliance logging that no vendor fully supports. Third, the feature store is a genuine competitive differentiator for real-time ML at scale. The key risk is vendor lock-in, which I'd mitigate by requiring an abstraction layer over the vendor's APIs from day one. Total 3-year cost: approximately $7.5M hybrid vs. $6M pure buy vs. $4.8M pure build — but the hybrid delivers value 9 months earlier and covers compliance gaps."*

**Evening practice exercise (1.5 hours):**
Re-do Cases #2 and #3 from memory without looking at the worked solutions. Time yourself: 3 minutes to structure, 10 minutes to analyze, 2 minutes to recommend. Record yourself delivering the recommendation and listen back — are you leading with the answer? Are you using ownership language? Are you under 2 minutes?

---

## Day 4: Advanced cases, ethical dimensions, and pressure testing

**Morning (2–3 hours): Cases #4 and #5**

**Case #4 — Data quality crisis during model training**

**Prompt:** *"Your team is 3 weeks into training Revolut's new credit risk model. A data engineer discovers that 18% of the training data has incorrectly labeled outcomes — customers marked as 'defaulted' who actually didn't, due to a bug in the payment reconciliation system that was fixed 2 months ago. The model is showing surprisingly good validation metrics. What do you do?"*

**Framework:**
```
Data quality crisis response
├── Immediate assessment
│   ├── Scope of contamination (which time periods? which customer segments?)
│   ├── Impact on model validity (are the "good" metrics actually artifacts of label noise?)
│   └── Downstream exposure (has any contaminated model been serving in production?)
├── Technical remediation
│   ├── Data correction feasibility (can labels be retroactively fixed?)
│   ├── Retraining requirements (full retrain vs. fine-tuning on corrected data)
│   └── Validation strategy (hold-out set from clean data period only)
├── Process and governance
│   ├── Root cause analysis (why wasn't this caught earlier?)
│   ├── Data quality monitoring gaps to close
│   └── Model validation protocol updates
└── Stakeholder communication
    ├── Compliance/risk team notification (regulatory implications)
    ├── Timeline impact to leadership
    └── Remediation plan with milestones
```

**Key insight to demonstrate:** The "surprisingly good validation metrics" are a red flag, not a positive signal. When 18% of defaults are mislabeled as non-defaults, the model learns that certain high-risk patterns are "safe" — it's essentially being trained to approve risky customers. The validation metrics look good because the validation set has the same label corruption. This is **worse than low accuracy** — it's systematically biased toward approving bad credit risks.

**Recommendation:** *"I'd halt model deployment immediately and take three actions. First, quarantine the current model — under no circumstances should it reach production, because the 'good' validation metrics are actually an artifact of label corruption. The model has learned to approve high-risk customers, which could cost Revolut millions in defaults. Second, I'd initiate a data correction sprint: work with the data engineering team to re-derive correct labels using the fixed reconciliation system, targeting completion in one week. Third, I'd notify the compliance team proactively — in a regulated financial institution, training a credit model on known-corrupted data without disclosure is a regulatory risk even if the model never reaches production. The timeline impact is approximately 2–3 weeks to retrain and revalidate on corrected data. To prevent recurrence, I'd implement automated label distribution monitoring that flags statistical anomalies in training data before model training begins."*

**Case #5 — Stakeholder alignment on AI ethics**

**Prompt:** *"Revolut's product team wants to use an ML model to automatically decline loan applications. The model performs well on aggregate metrics (AUC 0.92) but your analysis reveals it has a 23% higher false rejection rate for customers in certain geographic postcodes that correlate strongly with ethnic minority communities. The product team argues the model uses no demographic features directly. The business team says launching quickly is critical for Q3 revenue targets. How do you handle this?"*

**Framework:**
```
AI ethics and fairness decision
├── Technical assessment
│   ├── Proxy discrimination analysis (which features correlate with protected attributes?)
│   ├── Fairness metrics across subgroups (equalized odds, demographic parity, calibration)
│   └── Mitigation options (re-weighting, adversarial debiasing, threshold adjustment)
├── Regulatory and legal exposure
│   ├── EU AI Act compliance (high-risk AI system classification)
│   ├── UK Equality Act implications
│   └── FCA expectations on algorithmic fairness in lending
├── Business impact analysis
│   ├── Revenue impact of delay vs. regulatory fine/reputational risk
│   ├── Customer trust and brand implications
│   └── Competitive positioning (fair AI as differentiator)
└── Stakeholder alignment strategy
    ├── Framing for product team (not about blame, about risk mitigation)
    ├── Framing for business team (quantify downside risk vs. launch delay cost)
    └── Escalation path (who makes the final call?)
```

**Recommendation:** *"I would not launch the model in its current form, and I'd frame this as a business risk decision, not an ethics debate. Here's why. First, the EU AI Act classifies credit scoring as high-risk AI, requiring documented fairness assessments before deployment — launching with known disparate impact creates regulatory exposure that dwarfs Q3 revenue gains. Second, if this bias becomes public, reputational damage to Revolut could cost significantly more than a 4–6 week delay. Third, the technical fix is achievable: postcode and correlated proxy features can be identified using SHAP values, and techniques like adversarial debiasing or calibrated threshold adjustment across subgroups can typically reduce disparate impact by 60–80% with only 1–2% aggregate AUC loss. My proposed path: a 3-week sprint to implement fairness constraints, with a parallel legal review. I'd present this to the business team as 'we launch 3 weeks late with a defensible model' versus 'we launch now with a model that could trigger an FCA investigation.' To align stakeholders, I'd schedule a 30-minute meeting with product, legal, and the business lead this week, presenting the quantified risk comparison."*

**Afternoon (2 hours): Pressure drill and pitfall avoidance**

**Key pitfalls for first-time case interviewers:**

**Pitfall 1 — The "data dump" response.** Technical candidates instinctively share every analytical detail. In a case interview, this signals inability to prioritize. **Fix:** Before speaking, ask yourself "what are the 2–3 things that matter most?" and only share those.

**Pitfall 2 — Generic frameworks.** Interviewers immediately detect recycled Porter's Five Forces or generic profitability trees. **Fix:** Every framework must be tailored to the specific case. Use MECE principles to build bespoke structures, not memorized templates.

**Pitfall 3 — Hedging and "it depends."** Technical people love nuance. Case interviews reward decisiveness. **Fix:** Always take a position. You can acknowledge uncertainty, but you must still recommend a path: "Given the available data, I'd recommend X, with the caveat that Y could change this if..."

**Pitfall 4 — Solving in silence.** Engineers are comfortable with long silent pauses while thinking. Interviewers interpret silence as being stuck. **Fix:** Narrate your thinking: "Let me take 30 seconds to structure this... I'm thinking about breaking this into three areas..."

**Pitfall 5 — Bottom-up presentation.** Starting with data and building to a conclusion. **Fix:** Force yourself to state the answer first, every single time, even if it feels uncomfortable. The Pyramid Principle is non-negotiable.

**Pitfall 6 — Ignoring the "so what."** Computing that costs increased 15% and moving on without interpreting what that means for the decision. **Fix:** After every number, complete this sentence: "This tells us that... and therefore we should..."

**Pitfall 7 — Treating it as a solo exercise.** Case interviews are collaborative conversations. Engaging the interviewer — asking "does that directionally make sense to you?" or "I'd like to dig into costs next, does that seem like the right priority?" — signals you're someone they'd want on their team.

**Evening practice exercise (1.5 hours):**
Do a full timed run of a case you haven't seen before. Use this prompt: *"Revolut wants to expand its ML-powered wealth management product (robo-advisor) from the UK to 5 new European markets. You have a $4M budget and an 8-month timeline. How would you approach this?"* Give yourself exactly 25 minutes: 3 minutes to clarify and structure, 15 minutes to analyze (make assumptions where needed), 2 minutes to recommend, 5 minutes to handle "follow-up questions" you invent for yourself (e.g., "What if the budget is cut to $2M?" or "What's your biggest risk?"). Record yourself and review.

---

## Day 5: Full simulation, polish, and interview-day preparation

**Morning (2–3 hours): Two full-length case simulations**

Run two complete 30-minute case simulations back-to-back, simulating Revolut's actual interview pace. If possible, recruit a friend or colleague to play interviewer. If solo, use a timer and speak every answer out loud as if someone is listening.

**Simulation 1 prompt:** *"Revolut's auto-ML pipeline generates 200+ model experiments per week, but only 3% make it to production. Engineering leadership is frustrated by the resource waste. As the ML PM, how would you diagnose and fix this?"*

Structure this using: funnel analysis (where do experiments drop off?), root cause categories (quality gates too strict? experiment design too broad? production deployment process too slow?), and cost-benefit (is 3% actually a problem, or is high experimentation volume a feature?).

**Simulation 2 prompt:** *"A major Revolut competitor just launched a GPT-powered financial assistant that's generating significant press coverage. Your CEO asks you to present a plan by Friday for Revolut's response. What do you recommend?"*

Structure this using: competitive threat assessment (is this a real threat or marketing?), build vs. partner vs. wait analysis, Revolut-specific advantages (data moat, existing user base, regulatory experience), and risk analysis (LLM hallucinations in financial advice context).

**Afternoon (2 hours): Communication polish and final review**

**Record yourself delivering all 5 case recommendations** from the week. Each should be under 2 minutes. Grade yourself on:

- Did you lead with the recommendation in one clear sentence?
- Did you support with exactly 2–3 reasons (not 1, not 5)?
- Did each reason include specific evidence or numbers?
- Did you include risks and next steps?
- Did you use ownership language ("I would" not "one might consider")?
- Did you avoid filler words and hedging?

**Master these transition phrases** that signal structure:

For starting: *"Let me break this into three areas..."*
For prioritizing: *"I'd start with X because it's the highest-impact lever, and here's why..."*
For pivoting: *"That's what I see on the revenue side. Turning to costs..."*
For synthesizing mid-case: *"So what this tells us so far is that the root cause is likely X, because..."*
For recommending: *"Based on this analysis, I recommend... for three reasons."*
For handling uncertainty: *"I don't have data on X, but based on Y and Z, a reasonable estimate would be..."*

**Evening (1 hour): Mental preparation and logistics**

Review Revolut's five values one final time and prepare a mental checklist for demonstrating each:

**Never Settle** → Push for the best answer, not just a good enough one. When you finish your recommendation, add: "And if we really wanted to go further, we could also..."

**Think Deeper** → Always ask "why" one more time than feels necessary. Question your own assumptions out loud.

**Get It Done** → Every recommendation must include specific implementation steps. "By Monday, I would..." is the language Revolut wants to hear.

**Dream Team** → Show collaborative instincts. "I'd work with the data engineering team to..." and "I'd align with compliance before..."

**Deliver WOW** → Show customer-centricity. Tie ML decisions back to user experience impact.

---

## Quick-reference framework cheat sheet

| Framework | When to use | Structure |
|---|---|---|
| **MECE issue tree** | Breaking down any problem | 3–5 branches, each with 2–3 sub-branches, zero overlap, full coverage |
| **Profitability tree** | Revenue/cost problems | Profit = Revenue (Price × Volume) − Costs (Fixed + Variable) |
| **Hypothesis-driven** | Throughout every case | State hypothesis → test with data → refine → conclude |
| **ICE scoring** | Prioritizing solutions | Impact (1–10) × Confidence (1–10) × Ease (1–10) |
| **2×2 matrix** | Comparing options | Impact vs. Feasibility, Urgency vs. Importance |
| **Build vs. buy** | Technology decisions | Cost (TCO), Capability fit, Strategic value, Risk |
| **Pyramid Principle** | Every recommendation | Answer → 2–3 reasons → evidence → risks → next steps |
| **Bulletproof 7-step** | Complex open-ended cases | Define → Disaggregate → Prioritize → Workplan → Analyze → Synthesize → Communicate |

---

## What separates candidates who pass from those who don't

The difference is not analytical horsepower — you already have that. **The difference is visible structure and decisive communication.** Revolut's interviewers are evaluating whether they'd trust you to run a room with engineers, data scientists, and business stakeholders. That trust comes from watching you take an ambiguous, messy problem and, in real-time, turn it into a clear framework, test hypotheses efficiently, and deliver a recommendation that sounds like a plan someone could execute tomorrow morning.

The interviewers aren't looking for the "right" answer. They're looking for a thinking process they can follow, a recommendation they can challenge, and a candidate who responds to pushback by refining their position rather than abandoning it. Every hour of practice this week should serve that goal: structure visibly, recommend decisively, own the outcome completely.

# Revolut — Problem Solving Interview: Candidate Prep Guide

---

## Why is problem solving important at Revolut?

At Revolut, we place a strong emphasis on problem-solving, considering it a core value that underpins our entire company culture. Our "Think Deeper" value encourages our team members to approach challenges with a critical eye and an unwavering determination to dive deeper into issues to uncover unique solutions. We firmly believe that our ability to solve complex problems distinguishes us from our competitors and enables us to develop innovative financial solutions that serve our customers' needs.

Our relentless focus on problem-solving has been an integral part of Revolut's DNA from its inception. Despite being told that the problem they were attempting to solve was impossible to achieve, our founding team refused to give up. Instead, they approached the problem from first principles, questioning every assumption and analysing every detail with a rigorous process that ultimately led to the creation of the now-famous Revolut solution.

As we strive to build the world's first financial superapp, we continue to push the boundaries of what is achievable in the industry. Of course, this ambitious goal presents significant challenges, but our employees confront them head-on every day with a commitment to problem-solving that has become a hallmark of our company.

---

## What to expect at the interview?

The problem you will encounter during the interview is a hypothetical challenge inspired by genuine obstacles that our company has successfully surmounted. Unlike a traditional exam, there are no right or wrong answers — our goal is to gauge your ability to analyse the issue, prioritise actions, and articulate your proposed solutions.

This interview represents an excellent chance for you to engage with us, ask insightful questions, and exhibit your creativity, analytical thinking, and practical problem-solving capabilities. We are eager to witness your problem-solving abilities in action and excited to learn from the unique perspectives and approaches that you bring to the table.

---

## Our Culture & Values

> We believe brilliant people in an empowered culture produce unbelievable success.

Revolut's unique culture is built on five core values. By working to these values every day, we create a fertile environment for success. Our values define 'the Revolut way', and we put them into practice every day across our organisation. They keep us on the right path, motivate us and ensure we hire the best people.

**The five values:** Never Settle · Dream Team · Think Deeper · Get \*\*It Done · Deliver Wow

---

## 1. Never Settle

> We constantly push, rethink, and rework to get 10x further from where we are now. We aren't afraid to be ambitious — and we're always looking for the next big thing.

### Shoot for the moon

- Relentlessly push to become number one in the world. Look for ways to disrupt, scale, reinvent.
- Come up with ideas that are new, better and unique. Be creative — reiterate, simplify, move beyond the traditional way. Connect the dots from different areas, industries, and products.
- Vigorously set ambitious, bold, and rational goals to guide your way.

### Push the envelope

- Constantly change your lens. Challenge solutions from all angles to deliver the best. Run toward critique to advance it even further.
- Recognise and celebrate those who challenge the status quo for the better.
- Pull at every thread. Don't just meet the ask, go above and beyond when solving a problem and never leave loose ends.

### Jump in with both feet

- Enjoy the challenge, celebrate achievements, and have fun.
- Show initiative, inspire others. Enjoy taking on stretch assignments even if they're outside of your core responsibilities.
- Share optimism and confidence. Remain positive and energised when facing adversity.

### Never lose 'North'

- Always think beyond the task at hand, keep the bigger picture in mind. Think several steps ahead. (e.g. Will our solution create more problems? What will the next problem be once we solve this one?). Look for ways to create scalable frameworks and tools to increase the impact.
- Avoid 'analysis paralysis' so that we move toward solutions.
- Focus on the outcome and continue checking your compass along the way (i.e. Are we still going in the right direction?). If not, take courage to start from scratch.

### Be open minded — listen, probe, adjust

- Invite criticism and alternative views to tackle problems better. Constantly challenge assumptions in your thinking. Do not follow any previously agreed upon approach blindly.
- Take turns speaking and listening. Consider all feedback regardless of the person's title. There is no place for politics in Revolut.
- Think through your recommendation, don't say "yes" or "no" too quickly.

---

## 2. Get \*\*It Done

> We believe that ideas are great, but execution is everything. That's why respect at Revolut comes from sweat and stretch.

### Act like an owner

- Own your work and the tasks required end-to-end. Look for answers and solutions, not excuses.
- Assume full responsibility and accountability beyond your role or over expectations. Don't wait for guidance, self-direct.
- It is never "someone else's job or problem".

### Commit and execute

- Bring a can-do attitude at all times. Keep calm when facing challenging work.
- Unblock roadblocks. Break walls. Persevere until the project is finished. Completion is a must. And then iterate.
- Deliver on commitments, instil trust in your go-getter attitude.

---

## 3. Deliver Wow

> We believe that everything we do should solve our customers' needs. To create awe and inspire, we pay attention to every single detail.

### Put customer first

- Put yourself in the shoes of the customer (external or internal) and understand how they are using the product or process, be curious.
- Focus on, and think through every single detail.
- Don't ship anything unless it's ready, fully-baked, tested, and reviewed.

### Keep it simple

- Simplify everything — minimise any friction for the customer. Save time for your customers, your manager, and your stakeholders.
- Make decisions on what to build and what to kill.
- Use language everyone can easily understand. Extract the essence. Lead with the most important information. Bottom line up front.