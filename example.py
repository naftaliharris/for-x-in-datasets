"""A python example of how to work with these datasets."""

import os
import pandas as pd  # if necessary, install this with $ pip install pandas

datasets = pd.read_csv("METADATA.tsv", index_col="name", sep="\t")

for name, metadata in datasets.iterrows():
    n, p = metadata["n"], metadata["p"]
    y_type = metadata["y_type"]
    numeric_X = metadata["numeric_X"]
    binary_X = metadata["binary_X"]
    categorical_X = metadata["categorical_X"]
    missing_X = metadata["missing_X"]

    # Determine whether to use the dataset. Example rules:
    #if y_type == "binary" and n > 1000:
    #if y_type == "numeric" and p < n:
    #if y_type in ["binary", "categorical"] and not missing_X:
    if True:
        X = pd.read_csv(os.path.join("datasets", name, "DATA.tsv"), sep="\t")
        y = X[X.columns[0]]
        del X[X.columns[0]]

        # Do some stats or ML with X and y here:
        pass
