# Deploy Your Dashboard to Streamlit Cloud

## 🚀 **Complete Deployment Guide** (15 minutes total)

---

## **Step 1: Initialize Git & Push to GitHub** (5 min)

### A. Initialize Git Repository

Open Terminal in your minerals folder and run:

```bash
cd ~/Desktop/minerals
git init
git add .
git commit -m "Initial commit - Critical Minerals Tracker"
```

### B. Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `minerals-tracker` (or whatever you prefer)
3. Description: "Critical Minerals News Tracker for ClearPath"
4. **Make it PRIVATE** (important for internal tool)
5. **Don't** initialize with README (you already have one)
6. Click **"Create repository"**

### C. Push Your Code

GitHub will show you commands - copy and paste them. They'll look like:

```bash
git remote add origin https://github.com/YOUR-USERNAME/minerals-tracker.git
git branch -M main
git push -u origin main
```

✅ **Checkpoint:** Your code is now on GitHub!

---

## **Step 2: Deploy to Streamlit Community Cloud** (5 min)

### A. Sign Up for Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click **"Sign up"** (or "Continue with GitHub")
3. Authorize Streamlit to access your GitHub account

### B. Deploy Your App

1. Click **"New app"** button
2. Fill in the form:
   - **Repository:** Select `YOUR-USERNAME/minerals-tracker`
   - **Branch:** `main`
   - **Main file path:** `minerals_dashboard.py`
   - **App URL:** Choose a custom URL like `clearpath-minerals` (or let it auto-generate)

3. Click **"Deploy!"**

### C. Wait for Deployment (2-3 min)

You'll see a build log. Wait for:
```
✓ Your app is live!
```

✅ **Checkpoint:** Your dashboard is now online!

---

## **Step 3: Set Up Access Control** (Optional - 5 min)

By default, your app is public. To restrict access:

### A. Make Repository Private

1. Go to your GitHub repo settings
2. Scroll to "Danger Zone"
3. Click "Change visibility" → "Make private"
4. Confirm

### B. Share with Team

Since the repo is private, only people with GitHub access to your repo can see the deployment logs, but the **app URL is still public**.

**To truly restrict access:**
1. In Streamlit Cloud, go to app settings
2. Enable **"Viewer authentication"**
3. Add team members' email addresses
4. They'll need to sign in with GitHub/Google/Email to access

---

## **Step 4: Share with Your Team** (2 min)

Your app URL will be something like:
```
https://clearpath-minerals.streamlit.app
```

Send this to your team with a message like:

> **Critical Minerals Tracker is now live!**
>
> Access the dashboard here: [YOUR URL]
>
> Features:
> - Weekly digest for meeting prep
> - Interactive meeting mode with task tracking
> - High-priority action items
>
> Toggle "Weekly Meeting Mode" in the sidebar for tomorrow's meeting!

---

## **Step 5: Future Updates** (Automatic!)

Whenever you make changes:

```bash
cd ~/Desktop/minerals
git add .
git commit -m "Description of changes"
git push
```

**Streamlit Cloud automatically redeploys when you push to GitHub!** 🎉

---

## **Troubleshooting**

### "ModuleNotFoundError" during deployment
- Check that `requirements.txt` has all dependencies
- Streamlit Cloud should auto-detect and install them

### App loads but shows errors
- Check the logs in Streamlit Cloud dashboard
- RSS feeds might be temporarily down (this is normal)

### App is slow
- First load is always slower
- Subsequent loads use caching (much faster)
- Consider reducing cache TTL if data needs to be fresher

### Need to update code
```bash
# Make your changes, then:
git add .
git commit -m "Your change description"
git push
# Streamlit Cloud will auto-redeploy!
```

---

## **Advanced: Custom Domain** (Optional)

Want `minerals.clearpath.org` instead of `xxx.streamlit.app`?

1. In Streamlit Cloud app settings, go to "Custom domain"
2. Follow instructions to add CNAME record in your DNS
3. ClearPath IT team can help with this

---

## **Cost**

- **Streamlit Community Cloud:** FREE ✅
- **GitHub Private Repo:** FREE ✅
- **Total Cost:** $0/month 🎉

---

## **Support**

- Streamlit Docs: https://docs.streamlit.io/
- Community Forum: https://discuss.streamlit.io/
- Status Page: https://streamlitstatus.com/

---

**You're ready to deploy! Start with Step 1 above.** 🚀
