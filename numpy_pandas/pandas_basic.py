import pandas as pd
import numpy as np

# print(pd.__version__) # Printing pandas version

data = np.random.randint(10, 100, size=(40, 5))  # Generate random data for the DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])  # Create a DataFrame with the random data
print("DataFrame:\n", df.head(10))  # Print the DataFrame

dict_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
} # Create a dictionary with sample data

df = pd.DataFrame(dict_data)  # Create a DataFrame from the dictionary
print("DataFrame:\n", df)  # Print the DataFrame

print('\n')
# Series = A Pandas 1-Dimensional labeled array that can hold any data type
# Think of it like a single column in a spreadsheet (1-Dimensional)

arr = np.array([100, 150, 200, 250, 300])

series = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e'])

print(series)

calories = {'day1': 1650, 'day2': 1800, 'day3': 2100}

df1  = pd.Series(calories)

df1.loc['day2'] += 500 # Additional calories

print(df1[df1 > 2000])


employee_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
} # Create a dictionary with sample data

df2 = pd.DataFrame(employee_data, index=['E1', 'E2', 'E3', 'E4', 'E5'])

df2['Designation'] = ['Developer', 'Programmer', 'Founder', 'Manager', 'CEO'] # Added a new column

new_row = pd.DataFrame([{'Name': 'Lucas', 'Age': 22, 'City': 'California', 'Designation': 'Head-Manager'}], index=['E6']) # new row

df2 = pd.concat([df2, new_row]) # Added a new row

print(df2[df2['Age'] <= 30]) # Employee less than or equal to the age of 30

print(df2)
