import numpy as np
rng=np.random.default_rng(42)
house_size=rng.uniform(30,300,100)
room_no=rng.integers(1,6,100)
price=(30+15*house_size+
       2*room_no)
y=price.reshape(100,1)
print (y)
x=np.column_stack((np.ones(len(y)),house_size,room_no))
indices=rng.permutation(len(y))
train_size=int(0.8*len(y))
test_size=len(y)-train_size

train_index=indices[:train_size]
test_index=indices[train_size:]

x_train=x[train_index].copy()
y_train=y[train_index].copy()

x_test=x[test_index].copy()
y_test=y[test_index].copy()




mu = x_train[:, 1:].mean(axis=0)
sigma = x_train[:, 1:].std(axis=0)

sigma[sigma == 0] = 1

x_train[:, 1:] = (x_train[:, 1:] - mu) / sigma
x_test[:, 1:] = (x_test[:, 1:] - mu) / sigma
sigma[sigma == 0] = 1
alpha =0.0001
beta=np.zeros((x_train.shape[1],1))
epoch=3000
for i in range ( epoch):
    x_pre=x_train @beta
    error =x_pre-y_train
    gradient=(2/len(y_train))*x_train.T @error
    beta=beta-alpha*gradient
x_pre=x_train @ beta
train_mse=np.mean((x_pre-y_train)**2)

test_pre=x_test @ beta
test_mse=np.mean((test_pre-y_test)**2)

print("train size" ,train_size)
print("test size:" ,test_size)
print("\nMatrix shapes:")
print("X_train:", x_train.shape)
print("y_train:", y_train.shape)
print("X_test:", x_test.shape)
print("y_test:", y_test.shape)
print("beta:", beta.shape)
print("test predictions:", test_pre.shape)

print("\nLearned parameters:")
print(beta)

print("\nTraining MSE:",train_mse)
print("Testing MSE:", test_mse)


