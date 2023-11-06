import calculator

# User inputs
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# convert string to float 
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    calculator.add(first_number, second_number)
elif operation == "subtract":
    calculator.subtract(first_number, second_number)
elif operation == "multiply":
    calculator.multiple(first_number, second_number)
elif operation == "divide":
    calculator.divide(first_number, second_number)
else:
    print("Sorry, I do not understand your request.")