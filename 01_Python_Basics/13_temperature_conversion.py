temperature = float(input("Enter temperature: "))
choice = input("Convert to Celsius or Fahrenheit? (C/F): ").upper()

if choice == "F":
    result = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", result)

elif choice == "C":
    result = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice. Please enter C or F.")