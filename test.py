"""
1) Test all of the datasets for adhering to the spec.
2) Make sure the examples run.
"""

import sys
import os
from utils.validate import validate_dataset
from utils.read import all_datasets


def test_datasets():
    for ds in all_datasets():
        try:
            validate_dataset(ds)
        except Exception as e:
            print "\nDataset \"%s\":" % ds
            print e.message
        else:
            sys.stdout.write(".")
    print ""


def test_examples():
    # Python
    import example
    example.main()

    # R
    pass


def main():
    test_datasets()
    test_examples()


if __name__ == "__main__":
    main()
