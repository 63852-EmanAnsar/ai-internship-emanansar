
# Question 3: GroupBy Operations
import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Zain", "Hamza"],
    "Department": ["CS", "IT", "CS", "IT", "CS", "IT"],
    "Marks": [85, 90, 78, 92, 88, 80],
    "Age": [20, 21, 19, 22, 20, 21]
}

df = pd.DataFrame(data)

print("========== ORIGINAL DATAFRAME ==========")
print(df)


# GroupBy Department

group = df.groupby("Department")

# Average Marks
print("\nAverage Marks by Department:")
print(group["Marks"].mean())

# Total Marks
print("\nTotal Marks by Department:")
print(group["Marks"].sum())

# Maximum Marks
print("\nHighest Marks by Department:")
print(group["Marks"].max())

# Minimum Marks
print("\nLowest Marks by Department:")
print(group["Marks"].min())

# Number of Students
print("\nNumber of Students in Each Department:")
print(group["Name"].count())

# Multiple Summary Statistics
print("\nComplete Summary:")
print(group["Marks"].agg(["mean", "sum", "max", "min", "count"]))