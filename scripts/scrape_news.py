from newspaper import Article
import pandas as pd

def get_injury_news(players):
    news_list = []
    for player in players[:20]:  # limit first 20 for demo
        try:
            url = f"https://www.espn.com/nba/player/_/id/{player['id']}"
            article = Article(url)
            article.download()
            article.parse()
            news_list.append({"player": player['name'], "news": article.text})
        except:
            continue
    return pd.DataFrame(news_list)
