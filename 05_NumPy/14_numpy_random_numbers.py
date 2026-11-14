import numpy as np

# 1. Generate random integers
random_int = np.random.randint(1, 100, size=5)

print("Random Integers:", random_int)

# 2. Generate random decimal values between 0 and 1
random_float = np.random.rand(5)

print("\nRandom Float Values:", random_float)

# 3. Generate values from standard normal distribution
random_normal = np.random.randn(5)

print("\nRandom Normal Values:", random_normal)

# 4. Generate a random 2D array
random_2d = np.random.randint(1, 50, size=(3, 3))

print("\nRandom 2D Array:")
print(random_2d)

# 5. Set random seed
np.random.seed(42)

seed_array = np.random.randint(1, 100, size=5)

print("\nRandom Values with Seed:", seed_array)

# 6. Shuffle an array
numbers = np.array([10, 20, 30, 40, 50])

np.random.shuffle(numbers)

print("\nShuffled Array:", numbers)