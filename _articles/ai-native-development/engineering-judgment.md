---
title: "AI Agents වලට Code ලියන්න පුළුවන්. ඒත් සැබෑ Problem එක හඳුනාගන්න පුළුවන්ද?"
description: "Instructions Follow කරලා Tests Pass කිරීම සහ සැබෑ Business Problem එක විසඳීම අතර වෙනස. Human Engineering Judgment, Engineering Intuition සහ FDE-Gym Research එකෙන් ලැබෙන අදහස් ගැන."
lead: false
date: 2026-11-08 11:01:00 +0530
lang: si
translation_key: ai-native-development-engineering-judgment
series: ai-native-development
part: 10
cover: /images/learn/engineering-judgment.png
cover_alt: "AI Agent එක Tests Pass කළත් වෙනත් Service එකක ගැටලුවක් පෙන්වන Dashboard එකක් පරීක්ෂා කරන Engineer කෙනෙක්"
image:
  path: /images/og/engineering-judgment.jpg
  width: 1200
  height: 630
  alt: "AI Agents, සැබෑ Problems හඳුනාගැනීම සහ Human Engineering Judgment"
locale: si_LK
tags: [AIEngineering, SoftwareEngineering, EngineeringJudgment, ProblemDiscovery, ForwardDeployedEngineer]
---

අද AI Coding Agents වලට Code ලියන්න, Bugs Fix කරන්න, Tests Run කරන්න වගේම සංකීර්ණ Tasks පවා විසඳන්න පුළුවන්.

නමුත් සැබෑ Software Projects වලදී ගැටලුව හැම වෙලාවෙම Code එකේම තියෙනවද?

හිතන්න Customer කෙනෙක් System එකක Feature එකක් Fix කරන්න කියනවා. ඒ වගේම වෙනත් System එකක් හොඳින් වැඩ කරන නිසා ඒක ගැන බලන්න අවශ්‍ය නැහැ කියලත් කියනවා.

AI Agent එකක් ලබාදුන් Instructions අනුව Fix එක Implement කරලා Tests පවා Pass කරන්න පුළුවන්.

නමුත් සැබෑ **Root Cause** එක තියෙන්නේ Customer බලන්න එපා කිව්ව System එකේම නම්?

## Human Engineering Judgment

මෙතැනදී තමයි **Human Engineering Judgment** වැදගත් වෙන්නේ.

මේ ගැටලුව ගැන මෑතකදී පළවුණු [**FDE-Gym Research**](https://arxiv.org/abs/2610.22350) එකෙන් වැදගත් කරුණක් හෙළි වෙනවා. Industries 18ක සැබෑ Projects පදනම් කරගත් Simulated Customer Environments වල **Tasks 95ක්** භාවිත කරලා AI Model Configurations 13ක් Evaluate කළා. ලබා නොදුන් Constraints තමන් විසින්ම හඳුනාගත යුතු Setting එකේ, හොඳම Configuration එකට පවා නියමිත Success Criteria සපුරාලමින් විසඳන්න හැකි වුණේ **Tasks 14ක් පමණයි (14.7%)**. මෙහි Task එකක් විසඳූ බව සැලකුවේ අවම වශයෙන් 0.8ක Score එකක්, Incident එකකින් තොරව ලබාගත් විටයි. ප්‍රධාන අභියෝගයක් වුණේ ලබා නොදුන් Requirements සහ Constraints තමන් විසින්ම හඳුනාගැනීමයි.

Experienced Engineer කෙනෙක් ලබාදුන් Instructions විතරක් Follow කරන්නේ නැහැ.

එයා Requirements ගැන ප්‍රශ්න කරනවා. වෙනත් Systems සහ Dependencies පරීක්ෂා කරනවා. අවශ්‍ය නම් Stakeholders එක්ක කතා කරනවා. එකම Problem එක Technical, Business සහ Operational Perspectives වලින් බලනවා.

සමහර වෙලාවට Documentation එකක නැති ගැටලුවක් ගැන සැකයක් ඇති වෙන්නේ කලින් ලැබුණු Experience එක නිසා.

ඒකට අපි **Engineering Intuition** කියලා කියන්න පුළුවන්. හැබැයි ඒ සැකය Evidence වලින් Validate කරන්නත් ඕන.

## AI Agents වලට මේ දේවල් කරන්න බැරිද?

බැහැ කියන එක නෙවෙයි. AI Agents වලටත් Hypotheses Generate කරන්න, Dependencies හොයන්න සහ Solutions යෝජනා කරන්න පුළුවන්.

නමුත් Real-World Projects වල Context එක අසම්පූර්ණ වෙන්න, Requirements පරස්පර වෙන්න, වැදගත් Business Rules Documentation වල නොතිබෙන්න පුළුවන්. සමහර තීරණ සඳහා අවශ්‍ය Access හෝ Authority Agent එකකට නැති වෙන්නත් පුළුවන්.

ඒ නිසා **Task** එක සාර්ථකව Complete කිරීම සහ සැබෑ **Business Problem** එක විසඳීම කියන්නේ එකම දෙයක් නෙවෙයි.

## සැබෑ අවශ්‍යතාව හඳුනාගැනීම

කලින් Post එකක අපි කතා කළ [**Product Engineers සහ Forward Deployed Engineers**](/learn/ai-native-development/product-and-forward-deployed-engineers/) වගේ Roles වල වැදගත්කමත් මෙතැනදී මතු වෙනවා.

Customer කියන දේ විතරක් නොවෙයි, Customer ට ඇත්තටම අවශ්‍ය දේ තේරුම් ගැනීමත් Engineering වල කොටසක්.

ඒ නිසා අලුත් පරම්පරාවේ Engineers ලාට Coding සහ AI Tools වලට අමතරව **Critical Thinking**, **Systems Thinking** සහ **Problem Discovery** වගේ Skills ප්‍රායෝගිකව පුහුණු කිරීම වැදගත්.

අනාගතයේ වටිනාකම තියෙන්නේ AI එකට Instructions දීමේ හැකියාවට පමණක් නෙවෙයි. අවශ්‍ය වෙලාවට ඒ Instructions පවා ප්‍රශ්න කරලා, සැබෑ ගැටලුව හඳුනාගෙන වගකීමෙන් තීරණ ගන්න පුළුවන් හැකියාවටයි.
