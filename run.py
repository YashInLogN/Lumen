import numpy as np
import pandas as pd

# data = np.abs(np.random.randn(100, 3))   Generate random data
# df = pd.DataFrame(data, columns=['A', 'B', 'C'])  Display the first few rows of the DataFrame
# print(df)

# print("\nSummary Statistics:")
# print(df.describe())   Display summary statistics of the DataFrame

arr = np.array([1, 2, 3, 4, 5])

print("Slicing: ", arr[1: 4])  # Calculate and print the mean of the array

print("Filtering: ", arr[arr>1])  # Filter and print elements greater than 1

print("Original Array: ", arr)
print("Shape of Array: ", arr.shape)  # Print the shape of the array

arr = arr.reshape(5, 1)  # Reshape the array to a 5x1 matrix

print("Reshaped Array: ", arr)

print("Shape of Reshaped Array: ", arr.shape)  # Print the shape of the reshaped array

for r, values in np.ndenumerate(arr):  # Iterate over the array and print the index and value of each element
    print(f"Index: {r}, Value: {values}")


data = np.array([[1, 2, 3], [4, 5, 6]])
dt = data.flatten()  # Flatten the array
print("Flattened Array: ", dt)

# new_arr = np.array([1, 2, 3, 4, 5])
# print("Original Array: ", new_arr)
# new_arr = new_arr.astype(float)   Convert the array to float type
# new_arr = np.insert(new_arr, 1, 1.5)   Insert a new element into the array
# print("Array after insertion: ", new_arr)

square_arr = np.array([[1, 2], [3, 4]])
square_arr = square_arr.astype(float)  # Convert the array to float type
new_col = np.array([0, 1.5])
square_arr = np.insert(square_arr, 2, new_col, axis=1)  # Insert a new row into the array
print("Array after insertion: ", square_arr)

arr_1 = np.array([1, 2, 3])
arr_2 = np.array([5, 4, 3])
arr_3 = np.array([5, 4, 3])
result = np.concatenate((arr_1, arr_2, arr_3))  # Perform element-wise
print("Concatenated Array: ", result)

arr_2d = np.array([[1, 2], [3, 4]])
mdf_arr = np.delete(arr_2d, 1, axis=1)  # Delete the second column from the 2D array
print("Array after deletion: ", mdf_arr)

# horizontal stacking & vertical stacking
arr_h1 = np.array([[1, 2], [3, 4]])
arr_h2 = np.array([[5, 6], [7, 8]])
hstacked_arr = np.hstack((arr_h1, arr_h2))  # Horizontally stack the two arrays
print("Horizontally Stacked Array: ", hstacked_arr) 
arr_v1 = np.array([[1, 2], [3, 4]])
arr_v2 = np.array([[5, 6], [7, 8]])
vstacked_arr = np.vstack((arr_v1, arr_v2))  # Vertically stack the two arrays
print("Vertically Stacked Array: ", vstacked_arr)

# linear split & horizontal split & vertical split
arr_split = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linear_split = np.array_split(arr_split, 3)  # Split the array into 3 equal parts
print("Linear Split: ", linear_split)
h_split = np.hsplit(arr_split, 3)  # Horizontally split the array into 3 equal parts
print("Horizontal Split: ", h_split)
v_split = np.vsplit(arr_split, 3)  # Vertically split the array into 3 equal parts
print("Vertical Split: ", v_split)

a = 5
b = 10

print('A bigger') if a > b else print('B bigger')  # Use a conditional expression to print which variable is bigger


num = np.linspace(0, 10, 5)  # Generate an array of 5 evenly spaced numbers between 0 and 10
print("Linearly Spaced Array: ", num)