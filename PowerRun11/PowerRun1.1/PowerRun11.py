import time
import random

# Boot Screen Animation
def boot_screen():
    print("Booting up Power Run 1.0...")
    for i in range(3):
        time.sleep(1)
        print("Loading" + "." * (i + 1))
    print("\nSystem Ready!\n")
    print("Power Run 1.0 Managed by: IPGC SOFTWARE BRANCH")
    print("All rights reserved. Copyright IPGC NETWORK - https://sites.google.com/moe-dl.edu.my/innerpower/home\n")

# Theme Selection
def select_theme():
    themes = {
        "green": "\033[92m",  # Green text
        "blue": "\033[94m",   # Blue text
        "amber": "\033[33m"    # Amber (yellow) text
    }
    print("Available Themes: Green, Blue, Amber")
    choice = input("Select Theme: ").lower()
    return themes.get(choice, "\033[92m")  # Default to green

# Mini-Games
def number_guess_game():
    print("\nWelcome to Number Guesser! Guess a number between 1 and 10.")
    secret = random.randint(1, 10)
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit() and int(guess) == secret:
            print("Correct! You win!\n")
            break
        else:
            print("Wrong! Try again.")

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("\nWelcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue
        cpu_choice = random.choice(choices)
        print(f"CPU chose {cpu_choice}!")
        if user_choice == cpu_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and cpu_choice == "scissors") or \
             (user_choice == "paper" and cpu_choice == "rock") or \
             (user_choice == "scissors" and cpu_choice == "paper"):
            print("You win!\n")
        else:
            print("You lose!\n")
        break

# Zenith AI Assistant
def zenith_ai():
    print("\n************************************")
    print("*       WELCOME TO ZENITH AI       *")
    print("************************************\n")
    print("Zenith: Hello! I am your AI assistant. How can I help you today?\n")
    while True:
        user_input = input("Zenith> ").strip().lower()
        if user_input in ["exit", "quit"]:
            print("Zenith: Goodbye!\n")
            break
        elif user_input in ["hello", "hi"]:
            print("Zenith: Hi there! How's it going?")
        elif user_input == "who are you":
            print("Zenith: I am Zenith, your AI assistant in Power Run 1.0!")
        elif user_input == "joke":
            jokes = [
                "Why don't programmers like nature? Because it has too many bugs!",
                "Why did the computer catch a cold? It left its Windows open!",
                "What do you call an AI that loves to chat? Me, Zenith!"
            ]
            print(f"Zenith: {random.choice(jokes)}")
        elif user_input == "time":
            print(f"Zenith: The current time is {time.strftime('%H:%M:%S')}.")
        elif user_input == "fact":
            facts = [
                "The first computer was invented in 1943.",
                "Python was created by Guido van Rossum in 1991.",
                "The human brain has more connections than all computers in the world combined!"
            ]
            print(f"Zenith: {random.choice(facts)}")
        else:
            print("Zenith: Sorry, I don't understand that command.")

# Show Controls
def show_controls():
    print("\nAvailable Commands:")
    print("  controls       - Show this list of commands")
    print("  admin         - Enter Admin Controls")
    print("  theme         - Change text theme (Green, Blue, Amber)")
    print("  games         - Play a mini-game (Number Guesser, Rock-Paper-Scissors)")
    print("  zenith        - Activate AI Assistant")
    print("  exit / quit   - Exit Power Run 1.0\n")

# Main Program
boot_screen()
theme = select_theme()
print(f"{theme}Welcome to Power Run 1.0!\033[0m\n")

while True:
    command = input("Syntax> ").strip().lower()
    if command in ["exit", "quit"]:
        print("Exiting Power Run 1.0...")
        break
    elif command == "controls":
        show_controls()
    elif command == "theme":
        theme = select_theme()
        print(f"{theme}Theme changed!\033[0m")
    elif command == "games":
        print("Available Games: 1. Number Guesser  2. Rock-Paper-Scissors")
        game_choice = input("Enter game number: ")
        if game_choice == "1":
            number_guess_game()
        elif game_choice == "2":
            rock_paper_scissors()
        else:
            print("Invalid choice.")
    elif command == "zenith":
        zenith_ai()
    else:
        print(f"{theme}Executing: {command}\033[0m")
