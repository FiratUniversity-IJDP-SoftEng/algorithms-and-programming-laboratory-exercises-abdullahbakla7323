# Your Student ID:230543003
# Your Name and Surname:Abdullah Bakla

conversion_type = input("Which conversion would you like to perform? (C to F or F to C): ")


if conversion_type == "C to F":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "°C is", fahrenheit, "°F")

elif conversion_type == "F to C":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit, "°F is", celsius, "°C")


else:
    print("Invalid input. Please enter either 'C to F' or 'F to C'.")






