# An R example of how to work with these datasets.

for (ds in list.files("datasets")) {
    md <- read.delim(file.path("datasets", ds, "METADATA.tsv"))
    n <- md$n[0]
    p <- md$p[0]
    y_type <- md$y_type[0]
    X_numeric = md$numeric_X[0]
    X_binary = md$binary_X[0]
    X_categorical = md$categorical_X[0]
    X_missing <- md$missing_X[0]

    # Determine whether to use the dataset. Example rules:
    #if (y_type == "binary" && n > 1000) {
    #if ((y_type == "numeric" && p < n) {
    #if ((y_type %in% c("binary", "categorical") && !X_missing) {
    if (TRUE) {
        data <- read.delim(file.path("datasets", ds, "DATA.tsv"))
        X <- data[,-1]
        y <- data[,1]

        # Do some stats or ML with X and y here
    }
}
