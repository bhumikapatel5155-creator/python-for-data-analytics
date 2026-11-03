import numpy as np

# 1. Integer Array
int_array = np.array([10, 20, 30, 40])

# 2. Float Array
float_array = np.array([10.5, 20.5, 30.5])

# 3. String Array
string_array = np.array(["Python", "SQL", "Excel"])

# 4. Boolean Array
bool_array = np.array([True, False, True])

print("Integer Array:", int_array)
print("Integer Data Type:", int_array.dtype)

print("\nFloat Array:", float_array)
print("Float Data Type:", float_array.dtype)

print("\nString Array:", string_array)
print("String Data Type:", string_array.dtype)

print("\nBoolean Array:", bool_array)
print("Boolean Data Type:", bool_array.dtype)

# 5. Type Conversion using astype()
numbers = np.array([10.8, 20.5, 30.9, 40.2])
integer_numbers = numbers.astype(int)

print("\nOriginal Array:", numbers)
print("Converted Array:", integer_numbers)
print("Converted Data Type:", integer_numbers.dtype)