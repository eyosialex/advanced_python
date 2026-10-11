import numpy as np;
x1 = np.array([1, 2, 3, 4, 5], dtype=float)
x2 = np.array([2, 1, 4, 3, 5], dtype=float)
y = np.array([5, 7, 10, 11, 14], dtype=float).reshape(-1, 1)
x= np.column_stack((np.ones(len(y)),x1,x2))
n=len(y)
p=x.shape[1]
d=np.eye(p)
d[0,0]=0
beta=np.zeros((p,1))
alpha=0.001
epoch=3000
lambda_rang=0.1
for i in range(epoch):
    y_pred=x@beta
    erorr=y- y_pred
    gradient=(2/n)*x.T@erorr+2*lambda_rang*d@ beta 
    beta=beta-alpha*gradient
x_pre=x@beta 
mse=np.mean((x_pre-y)**2)
penality=lambda_rang*(beta.T @d@beta).item()
total_lose=mse+penality
print("learned parameters : \n",beta)
print ( "MSE: ",mse)
print("penality :",penality)
print("total lose : ",total_lose)