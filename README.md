# Cutting-Edge Innovation Finder

This is an innovation sweeping newsletter that discovers and displays cutting-edge articles across multiple cutting-edge fields including materials science, biochemistry, chemistry, rockets, space exploration, mining, industrial manufacturing, machinery, engines, quantum hardware, satellites, water technology, food technology, flight, and nature.

## Features

- **Python Web Scraper**: Automatically fetches the latest innovation articles from NewsAPI
- **GitHub Pages Website**: Beautiful, responsive website displaying discovered articles
- **Multi-field Coverage**: Covers 20+ cutting-edge technology and science fields
- **JSON Data Export**: Articles saved in structured JSON format for easy integration
- **Modern UI**: Gradient background (blue → steel → sunrise) with responsive design

## Setup

### Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Running the Scraper

First, set your NewsAPI key as an environment variable (optional - a default key is provided):

```bash
export NEWS_API_KEY="your-api-key-here"
```

To fetch the latest cutting-edge articles:

```bash
python innovation_sweep.py
```

This will:
1. Fetch articles from NewsAPI across all specified fields
2. Filter for innovation-related content
3. Generate `articles.json` with the top 20 most recent discoveries

### Viewing the Website

Open `index.html` in a web browser, or deploy to GitHub Pages:

1. Push the code to GitHub
2. Go to repository Settings → Pages
3. Select the branch to deploy (e.g., `cutting-edge-finder`)
4. The site will be available at: `https://[username].github.io/[repo-name]/`

## File Structure

- `innovation_sweep.py` - Main scraper script
- `index.html` - GitHub Pages main page
- `styles.css` - Styling with gradient background
- `script.js` - Dynamic article loading and display
- `articles.json` - Scraped articles data
- `requirements.txt` - Python dependencies

## Fields Covered

- Materials Science
- Biochemistry & Chemistry
- Rockets & Space Exploration
- Mining Technology
- Industrial Manufacturing
- Machinery & Engines
- Quantum Hardware & Computing
- Satellites
- Water Technology
- Food Technology
- Flight & Aviation
- Nature & Biomimicry
- Nanotechnology & Aerospace
