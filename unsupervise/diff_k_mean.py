
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [8, 8],
    [9, 8],
    [8, 9]
])

wcss = []
silhouette_scores = []

k_values = range(2, 6)

for k in k_values:

    model = KMeans(
        n_clusters=k,
        init="k-means++",
        n_init=10,
        random_state=42
    )

    labels = model.fit_predict(data)

    wcss.append(model.inertia_)

    score = silhouette_score(data, labels)

    silhouette_scores.append(score)

    print(f"K = {k}")
    print(f"WCSS = {model.inertia_:.4f}")
    print(f"Silhouette Score = {score:.4f}")
    print("--------------------")

# Plot both evaluation methods
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(
    list(k_values),
    wcss,
    marker="o"
)
axes[0].set_title("Elbow Method")
axes[0].set_xlabel("Number of Clusters (K)")
axes[0].set_ylabel("WCSS")

axes[1].plot(
    list(k_values),
    silhouette_scores,
    marker="o"
)
axes[1].set_title("Silhouette Analysis")
axes[1].set_xlabel("Number of Clusters (K)")
axes[1].set_ylabel("Silhouette Score")

plt.tight_layout()
plt.show()
