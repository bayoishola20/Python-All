import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = { 1:'r', -1:'b' }

        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
        
    def fit(self, data):
        pass
    
    def predict(self, features):
        # sign(x.w + b)
        classification = np.sign( np.dot(np.dot(features), self.w) + self.b )
        return classification

data_dict = { -1: np.array([ [1,7],[4,6],[2,3] ]), 1: np.array([ [3,3],[4,1],[9,2] ]) }

print np.array([[]])