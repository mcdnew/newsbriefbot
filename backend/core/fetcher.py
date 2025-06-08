import feedparser
import requests
from bs4 import BeautifulSoup

def fetch_rss_articles(feed_url, max_items=5):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:max_items]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", ""),
            "content": entry.get("summary", "")
        })
    return articles

def scrape_article(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return ""

