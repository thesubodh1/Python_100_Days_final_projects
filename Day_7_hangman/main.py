import random
import hangman_art
import hangman_word

print(hangman_art.logo)

lives = 6
guessed_list = []
words = hangman_word.word_list
chosen_word = random.choice(words)
print(chosen_word)

dashed = ["_" for _ in chosen_word]
to_guess = "".join(dashed)
print(f"word to guess: {to_guess}")
game_over = False
while not game_over:
    display = ""
    user_guess = input("Guess a letter: ")
    if user_guess in guessed_list:
        print(f"You have already guessed the letter {user_guess}")
    for letter in chosen_word:
        if letter == user_guess:
            display += user_guess
            guessed_list.append(user_guess)
        elif letter in guessed_list:
            display += letter
        else:
            display += "_"


    if user_guess not in chosen_word:
        lives -= 1
        print(f"you have guessed {user_guess} that is not on the list. You lose a life")

        if lives == 0:
            game_over = True
            print("Sorry you lost the game")
            print(f"The correct word was: {chosen_word}")

    print(f"{lives}/6 lives left")


    if "_" not  in display:
        game_over = True
        print("you won Yaay!!!!")
        print(f"you Successfully guessed the word {chosen_word}")

    print(hangman_art.stages[lives])
    print(f"word to guess:{display}")


