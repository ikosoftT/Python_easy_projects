# Logic Flow
# 1 - Display Options to User
# 1 - Check User Option if Valid Go to Next else Break
# 1 - Generat Computer Option
# 1 - check Winer(UserOp, Com_Op)

import random
import sys


def check_winner(user, computer):
    if user == computer:
        print("Draw.")
    elif user == "paper" and computer == "rock":
        print(f"User Won! {user} beats {computer}")
    elif user == "Sescor" and computer == "paper":
        print(f"User Won! {user} beats {computer}")
    elif user == "rock" and computer == "Sescor":
        print(f"User Won! {user} beats {computer}")
    else:
        print(f"Computer Won! {computer} Beats {user}")

def game():
    print("\nWelcome To EasyGame!\n")
    print("1 - Paper\n")
    print("2 - Sescor\n")
    print("3 - Rock\n")
    print("4 - Exit\n")

    user_option = int(input('Please Choose one of above\n'))

    # Check User
    if user_option not in [1,2,3,4]:
        print(f"{user_option} is Out of Range!")
        sys.exit(1)
    if user_option == 4:
        print("Happy Coding!!")
        sys.exit(1)

    options = ["paper", "Sescor", "rock"]

    user = options[user_option - 1]
    computer = options[random.randint(0,2)]
    # Check Winner
    check_winner(user, computer)



if __name__ == "__main__":
    game()
