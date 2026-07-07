import pandas as pd

print("========== TITANIC DATA ANALYSIS ==========\n")

# Read the dataset
df = pd.read_csv("titanic.csv")

# Display first five rows
print("First Five Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Data Cleaning
# -----------------------------

# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Embarked values with the most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove Cabin column because it contains many missing values
df = df.drop(columns=["Cabin"])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------
# Summary Statistics
# -----------------------------

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Exploratory Data Analysis
# -----------------------------

print("\nPassengers by Gender:")
print(df["Sex"].value_counts())

print("\nPassengers by Passenger Class:")
print(df["Pclass"].value_counts())

print("\nSurvival Count:")
print(df["Survived"].value_counts())

print("\nAverage Age:")
print(df["Age"].mean())

print("\nAverage Fare:")
print(df["Fare"].mean())

print("\nAverage Age by Gender:")
print(df.groupby("Sex")["Age"].mean())

print("\nAverage Fare by Passenger Class:")
print(df.groupby("Pclass")["Fare"].mean())

print("\nProject Completed Successfully!")