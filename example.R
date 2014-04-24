# An R example of how to work with these datasets.

library(rjson)  # you'll need to use install.package("rjson") if you don't have this

use_dataset <- function(md) {
    # Determine whether or not to use the dataset in your work

    n <- md$instances
    p <- md$variables
    response <- md$response
    missing <- md$missing

    # Example rules:
    #return(response == "binary" && n > 1000)
    #return(response == "numeric" && p < n)
    #return(response %in% c("binary", "categorical") && !missing)

    return(TRUE)
}

for(ds in list.files("datasets")) {
    md <- fromJSON(file=file.path("datasets", ds, "METADATA.json"))
    if (use_dataset(md)) {
        X <- read.csv(file.path("datasets", ds, "X.csv"))
        y <- read.csv(file.path("datasets", ds, "y.csv"))

        # Do some statistics or ML with X and y
    }
}
