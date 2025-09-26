# main.py
import pandas as pd
from scripts.scrape_players import get_players
from scripts.scrape_stats import get_player_stats
from scripts.scrape_team import get_team_stats
from scripts.scrape_news import get_injury_data
from scripts.fetch_odds import fetch_odds
from scripts.projections import calculate_projections
from scripts.process_data import process_data

def run():
    print("Fetching player list...")
    players = get_players()

    if players.empty:
        print("⚠️ Season has not started or no player data available yet. Exiting...")
        return

    print("Scraping player stats...")
    player_stats = get_player_stats(players)

    print("Scraping team advanced stats...")
    team_stats = get_team_stats()

    print("Scraping injury/news adjustments...")
    injury_data = get_injury_data()

    print("Fetching odds from sportsbook API...")
    odds_df = fetch_odds()

    print("Calculating projections...")
    projections = calculate_projections(player_stats, team_stats, injury_data)

    print("Processing data and calculating edges...")
    results = process_data(projections, odds_df)

    if results.empty:
        print("❌ No results after processing. Exiting...")
        return

    print("✅ Projections and edges calculated successfully!")
    print(results.head(10))

if __name__ == "__main__":
    run()
