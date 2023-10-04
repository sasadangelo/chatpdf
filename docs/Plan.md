# AI Experiments Plan

The goal of this file is to document my plans in AI experiments and how to improve the automation of a software organization running using Agile philosophy and DevOps practices. I have divided my plan into possible scenarios that need to be reviewed and prioritized at team level in order to focus on those that can add the most immediate value.

## Agile

Agile like many cultural approach is based on values, principles and practices. Infact, Agile is based on 4 values, 12 principles, and different practices like DevOps, Scrum, Spotify model, etc. In particular, the Scrum framework uses some artifacts like:

1. Product Backlog
2. Scrum Backlog
3. Daily Scrum
4. Sprint Review
5. Sprint Retrospective

I think AI can help a team to improve the management of these artifacts. In this document I am going to consider only 1, 2, aand 3.

### Product Backlog

A chatbot can be used to create Epic and Task on different Product Backlog back end like Jira, ZenHUB, Trello, etc. The basic idea is simple, the user authenticates itself on the chatbot and depending on his role he can create Epic and Task specifying:

* Title
* Description
* Estimation in Story Points
* Dependencies

In any moment, the user can interact with these artifacts using a simple chaatbot interface. He can change the above parameters, add comments, chaange the dependencies and so on. The conversation will be translated in a request for a AIOps server that will interact with the backend system.

### Sprint Backlog

When a new Sprint starts the Scrum Team can prioritize the Backlog by Size and Value. Since the Goal of the Product Owner is to maximize the value of a Product at each Sprint, the Scrum Team will select the Product Backlog items to insert in the Sprint Backlog using aa simple chat interface.

### Daily Scrum

When daily scrums are run online, the team can record the session. Later a pipeline will extraact the audio, convert the audio in text that will be summaarized by AI using a schemaa like this:

* Summary
* Action items by person
* Blockers

later each person will receive the summary and his action items and blockers so that everyone will have cleaar the activities for that day.

## Tribe Organization

A Tribe is a set of people with a single mission. Usually, in the Spotify model a Tribe is organized in Squad, Chapters, Guild and they can be spread across different organization. In order to manage a large group of people in a Tribe there could be several manager that works at different level in the organization. There are different elements in the organization of a Tribe, in this document I waant to focus only on two of them:

* Vacations
* Daily Shift

I think that people caan use a simple chatbot and give simple interaction to create their vacation plan. Moreover, this vacation can be syncronized with the daily shift calendar to find possible conflicts. I think that LLM is the perfect tool to manage these elements and send them to aan AIOps server that can synchup them on the official calendar aand daily shift tools of the organization. 

Generally people are creatures of habit and tend to always take their holidays at the same times. For this reason, an AI could create an initial calendar based on past habits which the user can then change by simply interacting with a chatbot. When all people insert their vacations manager can immediately see in a backend system the vacation of all his reports and find immeddiaately conflicts.

The vacation overview can be used to create a daily shift to cover a 24/7 support on different geography simply comparing the orgaanization, the people, the geograaphy, and vacations. Every month aa daily shift plan can be compiled and store in aa backend system like, for example, pager duty. 



