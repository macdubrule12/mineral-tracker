# 🚀 Gmail SMTP Email Automation - Quick Setup (5 minutes)

## What This Does

Sends automated weekly emails to `mining@clearpath.org` every Friday at 8am ET with High Priority stories from your Critical Minerals Tracker.

**No new accounts needed!** Uses your existing Gmail account.

---

## 📋 Setup Steps

### ☐ Step 1: Enable Gmail App Password (2 min)

**Important:** Gmail requires an "App Password" for automated scripts (not your regular password).

1. **Go to:** https://myaccount.google.com/security
2. **Turn on 2-Step Verification** (if not already on):
   - Click "2-Step Verification"
   - Follow the prompts to set it up
   - This is required for App Passwords
3. **Create App Password:**
   - Go back to https://myaccount.google.com/security
   - Scroll to "2-Step Verification" section
   - Click "App passwords" at the bottom
   - Select app: "Mail"
   - Select device: "Other (Custom name)"
   - Type: "Minerals Tracker"
   - Click "Generate"
   - **COPY THE 16-CHARACTER PASSWORD** (looks like: `xxxx xxxx xxxx xxxx`)
   - You won't see it again!

---

### ☐ Step 2: Add GitHub Secrets (2 min)

1. **Go to:** https://github.com/macdubrule12/mineral-tracker/settings/secrets/actions
2. **Click "New repository secret"** (do this 3 times):

**Secret 1:**
- Name: `EMAIL_FROM`
- Value: `your-email@clearpath.org` (or your Gmail if that's easier)

**Secret 2:**
- Name: `EMAIL_PASSWORD`
- Value: [Paste the 16-character App Password from Step 1]

**Secret 3:**
- Name: `EMAIL_TO`
- Value: `mining@clearpath.org`

---

### ☐ Step 3: Push Files to GitHub (1 min)

Open **GitHub Desktop**:

1. You'll see these updated files:
   - `send_weekly_email.py` (updated for Gmail)
   - `.github/workflows/weekly-email.yml` (updated)
   - `requirements.txt` (no longer needs sendgrid)
2. Commit message: `Switch to Gmail SMTP for email automation`
3. Click **"Commit to main"**
4. Click **"Push origin"**

---

### ☐ Step 4: Test It! (3 min)

#### **Option A: Manual Local Test (Recommended)**

In Terminal:
```bash
cd ~/Desktop/minerals

# Set environment variables for testing
export EMAIL_FROM="your-email@clearpath.org"
export EMAIL_PASSWORD="your-16-char-app-password"
export EMAIL_TO="your-test-email@gmail.com"  # Use YOUR email for testing

# Run the script
python send_weekly_email.py
```

**Check your test email!** Should arrive within 30 seconds.

#### **Option B: GitHub Actions Test**

1. Go to: https://github.com/macdubrule12/mineral-tracker/actions
2. Click **"Weekly Minerals Email"** workflow
3. Click **"Run workflow"** → **"Run workflow"**
4. Wait ~1-2 minutes
5. Check logs to see if it succeeded
6. Check `mining@clearpath.org` inbox

---

## ✅ Success Checklist

You're all set when:
- ✅ Manual test sends email to your inbox
- ✅ Email looks professional (HTML formatting, colors, links work)
- ✅ GitHub Actions test completes without errors
- ✅ `mining@clearpath.org` receives the test email
- ✅ Links in email work (dashboard, article sources)

---

## 📧 What the Email Contains

**Subject:** `Critical Minerals Weekly Digest – Jan 24 to Jan 31, 2026`

**Content:**
- 📊 **Week at a Glance**: Summary stats and top themes
- 🔴 **High Priority Stories** (3-5 items):
  - Full headline and metadata
  - "Why It Matters" analysis
  - "ClearPath Strategic Angle" with action recommendations
  - Links to source articles
- 🟠 **Notable Stories** (5 items): Brief summaries
- 📊 **Dashboard Link**: Interactive view
- 👋 **Footer**: Contact info

**Designed for mobile and desktop!**

---

## 🐛 Troubleshooting

**"Authentication failed" error:**
- Make sure you're using the App Password, NOT your regular Gmail password
- Verify 2-Step Verification is enabled on your Google account
- Check that the App Password is correctly copied into GitHub Secrets (no spaces)

**"No email sent":**
- Script only sends if there are High Priority stories from the last 7 days
- Check your dashboard - are there recent High Priority items?

**"Email goes to spam":**
- Have recipients add sender email to their contacts
- This is common for first automated email, should improve after a few sends

**GitHub Actions failing:**
- Go to repo → Actions → click latest run
- Look for red error messages
- Most common: incorrect secrets format (extra spaces, wrong name)

**Can't find App Passwords option:**
- Make sure 2-Step Verification is enabled first
- You need to be signed into the correct Google account
- Some workspace accounts restrict App Passwords (check with IT)

---

## 🔐 Security Notes

✅ **App Password is encrypted** in GitHub Secrets (not visible in code)
✅ **Only GitHub Actions can access it** (not in public repo)
✅ **Can be revoked anytime** in Google account settings
✅ **Separate from your main password** (doesn't give full account access)

---

## 🎨 Customization

### Change email schedule:
Edit `.github/workflows/weekly-email.yml`:
```yaml
schedule:
  - cron: '0 13 * * 5'  # Friday 8am ET
```

**Common schedules:**
- Daily 8am ET: `0 13 * * *`
- Mon/Wed/Fri: `0 13 * * 1,3,5`
- Every weekday: `0 13 * * 1-5`

### Change recipients:
Update `EMAIL_TO` in GitHub Secrets to:
```
mining@clearpath.org,policy@clearpath.org,ga@clearpath.org
```

### Change time range:
Edit `send_weekly_email.py` line 23:
```python
week_ago = (datetime.now() - timedelta(days=7))  # Change 7 to 1 for daily
```

---

## 💰 Cost

**Gmail SMTP:** $0/month (free forever)
**GitHub Actions:** $0/month (within free tier)
**Total:** $0/month 🎉

---

## 📅 Schedule

**Automatic sends:** Every Friday at 8:00 AM ET
**First automated email:** This Friday morning
**Manual triggers:** Anytime via GitHub Actions

---

## 🎯 Next Steps

After setup completes:

1. ✅ Tell Jackson automated emails are live
2. ✅ Monitor Friday's first automated send
3. ✅ Get team feedback on format/content
4. ✅ Adjust frequency/recipients if needed

---

## 📞 Need Help?

**Email not working?**
- Check GitHub Actions logs (repo → Actions tab)
- Verify all 3 secrets are set correctly
- Make sure App Password is from correct Gmail account

**Want to change something?**
- Schedule: Edit `.github/workflows/weekly-email.yml`
- Content: Edit `send_weekly_email.py`
- Recipients: Update GitHub Secret

---

**That's it! Start with Step 1 above.** 🚀
