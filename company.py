import pandas as pd

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("./csv_files/company.csv")

# Explore the data
# print(data.head(5)) # Display the first five few rows
# print(data.describe())
# print(data.info())

## Perform analysis ##

# 1.Calculate the average age of employees.
average_employee_age = data["Age"].mean()
print(f"Average age in the company is: {average_employee_age}")

# 2.Find the maximum salary in the "Finance" department.
max_salary_finance = data[data["Department"].str.startswith("Finance")]["Salary"].max()
print(f"Highest salary in finance department: {max_salary_finance}")

# 3.Create a new column called "Salary Increase" by increasing each employee's salary by 10%.
data['Salary Increase'] = data['Salary'] * 0.1
#print(f"Updated DataFrame: \n{data}")

# 4.Updated salary and changing Dtype from float to int
data['New Salary'] = data["Salary"] + data["Salary Increase"]
data['New Salary'] = data['New Salary'].astype("int")
#print(f"Updated DataFrame: \n{data}")

# 5.Sort the DataFrame by the "Salary Increase" column in descending order.
sorted_df = data.sort_values(by='Salary Increase', ascending=False)
print(sorted_df)

# 6.Export the updated DataFrame to a new CSV file.
data.to_csv('./csv_files/updated_data.csv', index=False)
