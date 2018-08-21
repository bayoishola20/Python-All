import warnings
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import pandas as pd
import random

style.use('fivethirtyeight')

# print style.available

dataset = { 'k': [[1,2],[2,3],[3,1]], 'r': [[6,5],[7,7],[8,6]]}
new_features = [5,7]

""" for i in dataset:
    for j in dataset[i]:
        plt.scatter(j[0], j[1], s=100, c=i) """

""" [[plt.scatter(j[0], j[1], s=100, c=i) for j in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], s=100, c='g')
plt.show() """

def kNearest(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('k should be higher than the total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:
            # euclidean_dist = sqrt( (features[0] - predict[0])**2 + (features[1] - predict[1])**2 )
            # euclidean_dist = np.sqrt( np.sum( (np.array(features) - np.array(predict)) **2) )
            euclidean_dist = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_dist, group])
    votes = [ i[1] for i in sorted(distances)[:k] ]
    # print Counter(votes).most_common(1)
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / float(k)
    return vote_result, confidence

# print "kNearest is:", kNearest(dataset, new_features, k=3)

""" result = kNearest(dataset, new_features, k=3)
[[plt.scatter(j[0], j[1], s=100, c=i) for j in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], s=50, c=result)
plt.show() """

accuracies = []

for i in xrange(5): #5 is number of iterations for test
    df = pd.read_csv('./ML/Data/breast-cancer.txt')
    df.replace('?', -99999, inplace=True)
    df.drop(['id'], 1, inplace=True)
    full_data = df.astype(float).values.tolist()
    # print len(full_data)

    random.shuffle(full_data)

    test_size = 0.2
    sample_set = {2:[], 4:[]}
    test_set = {2:[], 4:[]}

    sample_data = full_data[:-int(test_size*len(full_data))]
    # print len(sample_data)
    test_data = full_data[-int(test_size*len(full_data)):]

    for i in sample_data:
        sample_set[i[-1]].append(i[:-1])

    for j in test_data:
        test_set[j[-1]].append(j[:-1])

    correct = 0
    total = 0

    for group in test_set:
        for data in test_set[group]:
            vote, confidence = kNearest(sample_set, data, k=5)
            if group == vote:
                correct += 1
            else:
                print confidence
            total += 1

    print 'Accuracy:', float(correct)/total
    accuracies.append(correct/total)

print sum(accuracies)/len(accuracies)
