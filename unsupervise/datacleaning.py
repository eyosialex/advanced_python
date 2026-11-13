import pandas as pd 
import matplotlib.pyplot as plt
import numpy as num 
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
scaler=StandardScaler()

data = {
    "student_id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115,
        101, 117, 118, 119, 120
    ],
    "age": [
        20, 21, 19, 22, np.nan,
        20, 23, 21, 19, 22,
        20, np.nan, 24, 21, 20,
        20, 22, 23, 19, 21
    ],
    "study_hours": [
        3, 5, 2, 6, 4,
        np.nan, 7, 3, 2, 5,
        4, 6, 8, 3, 5,
        3, 4, np.nan, 2, 6
    ],

    "attendance": [
        80, 90, 65, 95, 85,
        75, 98, np.nan, 60, 88,
        82, 92, 99, 70, 87,
        80, 78, 94, 55, 91
    ],

    "exam_score": [
        65, 85, 55, 92, 75,
        68, 96, 72, np.nan, 83,
        78, 89, 98, 60, 86,
        65, 74, 91, 50, 88
    ],

    "department": [
        "Software Engineering",
        "Computer Science",
        "Information Technology",
        "Software Engineering",
        "Computer Science",
        "Information Technology",
        "Software Engineering",
        "Computer Science",
        "Information Technology",
        "Software Engineering",
        "Computer Science",
        "Information Technology",
        "Software Engineering",
        "Computer Science",
        "Information Technology",
        "Software Engineering",
        "Computer Science",
        "Information Technology",
        "Software Engineering",
        "Computer Science"
    ],

    "gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Male", "Female", "Male", "Female", "Male"
    ]
}

df = pd.DataFrame(data=data)
print(df.head())

print( df.tail())
print( df.shape)
print(df.describe())
print(df.info())
print (df.isnull())
print(df.isnull().sum())
df=df.drop_duplicates()
print("the size of the after remove deplication : " ,df.shape)
numeric_col=["age","study_hours","attendance","exam_score"]
df=df.fillna(df[numeric_col].median())
print( df.isnull().sum())
encoded_df=pd.get_dummies(
    df,columns=["department"],
    dtype=int
)

print(encoded_df)
standard_data=scaler.fit_transform()
df[numeric_col]
print(standard_data.head())
