import requests
import pandas as pd

def fetch_odds(api_key):
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey={api_key}&regions=us&markets=totals"
    response = requests.get(url)
    data = response.json()

    games = []
    for game in data:
        try:
            game_name = f"{game['home_team']} vs {game['away_team']}"
            for bookmaker in game['bookmakers']:
                for market in bookmaker['markets']:
                    for outcome in market['outcomes']:
                        games.append({
                            "game": game_name,
                            "player": outcome.get("name"),
                            "line": outcome.get("point"),
                            "type": market.get("key"),
                            "bookmaker": bookmaker.get("title")
                        })
        except Exception as e:
            continue
    return pd.DataFrame(games)
