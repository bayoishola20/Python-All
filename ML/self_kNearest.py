import warnings
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

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
    knnalgos
    return vote_result