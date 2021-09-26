while True:
 x = float(input("введіть перше число:"))
 operation = input("введіть операцію:")
 y = float(input("введіть друге чило:"))
 z = None
 if operation == "+":
    z = x + y
 elif operation == "-":
    z = x - y
 elif operation == "*":
    z = x * y
 elif operation == "/":
    if y == 0:
        print("error")
    else:
        z = x / y
 elif operation == "**":
    z = x ** y
 elif operation == "sqrt":
    z = x ** (1/2)
 else:
     print("Error")
 if z is not None:
     print("result", z)