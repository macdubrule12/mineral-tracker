#!/usr/bin/env python3
"""
Generate priorities.json file for Zapier integration
Creates a static JSON file with High Priority items from last 7 days
"""

import json
from datetime import datetime, timedelta
from news_fetcher import fetch_news

def generate_priorities_json():
    """Fetch news and filter for High Priority items"""
    print("Fetching news...")
    all_stories = fetch_news()

    # Filter for High Priority items from last 7 days
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    high_priority = []
    for item in all_stories:
        if item.get("relevance_level") == "High" and item.get("date", "") >= week_ago:
            high_priority.append({
                "title": item.get("title", ""),
                "source": item.get("source", ""),
                "link": item.get("link", ""),
                "date": item.get("date", ""),
                "summary": item.get("summary", "")[:200] + "...",  # Truncate for email
                "why_it_matters": item.get("why_it_matters", ""),
                "clearpath_angle": item.get("clearpath_angle", ""),
                "regions": ", ".join(item.get("regions", [])),
                "minerals": ", ".join(item.get("minerals", []))
            })

    # Limit to top 5 for email
    high_priority = high_priority[:5]

    # Add metadata
    output = {
        "generated_at": datetime.now().isoformat(),
        "count": len(high_priority),
        "items": high_priority
    }

    # Write to file
    with open("priorities.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"✓ Generated priorities.json with {len(high_priority)} High Priority items")
    return output

if __name__ == "__main__":
    generate_priorities_json()
