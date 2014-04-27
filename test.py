"""
1) Test all of the datasets for adhering to the spec.
2) Make sure the examples run.
"""

import sys
import os
import subprocess
from utils.validate import validate_dataset
from utils.read import all_datasets


def test_datasets():
    sys.stdout.write("Testing datasets")
    sys.stdout.flush()
    for ds in all_datasets():
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
    print "Testing python example..."
    import example
    example.main()

    # R
    print "Testing R example..."
    if subprocess.call(["R", "--slave"], stdin=open("example.R")) != 0:
        raise RuntimeError("R script failed!")


def main():
    test_datasets()
    test_examples()
    print "Success!"


if __name__ == "__main__":
    main()
