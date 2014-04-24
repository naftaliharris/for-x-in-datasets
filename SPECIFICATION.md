# Data Format Specification

Each directory under data/ represents a particular dataset. Each directory
must contain a METADATA.json file.

* Numeric, integral, and binary values are represented with numeric strings,
  (scientific notation ok).
* Categorical variables with at least three levels are represented as quoted
  strings.
* Missing data is represented by no text.
* UTF-8 format only.

Open issues:
* Encoding sparse matrices
* Semi-supervized problems: X0.csv?
* Including text fields
* Including ordinal or circular fields
