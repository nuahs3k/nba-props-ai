import pandas as pd
import numpy as np

def generate_projections(merged):
    merged["projection"] = merged["PTS"].astype(float) * 0.4 + \
                           merged["AST"].astype(float) * 0.3 + \
                           merged["TRB"].astype(float) * 0.3
    return merged
