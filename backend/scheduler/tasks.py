from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from models.database import SessionLocal
from models.source import Source, Summary
from core.fetcher import fetch_rss_articles, scrape_article
from core.summarizer import summarize_text
from core.generator import generate_brief

def run_job():
    db: Session = SessionLocal()

    sources = db.query(Source).all()
    all_summaries = []

    for source in sources:
        config = source.config
        articles = []

        if source.type == "rss":
            articles = fetch_rss_articles(config["url"])
        elif source.type == "web":
            for url in config.get("urls", []):
                content = scrape_article(url)
                articles.append({"title": url, "content": content, "link": url})

        for article in articles:
            summary_text = summarize_text(article["content"])
            summary = Summary(
                source_id=source.id,
                title=article["title"],
                content=article["content"],
                summary=summary_text
            )
            db.add(summary)
            all_summaries.append({
                "title": article["title"],
                "summary": summary_text
            })

    db.commit()
    print("Brief generated:\n")
    print(generate_brief(all_summaries))

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_job, "interval", minutes=60)  # 🔁 runs hourly
    scheduler.start()

