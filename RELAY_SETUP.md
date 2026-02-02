# Relay Email Automation Setup (5 Minutes)

## Overview
Send High Priority minerals news to mining@clearpath.org every **Monday and Friday at 8am ET** using Relay's visual workflow builder.

Relay is perfect for this because:
- ✅ Visual, drag-and-drop interface
- ✅ Generous free tier (10,000 workflow runs/month)
- ✅ Easy to test and iterate
- ✅ Clean email formatting

---

## Setup Steps

### 1. Create New Workflow
- Go to [relay.app](https://relay.app) and sign in
- Click **"Create Workflow"** or **"New Workflow"**
- Name it: **"Monday Minerals Digest"**

### 2. Add Trigger: Schedule
**Trigger Type: Schedule**
- Click **"Add Trigger"** → **"Schedule"**
- Frequency: **Weekly**
- Day: **Monday**
- Time: **8:00 AM**
- Timezone: **America/New_York** (Eastern Time)
- Save trigger ✓

### 3. Add Step: Fetch JSON Data
**Action: HTTP Request**
- Click **"Add Step"** → Search for **"HTTP Request"** or **"Webhook"**
- Method: **GET**
- URL: `https://raw.githubusercontent.com/macdubrule/mineral-tracker/main/priorities.json`
- Headers: Leave empty
- Save step ✓

**Test it:** Click "Test step" and you'll see the JSON response with High Priority items!

### 4. Add Step: Send Email
**Action: Gmail (or Email)**
- Click **"Add Step"** → Search for **"Gmail"** or **"Send Email"**
- Connect your Gmail account (macdubrule@gmail.com)
- Configure email:

**To:** `mining@clearpath.org`

**Subject:** `Critical Minerals Digest - Monday High Priority Updates`

**Body:** Click into the body field, then map fields from the HTTP Request step:

```
Hi team,

Here are this week's High Priority critical minerals updates:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📰 [Insert: items[0].title]

Source: [Insert: items[0].source] | Date: [Insert: items[0].date]

Why it matters: [Insert: items[0].why_it_matters]

ClearPath Angle: [Insert: items[0].clearpath_angle]

Read more: [Insert: items[0].link]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📰 [Insert: items[1].title]

Source: [Insert: items[1].source] | Date: [Insert: items[1].date]

Why it matters: [Insert: items[1].why_it_matters]

ClearPath Angle: [Insert: items[1].clearpath_angle]

Read more: [Insert: items[1].link]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📰 [Insert: items[2].title]

Source: [Insert: items[2].source] | Date: [Insert: items[2].date]

Why it matters: [Insert: items[2].why_it_matters]

ClearPath Angle: [Insert: items[2].clearpath_angle]

Read more: [Insert: items[2].link]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

View full dashboard: https://clearpath-minerals.streamlit.app/

Best,
ClearPath Minerals Tracker
```

**How to insert fields:**
1. Click into the email body
2. You'll see a `+` or **"Insert data"** button
3. Select the HTTP Request step
4. Navigate to `items` → `[0]` → `title` (for first item)
5. Repeat for each field you want to include

### 5. Test the Workflow
- Click **"Test Workflow"** at the top
- Check your email to see the digest!
- Adjust formatting as needed

### 6. Turn On the Workflow
- Click **"Turn On"** in the top right
- Your Monday emails are now automated! 🎉

### 7. Duplicate for Friday
- Go to your workflows list
- Find "Monday Minerals Digest"
- Click **"..."** → **"Duplicate"**
- Rename to: **"Friday Minerals Digest"**
- Edit the trigger to change day to **Friday**
- Update subject line to say "Friday" instead of "Monday"
- **Turn On** ✓

---

## Done! 🎉

You now have:
- ✅ Automated emails Monday + Friday at 8am ET
- ✅ High Priority stories from your dashboard
- ✅ Sent to mining@clearpath.org
- ✅ Easy to test and modify anytime

---

## Advanced: HTML Email Formatting

If Relay supports HTML emails, you can make them prettier:

```html
<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
  <h2 style="color: #193D69; border-bottom: 3px solid #193D69; padding-bottom: 10px;">
    Critical Minerals Digest - High Priority Updates
  </h2>

  <p>Hi team,</p>
  <p>Here are this week's High Priority critical minerals updates:</p>

  <!-- Story 1 -->
  <div style="border-left: 4px solid #FFC107; padding-left: 12px; margin: 20px 0; background: #FAFAFA; padding: 15px;">
    <h3 style="color: #193D69; margin-top: 0;">[Insert: items[0].title]</h3>
    <p style="color: #666; font-size: 13px;">
      <strong>Source:</strong> [Insert: items[0].source] |
      <strong>Date:</strong> [Insert: items[0].date]
    </p>
    <p><strong style="color: #1976D2;">Why it matters:</strong> [Insert: items[0].why_it_matters]</p>
    <p><strong style="color: #1976D2;">ClearPath Angle:</strong> [Insert: items[0].clearpath_angle]</p>
    <p><a href="[Insert: items[0].link]" style="color: #9D1C20; text-decoration: none;">Read more →</a></p>
  </div>

  <!-- Repeat for items[1] and items[2] -->

  <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid #E0E0E0;">
    <p><a href="https://clearpath-minerals.streamlit.app/" style="color: #9D1C20; font-weight: bold;">View full dashboard →</a></p>
    <p style="color: #999; font-size: 12px;">Generated by ClearPath Minerals Tracker</p>
  </div>
</div>
```

---

## Tips for Using Relay

**Testing:**
- Use the "Test Workflow" button liberally - it's free!
- Test emails will actually send, so maybe use your personal email first

**Debugging:**
- Click on each step to see the data it received/sent
- The visual data flow makes it easy to spot issues

**Modifying:**
- Change the schedule anytime by editing the trigger
- Add more stories by duplicating the email sections
- Change recipients without touching any code

**Free Tier:**
- 10,000 runs/month = plenty for 2 emails/week
- No credit card required to start

---

## Troubleshooting

**No data appearing in email?**
- Check that the HTTP Request step successfully fetched JSON
- Make sure you're inserting fields from `items[0]`, `items[1]`, etc.
- The JSON structure has: `items` (array) → each item has `title`, `source`, etc.

**Email not sending?**
- Verify Gmail is connected in Relay
- Check your Gmail sent folder
- Make sure mining@clearpath.org is a valid address

**Workflow not running on schedule?**
- Verify the workflow is "On" (toggle in top right)
- Check timezone is set to America/New_York
- View workflow runs in the history tab

**Want to send immediately?**
- Click "Test Workflow" to send right now
- Great for showing Jackson the first email!
