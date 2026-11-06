
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Generate data
X, y = make_moons(
    n_samples=300,
    noise=0.3,
    random_state=42
)


# 2. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# 3. Create the scaler
scaler = StandardScaler()

# 4. Learn mean and standard deviation from training data
X_train_scaled = scaler.fit_transform(X_train)

# 5. Apply the SAME transformation to test data
X_test_scaled = scaler.transform(X_test)

# 6. Train KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# 7. Predict
y_pred = knn.predict(X_test_scaled)

# 8. Evaluate
print(
    f"Test Accuracy: {accuracy_score(y_test, y_pred):.2f}"
)
