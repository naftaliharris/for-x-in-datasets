"""
Tests...
"""

import sys
import re
import os
import json
import pandas as pd
from read import dataset_dir, read_csv

dataset_pattern = r"^[A-Z0-9][a-zA-Z0-9]+(_[A-Z0-9][a-zA-Z0-9]+)*$"
required_files = ["METADATA.json", "X.csv", "y.csv"]
optional_files = ["X0.csv", "X_rownames.csv", "X0_rownames.csv",
                  "DESCRIPTION.txt"]

complexity = {
    "numeric": 0,
    "binary": 1,
    "categorical": 2,
    "text": 3
}


def datatype(x):
    """Guesses the sort of data that x is"""
    if x.dtype == object:
        return "categorical"
    for y in x:
        if y != 0 and y != 1:
            return "numeric"  # return fast for numeric data
    return "binary"


def validate_dataset(dataset):
    """Checks a dataset for validity"""

    # Check the name
    if not re.match(dataset_pattern, dataset):
        raise ValueError("Invalid dataset name")

    directory = dataset_dir(dataset)

    # Only certain files are allowed
    allowed_files = required_files + optional_files
    file_names = os.listdir(directory)
    for file_name in file_names:
        if file_name not in allowed_files:
            raise ValueError("\"%s\" is not an allowed file name" % file_name)

    # Some files are required
    for required_file in required_files:
        if required_file not in file_names:
            raise ValueError("Missing required file \"%s\"" % required_file)

    # METADATA.json must have certain required elements
    metadata = json.load(open(os.path.join(directory, "METADATA.json")))
    pass

    # Check the columns of X for correctness of X_type
    X = read_csv(os.path.join(directory, "X.csv"))
    X_type = "numeric"
    for column in X.columns:
        dt = datatype(X[column])
        if complexity[dt] > complexity[X_type]:
            X_type = dt
    if complexity[X_type] > complexity[metadata["X_type"]]:
        raise ValueError("METADATA X_type (%s) doesn't agree with empirical "
                         "X_type (%s)" % (metadata["X_type"], X_type))

    # No lying about the dimensions of X
    metadata_shape = (metadata["rows"], metadata["cols"])
    if X.shape != metadata_shape:
        raise ValueError("Dimensions of X.csv %s don't agree with the "
                         "dimensions in METADATA.json %s"
                         % (str(X.shape), str(metadata_shape)))

    # No lying about missingness in X
    missing = pd.isnull(X).any().any()
    if missing != metadata["X_missing"]:
        raise ValueError("Empirical missingness of X.csv (%s) doesn't agree "
                         "with the value in METADATA.json (%s)"
                         % (missing, metadata["missing"]))

    # Check y for the proper shape
    Y = read_csv(os.path.join(directory, "y.csv"))
    if Y.shape[1] != 1:
        raise ValueError("y.csv must be a single column")
    if Y.shape[0] != metadata_shape[0]:
        raise ValueError("y.csv has %d rows, "
                         "but METADATA.json claims %d rows"
                         % (Y.shape[0], metadata_shape[0]))
    y = Y.iloc[:, 0]

    # Check y for validity
    dt = datatype(y)
    if dt == "categorical" and len(y.value_counts()) < 3:
        raise ValueError("y is categorical but has less than three values")
    if pd.isnull(y).any():
        raise ValueError("No missing data allowed in y.csv")
    if datatype(y) != metadata["y_type"]:
        raise ValueError("METADATA.json response type (\"%s\") "
                         "isn't the observed response type (\"%s\") in y.csv"
                         % (metadata["y_type"], datatype(y)))
