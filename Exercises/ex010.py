# Your Student ID:230543003
# Your Name and Surname:Abdullah Bakla

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
        print("Result:", result)
    elif operation == "-":
        result = num1 - num2
        print("Result:", result)
    elif operation == "*":
        result = num1 * num2
        print("Result:", result)
    elif operation == "/":
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid operation! Please choose +, -, *, or /.")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()

    if another_calculation != "yes":
        break

print("Goodbye!")

