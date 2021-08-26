import random


def game(computer, player):
    if computer == "R":
        if player == "S":
            print("Computer Choose Rock \n You Choose Scissors.\n You Lose!")
        elif player == "P":
            print("Computer Choose Rock \n You Choose Paper. \n You Win!")
        else:
            print("You both choose Rock. \n It's a Tie")
    elif computer == "P":
        if player == "S":
            print("Computer Choose Paper \n You Choose Scissors \n You Win")
        elif player == "R":
            print("Computer Choose Paper \n You Choose Rock \n You Lose")
        else:
            print("You both choose Paper. \n It's a Tie")
    elif computer == "S":
        if player == "R":
            print("Computer Choose Scissors \n You Choose Rock \n You Win")
        elif player == "P":
            print("Computer Choose Scissors \n You choose Paper \n You Lose")
        else:
            print("You both choose Scissors \n It's a tie")
    else:
        pass


randNumber = random.randint(1, 3)
print("Computer's Turn: Rock(R) Paper(P) Scissors(S): \n")
computerPlay = str()
if randNumber == 1:
    computerPlay = "R"
elif randNumber == 2:
    computerPlay = "P"
elif randNumber == 3:
    computerPlay = "S"

playerInput = input("Your Turn: Rock(R) Paper(P) Scissors(S): \n")

game(computerPlay, playerInput)

