#=============================================
    #   SVM is a binary classifier  #
    #*******************************#
    # It finds the best seperating
    # hyper plane for our data
#=============================================

import numpy as np
from sklearn import preprocessing,model_selection, svm
import pandas as pd

df = pd.read_csv('./ML/Data/breast-cancer.txt')
# print len(df)
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True) # drop the "id" column

x = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_sample, X_test, y_sample, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = svm.SVC()
clf.fit(X_sample, y_sample)

accuracy = clf.score(X_test, y_test)
print "Accuracy is: ", accuracy


#========================================
    # Sequential Minimal Optimization
    # Common alternative for SVM today
    # Also CVXOPT
#========================================