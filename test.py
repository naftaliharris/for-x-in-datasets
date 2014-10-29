"""
1) Test all of the datasets for adhering to the spec.
2) Make sure the examples run.
"""

import sys
import re
import os
import subprocess
import pandas as pd

dataset_pattern = r"^[A-Z0-9][a-zA-Z0-9]+(_[A-Z0-9][a-zA-Z0-9]+)*$"
required_files = ["DATA.tsv", "DESCRIPTION.txt"]
optional_files = []

METADATA_COLS = ["name", "n", "p", "numeric_X", "binary_X", "categorical_X",
                 "y_type", "missing_X"]


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


def validate_dataset(name, metadata):
    """Checks a dataset for validity"""

    # Check the name
    if not re.match(dataset_pattern, name):
        raise ValueError("Invalid dataset name")

    directory = dataset_dir(name)

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

    # Read X and y
    data = pd.read_csv(os.path.join(directory, "DATA.tsv"), sep="\t", encoding="utf-8")
    y = data[data.columns[0]]
    X = data
    del X[X.columns[0]]

    # No lying about the dimensions of X
    metadata_shape = (metadata["n"], metadata["p"])
    if X.shape != metadata_shape:
        raise ValueError("Dimensions of X.csv %s don't agree with the "
                         "dimensions in METADATA.tsv %s"
                         % (str(X.shape), str(metadata_shape)))

    # Check the columns of X for correctness of X_types
    X_types = set()
    for column in X.columns:
        X_types.add(datatype(X[column]))
    metadata_types = set()
    for data_type in ["numeric", "binary", "categorical"]:
        if metadata["%s_X" % data_type]:
            metadata_types.add(data_type)
    if X_types != metadata_types:
        raise ValueError("METADATA data types %s don't agree with empirical "
                         "data types %s" % (metadata_types, X_types))

    # No lying about missingness in X
    missing = pd.isnull(X).any().any()
    if missing != metadata["missing_X"]:
        raise ValueError("Empirical missingness of X.csv (%s) doesn't agree "
                         "with the value in METADATA.tsv (%s)"
                         % (missing, metadata["missing_X"]))

    # Check y for validity
    dt = datatype(y)
    if dt == "categorical" and len(y.value_counts()) < 3:
        raise ValueError("y is categorical but has less than three values")
    if pd.isnull(y).any():
        raise ValueError("No missing values allowed in y")
    if datatype(y) != metadata["y_type"]:
        raise ValueError("METADATA.tsv response type (\"%s\") "
                         "isn't the observed response type (\"%s\") in y"
                         % (metadata["y_type"], datatype(y)))


def test_datasets():
    sys.stdout.write("Testing datasets")
    sys.stdout.flush()
    datasets = pd.read_csv("METADATA.tsv", index_col="name", sep="\t")
    for name, metadata in datasets.iterrows():
        try:
            validate_dataset(name, metadata)
        except Exception as e:
            print "\nDataset \"%s\":" % ds
            raise
        else:
            sys.stdout.write(".")
            sys.stdout.flush()
    print ""


def test_example(proglang, script, tester):
    sys.stdout.write("Testing %s example... " % proglang)
    sys.stdout.flush()
    try:
        res = tester()
    except OSError:
        print "no %s on this machine; didn't test %s" % (proglang, script)
    else:
        print "success!" if res == 0 else "failure!"


def test_examples():
    py_test = lambda: subprocess.call(["python", "example.py"])
    test_example("Python", "example.py", py_test)

    R_test = lambda: subprocess.call(["R", "--slave"], stdin=open("example.R"))
    test_example("R", "example.R", R_test)

    jl_test = lambda: subprocess.call(["julia", "example.jl"])
    test_example("Julia", "example.jl", jl_test)

    m_test = lambda: subprocess.call(["matlab"])
    test_example("Matlab", "example.m", m_test)


def main():
    test_datasets()
    test_examples()
    print "Done!"


if __name__ == "__main__":
    main()
