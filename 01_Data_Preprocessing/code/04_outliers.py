"""
Topic: Handling Outliers
Author: Pooja Goswami
Repository: Machine Learning Journey

Techniques Covered:

1. IQR Method
2. Z-Score Method
3. Outlier Detection
4. Outlier Removal
5. Box Plot Visualization
"""
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import zscore
# Load Dataset

df = pd.read_csv("../datasets/04_outliers.csv")

print("Original Dataset:")
print(df)


# -------------------------------
# IQR Method
# -------------------------------

Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Detect Outliers

outliers = df[
    (df["salary"] < lower_bound) |
    (df["salary"] > upper_bound)
]

print("\nOutliers:")
print(outliers)

# -------------------------------
# Remove Outliers using IQR
# -------------------------------

df_iqr = df[
    (df["salary"] >= lower_bound) &
    (df["salary"] <= upper_bound)
]

print("\nDataset after removing outliers using IQR:")
print(df_iqr)

# -------------------------------
# Z-Score Method
# -------------------------------

df["z_score"] = zscore(df["salary"])

print("\nZ-Scores:")
print(df[["salary", "z_score"]])

# Detect Outliers using Z-Score

z_score_outliers = df[
    abs(df["z_score"]) > 3
]

print("\nOutliers using Z-Score:")
print(z_score_outliers)


# -------------------------------
# Box Plot Visualization
# -------------------------------

plt.figure(figsize=(8, 5))

plt.boxplot(df["salary"])

plt.title("Salary Distribution - Outlier Detection")
plt.ylabel("Salary")

plt.show()