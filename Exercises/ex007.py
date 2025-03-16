# Your Student ID:230543003
# Your Name and Surname:Abdullah Bakla


user_input = input("Enter a string: ")

char_count = {}
for char in user_input:
    char_count[char] = char_count.get(char, 0) + 1

print("Character frequencies:")
for char in sorted(char_count):
    print(f"{char}: {char_count[char]}")
