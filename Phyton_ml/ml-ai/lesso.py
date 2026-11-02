from sklearn import linear_model

# Training data
X = [[0, 0],
     [1, 1]]

y = [0, 1]

# Create Lasso model
reg = linear_model.Lasso(alpha=0.1)

# Train
reg.fit(X, y)

# Predict
prediction = reg.predict([[1, 1]])

print(prediction)