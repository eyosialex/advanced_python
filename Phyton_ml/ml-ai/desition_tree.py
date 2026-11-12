
# ==========================================
# 1. IMPORT LIBRARIES
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree


# ==========================================
# 2. CREATE DATASET
# ==========================================

data = {
    "income": [5000, 6000, 2000, 3000, 7000, 2500],
    "credit_score": [750, 800, 450, 500, 720, 480],
    "existing_debt": [0, 0, 1, 1, 0, 1],
    "loan": [
        "Approve",
        "Approve",
        "Reject",
        "Reject",
        "Approve",
        "Reject"
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

print("ORIGINAL DATASET:")
print(df)


# ==========================================
# 3. SEPARATE FEATURES AND TARGET
# ==========================================

# Input features
X = df[["income", "credit_score", "existing_debt"]]

# Target variable
y = df["loan"]


# ==========================================
# 4. CREATE DECISION TREE MODEL
# ==========================================

model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=1,
    random_state=42
)


# ==========================================
# 5. TRAIN THE MODEL
# ==========================================

model.fit(X, y)

print("\nMODEL TRAINING COMPLETED!")


# ==========================================
# 6. VISUALIZE THE DECISION TREE
# ==========================================

plt.figure(figsize=(14, 8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True,
    fontsize=12
)

plt.title("Decision Tree - Loan Approval Prediction")

plt.show()


# ==========================================
# 7. GET ROOT NODE INFORMATION
# ==========================================

# Get selected root feature index
root_feature_index = model.tree_.feature[0]

# Get selected feature name
root_feature = X.columns[root_feature_index]

# Get root threshold
root_threshold = model.tree_.threshold[0]

print("\nROOT NODE INFORMATION:")
print("Selected Feature:", root_feature)
print("Selected Threshold:", root_threshold)

# Get root entropy
root_entropy = model.tree_.impurity[0]

print("Root Entropy:", root_entropy)

# Get number of samples
root_samples = model.tree_.n_node_samples[0]

print("Root Samples:", root_samples)


# ==========================================
# 8. DISPLAY CHILD NODE INFORMATION
# ==========================================

print("\nCHILD NODE INFORMATION:")

for node_id in range(1, model.tree_.node_count):

    print(f"\nNode {node_id}")

    print("Entropy:", model.tree_.impurity[node_id])

    print("Samples:", model.tree_.n_node_samples[node_id])

    print("Class Distribution:", model.tree_.value[node_id])


# ==========================================
# 9. PREDICT A NEW CUSTOMER
# ==========================================

new_customer = pd.DataFrame([{
    "income": 5500,
    "credit_score": 680,
    "existing_debt": 0
}])

prediction = model.predict(new_customer)

print("\nNEW CUSTOMER:")
print(new_customer)

print("\nLOAN PREDICTION:", prediction[0])


# ==========================================
# 10. DISPLAY PREDICTION PROBABILITIES
# ==========================================

probabilities = model.predict_proba(new_customer)

print("\nPREDICTION PROBABILITIES:")

for class_name, probability in zip(model.classes_, probabilities[0]):
    print(f"{class_name}: {probability:.2%}")
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset (features X and labels y)
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split into 80% training data and 20% unseen test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Initialize and train the Decision Tree
# max_depth=3 prevents the tree from growing too deep and overfitting
clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# 4. Make predictions on the test set
y_pred = clf.predict(X_test)

# 5. Evaluate performance
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 6. Print the actual if-else decision rules the tree learned
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Learned Decision Tree Rules:\n")
print(tree_rules)