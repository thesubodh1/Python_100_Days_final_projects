import random


print("This is Rock, Paper, Scissor!!")
computer_choice = random.choice(["Rock","Paper","Scissor"])

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor:- "))

if user_choice == 0:
    if computer_choice == "Rock":
        print("It's a Draw! You both chose Rock")

    elif computer_choice == "Paper":
        print("You lost! Computer choose Paper")

    else:
        print("You won! Rock breaks Scissor")

elif user_choice == 1:
    if computer_choice == "Rock":
        print("You Won! Paper Covers Rock")

    elif computer_choice == "Paper":
        print("Its a Draw! You both choose Paper")

    else:
        print("You lost! Computer choose Scissor")

elif user_choice == 2:
    if computer_choice == "Rock":
        print("You Lost! Computer chose Rock")

    elif computer_choice == "Paper":
        print("You won! Scissor cute Paper")

    else:
        print("Its a Draw! You both choose Scissor")

else:
    print("Please choose a number between 0,1 and 2")


