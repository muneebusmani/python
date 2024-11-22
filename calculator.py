print("""Which Operation do you want to perform:
addition(+)
subtraction(-)
multiplication(*)
division(/)
""")
# Get user input for operation
operation = input("Enter your choice (+,-,*,/): \n")

# Define a set of valid operations
operations = {"+","-","*","/"}

# Check if user input is a valid operation
if operation not in operations:
    print("Invalid choice. Please enter a number between 1 and 4.\n")
    exit()

# Get User input for numbers
print("enter first number:")
first_number = int(input("\n"))
print("enter second number:")
second_number = int(input("\n"))

# Check divide by zero error
if operation == "/" and second_number == 0:
    print("Error: Division by zero is not allowed.\n")
    exit()
result = 0
# Perform the chosen operation
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
else:
    print("\nInvalid operation. Please try again.\n")
    exit()
print(f"your answer is :  {result}\n")