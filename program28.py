def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def devide(P,Q):
    return P / Q

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("a. Multiply")
print("a. Divide")

choice = input("Please eneter the choice(a/b/c/d):")

num_1 = int(input("Please enter the first number:"))
num_2 = int(input("Please enter the secound number:"))

if choice =="a":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
if choice =="b":
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
if choice =="c":
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
if choice =="d":
    print(num_1,"/",num_2,"=",devide(num_1,num_2))







