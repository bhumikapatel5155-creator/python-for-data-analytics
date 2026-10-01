number_of_terms = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(number_of_terms):
    print(a, end=" ")
    a, b = b, a + b