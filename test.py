"""
1) Test all of the datasets for adhering to the spec.
2) Make sure the examples run.
"""

import sys
import re
import os
import json
import subprocess
import pandas as pd

dataset_pattern = r"^[A-Z0-9][a-zA-Z0-9]+(_[A-Z0-9][a-zA-Z0-9]+)*$"
required_files = ["METADATA.json", "X.csv", "y.csv", "DESCRIPTION.txt"]
optional_files = ["X0.csv", "X_rownames.csv", "X0_rownames.csv"]


def read_csv(path):
    return pd.read_csv(path, encoding="utf-8")


def dataset_dir(dataset):
    return os.path.abspath(os.path.join("datasets", dataset))


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

    # Check the columns of X for correctness of X_types
    X = read_csv(os.path.join(directory, "X.csv"))

    if len(set(metadata["X"]["types"])) != len(metadata["X"]["types"]):
        raise ValueError("METADATA X_types (%s) contains duplicates" %
                         metadata["X"]["types"])

    X_types = set()
    for column in X.columns:
        X_types.add(datatype(X[column]))
    if X_types != set(metadata["X"]["types"]):
        raise ValueError("METADATA X_types %s doesn't agree with empirical "
                         "X_types %s" % (set(metadata["X"]["types"]), X_types))

    # No lying about the dimensions of X
    metadata_shape = (metadata["X"]["rows"], metadata["X"]["cols"])
    if X.shape != metadata_shape:
        raise ValueError("Dimensions of X.csv %s don't agree with the "
                         "dimensions in METADATA.json %s"
                         % (str(X.shape), str(metadata_shape)))

    # No lying about missingness in X
    missing = pd.isnull(X).any().any()
    if missing != metadata["X"]["missing"]:
        raise ValueError("Empirical missingness of X.csv (%s) doesn't agree "
                         "with the value in METADATA.json (%s)"
                         % (missing, metadata["X"]["missing"]))

    # Check y for the proper shape
    Y = read_csv(os.path.join(directory, "y.csv"))
    if Y.shape[1] != 1:
        raise ValueError("y.csv must be a single column")
    if Y.shape[0] != metadata["y"]["rows"]:
        raise ValueError("y.csv has %d rows, "
                         "but METADATA.json claims %d rows"
                         % (Y.shape[0], metadata["y"]["rows"]))
    y = Y.iloc[:, 0]

    # Check y for validity
    dt = datatype(y)
    if dt == "categorical" and len(y.value_counts()) < 3:
        raise ValueError("y is categorical but has less than three values")
    if pd.isnull(y).any():
        raise ValueError("No missing data allowed in y.csv")
    if datatype(y) != metadata["y"]["type"]:
        raise ValueError("METADATA.json response type (\"%s\") "
                         "isn't the observed response type (\"%s\") in y.csv"
                         % (metadata["y"]["type"], datatype(y)))


def test_datasets():
    sys.stdout.write("Testing datasets")
    sys.stdout.flush()
    for ds in os.listdir("datasets"):
        try:
            validate_dataset(ds)
        except Exception as e:
            print "\nDataset \"%s\":" % ds
            raise
        else:
            sys.stdout.write(".")
            sys.stdout.flush()
    print ""


def test_examples():
    # Python
    print "Testing Python example..."
    if subprocess.call(["python", "example.py"]) != 0:
        raise RuntimeError("Python script failed!")

    # R
    print "Testing R example..."
    if subprocess.call(["R", "--slave"], stdin=open("example.R")) != 0:
        raise RuntimeError("R script failed!")

    # Julia
    print "Testing Julia example..."
    if subprocess.call(["julia", "example.jl"]) != 0:
        raise RuntimeError("Julia script failed!")


def main():
    test_datasets()
    test_examples()
    print "Success!"


if __name__ == "__main__":
    main()
