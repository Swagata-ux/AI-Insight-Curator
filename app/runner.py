from typing import List
from .config import YOUTUBE_CHANNELS
from .scrapers.youtube import YouTubeScraper, ChannelVideo
from .scrapers.openai import OpenAIScraper, OpenAIArticle
from .scrapers.anthropic import AnthropicScraper, AnthropicArticle
from .scrapers.github_trending import GitHubTrendingScraper
from .scrapers.ai_jobs import AIJobScraper
from .database.repository import Repository


def run_scrapers(hours: int = 24) -> dict:
    youtube_scraper = YouTubeScraper()
    openai_scraper = OpenAIScraper()
    anthropic_scraper = AnthropicScraper()
    github_scraper = GitHubTrendingScraper()
    job_scraper = AIJobScraper()
    repo = Repository()
    
    youtube_videos = []
    video_dicts = []
    for channel_id in YOUTUBE_CHANNELS:
        videos = youtube_scraper.get_latest_videos(channel_id, hours=hours)
        youtube_videos.extend(videos)
        video_dicts.extend([
            {
                "video_id": v.video_id,
                "title": v.title,
                "url": v.url,
                "channel_id": channel_id,
                "published_at": v.published_at,
                "description": v.description,
                "transcript": v.transcript
            }
            for v in videos
        ])
    
    openai_articles = openai_scraper.get_articles(hours=hours)
    anthropic_articles = anthropic_scraper.get_articles(hours=hours)
    
    github_repos = github_scraper.get_trending_repos(language="python", since="daily")
    ai_jobs = job_scraper.get_ai_jobs(limit=20)
    
    if video_dicts:
        repo.bulk_create_youtube_videos(video_dicts)
    
    if openai_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in openai_articles
        ]
        repo.bulk_create_openai_articles(article_dicts)
    
    if anthropic_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in anthropic_articles
        ]
        repo.bulk_create_anthropic_articles(article_dicts)
    
    if github_repos:
        repo_dicts = [
            {
                "repo_name": r.repo_name,
                "url": r.url,
                "description": r.description,
                "stars": r.stars,
                "language": r.language,
                "stars_today": r.stars_today,
                "scraped_at": r.scraped_at
            }
            for r in github_repos
        ]
        repo.bulk_create_github_repos(repo_dicts)
    
    if ai_jobs:
        job_dicts = [
            {
                "job_id": j.job_id,
                "title": j.title,
                "company": j.company,
                "location": j.location,
                "url": j.url,
                "description": j.description,
                "posted_at": j.posted_at,
                "job_type": j.job_type
            }
            for j in ai_jobs
        ]
        repo.bulk_create_ai_jobs(job_dicts)
    
    return {
        "youtube": youtube_videos,
        "openai": openai_articles,
        "anthropic": anthropic_articles,
        "github_repos": github_repos,
        "ai_jobs": ai_jobs,
    }


if __name__ == "__main__":
    results = run_scrapers(hours=24)
    print(f"YouTube videos: {len(results['youtube'])}")
    print(f"OpenAI articles: {len(results['openai'])}")
    print(f"Anthropic articles: {len(results['anthropic'])}")
    print(f"GitHub repos: {len(results['github_repos'])}")
    print(f"AI jobs: {len(results['ai_jobs'])}")

