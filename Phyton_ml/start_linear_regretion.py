import numpy as np
rng=np.random.default_rng(42)
house_size=rng.uniform(30,300,100)
room_no=rng.integers(1,6,100)
price=(30+15*house_size+
       2*room_no)
y=price.reshape(100,1)
print (y)
x=np.column_stack(np.ones(len(y)),house_size,room_no)
indices=rng.permutation(len(y))
train_size=int(0.8*len(y))
test_size=len(y)-train_size


train_index=indices[:,train_size]
test_index=indices[train_size,:]

x_train=indices[train_index]
y_train=indices[train_index]

x_test=x[test_index]
y_test=y[test_index]


mu=x_train[:,1:].mean(axis=0)
sigma=x_train[:,1:].std(axis=0)

x_train =((x_train[:,1:]-mu)/sigma)
y_train =((y_train[:,1:]-mu)/sigma)
alpha =0.001
beta=np.zeros(x.shape[1])



