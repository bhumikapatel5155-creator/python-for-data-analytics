# String Methods
text = "  Python for Data Analytics  "
print("Original:", text)

# Remove extra spaces
print("Strip:", text.strip())

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Replace text
print("Replace:", text.replace("Data Analytics", "Data Science"))

# Split string into words
print("Split:", text.split())

# Find position of a word
print("Position of 'Data':", text.find("Data"))

# Check whether text starts with a specific word
print("Starts with Python:", text.strip().startswith("Python"))

# Check whether text ends with a specific word
print("Ends with Analytics:", text.strip().endswith("Analytics"))