number_of_subjects = int(input("Enter number of subjects: "))
total_marks = float(input("Enter total marks for all subjects: "))

obtained_marks = 0

for i in range(1, number_of_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    obtained_marks += marks

percentage = (obtained_marks / total_marks) * 100

print("\n--- Result ---")
print("Total Marks:", total_marks)
print("Obtained Marks:", obtained_marks)
print("Percentage:", percentage, "%")