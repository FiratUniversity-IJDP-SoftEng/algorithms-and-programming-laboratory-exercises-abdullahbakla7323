# Your Student ID:230543003
# Your Name and Surname:Abdullah Bakla


numbers = list(range(1, 11))

print("Original list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

numbers.extend([11, 12, 13])
print("Extended list:", numbers)

print("List length:", len(numbers))

numbers.pop(0)  
numbers.pop(-1)  
print("Modified list:", numbers)


even_numbers = sorted([num for num in range(1, 14) if num % 2 == 0])
print("Sorted even numbers list:", even_numbers)

