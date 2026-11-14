
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 1: Create the dataset
data = np.array([
    [2],
    [5],
    [9],
    [10]
])

# Step 2: Create the clustering model
model = AgglomerativeClustering(
    n_clusters=2,
    metric="euclidean",
    linkage="average"
)

# Step 3: Train the model and predict clusters
labels = model.fit_predict(data)

# Step 4: Display the results
result = pd.DataFrame({
    "Student": ["A", "B", "C", "D"],
    "Score": data.flatten(),
    "Cluster": labels
})

print(result)

# Step 5: Draw the clusters
plt.scatter(
x=data[:,0],
y=np.zeros(len(data)),
c=labels,
cmap="viridis",
s=150

)

students=["A", "B", "C", "D"]



for i, student in enumerate(students):
    plt.annotate(student, (data[i, 0], 0.02))

plt.title("Agglomerative Clustering")
plt.xlabel("Exam Score")
plt.yticks([])
plt.show()

# Step 6: Create the dendrogram
linked = linkage(data, method="average", metric="euclidean")

plt.figure(figsize=(8, 5))

dendrogram(
    linked,
    labels=["A", "B", "C", "D"]
)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Students")
plt.ylabel("Distance")
plt.show()
