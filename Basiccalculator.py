num1 = float(input("Please inter your first number :"))

operation = input("Please enter + - * / :")

num2 = float(input("Please enter second your number :"))

try:
    if operation == '+':
     print(num1 + num2)

    elif operation == '-':
     print(num1 - num2)

    elif operation =='*':
     print(num1 * num2)

    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Can Not division by zero.")
        else:
            print(num1 / num2)

    else:
        print("Invalid operation.")

except :
    print("Error")