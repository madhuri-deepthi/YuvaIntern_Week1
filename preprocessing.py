import pandas as pd
import numpy as np

# Sample dataset
data = {
    "Name": ["Anu", "Ravi", "Sita", "John", "Priya"],
    "Age": [21, 22, np.nan, 23, 21],
    "Gender": ["Female", "Male", "Female", "Male", np.nan],
    "Marks": [85, 78, 92, np.nan, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Handle missing numerical values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Handle missing categorical values
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

# Encode categorical data
df["Gender"] = df["Gender"].map({"Female": 0, "Male": 1})

# Normalize Marks
df["Marks_Normalized"] = (
    (df["Marks"] - df["Marks"].min()) /
    (df["Marks"].max() - df["Marks"].min())
)

print("\nCleaned and Preprocessed Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())