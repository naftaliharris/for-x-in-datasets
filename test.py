"""
Test all of the datasets for adhering to the spec.
"""

import sys
import os
from utils.validate import validate_dataset


def main():
    for directory in os.listdir("datasets/"):
        try:
            validate_dataset("datasets/%s/" % directory)
        except Exception as e:
            print "\nDirectory \"%s\":" % directory
            print e.message
        else:
            sys.stdout.write(".")
    print ""

if __name__ == "__main__":
    main()
