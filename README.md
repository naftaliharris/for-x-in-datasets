# For X in Datasets

Suppose you have a statistics or machine learning procedure. How can you
determine if it's any good? Arguably the best way to do this is to see if the
procedure perform well on real datasets. Now, in the majority of research
papers, researchers tend to empirically evaluate their methods on simulated data
and perhaps one or two real example datasets. But wouldn't it be nice if you
could evaluate your method on ten, fifty or even a hundred real datasets instead
of just one or two?

In practice, doing so is quite challenging, for three reasons. First of all, you
need to find a large number of datasets. Second of all, you need to figure out
which of those datasets your method is applicable to. And thirdly, you need to
format those datasets consistently so that you can apply your method to them.

There are several online dataset collections, like the [UCI Machine Learning
Repository](http://archive.ics.uci.edu/ml/), [mldata.org](http://mldata.org/),
and [kdnuggets.com](http://www.kdnuggets.com/datasets/index.html), which solve
the first problem and (to varying degrees) the second. But all of them painfully
fail to solve the consistent formatting problem. Datasets file formats vary
between csv, tsv, MS Excel, Rdata, fixed-column width, SVMLight, MS Word
(seriously), and etchings in stone tablets. Even if you convert all of them to a
particular file format, you're still left with inconsistencies about how to
represent binary values, (0/1, -1/+1, g/b, 1/2, "foo"/"bar"), how to represent
missing data, ("NA", "N/A", "NaN", "Missing", 0, -1, "", "?"), and which
variables are supposed to be the predictors and which are the response, among
many others.

This project attempts to solve all three of these problems by collecting a
number of datasets, gathering metadata about them, and, critically, formatting
them consistently according to the explicit specifications in SPECIFICATIONS.md.
By doing so, trying out your method on a number of datasets is hardly more
challenging than a basic for-loop.


## Working with these datasets

You can find a very short example of how to work with these datasets in Python
or R in the corresonding example.\* script. Just clone or download this repo,
copy the script, and you're good to go!


## Contributing

If this project appeals to you, you can help out in many ways!

1.  Contribute one of your datasets: help advance the state of statistics and
    machine learning and see what people can do with your dataset!
2.  Write an example script for working with these datasets in your favorite
    language: Matlab, Julia, C++, Java...
3.  Help work out issues in the specification related to time-series data,
    spatial data, large datasets, unsupervized and semi-supervized learning,
    textual data...
4.  Improve the tools that test datasets for adherence to the specification.
5.  Build tools to help format datasets to adhere to the specification.
6.  Build tools to selectively download datasets so that you don't need to clone
    this whole repo just to work with a subset of its datasets.
