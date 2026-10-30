---
title: "AI Harness Engineering – Prompt එකෙන් ඔබ්බට යන Software Engineering"
description: "හොඳ AI Model එකක් තිබුණා කියලා විතරක් විශ්වාසදායක Software එකක් හෝ Agentic Application එකක් නිර්මාණය කරන්න පුළුවන්ද? මෙතැනදී තමයි AI Harness Engineering වැදගත් වෙන්නේ."
lead: false
date: 2026-10-30 11:00:00 +0530
lang: si
series: ai-native-development
part: 3
cover: /images/learn/ai-harness.jpg
cover_alt: "Cover: AI Harness Engineering, with an agent loop of Plan, Act, Observe, Evaluate, Repeat and Tools"
tags: [AIHarness, HarnessEngineering, AgenticAI, SoftwareEngineering]
---

අද AI ගැන කතා කරනකොට අපි වැඩිපුර අවධානය දෙන්නේ GPT, Claude, Gemini වගේ Models වල හැකියාවන් ගැන. නමුත් හොඳ AI Model එකක් තිබුණා කියලා විතරක් විශ්වාසදායක Software එකක් හෝ Agentic Application එකක් නිර්මාණය කරන්න පුළුවන්ද?

මෙතැනදී තමයි **AI Harness Engineering** වැදගත් වෙන්නේ.

## මොකක්ද AI Harness එකක්?

LLM එකක් තනිව භාවිත කරන විට සාමාන්යයෙන් අපේ Input එකට Response එකක් ලබාදෙනවා. නමුත් Agentic Task එකකදී ඒ Response එකෙන් පමණක් නවතින්නේ නැහැ.

හිතන්න අපි AI එකට කියනවා, *"මේ Project එකට Feature එකක් එකතු කරලා, ඒක නිවැරදිව වැඩ කරනවද පරීක්ෂා කරන්න"* කියලා.

මෙතැනදී AI එකට Files කියවන්න, Code වෙනස් කරන්න, Tests Run කරන්න, Errors හඳුනාගෙන නැවත නිවැරදි කරන්න සිදුවෙනවා.

ඒ සඳහා **Read → Plan → Act → Observe → Evaluate → Repeat** වගේ Execution Loop එකක් භාවිත කරන්න පුළුවන්. හැබැයි හැම Agentic Workflow එකක්ම මේ ආකාරයට ක්රියාත්මක වෙන්න අවශ්ය නැහැ.

මෙතැනදී AI Agent එක සහ Harness එක අතර වෙනසත් තේරුම් ගන්න ඕන.

| | |
|---|---|
| **AI Agent** | Goal එකක් ඉටු කරන්න ඊළඟට කළ යුතු දේ තීරණය කරමින් අවශ්ය Tools භාවිත කරන පද්ධතිය. |
| **AI Harness** | Agent එකට අවශ්ය Execution Environment, Tools, Context සහ Controls සපයමින් එහි Execution Loop එක හෝ Workflow එක කළමනාකරණය කරන Software Infrastructure එක. |
{: .defs}

> සරලව කිව්වොත් Agent එක ඊළඟට කළ යුතු දේ තීරණය කරන අතර Harness එක ඒ තීරණ ක්රියාත්මක කිරීමට සහ ක්රියාවලිය පාලනය කිරීමට අවශ්ය පහසුකම් සපයනවා. ප්රායෝගිකව මේ වගකීම් සමහර Frameworks වල එකිනෙකට සම්බන්ධ වෙන්නත් පුළුවන්.

Task එක සම්පූර්ණ වෙනතුරු, නියමිත සීමාවකට ළඟාවෙනතුරු හෝ Human Intervention අවශ්ය වෙනතුරු ක්රියාවලිය පාලනය කිරීමත් Harness එකේ කාර්යයක්.

ඒ වගේම Context, Memory, Tools, Security, Permissions සහ Evaluation වගේ හැකියාවනුත් Harness එකට ඇතුළත් වෙන්න පුළුවන්.

Claude Code, OpenAI Codex වගේ Coding Agents වල Harness මේ සඳහා උදාහරණ.

## අපිට Harness එකක් Customize කරන්න පුළුවන්ද?

ඔව්! Codex, Claude Code වගේ දැනට තියෙන Harness එකක් අපේ Project එකට ගැළපෙන විදිහට Customize කරන්න පුළුවන්.

උදාහරණයක් විදිහට:

- **Rules** – Architecture, Coding Standards සහ Business Rules.
- **Skills** – Project එකට අවශ්ය Reusable Workflows.
- **MCP / Tools** – Databases, APIs, Logs සහ External Systems සම්බන්ධ කිරීම.
- **Hooks** – Automated Tests සහ Security Checks.
- **Context & Memory** – Project Documentation සහ Technical Decisions.
- **Evaluation & Feedback** – ප්රතිඵල පරීක්ෂා කර නැවත වැඩිදියුණු කිරීම.

මේ බොහෝ දේවල් කරන්න Harness එකේ Source Code වෙනස් කරන්න අවශ්ය නැහැ.

## එතකොට අපේම Harness එකක් හදන්නේ ඇයි?

හිතන්න අපි Banking Application එකක් සඳහා විශේෂ AI Agent එකක් නිර්මාණය කරනවා කියලා.

එතැනදී දැඩි Security Policies, Local LLM Usage, Language Validation, Sensitive Data Protection, Audit Logs, Observability, Compliance Checks සහ Human Approval වගේ විශේෂ අවශ්යතා තිබෙන්න පුළුවන්.

මෙවැනි අවස්ථාවක Claude Code, Codex වගේ Existing Harness එකක් Customize කරන්න හෝ Google ADK, LangGraph වගේ Frameworks භාවිතයෙන් අපේම **Domain-Specific Harness** එකක් නිර්මාණය කරන්න පුළුවන්.

සුදුසු ක්රමය තීරණය වෙන්නේ අපේ Use Case එකේ අවශ්යතා අනුවයි.

## Software Engineers විදිහට අපි දැන් කරන්න ඕන මොකක්ද?

AI එකට Prompts ලබාදෙන එකෙන් විතරක් නවතින්නේ නැතුව, අපේ Project එකට ගැළපෙන විදිහට **Harness එක Engineer කිරීම** ගැනත් අවධානය දෙන්න ඕන.

උදාහරණයක් විදිහට Playwright හරහා UI Testing, Application Logs කියවීම, MCP හරහා Project Context ලබාදීම සහ Automated Feedback Loops එකතු කරන්න පුළුවන්.

මේවා නිවැරදිව සැලසුම් කිරීමෙන් අනවශ්ය Iterations අඩු කරලා, Token Usage සහ Development Cost Optimize කිරීමටත්, Software Quality සහ Development Efficiency වැඩිදියුණු කිරීමටත් පුළුවන්.

---

**අවසානයේ අපේ අරමුණ AI එකෙන් Software Develop කරගැනීම විතරක් නෙවෙයි. ඒ Software එකේ Quality එක පවත්වාගෙන යමින් Development Process එක කාර්යක්ෂම කිරීමයි.** ඒ සඳහා AI එක වැඩ කරන පරිසරයත් නිවැරදිව Engineer කළ යුතුයි. Harness Engineering වැදගත් වෙන්නේ ඒ නිසයි.

මේ Post එක ඔබට වැදගත් වුණා නම්, ඔබේ මිතුරන් එක්කත් Share කරන්න. Harness Engineering ගැන ඔබේ අදහස් සහ අත්දැකීම් Comment එකකින් බෙදාගන්න.

තවත් රසවත් තාක්ෂණික මාතෘකාවකින් ඊළඟ Post එකෙන් හමුවෙමු!
