# An R example of how to work with these datasets.

library(rjson)  # you'll need to use install.package("rjson") if you don't have this

use_dataset <- function(md) {
    # Determine whether or not to use the dataset in your work

    n <- md$rows
    p <- md$cols
    y_type <- md$y_type
    X_type <- md$X_type
    X_missing <- md$X_missing

    # Example rules:
    #return(y_type == "binary" && n > 1000)
    #return(y_type == "numeric" && p < n)
    #return(y_type %in% c("binary", "categorical") && !X_missing)

    return(TRUE)
}

for(ds in list.files("datasets")) {
    md <- fromJSON(file=file.path("datasets", ds, "METADATA.json"))
    if (use_dataset(md)) {
        X <- read.csv(file.path("datasets", ds, "X.csv"))
        y <- read.csv(file.path("datasets", ds, "y.csv"))[,1]

        # Do some statistics or ML with X and y
    }
}
