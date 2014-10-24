# For X in Datasets

Suppose you have a statistics or machine learning procedure. How can you
determine if it's any good? Arguably the best way to do this is to see if the
procedure performs well on real datasets. Now, in the majority of research
papers, researchers tend to empirically evaluate their methods on simulated data
and perhaps one or two real example datasets. But wouldn't it be nice if you
could evaluate your method on ten, fifty or even a hundred real datasets instead
of just one or two?

In practice, doing so is quite challenging. This is due primarily to the fact
that datasets are not formatted consistently. It's not at all hard to find lots of
datasets--there are a number of online collections, like the [UCI Machine Learning
Repository](http://archive.ics.uci.edu/ml/), [mldata.org](http://mldata.org/),
and [kdnuggets.com](http://www.kdnuggets.com/datasets/index.html)--but most
collections have datasets that are formatted painfully inconsistently.

Dataset file formats vary between csv, tsv, MS Excel, Rdata, fixed-column
width, SVMLight, MS Word (seriously), and etchings in stone tablets. Even if you
convert all of them to a particular file format, you're still left with
inconsistencies about how to represent binary values, (0/1, -1/+1, g/b, 1/2,
"foo"/"bar"), how to represent missing data, ("NA", "N/A", "NaN", "Missing", 0,
-1, "", "?"), and which variables are supposed to be the predictors and which
is the response, among many others.

This project attempts to solve this problem by collecting a number of datasets,
including from the sources above, gathering metadata about them, and,
critically, formatting them consistently according to the explicit
specifications in SPECIFICATIONS.md. By doing so, trying out your method on a
number of datasets is hardly more challenging than a basic for-loop in your
language of choice.

Different datasets have different structures, and are gathered to achieve
different goals. This project considers only datasets with a single tabular
structure, and for which the primary goal is to understand or predict a response
variable from some feature variables. In particular, this means that this
collection excludes relational data (like from a SQL database), nested data
(like json), graph data, and text data. It also excludes most time series data
and "high dimensional" data, for which there are many more predictor variables
than response variables.

The reason for these limitations is that each different structure requires its
own format. To do well on one thing rather than poorly on many, this project
focuses just on the structure that is arguably most popular, the traditional
"high n, low p" tabular dataset.


## Working with these datasets

You can find a very short example of how to work with these datasets in Python,
R, or Julia in the corresonding example.\* script. Just clone or download this
repo, copy the script, and you're good to go!


## Contributing

If this project appeals to you, you can help out in many ways!

1.  Contribute one of your datasets: help advance the state of statistics and
    machine learning and see what people can do with your dataset!
2.  Write an example script for working with these datasets in your favorite
    language: Matlab, C++, Java...
3.  Build tools to help format datasets to adhere to the specification.
4.  Use your imagination!
