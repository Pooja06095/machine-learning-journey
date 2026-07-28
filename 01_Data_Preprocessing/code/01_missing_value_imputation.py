"""
Topic: Missing Value Imputation
Author: Pooja Goswami
Repository: Machine Learning Journey

Techniques Covered:
1. Mean Imputation
2. Median Imputation
3. Mode Imputation
4. Random Sampling Imputation
"""


# Data imputation with Visualization
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer

# 1. Create sample dataset
data= {
    "id" : [1,2,3,4,5,6], 
    "age" : [25,np.nan,30,35,np.nan,100],      # include Nan value
    "salary" : [50000, 60000, np.nan, 80000, 90000, np.nan],
    "city" : ["New York", "London", np.nan, "Paris", "London", np.nan]
}
df= pd.DataFrame(data)
print("original Data:")
print(df)


# 2. Mean Imputation
mean_imputer = SimpleImputer(strategy="mean")
df_mean = df.copy()
df_mean[['age', 'salary']] = mean_imputer.fit_transform (df_mean[['age','salary']])
print('\nMean Imputed Data:')
print(df_mean)



# 3. Median Imputation
median_imputer = SimpleImputer(strategy="median")
df_median = df.copy()
df_median[['age', 'salary']] = median_imputer.fit_transform (df_median[['age','salary']])
print('\nMedian Imputed Data:')
print(df_median)



# 4. Mode Imputation(works for both num + cat)
mode_imputer = SimpleImputer(strategy="most_frequent")
df_mode = df.copy()
df_mode[['age', 'salary','city']] = mode_imputer.fit_transform (df_mode[['age','salary','city']])
print('\nMode Imputed Data:')
print(df_mode)



# 5. Random Sampling Imputation
df_random =df.copy()
def random_impute(series):
    # Drop Nan Values to avoid errors
    filled = series.dropna().tolist()
    return series.apply(lambda x: random.choice(filled)
    if pd.isnull(x) else x)
for col in ['age', 'salary', 'city']:
    df_random[col] = random_impute(df_random[col])

print("\nRandom Sampling Imputed Data:")
print(df_random)