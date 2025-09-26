import pandas as pd

def calculate_edges(projections):
    projections["edge"] = projections["projection"] - projections["line"].astype(float)
    projections = projections.sort_values("edge", key=abs, ascending=False)
    return projections
