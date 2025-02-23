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

# Show Controls
def show_controls():
    print("\nAvailable Commands:")
    print("  controls       - Show this list of commands")
    print("  admin         - Enter Admin Controls")
    print("  theme         - Change text theme (Green, Blue, Amber)")
    print("  games         - Play a mini-game (Number Guesser, Rock-Paper-Scissors)")
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
    else:
        print(f"{theme}Executing: {command}\033[0m")
