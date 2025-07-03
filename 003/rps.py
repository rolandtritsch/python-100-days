import random

_rps = ["R", "P", "S"]
_win = [("R", "S"), ("P", "R"), ("S", "P")]

def play():
    user_choice = input("Choose [R]ock, [P]aper, or [S]cissors: ").capitalize()
    computer_choice = _rps[random.randint(0, 2)]
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif _win.__contains__((user_choice, computer_choice)):
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    play()
