"""A python example of how to work with these datasets."""

from utils.read import all_datasets, get_metadata, get_X, get_y


def use_dataset(md):
    """Determine whether to use the dataset in your work"""

    n = md["instances"]
    p = md["variables"]
    response = md["response"]
    missing = md["missing"]

    # Example rules:
    #return response == "binary" and n > 1000
    #return response == "numeric" and p < n
    #return response in ["binary", "categorical"] and not missing

    return True


def main():
    for ds in all_datasets():
        md = get_metadata(ds)
        if use_dataset(md):
            X = get_X(ds)
            y = get_y(ds)

            # Do some statistics or ML with X and y


if __name__ == "__main__":
    main()
