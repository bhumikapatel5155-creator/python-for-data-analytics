import numpy as np

# 1. zeros() - Creates an array filled with zeros
zero_array = np.zeros(5)

# 2. ones() - Creates an array filled with ones
one_array = np.ones(5)

# 3. arange() - Creates numbers within a given range
range_array = np.arange(1, 11)

# 4. linspace() - Creates equally spaced numbers
space_array = np.linspace(1, 10, 5)

# 5. full() - Creates an array filled with a specific value
full_array = np.full(5, 100)

print("Zeros Array:", zero_array)
print("Ones Array:", one_array)
print("Range Array:", range_array)
print("Linspace Array:", space_array)
print("Full Array:", full_array)