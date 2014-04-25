# For X in Datasets

Suppose you have a statistics or machine learning procedure. How do you know if
it's any good? Simply put, a procedure is good if it tends to perform well on
real datasets. Now, in the majority of research papers, researchers tend to
empirically evaluate their methods on simulated data and perhaps one or two
real example datasets. But wouldn't it be nice if you could evaluate your method
on ten, fifty or even a hundred real datasets instead of a measly one or two?

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
missing data, ("NA", "N/A", "NaN", "Missing", "", "?"), and which variables are
supposed to be the predictors and which are the response, among many others.

This project attempts to solve all three of these problems by collecting a
number of datasets, gathering metadata about them, and, critically, formatting
them consistently according to strict, explicit specifications. By doing so,
trying out your method on a number of datasets is hardly more challenging then a
basic for-loop. You can find a very short example of how to work with these
datasets in your language of choice in the corresponding example.\* scripts.

The rest of this project is organized as follows: The datasets/ directory
contains the actual datasets, SPECIFICATION.md defines the formats they adhere
to, utils/ contains code for ensuring that adherence, and test.py runs that
code.
