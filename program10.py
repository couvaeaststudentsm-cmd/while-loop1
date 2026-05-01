var1 = int(input("Enter the base number: "))
var2 = int(input("Enter the times you want to mulipy by eg 2,3,4,5: "))

result = 1

for i in range(1, var2 + 1):
    result = result * var1

print("\nResult =", result)