# NewsBriefBot

NewsBriefBot is an open-source, self-hosted automation tool that fetches and summarizes content from sources like RSS feeds, websites, and email press releases. It generates concise, categorized briefings and provides a web UI for source management, preview, and export.

---

## 📌 Features (MVP)
- Source management (RSS, web scraping, email parsing)
- GPT or local-model summarization
- Daily or weekly scheduled runs (via APScheduler)
- Manual job trigger via UI
- Markdown/HTML output previews
- Export to file or email

---

## 🧱 Project Structure
```
newsbriefbot/
├── backend/
│   ├── api/                  # FastAPI routes
│   ├── core/                 # fetcher, summarizer, generator
│   ├── models/               # SQLAlchemy models
│   ├── scheduler/            # APScheduler tasks
│   └── main.py               # FastAPI app entry point
├── frontend/
│   └── src/
│       ├── pages/            # Config, dashboard, preview
│       ├── components/       # UI building blocks
│       └── api/              # API client
├── data/                     # Temp summaries and logs
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

## 🛠 Tech Stack
- **Backend**: Python, FastAPI, SQLAlchemy, APScheduler
- **Frontend**: React + TypeScript (TSX), Tailwind CSS, ShadCN/UI
- **AI/NLP**: OpenAI GPT-4 or HuggingFace (T5, BART)
- **Storage**: SQLite (default)

---

## 📂 Future Roadmap
- ✉️ Email newsletter export
- 📊 Admin dashboard & stats
- 🔐 Auth + multi-user support
- 🌍 Multi-language summarization

---

## 📄 License
MIT License. Free to use, modify, and distribute.

