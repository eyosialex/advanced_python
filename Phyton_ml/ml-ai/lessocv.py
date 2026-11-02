import numpy as np
from sklearn.linear_model import lasso_path
X = np.array([[1, 2, 3.1], [2.3, 5.4, 4.3]]).T
y = np.array([1, 2, 3.1])
# Use lasso_path to compute a coefficient path
_, coef_path, _ = lasso_path(X, y, alphas=[5., 1., .5])
print(coef_path)
import numpy as np
from sklearn.linear_model import lasso_path
X = np.array([[1, 2, 3.1], [2.3, 5.4, 4.3]]).T
y = np.array([1, 2, 3.1])
# Use lasso_path to compute a coefficient path
_, coef_path, _ = lasso_path(X, y, alphas=[5., 1., .5])
print(coef_path)