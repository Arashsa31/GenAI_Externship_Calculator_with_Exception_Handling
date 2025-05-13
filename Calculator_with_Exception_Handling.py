import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logging.error("ValueError: Invalid number input.")

def calculator():
    print("Welcome to the Error-Free Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == '1':
                result = num1 + num2
                print("Result:", result)
            elif choice == '2':
                result = num1 - num2
                print("Result:", result)
            elif choice == '3':
                result = num1 * num2
                print("Result:", result)
            elif choice == '4':
                result = num1 / num2
                print("Result:", result)
            else:
                print("Invalid option. Try again.")
        except ZeroDivisionError:
            print("Oops! Division by zero is not allowed.")
            logging.error("ZeroDivisionError: division by zero.")
        finally:
            print("Operation complete.")

calculator()
