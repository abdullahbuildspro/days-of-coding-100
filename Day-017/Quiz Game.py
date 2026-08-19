from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # بنحطوا فيه الاسئلة الموجودة في ملف data
for question in question_data:
    question_text = question["question"]   # نضع صيغة السؤال في المتغير
    question_answer = question["correct_answer"] # نضع الجواب في المتغير
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")