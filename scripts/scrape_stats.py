import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_player_stats(players, season="2025"):
    all_stats = []
    for player in players:
        pid = player['id']
        url = f"https://www.basketball-reference.com/players/{pid[0]}/{pid}/gamelog/{season}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table", {"id":"pgl_basic"})
        if table:
            df = pd.read_html(str(table))[0]
            df = df[df["Rk"] != "Rk"].dropna(subset=["PTS", "AST", "TRB"])
            df["player"] = player['name']
            all_stats.append(df)
    return pd.concat(all_stats, ignore_index=True)
