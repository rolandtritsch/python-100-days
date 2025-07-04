"""Day 004 - Rock Paper Scissors"""

import random
import sys

RPS = ["R", "P", "S"]
USER_WINS = [("R", "S"), ("P", "R"), ("S", "P")]


def play() -> None:
    """Play a game of Rock Paper Scissors"""

    user_choice = input("Choose [R]ock, [P]aper, or [S]cissors: ").capitalize()
    computer_choice = RPS[random.randint(0, len(RPS) - 1)]
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice, computer_choice) in USER_WINS:
        print("You win!")
    else:
        print("You lose!")

    sys.exit(0)


if __name__ == "__main__":
    play()
