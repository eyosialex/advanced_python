import numpy as np
x=np.array([1, 2, 3, 4, 5])
y = np.array([30, 40, 50, 60, 70])
X=np.column_stack((np.ones(len(x)),x))
print(X)
beta= np.linalg.inv(X.T @ X)@ X.T@ y
print (beta)
y_pred= X @ beta
print ( "pridiction of the model is : ")
print (y_pred)
error =y-y_pred
sse=np.sum(error **2 )
mse=np.mean(error**2)
mean_y=np.mean(y)
sst=np.sum((y-mean_y)**2)
R=1-(sse/sst)


print ("SSE:",sse)
print("MSE:", mse)
print ("R^2:",R)
print(error)