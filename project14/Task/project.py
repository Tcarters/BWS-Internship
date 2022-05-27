#Banking App
#Class BAsed
# Withdrawal and Deposit
#Write the transaction to a python file
#while True:
#input
#classes
#open()
#method
#properties
import datetime


class Bank:

    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount


    def track_transaction(self, transaction_rec):
        with open("transaction_file.txt", "a") as file:
            file.write(f"{transaction_rec} \t and new  Balance: {self.balance} $ \n")

    def Withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount < self.balance:
            self.balance = self.balance - amount
            self.track_transaction(f"Client withdrew: {amount} $ on {datetime.datetime.now() } ")
        else:
            print("\nInsufficient balance, can't proceed operation...")

    def Deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.track_transaction(f"Client Deposited {amount} $ on {datetime.datetime.now()} ")



print("""
     ============================================================
                        WELCOME TO BANK APP
     ============================================================
     """)
# Instantiate my class Bank
bank = Bank(50.50) 

while True:
    print("Please choose b/w these operations 'withdraw/w , deposit/d' to proceed ...\n")

    client_choice = input("What type of transaction you are looking for ? ")

    if client_choice in ["withdraw" , "w" , "deposit", "d", "D"]:
        if client_choice == "withdraw" or client_choice == "w" or client_choice == "W":
            withdraw_amount = input("What is your withdraw amount ? ")
            bank.Withdrawal(withdraw_amount)
            print("\n\t Balance after Withdrawing Operation: ", bank.balance, '$')

        elif client_choice == "deposit" or client_choice == "d" or client_choice == "D":
           depo_amount = input("What is your deposit amount ? ")
           bank.Deposit(depo_amount)
           print("\n\t Balance after Deposit Operation:", bank.balance,  '$', '\n' )
    else:
        print("\nUnknown transaction type !!! We can't proceed further... ")       
    
    play_again = input("You want to continue again y/n ? ")
    if play_again == 'y':
        continue
    else:
        print("\n\tClosing app...")      
    break      







# pre_init_amount = input("Enter initial amount: ")

