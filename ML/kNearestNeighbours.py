import numpy as np
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd

df = pd.read_csv('../ML/Data/breast-cancer.txt')
# print len(df)
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True) # drop the "id" column

x = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_sample, X_test, y_sample, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_sample, y_sample)

accuracy = clf.score(X_test, y_test)
print "Accuracy is: ", accuracy

example_measures = np.array([[7,2,1,2,2,8,3,1,2],[8,2,1,9,2,8,3,1,4]])
example_measures = example_measures.reshape(len(example_measures),-1)

pred = clf.predict(example_measures)

print pred

















""" Dataset base Url: http://archive.ics.uci.edu/ml/machine-learning-databases/
Dataset used: http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data
Dataset name: http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.names

Attribute Information: (class attribute has been moved to last column)

   #  Attribute                     Domain
   -- -----------------------------------------
   1. Sample code number            id number
   2. Clump Thickness               1 - 10
   3. Uniformity of Cell Size       1 - 10
   4. Uniformity of Cell Shape      1 - 10
   5. Marginal Adhesion             1 - 10
   6. Single Epithelial Cell Size   1 - 10
   7. Bare Nuclei                   1 - 10
   8. Bland Chromatin               1 - 10
   9. Normal Nucleoli               1 - 10
  10. Mitoses                       1 - 10
  11. Class:                        (2 for benign, 4 for malignant)
 """