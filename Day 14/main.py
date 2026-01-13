import random
from Game_data import data

score = 0
def get_name(current_question="Instagram"):
    data_list = random.choice(data)
    while current_question == data_list["name"]:
        data_list = random.choice(data)
    return  data_list

def check_answer(question_1,question_2):
    if question_1["follower_count"] > question_2["follower_count"]:
        return "A"
    else:
        return  "B"

question = random.choice(data)
first_question =get_name(question["name"])
second_question = get_name(first_question["name"])

game_is_on = True
while game_is_on:
    print(f"Compare A: {first_question["name"]}, a {first_question["description"]}, from {first_question["country"]}")
    print("VS")
    print(f"Compare B: {second_question["name"]}, a {second_question["description"]}, from {second_question["country"]}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_answer == check_answer(first_question,second_question):
        first_question = second_question
        second_question = get_name(first_question["name"])
        score += 1
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_is_on = False
