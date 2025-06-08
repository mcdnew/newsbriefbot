# NewsBriefBot

NewsBriefBot is an open-source, self-hosted automation tool that fetches and summarizes content from sources like RSS feeds, websites, and email press releases. It generates concise, categorized briefings and provides a web UI for source management, preview, and export.

---

## 📌 Features (MVP)
- Source management (RSS, web scraping, email parsing)
- GPT or local-model summarization
- Daily or weekly scheduled runs (via APScheduler)
- Manual job trigger via API
- Markdown/HTML output previews
- Export to file or email

---

## 🧱 Project Structure
```
newsbriefbot/
├── backend/
│   ├── api/                  # FastAPI routes (sources, generate)
│   │   ├── source.py         # API endpoints to add/list sources
│   │   └── generate.py       # Manual trigger endpoint
│   ├── core/                 # Core processing modules
│   │   ├── fetcher.py        # Fetch articles from RSS or URLs
│   │   ├── summarizer.py     # Summarize article content (OpenAI or local)
│   │   └── generator.py      # Generate formatted brief from summaries
│   ├── models/               # SQLAlchemy models and DB engine
│   │   ├── database.py       # Database connection and session
│   │   └── source.py         # Source and Summary data models
│   ├── scheduler/            # Scheduled task manager
│   │   └── tasks.py          # Runs jobs to fetch, summarize, store
│   └── main.py               # FastAPI app entry + scheduler start
├── frontend/
│   └── src/
│       ├── pages/            # UI pages (dashboard, config, preview)
│       ├── components/       # Reusable UI components
│       └── api/              # API client (Axios/fetch wrappers)
├── data/                     # Temporary summaries and logs
├── .env                      # Environment variables (e.g. API keys)
├── docker-compose.yml        # Service orchestration
└── README.md
```

---

## 🚀 Getting Started

### Requirements
- Python 3.9+
- Node.js (for frontend)
- Docker & Docker Compose (for local dev)

### Quick Start
1. Clone the repo:
   ```bash
   git clone https://github.com/mcdnew/newsbriefbot.git
   cd newsbriefbot
   ```
2. Create your `.env` file and add your OpenAI API key, etc.
3. Start the app:
   ```bash
   docker-compose up --build
   ```

Then visit:
- Backend API: `http://localhost:8000/docs`
- Frontend UI: `http://localhost:3000`

---

## 🛠 Backend Modules

### 🔹 `models/database.py`
- Sets up SQLite database
- Provides `SessionLocal` and `Base`

### 🔹 `models/source.py`
- `Source`: stores input feeds or websites
- `Summary`: stores fetched and summarized content

### 🔹 `core/fetcher.py`
- `fetch_rss_articles(url)`: uses `feedparser` to pull recent articles
- `scrape_article(url)`: uses `requests + BeautifulSoup` to extract text

### 🔹 `core/summarizer.py`
- `summarize_text(text)`: calls OpenAI API to generate summaries

### 🔹 `core/generator.py`
- `generate_brief(list)`: formats a Markdown summary document

### 🔹 `scheduler/tasks.py`
- `run_job()`: executes a full pipeline:
  - Fetch sources
  - Scrape/parse content
  - Summarize
  - Save to DB
  - Print brief
- `start_scheduler()`: launches APScheduler loop

### 🔹 `api/source.py`
- `GET /sources/`: list all sources
- `POST /sources/`: add new source (RSS, web, email)

### 🔹 `api/generate.py`
- `POST /generate/`: manually trigger the job runner

### 🔹 `main.py`
- Initializes FastAPI app
- Registers routes
- Starts scheduler

---

## 🧠 Usage Examples

### Add a Source (POST `/sources/`)
```json
{
  "name": "TechCrunch RSS",
  "type": "rss",
  "config": { "url": "https://techcrunch.com/feed/" },
  "schedule": "daily"
}
```

### Manually Generate Brief (POST `/generate/`)
Trigger the background job manually via Swagger or any HTTP client.

---

## 📂 Future Roadmap
- ✉️ Email newsletter export
- 📊 Admin dashboard & stats
- 🔐 Auth + multi-user support
- 🌍 Multi-language summarization

---

## 📄 License
MIT License. Free to use, modify, and distribute.

