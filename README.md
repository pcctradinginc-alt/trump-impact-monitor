[README.md](https://github.com/user-attachments/files/28196544/README.md)
# 🚨 Trump-Impact Monitor v2.4

Hourly automated monitoring of Trump-related news with AI-powered financial impact analysis.  
**No local setup required – 100% deployable via GitHub browser UI.**

---

## ⚡ Quick Deploy (Browser Only – 5 Steps)

### Step 1 – Create GitHub Repo

1. Go to [github.com/new](https://github.com/new)
2. Name: `trump-impact-monitor`
3. Visibility: **Private** ✅
4. Click **Create repository**

---

### Step 2 – Upload All Files

In your new repo, click **"uploading an existing file"** (or use **Add file → Upload files**):

Upload these files keeping the exact folder structure:

```
trump-impact-monitor/
├── .github/
│   └── workflows/
│       └── trump-monitor.yml     ← must be in this exact path!
├── alerts.db                     ← upload the empty one provided
├── main.py
├── requirements.txt
├── entities.json
└── init_db.py
```

> **Tip for the workflow file:** GitHub's upload UI doesn't create subfolders automatically.  
> Use the browser file editor instead:  
> Click **"Create new file"** → type `.github/workflows/trump-monitor.yml` in the name field  
> → paste the content → **Commit**.

---

### Step 3 – Add GitHub Secrets

Go to **Settings → Secrets and variables → Actions → New repository secret**

| Secret Name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-...` (your Claude key) |
| `SCRAPE_CREATORS_API_KEY` | Your ScrapeCreators key (100 free credits) |
| `NEWSAPI_KEY` | Your NewsAPI.org key (free tier works) |
| `GMAIL_EMAIL` | `yourname@gmail.com` |
| `GMAIL_APP_PASSWORD` | 16-char Gmail App Password (see below) |
| `RECIPIENT_EMAIL` | Where alerts should be sent |

**Create Gmail App Password:**
1. Google Account → Security → 2-Step Verification (must be ON)
2. Search "App passwords" → Select "Mail" → Name it "GitHub Actions"
3. Copy the 16-character code (no spaces)

---

### Step 4 – Test Manual Run

Go to **Actions → Trump Impact Monitor (hourly) → Run workflow → Run workflow**

Check the logs – you should see sources being fetched and (if a match is found) an e-mail arriving.

---

### Step 5 – Done ✅

The workflow now runs **every full hour automatically**.  
A new commit `chore: update alerts.db` appears each run if new alerts were found.

---

## 📁 File Overview

| File | Purpose |
|---|---|
| `main.py` | Core logic: fetch → entity-resolve → LLM → e-mail |
| `requirements.txt` | Python dependencies (minimal, fast install) |
| `entities.json` | Ticker → keyword mappings (extend freely) |
| `.github/workflows/trump-monitor.yml` | GitHub Actions cron job |
| `alerts.db` | SQLite deduplication database (auto-committed) |
| `init_db.py` | Optional: pre-create DB locally |

---

## 🔍 How It Works

```
Every hour:
  ┌─ Truth Social (ScrapeCreators API)
  ├─ NewsAPI.org (all sources, Donald Trump)
  ├─ NewsAPI.org (CNBC only, Donald Trump)
  └─ White House RSS
         │
         ▼
  Entity Resolution (entities.json)
         │
    Ticker found?
         │ Yes
         ▼
  Claude Sonnet (Anthropic API)
  → Sentiment + Investment check + Summary + Turbo suggestion
         │
         ▼
  Gmail Alert (SMTP + App Password)
  SQLite saved (deduplication)
```

---

## ✏️ Extend entities.json

Add any company you want to monitor:

```json
"NVDA": ["Nvidia", "NVDA", "Jensen Huang", "H100", "Blackwell"]
```

The key is the ticker symbol (used in e-mail subject), values are keywords to match in articles/posts.

---

## 🛠️ API Keys (all free tiers available)

| Service | Free Tier | Get Key |
|---|---|---|
| Anthropic Claude | Pay-per-use (~$0.003/alert) | [console.anthropic.com](https://console.anthropic.com) |
| ScrapeCreators | 100 free credits | [scrapecreators.com](https://scrapecreators.com) |
| NewsAPI | 100 req/day free | [newsapi.org/register](https://newsapi.org/register) |
| Gmail | Free (App Password) | [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) |
