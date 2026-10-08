import numpy as np
x=np.array([1, 2, 3, 4, 5])
y = np.array([30, 40, 50, 60, 70])
X=np.column_stack((np.ones(len(x)),x))
print(X)
beta= np.linalg.inv(X.T @ X)@ X.T@ y
print (beta)