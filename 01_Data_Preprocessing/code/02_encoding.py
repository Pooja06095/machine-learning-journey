"""
Topic: Encoding
Author: Pooja Goswami
Repository: Machine Learning Journey

Techniques Covered:

1. Label Encoding
2. One-Hot Encoding
3. Ordinal Encoding
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

# Load Dataset

df = pd.read_csv("../datasets/02_encoding.csv")

print("Original Dataset:")
print(df)



# Label Encoding

label_encoder = LabelEncoder()

df_label = df.copy()

df_label["gender"] = label_encoder.fit_transform(df_label["gender"])

print("\nLabel Encoded Data:")
print(df_label)



# One-Hot Encoding

df_onehot = df.copy()

one_hot = pd.get_dummies(df_onehot, columns=["city"], dtype=int)

print("\nOne-Hot Encoded Data:")
print(one_hot)




# Ordinal Encoding

df_ordinal = df.copy()

ordinal_encoder = OrdinalEncoder(
    categories=[["School", "College", "PhD"]]
)

df_ordinal[["education"]] = ordinal_encoder.fit_transform(
    df_ordinal[["education"]]
)

print("\nOrdinal Encoded Data:")
print(df_ordinal)