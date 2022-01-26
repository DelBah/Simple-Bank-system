from bank import Bank


b = Bank()
# The menu selection
def menu():
    print("1-Already customer\n2-Create/edit account\n3-Exit")
    answer = int(input("Enter your selection:\n"))

    # Diffrent selection regards to user needs
    # First selection
    if answer == 1:
        print("1-Show my account(s)\n2-Make a deposit/withdraw\n3-List of customers\n4-Exit")
        answer1 = int(input("Enter your choice:\n"))
        operations = [show_user_account, make_depOrwith, get_customers_list]
        output = operations[answer1 - 1]()
        print(output)

    # Secound selection
    elif answer == 2:
        print("1-Create customer\n2-Add account for existing customer\n3-Edit customer name\n4-Remove customer")
        answer1 = int(input("Enter your choice:\n"))
        operations = [create_customer, add_account, edit_info, remove_customer]
        output = operations[answer1 - 1]()
        output
        exit = input("Enter R to return or E to exit:\n")
        if exit.lower() == "r":
            menu()
        else:
            return "Have a nice day!"

    else:
        return "Have a nice day!"


#Show user account method
def show_user_account():
    pnr = input("Enter your social security number with 10 digits:\n")
    check = False

    while check is False:
        if len(pnr) != 10 or not pnr.isnumeric():
            pnr = input("You should enter 10 digits!\n")
        else:
            check = True
            b.get_customer_by_ssn(pnr)
            break

    exit = input("Enter R to return or E to exit:\n")
    if exit.lower() == "r":
        menu()
    else:
        return "Have a nice day!"


#User make deposit/withdraw method
def make_depOrwith():
    print("1-Deposit\n2-Withdraw\n3-Return")
    answer2 = int(input("Enter your selection:\n"))
    if answer2 == 1:
        pnr = input("Enter your social security number with 10 digits:\n")
        check = False
        while check is False:
            if len(pnr) != 10 or not pnr.isnumeric():
                pnr = input("You should enter 10 digits!\n")
            else:
                check = True
                break

        ac_number = int(input("Enter your account number with 4 digits:\n"))
        check = False
        while check is False:
            if len(str(ac_number)) != 4 or not pnr.isnumeric():
                ac_number = input("You should enter 4 digits!\n")
            else:
                check = True
                break

        while True:
            try:
                amount = int(input("Enter the amount you want to deposit:\n"))
            except:
                print("Only digits are accepted")
            else:
                break

        b.deposit(pnr, int(ac_number), amount)

        exit1 = input("\nEnter R to return or E to exit:\n")
        if exit1.lower() == "r":
            menu()
        else:
            print("Have a nice day!")
    #withdraw method
    elif answer2 == 2:
        pnr = input("Enter your social security number with 10 digits:\n")
        check = False
        while check is False:
            if len(pnr) != 10 or not pnr.isnumeric():
                pnr = input("You should enter 10 digits!\n")
            else:
                check = True
                break

        ac_number = int(input("Enter your account number with 4 digits:\n"))
        check = False
        while check is False:
            if len(str(ac_number)) != 4 or not pnr.isnumeric():
                ac_number = input("You should enter 4 digits!\n")
            else:
                check = True
                break

        while True:
            try:
                amount = int(input("Enter the amount you want to deposit:\n"))
            except:
                print("Only digits are accepted")
            else:
                break

        b.withdraw(pnr, int(ac_number), amount)
        exit2 = input("Enter R to return or E to exit:\n")
        if exit2.lower() == "r":
            menu()
        else:
            print("Have a nice day!")
    else:
        menu()

def create_customer():
    pnr = input("Enter your social security number with 10 digits:\n")
    check = False
    while check is False:
        if len(pnr) != 10 or not pnr.isnumeric():
            pnr = input("You should enter 10 digits!\n")
        else:
            check = True
            break

    username = input("Enter your first name:\n")
    check2 = False
    while check is False:
        if not username.isalpha():
            username = input("It seems you entered digits!\n")
        else:
            check = True
            break

    b.add_customer(username, pnr)

def add_account():
    pnr = input("Enter your social security number with 10 digits:\n")
    check = False
    while check is False:
        if len(pnr) != 10 or not pnr.isnumeric():
            pnr = input("You should enter 10 digits!\n")
        else:
            check = True
            break
    print(b.add_account(pnr))

def edit_info():
    pnr = input("Enter your social security number with 10 digits:\n")
    check = False
    while check is False:
        if len(pnr) != 10 or not pnr.isnumeric():
            pnr = input("You should enter 10 digits!\n")
        else:
            check = True
            break


    username=input("Enter the new name you want to change to:\n")
    check = False
    while check is False:
        if not username.isalpha():
            username = input("You should enter letters!\n")
        else:
            check = True
            break

    b.change_customer_name(username, pnr)


def remove_customer():
    pnr = input("Enter your social security number with 10 digits:\n")
    check = False
    while check is False:
        if len(pnr) != 10 or not pnr.isnumeric():
            pnr = input("You should enter 10 digits!\n")
        else:
            check = True
            break

        b.remove_customer(pnr)

#Function to get all existing customers
def get_customers_list():
    return ""