import numpy as np

# Create two arrays
array1 = np.array([10, 20, 30])
array2 = np.array([40, 50, 60])

print("Array 1:", array1)
print("Array 2:", array2)

# 1. Concatenate
combined = np.concatenate((array1, array2))

print("\nConcatenated Array:", combined)

# 2. Vertical Stack
vertical = np.vstack((array1, array2))

print("\nVertical Stack:")
print(vertical)

# 3. Horizontal Stack
horizontal = np.hstack((array1, array2))

print("\nHorizontal Stack:")
print(horizontal)

# 4. Split Array
numbers = np.array([10, 20, 30, 40, 50, 60])

split_array = np.split(numbers, 3)

print("\nSplit Array:")
for part in split_array:
    print(part)

# 5. Split a 2D Array
matrix = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

vertical_split = np.vsplit(matrix, 2)

print("\nVertical Split:")
for part in vertical_split:
    print(part)