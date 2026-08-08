import numpy as np
import pandas as pd

arr = np.arange(10, 1000000, 1000)

discount = 0.4

arr = arr * (1 - discount)  # Apply the discount to the array
df = pd.DataFrame(arr, columns=['Discounted Price'])  # Create a DataFrame from the discounted array
print(df.head(100))  # Print the array after applying the discount

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_1d = np.array([10, 20])
arr_1d = np.insert(arr_1d, 2, np.mean(arr_1d))
sum = arr_2d + arr_1d  # Perform element-wise addition using broadcasting

print("Result of Broadcasting: ", sum)  # Print the result of the broadcasting operation

nums = np.array([1, 2, 3, 4, np.nan, 6, 7, np.nan, 9])
print("NaN values in the array: ", np.isnan(nums))  # Check for NaN values in the array
print("Original Array: ", nums)  # Print the original array with NaN values
mean_value = np.nanmean(nums)  # Calculate the mean of the array, ignoring NaN values
nums = np.nan_to_num(nums, nan=mean_value).astype(int)  # Replace NaN values with the mean
print("Array after replacing NaN with mean: ", nums)  # Print the array

data = np.array([1, 2, np.inf, 4, 5, np.inf, 7, 8, 9])
print("Original Array: ", data)  # Print the original array with infinite values
# mean_value = np.mean(data[data != np.inf])   Calculate the mean of the array, ignoring infinite values
# data = np.where(data == np.inf, mean_value, data).astype(int)   Replace infinite values with the mean
data = np.nan_to_num(data, neginf=0, posinf=0).astype(int)  # Replace infinite values with NaN
print("Array after replacing inf with mean: ", data)
