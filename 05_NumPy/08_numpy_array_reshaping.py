import numpy as np

# Original 1D Array
numbers = np.arange(1, 13)
print("Original Array:")
print(numbers)

# 1. Convert 1D array into 2D array
array_2d = numbers.reshape(3, 4)
print("\n2D Array (3 Rows, 4 Columns):")
print(array_2d)

# 2. Convert into another shape
array_3d = numbers.reshape(2, 2, 3)
print("\n3D Array:")
print(array_3d)

# 3. Flatten - Convert into 1D array
flatten_array = array_2d.flatten()
print("\nFlatten Array:")
print(flatten_array)

# 4. Ravel - Convert into 1D array
ravel_array = array_2d.ravel()
print("\nRavel Array:")
print(ravel_array)

# 5. Automatic dimension using -1
auto_array = numbers.reshape(4, -1)
print("\nAutomatic Reshape:")
print(auto_array)