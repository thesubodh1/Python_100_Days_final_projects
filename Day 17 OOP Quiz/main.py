from quiz_brain import QuizBrain
from  question_model import Question
from data import  question_data

question_bank = []

for question in question_data:
    question_text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(question_text,answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print("Yaay!! you have completed this quiz")
print(f"print your final score is {quiz.score}")