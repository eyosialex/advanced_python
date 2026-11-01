from sklearn.datasets import make_regression

X, y, w = make_regression(
    n_samples=100, n_features=10, n_informative=8, coef=True, random_state=1
)

# Obtain the true coefficients
print(f"The true coefficient of this regression problem are:\n{w}")