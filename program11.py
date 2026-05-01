var1 = int(input("Enter number: "))
var2 = int(input("Enter power: "))

ans = 1

for i in range(var2):
    ans = ans * var1

print("Answer =", ans)