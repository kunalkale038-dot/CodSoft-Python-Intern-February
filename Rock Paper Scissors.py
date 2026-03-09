# CODSOFT Python Internship
# Task 4 - Rock Paper Scissors Game

import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("----- Rock Paper Scissors Game -----")

while True:
    user_choice = input("\nEnter rock, paper, or scissors (or type 'exit' to quit): ").lower()

    if user_choice == "exit":
        print("\nGame Over!")
        print("Final Score:")
        print("User:", user_score)
        print("Computer:", computer_score)
        break

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)