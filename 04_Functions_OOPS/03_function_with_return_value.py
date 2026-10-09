def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(250, 3)
print("Total Amount:", result)

final_amount = result + 100
print("Amount after adding extra charges:", final_amount)