import pandas as pd

data = {
    "income": [5000, 6000, 2000, 3000, 7000, 2500],
    "credit_score": [750, 800, 450, 500, 720, 480],
    "existing_debt": [0, 0, 1, 1, 0, 1],
    "loan": ["Approve", "Approve", "Reject",
             "Reject", "Approve", "Reject"]
}

df = pd.DataFrame(data)

X = df[["income", "credit_score", "existing_debt"]]
y = df["loan"]

print(df)