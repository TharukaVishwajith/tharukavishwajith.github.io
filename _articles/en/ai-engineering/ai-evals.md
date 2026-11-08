---
title: "AI Evals | How Do We Know an AI Agent Is Working?"
description: "Evaluate whether an AI agent's outputs and behavior meet your quality and success criteria, from correct decisions and policy compliance to reliability and business value."
lead: false
date: 2026-11-08 11:02:00 +0530
lang: en
translation_key: ai-engineering-ai-evals
permalink: /learn/en/ai-engineering/ai-evals/
series: ai-engineering
part: 1
cover: /images/learn/ai-evals.png
cover_alt: "An AI agent evaluation dashboard and whiteboard checking decisions, policy compliance, data use, task completion and overall quality"
image:
  path: /images/og/ai-evals.jpg
  width: 1200
  height: 630
  alt: "AI Evals – How Do We Know an AI Agent Is Working?"
locale: en_US
tags: [AIEvals, AIEngineering, AgenticAI, SoftwareEngineering]
---

When we build conventional software applications, we use unit tests, integration tests and similar checks to determine whether the system works correctly.

With **AI agentic systems**, things are somewhat different.

An AI agent can give different answers to the same question on different occasions. It may also complete a task while making the wrong decisions or taking the wrong actions along the way.

## Does completing the task mean success?

Imagine a customer support AI agent processing a refund request.

Is the task successful simply because the agent approves the refund?

Did it check company policy? Did it examine the customer's order details correctly? Is the customer eligible for a refund?

If it approves the refund without checking these things, it may have completed the task technically while making the wrong decision for the business.

This is where **AI evals (evaluations)** matter.

Put simply, evals systematically measure whether an AI system's outputs and behavior meet the quality and success criteria we expect.

## How do we use evals?

- First, define what a good result looks like.
- Collect test scenarios that resemble real usage, along with failures that have occurred before.
- Assess results through human review, automated checks or AI-based evaluators.
- Fix the issues identified and evaluate again.

This is an ongoing activity. Whenever we change models, prompts, tools or workflows, we need to measure whether the system has actually improved.

## How observability and evals connect

This also connects to [**AI observability**](/learn/en/ai-native-development/ai-native-observability/), which we discussed earlier.

**Observability** helps us understand what the agent did. **Evals** help us measure whether those actions meet our expectations.

Improving an AI system requires evidence beyond changing a prompt and deciding that the result looks better.

We need to be able to show that our change improved the system's quality, reliability and business value.

> **You can't reliably improve what you don't evaluate.**
