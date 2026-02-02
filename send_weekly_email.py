#!/usr/bin/env python3
"""
Automated Weekly Email for Critical Minerals Tracker
Sends digest of High Priority stories to mining@clearpath.org
"""

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Import our news fetching functions
from news_fetcher import fetch_news

def get_weekly_stories():
    """Fetch High Priority stories from the last 7 days"""
    print("Fetching news...")
    all_stories = fetch_news()

    # Filter for High Priority items from last 7 days
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    high_priority = [
        story for story in all_stories
        if story.get("relevance_level") == "High"
        and story.get("date", "") >= week_ago
    ]

    medium_priority = [
        story for story in all_stories
        if story.get("relevance_level") == "Medium"
        and story.get("date", "") >= week_ago
    ]

    print(f"Found {len(high_priority)} High Priority and {len(medium_priority)} Medium Priority stories")

    return high_priority[:5], medium_priority[:10]  # Top 5 high, top 10 medium


def create_email_html(high_stories, medium_stories):
    """Generate beautiful HTML email content"""

    # Calculate date range
    week_start = (datetime.now() - timedelta(days=7)).strftime("%b %d")
    week_end = datetime.now().strftime("%b %d, %Y")

    # Count top themes
    all_stories = high_stories + medium_stories
    theme_counts = {}
    for story in all_stories:
        for theme in story.get("themes", []):
            theme_counts[theme] = theme_counts.get(theme, 0) + 1
    top_themes = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    theme_text = ", ".join([t[0] for t in top_themes]) if top_themes else "Various topics"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #193D69; margin: 0; padding: 0; background-color: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; background-color: #ffffff; }}
            .header {{ background: linear-gradient(135deg, #193D69 0%, #2E5A8C 100%); color: white; padding: 30px 20px; text-align: center; }}
            .header h1 {{ margin: 0; font-size: 24px; }}
            .header p {{ margin: 10px 0 0 0; opacity: 0.9; font-size: 14px; }}
            .summary {{ background-color: #E8F4FD; padding: 20px; margin: 20px; border-radius: 8px; border-left: 4px solid #1976D2; }}
            .summary h3 {{ margin: 0 0 10px 0; color: #1565C0; }}
            .stat {{ display: inline-block; background-color: rgba(25,61,105,0.1); padding: 4px 12px; border-radius: 4px; margin-right: 10px; font-size: 13px; }}
            .content {{ padding: 0 20px 20px 20px; }}
            .section-title {{ color: #193D69; font-size: 18px; font-weight: 600; margin: 30px 0 15px 0; padding-bottom: 10px; border-bottom: 2px solid #193D69; }}
            .story {{ background-color: #FAFBFC; border: 1px solid #E8E8E8; border-radius: 8px; padding: 20px; margin-bottom: 20px; }}
            .story-headline {{ font-size: 16px; font-weight: 600; color: #193D69; margin: 0 0 10px 0; line-height: 1.4; }}
            .story-meta {{ font-size: 13px; color: #666; margin-bottom: 12px; }}
            .story-section {{ background-color: #F8F9FA; padding: 12px; border-radius: 6px; margin: 10px 0; }}
            .story-label {{ font-weight: 700; color: #193D69; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 4px; }}
            .clearpath-section {{ background-color: #E8F4FD; border-left: 4px solid #1976D2; padding: 12px; border-radius: 0 6px 6px 0; margin-top: 10px; }}
            .story-link {{ display: inline-block; background-color: #9D1C20; color: white !important; text-decoration: none; padding: 8px 16px; border-radius: 4px; margin-top: 10px; font-size: 14px; }}
            .story-link:hover {{ background-color: #7D1518; }}
            .footer {{ background-color: #f5f5f5; padding: 20px; text-align: center; font-size: 12px; color: #666; }}
            .footer a {{ color: #1976D2; text-decoration: none; }}
            .dashboard-link {{ background-color: #193D69; color: white; text-align: center; padding: 20px; margin: 20px; border-radius: 8px; }}
            .dashboard-link a {{ color: white; text-decoration: none; font-weight: 600; font-size: 16px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header -->
            <div class="header">
                <h1>📊 Critical Minerals Weekly Digest</h1>
                <p>{week_start} – {week_end}</p>
            </div>

            <!-- Summary -->
            <div class="summary">
                <h3>Week at a Glance</h3>
                <p>
                    <span class="stat">📰 {len(all_stories)} articles</span>
                    <span class="stat">🔴 {len(high_stories)} high priority</span>
                    <span class="stat">🟠 {len(medium_stories)} notable</span>
                </p>
                <p style="margin-top: 12px; font-size: 14px;">Top themes: {theme_text}</p>
            </div>

            <div class="content">
    """

    # High Priority Stories
    if high_stories:
        html += """
                <div class="section-title">🔴 High Priority – Action Required</div>
        """

        for story in high_stories:
            tier_emoji = {"Gov": "🏛️", "Wire": "📡", "Trade": "🏭", "Policy": "📋"}.get(story.get("tier_label"), "📄")
            triggers = ", ".join(story.get("policy_triggers", [])[:2])
            trigger_text = f" | {triggers}" if triggers else ""

            html += f"""
                <div class="story">
                    <div class="story-headline">{story['headline']}</div>
                    <div class="story-meta">{tier_emoji} {story['tier_label']} • {story['source']} • {story['date']}{trigger_text}</div>

                    <div class="story-section">
                        <span class="story-label">Why It Matters</span>
                        <div style="color: #333; line-height: 1.5;">{story.get('why_matters', 'Developing story.')}</div>
                    </div>

                    <div class="clearpath-section">
                        <span class="story-label" style="color: #1565C0;">ClearPath Strategic Angle</span>
                        <div style="color: #193D69; line-height: 1.5;">{story.get('clearpath_angle', 'Monitor for developments.')}</div>
                    </div>

                    <a href="{story['link']}" class="story-link">Read Full Article →</a>
                </div>
            """

    # Notable Stories (Medium Priority - Collapsed)
    if medium_stories:
        html += """
                <div class="section-title">🟠 Notable Stories</div>
                <div style="font-size: 14px; color: #666; margin-bottom: 15px;">Worth monitoring but not urgent</div>
        """

        for story in medium_stories[:5]:  # Show top 5 medium
            tier_emoji = {"Gov": "🏛️", "Wire": "📡", "Trade": "🏭", "Policy": "📋"}.get(story.get("tier_label"), "📄")
            html += f"""
                <div style="background-color: #F8F9FA; padding: 12px; margin-bottom: 10px; border-radius: 6px; border-left: 3px solid #FF9800;">
                    <div style="font-weight: 600; color: #193D69; margin-bottom: 4px;">{story['headline']}</div>
                    <div style="font-size: 12px; color: #666; margin-bottom: 6px;">{tier_emoji} {story['tier_label']} • {story['source']} • {story['date']}</div>
                    <div style="font-size: 13px; color: #555;">{story.get('why_matters', '')}</div>
                    <a href="{story['link']}" style="color: #1976D2; font-size: 13px; text-decoration: none;">Read more →</a>
                </div>
            """

    # Dashboard Link
    html += """
                <div class="dashboard-link">
                    <a href="https://clearpath-minerals.streamlit.app">📊 View Full Dashboard</a>
                    <p style="margin: 10px 0 0 0; font-size: 13px; opacity: 0.9;">Interactive filters, meeting mode, and complete archive</p>
                </div>
            </div>

            <!-- Footer -->
            <div class="footer">
                <p><strong>Critical Minerals News Tracker</strong></p>
                <p>Automated intelligence for ClearPath policy team</p>
                <p style="margin-top: 15px;">
                    <a href="https://clearpath-minerals.streamlit.app">Dashboard</a> •
                    <a href="mailto:macdubrule@gmail.com">Contact</a>
                </p>
                <p style="margin-top: 10px; font-size: 11px; color: #999;">
                    You're receiving this because you're part of the ClearPath minerals working group.
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    return html


def send_email(to_email, from_email, password, subject, html_content):
    """Send email via Gmail SMTP"""
    print(f"Sending email to {to_email}...")

    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"ClearPath Minerals Tracker <{from_email}>"
    msg['To'] = to_email

    # Attach HTML content
    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)

        # Send email
        server.send_message(msg)
        server.quit()

        print(f"✅ Email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return False


def main():
    """Main execution"""
    print("=" * 50)
    print("Critical Minerals Weekly Email Automation")
    print("=" * 50)

    # Get email configuration from environment
    to_email = os.environ.get('EMAIL_TO', 'mining@clearpath.org')
    from_email = os.environ.get('EMAIL_FROM')
    password = os.environ.get('EMAIL_PASSWORD')

    if not from_email:
        print("ERROR: EMAIL_FROM environment variable not set")
        sys.exit(1)

    if not password:
        print("ERROR: EMAIL_PASSWORD environment variable not set")
        sys.exit(1)

    # Fetch stories
    high_stories, medium_stories = get_weekly_stories()

    # Don't send if no high priority stories
    if not high_stories:
        print("No high priority stories this week. Skipping email.")
        return

    # Create email content
    html_content = create_email_html(high_stories, medium_stories)

    # Create subject line
    week_start = (datetime.now() - timedelta(days=7)).strftime("%b %d")
    week_end = datetime.now().strftime("%b %d, %Y")
    subject = f"Critical Minerals Weekly Digest – {week_start} to {week_end}"

    # Send email
    success = send_email(to_email, from_email, password, subject, html_content)

    if success:
        print("✅ Weekly digest sent successfully!")
    else:
        print("❌ Failed to send email")
        sys.exit(1)


if __name__ == "__main__":
    main()
