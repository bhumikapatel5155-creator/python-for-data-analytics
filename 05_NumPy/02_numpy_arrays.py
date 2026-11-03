import numpy as np

# 1D Array
array_1d = np.array([10, 20, 30, 40, 50])

# 2D Array
array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# 3D Array
array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("1D Array:")
print(array_1d)

print("\n2D Array:")
print(array_2d)

print("\n3D Array:")
print(array_3d)

print("\nDimensions:")
print("1D:", array_1d.ndim)
print("2D:", array_2d.ndim)
print("3D:", array_3d.ndim)

print("\nShapes:")
print("1D:", array_1d.shape)
print("2D:", array_2d.shape)
print("3D:", array_3d.shape)