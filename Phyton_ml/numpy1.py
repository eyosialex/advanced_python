import numpy as np
y=np.array([23,78,90,89])

y_pred=np.array([21,75,67,89])
error = y-y_pred
SSE=np.sum(error **2)
MAA=np.mean(y)
SST=np.sum((y-MAA)**2)
R=1-(SSE/SST)
print (SSE)
print(MAA)
print(R)