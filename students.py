import pandas as pd

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("./csv_files/students.csv")

## Explore the data ##

# 1.Display the first 5 rows of the dataset.
# print(data.head(5))

## Perform analysis ##

# 2.Calculate the average age of the students.
average_age_students = data["Age"].mean()
print(f"Average age of students is: {average_age_students}")

# 3.Filter the dataset to include only female students.
female_students = data[data["Gender"] == "Female"]
print(female_students)

# 4.Calculate the maximum score achieved by any student.
max_score = data["Score"].max()
print(f"Maximum score is: \n{max_score}")

# 5.Create a new column called 'Pass' that indicates whether a student passed or failed based on a score of 60 or higher.
data['Pass'] = data['Score'] >= 60

# 6.Convert the boolean values to 'Pass' and 'Fail' using map() function
data['Pass'] = data['Pass'].map({True: 'Pass', False: 'Fail'})

# 7.Save the modified dataset to a new CSV file called 'students_modified.csv'
data.to_csv("./csv_files/updated_students.csv")

print(data)