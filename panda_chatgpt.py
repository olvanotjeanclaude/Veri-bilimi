# Pandas Cheatsheet
"""
Introduction to Pandas
Pandas is a powerful Python library for data manipulation and analysis. 
It is primarily used for working with structured data, particularly 
data stored in tabular form (like CSV files, Excel spreadsheets, SQL databases, or other data formats). It provides easy-to-use data structures like DataFrame and Series, along with numerous functions that make data analysis tasks simpler.

Lesson 1: Introduction to Pandas
What is a DataFrame?
A DataFrame is a two-dimensional labeled data structure with columns of potentially
 different types. You can think of it like a table or a spreadsheet where each column
  is a different variable, and each row is a different observation or record.

What is a Series?
A Series is a one-dimensional array with labeled indices. It can be thought 
of as a single column in a DataFrame.
"""
import pandas as pd

# Lesson 1: Introduction to Pandas

# Creating DataFrame from a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# View the DataFrame
print(df)

# Basic DataFrame Operations
# View the first few rows of the DataFrame
print(df.head())

# Get summary statistics of the DataFrame
# print(df.describe())

# Get information about the DataFrame (data types, non-null counts)
# print(df.info())

# Lesson 2: Accessing Data

# Selecting Columns
# Accessing a single column
# print(df['Name'])

# Accessing multiple columns
# print(df[['Name', 'Age']])

# Row Accessing by Index
# Access by position (first row)
# print(df.iloc[0])

# Access by label (first row with index label 0)
# print(df.loc[0])

# Filtering Rows Based on Conditions
# Rows where Age is greater than 30
# print(df[df['Age'] > 30])

# Rows where City is 'Chicago'
# print(df[df['City'] == 'Chicago'])

# Lesson 3: Modifying DataFrames

# Adding New Columns
# Adding a new 'Salary' column
df['Salary'] = [50000, 60000, 70000]
# print(df)

# Renaming Columns
# Renaming 'Name' column to 'Full Name'
df.rename(columns={'Name': 'Full Name'}, inplace=True)
# print(df)

# Dropping Columns and Rows
# Dropping a column
# df.drop(columns=['City'], inplace=True)
# print(df)

# Dropping a row by index
# df.drop(index=1, inplace=True)  # Drops the second row
# print(df)

# Lesson 4: Handling Missing Data

# Creating DataFrame with missing values
data_with_missing = {
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_missing = pd.DataFrame(data_with_missing)
# print(df_missing)

# Checking for missing data
# print(df_missing.isnull())

# Filling missing data with a default value
import pandas as pd

# Creating DataFrame with missing values
data_with_missing = {
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_missing = pd.DataFrame(data_with_missing)

# Print the original DataFrame
# print(df_missing)

# Fill missing values in non-numeric columns
df_missing['Name'].fillna('Unknown', inplace=True)
df_missing['City'].fillna('Unknown', inplace=True)

# Fill missing values in the numeric 'Age' column with a numeric value (e.g., 0)
df_missing['Age'].fillna(0, inplace=True)

# Print the updated DataFrame
# print(df_missing)

df_missing.fillna('Unknown', inplace=True)
# print(df_missing)

# Dropping rows with missing data
# df_missing.dropna(inplace=True)
# print(df_missing)

# Lesson 5: Merging and Joining DataFrames

# Creating another DataFrame for merging
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Gender': ['F', 'M', 'M']
}
df2 = pd.DataFrame(data2)

# Merging DataFrames on a common column (Name)
merged_df = pd.merge(df, df2, on='Full Name')
# print(merged_df)

# Lesson 6: Grouping Data

# Grouping by a column and calculating the mean of other columns
grouped = df.groupby('City').mean()
# print(grouped)

# Lesson 7: Sorting Data

# Sorting by a column (ascending order)
# sorted_df = df.sort_values(by='Age')
# print(sorted_df)

# Sorting by multiple columns (ascending then descending)
# sorted_df_multi = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
# print(sorted_df_multi)

# Lesson 8: File I/O (Reading and Writing Data)

# Reading CSV file into DataFrame
# df_csv = pd.read_csv('data.csv')
# print(df_csv)

# Writing DataFrame to a CSV file
# df.to_csv('output.csv', index=False)

# Reading Excel file
# df_excel = pd.read_excel('data.xlsx')
# print(df_excel)

# Writing DataFrame to an Excel file
# df.to_excel('output.xlsx', index=False)

# Lesson 9: Advanced Operations

# Pivot Tables
# Create a pivot table
pivot_table = df.pivot_table(values='Salary', index='City', aggfunc='mean')
# print(pivot_table)

# Working with DateTime
# Convert a column to datetime
df['Date'] = pd.to_datetime(['2020-01-01', '2021-02-01', '2022-03-01'])
# print(df['Date'])

# Extract Year, Month, and Day from datetime
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
# print(df)

# Applying Functions to Columns
# Apply a function to a column
df['Age in 10 years'] = df['Age'].apply(lambda x: x + 10)
# print(df)
