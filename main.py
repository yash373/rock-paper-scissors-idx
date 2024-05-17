from user import User
from comp import Comp

# Scissors -> 1
# Rock -> 2
# Paper -> 3

def eval(comp, user):
    if comp == user:
        return -1
    if comp == 1 and user == 2:
        return 1
    if comp == 2 and user == 3:
        return 1
    if comp == 3 and user == 1:
        return 1
    if comp == 2 and user == 1:
        return 2
    if comp == 3 and user == 2:
        return 2
    if comp == 1 and user == 3:
        return 2

def display_score(comp,user,win_msg):
    print(f"Computer: {comp.score}")
    print(f"Player: {user.score}")
    if comp.score == user.score:
        pass
    elif comp.score > user.score:
        print(f"Computer {win_msg}")
    elif user.score > comp.score:
        print(f"Player {win_msg}")

turns = int(input("Enter the number of turns you want to play for: "))
computer = Comp()
player = User()
assets = ["Scissors","Rock","Paper"]

for i in range(turns):  
    # take inputs
    user_input = player.get_user_input()
    computer_input = computer.pick()
    print(f"Computer picked: {assets[computer_input-1]}")

    # change scores
    result = eval(computer_input, user_input)
    if result == -1:
        print("Draw")
        computer.increase_point()
        player.increase_point()
    if result == 1:
        player.increase_point()
    if result == 2:
        computer.increase_point()

    # display score
    display_score(comp=computer, user=player, win_msg="is in the lead")

# display score
display_score(comp=computer, user=player, win_msg="has won!")