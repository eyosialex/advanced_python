import numpy as np
X = np.array([
    [1, 2, 7, 1],   
    [1, 4, 8, 2],   
    [1, 6, 7, 3],   
    [1, 8, 9, 4]    
])

y = np.array([60, 75, 85, 95])
epoch=100
x1=X.shape[0]
y1=X.shape[1]
a=0.001
beta=np.zeros(y1)
for i in range(epoch):
    for j in range(x1):
        xi=X[j]
        yj=y[j]

        y_pre=xi*beta
        error=y-y_pre
        gradient= (2)*xi*error
        beta=beta-a*gradient
print ("parameters: ",beta)
