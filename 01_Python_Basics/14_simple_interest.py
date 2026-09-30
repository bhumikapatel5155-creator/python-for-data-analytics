principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest
print("\nInterest Calculation")
print("Principal Amount:", principal)
print("Interest Rate:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)