# Titanic Dataset Analysis

## Dataset

This project analyzes the Titanic dataset using the Pandas library. The dataset contains information about passengers such as age, gender, passenger class, fare, and survival status.

## Data Cleaning Process

The following data cleaning steps were performed:

- Filled missing values in the Age column using the average age.
- Filled missing values in the Embarked column using the most common value.
- Renamed the Sex column to Gender for better readability.
- Removed the Cabin column because it contained many missing values.

## Analysis Performed

The project performs the following analyses:

- Reads the Titanic CSV dataset.
- Displays the first five rows of the dataset.
- Displays dataset information.
- Checks for missing values.
- Generates summary statistics.
- Counts passengers by gender.
- Counts passengers by passenger class.
- Counts survival status.
- Calculates the average age.
- Calculates the average fare.
- Calculates the average age by gender.
- Calculates the average fare by passenger class.
- Calculates the average survival rate by gender and passenger class.

## Key Findings

- Most passengers traveled in Third Class.
- Male passengers were more than female passengers.
- Missing values in the Age column were replaced with the average age.
- The Cabin column contained many missing values and was removed.
- Passenger class and gender influenced survival rates.

## Tools Used

- Python
- Pandas