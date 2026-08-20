"""
Topic: Handling Imbalanced Data
Author: Pooja Goswami
Repository: Machine Learning Journey

Techniques Covered:

1. Random Over Sampling
2. Random Under Sampling
3. SMOTE
4. Class Distribution Comparison
"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.utils import resample
from imblearn.over_sampling import SMOTE

# Load Dataset

df = pd.read_csv("../datasets/05_imbalanced_data.csv")

print("Original Dataset:")
print(df)

# Check Class Distribution

print("\nOriginal Class Distribution:")
print(df["purchased"].value_counts())

# -------------------------------
# Random Over Sampling
# -------------------------------

majority_class = df[df["purchased"] == 0]
minority_class = df[df["purchased"] == 1]

minority_oversampled = resample(
    minority_class,
    replace=True,
    n_samples=len(majority_class),
    random_state=42
)

oversampled_df = pd.concat(
    [majority_class, minority_oversampled]
)

print("\nClass Distribution After Random Over Sampling:")
print(oversampled_df["purchased"].value_counts())


# Random Under Sampling
majority_undersampled = resample(
    majority_class,
    replace= False,
    n_samples=len(minority_class),
    random_state=42
)

undersampled_df = pd.concat(
    [majority_undersampled, minority_class]
)
print("\nClass Distribution After Random Under Sampling:")
print(undersampled_df["purchased"].value_counts())


# -------------------------------
# SMOTE (Synthetic Minority Oversampling Technique)
# -------------------------------

X = df.drop("purchased", axis=1)
y = df["purchased"]

smote = SMOTE(k_neighbors=1, random_state=42)

X_smote, y_smote = smote.fit_resample(X, y)

print("\nClass Distribution After SMOTE:")
print(y_smote.value_counts())

# -------------------------------
# Class Distribution Comparison
# -------------------------------

original_counts = df["purchased"].value_counts().sort_index()
oversampled_counts = oversampled_df["purchased"].value_counts().sort_index()
undersampled_counts = undersampled_df["purchased"].value_counts().sort_index()
smote_counts = y_smote.value_counts().sort_index()

comparison = pd.DataFrame({
    "Original": original_counts,
    "Over Sampling": oversampled_counts,
    "Under Sampling": undersampled_counts,
    "SMOTE": smote_counts
})

print("\nClass Distribution Comparison:")
print(comparison)

# Plot Comparison

comparison.plot(kind="bar")

plt.title("Class Distribution Comparison")
plt.xlabel("Purchased Class")
plt.ylabel("Number of Samples")
plt.xticks(rotation=0)
plt.legend()
plt.tight_layout()
plt.show()