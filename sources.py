# Critical Minerals News Sources
# Balanced, non-partisan sources organized by credibility tier

# Format: (url, source_name, preset_mineral or None, tier)
# If preset_mineral is None, articles are filtered by KEYWORDS

MINERAL_FEEDS = [
    # === TIER 1: GOVERNMENT (via Google News RSS - only reliable method) ===
    ("https://news.google.com/rss/search?q=critical+minerals+site:energy.gov&hl=en-US&gl=US&ceid=US:en", "DOE", None, 1),
    ("https://news.google.com/rss/search?q=critical+minerals+site:usgs.gov&hl=en-US&gl=US&ceid=US:en", "USGS", None, 1),
    ("https://news.google.com/rss/search?q=critical+minerals+site:whitehouse.gov&hl=en-US&gl=US&ceid=US:en", "White House", None, 1),

    # === TIER 2: WIRE SERVICES / BUSINESS NEWS ===
    ("https://news.google.com/rss/search?q=critical+minerals+site:reuters.com&hl=en-US&gl=US&ceid=US:en", "Reuters", None, 2),
    ("https://news.google.com/rss/search?q=critical+minerals+site:bloomberg.com&hl=en-US&gl=US&ceid=US:en", "Bloomberg", None, 2),

    # === TIER 3: MINING TRADE PRESS (actual RSS feeds) ===
    ("https://www.mining.com/feed/", "Mining.com", None, 3),
    ("https://www.northernminer.com/feed/", "Northern Miner", None, 3),
    ("https://www.mining-technology.com/feed/", "Mining Technology", None, 3),
    ("https://im-mining.com/feed/", "International Mining", None, 3),

    # === TIER 4: POLICY & ANALYSIS (via Google News RSS) ===
    ("https://news.google.com/rss/search?q=critical+minerals+policy&hl=en-US&gl=US&ceid=US:en", "Policy News", None, 4),
]

# Tier labels and colors for display
SOURCE_TIERS = {
    1: {"label": "Gov", "color": "#1E88E5"},      # Blue - government
    2: {"label": "Wire", "color": "#43A047"},     # Green - wire services
    3: {"label": "Trade", "color": "#FB8C00"},    # Orange - trade press
    4: {"label": "Policy", "color": "#8E24AA"},   # Purple - policy/analysis
}

# Keywords for filtering general feeds (when preset_mineral is None)
KEYWORDS = [
    "lithium", "cobalt", "nickel", "copper", "rare earth", "graphite",
    "manganese", "mining", "critical mineral", "battery metal",
    "ev battery", "supply chain", "mineral processing", "minerals"
]

# Mineral categories for classification
MINERALS = [
    "lithium",
    "cobalt",
    "nickel",
    "graphite",
    "rare earth",
    "copper",
    "manganese"
]

# === AUTO-TAGGING CONFIGURATION ===

# Theme detection keywords
THEME_KEYWORDS = {
    "Permitting": ["permit", "permitting", "environmental review", "NEPA", "approval", "license"],
    "Processing": ["processing", "refining", "refinery", "smelter", "conversion", "cathode", "anode"],
    "Mining": ["mine", "mining", "extraction", "deposit", "ore", "drill", "exploration"],
    "Recycling": ["recycling", "recycle", "circular", "recovery", "urban mining", "end-of-life"],
    "Trade": ["tariff", "export", "import", "trade", "sanctions", "export controls", "quota"],
    "Prices": ["price", "pricing", "cost", "market", "spot", "futures", "rally", "decline"],
    "ESG": ["ESG", "sustainability", "environmental", "carbon", "emissions", "responsible sourcing"],
    "Security": ["national security", "defense", "DoD", "military", "strategic", "stockpile", "CHIPS"],
}

# Region detection keywords
REGION_KEYWORDS = {
    "US": ["united states", "u.s.", "US ", "america", "biden", "trump", "congress", "DOE", "washington"],
    "Canada": ["canada", "canadian", "ontario", "quebec", "british columbia", "alberta"],
    "EU": ["europe", "european", "EU ", "germany", "france", "brussels"],
    "China": ["china", "chinese", "beijing", "CATL", "BYD"],
    "LATAM": ["chile", "argentina", "brazil", "mexico", "peru", "latin america", "bolivia"],
    "Africa": ["africa", "DRC", "congo", "zambia", "south africa", "zimbabwe", "morocco"],
    "Australia": ["australia", "australian", "pilbara", "western australia"],
    "Asia": ["japan", "korea", "indonesia", "india", "vietnam", "philippines"],
}

# Priority keywords - POLICY-ACTIONABLE items for ClearPath team
# Balance: specific enough to filter noise, broad enough to catch real actions
PRIORITY_KEYWORDS = [
    # Legislation (US-focused)
    "introduce bill", "bill to create", "passes bill", "passed bill",
    "signed into law", "lawmakers introduce",

    # Executive Actions
    "executive order", "president signs", "president directs",
    "administration announces", "white house announces",

    # Major Deals/Funding (with amounts)
    "billion deal", "bln deal", "billion investment", "bln investment",
    "million grant", "receives grant", "awarded grant",

    # Regulatory Decisions
    "permit approved", "permit denied", "permit granted",
    "final rule",

    # Trade Actions
    "imposes tariff", "tariff on", "sanctions on",
    "export ban", "import ban", "export restriction",

    # Strategic/Stockpile
    "stockpile", "strategic reserve", "defense contract",
]

# === CLEARPATH RELEVANCE SCORING ===
# Categories that matter most to ClearPath's mission (clean energy policy)

RELEVANCE_CATEGORIES = {
    "US Policy": {
        "keywords": ["congress", "senate", "house", "legislation", "bill", "act", "DOE", "department of energy",
                     "EPA", "IRA", "inflation reduction act", "CHIPS", "bipartisan", "federal", "white house"],
        "weight": 3
    },
    "Permitting": {
        "keywords": ["permit", "permitting", "NEPA", "environmental review", "approval", "license", "EIS",
                     "regulatory", "BLM", "forest service"],
        "weight": 3
    },
    "Domestic Supply": {
        "keywords": ["domestic production", "US mining", "american", "onshoring", "reshoring", "made in america",
                     "US processing", "domestic supply chain"],
        "weight": 3
    },
    "Trade & Tariffs": {
        "keywords": ["tariff", "import", "export", "trade", "sanctions", "FEOC", "entity of concern",
                     "trade agreement", "IRA compliance"],
        "weight": 2
    },
    "DOE Programs": {
        "keywords": ["loan program", "LPO", "ATVM", "48C", "tax credit", "grant", "DOE funding",
                     "clean energy", "demonstration"],
        "weight": 3
    },
    "China Dependence": {
        "keywords": ["china", "chinese", "CATL", "BYD", "decoupling", "supply chain risk", "rare earth",
                     "processing capacity", "dominance"],
        "weight": 2
    },
    "EV & Batteries": {
        "keywords": ["EV", "electric vehicle", "battery", "cathode", "anode", "gigafactory", "cell manufacturing",
                     "battery supply chain", "IRA battery"],
        "weight": 2
    },
    "Investment": {
        "keywords": ["billion", "million", "investment", "funding", "project", "expansion", "partnership",
                     "joint venture", "offtake"],
        "weight": 1
    },
}

# Policy Trigger tags - specific policy mechanisms ClearPath tracks
POLICY_TRIGGERS = {
    "IRA Tax Credits": ["45X", "48C", "30D", "IRA", "tax credit", "production credit", "manufacturing credit"],
    "DOE/LPO": ["loan program", "LPO", "ATVM", "DOE loan", "conditional commitment", "loan guarantee"],
    "Permitting": ["permit", "NEPA", "EIS", "BLM", "forest service", "environmental review", "ROD"],
    "Tariffs": ["tariff", "section 301", "section 232", "import duty", "trade remedy", "anti-dumping"],
    "FEOC Rules": ["FEOC", "foreign entity of concern", "entity of concern", "IRA guidance", "treasury rule"],
    "Export Controls": ["export control", "export ban", "export restriction", "critical mineral export"],
    "Stockpile": ["strategic reserve", "stockpile", "NDS", "defense stockpile", "DPA", "defense production"],
    "State Policy": ["state incentive", "state law", "governor", "state legislature", "state funding"],
}

# ClearPath angle templates based on category - ENHANCED WITH ACTION GUIDANCE
CLEARPATH_ANGLES = {
    "US Policy": "STRATEGIC VALUE: Direct federal policy development. CONSIDER: Analyze how this aligns with/contradicts ClearPath's legislative priorities. Monitor for opportunities to provide technical input to Congressional staff or submit written testimony. Track if bill sponsors are ClearPath allies/targets for outreach.",

    "Permitting": "STRATEGIC VALUE: Core ClearPath advocacy area. CONSIDER: Use as case study in permitting reform materials. Assess if timeline supports or undermines reform arguments. Consider op-ed opportunity if this demonstrates need for modernized review process. Brief members on implications for energy infrastructure timelines.",

    "Domestic Supply": "STRATEGIC VALUE: Aligns with US competitiveness messaging. CONSIDER: Potential partnership or amplification opportunity if project uses innovative clean tech. Highlight in materials showing market response to IRA incentives. Assess if this creates model for scaling domestic processing/manufacturing.",

    "Trade & Tariffs": "STRATEGIC VALUE: Impacts IRA effectiveness and supply chain resilience. CONSIDER: Brief policy team on how trade barriers affect clean energy deployment costs. Monitor for unintended consequences of protectionist measures. Engage with Treasury/USTR if guidance needed on FEOC rules or trade enforcement.",

    "DOE Programs": "STRATEGIC VALUE: Direct oversight opportunity. CONSIDER: Track project for future case study/success story. Monitor timeline and structure for LPO/grant program advocacy. Assess if this validates specific program models ClearPath has recommended. Consider featuring in materials to Congress on program performance.",

    "China Dependence": "STRATEGIC VALUE: National security + economic competitiveness framing. CONSIDER: Use to reinforce urgency of domestic capacity building. Assess whether this demonstrates market failure requiring policy intervention. Consider brief to defense/intel committees if supply chain vulnerability implications. Potential op-ed hook on strategic competition.",

    "EV & Batteries": "STRATEGIC VALUE: Transportation decarbonization pathway. CONSIDER: Track for IRA implementation analysis. Assess impact on US battery manufacturing competitiveness. Monitor if project leverages IRA incentives (proof of concept for policy effectiveness). Consider implications for 30D EV tax credit compliance.",

    "Investment": "STRATEGIC VALUE: Demonstrates market response to policy signals. CONSIDER: Use as proof point for clean energy investment trends. Assess whether ClearPath policy recommendations enabled this deal. Track investor/company for future partnership opportunities. Monitor if financing model could inform policy design recommendations.",

    "General": "STRATEGIC VALUE: General sector awareness. CONSIDER: Monitor for emerging trends or issues that could require ClearPath positioning. Assess if this signals market shift that affects policy advocacy priorities. File for background intelligence on critical minerals landscape.",
}