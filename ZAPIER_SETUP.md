# Zapier Email Automation Setup (5 Minutes)

## Overview
Send High Priority minerals news to mining@clearpath.org every **Monday and Friday at 8am ET** using your existing dashboard.

---

## Setup Steps

### 1. Create New Zap
- Go to [zapier.com](https://zapier.com)
- Click **"Create Zap"**

### 2. Set Up Trigger (Schedule)
**Trigger: Schedule by Zapier**
- Event: **"Every Week"**
- Day: **Monday**
- Time: **8:00 AM**
- Timezone: **Eastern Time**
- Test trigger ✓

### 3. Add Action - Fetch Data
**Action: Webhooks by Zapier**
- Event: **"GET"**
- URL: `https://clearpath-minerals.streamlit.app/?format=json`
- Leave other fields blank
- Test action ✓

You'll see JSON data with High Priority stories!

### 4. Add Action - Send Email
**Action: Gmail**
- Event: **"Send Email"**
- To: `mining@clearpath.org`
- From: Your Gmail (macdubrule@gmail.com)
- Subject: `Critical Minerals Digest - High Priority Updates`

**Body (use this template):**
```
Hi team,

Here are this week's High Priority critical minerals updates:

{{1. Data__title}}
Source: {{1. Data__source}}
Why it matters: {{1. Data__why_it_matters}}
ClearPath Angle: {{1. Data__clearpath_angle}}
Link: {{1. Data__link}}

---

{{2. Data__title}}
Source: {{2. Data__source}}
Why it matters: {{2. Data__why_it_matters}}
ClearPath Angle: {{2. Data__clearpath_angle}}
Link: {{2. Data__link}}

---

{{3. Data__title}}
Source: {{3. Data__source}}
Why it matters: {{3. Data__why_it_matters}}
ClearPath Angle: {{3. Data__clearpath_angle}}
Link: {{3. Data__link}}

---

View full dashboard: https://clearpath-minerals.streamlit.app/

Best,
ClearPath Minerals Tracker
```

- Test action ✓
- **Turn Zap ON**

### 5. Duplicate for Friday
- In your Zaps list, click the **"..."** menu
- Click **"Duplicate"**
- Edit the trigger to change day to **Friday**
- Keep everything else the same
- **Turn Zap ON**

---

## Done! 🎉

You now have:
- ✅ Automated emails Monday + Friday at 8am ET
- ✅ High Priority stories from your dashboard
- ✅ Sent to mining@clearpath.org
- ✅ Easy to test with "Test Zap" button

---

## Advanced: Better Email Formatting

If you want prettier emails, use **"Gmail > Send Email (with Rich Text)"** and format with HTML:

```html
<h2>Critical Minerals Digest - High Priority Updates</h2>
<p>Hi team,</p>
<p>Here are this week's High Priority critical minerals updates:</p>

<div style="border-left: 4px solid #FFC107; padding-left: 12px; margin: 16px 0;">
  <h3>{{1. Data__title}}</h3>
  <p><strong>Source:</strong> {{1. Data__source}}</p>
  <p><strong>Why it matters:</strong> {{1. Data__why_it_matters}}</p>
  <p><strong>ClearPath Angle:</strong> {{1. Data__clearpath_angle}}</p>
  <p><a href="{{1. Data__link}}">Read more →</a></p>
</div>

<!-- Repeat for items 2 and 3 -->

<p><a href="https://clearpath-minerals.streamlit.app/">View full dashboard →</a></p>
```

---

## Troubleshooting

**No data appearing?**
- Make sure you tested the Webhook step and saw JSON data
- Check that the dashboard is live at clearpath-minerals.streamlit.app

**Email not formatting right?**
- Use the simple text version first
- Then upgrade to HTML once it's working

**Want to change the schedule?**
- Edit the Zap → Change trigger time/day
- Can do daily, weekly, or custom schedule
