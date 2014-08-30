# Dataset Formatting Specification

This document contains the specification for dataset formatting in this project.
The underlying goal for this specification is simplicity:

1. This specification to be easy to understand.
2. It to be easy to format datasets to obey this specification.
3. Datasets formatted according to this specification should be easy to work with.


## The dataset directory

Each dataset consists of three files in a directory: The data itself, called
**DATA.tsv**, some short metadata about the dataset, called **METADATA.tsv**,
and a textual description of the dataset, called **DESCRIPTION.txt**.

The name of the dataset also serves as the directory name. Dataset names should
consist of capitalized words separated by underscores rather than spaces, using
just ASCII letters and digits.  Examples of valid dataset names are:
"Baseball\_Hitters", "Habermans\_Survival", and "Titanic". The reason for these
limitations on naming is that spaces and unusual characters in file names
often pose difficulties for scripts.


## DATA.tsv

DATA.tsv contains the dataset's actual data, in a tabular format described
in the later **TSV Format** section. The first column of DATA.tsv is the
response variable, (sometimes known as "y" or the dependent variable). The
remaining columns of DATA.tsv are the feature variables, (sometimes known as
"X", independent variables, covariates, or the design matrix). In each dataset,
the goal is to predict or understand the response variable using the feature
variables.

There are two differences between the way we treat the response variable and the
feature variables. Firstly, the response variable is not allowed to have missing
data, while the feature variables are allowed to. Secondly, if the response
variable is binary, it must use 0/1 formatting rather than "categorical string"
encoding, (both described in the **TSV Format** section). It is preferred, but
not required, that binary feature variables use 0/1 formatting.

Sometimes the rows of a dataset have names. For example, each observation (row)
might refer to a particular chemical, and the rowname might be the name of this
chemical. Do not include rownames in DATA.tsv, as they should not be used in
building models and consequently complicate doing so. Similarly, do not include
a column of train/test split ids. The general rule is that DATA.tsv should
contain only the response variable and the feature variables, nothing more.


## METADATA.tsv

METADATA.tsv is a very short file describing the dataset's data. In fact, it
is a tabular tsv file, (described in **TSV Format**), with just a header and a
single row. The columns of this file are:

1.  "name": The name of the dataset, (equivalently the directory name).
2.  "n": An integral value indicating the number of observations (rows excluding
    the header) in the dataset.
3.  "p": An integral value indicating the number of feature variables,
    (equivalently the number of columns of the design matrix, or the number of
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


## DESCRIPTION.txt

DESCRIPTION.txt is an ASCII text description of the dataset, often copied from
the original source of the data. The general idea is that you should be able to
get some extra information about the dataset if you need to by reading this
file. Unlike DATA.tsv and METADATA.tsv, however, there are no requirements about
what to put in here, however.


## TSV Specification

DATA.tsv and METADATA.tsv are both ASCII-encoded TSV files. A TSV file
represents a table, with a certain number of rows and columns. Each of the rows
of this table is a line in the TSV file, with the fields of that row separated
by the tab character.

The representation of the elements of the TSV file depends on their "types":
There are three types of variables we'll consider: numeric variables, binary
variables, and categorical variables.

Numeric variables are numbers, and should be represented in the usual way, in
integer, decimal, or scientic notation. Don't quote numeric variables, or use
thousands-place commas. Examples of valid representations of numeric variables
are '15', '-0.2', '1234', '3.1e-10', and '3.1E-10', (all without the single
quotes). Examples of invalid representations are '"15"', '1,234', and
'3.1x10^-10', (again without the single quotes).

Binary variables are those that have only two values. Preferably they should be
represented as either '0' or '1', (without the single quotes). This is a
requirement if the response variable is binary. However, binary feature
variables may be represented as double-quoted strings, for example, '"pitcher"'
and '"nonpitcher"', (no single quotes).

Categorical variables are represented as double-quoted strings. The strings
should not themselves contain single or double quotes, tabs, or newlines.
Examples of valid representations of categorical variables are '"Africa"',
'"North America"', and '"Asia"'. Examples of invalid representations are
'Africa', and '"Dwayne "The Rock" Johnson"'. Don't include categorical variables
with more than a few dozen levels. In particular, don't include any free-form
text that you would need to further featurize.

All of the fields of a column (variable) should be of the same type. The one
exception to this is that fields in feature variables can be missing. Missing
entries should be represented by an empty field '', not 'NA', 'NaN', '?', '""',
or anything else.

Each TSV must have a header containing the names of each of the columns. If the
columns don't have names, name them "V1", "V2", "V3", like R does.

For example, a DATA.tsv file representing an email spam dataset might look like
this:

```
"Is Spam"<TAB>Score<TAB>"Email Provider"<TAB>"Has Dollar Sign"
1<TAB>23.4<TAB>"gmail"<TAB>1
0<TAB>-37<TAB>"yahoo"<TAB>1
0<TAB>0<TAB>"gmail"<TAB>0
0<TAB><TAB>"hotmail"<TAB>1
1<TAB>49.1<TAB>"yahoo"<TAB>
```

"Is Spam" is the response variable, which we are trying to predict from the
"Score", "Email Provider", and "Has Dollar Sign" variables. "Is Spam" and "Has
Dollar Sign" are binary variables, "Score" is a numeric variable, and "Email
Provider" is a categorical variable.
