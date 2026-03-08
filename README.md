# AI Insight Curator

An intelligent AI news aggregation system that scrapes, curates, and delivers personalized daily digests from top AI sources, trending GitHub repositories, and job postings via email and Slack.

## Features

- 🤖 **AI-Powered Curation**: Uses OpenAI GPT-4 to rank and summarize articles based on your interests
- 📰 **Multi-Source Aggregation**: OpenAI blog, Anthropic blog, YouTube channels, GitHub trending repos, AI jobs
- 📧 **Email Delivery**: Beautiful HTML email digests sent to your inbox
- 💬 **Slack Integration**: Formatted notifications to your Slack workspace
- 🗄️ **PostgreSQL Database**: Persistent storage with duplicate detection
- 🐳 **Docker Support**: Easy deployment with Docker Compose
- ⚙️ **Fully Customizable**: Adjust sources, preferences, and delivery options

## What You Get

**Daily Digest Includes:**
- Top 10 curated AI news articles with summaries
- 5 trending AI/ML GitHub repositories
- 5 latest AI job opportunities
- Personalized introduction and insights

## Quick Start

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- OpenAI API key
- Gmail account with app password
- (Optional) Slack webhook URL

### Installation

```bash
# Clone repository
git clone https://github.com/Swagata-ux/AI-Insight-Curator.git
cd AI-Insight-Curator

# Install dependencies
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# Setup environment
cp app/example.env app/.env
# Edit app/.env with your credentials (see API Setup Guide below)

# Start database
cd docker
docker compose up -d
cd ..

# Initialize database
uv run python -m app.database.create_tables

# Run the aggregator
uv run python main.py 168 10  # Last 168 hours, top 10 articles
```

## API Setup Guide

### 1. OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-proj-...`)
4. Add to `.env`: `OPENAI_API_KEY=sk-proj-YOUR_KEY`
5. Add credits: https://platform.openai.com/settings/organization/billing

**Detailed guide**: [docs/API_SETUP.md](docs/API_SETUP.md)

### 2. Gmail App Password

1. Enable 2-Step Verification: https://myaccount.google.com/security
2. Go to App Passwords: https://myaccount.google.com/apppasswords
3. Select "Mail" → "Other" → Name it "AI News Aggregator"
4. Copy the 16-character password (remove spaces)
5. Add to `.env`:
   ```env
   MY_EMAIL=your.email@gmail.com
   APP_PASSWORD=your16charpassword
   ```

**Detailed guide**: [docs/API_SETUP.md](docs/API_SETUP.md)

### 3. Slack Webhook (Optional)

1. Go to https://api.slack.com/apps
2. Create app → Enable Incoming Webhooks
3. Add webhook to your channel
4. Copy webhook URL
5. Add to `.env`: `SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...`

**Detailed guide**: [docs/SLACK_SETUP.md](docs/SLACK_SETUP.md)

## Configuration

### Customize User Profile

Edit `app/profiles/user_profile.py`:

```python
USER_PROFILE = {
    "name": "Your Name",
    "interests": [
        "Large Language Models",
        "AI Safety",
        # Add your interests
    ]
}
```

### Add News Sources

Edit `app/config.py`:

```python
YOUTUBE_CHANNELS = [
    "UCawZsQWqfGSbCI5yjkdVkTA",  # Matthew Berman
    # Add more channel IDs
]
```

## Usage

### Run Once

```bash
# Last 24 hours, top 10 articles
uv run python main.py

# Last 7 days, top 15 articles
uv run python main.py 168 15
```

### Schedule Daily (Cron)

```bash
# Add to crontab
0 8 * * * cd /path/to/AI-Insight-Curator && uv run python main.py
```

### Deploy to Render.com

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for cloud deployment instructions.

## Project Structure

```
ai-news-aggregator/
├── app/
│   ├── agent/           # AI agents (curator, digest, email)
│   ├── database/        # PostgreSQL models and repository
│   ├── profiles/        # User profile configuration
│   ├── scrapers/        # Source scrapers (YouTube, OpenAI, GitHub, Jobs)
│   ├── services/        # Processing services
│   ├── config.py        # Configuration
│   └── .env            # Environment variables (create from example.env)
├── docker/
│   └── docker-compose.yml
├── docs/               # Documentation
├── main.py            # Entry point
└── pyproject.toml     # Dependencies
```

## How It Works

1. **Scraping**: Collects articles, videos, GitHub repos, and jobs
2. **Processing**: Extracts transcripts, converts markdown, enriches content
3. **Curation**: AI ranks and selects top content based on your profile
4. **Digest Generation**: Creates personalized summaries
5. **Delivery**: Sends via email and Slack

## Technology Stack

- **Python 3.12+**
- **OpenAI GPT-4o-mini** for AI curation
- **PostgreSQL 17** for data storage
- **BeautifulSoup** for web scraping
- **Docker** for containerization
- **SMTP & Slack** for notifications

## Cost Estimates

- **OpenAI API**: ~$1-2/month for daily digests
- **Gmail**: Free
- **Slack**: Free
- **Database**: Free (local) or $7/month (Render.com)

## Troubleshooting

### Database Connection Error
```bash
# Ensure Docker is running
docker ps

# Restart database
cd docker && docker compose restart
```

### No Articles Found
```bash
# Increase time range
uv run python main.py 168 10  # 7 days instead of 24 hours
```

### Email Not Sending
- Use Gmail App Password, not regular password
- Ensure 2-Step Verification is enabled
- Remove spaces from app password

## Documentation

- [API Setup Guide](docs/API_SETUP.md) - Detailed credential setup
- [Slack Setup](docs/SLACK_SETUP.md) - Slack integration guide
- [Deployment Guide](docs/DEPLOYMENT.md) - Cloud deployment instructions

## Contributing

Contributions welcome! Feel free to:
- Add new scrapers for additional sources
- Improve AI curation logic
- Enhance email/Slack formatting
- Add new features

## License

MIT License - feel free to use and modify

## Support

For issues or questions:
- Open an issue on GitHub
- Check documentation in `docs/`

---

**Built with ❤️ for the AI community**
