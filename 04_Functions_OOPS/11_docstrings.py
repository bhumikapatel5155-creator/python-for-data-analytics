def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: A list of numeric values.

    Returns:
        The average of the numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average
marks = [80, 85, 90, 75, 95]
result = calculate_average(marks)
print("Student Marks:", marks)
print("Average Marks:", result)
print("Function Documentation:")
print(calculate_average.__doc__)
