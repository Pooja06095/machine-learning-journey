"""
Topic: Feature Scaling
Author: Pooja Goswami
Repository: Machine Learning Journey

Techniques Covered:

1. Standardization
2. Min-Max Scaling
3. Robust Scaling
4. Normalization
"""
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer

# Load Dataset

df = pd.read_csv("../datasets/03_feature_scaling.csv")

print("Original Dataset:")
print(df)


# -------------------------------
# Standardization
# -------------------------------

standard_scaler = StandardScaler()

standard_scaled = standard_scaler.fit_transform(
    df[["age", "salary", "height", "weight"]]
)

standard_df = pd.DataFrame(
    standard_scaled,
    columns=["age", "salary", "height", "weight"]
)

print("\nStandardized Data:")
print(standard_df)

standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(
    df[["age", "salary", "height", "weight"]]
)

standard_df = pd.DataFrame(
    standard_scaled,
    columns=["age", "salary", "height", "weight"]
)


# -------------------------------
# Min-Max Scaling
# -------------------------------

minmax_scaler = MinMaxScaler()

minmax_scaled = minmax_scaler.fit_transform(
    df[["age", "salary", "height", "weight"]]
)

minmax_df = pd.DataFrame(
    minmax_scaled,
    columns=["age", "salary", "height", "weight"]
)

print("\nMin-Max Scaled Data:")
print(minmax_df)


# -------------------------------
# Robust Scaling
# -------------------------------

robust_scaler = RobustScaler()

robust_scaled = robust_scaler.fit_transform(
    df[["age", "salary", "height", "weight"]]
)

robust_df = pd.DataFrame(
    robust_scaled,
    columns=["age", "salary", "height", "weight"]
)

print("\nRobust Scaled Data:")
print(robust_df)


# -------------------------------
# Normalization
# -------------------------------

normalizer = Normalizer()

normalized_data = normalizer.fit_transform(
    df[["age", "salary", "height", "weight"]]
)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=["age", "salary", "height", "weight"]
)

print("\nNormalized Data:")
print(normalized_df)