import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_team_stats(season="2025"):
    teams = ["LAL", "BOS", "GSW", "MIA"]  # expand for all NBA teams
    all_stats = []
    for team in teams:
        url = f"https://www.basketball-reference.com/teams/{team}/{season}.html"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table", {"id":"advanced"})
        if table:
            df = pd.read_html(str(table))[0]
            df["team"] = team
            all_stats.append(df)
    return pd.concat(all_stats, ignore_index=True)
