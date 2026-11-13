import numpy as np
from sklearn.cluster import KMeans
data=np.array(
    [
    [1, 1],
    [2, 1],
    [1, 2],
    [8, 8],
    [9, 8],
    [8, 9]
]
)
model=KMeans(
    n_clusters=2,
    init="k-means++",
    random_state=42,
    n_init=10


)
lables=model.fit_predict(data)
centroid=model.cluster_centers_
wss=model.inertia_
print("lables ",lables)
print("centroid",centroid)
print("wss ",wss)