import numpy as np 
from sklearn.model_selection import(
    train_test_split,KFold,GridSearchCV,learning_curve
)
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
import  matplotlib.pyplot as plt
np.random.seed(42)
n=100
house_size=np.random.uniform(100,1000,n)
room_no=np.random.randint(1,6,n)
x=np.column_stack((house_size,room_no))
noice=np.random.normal(0,20,n)
y=15+50*room_no+10*house_size+noice

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=make_pipeline(
    StandardScaler(),
    Ridge()
)
parametres={
    "ridge__alpha":[0.001, 0.01, 0.1, 1, 10, 100]
}
cv=KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
search=GridSearchCV(
    estimator=model,
    param_grid=parametres,
    scoring="neg_mean_squared_error",
    cv=cv
)
size_score,train_scores,val_scores=learning_curve(
    model,x_train,y_train,
    train_sizes=np.linspace(0.2, 1.0,5),
    cv=cv,scoring="neg_mean_squared_error"
)
search.fit(x_train,y_train)
print("best parameters : ",search.best_params_['ridge__alpha'])
print ("best CV MSE",-search.best_score_)
for alpha, score in zip(
    search.cv_results_["param_ridge__alpha"],
    search.cv_results_["mean_test_score"]
):
    print(f"alpha={alpha}: CV MSE={-score:.2f}")
best_model=search.best_estimator_
test_pridict=best_model.predict(x_test)
mse=mean_squared_error(
   test_pridict,y_test 
)
print ( "test MSE ",mse)

train_mse = -train_scores.mean(axis=1)
val_mse = -val_scores.mean(axis=1)

# 6. Print the results
print("Training size | Training MSE | Validation MSE")

for size, train_error, val_error in zip(
    size_score, train_mse, val_mse
):
    print(
        f"{size:13d} | "
        f"{train_error:12.2f} | "
        f"{val_error:14.2f}"
    )
plt.plot(size_score, train_mse, marker="o", label="Training MSE")
plt.plot(size_score, val_mse, marker="o", label="Validation MSE")

plt.xlabel("Number of training examples")
plt.ylabel("Mean Squared Error")
plt.title("Ridge Regression Learning Curve")
plt.legend()
plt.grid(True)
plt.show()