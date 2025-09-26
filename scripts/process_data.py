import pandas as pd

def merge_data(player_stats, team_stats, news_data, odds_data):
    merged = player_stats.merge(team_stats, how="left", left_on="Tm", right_on="team")
    merged = merged.merge(news_data, how="left", on="player")
    merged = merged.merge(odds_data, how="left", on="player")
    return merged
