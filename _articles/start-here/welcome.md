---
title: "Welcome to Wizard Lab: how these series work"
description: What you'll find here, how the series are organised, and how to get the most out of them.
date: 2026-10-30
tags: [start-here]
---

For years I've explained software, AI and data on [Wizard LK](https://www.youtube.com/wizardlk) and in university lecture halls. This is the written home for that work: longer, searchable, and easy to come back to.

## What you'll learn

Everything here is organised into **series**: paths you can follow from part one, or dip into when you need a specific idea.

- **AI Engineering with LLMs**: from your first model call to production RAG, hybrid search, re-ranking, evaluation and agents.
- **Data Engineering, Practically**: ETL and ELT, connectors, warehouses, dbt and orchestration, the plumbing that feeds analytics and AI.
- **Software Engineering Foundations**: APIs, databases, architecture, testing and cloud deployment.

## How the articles are written

Each article tries to do three things:

1. Explain the idea in plain language first.
2. Show working code you can run.
3. Point out what changes when you take it to production.

Code looks like this, and every block has a copy button:

```python
from openai import OpenAI  # or any LLM client

def answer(question: str, context: list[str]) -> str:
    """The smallest possible RAG step: ground the model in retrieved text."""
    prompt = "Answer using only this context:\n\n" + "\n---\n".join(context)
    prompt += f"\n\nQuestion: {question}"
    ...
```

> **Tip:** If a part assumes something you haven't met yet, it links back to the article that covers it.

## Staying up to date

New parts are announced on the [RSS feed](/learn/feed.xml) and on [Wizard LK](https://www.youtube.com/wizardlk). If something is unclear or you'd like a topic covered, [send me an email](mailto:tharukavishwajiths@gmail.com).

Pick a series and start with part one.
