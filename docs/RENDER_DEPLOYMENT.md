# Deploy to Render.com (Free Tier)

## Overview
Deploy AI Insight Curator to Render.com with free PostgreSQL database and scheduled daily execution.

## Prerequisites
- GitHub account with your repository
- Render.com account (free)
- OpenAI API key
- Gmail app password
- (Optional) Slack webhook URL

## Step-by-Step Deployment

### 1. Create Render Account

1. Go to https://render.com
2. Sign up with GitHub
3. Verify your email

### 2. Deploy via Blueprint

1. In Render dashboard, click **"New"** → **"Blueprint"**
2. Connect your GitHub repository: `Swagata-ux/AI-Insight-Curator`
3. Select branch: `master`
4. Render will detect `render.yaml` automatically
5. Click **"Apply"**

Render will create:
- **PostgreSQL Database** (free tier, 90 days retention)
- **Cron Job** (runs daily at 8 AM UTC)

### 3. Set Environment Variables

After deployment, go to the cron job service:

1. Click on **"daily-digest-job"**
2. Go to **"Environment"** tab
3. Add these variables:

```
OPENAI_API_KEY=sk-proj-YOUR_KEY_HERE
MY_EMAIL=your.email@gmail.com
APP_PASSWORD=your16charapppassword
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

**Note**: `DATABASE_URL` is auto-set by Render

### 4. Manual Trigger (Test)

1. Go to cron job service
2. Click **"Manual Deploy"** → **"Deploy latest commit"**
3. Check logs to verify it works
4. Check your email and Slack

### 5. Verify Schedule

The cron job runs daily at **8 AM UTC**. To change:

Edit `render.yaml`:
```yaml
schedule: "0 14 * * *"  # 2 PM UTC (9 AM EST)
```

Push changes to GitHub, Render auto-updates.

## Cron Schedule Format

`"minute hour day month weekday"`

Examples:
- `"0 8 * * *"` - Daily at 8 AM UTC
- `"0 14 * * *"` - Daily at 2 PM UTC
- `"0 0 * * 1"` - Every Monday at midnight UTC
- `"0 */12 * * *"` - Every 12 hours

## Free Tier Limits

**PostgreSQL:**
- 1 GB storage
- 90 days data retention
- Expires after 90 days (data deleted)

**Cron Jobs:**
- Limited execution time
- No concurrent runs

**Recommendation**: Upgrade to Starter ($7/month) for persistent database.

## Update Deployment

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add -A
   git commit -m "Update configuration"
   git push
   ```
3. Render auto-deploys on next scheduled run

## Troubleshooting

### Database Connection Error
- Verify `DATABASE_URL` is set (should be automatic)
- Check database service is running
- Restart cron job service

### Cron Job Not Running
- Check logs in Render dashboard
- Verify schedule syntax in `render.yaml`
- Ensure Docker build succeeded

### Email Not Sending
- Verify `MY_EMAIL` and `APP_PASSWORD` are correct
- Use Gmail app password, not regular password
- Check email service logs

### Build Failures
- Check Dockerfile syntax
- Verify all dependencies in `pyproject.toml`
- Review build logs for errors

## Monitor Execution

1. Go to cron job service in Render
2. Click **"Logs"** tab
3. View execution history and output
4. Check for errors or warnings

## Cost Optimization

**Free Tier Strategy:**
- Use free PostgreSQL (90 days)
- Run once daily (minimal compute)
- Monitor usage in Render dashboard

**Upgrade When:**
- Need persistent database (>90 days)
- Want more frequent runs
- Require better performance

## Alternative: Manual Deployment

If Blueprint doesn't work:

1. Create PostgreSQL database manually
2. Create Cron Job service:
   - Environment: Docker
   - Dockerfile path: `./Dockerfile`
   - Schedule: `0 8 * * *`
   - Command: `python main.py 168 10`
3. Add environment variables
4. Connect database

## Support

- Render Docs: https://render.com/docs
- Render Support: Available in dashboard
- Project Issues: GitHub repository

---

**Your AI Insight Curator will now run automatically every day!** 🚀
