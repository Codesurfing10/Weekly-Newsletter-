import requests
import datetime
import heapq

NEWS_API_KEY = "422c66187c1b4815bd4b904a83eac6ee"  # Inserted NewsAPI key
KEYWORDS = [
    "innovation", "breakthrough", "revolutionary", "patent", "disruptive", "technology",
    "discovery", "new product", "novel", "startup", "award-winning", "groundbreaking"
]
INDUSTRIES = [
    "healthcare", "finance", "energy", "transportation", "technology", "agriculture",
    "manufacturing", "education", "retail", "construction"
]

def fetch_articles(query, from_date, to_date, page=1):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&from={from_date}&to={to_date}&language=en&pageSize=100&page={page}&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["articles"]

def is_innovation_related(article):
    content = (article.get("title", "") or "") + " " + (article.get("description", "") or "")
    return any(keyword in content.lower() for keyword in KEYWORDS)

def summarize_article(article):
    # Simple summarization: return title and first 200 chars of description
    desc = (article.get("description", "") or "")
    return f"{article.get('title')}: {desc[:200]}..."

def sweep_innovations():
    today = datetime.datetime.utcnow().date()
    from_date = today - datetime.timedelta(days=7)
    all_innovations = []
    for industry in INDUSTRIES:
        try:
            articles = fetch_articles(f"{industry} innovation", from_date, today)
            for article in articles:
                if is_innovation_related(article):
                    summary = summarize_article(article)
                    all_innovations.append((
                        article.get("publishedAt", ""),
                        summary,
                        article.get("url", "")
                    ))
        except Exception as e:
            print(f"Error fetching articles for {industry}: {e}")
    # Get the top 20 most recent innovations
    top_innovations = heapq.nlargest(20, all_innovations, key=lambda x: x[0])
    return top_innovations

if __name__ == "__main__":
    innovations = sweep_innovations()
    print("Top Innovations Across All Industries (Past Week):")
    for date, summary, url in innovations:
        print(f"- {date}: {summary}\n  Read more: {url}\n")
