def shutdown(choice):
    if choice == "Yes":
        print("Shutting down")
    
    elif choice == "No":
        print("Abort shut down")
    
    else:
        print("Sorry")

user = input("Enter Yes or No: ")

shutdown(user)