import numpy as np

# Create a 2D NumPy array
marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 85]
])

print("Array:")
print(marks)

# Array attributes
print("\nNumber of Dimensions:", marks.ndim)
print("Array Shape:", marks.shape)
print("Total Elements:", marks.size)
print("Data Type:", marks.dtype)
print("Item Size:", marks.itemsize, "bytes")
print("Total Memory:", marks.nbytes, "bytes")