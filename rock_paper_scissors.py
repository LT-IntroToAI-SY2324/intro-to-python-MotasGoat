
import random

player_choice = "rock"
computer_choice = "paper"

    
def get_choices():
        options = ["rock", "paper", "scissors"]
        player_choice = "scissors"
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices
choices = get_choices()
print(choices)