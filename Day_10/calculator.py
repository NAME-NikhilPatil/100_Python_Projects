from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What is the 1'st Number:"))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from line above:")
        num2 = float(input("What is the 2'nd Number:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1}{operation_symbol}{num2}:{answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' for new calculation:.") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
