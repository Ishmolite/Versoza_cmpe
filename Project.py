import time
import os
import json
import sys
import cards_function


#FLASHCARDS

def selection():

    print("=============================================")
    print("")
    print("\t> ✏️ Generate Own Flashcards [1]")
    print("\t> 📝 Check Existing Flashcards [2]")
    print("\t> 📚 Review My Flashcards [3]")
    print("\t> ❓ How To Use [4]")
    print("")
    print("\t> 🏃 Exit [X]")
    print("")

def menu():
    while True:

        print("=============================================")
        selector = input("What would you like to do today? ")

        match selector.upper():
            case "1":
                print("=============================================")
                cards_function.create_card(my_cards)
                time.sleep(2)

            case "2":
                print("=============================================")
                cards_function.load_print_cards()
                time.sleep(2)

            case "3":
                print("=============================================")
                cards_function.review_cards(my_cards)
                time.sleep(2)

            case "4":
                cards_function.how_to_use()
                time.sleep(5)
                menu()

            case "X":
                print("Exiting...")
                time.sleep(1)
                sys.exit()

            case "?":
                print("=============================================")
                print("")
                print("\t> ✏️ Generate Own Flashcards [1]")
                print("\t> 📝 Check Existing Flashcards [2]")
                print("\t> 📚 Review My Flashcards [3]")
                print("\t> ❓ How To Use [4]")
                print("")
                print("\t> 🏃 Exit [X]")
                print("")


            case _:
                print("Please input a number value, otherwise, enter 'X' to exit.")

my_cards = cards_function.load_cards()

print("Initializing code...")
time.sleep(1)
print("Checking for cards...")
time.sleep(0.9)
print(f"Loaded {len(my_cards)} cards.")
time.sleep(1)
print("=============================================")
print("Welcome to Flashcard Generator.")

selection()
time.sleep(1)
menu()