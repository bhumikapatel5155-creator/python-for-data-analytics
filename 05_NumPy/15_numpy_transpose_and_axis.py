import numpy as np

# Create a 2D array
marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 85]
])

print("Original Array:")
print(marks)

# 1. Transpose using T
transposed = marks.T

print("\nTransposed Array:")
print(transposed)

# 2. Transpose using transpose()
print("\nUsing transpose():")
print(np.transpose(marks))

# 3. Sum of all elements
print("\nTotal Marks:", np.sum(marks))

# 4. Column-wise sum
print("Column-wise Sum:", np.sum(marks, axis=0))

# 5. Row-wise sum
print("Row-wise Sum:", np.sum(marks, axis=1))

# 6. Column-wise average
print("Column-wise Average:", np.mean(marks, axis=0))

# 7. Row-wise average
print("Row-wise Average:", np.mean(marks, axis=1))