import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4])
y = np.array([2, 3, 5, 4])
epoch=1000
a=0.001
loss= []
x=np.column_stack((np.ones(x.shape[0]),x))
n=len(y)
beta= np.zeros(x.shape[1])
for i in range(epoch):

    y_pre=x@beta
    error=y-y_pre
    #calculate the gradient 
    gradient=(2/n) *x.T @ error
    #update the parameters 
    beta=beta-a*gradient
    #caculate he update pridiction 
    y_new_pred=x@beta

    loss.append(np.mean((y-y_new_pred)**2))
plt.plot(range(1,(epoch+1)),loss)
plt.xlabel("Number Epoch")
plt.ylabel("Loss")
plt.show()
