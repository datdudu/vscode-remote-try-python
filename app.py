#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Define the valid options
options = ["rock", "paper", "scissors"]

# Define the scores
player_score = 0
computer_score = 0

# Define the game loop
while True:
    # Get the player's choice
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate the player's choice
    if player_choice not in options:
        print("Invalid option. Please choose rock, paper, or scissors.")
        continue

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Determine the winner
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")
        player_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    # Print the scores
    print(f"Player: {player_score}  Computer: {computer_score}")

    # Ask the player if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break


