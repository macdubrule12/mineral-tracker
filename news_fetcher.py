import feedparser
from datetime import datetime
import ssl
import urllib.request

# Import sources from centralized config
from sources import (
    MINERAL_FEEDS, KEYWORDS, SOURCE_TIERS,
    THEME_KEYWORDS, REGION_KEYWORDS, PRIORITY_KEYWORDS,
    RELEVANCE_CATEGORIES, POLICY_TRIGGERS, CLEARPATH_ANGLES
)

# Disable SSL verification for RSS feeds (common macOS Python issue)
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# Set User-Agent to avoid being blocked by sites
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
feedparser.USER_AGENT = USER_AGENT

def classify_mineral(text):
    """Determine which mineral category an article belongs to"""
    text_lower = text.lower()

    if "lithium" in text_lower:
        return "Lithium"
    elif "cobalt" in text_lower:
        return "Cobalt"
    elif "nickel" in text_lower:
        return "Nickel"
    elif "copper" in text_lower:
        return "Copper"
    elif "rare earth" in text_lower or "rare-earth" in text_lower:
        return "Rare Earth"
    elif "graphite" in text_lower:
        return "Graphite"
    elif any(word in text_lower for word in ["battery", "ev", "electric vehicle"]):
        return "Battery Metals"
    else:
        return "Mining"


def detect_themes(text):
    """Detect article themes based on keywords"""
    text_lower = text.lower()
    themes = []
    for theme, keywords in THEME_KEYWORDS.items():
        if any(kw.lower() in text_lower for kw in keywords):
            themes.append(theme)
    return themes[:3] if themes else ["General"]  # Max 3 themes


def detect_regions(text):
    """Detect geographic regions mentioned in article"""
    text_lower = text.lower()
    regions = []
    for region, keywords in REGION_KEYWORDS.items():
        if any(kw.lower() in text_lower for kw in keywords):
            regions.append(region)
    return regions[:2] if regions else ["Global"]  # Max 2 regions


def is_priority(text):
    """Check if article is policy-actionable (may require ClearPath response)"""
    text_lower = text.lower()
    # Only flag as priority if it contains actionable policy keywords
    return any(kw.lower() in text_lower for kw in PRIORITY_KEYWORDS)


def generate_clearpath_angle(text, primary_category, policy_triggers, regions):
    """Generate context-specific ClearPath strategic angle"""
    text_lower = text.lower()

    # Build strategic angle components
    strategic_value = ""
    consider_items = []

    # STRATEGIC VALUE - based on primary category but with context
    if primary_category == "US Policy":
        strategic_value = "Federal policy development opportunity"
        if any(w in text_lower for w in ["bill", "legislation"]):
            consider_items.append("Track bill sponsors for potential ClearPath ally engagement")
            consider_items.append("Draft analysis for Congressional staff on technical implications")
        if any(w in text_lower for w in ["passed", "signed"]):
            consider_items.append("Assess implementation timeline and regulatory follow-up needed")
            consider_items.append("Consider brief to members on policy outcomes")

    elif primary_category == "Permitting":
        strategic_value = "Core ClearPath permitting reform advocacy"
        if any(w in text_lower for w in ["approved", "granted"]):
            consider_items.append(f"Use as positive case study - timeline took [ANALYZE] months")
            consider_items.append("Highlight in materials showing reform benefits")
        elif any(w in text_lower for w in ["denied", "rejected", "delayed"]):
            consider_items.append("Use as evidence for need for permitting modernization")
            consider_items.append("Potential op-ed hook on regulatory barriers to clean energy")
        else:
            consider_items.append("Monitor timeline for permitting reform advocacy data")
            consider_items.append("Track for environmental review process insights")

    elif primary_category == "Domestic Supply":
        strategic_value = "US competitiveness and supply chain resilience"
        if any(w in text_lower for w in ["processing", "refining"]):
            consider_items.append("Highlight midstream gap - critical for IRA effectiveness")
            consider_items.append("Potential partnership if using innovative technology")
        if "US" in regions:
            consider_items.append("Feature as domestic manufacturing success story")
            consider_items.append("Assess if IRA incentives enabled this investment")

    elif primary_category == "Trade & Tariffs":
        strategic_value = "IRA implementation and trade policy implications"
        if "FEOC Rules" in policy_triggers:
            consider_items.append("Brief policy team on FEOC guidance impact on supply chains")
            consider_items.append("Monitor for unintended consequences on clean energy costs")
        if any(w in text_lower for w in ["tariff", "import"]):
            consider_items.append("Analyze how this affects domestic production economics")
            consider_items.append("Consider Treasury/USTR engagement if guidance needed")

    elif primary_category == "DOE Programs":
        strategic_value = "Direct DOE program oversight and advocacy"
        if "DOE/LPO" in policy_triggers:
            consider_items.append("Track project milestones for LPO effectiveness analysis")
            consider_items.append("Feature in Congressional materials on program success")
        if "IRA Tax Credits" in policy_triggers:
            consider_items.append("Document as IRA incentive proof point")
            consider_items.append("Assess if credit structure drove investment decision")

    elif primary_category == "China Dependence":
        strategic_value = "Supply chain security and strategic competition"
        if any(w in text_lower for w in ["rare earth", "processing"]):
            consider_items.append("Emphasize processing bottleneck in national security framing")
            consider_items.append("Potential brief to defense/intel committees")
        if any(w in text_lower for w in ["diversify", "alternative"]):
            consider_items.append("Use to reinforce friend-shoring strategy messaging")
            consider_items.append("Highlight market response to supply chain risk")

    elif primary_category == "EV & Batteries":
        strategic_value = "Transportation decarbonization and IRA implementation"
        if any(w in text_lower for w in ["gigafactory", "manufacturing"]):
            consider_items.append("Track for US battery manufacturing competitiveness analysis")
            consider_items.append("Assess IRA 48C/45X incentive utilization")
        if "30D" in text_lower or "tax credit" in text_lower:
            consider_items.append("Monitor for EV tax credit compliance implications")

    elif primary_category == "Investment":
        strategic_value = "Market signals and policy effectiveness"
        if "billion" in text_lower:
            consider_items.append("Use as proof point - policy creating investment certainty")
            consider_items.append("Track investor/company for partnership opportunities")
        consider_items.append("Assess if ClearPath advocacy enabled favorable policy environment")

    else:  # General
        strategic_value = "General sector intelligence"
        consider_items.append("Monitor for emerging trends affecting advocacy priorities")
        consider_items.append("File for background on critical minerals landscape")

    # Add region-specific considerations
    if "US" in regions and any(region in regions for region in ["Canada", "Australia"]):
        consider_items.append("Highlight allied partnership strengthening friend-shoring")

    # Add trigger-specific considerations if not already covered
    if "Stockpile" in policy_triggers and not any("stockpile" in c.lower() for c in consider_items):
        consider_items.append("Track for defense stockpile strategy implications")

    if "State Policy" in policy_triggers and not any("state" in c.lower() for c in consider_items):
        consider_items.append("Monitor state-level policy innovation for federal replication")

    # Build final angle string - take top 3 most relevant considerations
    if consider_items:
        angle = f"STRATEGIC VALUE: {strategic_value}. CONSIDER: {' | '.join(consider_items[:3])}"
    else:
        # Fallback to template if no specific items generated
        angle = CLEARPATH_ANGLES.get(primary_category, CLEARPATH_ANGLES["General"])

    return angle


def calculate_relevance(text, tier):
    """Calculate ClearPath relevance score (High/Medium/Low) with reasoning"""
    text_lower = text.lower()

    # Start with tier-based score (Gov=3, Wire=2, Trade=1, Policy=2)
    tier_scores = {1: 3, 2: 2, 3: 1, 4: 2}
    base_score = tier_scores.get(tier, 1)

    # Find matching categories and calculate weighted score
    matched_categories = []
    total_weight = base_score

    for category, config in RELEVANCE_CATEGORIES.items():
        if any(kw.lower() in text_lower for kw in config["keywords"]):
            matched_categories.append(category)
            total_weight += config["weight"]

    # Determine relevance level
    if total_weight >= 8:
        level = "High"
    elif total_weight >= 4:
        level = "Medium"
    else:
        level = "Low"

    # Get primary category (first match, or "General")
    primary_category = matched_categories[0] if matched_categories else "General"

    return {
        "level": level,
        "score": total_weight,
        "categories": matched_categories[:3],  # Max 3
        "primary_category": primary_category,
    }


def detect_policy_triggers(text):
    """Detect specific policy mechanisms mentioned in article"""
    text_lower = text.lower()
    triggers = []

    for trigger, keywords in POLICY_TRIGGERS.items():
        if any(kw.lower() in text_lower for kw in keywords):
            triggers.append(trigger)

    return triggers[:3]  # Max 3 triggers


def generate_why_it_matters(text, relevance_info, regions):
    """Generate comprehensive 'Why it matters' analysis based on content"""
    text_lower = text.lower()

    # Collect multiple context points
    context_points = []

    # POLICY SIGNIFICANCE
    if any(w in text_lower for w in ["bill", "legislation", "congress", "senate", "house"]):
        if any(w in text_lower for w in ["introduce", "passed", "signed"]):
            context_points.append("Active legislative development that could reshape regulatory landscape")
        else:
            context_points.append("Congressional attention signals potential for policy action")

    if any(w in text_lower for w in ["executive order", "administration announces", "white house"]):
        context_points.append("High-level executive action with potential for immediate implementation")

    # FINANCIAL SCALE
    if "billion" in text_lower or "bln" in text_lower:
        if any(w in text_lower for w in ["investment", "deal", "project"]):
            context_points.append("Billion-dollar scale investment demonstrates serious market commitment and capital availability")
    elif "million" in text_lower:
        if any(w in text_lower for w in ["grant", "funding", "award"]):
            context_points.append("Federal funding deployment shows program execution and policy implementation in action")

    # CHINA DYNAMICS
    if any(w in text_lower for w in ["china", "chinese"]):
        if any(w in text_lower for w in ["reduce", "alternative", "diversify", "domestic", "onshore"]):
            context_points.append("Supply chain diversification effort addresses critical dependency on Chinese processing capacity")
        elif any(w in text_lower for w in ["dominance", "control", "monopoly"]):
            context_points.append("Highlights China's structural advantages and concentration risk in critical minerals value chain")
        else:
            context_points.append("Chinese market activity affects global pricing and supply chain dynamics")

    # PERMITTING & REGULATORY
    if any(w in text_lower for w in ["permit approved", "permit granted", "approval"]):
        context_points.append("Permitting approval provides real-world data point on timeline and process for critical minerals projects")
    elif any(w in text_lower for w in ["permit denied", "permit rejected"]):
        context_points.append("Permitting setback illustrates ongoing challenges in domestic project development")
    elif "nepa" in text_lower or "environmental review" in text_lower:
        context_points.append("Environmental review process timeline directly relevant to permitting reform advocacy")

    # IRA IMPLEMENTATION
    if any(w in text_lower for w in ["45x", "48c", "30d", "ira", "inflation reduction act"]):
        context_points.append("Direct IRA implementation example showing how incentives are (or aren't) driving investment decisions")

    if any(w in text_lower for w in ["tax credit", "production credit"]):
        context_points.append("Manufacturing tax credit utilization demonstrates policy effectiveness in mobilizing private capital")

    # SUPPLY CHAIN & COMPETITIVENESS
    if any(w in text_lower for w in ["processing", "refining", "midstream"]):
        context_points.append("Processing capacity development addresses critical gap in US supply chain (currently ~90% China-controlled)")

    if any(w in text_lower for w in ["domestic", "made in america", "us production"]) and "US" in regions:
        context_points.append("Domestic production advancement supports supply chain resilience and reduces import dependence")

    # EV & BATTERY SECTOR
    if any(w in text_lower for w in ["ev", "electric vehicle", "battery"]):
        if any(w in text_lower for w in ["gigafactory", "manufacturing", "production"]):
            context_points.append("Battery manufacturing investment critical for US automotive competitiveness in EV transition")
        else:
            context_points.append("EV supply chain development affects transportation decarbonization pathway")

    # INTERNATIONAL PARTNERSHIPS
    if any(region in regions for region in ["Canada", "Australia", "EU"]) and "US" in regions:
        context_points.append("Allied partnership strengthens friend-shoring strategy and diversifies away from adversarial suppliers")

    # DOE PROGRAMS
    if any(w in text_lower for w in ["lpo", "loan program", "doe loan", "loan guarantee"]):
        context_points.append("LPO deployment shows federal financing de-risking early-stage critical minerals projects")

    # TRADE & TARIFFS
    if any(w in text_lower for w in ["tariff", "import", "export ban", "sanctions"]):
        context_points.append("Trade policy action affects economics of domestic production and supply chain reconfiguration")

    # TECHNOLOGY & INNOVATION
    if any(w in text_lower for w in ["recycling", "urban mining", "circular"]):
        context_points.append("Recycling/circular economy approach could reduce primary mining dependence and improve sustainability")

    if any(w in text_lower for w in ["innovation", "breakthrough", "technology"]):
        context_points.append("Technological advancement could alter cost curves or unlock new domestic resources")

    # Combine points or use fallback
    if len(context_points) >= 2:
        # Use top 2 most relevant points
        return " | ".join(context_points[:2])
    elif len(context_points) == 1:
        return context_points[0]
    else:
        # Enhanced fallback based on category
        category = relevance_info.get("primary_category", "General")
        fallback_analysis = {
            "US Policy": "Federal policy development relevant to critical minerals strategy and clean energy deployment",
            "Permitting": "Permitting and regulatory process development affecting project timelines and feasibility",
            "Domestic Supply": "Domestic supply chain development supporting US competitiveness and resilience goals",
            "Trade & Tariffs": "Trade policy affecting critical minerals economics and supply chain configuration",
            "DOE Programs": "DOE program implementation providing insight into federal strategy execution",
            "China Dependence": "China supply chain dynamics affecting US strategic positioning and dependency risk",
            "EV & Batteries": "EV/battery sector development critical to transportation decarbonization and industrial policy",
            "Investment": "Investment activity signaling market response to policy incentives and commercial opportunities",
        }
        return fallback_analysis.get(category, "Developing story with potential implications for critical minerals policy and markets")


def fetch_feed(url):
    """Fetch RSS feed with proper headers to avoid blocks"""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        response = urllib.request.urlopen(request, timeout=15)
        return feedparser.parse(response.read())
    except Exception as e:
        return feedparser.parse("")  # Return empty feed on error

def fetch_news():
    """Fetch news articles from RSS feeds"""
    articles = []

    for feed_url, source_name, preset_mineral, tier in MINERAL_FEEDS:
        try:
            print(f"Fetching from {source_name} ({preset_mineral if preset_mineral else 'General'})...")
            feed = fetch_feed(feed_url)
            
            if hasattr(feed, 'bozo_exception'):
                print(f"  Warning: {feed.bozo_exception}")
            
            entries_found = len(feed.entries)
            print(f"  Found {entries_found} entries")
            
            matched = 0
            for entry in feed.entries[:20]:
                title = entry.get("title", "")
                summary = entry.get("summary", "")
                combined_text = f"{title} {summary}"
                
                # If feed is mineral-specific, take all articles
                # If general feed, check keywords
                if preset_mineral:
                    is_relevant = True
                    mineral = preset_mineral
                else:
                    combined_lower = combined_text.lower()
                    is_relevant = any(keyword in combined_lower for keyword in KEYWORDS)
                    mineral = classify_mineral(combined_text) if is_relevant else None
                
                if is_relevant:
                    matched += 1
                    # Get published date
                    pub_date = entry.get("published", "")
                    try:
                        # Try different date formats
                        for fmt in ["%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z"]:
                            try:
                                date_obj = datetime.strptime(pub_date, fmt)
                                formatted_date = date_obj.strftime("%Y-%m-%d")
                                break
                            except:
                                continue
                        else:
                            formatted_date = pub_date[:10] if len(pub_date) >= 10 else "No date"
                    except:
                        formatted_date = pub_date[:10] if pub_date else "No date"
                    
                    # Calculate relevance and other enrichments
                    regions = detect_regions(combined_text)
                    relevance = calculate_relevance(combined_text, tier)
                    policy_triggers = detect_policy_triggers(combined_text)
                    why_matters = generate_why_it_matters(combined_text, relevance, regions)
                    clearpath_angle = generate_clearpath_angle(
                        combined_text,
                        relevance["primary_category"],
                        policy_triggers,
                        regions
                    )

                    articles.append({
                        "headline": title,
                        "source": source_name,
                        "date": formatted_date,
                        "link": entry.get("link", "#"),
                        "mineral": mineral,
                        "tier": tier,
                        "tier_label": SOURCE_TIERS[tier]["label"],
                        "tier_color": SOURCE_TIERS[tier]["color"],
                        "themes": detect_themes(combined_text),
                        "regions": regions,
                        "is_priority": is_priority(combined_text),
                        # New ClearPath-specific fields
                        "relevance_level": relevance["level"],
                        "relevance_score": relevance["score"],
                        "relevance_categories": relevance["categories"],
                        "clearpath_angle": clearpath_angle,
                        "policy_triggers": policy_triggers,
                        "why_matters": why_matters,
                    })
            
            print(f"  Added {matched} articles")
            
        except Exception as e:
            # Log error but continue with other feeds
            print(f"Error fetching {source_name}: {str(e)}")
            continue
    
    # Remove duplicates based on headline
    seen = set()
    unique_articles = []
    for article in articles:
        if article["headline"] not in seen:
            seen.add(article["headline"])
            unique_articles.append(article)

    # Sort by date (newest first), then by relevance score, then by tier
    relevance_order = {"High": 3, "Medium": 2, "Low": 1}
    unique_articles.sort(key=lambda x: (
        x["date"],
        relevance_order.get(x.get("relevance_level", "Low"), 1),
        -x["tier"]
    ), reverse=True)

    print(f"\n✓ Total: {len(unique_articles)} unique articles")
    return unique_articles

if __name__ == "__main__":
    news = fetch_news()
    print(f"\nFound {len(news)} articles")
    
    # Show breakdown by mineral
    from collections import Counter
    mineral_counts = Counter(item["mineral"] for item in news)
    print("\nBreakdown by mineral:")
    for mineral, count in mineral_counts.most_common():
        print(f"  {mineral}: {count}")
    
    print("\nSample articles:")
    for item in news[:5]:
        print(f"  • [{item['mineral']}] {item['headline']}")