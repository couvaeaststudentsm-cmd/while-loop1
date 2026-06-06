def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def devide(num1,num2):
    return num1 / num2

try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter secound number:"))

    operation = input("Enter operation(+,-,*,/):")

    if operation =='+':
        print("Answer =",add(num1,num2))

    elif operation =='-':
        print("Answer =",subtract(num1,num2))

    elif operation =='*':
        print("Answer =",multiply(num1,num2))

    elif operation =='/':
        print("Answer =",devide(num1,num2))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter numbers only")
