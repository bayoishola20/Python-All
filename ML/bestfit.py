from scipy import mean
import numpy as np
import matplotlib.pyplot as plt


xs = np.array([4,2,3,1,5,9], np.float64)

ys = np.array([2,4,6,2,6,8], np.float64)

# bfs - best fit slope 

def bfs(xs, ys):
    m = ( ((mean(xs) * mean(ys)) - mean(xs*ys)) / ((mean(xs)**2) - mean(xs*xs)) )
    return m

print bfs(xs, ys)

# plt.plot(xs, ys)
''' plt.scatter(xs, ys)
plt.show() '''