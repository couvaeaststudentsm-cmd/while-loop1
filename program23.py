def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

num1 = int(input("Enter your first number that you want to calculate"))
num2 = int(input("Enter your secound number that you want to calculate"))

print("Addition = ",add(num1,num2))
print("Subtraction = ",subtract(num1,num2))
print("Multiplication =", multiply(num1,num2))
print("Division =",divide(num1,num2))