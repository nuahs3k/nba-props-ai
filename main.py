from scripts.fetch_odds import fetch_odds
from scripts.scrape_players import get_all_players
from scripts.scrape_stats import get_player_stats
from scripts.scrape_team import get_team_stats
from scripts.scrape_news import get_injury_news
from scripts.process_data import merge_data
from scripts.projections import generate_projections
from scripts.projector import calculate_edges

def run():
    print("Fetching player list...")
    players = get_all_players()

    print("Scraping player stats...")
    player_stats = get_player_stats(players)

    print("Scraping team stats...")
    team_stats = get_team_stats()

    print("Scraping injury/news updates...")
    news_data = get_injury_news(players)

    print("Fetching odds...")
    odds_data = fetch_odds(api_key="d8475e9d02d7bdd135300c54d7b6c116")

    print("Merging data...")
    merged_data = merge_data(player_stats, team_stats, news_data, odds_data)

    print("Generating projections...")
    projections = generate_projections(merged_data)

    print("Calculating edges and top plays...")
    results = calculate_edges(projections)

    print("Top 25 Picks + Play of the Day:")
    print(results.head(25))
    results.to_csv("nba_top_plays.csv", index=False)
    print("Saved to nba_top_plays.csv")

if __name__ == "__main__":
    run()
