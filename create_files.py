import os

# Folder structure
folders = ["scripts", "data"]
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Files and starter content
files = {
    "scripts/scrape_players.py": "# Auto-map all NBA players from Basketball Reference\n",
    "scripts/scrape_stats.py": "# Scrape player game logs + positional stats\n",
    "scripts/scrape_team.py": "# Scrape team advanced stats (defense, pace, etc.)\n",
    "scripts/scrape_news.py": "# Scrape injury/news for players\n",
    "scripts/fetch_odds.py": "# Fetch odds from free sportsbook API\n",
    "scripts/projector.py": "# Weighted projection + edge calculation\n",
    "main.py": "# Main runner script\n"
}

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)

print("✅ All files and folders created successfully!")
