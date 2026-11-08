---
title: "AI Agents Can Write Code. But Can They Identify the Real Problem?"
description: "Passing tests and completing an assigned task do not always solve the customer's business problem. Why engineering judgment, evidence and problem discovery still matter."
lead: false
date: 2026-11-08 11:01:00 +0530
lang: en
translation_key: ai-native-development-engineering-judgment
permalink: /learn/en/ai-native-development/engineering-judgment/
series: ai-native-development
part: 10
cover: /images/learn/engineering-judgment.png
cover_alt: "An engineer investigates a failing downstream service while an AI agent reports that its code fix has passed all tests"
image:
  path: /images/og/engineering-judgment.jpg
  width: 1200
  height: 630
  alt: "AI Agents, Problem Discovery and Human Engineering Judgment"
locale: en_US
tags: [AIEngineering, SoftwareEngineering, EngineeringJudgment, ProblemDiscovery, ForwardDeployedEngineer]
---

Today, AI coding agents can write code, fix bugs, run tests and even solve complex tasks.

But in real software projects, is the problem always in the code itself?

Imagine a customer asks you to fix a feature in one system. They also say another system is working well, so there is no need to look at it.

An AI agent could follow those instructions, implement a fix and even pass the tests.

But what if the real **root cause** lies in the very system the customer said not to examine?

## Human engineering judgment

This is where **human engineering judgment** matters.

The recent [**FDE-Gym research**](https://arxiv.org/abs/2610.22350) highlights an important challenge. It evaluated 13 AI model configurations on **95 tasks** in simulated customer environments adapted from real projects across 18 industries. In the setting where agents had to discover unstated constraints, even the best configuration resolved only **14 tasks (14.7%)** under the benchmark's success criteria: a score of at least 0.8 with no incident. Discovering unstated requirements and constraints was a primary challenge.

An experienced engineer does more than follow the instructions provided.

They question requirements, investigate other systems and dependencies, and speak with stakeholders when necessary. They examine the same problem from technical, business and operational perspectives.

Sometimes, previous experience raises a suspicion about a problem that no document describes.

We can call that **engineering intuition**. But the suspicion still needs to be validated with evidence.

## Can't AI agents do these things too?

This does not mean they cannot. AI agents can also generate hypotheses, explore dependencies and propose solutions.

However, real projects can have incomplete context, contradictory requirements and important business rules that are missing from the documentation. An agent may also lack the access or authority needed for some decisions.

Successfully completing a **task** and solving the real **business problem** are therefore not always the same thing.

## Discovering the real need

This also highlights the importance of roles such as [**product engineers and forward deployed engineers**](/learn/en/ai-native-development/product-and-forward-deployed-engineers/), which we discussed in an earlier article.

Engineering includes understanding what the customer actually needs, alongside what the customer says.

That is why the next generation of engineers needs practical training in **critical thinking**, **systems thinking** and **problem discovery**, in addition to coding and AI tools.

Future value will come from the ability to question instructions when necessary, identify the real problem and make responsible decisions, as well as the ability to give instructions to AI.
