---
title: "AI Evals | AI Agent එකක් වැඩ කරනවා කියලා අපි කොහොමද දන්නේ?"
description: "AI Agent එකක Outputs සහ Behavior අපේ Quality සහ Success Criteria සපුරාලනවද කියලා මැන බලමු. Task Completion වලින් ඔබ්බට ගොස් නිවැරදි තීරණ, Business Rules සහ සැබෑ Value පරීක්ෂා කිරීම ගැන."
lead: false
date: 2026-11-08 11:02:00 +0530
lang: si
translation_key: ai-engineering-ai-evals
series: ai-engineering
part: 1
cover: /images/learn/ai-evals.png
cover_alt: "AI Agent එකක තීරණ, Policy අනුගමනය කිරීම, භාවිත කළ Data සහ සමස්ත Quality පරීක්ෂා කරන Evals Dashboard එකක්"
image:
  path: /images/og/ai-evals.jpg
  width: 1200
  height: 630
  alt: "AI Evals – AI Agent එකක් වැඩ කරනවා කියලා අපි කොහොමද දන්නේ?"
locale: si_LK
tags: [AIEvals, AIEngineering, AgenticAI, SoftwareEngineering]
---

අපි සාමාන්‍ය Software Applications නිර්මාණය කරනකොට Unit Tests, Integration Tests වගේ දේවල් භාවිත කරලා System එක නිවැරදිව වැඩ කරනවද කියලා පරීක්ෂා කරනවා.

නමුත් **AI Agentic Systems** වලදී මේක තරමක් වෙනස්.

එකම ප්‍රශ්නයට AI Agent එකක් වෙනස් අවස්ථාවල වෙනස් පිළිතුරු දෙන්න පුළුවන්. ඒ වගේම Task එක Complete කළත්, ඒකට ගත්ත තීරණ හෝ ක්‍රියාමාර්ග වැරදි වෙන්න පුළුවන්.

## Task එක Complete වුණාම සාර්ථකද?

හිතන්න Customer Support AI Agent එකක් Refund Request එකක් Process කරනවා.

Agent එක Refund එක Approve කළා කියලා Task එක සාර්ථකද?

Company Policy එක පරීක්ෂා කළාද? Customer ගේ Order Details නිවැරදිව බැලුවද? Refund එකට Customer සුදුසුද?

මේ දේවල් පරීක්ෂා නොකර Refund එක Approve කළා නම්, Technical වශයෙන් Task එක Complete වුණත් Business එකට ඒක වැරදි තීරණයක්.

මෙතැනදී තමයි **AI Evals (Evaluations)** වැදගත් වෙන්නේ.

සරලවම කිව්වොත්, Evals මඟින් අපි AI System එකක Outputs සහ Behavior අපි බලාපොරොත්තු වෙන Quality සහ Success Criteria සපුරාලනවද කියලා ක්‍රමානුකූලව මැන බලනවා.

## Evals භාවිත කරන්නේ කොහොමද?

- පළමුව හොඳ Result එකක් කියන්නේ මොකක්ද කියලා නිර්වචනය කරනවා.
- සැබෑ භාවිතයට සමාන Test Scenarios සහ කලින් සිදුවුණු Failures එකතු කරනවා.
- Human Review, Automated Checks හෝ AI-based Evaluators මඟින් Results පරීක්ෂා කරනවා.
- හඳුනාගත් ගැටලු නිවැරදි කරලා නැවත Evaluate කරනවා.

මේක එක වතාවක් කරන Testing Activity එකක් නෙවෙයි. අලුත් Models, Prompts, Tools හෝ Workflows වෙනස් කරන හැම අවස්ථාවකම System එක ඇත්තටම Improve වුණාද කියලා මැන බලන්න ඕන.

## Observability සහ Evals අතර සම්බන්ධය

කලින් අපි කතා කළ [**AI Observability**](/learn/ai-native-development/ai-native-observability/) එක්කත් මේක සම්බන්ධයි.

**Observability** මඟින් Agent එක මොනවද කළේ කියලා තේරුම් ගන්න පුළුවන්. **Evals** මඟින් ඒ දේවල් අපේ බලාපොරොත්තු සපුරාලනවද කියලා මැන බලන්න පුළුවන්.

AI System එකක් Improve කරනවා කියන්නේ Prompt එක වෙනස් කරලා Result එක හොඳයි වගේ පෙනෙන එක නෙවෙයි.

අපි කරපු වෙනස ඇත්තටම System එකේ Quality, Reliability සහ Business Value වැඩි කළාද කියලා Evidence එක්ක පෙන්වන්න පුළුවන් වීමයි.

> **You can't reliably improve what you don't evaluate.**
