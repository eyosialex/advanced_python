import numpy as np
x =np.array([
    [1, 2, 7, 1],
    [1, 4, 8, 2],
    [1, 6, 7, 3],
    [1, 8, 9, 4]
])
y = np.array([60, 75, 85, 95])
beta=np.zeros(x.shape[1])
a=0.001
n=len(x)
for epoch in range(10000):
    y_pred=x @ beta
    error=y_pred-y
    gradient_desent=(2/n)* x.T @ error
    beta=beta-a*gradient_desent
print ( "parmeters: \n",beta)
y_pred=x@beta
print ( y_pred)
mse=np.mean((y-y_pred)**2)
print ( "MSE: ",mse)