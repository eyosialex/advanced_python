import numpy as np
x= np.array(
[
    [2, 7, 1],
    [4, 8, 2],
    [6, 7, 3],
    [8, 9, 4]
])
y=np.array([60, 75, 85, 95])
print("features:\n",x)
print("target:\n",y)
print("Feature & Obsevation:\n",x.shape);
print ("the length of the array : ",len(x))
x=np.column_stack((np.ones(len(x)),x))
print ("the update value of x: \n",x)
beta=np.linalg.pinv(x.T @ x) @ x.T @ y
print("the pameters value:\n ",beta)
y_pre=x @ beta
print ("pridiction \n:",y_pre)
error=y-y_pre
mse=np.mean(error**2)
rmse=np.sqrt(mse)
sse=np.sum(error**2)
mean_y=np.mean(y)
SST=np.sum((y-mean_y)**2)
r=1-sse/SST
print ("SSE: ",sse);
print("MSE: ",mse)
print("RMSE: ",rmse)
print("R^2: ",r)



