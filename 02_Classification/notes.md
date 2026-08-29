# 📊 Classification – Notes

## What is Classification?

Classification is a **Supervised Machine Learning technique** used to predict a **categorical class or label**.

The model learns from labelled training data and predicts the class of new data.

### Example

Suppose we want to predict whether a customer will purchase a product.

| Age | Salary | Purchased |
|-----|--------|-----------|
| 22 | 25000 | 0 |
| 31 | 42000 | 1 |
| 41 | 62000 | 1 |

Here:

- Age and Salary → Features (X)
- Purchased → Target (y)
- 0 → Not Purchased
- 1 → Purchased

---

## Why is Classification Used?

Classification is used when the output is a **category or class** instead of a continuous numerical value.

### Examples

- Spam / Not Spam
- Pass / Fail
- Yes / No
- Purchased / Not Purchased
- Disease / No Disease
- Cat / Dog

---

# Types of Classification

## 1. Binary Classification

Binary Classification has **only two classes**.

### Examples

- Yes / No
- Pass / Fail
- Spam / Not Spam
- 0 / 1

In our practical:

- 0 → Not Purchased
- 1 → Purchased

Therefore, our practical is a **Binary Classification** problem.

---

## 2. Multiclass Classification

Multiclass Classification has **more than two classes**.

### Example

- Cat
- Dog
- Horse

Here, the model predicts one class from multiple possible classes.

---

## 3. Multilabel Classification

In Multilabel Classification, one observation can belong to **multiple classes at the same time**.

### Example

A movie can have multiple genres:

- Action
- Comedy
- Thriller

Therefore, one movie can have multiple labels.

---

# Features and Target

## Features (X)

Features are the input variables used by the model to make predictions.

Example:

- Age
- Salary

## Target (y)

Target is the output variable or class that the model needs to predict.

Example:

- Purchased

---

# Class Distribution

Class Distribution tells us how many observations belong to each class.

Example:

- Class 0 → 15 records
- Class 1 → 5 records

It is important to check class distribution because an unequal distribution can lead to an **imbalanced dataset**.

---

# Classification Workflow

Dataset

↓

Data Preprocessing

↓

Features (X) + Target (y)

↓

Train-Test Split

↓

Train Classification Model

↓

Make Predictions

↓

Evaluate Model

---

# Visualization

Classification data can be visualized using:

- Scatter Plot
- Bar Chart
- Confusion Matrix
- Decision Boundary

In our practical, we used a **Scatter Plot** to visualize:

- Age → X-axis
- Salary → Y-axis
- Purchased / Not Purchased → Different classes

---

# Important Classification Algorithms

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree
4. Random Forest
5. Support Vector Machine (SVM)
6. Naive Bayes

---

# Interview Questions

### Q1. What is Classification?

Classification is a Supervised Machine Learning technique used to predict categorical or discrete class labels.

### Q2. What is Binary Classification?

Binary Classification is a classification problem with exactly two classes.

Example: Spam / Not Spam.

### Q3. What is Multiclass Classification?

Multiclass Classification is a classification problem where the target contains more than two classes.

### Q4. What is Multilabel Classification?

Multilabel Classification allows one observation to belong to multiple classes simultaneously.

### Q5. Is Classification supervised or unsupervised learning?

Classification is a **Supervised Learning** technique because the model learns from labelled data.

### Q6. What are Features and Target?

Features are input variables used for prediction, while the target is the output variable that the model predicts.

---

# Summary

- Classification is a **Supervised Machine Learning** technique.
- It predicts categorical class labels.
- Binary Classification has two classes.
- Multiclass Classification has more than two classes.
- Multilabel Classification can have multiple labels for one observation.
- Features are represented by X.
- Target is represented by y.
- Class Distribution shows the number of observations in each class.
- Classification is widely used for prediction problems.

---

## Status

- Topic: Classification Introduction
- Practical: Python + Jupyter Notebook
- Dataset: Customer Purchase Dataset
- Visualization: Scatter Plot
- Status: ✅ Completed