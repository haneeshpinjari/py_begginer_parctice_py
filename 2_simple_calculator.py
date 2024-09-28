def calc():
    operation = input("Enter the operation to perform (+ , -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if operation == '+':
        print(f"result = {num1 + num2}")
    elif operation == '-':
        print(f"result = {num1 - num2}")
    elif operation == '*':
        print(f"result = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"result = {num1 / num2}")
        else:
            print(f"can't divide with zero")
    else:
        print(f"INvalid operator")

calc()