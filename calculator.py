def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def show_menu():
    print("\n   CLI Calculator ")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")

while True:
    show_menu()
    operator = input("Enter operator: ").strip()
    
    if operator.lower() == 'quit':
        print("Goodbye!")
        break
    
    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator! Try again.")
        continue
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number! Try again.")
        continue
    
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)
    
    print(f"Result: {result}")
    print("-" * 20)


