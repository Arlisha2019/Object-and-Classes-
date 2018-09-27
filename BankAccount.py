class BankAccount:
    def __init__(self, first_name,last_name,middle_name,account_type,account_balance, status):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.account_type = account_type
        self.account_balance = account_balance
        self.status = status

    def deposit(self,cash_deposit):
        self.cash_deposit = cash_deposit + account_balance

    def withdrawal(self, cash_withdrawal):
        self.cash_withdrawal = cash_withdrawal - account_balance

    def transferAccountToAccount(self, acc_to_acc_trans):
        self.acc_to_acc_trans = acc_to_acc_trans

account_balance = 0

account_info = []

print("Thank You for chosing to open an account with Purple Bank!")

while True:

    initial_question = input("In order to open an account you must deposit $100, Do you have this amount to deposit 'Y' or 'N': ")
    initial_question = initial_question.lower()
    if initial_question == 'n':
        print("Thank you for your time!")
        break
    elif initial_question == 'y':
        first_name = input("Enter your First Name: ")
        middle_name = input("Enter your Middle Name: ")
        last_name = input("Enter your Last Name: ")
        if initial_question == 'y':
            status = "Open"

    account_type = input("Please enter what type of account you want to open, 'C' for Checking, 'S' for Savings or 'M' for Money Market: ")
    account_type = account_type.lower()

    account_balance = 0

    if account_type == 'c':
        account_type = 'Checking'
        account_balance = 100.00
    elif account_type == 's':
        account_type = 'Savings'
        account_balance = 100.00
    elif account_type == 'm':
        account_type = 'Money Market'
        account_balance = 100.00
    else:
        print("Invald Entry: Enter 'C', 'S', or 'M'")

    transaction = input("Do you want to 'D' deposit funds, 'W' withdraw funds, 'T' transfer funds or 'N' to quit:  ")
    transaction = deposit_funds.lower()

    if transaction == 'n':
        print("Thank You Again")
    while True:
        funds_amount = float(input("Enter the amount that you want to {0} :  ".format(transctions)))

        if transaction == 'd':
            transactions = "Deposit"
            account_balance = account_balance + funds_amount
            print("Your new balance is now {0}!".format(account_balance))
            return
        elif transaction == 'w':
            transctions = "Withdraw"
            account_balance = account_balance - funds_amount
            print("Your new balance is now {0}!".format(account_balance))
            return

        elif transaction == 't':
            transctions = "Transfer"
            account_balance = account_balance - funds_amount
            print("Your new balance is now {0}!".format(account_balance))
            return

    bank_account = BankAccount(first_name,middle_name,last_name,account_type,account_balance,status)

    account_info.append(bank_account)



print(bank_account.first_name)
print(bank_account.middle_name)
print(bank_account.last_name)
print(bank_account.account_type)
print(bank_account.account_balance)
print(bank_account.status)
