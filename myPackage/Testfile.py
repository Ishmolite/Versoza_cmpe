
#SIMPLE DEMO OF ATM WITHDRAWAL FLOW

"""
welcome_message():
card_reader(isCardInserted): return isCardInserted
input_and_validate_pin_number() return isValid
transaction_selection() #withdraw, check balance, cancel transaction, return transaction
transaction_validation(amount) return isValid
card_ejection()
cash_Dispensing()
receipt_receipt()
"""

import time

amount = 5000
user1_balance = 10000.00
user1_pin = "123456"

def welcome_message():
    print("======================================")
    print("Welcome to Project Moon Bank!")
    print("'Go To Work, Spend Your Paycheck.'")
    print("======================================")
    time.sleep(1)
    print("Please insert your ATM card.")
    print("======================================")
    time.sleep(1)

def card_reader(isCardDetected):
    if isCardDetected.upper() == "YES":
        print("Card is inserted.")
        return True
    else:
        return False

def card_ejection():
    #Activates when attempts have reached maximum.
    print("======================================")
    print("Card is ejected, you may take your card from the ATM Card Slot.")
    print(" ")
    time.sleep(1)

def input_pin_number_and_validate():
    #Validation check for PIN
    for i in range (3):
        input_pin = input("Please Enter your PIN Number: ")
        if input_pin == user1_pin:
            time.sleep(0.5)
            print("PIN Number is valid.")
            return True
        else:
            print("Invalid PIN Number, Please try again. (Attempt " + str(i + 1) + ")")
    time.sleep(0.5)
    print("Attempt limit exceeded, transaction failed.")
    return False

def transaction_selection():
    print("======================================")
    print("Check Balance")
    print("Withdraw")
    print("Deposit")
    print("Cancel Transaction")
    print("======================================")
    transaction = input("Please Enter your Transaction of Choice: ")
    return transaction

def cash_dispense():
    #Code for Withdrawal
    print("Please get your cash now!")

def print_receipt(amount):
    global user1_balance #Recognized by the entire code
    user1_balance = user1_balance - amount #Recognized locally
    print("Thank you for working with us today!")
    print(" ")
    print("Cash dispensed : " + "$" + str(amount))
    print("Your New Balance : " + "$" + str(user1_balance))
    print(" ")
    time.sleep(1)
    print("Receipt printed, please get your receipt.")

def print_receiptDeposit(amountDeposit):
    global user1_balance #Recognized by the entire code
    user1_balance = user1_balance + amountDeposit #Recognized locally
    print("Thank you for working with us today!")
    print(" ")
    print("Cash deposited : " + "$" + str(amountDeposit))
    print("Your New Balance : " + "$" + str(user1_balance))
    print(" ")
    time.sleep(1)
    print("Receipt printed, please get your receipt.")


def transaction_validation(amount):
    global user1_balance

    if amount <= 0:
        print("Invalid amount.")
        return False

    if user1_balance > amount:
        print("Valid amount for withdrawal")
        return True
    else:
        print("Insufficient balance, please try again")
        return False

def transaction_validationDeposit(amountDeposit):
    global user1_balance

    if amountDeposit >= 0:
        print("Valid amount for depositing.")
        return True

    if amountDeposit <= 0:
        print("Invalid amount.")
        return False

while True:
    welcome_message()
    isCardDetected = input("Is the ATM Card Detected? (YES/NO) ")
    if not card_reader(isCardDetected): #Activates when the card is not inserted.
        print("Transaction failed, retrying...")
        time.sleep(2)
        continue

    if not input_pin_number_and_validate():
        time.sleep(1)
        print("======================================")
        card_ejection()
        time.sleep(1)
        continue

    transaction_selected = transaction_selection()
    if transaction_selected.upper() == "WITHDRAW":
        print("Transaction selected: WITHDRAWAL")
        time.sleep(1)
        print("======================================")
        print("Your Current Balance: " "$" + str(user1_balance))
        amount = int(input("Enter the amount to withdraw: "))
        if transaction_validation(amount):
            card_ejection()
            time.sleep(2)
            cash_dispense()
            time.sleep(1)
            print_receipt(amount)
            time.sleep(1)
        else:
            card_ejection()
            continue


    elif transaction_selected.upper() == "DEPOSIT":
        print("Transaction selected: DEPOSIT")
        print("======================================")
        print("Your Current Balance: " "$" + str(user1_balance))
        amountDeposit = int(input("Enter the amount to Deposit: "))
        if transaction_validationDeposit(amountDeposit):
            card_ejection()
            time.sleep(2)
            print_receiptDeposit(amountDeposit)
            time.sleep(1)
        else:
            print("Transaction cancelled.")
            card_ejection()
            continue

    elif transaction_selected.upper() == "CHECK BALANCE":
        print("Transaction selected: CHECK BALANCE")
        print("Your balance is: " + "Php" + str(user1_balance))
        time.sleep(1)
        card_ejection()
        continue
    else:
        print("Transaction cancelled.")
        card_ejection()
        continue