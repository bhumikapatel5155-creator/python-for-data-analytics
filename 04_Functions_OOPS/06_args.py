
def calculate_sum(*args):
    total = 0

    for number in args:
        total += number
    return total

print("Sum of 2 numbers:", calculate_sum(10, 20))
print("Sum of 3 numbers:", calculate_sum(10, 20, 30))
print("Sum of 5 numbers:", calculate_sum(10, 20, 30, 40, 50))