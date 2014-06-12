# Data Format Specification

This document contains the specification for dataset formatting in this project.
The primary underlying goal for this specification is simplicity. I want this
specification to be easy to understand, and the resulting datasets to be easy to
work with and easy to format to this specification.


## The dataset directory

Each dataset consists of three files in a directory: The dataset itself, called
**DATA.tsv**, some short metadata about the dataset, called **METADATA.tsv**,
and a textual description of the dataset and perhaps the variables in it, called
**DESCRIPTION.txt**.

The name of the dataset also serves as the directory name. Dataset names should
consist of capitalized words separated by underscores rather than spaces, using
just ASCII letters and digits.  Examples of valid dataset names are:
"Baseball\_Hitters", "Habermans\_Survival", and "Titanic".


## DATA.tsv

**DATA.tsv** contains the dataset's actual data, in a tabular format described
in the later **TSV Format** section. The first column of **DATA.tsv** is the
response variable, (sometimes known as "y" or the dependent variable). The
remaining columns of **DATA.tsv** are the feature variables, (sometimes known as
"X", independent variables, covariates, or the design matrix). In each dataset,
the goal is to predict or understand the response variable using the feature
variables.

There are two differences between the way we treat the response variable and the
feature variables. Firstly, the response variable is not allowed to have missing
data, while the feature variables are allowed to. Secondly, if the response
variable is binary, it must use 0/1 formatting rather than "categorical string"
encoding, (both described in the **TSV Format** section). It is preferred, but
not required, that binary feature variables use 0/1 formatting.


## METADATA.tsv

**METADATA.tsv** is a very short file describing the dataset's data. In fact, it
is a tabular tsv file, (described in **TSV Format**), with just a header and a
single row. The columns of this file are:

1.  "name": The name of the dataset, (equivalently the directory name).
2.  "n": An integral value indicating the number of observations (rows excluding
    the header) in the dataset.
3.  "p": An integral value indicating the number of feature variables,
    (equivalently the number of columns of the design matrix, or the number
columns in DATA.tsv minus one).
4.  "numeric\_X": A binary value indicating whether at least one of the feature
    variables is "strictly numeric", ie, numeric but not binary.
5.  "binary\_X": A binary value indicating whether at least one of the feature
    variables is binary.
6.  "categorical\_X": A binary value indicating whether at least one of the
    feature variables is categorical.
7.  "y\_type": A categorical variable indicating the type of the response
    variable, one of "numeric", "binary", or "categorical".
8.  "missing\_X": A binary variable indicating whether the feature variables
    contain any missing values.


## What kinds of datasets are we considering?

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


## METADATA.json Specification

The METADATA.json file contains information about the particular dataset. Just
by reading it, one should be able to decide whether the dataset would be useful
to work with. The file is a single JSON object, with the following key value
pairs:

* "y\_type": the data type for the y vector
* "X\_types": an array of the unique types that variables in X have
* "X\_missing": a boolean value indicating whether any X has any missing values
* "rows": the number of rows (observations) in X
* "cols": the number of columns (variables) in X and y.

    vi) inclusion of DESCRIPTION, rownames, unsupervized data...
    viii) possible compression used
    ix) possible data format used
    x) possible column type data...
    xi) perhaps short description, domain, etc


## TSV Specification

* ASCII encoding only.
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
