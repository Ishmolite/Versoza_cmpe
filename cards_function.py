import json
import os

FILENAME = "saved_flashcard.json"

def load_cards():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def load_print_cards():

    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            cards = json.load(f)
    else:
        print(" 😔 There are currently no cards.")
        return
    for card in cards:
            print("-----")
            print(f"Term: {card['term']}")
            print(f"Definition: {card['definition']}")

def save_cards(cards):
    with open(FILENAME, "w") as f:
        json.dump(cards, f, indent=4)
    print("> ✅ Flashcards saved successfully!")


def create_card(cards):
    print("--- CREATING NEW CARD ---")
    term = input("Enter the Term: ")
    definition = input("Enter the Definition: ")

    new_card = {"term": term, "definition": definition}
    cards.append(new_card)

    save_cards(cards)

def review_cards(cards):
    if not cards:
        print(" ❗ There are no cards to review!")
        return

    print("--- REVIEWING CARDS ---")
    for card in cards:
        print(f"TERM: {card['term']}")
        input("Press Enter to flip...")
        print(f"DEFINITION: {card['definition']}")
        print("-" * 20)

def how_to_use():
    print("=============================================")
    print("--- HOW TO USE ---")
    print("❓ Entering the value of '1' allows you to create your own flashcards.")
    print("\t>> From there, simply provide a term and its definition. It will automatically save each card.", )
    print("❓ Entering the value of '2' allows you to check your existing flashcards.")
    print("\t>> This shows you the flashcards you have already made.")
    print("❓ Entering the value of '3' allows you to review your own flashcards.")
    print("\t>> This allows you to review your flashcards, by showing the definition first before the definition.")
    print("❓ Entering the value of '4' allows you to view this tutorial page.")
    print("❓ Entering the value of '?' shows the available choices again.")
    print("❓ Entering the value of 'X' closes the program.")



