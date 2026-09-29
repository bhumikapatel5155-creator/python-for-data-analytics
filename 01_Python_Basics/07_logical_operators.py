# Logical Operators
age = 21
has_degree = True
has_experience = False

print("Age:", age)
print("Has Degree:", has_degree)
print("Has Experience:", has_experience)
print("\nLogical Operations:")

# AND: Both conditions must be True
print("Eligible for graduation job:", age >= 18 and has_degree)

# OR: At least one condition must be True
print("Has qualification or experience:", has_degree or has_experience)

# NOT: Reverses the result
print("Does not have experience:", not has_experience)