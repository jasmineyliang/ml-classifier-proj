# ml-skill-proj3


1. You are provided with a training set of
examples . Which feature will you pick
first to split the data as per the ID3 decision tree learning
algorithm? Show all your work: compute the information gain for
all the four attributes and pick the best one.



2. We know that we can convert any decision tree
into a set of if-then rules, where there is one rule per leaf
node. Suppose you are given a set of rules $R = \{r_1, r_2,
\dots, r_k\}$, where $r_i$ corresponds to the $i^{th}$ rule. Is
it possible to convert the rule set $R$ into an equivalent
decision tree? Explain your construction or give a
counterexample.

3. Suppose $\boldsymbol x = [x_1, x_2, \dots,
x_d]$ and $\boldsymbol z = [z_1, z_2, \dots, z_d]$ be two points in
a high-dimensional space (i.e., $d$ is very large).

(a) Try to prove the following, where the
    right-hand side quantity represent the standard Euclidean
    distance.
![image](https://github.com/jasmineyliang/ml-skill-proj3/assets/150869870/d2be0143-ee95-4a8e-b3e1-2b1187b2153b)


    
(b) We know that the computation of nearest
    neighbors is very expensive in the high-dimensional space.
    Discuss how we can make use of the above property to make the
    nearest neighbors computation efficient?



4. Fortune Cookie Classifier: You will
build a binary fortune cookie classifier. This classifier will be
used to classify fortune cookie messages into two classes:
messages that predict what will happen in the future (class 1)
and messages that just contain a wise saying (class 0). For
example, ``Never go in against a Sicilian when death is on the
line'' would be a message in class 0. ``You will get an A in
Machine learning class'' would be a message in class 1.

There are three sets of files. All words
in these files are lower case and punctuation has been removed.

1) The training data: traindata.txt. This is the training data
consisting of fortune cookie messages. trainlabels.txt: This file
contains the class labels for the training data. 

2) The testing data: testdata.txt. This is the testing data
consisting of fortune cookie messages. testlabels.txt: This file
contains the class labels for the testing data. 

3) A list of stopwords: stoplist.txt 

There are two steps: the pre-processing step and the
classification step. In the pre-processing step, we convert
fortune cookie messages into features to be used by your
classifier. We use a bag of words representation. The following
steps outline the process involved: 

Form the vocabulary. The vocabulary consists of the set of all
the words that are in the training data with stop words removed
(stop words are common, uninformative words such as ``a'' and
``the'' that are listed in the file stoplist.txt). The vocabulary
will now be the features of your training data. Keep the
vocabulary in alphabetical order to help you with debugging. 

Then, we convert the training data into a set of features. Let M
be the size of your vocabulary. For each fortune cookie message,
we convert it into a feature vector of size M. Each slot in
that feature vector takes the value of 0 or 1. For these M slots,
if the ith slot is 1, it means that the ith word in the
vocabulary is present in the fortune cookie message; otherwise,
if it is 0, then the ith word is not present in the message. Most
of these feature vector slots will be 0. Since you are keeping
the vocabulary in alphabetical order, the first feature will be
the first word alphabetically in the vocabulary.

(a) Implement the ID3 decision tree learning
algorithm that we discussed in the class. The key step in the
decision tree learning is choosing the next feature to split on.
Implement the information gain heuristic for selecting the next
feature.

(b) Implement the decision tree pruning algorithm
discussed in the class (via validation data).

(c)  Compute the accuracy of decision tree and
pruned decision tree on validation examples and testing examples.
List your observations by comparing the performance of decision
tree with and without pruning.

