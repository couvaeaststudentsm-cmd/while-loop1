try:
    num1,num2 = eval(input("Enter two number,seperated by a comma:"))
    result = num1 / num2
    print("Result is",result)
except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is msising.Enter numbers sepearted by comma like this 1,2")

except:
    print("Wrong Input")
else:
    print('No exceptions')
finally:
    print("This will execute no matter what")