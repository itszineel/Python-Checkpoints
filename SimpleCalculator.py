def calculator(num1, num2):
    while True:
        operator = input("Enter the operator (+, -, *, /): ").strip()

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: division by zero is not allowed.")
            else:
                return num1 / num2
        else:
            print("Invalid operator. Please enter +, -, *, or /.")


def read_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("Simple Calculator")

    while True:
        num1 = read_number("Enter the first number: ")
        num2 = read_number("Enter the second number: ")

        result = calculator(num1, num2)

        if result is not None:
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print("The result is:", result)

        choice = input("Would you like to perform another calculation? (yes/no): ").strip().lower()

        if choice != "yes":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()