import numpy as np

# Create an array of student marks
marks = np.array([45, 60, 75, 80, 90, 95, 55, 85])

print("Student Marks:", marks)

# 1. Comparison Operators
print("\nMarks greater than 80:")
print(marks > 80)

print("\nMarks less than 60:")
print(marks < 60)

print("\nMarks equal to 80:")
print(marks == 80)

# 2. Boolean Filtering
print("\nStudents scoring above 80:")
print(marks[marks > 80])

# 3. Filtering with multiple conditions
print("\nMarks between 60 and 90:")
print(marks[(marks >= 60) & (marks <= 90)])

# 4. Filtering using OR condition
print("\nMarks below 50 or above 90:")
print(marks[(marks < 50) | (marks > 90)])

# 5. Using np.where()
result = np.where(marks >= 60, "Pass", "Fail")

print("\nStudent Results:")
print(result)