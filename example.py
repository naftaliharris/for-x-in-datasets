"""A python example of how to work with these datasets."""

from utils.read import all_datasets, get_metadata, get_X, get_y


def use_dataset(md):
    """Determine whether to use the dataset in your work"""

    n = md["rows"]
    p = md["cols"]
    y_type = md["y_type"]
    X_type = md["X_type"]
    X_missing = md["X_missing"]

    # Example rules:
    #return y_type == "binary" and n > 1000
    #return y_type == "numeric" and p < n
    #return y_type in ["binary", "categorical"] and not X_missing

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
