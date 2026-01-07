import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = []
computer_cards = []
game_is_on = False

for _ in range(2):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

def fetch_card():
    return random.choice(cards)

def calculate_score(cards_lists):
    return sum(cards_lists)

def deal_computers_card():
    if calculate_score(computer_cards) < 17:
        computer_cards.append(fetch_card())

def winner(user_score,computer_score):
    if computer_score > 21:
        return f"you won computer went over, your final card:{user_cards}, score : {calculate_score(user_cards)} \n computers final card:{computer_cards}, score: {calculate_score(computer_cards)}"
    elif user_score == 21:
        return f"You won,your final card:{user_cards}, score : {calculate_score(user_cards)} \n computers final card:{computer_cards}, score: {calculate_score(computer_cards)}"
    elif computer_score == 21:
        return f"computer won,your final card:{user_cards}, score : {calculate_score(user_cards)} \n computers final card:{computer_cards}, score: {calculate_score(computer_cards)}"
    elif user_score > computer_score:
        return f"you won,your final card:{user_cards}, score : {calculate_score(user_cards)} \n computers final card:{computer_cards}, score: {calculate_score(computer_cards)}"
    elif user_score < computer_score:
        return f"computer won,your final card:{user_cards}, score : {calculate_score(user_cards)} \n computers final card:{computer_cards}, score: {calculate_score(computer_cards)}"
    else:
        return f"the table won,your final card:{user_cards}, score : {calculate_score(user_cards)} \n computers final card:{computer_cards}, score: {calculate_score(computer_cards)}"


play = input("Do you want to play the game of blackjack? type 'y' or 'n': ").lower()
if play == 'y':
    game_is_on = True

while game_is_on:
    print(f"Your cards:{user_cards}, current score : {calculate_score(user_cards)}")
    print(f"Computers first card: {computer_cards[0]}")
    if calculate_score(user_cards) < 21:
        again = input("Type 'y' to get another card, type 'n' to pass.").lower()
        if again == 'y':
            user_cards.append(fetch_card())

        else:
            deal_computers_card()
            print(winner(calculate_score(user_cards),calculate_score(computer_cards)))
            game_is_on = False
    elif calculate_score(user_cards) > 21:
        print(f"you lost!! you went over, your final card:{user_cards}, score : {calculate_score(user_cards)} \n computers final card:{computer_cards}, score: {calculate_score(computer_cards)}")
        game_is_on = False

    else:
        deal_computers_card()
        print(winner(calculate_score(user_cards), calculate_score(computer_cards)))
        game_is_on = False















