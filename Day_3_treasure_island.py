print("Welcome to Treasure Island\nYour mission is to find the treasure")

left_or_right = input("You are at a cross road. Where do you want to go \n'left' or 'right':- ").lower()
if left_or_right == "left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake \n would you like to 'swim' or 'wait':- ").lower()
    if swim_or_wait == "wait":
        door = input("you have three doors on your front choose one 'red', 'yellow' or 'blue':- ").lower()
        if door == "yellow":
            print("yaay!!! you Won")
        elif door == "blue":
            print("You got eaten by Beasts!!! Game Over")
        elif door == "red":
            print("You got Burned!!! Game Over")
        else:
            print("Game Over!!!!")
    else:print("You died!!! you are attacked by Trout!! Game Over")
else:
    print("You died by falling into a hole!!!! Game over")
