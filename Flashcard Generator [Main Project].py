import sys
import cards_function
import time

#FLASHCARDS

def checking_cards():
    for i in range (2):
        while True:
            for dots in [".  ", ".. ", "..."]:
                print(f"\rLoading cards{dots}", end="", flush=True)
                time.sleep(0.5)
            break

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
                cards_function.load_cards()

            case "2":
                print("=============================================")
                cards_function.load_print_cards()
                cards_function.loading()

            case "3":
                print("=============================================")
                cards_function.review_cards(my_cards)
                cards_function.loading()

            case "4":
                cards_function.how_to_use()
                cards_function.loading()
                menu()

            case "X":
                while True:
                    for dots in [".  ", ".. ", "..."]:
                        print(f"\rExiting{dots}", end="", flush=True)
                        time.sleep(0.5)
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


cards_function.initialization()
time.sleep(1)
checking_cards()
print(f"\rLoaded {len(my_cards)} cards")
time.sleep(1)
print("=============================================")
print("Welcome to Flashcard Generator.")

selection()
time.sleep(1)
menu()