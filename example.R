# An R example of how to work with these datasets.

datasets <- read.delim("METADATA.tsv")

for (i in 1:nrow(datasets)) {
    name <- datasets$name[i]
    n <- datasets$n[i]
    p <- datasets$p[i]
    y_type <- datasets$y_type[i]
    numeric_X = datasets$numeric_X[i]
    binary_X = datasets$binary_X[i]
    categorical_X = datasets$categorical_X[i]
    missing_X <- datasets$missing_X[i]

    # Determine whether to use the dataset. Example rules:
    #if (y_type == "binary" && n > 1000) {
    #if ((y_type == "numeric" && p < n) {
    #if ((y_type %in% c("binary", "categorical") && !missing_X) {
    if (TRUE) {
        data <- read.delim(file.path("datasets", name, "DATA.tsv"))
        X <- data[,-1]
        y <- data[,1]

        # Do some stats or ML with X and y here
    }
}
