import numpy as np

# 1D Array
numbers = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original Array:", numbers)

# Slicing
print("First Three Elements:", numbers[0:3])
print("Elements from Index 2 to 5:", numbers[2:6])
print("First Four Elements:", numbers[:4])
print("Last Three Elements:", numbers[-3:])
print("Every Second Element:", numbers[::2])

# 2D Array
marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 85],
    [60, 65, 70]
])

print("\nOriginal 2D Array:")
print(marks)

# Extract rows
print("\nFirst Two Rows:")
print(marks[0:2, :])

# Extract columns
print("\nFirst Two Columns:")
print(marks[:, 0:2])

# Extract selected rows and columns
print("\nSelected Elements:")
print(marks[0:2, 1:3])