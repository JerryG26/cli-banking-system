isActive = True
print("---Welcome to Jerry's Bank---")
while isActive:

    print("\nEnter 1 to login")
    print("Enter 2 to register")
    print("Enter 3 to exit")

    user_choice = int(input(": "))
    match user_choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case _:
            print("Invalid input")


