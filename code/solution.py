import math

THETA = 0.5


class Tree(object):

    def __init__(self, vocab=None, feature=None, ys=[], left=None, right=None):
        self.vocab = vocab
        self.feature = feature
        self.ys = ys
        self.left = left
        self.right = right

    @property
    def size(self):
        size = 1
        if type(self.left) == int:
            size += 1
        else:
            size += self.left.size
        if type(self.right) == int:
            size += 1
        else:
            size += self.right.size
        return size

    @property
    def depth(self):
        left_depth = 1 if type(self.left) == int else self.left.depth
        right_depth = 1 if type(self.right) == int else self.right.depth
        return max(left_depth, right_depth)+1

    def entropy(self, data):
        """Compute entropy of data.

        Args:
            data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]

        Returns:
            entropy of data (float)
        """
        ### YOUR CODE HERE



        ### END YOUR CODE

    def gain(self, data, feature):
        """Compute the gain of data of splitting by feature.

        Args:
            data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]
            feature: index of feature to split the data

        Returns:
            gain of splitting data by feature
        """
        ### YOUR CODE HERE

        # please call self.entropy to compute entropy


        ### END YOUR CODE

    def get_best_feature(self, data):
        """Find the best feature to split data.

        Args:
            data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]

        Returns:
            index of feature to split data
        """
        ### YOUR CODE HERE

        # please call self.gain to compute gain

        ### END YOUR CODE

    def build_tree(self, data):
        ys = {}
        for x, y in data:
            ys[y] = ys.get(y, 0) + 1
        if len(ys) == 1:
            return list(ys)[0]
        feature = self.get_best_feature(data)

        ### YOUR CODE HERE

        # please split your data with feature and build two sub-trees
        # by calling self.build_tree recursively

        # Use THETA to split the continous feature

        ### END YOUR CODE

    def test_entry(self, tree, entry):
        x, y = entry
        if type(tree) == int:
            return tree, y
        if x[self.vocab.index(tree.feature)] < THETA:
            return self.test_entry(tree.left, entry)
        else:
            return self.test_entry(tree.right, entry)

    def test_data(self, tree, data):
        count = 0
        for d in data:
            y_hat, y = self.test_entry(tree, d)
            count += (y_hat == y)
        return round(count/float(len(data)), 4)

    def prune_tree(self, tree, data):
        """Find the best feature to split data.

        Args:
            tree: a decision tree to prune
            data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]

        Returns:
            a pruned tree
        """
        ### YOUR CODE HERE

        # please call self.test_data to obtain validation error
        # please call self.prune_tree recursively for pruning tree

        ### END YOUR CODE
