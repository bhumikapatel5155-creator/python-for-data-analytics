import numpy as np

# 1D Array
numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:", numbers)

# Access individual elements
print("\nFirst Element:", numbers[0])
print("Second Element:", numbers[1])
print("Last Element:", numbers[-1])
print("Second Last Element:", numbers[-2])

# 2D Array
marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 85]
])

print("\n2D Array:")
print(marks)

# Access elements using row and column
print("\nFirst Row, First Column:", marks[0, 0])
print("First Row, Second Column:", marks[0, 1])
print("Second Row, Third Column:", marks[1, 2])
print("Last Row, Last Column:", marks[-1, -1])