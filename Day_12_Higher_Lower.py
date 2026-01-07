import random

levels = {
    "easy" : 10,
    "hard": 5
}

number = random.randint(1,100)


print("welcome to the number guessing game!")
print("I'm thinking of number number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
lives = levels[difficulty]

while lives > 0:
    print(f"You have {lives} attempts left to guess the number. ")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You won! The answer was {number}")
        lives = 0

    elif guess > number:
        print("Too high")

    else:
        print("Too low")
    lives -= 1


