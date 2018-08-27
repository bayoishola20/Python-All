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
        self.data = data
        # { ||w||: [w,b] }
        opt_dict = {}

        transforms = [ [1,1],[-1,1],[-1,-1],[1,-1] ]

        all_data = []

        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        step_sizes = [ self.max_feature_value * 0.1, self.max_feature_value * 0.01, self.max_feature_value * 0.001 ]

        # extremely expensive
        b_range_multiple = 5

        b_multiple = 5

        latest_optimum = self.max_feature_value * 10

        for step in step_sizes:
            w = np.array( [latest_optimum, latest_optimum] )

            optimized = False
            while not optimized:
                for b in np.arange( -1*(self.max_feature_value*b_range_multiple), self.max_feature_value*b_range_multiple, step*b_multiple ):
                    for transformation in transforms:
                        w_t = w*transformation
                        found_option = True
                        # yi(xi.w + b) >= 1
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                if not yi * ( np.dot(w_t, xi)+b ) >= 1:
                                    found_option = False
                        
                        if found_option:
                            opt_dict[np.linalg.norm(w_t) = [w_t, b]]
                                
    
    def predict(self, features):
        # sign(x.w + b)
        classification = np.sign( np.dot(np.dot(features), self.w) + self.b )
        return classification

data_dict = { -1: np.array([ [1,7],[4,6],[2,3] ]), 1: np.array([ [3,3],[4,1],[9,2] ]) }

print np.array([[]])

#26