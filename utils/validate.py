"""
Tests...
"""

import sys
import os
import json
import pandas as pd


required_files = ["METADATA.json", "X.csv", "y.csv"]
optional_files = ["X0.csv", "DESCRIPTION.txt"]


def datatype(x):
    """Determines the sort of data that x is"""
    if x.dtype == object:
        return "categorical"
    elif set(x.value_counts().index) == set([0, 1]):
        return "binary"
    else:
        return "numeric"


def validate_column(x):
    """Checks a pandas series for validity"""
    
    # Categorical variables must have at least three levels
    if datatype(x) == "categorical" and len(x.value_counts()) < 3:
        raise ValueError("Categorical variables need at least three levels")


def validate_dataset(directory):
    """Checks a dataset for validity"""

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

    # METADATA.json must have required elements
    metadata = json.load(open(directory + "METADATA.json"))
    pass

    # Check the columns of X for adherence to the spec
    X = pd.read_csv(directory + "X.csv", encoding="utf-8")
    for column in X.columns:
        try:
            validate_column(X[column])
        except Exception as e:
            raise type(e),\
                  type(e)("Column \"%s\": " % column + e.message),\
                  sys.exc_info()[2]

    # No lying about the dimensions of X
    metadata_shape = (metadata["instances"], metadata["variables"])
    if X.shape != metadata_shape:
        raise ValueError("Dimensions of X.csv %s don't agree with the "
                         "dimensions in METADATA.json %s"
                         % (str(X.shape), str(metadata_shape)))

    # No lying about missingness in X
    missing = pd.isnull(X).any().any()
    if missing != metadata["missing"]:
        raise ValueError("Empirical missingness of X.csv (%s) doesn't agree "
                         "with the value in METADATA.json (%s)"
                         % (missing, metadata["missing"]))

    # Check y for the proper shape
    Y = pd.read_csv(directory + "y.csv", encoding="utf-8")
    if Y.shape[1] != 1:
        raise ValueError("y.csv must be a single column")
    if Y.shape[0] != metadata_shape[0]:
        raise ValueError("y.csv has %d instances, "
                         "but METADATA.json claims %d instances"
                         % (Y.shape[0], metadata_shape[0]))
    y = Y.iloc[:,0]

    # Check y for validity
    validate_column(y)
    if pd.isnull(y).any():
        raise ValueError("No missing data allowed in y.csv")
    if datatype(y) != metadata["response"]:
        raise ValueError("METADATA.json response type (\"%s\") "
                         "isn't the observed response type (\"%s\") in y.csv"
                         % (metadata["response"], datatype(y)))
