"""A python example of how to work with these datasets."""

import os
import json
import pandas as pd  # if necessary, install this with $ easy_install pandas


for ds in os.listdir("datasets"):
    md = json.load(open(os.path.join("datasets", ds, "METADATA.json")))
    n, p = md["rows"], md["cols"]
    y_type, X_type, X_missing = md["y_type"], md["X_type"], md["X_missing"]

    # Determine whether to use the dataset. Example rules:
    #if y_type == "binary" and n > 1000:
    #if y_type == "numeric" and p < n:
    #if y_type in ["binary", "categorical"] and not X_missing:
    if True:
        X = pd.read_csv(os.path.join("datasets", ds, "X.csv"))
        y = pd.read_csv(os.path.join("datasets", ds, "y.csv")).iloc[:, 0]

        # Do some stats or ML with X and y here:
        pass
