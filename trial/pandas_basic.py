import pandas as pd
import numpy as np

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