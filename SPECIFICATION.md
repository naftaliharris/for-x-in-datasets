# Data Format Specification

This document contains the specification for dataset formatting in this project.
It's still a work in progress, unfortunately... the "real spec" right now is
whatever is in the test script now, unfortunately.


## Categorizations of Datasets

Specifying a format for datasets requires describing the kinds of datasets that
we will specify formats for. There are three kinds of datasets we will consider:

1.  **Supervized datasets**: These are (x, y) pairs, where the goal is to
    predict y from x or more generally learn about the relationship between y
    and x.
2.  **Unsupervized datasets**: These are just a list of x's, where the goal is
    to cluster the x's, determine a density for them, or more generally learn
    about the x's.
3.  **Semisupervized datasets**: Like supervized datasets, these datasets
    consist of (x, y) pairs, where one attempts to predict y from x. Like
    unsupervized problems, however, semisupervized problems also contain
    unlabeled x's, with the idea that these unlabeled x's may help in the
    prediction.


## The Dataset Directory

Each dataset must be located in a single directory. The name of the dataset also
serves as the directory name. Dataset names should consist of capitalized words
separated by underscores rather than spaces, and more generally use no
characters that require escaping in a bash shell. Examples of valid dataset
names are: "Baseball\_Hitters", "Habermans\_Survival", and "Titanic".

Inside each dataset directory there must be a METADATA.json file, described
below. There may also be files X.csv, y.csv, X0.csv, 


## METADATA.json Specification

The METADATA.json file
    i) n
    ii) p
    iii) X type
    iv) y type
    v) missingness of X
    vi) inclusion of DESCRIPTION, rownames, unsupervized data...
    viii) possible compression used
    ix) possible data format used
    x) possible column type data...
    xi) perhaps short description, domain, etc


## Optional Files

There are several optional files that may be associated with a dataset:

* DESCRIPTION.txt: A textual description of the dataset, (in any format).
* rownames.csv: ...


## Definition of Data Types

3) Data types, (in decreasing order of "simplicity"):
    i) Numeric
    ii) Binary
    iii) Ordinal
    iv) Circular-ordinal
    v) Categorical
    vi) Text
    vii) Circular numeric???


## CSV Specification

* Numeric, integral, and binary values are represented with numeric strings,
  (scientific notation ok).
* Categorical variables with at least three levels are represented as "quoted
  strings".
* Missing data is represented by no text, not NA, NaN, ?, or anything else.
* UTF-8 format only.

## Open issues:

* Encoding sparse matrices
* Compressing large datasets
* Multiple response problems
* Canonical train/test splits
* Does each csv need a header?
* Including text fields
* Including ordinal or circular fields
* Row names: rownames.csv.
