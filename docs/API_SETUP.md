# API Keys & Credentials Setup Guide

## 1. OpenAI API Key

### Create OpenAI API Key

1. **Sign up/Login to OpenAI**
   - Go to https://platform.openai.com/
   - Create an account or sign in

2. **Navigate to API Keys**
   - Click on your profile (top right)
   - Select **"API keys"** from the menu
   - Or go directly to: https://platform.openai.com/api-keys

3. **Create New Key**
   - Click **"Create new secret key"**
   - Give it a name (e.g., "AI News Aggregator")
   - Click **"Create secret key"**

4. **Copy the Key**
   - Copy the key immediately (starts with `sk-proj-...`)
   - **Important**: You won't be able to see it again!
   - Store it securely

5. **Add to .env**
   ```env
   OPENAI_API_KEY=sk-proj-YOUR_KEY_HERE
   ```

### Add Credits (Required)

- Go to https://platform.openai.com/settings/organization/billing
- Add payment method
- Add at least $5 credit
- The app uses GPT-4o-mini (very affordable)

---

## 2. Gmail App Password

### Prerequisites
- Gmail account
- 2-Step Verification must be enabled

### Enable 2-Step Verification (if not already enabled)

1. Go to https://myaccount.google.com/security
2. Scroll to **"How you sign in to Google"**
3. Click **"2-Step Verification"**
4. Follow the setup process

### Create App Password

1. **Go to App Passwords**
   - Visit: https://myaccount.google.com/apppasswords
   - Or: Google Account → Security → 2-Step Verification → App passwords

2. **Generate Password**
   - Select app: **"Mail"**
   - Select device: **"Other (Custom name)"**
   - Enter name: **"AI News Aggregator"**
   - Click **"Generate"**

3. **Copy the Password**
   - You'll see a 16-character password (e.g., `abcd efgh ijkl mnop`)
   - Copy it (remove spaces)

4. **Add to .env**
   ```env
   MY_EMAIL=your.email@gmail.com
   APP_PASSWORD=abcdefghijklmnop
   ```

### Troubleshooting Gmail

**"Less secure app access" error:**
- Use App Password (not your regular password)
- Ensure 2-Step Verification is enabled

**"Invalid credentials" error:**
- Remove spaces from app password
- Regenerate app password if needed

---

## 3. Slack Webhook URL (Optional)

### Create Slack Webhook

1. **Go to Slack API**
   - Visit: https://api.slack.com/apps
   - Click **"Create New App"**

2. **Create App**
   - Choose **"From scratch"**
   - App Name: **"AI News Aggregator"**
   - Select your workspace
   - Click **"Create App"**

3. **Enable Incoming Webhooks**
   - In left sidebar, click **"Incoming Webhooks"**
   - Toggle **"Activate Incoming Webhooks"** to ON
   - Scroll down, click **"Add New Webhook to Workspace"**

4. **Select Channel**
   - Choose channel (e.g., `#ai-news`)
   - Click **"Allow"**

5. **Copy Webhook URL**
   - Copy the webhook URL (starts with `https://hooks.slack.com/services/...`)

6. **Add to .env**
   ```env
   SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
   ```

---

## Complete .env File Example

```env
# OpenAI API Key (Required)
OPENAI_API_KEY=sk-proj-YOUR_OPENAI_KEY_HERE

# Gmail Credentials (Required)
MY_EMAIL=your.email@gmail.com
APP_PASSWORD=your16charapppassword

# Slack Webhook (Optional)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T.../B.../XXX...

# Database (Auto-configured with Docker)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ai_news_aggregator
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

## Security Best Practices

1. **Never commit .env file**
   - Already in `.gitignore`
   - Keep credentials private

2. **Rotate keys regularly**
   - Change API keys every few months
   - Regenerate app passwords if compromised

3. **Use environment-specific keys**
   - Different keys for development/production
   - Limit API key permissions

4. **Monitor usage**
   - Check OpenAI usage: https://platform.openai.com/usage
   - Monitor Gmail activity: https://myaccount.google.com/security

---

## Cost Estimates

**OpenAI API (GPT-4o-mini):**
- ~$0.01-0.05 per daily digest
- ~$1-2 per month for daily use

**Gmail:**
- Free (no cost)

**Slack:**
- Free (no cost)

---

## Troubleshooting

### OpenAI API Issues

**"Invalid API key":**
- Verify key starts with `sk-proj-`
- Check for extra spaces
- Regenerate key if needed

**"Insufficient credits":**
- Add credits at https://platform.openai.com/settings/organization/billing

### Gmail Issues

**"Authentication failed":**
- Use App Password, not regular password
- Enable 2-Step Verification first
- Remove spaces from app password

### Slack Issues

**"Webhook not found":**
- Verify webhook URL is correct
- Check if app is still installed in workspace
- Regenerate webhook if needed

---

## Need Help?

- OpenAI Support: https://help.openai.com/
- Gmail Help: https://support.google.com/mail
- Slack Help: https://slack.com/help
