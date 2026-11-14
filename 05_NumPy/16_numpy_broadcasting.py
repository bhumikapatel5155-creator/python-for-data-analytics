import numpy as np

# 1. Add a scalar to an array
numbers = np.array([10, 20, 30, 40, 50])

result = numbers + 5

print("Original Array:", numbers)
print("After Adding 5:", result)

# 2. Multiply an array by a scalar
result2 = numbers * 2

print("\nAfter Multiplying by 2:", result2)

# 3. Broadcasting with 2D array
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [85, 90, 95]
])

bonus = np.array([5, 5, 5])

updated_marks = marks + bonus

print("\nOriginal Marks:")
print(marks)

print("\nUpdated Marks:")
print(updated_marks)

# 4. Broadcasting with different shapes
array1 = np.array([
    [10],
    [20],
    [30]
])

array2 = np.array([1, 2, 3])

result3 = array1 + array2

print("\nBroadcasting Result:")
print(result3)