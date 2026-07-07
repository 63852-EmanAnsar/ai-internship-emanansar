
# Question 4: Merge and Join DataFrames
import pandas as pd

# First DataFrame
students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"]
})

# Second DataFrame
marks = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Marks": [85, 90, 78, 92]
})

print("========== STUDENTS DATAFRAME ==========")
print(students)

print("\n========== MARKS DATAFRAME ==========")
print(marks)

# Merge DataFrames
merged_df = pd.merge(students, marks, on="StudentID")

print("\n========== MERGED DATAFRAME ==========")
print(merged_df)


# Join DataFrames

students_index = students.set_index("StudentID")
marks_index = marks.set_index("StudentID")

joined_df = students_index.join(marks_index)

print("\n========== JOINED DATAFRAME ==========")
print(joined_df)