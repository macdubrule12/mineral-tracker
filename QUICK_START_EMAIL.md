# 🚀 Quick Start: Automated Weekly Emails

## What You Just Got

✅ **Email Script** (`send_weekly_email.py`) - Fetches news and sends beautiful HTML emails
✅ **GitHub Actions Workflow** (`.github/workflows/weekly-email.yml`) - Runs every Friday at 8am ET
✅ **Updated Requirements** - Added SendGrid package

---

## 📋 Setup Checklist (20 minutes)

### ☐ Step 1: Sign Up for SendGrid (5 min)

1. Go to: **https://signup.sendgrid.com/**
2. Sign up with your ClearPath email
3. Verify your email (check inbox)
4. Complete the form:
   - Industry: **Non-profit**
   - Purpose: **Transactional emails**
5. **Create Single Sender:**
   - Settings → Sender Authentication → Single Sender Verification
   - From Name: `ClearPath Minerals Tracker`
   - From Email: `your-email@clearpath.org`
   - Reply To: `your-email@clearpath.org`
   - Verify this email (check inbox again)
6. **Create API Key:**
   - Settings → API Keys → Create API Key
   - Name: `minerals-tracker-weekly`
   - Full Access
   - **COPY THE KEY!** (you won't see it again)

---

### ☐ Step 2: Add Secrets to GitHub (3 min)

1. Go to: **https://github.com/macdubrule12/mineral-tracker/settings/secrets/actions**
2. Click **"New repository secret"** (3 times, one for each):

**Secret 1:**
- Name: `SENDGRID_API_KEY`
- Value: [Paste your SendGrid API key]

**Secret 2:**
- Name: `EMAIL_TO`
- Value: `mining@clearpath.org`

**Secret 3:**
- Name: `EMAIL_FROM`
- Value: `your-verified-email@clearpath.org` (the one you verified in Step 1)

---

### ☐ Step 3: Push New Files to GitHub (2 min)

Open **GitHub Desktop**:

1. You'll see new files:
   - `send_weekly_email.py`
   - `.github/workflows/weekly-email.yml`
   - `requirements.txt` (modified)
2. Commit message: `Add automated weekly email feature`
3. Click **"Commit to main"**
4. Click **"Push origin"**

---

### ☐ Step 4: Test It! (5 min)

#### **Manual Test (Recommended First):**

In Terminal:
```bash
cd ~/Desktop/minerals

# Install SendGrid locally
pip install sendgrid --break-system-packages

# Set environment variables (temporary - just for testing)
export SENDGRID_API_KEY="paste-your-key-here"
export EMAIL_TO="your-test-email@gmail.com"  # Use YOUR email for testing
export EMAIL_FROM="your-verified-sender@clearpath.org"

# Run the script
python send_weekly_email.py
```

**Check your test email!** You should receive a beautiful digest.

#### **GitHub Actions Test:**

1. Go to: **https://github.com/macdubrule12/mineral-tracker/actions**
2. Click **"Weekly Minerals Email"** workflow
3. Click **"Run workflow"** → **"Run workflow"**
4. Wait ~1-2 minutes
5. Check the logs to see if it succeeded
6. Check `mining@clearpath.org` inbox!

---

### ☐ Step 5: Verify Schedule (1 min)

The email will automatically send every **Friday at 8:00 AM ET**.

To change the schedule, edit `.github/workflows/weekly-email.yml`:
```yaml
schedule:
  - cron: '0 13 * * 5'  # Friday 8am ET
```

**Common schedules:**
- Daily at 8am ET: `0 13 * * *`
- Monday/Wednesday/Friday: `0 13 * * 1,3,5`
- Every morning at 7am ET: `0 12 * * *`

---

## ✅ Success Criteria

You'll know it's working when:
- ✅ Manual test sends email to your inbox
- ✅ GitHub Actions test completes successfully
- ✅ `mining@clearpath.org` receives the test email
- ✅ Email looks good on desktop and mobile
- ✅ All links work

---

## 📧 What the Email Looks Like

**Subject:** `Critical Minerals Weekly Digest – Jan 24 to Jan 31, 2026`

**Content:**
- 📊 Week at a Glance (summary stats)
- 🔴 High Priority Stories (3-5 items with full context)
- 🟠 Notable Stories (5 items, brief format)
- 📊 Link to full dashboard
- Footer with contact info

---

## 🐛 Troubleshooting

**"Email not sending"**
- Check GitHub Actions logs (repo → Actions tab)
- Verify API key is correct in GitHub Secrets
- Verify sender email is verified in SendGrid

**"Email has no stories"**
- Script only sends if there are High Priority items
- Check your dashboard - are there High Priority stories?

**"Email goes to spam"**
- Have recipients add sender to contacts
- Ask IT to whitelist SendGrid IPs

**"Wrong sender name/email"**
- Update `EMAIL_FROM` in GitHub Secrets
- Make sure it's verified in SendGrid

---

## 🎨 Customization Ideas

Want to customize the email? Edit `send_weekly_email.py`:

**Change email frequency:**
- Line 53: Change `timedelta(days=7)` to `timedelta(days=1)` for daily

**Change number of stories:**
- Line 66: Change `high_stories[:5]` to show more/fewer

**Change recipients:**
- Update `EMAIL_TO` secret to: `mining@clearpath.org,policy@clearpath.org`

**Change styling:**
- Line 79+: Edit the HTML/CSS template

---

## 💰 Cost

**SendGrid Free Tier:**
- 100 emails/day
- Perfect for weekly digest
- $0/month forever

---

## 🎯 Next Steps

After setup works:
1. ✅ Tell Jackson it's live
2. ✅ Monitor first automated send (this Friday)
3. ✅ Get feedback from team
4. ✅ Iterate on format/content as needed

---

## 📞 Need Help?

**GitHub Actions failing?**
- Check logs: repo → Actions → click latest run
- Look for red error messages

**SendGrid issues?**
- Check activity: SendGrid dashboard → Activity
- See delivery status

**Code questions?**
- Ask me! Happy to help troubleshoot

---

**You're ready! Start with Step 1 above.** 🚀
