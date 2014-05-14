# An R example of how to work with these datasets.

library(rjson)  # you'll need to use install.package("rjson") if you don't have this

for (ds in list.files("datasets")) {
    md <- fromJSON(file=file.path("datasets", ds, "METADATA.json"))
    n <- md$rows
    p <- md$cols
    y_type <- md$y_type
    X_types <- md$X_types
    X_missing <- md$X_missing

    # Determine whether to use the dataset. Example rules:
    #if (y_type == "binary" && n > 1000) {
    #if ((y_type == "numeric" && p < n) {
    #if ((y_type %in% c("binary", "categorical") && !X_missing) {
    if (TRUE) {
        X <- read.csv(file.path("datasets", ds, "X.csv"))
        y <- read.csv(file.path("datasets", ds, "y.csv"))[,1]

        # Do some stats or ML with X and y here
    }
}
