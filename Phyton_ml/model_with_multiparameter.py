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
print("target:\n",x)
print("Feature & Obsevation:\n",x.shape);
print ("the length of the array : ",len(x))
x=np.column_stack((np.ones(len(x)),x))
print ("the update value of x: \n",x)



