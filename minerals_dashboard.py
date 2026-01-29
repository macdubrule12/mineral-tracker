import streamlit as st
from news_fetcher import fetch_news
from datetime import datetime, timedelta
import re

# Page config - MUST be first Streamlit command
st.set_page_config(
    page_title="Critical Minerals Tracker",
    page_icon="🔋",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
/* Main app */
.stApp { background-color: #FFFFFF !important; }
.stApp h1, .stApp h2, .stApp h3 { color: #193D69 !important; }
.stApp p, .stApp span, .stApp div, .stApp label { color: #193D69 !important; }
[data-testid="stMetricValue"] { color: #193D69 !important; }
[data-testid="stMarkdownContainer"] { color: #193D69 !important; }
a { color: #9D1C20 !important; }

/* Sidebar styling */
[data-testid="stSidebar"] { background-color: #F8F9FA !important; border-right: 2px solid #193D69; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: #193D69 !important; }
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #193D69 !important; }

/* Selectbox styling - white background with navy text */
[data-testid="stSidebar"] [data-baseweb="select"] { background-color: #FFFFFF !important; }
[data-testid="stSidebar"] [data-baseweb="select"] * { color: #193D69 !important; background-color: #FFFFFF !important; }
[data-testid="stSidebar"] input { background-color: #FFFFFF !important; color: #193D69 !important; }

/* Tier tag with emoji */
.tier-tag {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 500;
    margin-right: 8px;
    background-color: #F5F5F5;
    color: #193D69 !important;
    border: 1px solid #E0E0E0;
}

/* Sidebar section headers */
.sidebar-header {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #6c757d !important;
    margin-top: 20px;
    margin-bottom: 8px;
}

/* Region map buttons */
.region-btn {
    display: inline-block;
    padding: 6px 10px;
    margin: 3px;
    border-radius: 6px;
    font-size: 12px;
    cursor: pointer;
    border: 1px solid #dee2e6;
    background-color: #ffffff;
    color: #193D69 !important;
    text-align: center;
}
.region-btn:hover { background-color: #e9ecef; }
.region-btn.selected { background-color: #193D69; color: white !important; border-color: #193D69; }

/* Theme and region tags */
.tag {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 11px;
    margin-right: 4px;
    margin-top: 4px;
}
.theme-tag { background-color: #E3F2FD; color: #1565C0 !important; }
.region-tag { background-color: #FFF3E0; color: #E65100 !important; }

/* Compact action items row */
.action-items-row {
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
    flex-wrap: wrap;
}
.action-item-compact {
    flex: 1;
    min-width: 280px;
    max-width: 400px;
    background-color: #FFFFFF;
    border: 1px solid #E0E0E0;
    border-left: 4px solid #FFC107;
    border-radius: 6px;
    padding: 12px 14px;
    transition: box-shadow 0.2s;
}
.action-item-compact:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.action-item-title {
    font-weight: 600;
    font-size: 13px;
    color: #193D69 !important;
    margin-bottom: 6px;
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.action-item-meta {
    font-size: 11px;
    color: #6c757d !important;
    margin-bottom: 6px;
}
.action-item-angle {
    font-size: 11px;
    color: #1565C0 !important;
    background-color: #E8F4FD;
    padding: 4px 8px;
    border-radius: 4px;
    display: inline-block;
}
.action-item-link {
    font-size: 11px;
    margin-top: 8px;
}

/* Priority section (expanded view) */
.priority-card {
    background-color: #FFF8E1;
    border-left: 4px solid #FFC107;
    padding: 12px;
    margin-bottom: 12px;
    border-radius: 4px;
}
.priority-headline {
    font-weight: 600;
    color: #193D69 !important;
    margin-bottom: 4px;
}

/* Relevance badges */
.relevance-high { background-color: #C62828; color: white !important; }
.relevance-medium { background-color: #F57C00; color: white !important; }
.relevance-low { background-color: #9E9E9E; color: white !important; }
.relevance-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: bold;
    margin-right: 6px;
}

/* Policy trigger tags */
.trigger-tag {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 10px;
    margin-right: 4px;
    margin-top: 4px;
    background-color: #E8EAF6;
    color: #3949AB !important;
    border: 1px solid #7986CB;
}

/* Why it matters section - enhanced */
.why-matters {
    background-color: #F8F9FA;
    padding: 12px 14px;
    margin: 10px 0;
    border-radius: 8px;
    font-size: 13px;
    border: 1px solid #E8E8E8;
}
.why-label {
    font-weight: 700;
    color: #193D69 !important;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
    display: block;
}
.why-text {
    color: #333 !important;
    line-height: 1.5;
    margin-bottom: 10px;
}
.clearpath-section {
    background-color: #E8F4FD;
    border-left: 4px solid #1976D2;
    padding: 10px 12px;
    margin-top: 10px;
    border-radius: 0 6px 6px 0;
}
.clearpath-label {
    font-weight: 700;
    color: #1565C0 !important;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
    display: block;
}
.clearpath-text {
    color: #193D69 !important;
    font-size: 13px;
    line-height: 1.5;
}

/* Meeting mode card */
.meeting-card {
    background-color: #E3F2FD;
    border-left: 4px solid #1976D2;
    padding: 12px;
    margin-bottom: 12px;
    border-radius: 4px;
    transition: opacity 0.3s ease;
}

/* Meeting mode enhancements */
.meeting-progress {
    background: linear-gradient(135deg, #E8F4FD 0%, #F0F7FF 100%);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 20px;
}

.followup-summary {
    background-color: #FFF8E1;
    border: 1px solid #FFD54F;
    border-radius: 8px;
    padding: 16px;
    margin-top: 20px;
}

.followup-item {
    background-color: #FFFFFF;
    border-left: 3px solid #FF9800;
    padding: 10px 12px;
    margin-bottom: 10px;
    border-radius: 4px;
}

/* Checkbox styling for meeting mode */
[data-testid="stCheckbox"] {
    margin-top: 20px;
}

/* Text area for action notes - light background */
[data-testid="stTextArea"] textarea {
    background-color: #FFFFFF !important;
    color: #193D69 !important;
    border: 1px solid #dee2e6 !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: #193D69 !important;
    box-shadow: 0 0 0 1px #193D69 !important;
}

/* Fix code display in markdown - completely remove code formatting */
.why-text code, .clearpath-text code,
.why-text pre, .clearpath-text pre,
.digest-item code, .digest-item pre,
.meeting-card code, .meeting-card pre {
    background-color: transparent !important;
    color: inherit !important;
    padding: 0 !important;
    font-family: inherit !important;
    border: none !important;
    display: inline !important;
}

/* Hide any code blocks completely */
.why-matters pre, .clearpath-section pre {
    display: none !important;
}

/* Friday highlights banner */
.friday-banner {
    background: linear-gradient(135deg, #193D69 0%, #2E5A8C 100%);
    color: white !important;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.friday-banner h3 { color: white !important; margin-bottom: 10px; }
.friday-banner p { color: #E0E0E0 !important; }
.friday-item {
    background-color: rgba(255,255,255,0.1);
    padding: 10px 12px;
    border-radius: 6px;
    margin: 8px 0;
    border-left: 3px solid #FFC107;
}
.friday-item strong { color: white !important; }
.friday-item span { color: #B0BEC5 !important; font-size: 12px; }

/* Override Streamlit black accents with navy/gray theme */
.stButton > button {
    background-color: #FFFFFF !important;
    color: #193D69 !important;
    border: 1px solid #193D69 !important;
}
.stButton > button:hover {
    background-color: #193D69 !important;
    color: #FFFFFF !important;
}
[data-testid="stMetricLabel"] { color: #6c757d !important; }
[data-testid="stMetricValue"] { color: #193D69 !important; }
hr { border-color: #dee2e6 !important; }
.stDivider { background-color: #dee2e6 !important; }

/* Remove black from inputs, toggles, and controls */
.stTextInput input, .stSelectbox select, .stMultiSelect input {
    border-color: #dee2e6 !important;
    color: #193D69 !important;
}
.stTextInput input:focus, .stSelectbox select:focus {
    border-color: #193D69 !important;
    box-shadow: 0 0 0 1px #193D69 !important;
}
[data-testid="stToggle"] span { color: #193D69 !important; }
.stToggle > label > div[data-checked="true"] { background-color: #193D69 !important; }

/* Expander styling - remove all black */
.streamlit-expanderHeader { color: #193D69 !important; border-color: #dee2e6 !important; background-color: #FFFFFF !important; }
.streamlit-expanderHeader:hover { color: #193D69 !important; background-color: #F8F9FA !important; }
.streamlit-expanderHeader:focus { color: #193D69 !important; background-color: #F8F9FA !important; outline: none !important; box-shadow: none !important; }
[data-testid="stExpander"] { border-color: #dee2e6 !important; background-color: #FFFFFF !important; }
[data-testid="stExpander"] summary { color: #193D69 !important; background-color: #FFFFFF !important; }
[data-testid="stExpander"] summary:focus { outline: none !important; box-shadow: none !important; }
[data-testid="stExpander"] details { border-color: #dee2e6 !important; }
[data-testid="stExpander"] svg { fill: #193D69 !important; stroke: #193D69 !important; }
details[open] summary { background-color: #F8F9FA !important; }

/* Header area styling */
header[data-testid="stHeader"] { background-color: #FFFFFF !important; }
[data-testid="stToolbar"] { background-color: #FFFFFF !important; }
[data-testid="stToolbar"] button { color: #193D69 !important; }
[data-testid="stDecoration"] { background-color: #193D69 !important; }

/* Main content area */
.main .block-container { background-color: #FFFFFF !important; }
[data-testid="stMainBlockContainer"] { background-color: #FFFFFF !important; }

/* Tab styling */
.stTabs [data-baseweb="tab-list"] { border-bottom-color: #dee2e6 !important; }
.stTabs [data-baseweb="tab"] { color: #6c757d !important; }
.stTabs [aria-selected="true"] { color: #193D69 !important; border-bottom-color: #193D69 !important; }

/* Checkbox and radio */
.stCheckbox label, .stRadio label { color: #193D69 !important; }
[data-testid="stCheckbox"] svg { fill: #193D69 !important; }

/* Download button - navy like other buttons */
.stDownloadButton > button {
    border-color: #193D69 !important;
    color: #193D69 !important;
    background-color: #FFFFFF !important;
}
.stDownloadButton > button:hover {
    background-color: #193D69 !important;
    color: #FFFFFF !important;
}

/* Link button - red accent for action items */
.stLinkButton > a { border-color: #9D1C20 !important; color: #9D1C20 !important; background-color: #FFFFFF !important; }
.stLinkButton > a:hover { background-color: #9D1C20 !important; color: #FFFFFF !important; }

/* Action items expander - button-like styling */
[data-testid="stExpander"]:has(summary:first-child) {
    border: 1px solid #193D69 !important;
    border-radius: 4px !important;
}
[data-testid="stExpander"] summary {
    padding: 8px 16px !important;
}
[data-testid="stExpander"] summary:hover {
    background-color: #193D69 !important;
    color: #FFFFFF !important;
}
[data-testid="stExpander"] summary:hover p,
[data-testid="stExpander"] summary:hover span {
    color: #FFFFFF !important;
}

/* Sidebar button styling */
[data-testid="stSidebar"] .stButton > button {
    background-color: #FFFFFF !important;
    color: #193D69 !important;
    border: 1px solid #dee2e6 !important;
    font-size: 12px !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #e9ecef !important;
    color: #193D69 !important;
}

/* Region map image */
.region-map {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 10px;
    opacity: 0.9;
}

/* Weekly digest styling */
.digest-container {
    background-color: #FAFBFC;
    border: 1px solid #dee2e6;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}
.digest-header {
    display: flex;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 2px solid #193D69;
}
.digest-header h3 {
    margin: 0;
    color: #193D69 !important;
}
.digest-date {
    color: #6c757d !important;
    font-size: 14px;
    margin-left: auto;
}
.digest-section {
    margin-bottom: 20px;
}
.digest-section-title {
    font-size: 14px;
    font-weight: 600;
    color: #193D69 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.digest-item {
    background-color: #FFFFFF;
    border: 1px solid #E8E8E8;
    border-radius: 8px;
    padding: 14px;
    margin-bottom: 10px;
}
.digest-item-headline {
    font-weight: 600;
    color: #193D69 !important;
    margin-bottom: 6px;
    font-size: 14px;
}
.digest-item-meta {
    font-size: 12px;
    color: #6c757d !important;
    margin-bottom: 8px;
}
.clearpath-implications {
    background-color: #E8F4FD;
    border-left: 4px solid #1976D2;
    padding: 12px 14px;
    border-radius: 0 6px 6px 0;
    margin-top: 10px;
}
.clearpath-implications-title {
    font-size: 11px;
    font-weight: 700;
    color: #1565C0 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
}
.clearpath-implications-text {
    color: #193D69 !important;
    font-size: 13px;
    line-height: 1.5;
}
.digest-summary {
    background: linear-gradient(135deg, #193D69 0%, #2E5A8C 100%);
    color: white !important;
    padding: 16px;
    border-radius: 8px;
    margin-bottom: 16px;
}
.digest-summary h4 { color: white !important; margin: 0 0 8px 0; }
.digest-summary p { color: #E0E0E0 !important; margin: 0; font-size: 14px; }
.digest-stat {
    display: inline-block;
    background-color: rgba(255,255,255,0.15);
    padding: 4px 10px;
    border-radius: 4px;
    margin-right: 8px;
    font-size: 12px;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Load news data
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_news():
    return fetch_news()

# Helper function to sanitize text for HTML display
def sanitize_html(text):
    """Remove problematic characters that cause rendering issues"""
    if not text:
        return ""
    # Convert to string if not already
    text = str(text)

    # Remove any base64-like or URL-encoded strings (long alphanumeric sequences)
    text = re.sub(r'[A-Za-z0-9+/=]{50,}', '', text)

    # Remove any markdown code blocks completely
    text = re.sub(r'```[\s\S]*?```', '', text)  # Remove triple backtick blocks
    text = re.sub(r'`[^`]+`', '', text)  # Remove inline code

    # Replace any remaining backticks or code markers
    text = text.replace('`', '').replace('~', '')

    # Replace angle brackets that might be interpreted as HTML
    text = text.replace('<', '&lt;').replace('>', '&gt;')

    # Replace special chars that might cause issues
    text = text.replace('{', '&#123;').replace('}', '&#125;')
    text = text.replace('[', '&#91;').replace(']', '&#93;')

    # Remove any HTML/XML-like tags that might have gotten through
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up extra whitespace
    text = ' '.join(text.split())

    return text.strip()

news_items = load_news()

# Tier emoji mapping
TIER_EMOJIS = {
    "Gov": "🏛️",
    "Wire": "📡",
    "Trade": "🏭",
    "Policy": "📋"
}

# SIDEBAR - Logo and branding
st.sidebar.image(
    "https://clearpath.org/wp-content/uploads/sites/44/2018/04/clearpath-logo-vpad-300x300.png",
    use_column_width=True
)
st.sidebar.markdown("### Critical Minerals Tracker")
st.sidebar.caption("Policy Intelligence Dashboard")
st.sidebar.markdown("---")

# Filter section
st.sidebar.markdown('<p class="sidebar-header">Filter Articles</p>', unsafe_allow_html=True)

tiers = ["All", "Gov", "Wire", "Trade", "Policy"]
selected_tier = st.sidebar.selectbox("Source Type", tiers, label_visibility="visible")

minerals = ["All", "Lithium", "Cobalt", "Nickel", "Copper", "Rare Earth", "Graphite", "Battery Metals", "Mining"]
selected_mineral = st.sidebar.selectbox("Mineral", minerals, label_visibility="visible")

sources = ["All"] + sorted(set(item["source"] for item in news_items))
selected_source = st.sidebar.selectbox("Source", sources, label_visibility="visible")

# Region picker
st.sidebar.markdown("---")
st.sidebar.markdown('<p class="sidebar-header">Region</p>', unsafe_allow_html=True)

# Define regions with emoji flags
regions_map = {
    "All": "🌍 All",
    "US": "🇺🇸 US",
    "Canada": "🇨🇦 Canada",
    "EU": "🇪🇺 EU",
    "China": "🇨🇳 China",
    "LATAM": "🌎 LATAM",
    "Africa": "🌍 Africa",
    "Australia": "🇦🇺 Australia",
    "Asia": "🌏 Asia",
}

# Create button grid for regions
if "selected_region" not in st.session_state:
    st.session_state.selected_region = "All"

col1, col2, col3 = st.sidebar.columns(3)
region_keys = list(regions_map.keys())

for i, region in enumerate(region_keys):
    col = [col1, col2, col3][i % 3]
    if col.button(regions_map[region], key=f"region_{region}", use_container_width=True):
        st.session_state.selected_region = region

selected_region = st.session_state.selected_region
st.sidebar.caption(f"Selected: **{regions_map[selected_region]}**")

# Relevance filter
st.sidebar.markdown("---")
st.sidebar.markdown('<p class="sidebar-header">ClearPath Relevance</p>', unsafe_allow_html=True)
relevance_options = ["All", "High", "Medium", "Low"]
selected_relevance = st.sidebar.selectbox("Relevance Level", relevance_options, label_visibility="collapsed")

# Weekly Meeting Mode
st.sidebar.markdown("---")
st.sidebar.markdown('<p class="sidebar-header">View Mode</p>', unsafe_allow_html=True)
meeting_mode = st.sidebar.toggle("Weekly Meeting Mode", value=False, help="Interactive meeting view with tracking")

# Initialize meeting session state
if "meeting_discussed" not in st.session_state:
    st.session_state.meeting_discussed = set()
if "meeting_followup" not in st.session_state:
    st.session_state.meeting_followup = {}
if "meeting_notes" not in st.session_state:
    st.session_state.meeting_notes = {}

# Tier legend
st.sidebar.markdown("---")
st.sidebar.markdown('<p class="sidebar-header">Source Types</p>', unsafe_allow_html=True)
st.sidebar.markdown("""
🏛️ **Gov** - Government sources
📡 **Wire** - Wire services
🏭 **Trade** - Industry press
📋 **Policy** - Policy analysis
""")

# MAIN HEADER
st.title("Critical Minerals News Tracker")
st.write("Daily intelligence for ClearPath policy team")

# WEEKLY DIGEST - Pre-meeting preparation
is_friday = datetime.now().weekday() == 4  # 4 = Friday

# Initialize session state
if "show_weekly_digest" not in st.session_state:
    st.session_state.show_weekly_digest = is_friday
if "digest_dismissed" not in st.session_state:
    st.session_state.digest_dismissed = False

# Get weekly data (last 7 days)
week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
weekly_items = [item for item in news_items if item.get("date", "") >= week_ago]
weekly_high = [i for i in weekly_items if i.get("relevance_level") == "High"]
weekly_medium = [i for i in weekly_items if i.get("relevance_level") == "Medium"]

# Group by themes for digest
theme_counts = {}
for item in weekly_high + weekly_medium:
    for theme in item.get("themes", []):
        theme_counts[theme] = theme_counts.get(theme, 0) + 1
top_themes = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)[:3]

# Sidebar toggle for weekly digest
with st.sidebar:
    st.markdown("---")
    if st.button("📊 Weekly Digest", use_container_width=True, help="Pre-meeting summary"):
        st.session_state.show_weekly_digest = True
        st.session_state.digest_dismissed = False
        st.rerun()

# Show Weekly Digest
if (st.session_state.show_weekly_digest or is_friday) and not st.session_state.digest_dismissed and weekly_high:
    st.markdown('<div class="digest-container">', unsafe_allow_html=True)

    # Header
    week_start = (datetime.now() - timedelta(days=7)).strftime("%b %d")
    week_end = datetime.now().strftime("%b %d, %Y")
    st.markdown(f"""
    <div class="digest-header">
        <h3>📊 Weekly Digest</h3>
        <span class="digest-date">{week_start} - {week_end}</span>
    </div>
    """, unsafe_allow_html=True)

    # Summary stats
    theme_text = ", ".join([t[0] for t in top_themes]) if top_themes else "Various"
    st.markdown(f"""
    <div class="digest-summary">
        <h4>Week at a Glance</h4>
        <p>
            <span class="digest-stat">📰 {len(weekly_items)} articles</span>
            <span class="digest-stat">🔴 {len(weekly_high)} high priority</span>
            <span class="digest-stat">🟠 {len(weekly_medium)} notable</span>
        </p>
        <p style="margin-top: 10px;">Top themes: {theme_text}</p>
    </div>
    """, unsafe_allow_html=True)

    # High priority items with ClearPath implications
    if weekly_high:
        st.markdown("""
        <div class="digest-section">
            <div class="digest-section-title">🔴 High Priority - Action Required</div>
        </div>
        """, unsafe_allow_html=True)

        for item in weekly_high[:5]:
            tier_emoji = TIER_EMOJIS.get(item["tier_label"], "📄")
            triggers = ", ".join(item.get("policy_triggers", [])[:2])
            trigger_text = f" | Triggers: {triggers}" if triggers else ""

            # Sanitize text
            why_matters_clean = sanitize_html(item.get("why_matters", "Developing story with policy implications."))
            clearpath_clean = sanitize_html(item.get("clearpath_angle", "Monitor for potential engagement opportunities."))

            st.markdown(f"""
            <div class="digest-item">
                <div class="digest-item-headline">{sanitize_html(item["headline"])}</div>
                <div class="digest-item-meta">{tier_emoji} {item["tier_label"]} • {item["source"]} • {item["date"]}{trigger_text}</div>
                <div class="clearpath-implications">
                    <div class="clearpath-implications-title">What This Means for ClearPath</div>
                    <div class="clearpath-implications-text">
                        <strong>Context:</strong> {why_matters_clean}<br>
                        <strong>Strategic angle:</strong> {clearpath_clean}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Notable items (medium relevance)
    if weekly_medium:
        with st.expander(f"🟠 Notable Stories ({len(weekly_medium)})", expanded=False):
            for item in weekly_medium[:5]:
                tier_emoji = TIER_EMOJIS.get(item["tier_label"], "📄")
                why_matters_clean = sanitize_html(item.get("why_matters", ""))
                st.markdown(f"""
                <div class="digest-item">
                    <div class="digest-item-headline">{sanitize_html(item["headline"])}</div>
                    <div class="digest-item-meta">{tier_emoji} {item["tier_label"]} • {item["source"]} • {item["date"]}</div>
                    <p style="font-size: 13px; color: #555; margin-top: 6px;">{why_matters_clean}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Dismiss button
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("✓ Dismiss digest"):
            st.session_state.digest_dismissed = True
            st.rerun()
    with col2:
        # Generate digest text for export
        digest_text = f"CLEARPATH WEEKLY DIGEST\n{week_start} - {week_end}\n\n"
        digest_text += f"SUMMARY: {len(weekly_items)} articles | {len(weekly_high)} high priority | {len(weekly_medium)} notable\n\n"
        digest_text += "HIGH PRIORITY ITEMS:\n" + "="*40 + "\n\n"
        for i, item in enumerate(weekly_high[:5], 1):
            digest_text += f"{i}. {item['headline']}\n"
            digest_text += f"   Source: {item['source']} | {item['date']}\n"
            digest_text += f"   Why it matters: {item.get('why_matters', 'N/A')}\n"
            digest_text += f"   ClearPath angle: {item.get('clearpath_angle', 'N/A')}\n"
            digest_text += f"   Link: {item['link']}\n\n"

        st.download_button(
            "📥 Export Digest",
            data=digest_text,
            file_name=f"clearpath_digest_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )

    st.markdown("---")

# PRIORITY SECTION - Only show HIGH relevance items from last 7 days
week_ago_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
priority_items = [
    item for item in news_items
    if item.get("relevance_level") == "High"
    and item.get("date", "") >= week_ago_date
][:3]  # Top 3 only

if priority_items:
    with st.expander(f"⚡ Action Items ({len(priority_items)})", expanded=False):
        for item in priority_items:
            tier_emoji = TIER_EMOJIS.get(item["tier_label"], "📄")
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{item['headline']}**")
                st.caption(f"{tier_emoji} {item['tier_label']} • {item['source']} • {item['date']}")
                if item.get("clearpath_angle"):
                    clearpath_clean = sanitize_html(item.get("clearpath_angle", ""))
                    st.markdown(f"💡 _{clearpath_clean}_")
            with col2:
                st.link_button("Read →", item["link"], use_container_width=True)
            st.divider()

# FILTER DATA
filtered = []
today = datetime.now()
week_ago = (today - timedelta(days=7)).strftime("%Y-%m-%d")

for item in news_items:
    tier_match = selected_tier == "All" or item["tier_label"] == selected_tier
    mineral_match = selected_mineral == "All" or item["mineral"] == selected_mineral
    source_match = selected_source == "All" or item["source"] == selected_source
    region_match = selected_region == "All" or selected_region in item.get("regions", [])
    relevance_match = selected_relevance == "All" or item.get("relevance_level") == selected_relevance

    # Meeting mode: only show last 7 days
    if meeting_mode:
        date_match = item.get("date", "") >= week_ago
    else:
        date_match = True

    if tier_match and mineral_match and source_match and region_match and relevance_match and date_match:
        filtered.append(item)

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    st.metric("Articles Found", len(filtered))
with col2:
    high_count = len([i for i in filtered if i.get("relevance_level") == "High"])
    st.metric("High Relevance", high_count)

# Add refresh and export buttons
btn_col1, btn_col2 = st.columns([1, 1])
with btn_col1:
    if st.button("🔄 Refresh News"):
        st.cache_data.clear()
        st.rerun()

# Generate export text for Slack
def generate_slack_brief(items, max_items=10):
    """Generate a Slack-formatted brief"""
    lines = ["*Critical Minerals Weekly Brief*", f"_{datetime.now().strftime('%B %d, %Y')}_", ""]

    # Group by relevance
    high_items = [i for i in items if i.get("relevance_level") == "High"][:5]
    medium_items = [i for i in items if i.get("relevance_level") == "Medium"][:5]

    if high_items:
        lines.append("*🔴 HIGH RELEVANCE*")
        for item in high_items:
            triggers = ", ".join(item.get("policy_triggers", [])[:2])
            trigger_text = f" [{triggers}]" if triggers else ""
            lines.append(f"• {item['headline']}{trigger_text}")
            lines.append(f"  _{item.get('why_matters', '')}_")
            lines.append(f"  {item['link']}")
        lines.append("")

    if medium_items:
        lines.append("*🟠 NOTABLE*")
        for item in medium_items:
            lines.append(f"• {item['headline']}")
            lines.append(f"  {item['link']}")

    return "\n".join(lines)

slack_text = generate_slack_brief(filtered)

with btn_col2:
    # Download as plain text file
    st.download_button(
        label="📥 Download Brief",
        data=slack_text,
        file_name=f"minerals_brief_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain",
        help="Download as text file"
    )

# DISPLAY RESULTS
if meeting_mode:
    st.markdown("### 📋 Weekly Meeting Brief")
    st.caption("Interactive meeting view • Last 7 days • Check off as you discuss")

    # Meeting progress tracker
    total_high = len([i for i in filtered if i.get("relevance_level") == "High"])
    discussed_count = len(st.session_state.meeting_discussed)
    followup_count = len(st.session_state.meeting_followup)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("High Priority Items", total_high)
    with col2:
        st.metric("Discussed", discussed_count)
    with col3:
        st.metric("Follow-up Flagged", followup_count)

    st.markdown("---")

    # Group articles by relevance for meeting mode
    for level in ["High", "Medium", "Low"]:
        level_items = [i for i in filtered if i.get("relevance_level") == level]
        if level_items:
            emoji = {"High": "🔴", "Medium": "🟠", "Low": "⚪"}[level]
            st.markdown(f"#### {emoji} {level} Relevance ({len(level_items)})")

            for idx, item in enumerate(level_items):
                item_id = f"{level}_{idx}_{item['headline'][:30]}"

                tier_emoji = TIER_EMOJIS.get(item["tier_label"], "📄")
                tier_tag = f'<span class="tier-tag">{tier_emoji} {item["tier_label"]}</span>'
                trigger_tags = "".join([f'<span class="trigger-tag">{t}</span>' for t in item.get("policy_triggers", [])])

                # Interactive container with checkbox
                col_check, col_content, col_actions = st.columns([0.5, 8, 1.5])

                with col_check:
                    is_discussed = st.checkbox(
                        "✓",
                        value=item_id in st.session_state.meeting_discussed,
                        key=f"discuss_{item_id}",
                        label_visibility="collapsed",
                        help="Mark as discussed"
                    )
                    if is_discussed:
                        st.session_state.meeting_discussed.add(item_id)
                    elif item_id in st.session_state.meeting_discussed:
                        st.session_state.meeting_discussed.remove(item_id)

                with col_content:
                    # Show strategic angle only for High relevance items in meeting mode
                    # Sanitize text to prevent code blocks
                    why_matters_text = sanitize_html(item.get("why_matters", "Developing story."))

                    if level == "High" and item.get("clearpath_angle"):
                        clearpath_text = sanitize_html(item.get("clearpath_angle", "Monitor for developments."))
                        clearpath_section = f"""
                            <div class="clearpath-section">
                                <span class="clearpath-label">ClearPath Angle</span>
                                <span class="clearpath-text">{clearpath_text}</span>
                            </div>
                        """
                    else:
                        clearpath_section = ""

                    # Add opacity if discussed
                    card_style = "opacity: 0.6;" if is_discussed else ""

                    st.markdown(f"""
                    <div class="meeting-card" style="{card_style}">
                        <strong>{sanitize_html(item["headline"])}</strong><br>
                        {tier_tag} {item["source"]} | {item["date"]} {trigger_tags}
                        <div class="why-matters">
                            <span class="why-label">Why It Matters</span>
                            <span class="why-text">{why_matters_text}</span>
                            {clearpath_section}
                        </div>
                        <a href="{item["link"]}" target="_blank">Read full article →</a>
                    </div>
                    """, unsafe_allow_html=True)

                with col_actions:
                    # Follow-up flag
                    is_flagged = item_id in st.session_state.meeting_followup
                    if st.button("📌" if not is_flagged else "✓ Follow-up", key=f"flag_{item_id}", use_container_width=True, type="secondary" if not is_flagged else "primary"):
                        if is_flagged:
                            del st.session_state.meeting_followup[item_id]
                            if item_id in st.session_state.meeting_notes:
                                del st.session_state.meeting_notes[item_id]
                        else:
                            st.session_state.meeting_followup[item_id] = item
                        st.rerun()

                # Show note input if flagged for follow-up
                if item_id in st.session_state.meeting_followup:
                    with st.expander("📝 Add action notes", expanded=False):
                        note_text = st.text_area(
                            "Action items / Owner / Timeline",
                            value=st.session_state.meeting_notes.get(item_id, ""),
                            key=f"note_{item_id}",
                            placeholder="e.g., Policy team to draft brief | Sarah | This week",
                            height=80
                        )
                        st.session_state.meeting_notes[item_id] = note_text

                st.markdown("<br>", unsafe_allow_html=True)

    # FOLLOW-UP SUMMARY at end of meeting
    if st.session_state.meeting_followup:
        st.markdown("---")
        st.markdown("### 📌 Follow-up Items")
        st.caption(f"{len(st.session_state.meeting_followup)} items flagged for action")

        for item_id, item in st.session_state.meeting_followup.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{item['headline']}**")
                if item_id in st.session_state.meeting_notes and st.session_state.meeting_notes[item_id]:
                    st.caption(f"📝 {st.session_state.meeting_notes[item_id]}")
                else:
                    st.caption("⚠️ No action notes added yet")
            with col2:
                if st.button("Remove", key=f"remove_followup_{item_id}"):
                    del st.session_state.meeting_followup[item_id]
                    if item_id in st.session_state.meeting_notes:
                        del st.session_state.meeting_notes[item_id]
                    st.rerun()

    # EXPORT MEETING NOTES
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        # Reset meeting tracking
        if st.button("🔄 Reset Meeting Tracking", use_container_width=True):
            st.session_state.meeting_discussed = set()
            st.session_state.meeting_followup = {}
            st.session_state.meeting_notes = {}
            st.rerun()

    with col2:
        # Export meeting notes
        if st.session_state.meeting_followup:
            meeting_notes_text = f"CLEARPATH MINERALS MEETING NOTES\n{datetime.now().strftime('%B %d, %Y')}\n\n"
            meeting_notes_text += "="*50 + "\n"
            meeting_notes_text += f"ATTENDANCE: [Add names]\n"
            meeting_notes_text += f"ITEMS DISCUSSED: {len(st.session_state.meeting_discussed)}\n"
            meeting_notes_text += f"FOLLOW-UP ITEMS: {len(st.session_state.meeting_followup)}\n"
            meeting_notes_text += "="*50 + "\n\n"

            meeting_notes_text += "FOLLOW-UP ACTIONS:\n" + "="*50 + "\n\n"

            for item_id, item in st.session_state.meeting_followup.items():
                meeting_notes_text += f"• {item['headline']}\n"
                meeting_notes_text += f"  Source: {item['source']} | {item['date']}\n"
                meeting_notes_text += f"  Link: {item['link']}\n"
                if item_id in st.session_state.meeting_notes and st.session_state.meeting_notes[item_id]:
                    meeting_notes_text += f"  ACTION: {st.session_state.meeting_notes[item_id]}\n"
                else:
                    meeting_notes_text += f"  ACTION: [Not specified]\n"
                meeting_notes_text += "\n"

            st.download_button(
                "📥 Export Notes",
                data=meeting_notes_text,
                file_name=f"meeting_notes_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )

else:
    st.markdown("### All Articles")

    if len(filtered) == 0:
        st.warning("No articles found matching your filters. Try selecting 'All' for both filters.")
    else:
        for item in filtered:
            st.subheader(item["headline"])

            # Show relevance + tier tag + metadata
            relevance_class = f"relevance-{item.get('relevance_level', 'Low').lower()}"
            relevance_badge = f'<span class="relevance-badge {relevance_class}">{item.get("relevance_level", "Low")}</span>'
            tier_emoji = TIER_EMOJIS.get(item["tier_label"], "📄")
            tier_tag = f'<span class="tier-tag">{tier_emoji} {item["tier_label"]}</span>'
            st.markdown(
                f'{relevance_badge} {tier_tag} {item["source"]} &nbsp;|&nbsp; {item["mineral"]} &nbsp;|&nbsp; {item["date"]}',
                unsafe_allow_html=True
            )

            # Show theme, region, and policy trigger tags
            theme_tags = "".join([f'<span class="tag theme-tag">{t}</span>' for t in item.get("themes", [])])
            region_tags = "".join([f'<span class="tag region-tag">{r}</span>' for r in item.get("regions", [])])
            trigger_tags = "".join([f'<span class="trigger-tag">{t}</span>' for t in item.get("policy_triggers", [])])
            if theme_tags or region_tags or trigger_tags:
                st.markdown(f'{theme_tags} {region_tags} {trigger_tags}', unsafe_allow_html=True)

            # Show "Why it matters" section
            if item.get("why_matters"):
                # Show strategic angle only for High relevance or Priority items
                show_strategic_angle = (item.get("relevance_level") == "High" or item.get("is_priority", False))

                # Sanitize text to prevent code blocks
                why_matters_clean = sanitize_html(item.get("why_matters", "Developing story with potential policy implications."))

                if show_strategic_angle and item.get("clearpath_angle"):
                    clearpath_clean = sanitize_html(item.get("clearpath_angle", "Monitor for engagement opportunities."))
                    st.markdown(f"""
                    <div class="why-matters">
                        <span class="why-label">Why It Matters</span>
                        <span class="why-text">{why_matters_clean}</span>
                        <div class="clearpath-section">
                            <span class="clearpath-label">ClearPath Strategic Angle</span>
                            <span class="clearpath-text">{clearpath_clean}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Just show why it matters without strategic angle
                    st.markdown(f"""
                    <div class="why-matters">
                        <span class="why-label">Why It Matters</span>
                        <span class="why-text">{why_matters_clean}</span>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown(f"[Read full article]({item['link']})")
            st.divider()