# Data Format Specification

This document contains the specification for dataset formatting in this project.
It's still a work in progress, unfortunately... the "real spec" right now is
whatever is in the test script now...


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

Each x is generally a vector with several or many components, called
"variables", some of which might be missing. Examples of variables would be
things like "height", "city", or "income". Each of the x's consists of the same
variables, and are commonly  Each y consists of just a single variable.

The variables that make up x are also known in different communities as 
"features", "covariates", or "independent variables".


## Variable Attributes

Now let's talk about what possible variables there are. At the most general
level, a variable is just a possible set of values. Different procedures treat
variables differently depending on the attributes of these sets. In this
section, we enumerate some of common attributes:

**Unordered**: These are

Linear, ordinal, circular, unordered.


## Variable Types

We must represent variables in our data somehow. We do this as follows:

* **Linear**: Must be represented as an unquoted number, in either decimal or
  scientific notation. (If the number is an integer, it needn't have a decimal
point). Large numbers should not include thousands-place commas. Examples of
valid representations of linear variables are '15', '-0.2', '1234' and
'3.1e-10', and '3.1E-10', (all without the single quotes). Examples of invalid
representations are '"15"', '1,234', and '3.1x10^-10', (again without the single
quotes).
* **Ordinal**: Must be represented as an unquoted integer, with the smallest
  value being '1' and each larger value increasing by one. Examples of valid
representations of ordinal variables are '1', '2', and '3'. Examples of invalid
representations are '"Bad"', '"Fair"', and '"Good"'.
* **Circular**: These are represented the same as ordinal variables.
* **Unordered**: These are represented as double-quoted strings. The strings
  should not themselves contain double quotes or newlines. Examples of valid
representations are '"Africa"', '"North America"', and '"Asia"'. Examples of
invalid representations are 'Africa', and '"Dwayne "The Rock" Johnson"'.

Specifying the dataset format also requires describing the types of variables
that may be present.

3) Data types, (in decreasing order of "simplicity"):
    i) Numeric
    ii) Binary
    iii) Ordinal
    iv) Circular-ordinal
    v) Categorical
    vi) Text
    vii) Circular numeric???


## Dataset Names and Directories

Each dataset must be located in a single directory. The name of the dataset also
serves as the directory name. Dataset names should consist of capitalized words
separated by underscores rather than spaces, use just ASCII letters and digits.
Examples of valid dataset names are: "Baseball\_Hitters", "Habermans\_Survival",
and "Titanic".

Inside each dataset directory there must be a METADATA.json file, described
below.


## METADATA.json Specification

The METADATA.json file contains information about the particular dataset. Just
by reading it, one should be able to decide whether the dataset would be useful
to work with. The file is a single JSON object, with the following key value
pairs:

* "y\_type": the data type for the y vector
* "X\_type": the hardest data type for the x vector  (NOTE: should be an array)
* "X\_missing": a boolean value indicating whether any X has any missing values
* "rows": the number of rows (observations) in X
* "cols": the number of columns (variables) in X and y.

    vi) inclusion of DESCRIPTION, rownames, unsupervized data...
    viii) possible compression used
    ix) possible data format used
    x) possible column type data...
    xi) perhaps short description, domain, etc


## Optional Files

There are several optional files that may be associated with a dataset:

* DESCRIPTION.txt: A textual description of the dataset, (in any format).
* rownames.csv: ...


## CSV Specification

* UTF-8 format only.
* Missing data is represented by no text, not NA, NaN, ?, or anything else.
* Each CSV must have a header containing the names of each of the columns. If
  the columns don't have fundamental names, name them "V1", "V2", "V3"...


## Open issues:

* Encoding sparse matrices
* Compressing large datasets... compress all datasets?
* Dealing with multiple response problems
* Canonical train/test splits: solve with splits\_X.csv? Kind of a pain.
* Including text fields
* Including ordinal or circular fields
