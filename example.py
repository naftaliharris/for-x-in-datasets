"""A python example of how to work with these datasets."""

import os
import pandas as pd  # if necessary, install this with $ easy_install pandas


for ds in os.listdir("datasets"):
    md = pd.read_csv(os.path.join("datasets", ds, "METADATA.tsv"), sep="\t")
    n, p = md["n"][0], md["p"][0]
    y_type = md["y type"][0]
    X_numeric = md["numeric X?"][0]
    X_binary = md["binary X?"][0]
    X_categorical = md["categorical X?"][0]
    X_missing = md["Missing?"][0]

    # Determine whether to use the dataset. Example rules:
    #if y_type == "binary" and n > 1000:
    #if y_type == "numeric" and p < n:
    #if y_type in ["binary", "categorical"] and not X_missing:
    if True:
        X = pd.read_csv(os.path.join("datasets", ds, "DATA.tsv"), sep="\t")
        y = X[X.columns[0]]  # y in the first column
        del X[X.columns[0]]

        # Do some stats or ML with X and y here:
        pass
