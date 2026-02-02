# Critical Minerals Dashboard - Implementation Checklist
**Based on 1/30/25 Weekly Meeting Feedback**

---

## 🎯 **Priority 1: Hot Words / Keyword Filtering** (High Impact)

### Feedback:
"Let everyone know - make it filter to hot words"
"Industry hot word in mind for the future policy release"

### Implementation:
- [ ] Add **"Hot Words"** filter to sidebar
  - [ ] Pre-set keywords: "billion", "tariff", "permit approved", "partnership", "investment"
  - [ ] Custom keyword search box (user can add their own)
  - [ ] Highlight matching stories in yellow/orange
- [ ] Create **"Policy Watch"** section
  - [ ] Track specific phrases: "Executive Order", "Final Rule", "Bill introduced"
  - [ ] Alert when high-impact policy terms appear
- [ ] Add **"Email Alert"** option (future)
  - [ ] Let users subscribe to specific keywords
  - [ ] Get email when matched story appears

**Estimated Time:** 2-3 hours
**Value:** Makes scanning faster, catches critical policy moments

---

## 🎯 **Priority 2: Email Integration** (Team Requested)

### Feedback:
"Permitting - main crime emails"
"DOE Email chain of partnerships - send team"
"Same or broken thing - send to Doug"

### Implementation:
- [ ] Add **"Share Story"** button on each item
  - [ ] Pre-fills email with headline + link + context
  - [ ] Option to send to: Mary, Alex, Doug, team list
- [ ] Add **"Email This Digest"** button
  - [ ] Sends weekly digest directly to specified recipients
  - [ ] Include only High Priority items + notes
- [ ] Create **"Permitting Email Alert"** filter
  - [ ] Auto-flag all permitting-related stories
  - [ ] One-click share to permitting team

**Estimated Time:** 3-4 hours
**Value:** Reduces email forwarding work, keeps team in loop

---

## 🎯 **Priority 3: Mary & Alex Supply Chain Focus** (Leadership Request)

### Feedback:
"Potential 1-1 - time to Mary - Alex Advancing supply chain news"
"Let everyone know - make it filter to hot words"

### Implementation:
- [ ] Create **"Supply Chain Priority View"**
  - [ ] Filter showing only: Domestic Supply, China Dependence, Trade & Tariffs
  - [ ] Bookmark-able URL for Mary/Alex to check
- [ ] Add **"Executive Summary"** mode
  - [ ] Top 3 stories with 2-sentence summaries
  - [ ] Perfect for quick leadership check-ins
- [ ] Add **"China Watch"** section
  - [ ] Dedicated view for China-related stories
  - [ ] Track: "China dominance", "decoupling", "processing capacity"

**Estimated Time:** 2 hours
**Value:** Gives leadership quick, focused view

---

## 🎯 **Priority 4: DOE Partnership Tracking** (Team Coordination)

### Feedback:
"DOE Email chain of partnerships - send team"
"DOE critical minerals office - team work week"

### Implementation:
- [ ] Add **"DOE Programs"** dedicated tab
  - [ ] Shows all DOE-related stories in one place
  - [ ] Track: LPO loans, grants, partnerships, programs
- [ ] Create **"Partnership Tracker"**
  - [ ] List of companies mentioned + their DOE connections
  - [ ] Track over time (e.g., "Company X announced 3 DOE deals this month")
- [ ] Add **"Team Distribution"** feature
  - [ ] One-click to send DOE updates to minerals working group

**Estimated Time:** 3 hours
**Value:** Better coordination on DOE engagement

---

## 🎯 **Priority 5: Daily vs Weekly Cadence** (Meeting Discussion)

### Feedback:
"Policy news digest weekly - daily"
"Weekly only"
"Industry hot word in mind for the future policy release"

### Implementation:
- [ ] Add **"Cadence Toggle"** in sidebar
  - [ ] Switch between "Daily View" and "Weekly View"
  - [ ] Daily: Shows last 24 hours only
  - [ ] Weekly: Current behavior (last 7 days)
- [ ] Add **"What's New Today"** banner
  - [ ] Shows # of new High Priority items since yesterday
  - [ ] Quick scan for daily check-ins
- [ ] Create **"Daily Brief"** export option
  - [ ] Lighter format than weekly digest
  - [ ] Just headlines + links for quick scanning

**Estimated Time:** 2 hours
**Value:** Supports both daily monitors and weekly reviewers

---

## 📋 **Quick Wins (Easy Additions)**

### Short-term improvements (<1 hour each):

- [ ] **Add "Send to Mary" button** on High Priority items
  - Pre-fills email to Mary with story details

- [ ] **Add "Permitting" quick filter** to sidebar
  - One-click to see only permitting stories

- [ ] **Add story counter** at top
  - "5 new stories since yesterday"

- [ ] **Add "Copy Link" button** on each story
  - Easy sharing in Slack/email

- [ ] **Add "Archive" feature** for old stories
  - Hide stories older than 14 days (optional view)

---

## 🚀 **Implementation Priority Order**

### **This Week (High Impact, Quick):**
1. ✅ Hot Words filter (2-3 hours)
2. ✅ Supply Chain view for Mary/Alex (2 hours)
3. ✅ Daily view toggle (2 hours)

### **Next Week (Team Requested):**
4. Email integration (3-4 hours)
5. DOE Programs tab (3 hours)

### **Later (Nice to Have):**
6. Partnership tracker (requires more data structure)
7. Email alerts (requires email service setup)

---

## 📊 **Success Metrics**

After implementing these, track:
- [ ] Time saved in weekly meeting (target: 15+ min)
- [ ] # of action items flagged per meeting (target: 3-5)
- [ ] # of stories shared with leadership (Mary/Alex)
- [ ] Team feedback: "Is this more useful?"

---

## 🤔 **Questions to Clarify**

Before implementing, confirm with team:

1. **Email integration:** Should we integrate with Gmail API or just create mailto: links?
2. **Mary/Alex view:** Should this be a separate URL or just a filter?
3. **Daily cadence:** Do people want daily email digests or just daily view in dashboard?
4. **Hot words:** What specific keywords matter most? (permitting, billion, investment, partnership, ?)
5. **DOE focus:** Should we track specific DOE offices/programs beyond general "DOE news"?

---

## 💡 **Future Ideas (Parking Lot)**

Ideas mentioned but not prioritized yet:
- Integration with ClearPath's internal systems
- Automated email to Doug when certain keywords appear
- Company/investor tracking over time
- Congressional member tracking (which members care about minerals)
- State-level policy tracking

---

**Next Steps:**
1. Review this checklist with Jackson/team
2. Prioritize top 3 features to implement
3. Set timeline for implementation
4. Test with team before deploying

**Questions?** Contact Mac for clarification or to discuss implementation approach.
