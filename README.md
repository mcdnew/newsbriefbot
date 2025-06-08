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
│   ├── public/               # HTML template
│   └── src/                  # React app
│       ├── api/              # Axios API wrappers
│       ├── pages/            # UI pages
│       ├── components/       # Shared UI components
│       ├── App.tsx           # Root component
│       ├── main.tsx          # Entry point
│       └── index.css         # Tailwind setup
├── data/                     # Temporary summaries and logs
├── nginx.conf                # Nginx reverse proxy config (frontend + /api backend)
├── .env                      # Environment variables
├── requirements.txt          # Python backend dependencies
├── docker-compose.yml        # Combined app orchestration
├── Dockerfile                # Backend/Frontend/Nginx Docker image
└── README.md
```

---

## 🚀 Getting Started (via Docker + Nginx Reverse Proxy)

### Requirements
- Docker
- Docker Compose

### Quick Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/mcdnew/newsbriefbot.git
   cd newsbriefbot
   ```
2. Create a `.env` file at the project root:
   ```env
   OPENAI_API_KEY=your_key_here
   ... other secrets ...
   ```
3. Build and run the app:
   ```bash
   docker-compose up --build
   ```

Then open:
- Full app (frontend + API): `http://localhost`
- FastAPI Swagger docs: `http://localhost/api/docs`

---

## 🔁 Reverse Proxy with Nginx

The app uses **Nginx as a reverse proxy** so:
- Frontend served at `/`
- API proxied at `/api/*` → FastAPI backend

This avoids CORS issues and provides clean paths for production.

---

## 🧠 Backend Modules Overview
(unchanged, see above)

---

## 🧠 Frontend Stack (Vite + React + Tailwind)
- **Framework**: Vite + React + TypeScript
- **Styling**: Tailwind CSS
- **HTTP**: Axios (uses `/api/*` paths)
- **Components**: `/src/pages`, `/src/components`

---

## 🐳 Docker Deployment

### 🧱 Services
- **frontend** → React app built and served via Nginx
- **backend** → FastAPI served via uvicorn (proxied by Nginx)
- **nginx** → Public gateway at `http://localhost`

### ✅ Run it:
```bash
docker-compose up --build
```

---

## 📂 Future Roadmap
- ✉️ Email newsletter export
- 📊 Admin dashboard & stats
- 🔐 Auth + multi-user support
- 🌍 Multi-language summarization

---

## 📄 License
MIT License. Free to use, modify, and distribute.



