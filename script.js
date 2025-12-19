// Load and display articles from the JSON file
async function loadArticles() {
    const articlesContainer = document.getElementById('articles-container');
    const lastUpdatedElement = document.getElementById('last-updated');
    const totalArticlesElement = document.getElementById('total-articles');

    try {
        // Fetch the articles JSON file
        const response = await fetch('articles.json');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Update info section
        const lastUpdated = new Date(data.last_updated);
        lastUpdatedElement.textContent = `Last Updated: ${lastUpdated.toLocaleString()}`;
        totalArticlesElement.textContent = `${data.total_articles} cutting-edge articles discovered`;
        
        // Clear loading message
        articlesContainer.innerHTML = '';
        
        // Check if there are articles
        if (!data.articles || data.articles.length === 0) {
            articlesContainer.innerHTML = '<p class="loading">No articles found. Run the scraper to fetch articles.</p>';
            return;
        }
        
        // Create and append article cards
        data.articles.forEach(article => {
            const articleCard = createArticleCard(article);
            articlesContainer.appendChild(articleCard);
        });
        
    } catch (error) {
        console.error('Error loading articles:', error);
        articlesContainer.innerHTML = `
            <div class="error">
                <h3>Unable to load articles</h3>
                <p>Error: ${error.message}</p>
                <p>Please ensure articles.json exists and the scraper has been run.</p>
            </div>
        `;
        lastUpdatedElement.textContent = 'Failed to load update information';
        totalArticlesElement.textContent = '';
    }
}

function createArticleCard(article) {
    // Create article card element
    const card = document.createElement('div');
    card.className = 'article-card';
    
    // Format date
    let formattedDate = 'Recent';
    if (article.date) {
        try {
            const date = new Date(article.date);
            formattedDate = date.toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'short', 
                day: 'numeric' 
            });
        } catch (e) {
            console.error('Error parsing date:', e);
        }
    }
    
    // Extract title and description from summary if needed
    let title = article.title || 'Untitled';
    let description = '';
    
    if (article.summary) {
        // If summary contains the full text, try to extract description
        const parts = article.summary.split(':');
        if (parts.length > 1) {
            description = parts.slice(1).join(':').trim();
        } else {
            description = article.summary;
        }
    }
    
    // Truncate description if too long
    if (description.length > 250) {
        description = description.substring(0, 250) + '...';
    }
    
    // Build card HTML
    card.innerHTML = `
        <div class="article-date">${formattedDate}</div>
        <div class="article-title">${escapeHtml(title)}</div>
        ${description ? `<div class="article-summary">${escapeHtml(description)}</div>` : ''}
        <a href="${article.url}" target="_blank" rel="noopener noreferrer" class="article-link">
            Read Full Article →
        </a>
    `;
    
    return card;
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Load articles when the page loads
document.addEventListener('DOMContentLoaded', loadArticles);
