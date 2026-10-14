def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

num = 5
result = factorial(num)
print("Number:", num)
print("Factorial:", result)
