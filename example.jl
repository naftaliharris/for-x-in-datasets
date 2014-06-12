# A Julia example of how to work with these datasets.

using DataFrames  # if you don't have this, install it with:
                  # julia> Pkg.add("DataFrames")

for ds in readdir("datasets")
    md_file = joinpath("datasets", ds, "METADATA.tsv")
    md = readtable(md_file)

    n, p = md[:n][1], md[:p][1]
    y_type = md[:y_type][1]
    X_numeric = md[:numeric_X][1]
    X_binary = md[:binary_X][1]
    X_categorical = md[:categorical_X][1]
    X_missing = md[:missing_X][1]

    # Determine whether to use the dataset. Example rules:
    #if y_type == "binary" && n > 1000
    #if y_type == "numeric" && p < n
    #if y_type in ["binary", "categorical"] && !X_missing
    if true
        data = readtable(joinpath("datasets", ds, "DATA.tsv"))
        X = data[2:end]
        y = data[1]

        # Do some stats or ML with X and y here
    end
end
