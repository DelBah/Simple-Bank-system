from bank import Bank


b = Bank()
b._load()
b._load_customers()
# The menu selection
def menu():
    print("1-Already customer\n2-Create/edit account\n3-Exit")
    answer = int(input("Enter your selection:\n"))

    # Diffrent selection regards to user needs
    # First selection
    if answer == 1:
        print("1-Show my account(s)\n2-Make a deposit/withdraw\n3-List of customers\n4-Exit/Return\n")
        answer1 = int(input("Enter your choice:\n"))
        operations = [show_user_account, make_depOrwith, get_customers_list, exit_meth]
        output = operations[answer1 - 1]()


    # Secound selection
    elif answer == 2:
        print("1-Create customer\n2-Add account for existing customer\n3-Edit customer name\n"
              "4-Remove customer\n5-Close account\n6-Exit/Return")
        answer1 = int(input("Enter your choice:\n"))
        operations = [create_customer, add_account, edit_info, remove_customer, close_acc, exit_meth]
        output = operations[answer1 - 1]()
        #output


    else:
        print("Have a nice day!")


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

    exit_meth()


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
        exit_meth()
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
                amount = int(input("Enter the amount you want to withdraw:\n"))
            except:
                print("Only digits are accepted")
            else:
                break

        b.withdraw(pnr, int(ac_number), amount)
        exit_meth()
    else:
        menu()
#Method to create customer
def create_customer():
    pnr = input("Enter your social security number with 10 digits:\n")
    check = False
    while check is False:
        if len(pnr) != 10 or not pnr.isnumeric():
            pnr = input("You should enter 10 digits!\n")
        else:
            check = True
            break

    username = input("Enter your name:\n")
    check2 = False
    while check is False:
        if not username.isalpha():
            username = input("It seems you entered digits!\n")
        else:
            check = True
            break

    b.add_customer(username, pnr)

#Method to add account to an existing customer
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
#Method to change customer name
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

#Method to remove a customer
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

def close_acc():
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
    b.close_account(pnr,ac_number)

#Function to get all existing customers
def get_customers_list():
    print(b.get_customers())
    exit_meth()

#This method to exit program or to return to main menu
def exit_meth():

    exit = input("\nEnter R to return or E to exit:\n")
    if exit.lower() == "r":
        menu()
    else:
        print ("Have a nice day!")