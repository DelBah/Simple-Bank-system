# The menu selection
def menu():
    print("1-Already customer\n2-Create/edit account\n3-Exit")
    answer = int(input("Enter your selection:\n"))

    # Diffrent selection regards to user needs
    # First selection
    if answer == 1:
        print("1-Show my account(s)\n2-Make a deposit/withdraw´\n3-Transactions\n4-List of customers\n5-Exit")
        answer1 = int(input("Enter your choice:\n"))
        operations = [show_user_account, make_depOrwith, transactions, get_customers_list]
        output = operations[answer1 - 1]()
        print(output)
    # Secound selection
    elif answer == 2:
        print("1-Create account\n2-Create account for existing customer\n3-Edit account info")
    else:
        print("Have a nice day!")


#Show user account method
def show_user_account():
    print("A function will come here soon!\n")
    exit = input("Enter R to return or E to exit:\n")
    if exit.lower() == "r":
        menu()
    else:
        print("Have a nice day!")


#User make deposit/withdraw method
def make_depOrwith():
    print("1-Deposit\n2-Withdraw\n3-Return")
    answer2 = int(input("Enter your selection:\n"))
    if answer2 == 1:
        print("a function will come here soon!\n")
        exit1 = input("Enter R to return or E to exit:\n")
        if exit1.lower() == "r":
            menu()
        else:
            print("Have a nice day!")
    elif answer2 == 2:
        print(" a function will come here soon!\n")
        exit2 = input("Enter R to return or E to exit:\n")
        if exit2.lower() == "r":
            menu()
        else:
            print("Have a nice day!")
    else:
        menu()

#Transaction method
def transactions():
    print("1-Make a transaction\n2-transaction history\n3-Exit")
    in_put = int(input("Enter your selection:\n"))
    if in_put == 1:
        print("Here will come a function")
        menu()
    elif in_put == 2:
        print("Here will come a function")
        menu()
    else:
        print("Have a nice day!")

#Function to get all existing customers
def get_customers_list():
    return ""