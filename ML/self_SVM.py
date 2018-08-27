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

        step_sizes = [ self.max_feature_value * 0.1, self.max_feature_value * 0.01, self.max_feature_value * 0.001, ]

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
                                # print xi, ':', yi * ( np.dot(w_t, xi)+b )
                        
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                
                if w[0] < 0:
                    optimized = True
                    print 'Optimized a step.'
                else:
                    w = w - step
            norms = sorted( [n for n in opt_dict] )

            opt_choice = norms[0]

            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]

            latest_optimum = opt_choice[0][0] + step * 2
    
    def predict(self, features):
        # sign(x.w + b)
        classification = np.sign( np.dot(np.array(features), self.w) + self.b )
        if classification != 0:
          self.ax.scatter(features[0], features[1], s = 200, marker= '+', c = self.colors[classification])
        return classification
    
    def visualize(self):
        [ [ self.ax.scatter( x[0], x[1], s=100, color=self.colors[i]) for x in data_dict[i]] for i in data_dict ]

        # hyperplane = x.w + b where v in below is value being sought
        #  v = x.w + b
        def hyperplane(x,w,b,v):
            return (-w[0]*x-b+v) / w[1]
        
        datarange = ( self.min_feature_value*0.9, self.max_feature_value*1.1 )
        hyperplane_x_min = datarange[0]
        hyperplane_x_max = datarange[1]

        # positive SV hyperplane: (w.x + b) = 1
        psv1 = hyperplane(hyperplane_x_min, self.w, self.b, 1)
        psv2 = hyperplane(hyperplane_x_max, self.w, self.b, 1)
        self.ax.plot( [hyperplane_x_min, hyperplane_x_max],[psv1, psv2],'k' )

        # negative SV hyperplane: (w.x + b) = -1
        nsv1 = hyperplane(hyperplane_x_min, self.w, self.b, -1)
        nsv2 = hyperplane(hyperplane_x_max, self.w, self.b, -1)
        self.ax.plot( [hyperplane_x_min, hyperplane_x_max],[nsv1, nsv2],'k' )

        # decision boundary SV hyperplane: (w.x + b) = 0
        db1 = hyperplane(hyperplane_x_min, self.w, self.b, 0)
        db2 = hyperplane(hyperplane_x_max, self.w, self.b, 0)
        self.ax.plot( [hyperplane_x_min, hyperplane_x_max],[db1, db2],'o--' )

        plt.show()



data_dict = { -1: np.array([ [1,7],[4,6],[2,3] ]), 1: np.array([ [3,3],[4,1],[9,2] ]) }

# print np.array([[]])

svm = Support_Vector_Machine()
svm.fit(data = data_dict)


predict_us = [ [2,10], [4,3], [2,2], [7,6], [4,4], [8,2], [1,7], [3,6] ]

for p in predict_us:
    svm.predict(p)


svm.visualize()

#30