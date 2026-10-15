import numpy as np 
from sklearn.model_selection import(
    train_test_split,KFold,GridSearchCV
)
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import Ridge
