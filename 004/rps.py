"""Day 004 - Rock Paper Scissors"""

import random
import sys

_rps = ["R", "P", "S"]
_user_wins = [("R", "S"), ("P", "R"), ("S", "P")]


def play() -> None:
    """Play a game of Rock Paper Scissors"""

    user_choice = input("Choose [R]ock, [P]aper, or [S]cissors: ").capitalize()
    computer_choice = _rps[random.randint(0, len(_rps) - 1)]
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice, computer_choice) in _user_wins:
        print("You win!")
    else:
        print("You lose!")

    sys.exit(0)


if __name__ == "__main__":
    play()
