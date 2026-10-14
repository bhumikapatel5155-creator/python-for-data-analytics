def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(
    name="Bhumika",
    branch="AIML",
    cgpa=7.03,
    city="Jabalpur"
)
print("\nAnother Student:")
student_details(
    name="Rahul",
    branch="CSE",
    cgpa=8.5
)
