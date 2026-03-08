# Slack Integration Setup Guide

## Setup Steps

### 1. Create Slack Webhook

1. Go to https://api.slack.com/apps
2. Click **"Create New App"** → **"From scratch"**
3. Name: `AI News Aggregator`, select workspace
4. Click **"Incoming Webhooks"** → Toggle ON
5. Click **"Add New Webhook to Workspace"**
6. Select channel (e.g., `#ai-news`) → **"Allow"**
7. Copy the webhook URL

### 2. Add to .env

```env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

### 3. Test

```bash
uv run python main.py 168 10
```

Check your Slack channel for the digest!

## What's Included

- Top 5 AI articles
- Top 3 GitHub repos
- Top 3 AI jobs

## Disable

Remove `SLACK_WEBHOOK_URL` from `.env` to skip Slack notifications.
