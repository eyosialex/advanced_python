
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree

# ==================================
# 1. Create the dataset
# ==================================

data = {
    "income": [5000, 6000, 2000, 3000, 7000, 2500],
    "credit_score": [750, 800, 450, 500, 720, 480],
    "existing_debt": [0, 0, 1, 1, 0, 1],
    "loan": [
        "Approve", "Approve", "Reject",
        "Reject", "Approve", "Reject"
    ]
}

df = pd.DataFrame(data)

# ==================================
# 2. Separate features and target
# ==================================

X = df[["income", "credit_score", "existing_debt"]]
y = df["loan"]

# ==================================
# 3. Create Random Forest
# ==================================

forest = RandomForestClassifier(
    n_estimators=5,
    criterion="entropy",
    max_features=2,
    bootstrap=True,
    random_state=42
)

# ==================================
# 4. Train the Random Forest
# ==================================

forest.fit(X, y)

print("Random Forest training completed!")

# ==================================
# 5. Display all Decision Trees
# ==================================

for i, tree in enumerate(forest.estimators_):

    plt.figure(figsize=(14, 7))

    plot_tree(
        tree,
        feature_names=X.columns,
        class_names=forest.classes_,
        filled=True,
        rounded=True
    )

    plt.title(f"Decision Tree {i + 1}")
    plt.show()

# ==================================
# 6. Inspect each tree's root question
# ==================================

for i, tree in enumerate(forest.estimators_):

    feature_index = tree.tree_.feature[0]
    threshold = tree.tree_.threshold[0]

    print(f"\nTree {i + 1}")

    if feature_index >= 0:
        feature_name = X.columns[feature_index]

        print(f"Root question: {feature_name} <= {threshold:.2f}")

    else:
        print("Root is a leaf (no split).")

# ==================================
# 7. Predict a new customer
# ==================================

new_customer = pd.DataFrame([{
    "income": 5500,
    "credit_score": 680,
    "existing_debt": 0
}])

# Individual tree predictions
print("\nIndividual Tree Predictions:")

for i, tree in enumerate(forest.estimators_):

    prediction = tree.predict(new_customer)

    print(f"Tree {i + 1}: {prediction[0]}")

# ==================================
# 8. Final Random Forest prediction
# ==================================

final_prediction = forest.predict(new_customer)

print("\nFinal Random Forest Prediction:")
print(final_prediction[0])

# ==================================
# 9. Prediction probabilities
# ==================================

probabilities = forest.predict_proba(new_customer)

print("\nPrediction Probabilities:")

for class_name, probability in zip(forest.classes_, probabilities[0]):
    print(f"{class_name}: {probability:.2%}")
