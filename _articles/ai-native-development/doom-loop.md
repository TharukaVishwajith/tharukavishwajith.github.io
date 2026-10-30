---
title: "AI Coding Agents සහ Doom Loop – වැරදි Context එකේ සැබෑ පිරිවැය"
description: "AI Coding Agent එකකට Task එකක් දුන්නාම සමහර වෙලාවට බලාපොරොත්තු වෙන ප්රතිඵලය ලැබෙන්නේ නැහැ. මේ විදිහට එකම ගැටලුව වටා නැවත නැවත යන තත්ත්වය Doom Loop ලෙස හඳුන්වනවා."
lead: false
date: 2026-10-30 12:00:00 +0530
lang: si
translation_key: ai-native-development-doom-loop
series: ai-native-development
part: 4
cover: /images/learn/doom-loop.jpg
cover_alt: "Cover: AI Coding Agents and the Doom Loop"
image:
  path: /images/og/doom-loop.jpg
  width: 1200
  height: 630
  alt: "Cover: AI Coding Agents and the Doom Loop"
locale: si_LK
tags: [ContextEngineering, AIAgents, DoomLoop, SoftwareEngineering]
---

AI Coding Agent එකකට Task එකක් දුන්නාම සමහර වෙලාවට බලාපොරොත්තු වෙන ප්රතිඵලය ලැබෙන්නේ නැහැ. නැවත Prompt කරනවා, Code වෙනස් කරනවා, ඒත් ප්රශ්නය විසඳෙන්නේ නැහැ.

මේ විදිහට එකම ගැටලුව වටා නැවත නැවත යන තත්ත්වය **Doom Loop** ලෙස හඳුන්වනවා.

මෙයට බලපාන ප්රධාන හේතුවක් තමයි **Poor Context**.

හිතන්න අපේ Project එකේ Architecture එක වෙනස් වෙලා. නමුත් AI Agent එක තවමත් පරණ Documentation භාවිත කරනවා කියලා. එතකොට Agent එක හොඳ Code එකක් ලිව්වත්, ඒක සැබෑ Requirements වලට ගැළපෙන්නේ නැති වෙන්න පුළුවන්.

> වැරදි Context → වැරදි Implementation → Re-prompting → Rework → වැඩි Token Usage සහ Development Cost.

## වැඩි Context ලබාදීම විසඳුමක්ද?

**අනිවාර්යයෙන්ම නැහැ!**

අපේ Project එකේ තියෙන හැම Documentation එකක්ම, Data Source එකක්ම සහ MCP Server එකක්ම Agent එකට සම්බන්ධ කළා කියලා ප්රතිඵල වඩා හොඳ වෙනවා කියලා සහතික කරන්න බැහැ.

තොරතුරු ප්රමාණය වැඩි වෙනකොට Agent එකට නිවැරදි තොරතුරු හඳුනාගැනීම අපහසු වෙන්න පුළුවන්. විශේෂයෙන් පරණ, අදාළ නොවන හෝ එකිනෙකට පටහැනි තොරතුරු තියෙන විට.

**Information Access තිබීම සහ නිවැරදි Information එක හඳුනාගැනීම කියන්නේ වෙනස් දේවල් දෙකක්.**

## එහෙනම් විසඳුම මොකක්ද?

මෙතැනදී තමයි **Context Engineering** සහ **Context Engine** සංකල්ප වැදගත් වෙන්නේ.

අපි අවධානය දෙන්න ඕන:

- **Relevant Context** – Task එකට අවශ්ය තොරතුරු පමණක් ලබාදීම.
- **Up-to-date Context** – පරණ Documentation වෙනුවට නිවැරදි සහ යාවත්කාලීන Sources භාවිත කිරීම.
- **Smart Retrieval** – GitHub PRs, Tickets, Logs සහ Documentation අතර සම්බන්ධතා හඳුනාගෙන අවශ්ය දේ ලබාගැනීම.
- **Conflict Resolution** – එකිනෙකට පටහැනි Requirements සහ Decisions හඳුනාගෙන නිවැරදි තොරතුරු තහවුරු කිරීම.
- **Validation & Feedback** – Agent එකේ ප්රතිඵල සැබෑ Requirements වලට ගැළපෙනවද පරීක්ෂා කිරීම.

AGENTS.md, Rules Files හෝ MCP Servers එකතු කිරීම ප්රයෝජනවත් වුණත්, ඒවා හරහා ලැබෙන තොරතුරු නිවැරදිද, අදාළද සහ විශ්වාසදායකද කියන එකත් වැදගත්.

## Software Engineers විදිහට අපි අවධානය දෙන්න ඕන මොකක්ද?

AI Agent එකට හැකි තරම් Context ලබාදීම වෙනුවට, **නිවැරදි Context එක අවශ්ය වෙලාවට, අවශ්ය ප්රමාණයෙන් ලබාදෙන ක්රමවේදයක් Engineer කිරීමයි** වැදගත්.

ඒ හරහා Doom Loops සහ අනවශ්ය Rework අඩු කරලා, Token Usage සහ Development Cost Optimize කරමින් Software Quality සහ Development Efficiency වැඩිදියුණු කරන්න පුළුවන්.

---

**AI Model එකේ හැකියාවන් වැදගත්. නමුත් ඒ හැකියාවන් නිවැරදිව භාවිත වෙන්න නම්, Model එකට ලැබෙන Context එකේ Quality එකත් ඒ තරමටම වැදගත්.**

ඔබත් AI Coding Agents භාවිත කරද්දී මේ වගේ Doom Loops වලට මුහුණ දීලා තියෙනවද? ඔබේ අත්දැකීම් Comment එකකින් බෙදාගන්න.

මීළඟ Post එකෙන් Agentic AI යුගයේ Code Reviews සහ “Review Tax” ගැන කතා කරමු!
