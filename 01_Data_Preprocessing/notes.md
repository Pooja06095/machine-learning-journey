# 📝 Missing Value Imputation Notes

## What is Missing Value?

Missing values are the data points that are not available or are empty (`NaN`, `NULL`, or blank) in a dataset. These missing values can reduce the accuracy of a Machine Learning model if not handled properly.

---

## Why Handle Missing Values?

- Improves model accuracy.
- Prevents errors during training.
- Makes the dataset complete.
- Helps algorithms learn better patterns.

---

## Types of Missing Value Imputation

### 1. Mean Imputation

Replace missing numerical values with the **mean (average)** of the column.

**Best For:** Normally distributed numerical data.

**Advantages**
- Simple and fast.
- Easy to implement.

**Disadvantages**
- Sensitive to outliers.
- May change the data distribution.

---

### 2. Median Imputation

Replace missing numerical values with the **median** of the column.

**Best For:** Skewed data or datasets with outliers.

**Advantages**
- Robust to outliers.
- Preserves the central tendency.

**Disadvantages**
- Ignores relationships between features.

---

### 3. Mode Imputation

Replace missing values with the **most frequent value** in the column.

**Best For:** Categorical data.

**Advantages**
- Easy to apply.
- Suitable for categorical features.

**Disadvantages**
- May introduce bias if one category dominates.

---

### 4. Random Sampling Imputation

Replace missing values by randomly selecting existing values from the same column.

**Best For:** Preserving the original data distribution.

**Advantages**
- Maintains data variability.
- Reduces bias compared to mean or median.

**Disadvantages**
- Results may vary because of randomness.

---

## Python Functions Used

- `isnull()`
- `fillna()`
- `mean()`
- `median()`
- `mode()`
- `sample()`

---

## Real-World Example

Suppose a company has employee salary data, but some salary values are missing.

- Mean → Replace with average salary.
- Median → Better if some employees have extremely high salaries.
- Mode → Used for missing department or city values.
- Random Sampling → Keeps the data distribution close to the original.

---

## Interview Questions

### Q1. What is Missing Value Imputation?
It is the process of replacing missing values with suitable values instead of removing the data.

### Q2. Which imputation method is best for categorical data?
Mode Imputation.

### Q3. Which method is less affected by outliers?
Median Imputation.

### Q4. Which method preserves the original data distribution?
Random Sampling Imputation.

---

## Summary

- Missing values must be handled before training a Machine Learning model.
- Mean is suitable for normal numerical data.
- Median is suitable for skewed data.
- Mode is suitable for categorical data.
- Random Sampling helps preserve the original distribution of data.

## Status

✅ Completed on: 27 July 2026