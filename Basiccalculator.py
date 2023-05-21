def calculator(num1, operation, num2):
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError('Cannot divide by zero.')
            else:
                return num1 / num2
        else:
            return 'Invalid operation.'
    except:
        return 'Error'

if __name__ == '__main__':
    num1 = float(input('Please enter your first number: '))
    operation = input('Please enter + - * /: ')
    num2 = float(input('Please enter your second number: '))

    result = calculator(num1, operation, num2)
    print('Result:', result)