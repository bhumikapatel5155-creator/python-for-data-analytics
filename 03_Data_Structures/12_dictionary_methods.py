student = {
    "name": "Bhumika",
    "age": 21,
    "branch": "AIML",
    "cgpa": 7.03
}

print("Original Dictionary:", student)

# Get all keys
print("Keys:", student.keys())

# Get all values
print("Values:", student.values())

# Get key-value pairs
print("Items:", student.items())

# Add a new key-value pair
student["city"] = "Jabalpur"
print("After adding city:", student)

# Update an existing value
student["cgpa"] = 7.5
print("After updating CGPA:", student)

# Remove a key-value pair
student.pop("age")
print("After removing age:", student)