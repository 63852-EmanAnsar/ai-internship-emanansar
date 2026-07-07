import pandas as pd


print("======PANDAS SERIES ======")

# Creating a Pandas Series
students = pd.Series(
    [85, 90, 78, 92, 88],
    index=["Ali", "Ahmed", "Sara", "Ayesha", "Zain"]
)

print("\nOriginal Series:")
print(students)

# Accessing an element
print("\nMarks of Sara:")
print(students["Sara"])

# Updating a value
students["Ali"] = 95

print("\nUpdated Series:")
print(students)

# Adding a new element
students["Hamza"] = 89

print("\nSeries after adding Hamza:")
print(students)

# =====================================
# DataFrame
# =====================================

print("\n========== DATAFRAME ==========")

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Zain"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

# Adding a new column
df["Grade"] = ["A", "A", "B", "A", "A"]

print("\nAfter Adding Grade Column:")
print(df)

# Updating data
df.loc[2, "Marks"] = 80

print("\nAfter Updating Sara's Marks:")
print(df)

# Adding a new row
df.loc[5] = ["Hamza", 21, 89, "A"]

print("\nAfter Adding a New Row:")
print(df)

# Deleting a column
df = df.drop("Age", axis=1)

print("\nAfter Deleting Age Column:")
print(df)