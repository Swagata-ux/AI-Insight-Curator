import os
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def send_slack_notification(digest_response) -> bool:
    """Send AI news digest to Slack channel"""
    if not SLACK_WEBHOOK_URL:
        print("SLACK_WEBHOOK_URL not configured, skipping Slack notification")
        return False
    
    try:
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🤖 Daily AI News Digest",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{digest_response.introduction.greeting}*\n\n{digest_response.introduction.introduction}"
                }
            },
            {
                "type": "divider"
            }
        ]
        
        # Add top articles
        for idx, article in enumerate(digest_response.articles[:5], 1):
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{idx}. {article.title}*\n{article.summary[:200]}...\n<{article.url}|Read more →>"
                }
            })
        
        # Add GitHub repos section
        if digest_response.github_repos:
            blocks.append({"type": "divider"})
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*🔥 Trending AI Repos on GitHub*"
                }
            })
            
            for repo in digest_response.github_repos[:3]:
                blocks.append({
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*{repo['repo_name']}* ({repo['language']})\n{repo['description'][:150]}...\n⭐ {repo['stars']} | 🌟 {repo['stars_today']} today\n<{repo['url']}|View on GitHub>"
                    }
                })
        
        # Add AI jobs section
        if digest_response.ai_jobs:
            blocks.append({"type": "divider"})
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*💼 Latest AI Job Opportunities*"
                }
            })
            
            for job in digest_response.ai_jobs[:3]:
                blocks.append({
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*{job['title']}* at {job['company']}\n📍 {job['location']} | {job['job_type']}\n<{job['url']}|Apply now>"
                    }
                })
        
        payload = {
            "blocks": blocks,
            "text": f"Daily AI News Digest - {digest_response.introduction.greeting}"
        }
        
        response = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
        response.raise_for_status()
        
        return True
    except Exception as e:
        print(f"Failed to send Slack notification: {e}")
        return False


if __name__ == "__main__":
    # Test with sample data
    from app.agent.email_agent import EmailDigestResponse, EmailIntroduction, RankedArticleDetail
    
    test_digest = EmailDigestResponse(
        introduction=EmailIntroduction(
            greeting="Hey Swagata, here is your daily digest of AI news.",
            introduction="Today's top AI news and updates."
        ),
        articles=[
            RankedArticleDetail(
                digest_id="test1",
                rank=1,
                relevance_score=9.5,
                title="Test Article",
                summary="This is a test summary",
                url="https://example.com",
                article_type="test"
            )
        ],
        total_ranked=1,
        top_n=1,
        github_repos=[],
        ai_jobs=[]
    )
    
    result = send_slack_notification(test_digest)
    print(f"Slack notification sent: {result}")
