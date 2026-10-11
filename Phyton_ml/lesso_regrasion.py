
import numpy as np

# 1. Create a dataset
rng = np.random.default_rng(42)
n = 200

x1 = rng.normal(size=n)
x2 = rng.normal(size=n)
x3 = rng.normal(size=n)  # mostly irrelevant feature

y = 4 + 3 * x1 - 2 * x2 + rng.normal(0, 0.5, n)

# 2. Split out the intercept
X_features = np.column_stack((x1, x2, x3))

# Standardize features
mu = X_features.mean(axis=0)
sigma = X_features.std(axis=0)
X_scaled = (X_features - mu) / sigma

# Center y so we can fit the intercept separately
y_mean = y.mean()
y_centered = y - y_mean

# 3. Coordinate descent for Lasso
alpha = 0.1
epochs = 5000

beta = np.zeros(X_scaled.shape[1])
n, p = X_scaled.shape

for epoch in range(epochs):
    for j in range(p):
        # Current predictions before updating coefficient j
        predictions = X_scaled @ beta

        # Add back the contribution of coefficient j
        residual_without_j = (
            y_centered - predictions + X_scaled[:, j] * beta[j]
        )

        rho = np.dot(X_scaled[:, j], residual_without_j) / n
        z = np.dot(X_scaled[:, j], X_scaled[:, j]) / n

        # Soft thresholding
        if rho > alpha:
            beta[j] = (rho - alpha) / z
        elif rho < -alpha:
            beta[j] = (rho + alpha) / z
        else:
            beta[j] = 0.0

# 4. Calculate intercept and predictions
intercept = y_mean - np.dot(mu / sigma, beta)
beta_original = beta / sigma

y_pred = intercept + X_features @ beta_original
mse = np.mean((y - y_pred) ** 2)

print("Intercept:", intercept)
print("Feature coefficients:", beta_original)
print("Training MSE:", mse)
print("Coefficients equal to zero:", np.sum(beta == 0))