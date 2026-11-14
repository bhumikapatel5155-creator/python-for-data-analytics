import numpy as np

# Create an array
numbers = np.array([50, 20, 80, 10, 40, 90, 30])

print("Original Array:", numbers)

# 1. Ascending Order
ascending = np.sort(numbers)

print("\nAscending Order:", ascending)

# 2. Descending Order
descending = np.sort(numbers)[::-1]

print("Descending Order:", descending)

# 3. Sort a 2D Array
marks = np.array([
    [80, 60, 90],
    [70, 95, 85],
    [90, 75, 65]
])

print("\nOriginal 2D Array:")
print(marks)

# Sort each row
print("\nRow-wise Sorting:")
print(np.sort(marks, axis=1))

# Sort each column
print("\nColumn-wise Sorting:")
print(np.sort(marks, axis=0))

# 4. Get sorted indices
indices = np.argsort(numbers)

print("\nSorted Indices:", indices)

# 5. Find Top 3 Values
top_three = np.sort(numbers)[-3:][::-1]

print("\nTop 3 Values:", top_three)