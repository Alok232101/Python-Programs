def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def perform_operation(operator, x, y):
    switch = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power,
        '%': modulus,
    }
    return switch.get(operator, lambda: "Invalid operator")(x, y)

if __name__ == "__main__":
    print("Available operations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("** : Power")
    print("% : Modulus")

    operator = input("Enter the operator: ")
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    result = perform_operation(operator, x, y)
    print(f"Result: {result}")
