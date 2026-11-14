import numpy as np

# Original Array
original = np.array([10, 20, 30, 40, 50])

print("Original Array:", original)

# 1. Using copy()
copied_array = original.copy()

# Modify copied array
copied_array[0] = 100

print("\nAfter Modifying Copy:")
print("Original Array:", original)
print("Copied Array:", copied_array)

# 2. Using view()
view_array = original.view()

# Modify view array
view_array[1] = 200

print("\nAfter Modifying View:")
print("Original Array:", original)
print("View Array:", view_array)

# 3. Check memory sharing
print("\nCopy Shares Memory:",
      np.shares_memory(original, copied_array))

print("View Shares Memory:",
      np.shares_memory(original, view_array))