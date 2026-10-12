
import numpy as np

# 1. Generate data
rng = np.random.default_rng(42)
n = 200

X_features = rng.normal(size=(n, 3))
true_beta = np.array([3.0, -2.0, 0.0])

y = 5 + X_features @ true_beta + rng.normal(0, 0.5, n)

# 2. Standardize features
mu = X_features.mean(axis=0)
sigma = X_features.std(axis=0)
X_scaled = (X_features - mu) / sigma

# Center y so we can learn the intercept separately
y_mean = y.mean()
y_centered = y - y_mean

# 3. Add the intercept column
X = np.column_stack((np.ones(n), X_scaled))

# 4. Elastic Net strengths
lambda1 = 0.1
lambda2 = 0.1

# Do not penalize the intercept
D = np.eye(X.shape[1])
D[0, 0] = 0

beta = np.zeros(X.shape[1])
alpha = 0.05
epochs = 5000

# 5. Proximal gradient descent
for epoch in range(epochs):
    predictions = X @ beta
    error = predictions - y_centered

    gradient = (2 / n) * (X.T @ error) \
               + 2 * lambda2 * (D @ beta)

    # Gradient step
    u = beta - alpha * gradient

    # L1 soft thresholding; skip the intercept
    beta[0] = u[0]
    beta[1:] = np.sign(u[1:]) * np.maximum(
        np.abs(u[1:]) - alpha * lambda1, 0
    )

# 6. Evaluate
predictions = y_mean + X[:, 1:] @ beta[1:]
mse = np.mean((y - predictions) ** 2)

print("Intercept:", y_mean + beta[0])
print("Feature coefficients:", beta[1:] / sigma)
print("Training MSE:", mse)