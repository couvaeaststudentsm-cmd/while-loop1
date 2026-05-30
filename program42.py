try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age!")
    else:
        print("Valid age.")

        if age % 2 == 0:
            print("Age is even.")
        else:
            print("Age is odd.")

except ValueError:
    print("Error! Please enter a valid number.")
