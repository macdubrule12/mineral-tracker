# Critical Minerals News Tracker

Daily intelligence dashboard for ClearPath policy team tracking critical minerals news and policy developments.

## Features

- 🔍 **Smart Relevance Scoring** - Automatically categorizes stories by ClearPath relevance (High/Medium/Low)
- 📊 **Weekly Meeting Mode** - Interactive meeting companion with task tracking
- 📝 **Action Items** - Contextual recommendations for team response
- 🗺️ **Geographic Tracking** - Filter by region (US, China, EU, etc.)
- 🏷️ **Policy Triggers** - Automatic detection of IRA, LPO, FEOC, and other policy mechanisms
- 📥 **Export Capabilities** - Download digests and meeting notes

## Running Locally

```bash
pip install -r requirements.txt
streamlit run minerals_dashboard.py
```

## Data Sources

- Government sources (DOE, USGS, White House)
- Wire services (Reuters, Bloomberg)
- Trade press (Mining.com, Northern Miner)
- Policy analysis feeds

## Built With

- Streamlit
- Python feedparser
- RSS news aggregation

---

Built for ClearPath by Mac | 2026
