
# Create and write a file

with open("student_data.txt", "w") as file:
    file.write("Name: Bhumika\n")
    file.write("Branch: AIML\n")
    file.write("CGPA: 7.03\n")

print("File created successfully!")

# Read the file

with open("student_data.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# Append new data

with open("student_data.txt", "a") as file:
    file.write("City: Jabalpur\n")

print("New data added successfully!")