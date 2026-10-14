
def student_details(name, age, branch, cgpa):
    print("Student Name:", name)
    print("Age:", age)
    print("Branch:", branch)
    print("CGPA:", cgpa)


student_details(
    name="Bhumika",
    age=21,
    branch="AIML",
    cgpa=7.03
)

print()

student_details(
    cgpa=8.5,
    branch="CSE",
    name="Rahul",
    age=22
)