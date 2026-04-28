while True:
    card = input("Insert your Card: ")
    if card=='c':
        print("Welcome Bhanusri!")
        password = int(input("Enter password: "))
        if password==1234:
            options = int(input("1. Balance Enquiry  2. Withdraw Money "))
            if options==1:
                print("Your account balance is 1,00,000")
            else:
                withdraw = int(input("Enter amount to withdraw: "))
                rem = 100000-withdraw
                print(f"Remaining account balance is {rem}")
        else:
            print("Incorrect Password")
    else:
        print("Invalid Card")
