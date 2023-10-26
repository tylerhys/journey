from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))

Quiz = QuizBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print(f"You've completed the Quiz.\nYour final score is {Quiz.score}/{Quiz.question_number}")