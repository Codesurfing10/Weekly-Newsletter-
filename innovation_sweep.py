import requests
import datetime
import heapq
import json
import os

NEWS_API_KEY = "422c66187c1b4815bd4b904a83eac6ee"  # Inserted NewsAPI key
KEYWORDS = [
    "innovation", "breakthrough", "revolutionary", "patent", "disruptive", "technology",
    "discovery", "new product", "novel", "startup", "award-winning", "groundbreaking",
    "cutting-edge", "advanced", "next-generation"
]
# Updated to cover cutting-edge fields as specified in the requirements
INDUSTRIES = [
    "materials science", "biochemistry", "chemistry", "rockets", "space exploration",
    "mining technology", "industrial manufacturing", "machinery", "engines",
    "quantum hardware", "quantum computing", "satellites", "water technology",
    "food technology", "flight technology", "aviation", "nature conservation",
    "biomimicry", "nanotechnology", "aerospace"
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

def save_to_json(innovations, filename="articles.json"):
    """Save the scraped articles to a JSON file for GitHub Pages."""
    articles_data = []
    for date, summary, url in innovations:
        # Extract title from summary
        title = summary.split(":")[0] if ":" in summary else summary[:100]
        articles_data.append({
            "date": date,
            "title": title,
            "summary": summary,
            "url": url
        })
    
    output_data = {
        "last_updated": datetime.datetime.utcnow().isoformat(),
        "total_articles": len(articles_data),
        "articles": articles_data
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(articles_data)} articles to {filename}")

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
    
    # Save to JSON file for GitHub Pages
    save_to_json(innovations, "articles.json")
    print("\nArticles have been saved to articles.json for GitHub Pages display.")
