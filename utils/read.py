"""
read.py

Python utils for reading the datasets.
"""

import os
import json
import pandas as pd


# Determine the path to the datasets
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../datasets"))


def read_csv(path):
    return pd.read_csv(path, encoding="utf-8")


def dataset_dir(dataset):
    return os.path.abspath(os.path.join(DATA_DIR, dataset))


def all_datasets():
    return os.listdir(DATA_DIR)


def get_metadata(dataset):
    return json.load(open(os.path.join(dataset_dir(dataset), "METADATA.json")))


def get_X(dataset):
    return read_csv(os.path.join(dataset_dir(dataset), "X.csv"))


def get_y(dataset):
    return read_csv(os.path.join(dataset_dir(dataset), "y.csv")).iloc[:,0]
