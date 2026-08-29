"""
Topic: Classification Introduction
Author: Pooja Goswami
Repository: Machine Learning Journey

Concepts Covered:
1. Classification
2. Features and Target
3. Binary Classification
4. Class Distribution
5. Data Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt


# Load Dataset

df = pd.read_csv("../datasets/01_classification_introduction.csv")

print("Dataset:")
print(df)


# Separate Features and Target

X = df[["age", "salary"]]
y = df["purchased"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)


# Class Distribution

print("\nClass Distribution:")
print(y.value_counts())


# Visualization

plt.scatter(
    df[df["purchased"] == 0]["age"],
    df[df["purchased"] == 0]["salary"],
    label="Not Purchased"
)

plt.scatter(
    df[df["purchased"] == 1]["age"],
    df[df["purchased"] == 1]["salary"],
    label="Purchased"
)

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Binary Classification Example")
plt.legend()

plt.show()