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



# Encoding

## What is Encoding?

Encoding is a data preprocessing technique used to convert categorical data into numerical values so that Machine Learning algorithms can understand and process the data.

---

## Why is Encoding Required?

Machine Learning algorithms work with numerical data, not text values.

Example:

Male, Female ❌

↓

1, 0 ✅

---

## Types of Encoding

### 1. Label Encoding

Assigns a unique integer to each category.

Example:

Male → 1

Female → 0

#### Best Used For

- Binary categorical features
- Target labels

#### Advantages

- Simple and fast
- Easy to implement

#### Disadvantages

- May create an artificial order between categories.

---

### 2. One-Hot Encoding

Creates a separate binary column for each category.

Example:

City

Delhi

Mumbai

Pune

↓

city_Delhi | city_Mumbai | city_Pune

1 | 0 | 0

0 | 1 | 0

0 | 0 | 1

#### Best Used For

- Nominal categorical data
- Features with no natural order

#### Advantages

- No false ordering between categories.
- Most commonly used encoding technique.

#### Disadvantages

- Creates many new columns if categories are large.

---

### 3. Ordinal Encoding

Assigns numbers according to the natural order of categories.

Example:

School → 0

College → 1

PhD → 2

#### Best Used For

- Ordered categorical data

#### Advantages

- Preserves category order.
- Simple and efficient.

#### Disadvantages

- Works only when categories have a meaningful order.

---

## Comparison

| Technique | Best For |
|-----------|----------|
| Label Encoding | Binary Data / Target Labels |
| One-Hot Encoding | Nominal Data |
| Ordinal Encoding | Ordered Categories |

---

## Dataset Used

Columns:

- id
- city
- gender
- education

---

## Libraries Used

- pandas
- scikit-learn

---

## Conclusion

Encoding converts categorical values into numerical form before training Machine Learning models.

Selecting the correct encoding technique improves model performance and avoids misleading relationships between categories.
---

## Status

- ✅ Completed on: 28 July 2026
- 📚 Module: Data Preprocessing
- 📖 Topic: Encoding
- 🔢 Topic Number: 02
- 🐍 Language: Python
- 📦 Libraries: pandas, scikit-learn



# Feature Scaling

## Definition

Feature Scaling is a data preprocessing technique used to bring numerical features to a similar scale. It helps Machine Learning algorithms perform better by preventing features with larger values from dominating those with smaller values.

---

## Why Feature Scaling?

Suppose we have:

Age = 25

Salary = 75000

Here, Salary has much larger values than Age.

Many Machine Learning algorithms such as KNN, K-Means, SVM, Logistic Regression, and Gradient Descent are affected by the difference in feature scales.

Feature Scaling solves this problem by converting features into a comparable range.

---

# Types of Feature Scaling

## 1. Standardization (Z-Score Scaling)

### Formula

Z = (X - Mean) / Standard Deviation

### Characteristics

- Mean becomes 0
- Standard Deviation becomes 1
- Values are not limited to a fixed range

### Advantages

- Works well for normally distributed data
- Commonly used in Machine Learning

### Disadvantages

- Sensitive to outliers

---

## 2. Min-Max Scaling

### Formula

(X - Min) / (Max - Min)

### Characteristics

- Converts values into the range of 0 to 1

### Advantages

- Easy to understand
- Preserves the original distribution

### Disadvantages

- Highly affected by outliers

---

## 3. Robust Scaling

### Formula

(X - Median) / IQR

Where,

IQR = Q3 - Q1

### Characteristics

- Uses Median instead of Mean
- Uses Interquartile Range (IQR)

### Advantages

- Works well with outliers
- More robust than Standardization

### Disadvantages

- Does not scale values into a fixed range

---

## 4. Normalization

### Formula

X = X / √(x₁² + x₂² + x₃² + ...)

### Characteristics

- Converts each row into unit length
- Each sample has magnitude equal to 1

### Advantages

- Useful for Cosine Similarity
- Used in Text Mining and KNN

### Disadvantages

- Not suitable for every Machine Learning algorithm

---

# Comparison

| Technique | Range | Outlier Handling | Best For |
|-----------|-------|-----------------|----------|
| Standardization | No fixed range | ❌ Sensitive | Normal Distribution |
| Min-Max Scaling | 0 to 1 | ❌ Sensitive | Neural Networks |
| Robust Scaling | No fixed range | ✅ Good | Data with Outliers |
| Normalization | Unit Length | Depends | Text Mining, KNN |

---

# Interview Questions

### What is Feature Scaling?

Feature Scaling is the process of transforming numerical features into a similar scale to improve Machine Learning model performance.

### Why do we use Feature Scaling?

To prevent features with larger values from dominating features with smaller values.

### Which scaler is best for data with outliers?

RobustScaler.

### Which scaler converts values between 0 and 1?

MinMaxScaler.

### Which scaler makes Mean = 0 and Standard Deviation = 1?

StandardScaler.

### Which scaler is commonly used for Text Mining?

Normalizer.

---

## Libraries Used

- pandas
- sklearn.preprocessing

---

## Status

✅ Completed on: 04 August 2026




# Handling Outliers

## Definition

An outlier is a data point that is significantly different from the other observations in a dataset.

Outliers may occur because of:

- Data entry errors
- Measurement errors
- Experimental errors
- Genuine unusual observations

Outliers can negatively affect Machine Learning models, especially algorithms that depend on mean, variance, or distance.

---

## Why Handle Outliers?

Outliers can:

- Distort the mean and standard deviation.
- Affect statistical analysis.
- Influence Machine Learning model performance.
- Cause inaccurate predictions.
- Affect distance-based algorithms.

Therefore, detecting and handling outliers is an important part of Data Preprocessing.

---

# Methods for Detecting Outliers

## 1. IQR Method

IQR stands for Interquartile Range.

### Formula

IQR = Q3 - Q1

Where:

- Q1 = First Quartile (25th percentile)
- Q3 = Third Quartile (75th percentile)

### Lower Bound

Lower Bound = Q1 - 1.5 × IQR

### Upper Bound

Upper Bound = Q3 + 1.5 × IQR

Any value:

- Below the Lower Bound, or
- Above the Upper Bound

is considered an outlier.

### Advantages

- Simple and easy to understand.
- Does not require normally distributed data.
- Less affected by extreme values.

### Disadvantages

- The 1.5 × IQR rule may not be suitable for every dataset.

---

## 2. Z-Score Method

Z-Score measures how far a data point is from the mean in terms of standard deviations.

### Formula

Z = (X - Mean) / Standard Deviation

Generally:

|Z| > 3

is considered an outlier.

### Advantages

- Simple mathematical method.
- Useful for normally distributed data.
- Shows how far an observation is from the mean.

### Disadvantages

- Sensitive to extreme values.
- Works best when data is approximately normally distributed.

---

# Outlier Removal

After detecting outliers, they can be removed from the dataset.

For the IQR method, only values within the lower and upper bounds are retained.

Example:

```python
df_iqr = df[
    (df["salary"] >= lower_bound) &
    (df["salary"] <= upper_bound)
]

## Status

✅ Completed on: 04 August 2026



# Handling Imbalanced Data

## Definition

Imbalanced data occurs when the classes in a classification dataset are not equally distributed.

Example:

* Class 0 → 20 samples
* Class 1 → 2 samples

Here, Class 0 is the **majority class** and Class 1 is the **minority class**.

Highly imbalanced data can make a Machine Learning model biased toward the majority class.

---

## Why Handle Imbalanced Data?

Imbalanced data can:

* Make the model biased toward the majority class.
* Reduce the model's ability to correctly identify the minority class.
* Produce misleading accuracy.
* Affect classification performance.

Therefore, handling imbalanced data is an important part of Data Preprocessing.

---

# Techniques for Handling Imbalanced Data

## 1. Random Over Sampling

Random Over Sampling increases the number of minority-class samples by randomly selecting and duplicating existing minority samples.

### Example

Before:

```text
Class 0 → 20
Class 1 → 2
```

After Over Sampling:

```text
Class 0 → 20
Class 1 → 20
```

### Advantages

* Simple and easy to implement.
* Does not remove majority-class data.
* Useful for small datasets.

### Disadvantages

* May cause overfitting.
* Duplicate samples do not add new information.

---

## 2. Random Under Sampling

Random Under Sampling reduces the number of majority-class samples by randomly removing some of them.

### Example

Before:

```text
Class 0 → 20
Class 1 → 2
```

After Under Sampling:

```text
Class 0 → 2
Class 1 → 2
```

### Advantages

* Reduces dataset size.
* Faster model training.
* Easy to implement.

### Disadvantages

* May remove useful information.
* Can reduce the overall amount of training data.

---

## 3. SMOTE

SMOTE stands for **Synthetic Minority Oversampling Technique**.

It creates new synthetic samples for the minority class instead of simply duplicating existing samples.

### Example

Before:

```text
Class 0 → 20
Class 1 → 2
```

After SMOTE:

```text
Class 0 → 20
Class 1 → 20
```

### Advantages

* Creates synthetic minority samples.
* Does not simply duplicate existing samples.
* Helps reduce overfitting compared to simple Random Over Sampling.

### Disadvantages

* May create noisy or less useful synthetic samples.
* Requires sufficient minority-class samples.
* Can increase computational cost.

### Important Parameter

```python
SMOTE(k_neighbors=1, random_state=42)
```

`k_neighbors` determines the number of neighboring minority samples used to generate synthetic samples.

In our dataset, only 2 minority samples were available, so `k_neighbors=1` was used.

---

# Class Distribution Comparison

| Technique             | Class 0 | Class 1 |
| --------------------- | ------- | ------- |
| Original              | 20      | 2       |
| Random Over Sampling  | 20      | 20      |
| Random Under Sampling | 2       | 2       |
| SMOTE                 | 20      | 20      |

---

# Comparison

| Technique             | Main Idea                         | Advantage             | Disadvantage             |
| --------------------- | --------------------------------- | --------------------- | ------------------------ |
| Random Over Sampling  | Duplicate minority samples        | Keeps majority data   | May cause overfitting    |
| Random Under Sampling | Remove majority samples           | Reduces dataset size  | May lose information     |
| SMOTE                 | Create synthetic minority samples | Generates new samples | May create noisy samples |

---

# Python Libraries Used

* pandas
* matplotlib
* scikit-learn
* imbalanced-learn

### Functions / Classes Used

* `resample()`
* `SMOTE()`
* `value_counts()`
* `pd.concat()`
* `DataFrame()`
* `plot()`

---

# Interview Questions

### Q1. What is Imbalanced Data?

Imbalanced data is a dataset where one class has significantly more samples than another class.

### Q2. What is the majority class?

The class having a larger number of samples is called the majority class.

### Q3. What is the minority class?

The class having fewer samples is called the minority class.

### Q4. What is Random Over Sampling?

It increases minority-class samples by randomly duplicating existing minority samples.

### Q5. What is Random Under Sampling?

It reduces majority-class samples by randomly removing some majority samples.

### Q6. What is SMOTE?

SMOTE stands for **Synthetic Minority Oversampling Technique**. It creates synthetic samples for the minority class.

### Q7. What is the difference between Over Sampling and SMOTE?

Random Over Sampling duplicates existing minority samples, while SMOTE generates new synthetic minority samples.

### Q8. Which technique may cause loss of information?

Random Under Sampling, because it removes majority-class samples.

### Q9. Which technique may cause overfitting due to duplicate samples?

Random Over Sampling.

---

# Key Takeaways

* Imbalanced data occurs when classes have unequal numbers of samples.
* Majority class has more samples.
* Minority class has fewer samples.
* Random Over Sampling duplicates minority samples.
* Random Under Sampling removes majority samples.
* SMOTE generates synthetic minority samples.
* Under Sampling may cause information loss.
* Over Sampling may cause overfitting.
* SMOTE is commonly used for handling imbalanced classification data.

---

## Status

✅ Completed on: 20 August 2026
