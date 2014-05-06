"""A python example of how to work with these datasets."""

from utils.read import all_datasets, get_metadata, get_X, get_y


def main():
    for ds in all_datasets():
        md = get_metadata(ds)
        n, p = md["rows"], md["cols"]
        y_type, X_type, X_missing = md["y_type"], md["X_type"], md["X_missing"]

        # Determine whether to use the dataset. Example rules:
        #if y_type == "binary" and n > 1000:
        #if y_type == "numeric" and p < n:
        #if y_type in ["binary", "categorical"] and not X_missing:
        if True:
            X = get_X(ds)
            y = get_y(ds)

            # Do some stats or ML with X and y here:
            pass

if __name__ == "__main__":
    main()
