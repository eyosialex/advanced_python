import numpy as np
X = np.array([
    [1, 2, 7, 1],
    [1, 4, 8, 2],
    [1, 6, 7, 3],
    [1, 8, 9, 4]
], )
y = np.array([60, 75, 85, 95])
x1=X.shape[0]
y1=X.shape[1]
epoch=1000
min_batch=2
a=0.001
beta=np.zeros(y1)
start=0
for i in range(epoch):
    for start in range (0,x1,min_batch):
        end=min(start+min_batch,x1 )
        x_in=X[start:end]
        y_out=y[start:end]
        y_pre=x_in@beta
        error=y_pre-y_out
        gradient_descent=(2/min_batch)*x_in.T@error
        beta=beta-a*gradient_descent
        

