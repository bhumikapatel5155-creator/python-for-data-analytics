numbers = [10, 20, 30, 40]
print("Original List:", numbers)
# Add an element
numbers.append(50)
print("After append:", numbers)
# Insert an element
numbers.insert(1, 15)
print("After insert:", numbers)
# Remove an element
numbers.remove(30)
print("After remove:", numbers)
# Remove the last element
numbers.pop()
print("After pop:", numbers)
# Sort the list
numbers.sort()
print("After sort:", numbers)
# Reverse the list
numbers.reverse()
print("After reverse:", numbers)
# Count an element
print("Count of 20:", numbers.count(20))