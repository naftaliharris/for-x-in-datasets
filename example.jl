# A Julia example of how to work with these datasets.

using JSON        # if you don't have this, install it with julia> Pkg.add("JSON")
using DataFrames  # if you don't have this, install it with julia> Pkg.add("DataFrames")

for ds in readdir("datasets")
    md_file = joinpath("datasets", ds, "METADATA.json")
    md = JSON.parse(readall(md_file))

    n, p = md["X"]["rows"], md["X"]["cols"]
    y_type, X_types = md["y"]["type"], md["X"]["types"]
    X_missing = md["X"]["missing"]

    # Determine whether to use the dataset. Example rules:
    #if y_type == "binary" && n > 1000
    #if y_type == "numeric" && p < n
    #if y_type in ["binary", "categorical"] && !X_missing
    if true
        X = readtable(joinpath("datasets", ds, "X.csv"))
        y = readtable(joinpath("datasets", ds, "y.csv"))

        # Do some stats or ML with X and y here
    end
end
