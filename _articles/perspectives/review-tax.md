---
title: "Agentic AI යුගයේ Code Review සහ Review Tax – හැම PR එකක්ම එකම විදිහට Review කරන්න ඕනද?"
description: "AI Coding Agents භාවිතයෙන් අද අපිට ඉතා වේගයෙන් Code Generate කරන්න සහ Pull Requests (PRs) නිර්මාණය කරන්න පුළුවන්. නමුත් Review කරන වේගයත් ඒ තරමටම වැඩි වෙනවද?"
lead: false
date: 2026-10-30 13:00:00 +0530
lang: si
category: Perspectives
cover: /images/learn/review-tax.jpg
cover_alt: "Cover: Code Review and Review Tax in the Agentic AI era"
tags: [AgenticAI, CodeReview, ReviewTax, SoftwareEngineering]
---

AI Coding Agents භාවිතයෙන් අද අපිට ඉතා වේගයෙන් Code Generate කරන්න සහ Pull Requests (PRs) නිර්මාණය කරන්න පුළුවන්.

නමුත් Code ලියන වේගය වැඩි වුණාට, ඒ Code එක Review කරලා Production එකට යොමු කරන වේගයත් ඒ තරමටම වැඩි වෙනවද?

මෙතැනදී තමයි **Review Tax** කියන සංකල්පය වැදගත් වෙන්නේ.

AI-generated PRs වැඩි වෙනකොට ඒවා Review කරන්න, Validate කරන්න සහ නැවත නිවැරදි කරන්න වැඩි කාලයක් වැය වෙන්න පුළුවන්. අවසානයේ Code Generation වේගවත් වුණත් සමස්ත Development Process එක මන්දගාමී වෙන්න පුළුවන්.

## hama PR එකකටම එකම අවධානය දෙන්න ඕනද?

නැහැ! මෙතැනදී වැදගත් සංකල්ප කිහිපයක් තියෙනවා.

### 1. One-Way Door vs Two-Way Door

- **Two-Way Door** – පහසුවෙන් Revert කරන්න පුළුවන් වෙනස්කම්. උදා: සීමිත UI වෙනස්කමක්.
- **One-Way Door** – ආපසු හැරවීම අපහසු හෝ වියදම් අධික වෙනස්කම්. උදා: Production Data Delete කිරීමක්.

### 2. Blast Radius

PR එකකින් System එකේ කොපමණ කොටසකට බලපෑමක් ඇති වෙන්න පුළුවන්ද? කුඩා UI Component එකක් වෙනස් කිරීම සහ Authentication System එක වෙනස් කිරීම අතර අවදානම එකම මට්ටමේ නැහැ.

### 3. Evidence-Based Review

AI Agent එක "Tests Pass" කියලා පැවසීම විතරක් ප්රමාණවත් නැහැ. Test Results, Screenshots සහ Before/After Behavior වගේ සැබෑ Evidence ලබාදීමත් වැදගත්.

## Ehenam Review Process එක වෙනස් කරන්නේ කොහොමද?

**Low Risk + Small Blast Radius + Easily Reversible** PRs සඳහා AI Code Review, Automated Tests සහ CI Checks භාවිත කරලා, සුදුසු ආරක්ෂක සීමාවන් යටතේ Human Review අඩු කරන්න හෝ Auto-Merge කරන්න පුළුවන්.

නමුත් **High Risk, Large Blast Radius** හෝ **Difficult-to-Reverse** වෙනස්කම් සඳහා වැඩි අවධානයක් සහ Human Approval අවශ්යයි.

මේ Risk Assessment එකත් AI මඟින් සිදු කරන්න පුළුවන්. නමුත් ඒ තීරණ Validate කරන Controls තිබීම වැදගත්.

## Software Engineers විදිහට අපි අවධානය දෙන්න ඕන මොකක්ද?

AI යුගයේ අපේ අරමුණ වැඩි PR ප්රමාණයක් Generate කිරීම විතරක් නෙවෙයි. Software Quality පවත්වාගෙන යමින්, අවදානම අනුව Review Effort එක වෙන් කරලා, Changes ආරක්ෂිතව Production එකට යොමු කිරීමයි.

> හැම PR එකකටම සමාන Review Time එකක් වැය කරනවා වෙනුවට, වැඩිම අවදානමක් තියෙන PR වලට වැඩිම Engineering Attention එක ලබාදීමයි වැදගත්.

ඔබේ Team එකේ AI-generated PRs Review කරන්න වෙනම Process එකක් තියෙනවද? ඔබේ අදහස් Comment එකකින් බෙදාගන්න.

මීළඟ Post එකෙන් **AI Software Factory** කියන සංකල්පය කතා කරමු!
