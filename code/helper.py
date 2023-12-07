def read_data(dataloc='../data/'):
    data = {}
    for dataset in ['test', 'train']:
        for feature in ['data', 'labels']:
            with open(dataloc+dataset+feature+'.txt') as f:
                lines = [line.strip() for line in f]
                if feature == 'labels':
                    lines = list(map(int, lines))
                data[(dataset, feature)] = lines

    with open(dataloc+'stoplist.txt') as f:
        data['stoplist'] = set([word.strip() for word in f])
    return preprocess(data)


def preprocess(data):
    vocabulary = set()
    for line in data[('train', 'data')]:
        vocabulary.update(line.split())
    vocabulary -= data['stoplist']
    vocabulary = sorted(vocabulary)
    data[('train', 'vector')] = []
    for line in data[('train', 'data')]:
        vector = [0]*len(vocabulary)
        for word in set(line.split())-data['stoplist']:
            vector[vocabulary.index(word)] = 1
        data[('train', 'vector')].append(vector)
    data[('test', 'vector')] = []
    for line in data[('test', 'data')]:
        vector = [0]*len(vocabulary)
        for word in set(line.split())-data['stoplist']:
            if word in vocabulary:
                vector[vocabulary.index(word)] = 1
        data[('test', 'vector')].append(vector)
    return vocabulary, data
