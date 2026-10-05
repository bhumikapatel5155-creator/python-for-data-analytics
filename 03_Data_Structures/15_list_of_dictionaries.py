students = [
    {
        "name": "sneha",
        "age": 21,
        "branch": "AIML",
        "cgpa": 7.03
    },
    {
        "name": "Rahul",
        "age": 22,
        "branch": "CSE",
        "cgpa": 8.1
    },
    {
        "name": "Priya",
        "age": 21,
        "branch": "IT",
        "cgpa": 8.5
    }
]

print("Student Information:")

for student in students:
    print(
        "Name:", student["name"],
        "| Age:", student["age"],
        "| Branch:", student["branch"],
        "| CGPA:", student["cgpa"]
    )