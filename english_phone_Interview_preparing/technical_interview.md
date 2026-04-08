# Technical interview

> **Tip 1. Ask clarifying questions about the case**
> 
> In case interviews, the interviewer will begin by stating the problem. It’s quite common to leave out important details when asking candidates to resolve a business problem. 
> 
> Don’t give the answer straight away; take some time to think and ask clarifying questions to demonstrate that you can identify what information is important, and what is not. Don’t be afraid to ask questions that check your understanding — it will help you understand what information the interviewer wants you to provide.

> **Tip 2. Make assumptions** 
> 
> Look for clues in the question, as it will help you solve the problem faster. Remember to justify your assumptions: *“I am going to assume it’s…, because ...”*. 
> 
> You might also want to restate the problem described by the interviewer. This is one of the problem-solving techniques that shouldn’t be underestimated.

> **Tip 3. Walk the interviewer through your thinking process**
> 
> Don’t worry too much about giving the “right” answer. Guide the interviewer though your line of thinking. Give an insight into how you would cope with the problem by sharing your logic and reasoning. 
> 
> Don’t go silent if you are asked a follow-up question that you can’t answer straight away. Saying something like *“That’s a good question”* will give you some time to think about your answer. 
> 
> You may also want to check with the interviewer if what you said makes sense and if your line of thinking is clear to them.

# **Useful language**

**Checking understanding**

- So you’re asking me … right?
- Let me make sure I’ve got it right.
- So, I need to … Is that correct?

**Thinking out loud**

- Well, the first thing I’d probably do is [verb]
- Probably, I’d start by [verb+*ing*]
- What I’m trying to say is …
- Another thing I would consider is [noun/verb+*ing*]
- In addition, …
- Finally, …
- Erm, what else?
- So that’s basically how I would …

**Asking for feedback**

- Does that make sense?
- Does that sound OK?

# Dialog

**Interviewer:**

An online marketplace company has introduced a new feature that allows potential buyers to start an audio chat with the seller before paying for the item they’re interested in. We have two tables that represent this data. How would you measure the efficiency of the new feature?

**Lucas:**

So you’re asking me to what extent a newly introduced audio chats feature has positively influenced the buyer’s decision to make a transaction, right?

**Interviewer:**

Exactly, and we’re taking into consideration only the buyer metrics.

**Lucas:**

Hmm, does this data represent both periods: before and after the feature launch, or only after the launch?

**Interviewer:**

Good question, Lucas. It includes both periods.

**Lucas:**

Well, off the top of my head I’d say that I’d opt for conducting an A/B test since the comparison of data before and after the launch may be affected by seasonality, market conditions or some other external factors. 

If we have neither a controlled group nor a historical period, then the estimation of feature effectiveness could be biased… inaccurate, you know.

**Interviewer:**

Right, fair enough. Although the A/B test hasn’t been run, let’s still compare the data before and after the change considering the dynamics only.

**Lucas:**

I got it, thanks. Well, the first thing I’d probably do is check how many people have used the call option, and it only makes sense to compare the customers who have seen this feature with those who haven’t. 

What I’m trying to say is that this feature might be useful, but if it’s being used by only one percent of people, it won’t affect the overall number. 

On the other hand, it may turn out that it’s popular with the loyal customers only. And if so, then it’s wrong to compare them with the historical period, since it includes both user types — loyal and occasional customers.

**Interviewer:**

All right, valid point. Let’s assume that there’s no difference between the types and we can make this comparison.

**Lucas:**

Sure. Erm.. another thing I would consider is checking whether there’s been a change, at least on average, between the conversion before the change was implemented and after it. 

In addition, I would have a look at the metrics split by item category, platform, and language, since changes can affect different segments of products and users in different ways. 

Then, finally, I would also look at whether the ARPU check has increased on average. Erm, what else? Do you use some special metrics to measure the efficiency?

**Interviewer:**

I’m ok with the conversion and average check metrics.

**Lucas:**

Then it’d be reasonable to consider how unanswered calls affect the conversion. What I’m trying to say is that answered calls increase the conversion greatly, while unanswered ones force the user to leave. In this case, we would have to focus on reducing such cases. 

In general, the feature might be useful, but we’re more likely to lose the client if a call is unanswered. Therefore we should think how we can reduce the “non-connected calls” rate. 

I’d also suggest calculating a cost-benefit analysis of this feature. It might turn out that this feature gives us some profit, but in fact we spend more resources on its development and support. 

So that’s basically how I would go about this case. Does that make sense?

**Interviewer:**

Thank you, Lucas. That was a very interesting and valuable insight. Let’s move on to the next question.

### Useful phrases

Well, the thing is, … → In fact, …

In a nutshell, … → Let me say it in a few words.

Just to give an example. → Let me give you an example.

So, to recap, … → So, to sum up, …

For instance, … → For example, …

As I see it, … → From my point of view, …

I’d say that … → I think that …

That’s a tough question. → That’s a difficult question.

Let me think about this for a second. → Let me just take a moment to consider your question.

Well, off the top of my head, I’d say that … → What comes to mind right away is that …

### Examples

So, to sum up , it’s important to identify any duplicates and validate the accuracy of the data.
Well, off the top of my head, I’d say I first need to track all the operations performed.
OK, let me think about this for a second… For live connection to the data source, I think you can check log.txt and tabprotosrv.txt files.
In a nutshell, if the data gets changed, the model should be able to scale accordingly.
That’s a tough question. I need some time to come up with an answer.
Well, the thing is, when you extract data from sources, the data may vary in representation.
For instance, I can name two types of statistical modeling methods used in data analysis — supervised and unsupervised learning.
Just to give you an example. If you have multiple independent variables like …

From my point of view, we should first identify which model best addresses the question at hand.

As I see it, you can use the simplex algorithm when analyzing this data.

To make sure we are on the same page, let me sum up what we have discussed.

Let me sure I have got it right. You are asking me how I can detect the drop of users in stories?

So, I need to find out why fever people are using stories. Is that correct?

So you’re asking me about some possible reasons, right?

Well, the first thing I would probably do is check how many people use it. Another thing I would consider is checking whether there is been a change.
Does that make sense?
What I’m trying to say is that we should design an experiment.

The problem we are facing here is that this kind of data can’t be managed easily
Well, the very first thing I’d probably do is check whether there’s been a change at least on average level.
Erm, what else? So that’s basically how I’d go about the problem.
Another thing I’d consider is finding the data that builds metrics.
Let me make sure I’ve got it right. We’re talking about important customer acquisition metrics to track, is that correct?
Probably, I’d start by checking if almost all of the data is one class. In addition, I’d check what features are meaningful in the model.
So, I need to come up with a few ideas how I would improve this feature, is that correct?

Could you elaborate on approaches you use?

It all boils down to one single problem. The heart of the matter is that we don’t have enough information.
I can’t underscore enough how important it is.
How does this look to you?
How do you feel about it?
What support do you need?
What would you add or change?
What do you think is best?
how soon you wants the task done?
Let’s me make sure I have got it right.

What’s important is we’d like the date format to be consistent across all the files.
Just to give you a bit of background on the situation, …
How long do you think this will take?
Do you see any blockers to that?
That will enable us to get more accurate information and optimize the process.
So, what we need is to have some sort of integration API.
The problem we’re facing here is that we don’t see what people choose.
The situation as it stands is that we don’t have any insight into that.
This will allow us to process similar requests much faster.

# Technical quiestions

(Ask ChatGPT for the right answers)

[Data Analyst Interview Questions](https://www.youtube.com/watch?v=Qcs7JhutDw0)

# **Tips on describing and explaining a task clearly**

A properly communicated task description will greatly affect the implementation and push the project forward. When explaining a task to a developer or engineer, keep in mind the following:

> **Tip 1**
> 
> You might want to start by describing the current state of things and provide the context for why you need this solution. 
> 
> When outlining the problem, it might be a good idea to illustrate your point with an example — it could help your colleague understand the task.

**Useful language**

- Just to give you a bit of background (on the situation), …
- The problem (we’re facing here) is that …
- The situation (as it stands) is that …

> **Tip 2**
> 
> When describing what exactly needs to be done, justify why it’s necessary or important. You might also want to mention how the project or the product would benefit from it. 
> 
> This could help your team members see the bigger picture and understand how they will contribute to the project success. Come up with relevant and sufficient details to help better understand the underlying logic and the scope of the task.

**Useful language**

- What we need is … (so that we can …)
- What’s important is *[that these events should have certain parameters].*
- This will allow us / enable us to …
- Is that something you can help with?
- Would you be able to …?

> **Tip 3**
> 
> Mention the deadline if there’s any. It’s a good idea to ask colleagues if there’s anything that could prevent them from doing the task.

**Useful language**

- How long do you think it will take?
- Do you see any blockers (to that)?