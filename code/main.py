import copy
from helper import read_data
from solution import Tree


def test_tree_accuracy(vocab, data):
    print('='*58)
    tree = Tree(vocab)
    trainlen = len(data[('train', 'vector')])
    tree = tree.build_tree(list(zip(
        data[('train', 'vector')][:int(trainlen * 0.8)],
        data[('train', 'labels')][:int(trainlen * 0.8)])))

    Ptree = tree.prune_tree(
        copy.deepcopy(tree), list(zip(
            data[('train', 'vector')][int(trainlen * 0.8):],
            data[('train', 'labels')][int(trainlen * 0.8):])))
    print(
        'Validate accuracy on tree without pruning ========>',
        tree.test_data(tree, list(zip(
            data[('train', 'vector')][int(trainlen * 0.8):],
            data[('train', 'labels')][int(trainlen * 0.8):]))))
    print(
        'Validate accuracy on tree with pruning ===========>',
        tree.test_data(Ptree, list(zip(
            data[('train', 'vector')][int(trainlen * 0.8):],
            data[('train', 'labels')][int(trainlen * 0.8):]))))
    print(
        'Test accuracy on tree without pruning ============>',
        tree.test_data(tree, list(zip(
            data[('test', 'vector')],
            data[('test', 'labels')]))))
    print(
        'Test accuracy on tree with pruning ===============>',
        tree.test_data(Ptree, list(zip(
            data[('test', 'vector')],
            data[('test', 'labels')]))))
    print('Tree size without pruning ========================> %6d' % (
        tree.size))
    print('Tree size with pruning ===========================> %6d' % (
        Ptree.size))
    print('Tree depth without pruning =======================> %6d' % (
        tree.depth))
    print('Tree depth with pruning ==========================> %6d' % (
        Ptree.depth))
    print('='*58)


if __name__ == '__main__':
    vocab, data = read_data(dataloc='../data/')
    test_tree_accuracy(vocab, data)
