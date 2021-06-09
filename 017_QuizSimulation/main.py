from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random, os
from art import logo

question_bank = []
os.system("clear")
print(logo)
print("Welcome to Computer Trivia Game!\n")
for entry in random.choices(question_data,k=10):
    question_bank.append(Question(entry["question"], entry["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed the quiz.\nYour final score is: {quiz.score}/{len(quiz.question_list)}.")