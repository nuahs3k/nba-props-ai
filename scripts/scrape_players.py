import requests
from bs4 import BeautifulSoup

# scrape_players.py
import pandas as pd

def get_players():
    # Replace this with your actual scraping logic
    # For now, we can return an empty DataFrame as a placeholder
    # The main.py will catch this and print the "season not started" message
    return pd.DataFrame(columns=["Player", "Team", "Position"])

def get_all_players():
    url = "https://www.basketball-reference.com/players/"
    players = []

    for letter in "abcdefghijklmnopqrstuvwxyz":
        page = requests.get(f"{url}{letter}/")
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find("table")
        if table:
            rows = table.find_all("tr")
            for row in rows:
                link = row.find("a")
                if link:
                    players.append({
                        "name": link.text,
                        "id": link['href'].split("/")[-1].replace(".html","")
                    })
    return players
