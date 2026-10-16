import numpy as np 
from sklearn.model_selection import(
    train_test_split,KFold,GridSearchCV
)
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
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
search.fit(x_train,y_train)
print("best parameters : ",search.best_params_['ridge__alpha'])
print ("best CV MSE",-search.best_score_)
