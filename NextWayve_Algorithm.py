theSchool = [[9, 66, 3.56],[ 23, 59, 3.54],[11, 43, 3.48]]

print(doc)

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
# License: BSD 3 clause

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn import datasets
from sklearn.svm import l1_min_c

X = theSchool;
y = []
for i in theSchool:
    y.append(i[0])

# #############################################################################
# Demo path functions

cs = l1_min_c(X, y, loss='log') * np.logspace(0, 3)


print("Not 100% sure what's happening")
start = datetime.now()
clf = linearmodel.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
coefs = []
for c in cs:
    clf.setparams(C=c)
    clf.fit(X, y)
    coefs.append(clf.coef.ravel().copy())
print("This took ", datetime.now() - start, "seconds")

coefs = np.array(coefs)
plt.plot(np.log10(cs), coefs)
ymin, ymax = plt.ylim()
plt.xlabel('log(C)')
plt.ylabel('Coefficients')
plt.title('Logistic Regression Path')
plt.axis('tight')
plt.show()