"""
Topic: Train-Test Split
Author: Pooja Goswami
Repository: Machine Learning Journey

Techniques Covered:

1. Train-Test Split
2. Feature and Target Separation
3. Training and Testing Data
4. Dataset Size Comparison
"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Load Dataset

df = pd.read_csv("../datasets/06_train_test_split.csv")

print("Original Dataset:")
print(df)

# Separate Features and Target

X = df.drop("purchased", axis=1)
y = df["purchased"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Display Training Data

print("\nTraining Features:")
print(X_train)

print("\nTraining Target:")
print(y_train)

# Display Testing Data

print("\nTesting Features:")
print(X_test)

print("\nTesting Target:")
print(y_test)

# Dataset Size Comparison

print("\nDataset Size:")
print("Original Dataset:", len(df))
print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))