from scipy import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([4,2,3,1,5,9], np.float64)

ys = np.array([2,4,6,2,6,8], np.float64)

# bfs - best fit 

def bf(xs, ys):
    # mean
    m = ( ((mean(xs) * mean(ys)) - mean(xs*ys)) / ((mean(xs)**2) - mean(xs*xs)) )

    # intercept
    b = mean(ys) - m * mean(xs)

    return m, b

print "slope %f, y-intercept %f" %(bf(xs, ys))

# r squared

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)

def coef_of_det(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr/squared_error_y_mean)

reg_line = [(m*x) + b for x in xs]

predict_x = 8
predict_y = (m * predict_x) + b

r_squared = coef_of_det(ys, reg_line)
print "R squared ", r_squared

# plt.plot(xs, ys)
plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, s=100, c='r')
plt.plot(xs, reg_line)
plt.show()