class Bank():
    global account_balance
    account_balance = 0

    def balance(self):
        return account_balance
    
    def withdraw_cash(self):
        print("Let me check your account balance...")
        if account_balance == 0:
            print("Sorry your account does not have the minimum balance to withdraw...")

        else:
            ammount = float(input("Enter the ammount you want to withdraw: "))
            remaining_balance = account_balance - ammount
            print("Now your account has leftover balance with: ",remaining_balance, "Rupees") 
        
        return
    
    def current_status(self):
        print("You are all set to withdraw or deposit the cash in your account")
        print("Checking your current balance...")
        print("Your current account balance is: ",account_balance,"Rupees")

        return

    def deposit(self):
        "To deposit the ammount of money"
        deposit_ammount = float(input("The ammount of money you want to deposit: "))
        print("Thank you for depsiting the money...")
        new_balance = account_balance + deposit_ammount
        print()
        print("Now your account balance is: ",new_balance,"Rupees")

        return
    
    def OpenAccount(self):
            
        def SavingsAccount():
            Account_Number = int(input("Enter your 10 digit account number:"))
            PIN = int(input("Enter the 4-digit pin number:"))
            Password = input("Enter the password you want to take for your account: ")
            print("Minimum balance should be equal to 1000 Rupees in your savings account..")
                
            # conditionals for the account number input
            if len(str(Account_Number)) > 10:
                    print("Account number should be equal to 10 digits, please re-enter")

            elif len(str(Account_Number)) < 10:
                    print("Account number should be equal to 10 digits, please re-enter")

        
            elif len(str(Account_Number)) < 0:
                    print("Invalid input, please re-enter")



            # conditionals for the pin
            if len(str(PIN)) > 4:
                print("PIN number should be 4 digits, please re-enter")

            elif len(str(PIN)) < 4:
                print("PIN number should be 4 digits, please re-enter")

        
            elif len(str(PIN)) < 0:
                print("Invalid input, please re-enter")

            print()
            print("Congratulations!!!, your accoun is ready and you can make money deposit as well as money transfer from this account internationally!!!")
            print("\nYour account details are shown as follows: \n1:Account Number:", Account_Number,"\n2:PIN:", PIN,"\n3:Password:", Password)
            print("Do you want to continue...")
                
        
        

        def ZeroBalance():
            # taking gthe user input
            # for the account details
        
            Account_Number = int(input("Enter your 10 digit account number:"))
            PIN = int(input("Enter the 4-digit pin number:"))
            
            # conditionals for the account number input
            if len(str(Account_Number))>10:
                print("Account number should be equal to 10 digits, please re-enter")

            elif len(str(Account_Number))<10:
                print("Account number should be equal to 10 digits, please re-enter")

        
            elif len(str(Account_Number))<0:
                print("Invalid input, please re-enter")
        


            # conditionals for the pin
            if len(str(PIN))>4:
                print("PIN number should be 4 digits, please re-enter")

            elif len(str(PIN))<4:
                print("PIN number should be 4 digits, please re-enter")

        
            elif len(str(PIN))<0:
                print("Invalid input, please re-enter")

                
            print("You can keep your account empty, there is no minimum balance requirement...")
            print("Congratulations!!!, your accoun is ready and you can make money deposit as well as money transfer from this account internationally!!!")
            print("Your monthly limit for bank money transfer is 40000 Rupees")
            print("\nYour account details are shown as follows: \n1:Account Number:", Account_Number,"\n2:PIN:", PIN)
            
        print()
        print("Choose the option...")
        choice = 1
        while choice != 0:
            print()
            print("1:General Savings Bank Account")
            print("2:Zero Balance Account")
            print()
            choice = int(input("Enter you choice: "))

            if choice == 1:
                SavingsAccount()
                break

            if choice == 2:
                ZeroBalance()
                break
        

a = Bank()
Choice = 1
while Choice != 0:
    print("1:To check the current status")
    print("2:Deposit Cash")
    print("3:Withdraw Cash")
    print("4:Account Balance")
    print("5:Open a new account")

    Choice = int(input("Enter your choice:"))
    if Choice == 1:
        (a.current_status())

    elif Choice == 2:
        (a.deposit())

    elif Choice == 3:
        (a.withdraw_cash())

    elif Choice == 4:
        (a.balance())

    elif Choice ==5:
        (a.OpenAccount())

    else:
        print("Invalid choice!")
    print()
    
    
                
        






