"""
1) Test all of the datasets for adhering to the spec.
2) Make sure the examples run.
"""

import sys
import os
import subprocess
from utils.validate import validate_dataset


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
