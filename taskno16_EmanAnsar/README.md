# Heart Disease Prediction using Machine Learning

## Project Overview

This project presents a complete end-to-end machine learning pipeline for predicting whether a patient is likely to have heart disease based on medical attributes. The project covers every stage of the machine learning workflow, including data preparation, preprocessing, exploratory data analysis (EDA), model development, evaluation, and prediction.

The objective is to build a reliable classification model that can assist in identifying patients at risk of heart disease.

---

# Dataset

**Dataset Name:** Heart Disease Dataset

The dataset contains medical information collected from patients. Each row represents one patient, while each column represents a medical feature used for prediction.

### Features

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG (restecg)
- Maximum Heart Rate Achieved (thalach)
- Exercise-Induced Angina (exang)
- ST Depression (oldpeak)
- Slope of ST Segment (slope)
- Number of Major Vessels (ca)
- Thalassemia (thal)

### Target Variable

- **target = 1** → Heart Disease Present
- **target = 0** → No Heart Disease

---

# Methodology

The project follows a standard machine learning pipeline consisting of the following steps:

### 1. Data Loading

- Loaded the Heart Disease dataset using Pandas.
- Checked the dataset shape and previewed the first few records.

### 2. Data Exploration

Performed exploratory data analysis to understand the dataset.

This included:

- Viewing dataset information
- Checking missing values
- Summary statistics
- Understanding feature distributions

### 3. Data Preprocessing

The following preprocessing steps were applied:

- Checked for missing values
- Separated features and target variable
- Split the dataset into training and testing sets
- Standardized numerical features using **StandardScaler**

### 4. Model Development

A machine learning classification model was trained on the processed dataset.

The pipeline included:

- Data preprocessing
- Feature scaling
- Model training
- Prediction on unseen test data

### 5. Model Evaluation

The trained model was evaluated using standard classification metrics.

Evaluation metrics included:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

# Implementation

The project was implemented using Python in Jupyter Notebook.

### Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

### Workflow

1. Import libraries
2. Load dataset
3. Explore the data
4. Preprocess the data
5. Split training and testing data
6. Scale features
7. Train the machine learning model
8. Predict test data
9. Evaluate model performance
10. Make sample predictions

---

# Results

The developed machine learning pipeline successfully classified patients based on their medical information.

The evaluation metrics demonstrated that the model achieved good predictive performance on the test dataset.

The confusion matrix and classification report showed that the model was capable of correctly identifying both patients with heart disease and patients without heart disease.

Overall, the pipeline produced reliable and consistent results.

---

# Conclusion

This project demonstrates the complete workflow of an end-to-end machine learning pipeline for heart disease prediction.

Key achievements include:

- Successful data preparation
- Effective preprocessing and feature scaling
- Model training and evaluation
- Accurate prediction of heart disease
- End-to-end implementation using Scikit-learn

The project illustrates how machine learning can be applied to healthcare data for disease prediction and decision support. With larger datasets and additional feature engineering, the model's performance could be further improved.

---



# Future Improvements

- Train multiple classification models for comparison.
- Perform hyperparameter tuning.
- Apply feature selection techniques.
- Deploy the model as a web application using Flask or Streamlit.
- Test the model on larger and more diverse datasets.

---

# Author

**Eman Ansar**

BS Computer Science

Riphah International University

AI Internship – Task 16