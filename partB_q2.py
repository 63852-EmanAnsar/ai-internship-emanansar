
# Question 2: Indexing, Filtering,
import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Zain"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("========== ORIGINAL DATAFRAME ==========")
print(df)

# 1. Indexing


print("\n========== INDEXING ==========")

# Access a single column
print("\nName Column:")
print(df["Name"])

# Access multiple columns
print("\nName and Marks Columns:")
print(df[["Name", "Marks"]])

# Access a row using loc
print("\nRow with index 2:")
print(df.loc[2])

# Access a row using iloc
print("\nFirst Row:")
print(df.iloc[0])


# 2. Filtering


print("\n========== FILTERING ==========")

# Students with marks greater than 85
high_marks = df[df["Marks"] > 85]

print("\nStudents with Marks > 85:")
print(high_marks)

# Students whose age is 20
age20 = df[df["Age"] == 20]

print("\nStudents with Age = 20:")
print(age20)


# 3. Sorting


print("\n========== SORTING ==========")

# Sort by Marks
sorted_marks = df.sort_values(by="Marks")

print("\nSorted by Marks (Ascending):")
print(sorted_marks)

# Sort by Age in descending order
sorted_age = df.sort_values(by="Age", ascending=False)

print("\nSorted by Age (Descending):")
print(sorted_age)


# 4. Selection


print("\n========== SELECTION ==========")

# Select first three rows
print("\nFirst Three Rows:")
print(df.head(3))

# Select last two rows
print("\nLast Two Rows:")
print(df.tail(2))

# Select specific rows and columns
print("\nRows 1 to 3 and Columns Name & Marks:")
print(df.loc[1:3, ["Name", "Marks"]])

# Select using iloc
print("\nRows 0 to 2 and First Two Columns:")
print(df.iloc[0:3, 0:2])