print("Basic Calculator (+, -, *, /, %)")

a = input("First number: ")
b = input("Second number: ")
op = input("Operator: ")

if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
    x, y = float(a), float(b)

    if op == '+':
        print(f"Result: {x + y}")
    elif op == '-':
        print(f"Result: {x - y}")
    elif op == '*':
        print(f"Result: {x * y}")
    elif op == '/':
        print(f"Result: {x / y}" if y != 0 else "Cannot divide by zero.")
    elif op == '%':
        print(f"Result: {x % y}" if y != 0 else "Cannot mod by zero.")
    else:
        print("Invalid operator.")
else:
    print("Enter valid numeric values.")
