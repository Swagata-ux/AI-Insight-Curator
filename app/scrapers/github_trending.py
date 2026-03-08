from datetime import datetime, timezone
from typing import List
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel


class TrendingRepo(BaseModel):
    repo_name: str
    url: str
    description: str
    stars: str
    language: str
    stars_today: str
    scraped_at: datetime


class GitHubTrendingScraper:
    def __init__(self):
        self.base_url = "https://github.com/trending"
    
    def get_trending_repos(self, language: str = "python", since: str = "daily") -> List[TrendingRepo]:
        """
        Scrape GitHub trending repositories
        language: programming language filter (python, javascript, etc.)
        since: daily, weekly, monthly
        """
        url = f"{self.base_url}/{language}?since={since}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            
            repos = []
            articles = soup.find_all("article", class_="Box-row")
            
            for article in articles:
                try:
                    repo_link = article.find("h2").find("a")
                    repo_name = repo_link.get("href").strip("/")
                    repo_url = f"https://github.com{repo_link.get('href')}"
                    
                    description_elem = article.find("p", class_="col-9")
                    description = description_elem.text.strip() if description_elem else "No description"
                    
                    stars_elem = article.find("span", class_="d-inline-block float-sm-right")
                    stars = stars_elem.text.strip() if stars_elem else "0"
                    
                    language_elem = article.find("span", attrs={"itemprop": "programmingLanguage"})
                    language = language_elem.text.strip() if language_elem else "Unknown"
                    
                    stars_today_elem = article.find("span", class_="d-inline-block float-sm-right")
                    stars_today = stars_today_elem.text.strip() if stars_today_elem else "0"
                    
                    repos.append(TrendingRepo(
                        repo_name=repo_name,
                        url=repo_url,
                        description=description,
                        stars=stars,
                        language=language,
                        stars_today=stars_today,
                        scraped_at=datetime.now(timezone.utc)
                    ))
                except Exception:
                    continue
            
            return repos
        except Exception:
            return []


if __name__ == "__main__":
    scraper = GitHubTrendingScraper()
    repos = scraper.get_trending_repos(language="python", since="daily")
    for repo in repos[:5]:
        print(f"{repo.repo_name}: {repo.description[:100]}")
