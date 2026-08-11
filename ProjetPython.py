import math


class Calculator:

    def __init__(self):
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, first_number, operation, second_number):

        if not isinstance(first_number, (int, float)):
            print("Error: The first value must be a number.")
            raise TypeError("The first value must be a number.")

        if not isinstance(second_number, (int, float)):
            print("Error: The second value must be a number.")
            raise TypeError("The second value must be a number.")

        if operation not in self.operations:
            print("Error: Invalid operation.")
            raise ValueError("Invalid operation.")

        if operation == "/" and second_number == 0:
            print("Error: Cannot divide by zero.")
            raise ZeroDivisionError("Cannot divide by zero.")

        return self.operations[operation](first_number, second_number)


# Advanced mathematical operations

def power(a, b):
    return a ** b


def square_root(a, b=None):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)


def logarithm(a, b=None):
    if a <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log(a)


# Create the calculator
calculator = Calculator()

# Add advanced operations
calculator.add_operation("^", power)
calculator.add_operation("sqrt", square_root)
calculator.add_operation("log", logarithm)


# Main program
while True:

    print("\nAvailable operations: +, -, *, /, ^, sqrt, log")
    print("Type 'q' to quit.")

    operation = input("Enter an operation: ")

    if operation == "q":
        print("Goodbye!")
        break

    try:
        first_number = float(input("Enter the first number: "))

        if operation not in ["sqrt", "log"]:
            second_number = float(input("Enter the second number: "))
        else:
            second_number = 0

        if not isinstance(first_number, (int, float)):
            raise TypeError("The first value must be a number.")

        if not isinstance(second_number, (int, float)):
            raise TypeError("The second value must be a number.")

        result = calculator.calculate(
            first_number,
            operation,
            second_number
        )

        print("Result =", result)

    except (ValueError, TypeError, ZeroDivisionError) as error:
        print("Error:", error)