# Automated Weekly Email Setup Guide

## 🎯 Goal
Send automated weekly digest emails to `mining@clearpath.org` every Friday morning with the week's top critical minerals news.

---

## 🏗️ Architecture

**Components:**
1. **Email Script** (`send_weekly_email.py`) - Fetches news and formats email
2. **GitHub Actions** - Runs script every Friday at 8am ET
3. **SendGrid** - Email delivery service (free tier: 100 emails/day)

**Flow:**
```
Friday 8am → GitHub Actions triggers → Script fetches news →
Filters High Priority → Formats HTML email → SendGrid sends →
mining@clearpath.org receives email
```

---

## 📝 Setup Steps

### Step 1: Sign Up for SendGrid (5 min)

1. Go to: https://signup.sendgrid.com/
2. Sign up with your ClearPath email
3. Verify your email address
4. Complete the "Tell us about yourself" form:
   - Industry: Non-profit
   - Purpose: Transactional emails
5. Create a **Single Sender** verification:
   - From Name: `ClearPath Minerals Tracker`
   - From Email: `your-email@clearpath.org`
   - Reply To: `your-email@clearpath.org`
6. Verify this sender email (check inbox)
7. Create an **API Key**:
   - Settings → API Keys → Create API Key
   - Name it: `minerals-tracker-weekly`
   - Full Access
   - **COPY THE KEY** (you won't see it again!)

---

### Step 2: Add SendGrid API Key to GitHub Secrets (2 min)

1. Go to your GitHub repo: https://github.com/macdubrule12/mineral-tracker
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Name: `SENDGRID_API_KEY`
6. Value: Paste your SendGrid API key
7. Click **Add secret**

Also add:
- Name: `EMAIL_TO`
- Value: `mining@clearpath.org`

- Name: `EMAIL_FROM`
- Value: `your-email@clearpath.org` (the verified sender)

---

### Step 3: Add Email Script to Your Repo (Done below!)

I'll create `send_weekly_email.py` for you - it will:
- Use the same news fetching logic as your dashboard
- Filter for High Priority items from the last 7 days
- Format as beautiful HTML email
- Send via SendGrid

---

### Step 4: Create GitHub Actions Workflow (Done below!)

I'll create `.github/workflows/weekly-email.yml` - it will:
- Run every Friday at 8:00 AM ET
- Install dependencies
- Run the email script
- Handle errors gracefully

---

### Step 5: Test It! (5 min)

**Manual Test:**
```bash
cd ~/Desktop/minerals

# Set your API key temporarily for testing
export SENDGRID_API_KEY="your-key-here"
export EMAIL_TO="your-test-email@gmail.com"
export EMAIL_FROM="your-verified-sender@clearpath.org"

# Run the script
python send_weekly_email.py
```

Check your email! You should receive a beautiful digest.

**GitHub Actions Test:**
1. Push the new files to GitHub
2. Go to: https://github.com/macdubrule12/mineral-tracker/actions
3. Click "Weekly Minerals Email"
4. Click "Run workflow" → "Run workflow"
5. Wait ~1 minute
6. Check `mining@clearpath.org` for the email!

---

## 📧 Email Format

The automated email will include:

**Subject:** `Critical Minerals Weekly Digest – [Date Range]`

**Content:**
- Executive summary (top 3 themes, story count)
- High Priority stories (3-5 items) with:
  - Headline
  - Source & date
  - "Why it matters" context
  - "ClearPath angle" recommendations
  - Link to full article
- Notable stories (collapsed section)
- Link to live dashboard
- Unsubscribe option (if needed)

---

## ⏰ Schedule

**Default:** Every Friday at 8:00 AM ET

**To change the schedule:** Edit `.github/workflows/weekly-email.yml`:
```yaml
schedule:
  - cron: '0 13 * * 5'  # Friday 8am ET (13:00 UTC)
```

Cron format: `minute hour day month weekday`
- Daily at 8am: `0 13 * * *`
- Monday/Wednesday/Friday at 9am: `0 14 * * 1,3,5`

---

## 🐛 Troubleshooting

**Email not sending?**
1. Check GitHub Actions logs: repo → Actions tab → click latest run
2. Verify SendGrid API key is correct in GitHub Secrets
3. Verify sender email is verified in SendGrid
4. Check SendGrid activity feed: SendGrid dashboard → Activity

**Wrong content in email?**
1. Script filters for High Priority items from last 7 days
2. If no High Priority items, it won't send (by design)
3. To test with any stories, temporarily change filter in script

**Emails going to spam?**
1. Add SPF/DKIM records (SendGrid provides these)
2. Ask IT to whitelist SendGrid IPs
3. Have recipients add to contacts

---

## 💰 Cost

**SendGrid Free Tier:**
- 100 emails/day (plenty for weekly digest!)
- Free forever
- No credit card required

**If you need more:**
- Essentials plan: $19.95/month for 50,000 emails

---

## 🔒 Security

- API key stored in GitHub Secrets (encrypted)
- Never committed to code
- Only accessible to GitHub Actions
- Can be rotated anytime in SendGrid dashboard

---

## 📊 Monitoring

**Check email delivery:**
1. SendGrid Dashboard → Activity
2. See opens, clicks, bounces
3. Download reports

**GitHub Actions runs:**
1. Repo → Actions tab
2. See all weekly runs
3. Check for failures

---

## 🎨 Customization

**Want to customize the email?**
Edit `send_weekly_email.py`:
- Change HTML template (line ~150)
- Modify filter criteria (line ~80)
- Add/remove sections
- Change styling

**Want to change recipients?**
Update `EMAIL_TO` in GitHub Secrets:
- Single: `mining@clearpath.org`
- Multiple: `mining@clearpath.org,policy@clearpath.org`

---

## ✅ Success Checklist

After setup, verify:
- [ ] SendGrid account created and verified
- [ ] API key added to GitHub Secrets
- [ ] Email script added to repo
- [ ] GitHub Actions workflow added
- [ ] Manual test successful
- [ ] GitHub Actions test successful
- [ ] Email looks good on mobile
- [ ] Recipients confirmed they want emails
- [ ] Schedule set correctly (Friday 8am ET)

---

**Next:** I'll create the actual scripts for you below!
