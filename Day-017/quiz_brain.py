class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False
        # للاختصار اكتب:
        return self.question_number < len(self.question_list)  # ال_len هنا ستعطيني عدد الاسئلة في المتغير

    def next_question(self):
        current_question = self.question_list[self.question_number]  # هنا لنضع رقم السؤال
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}. ")

        #يمكنك كتابة هذا بدل آخر سطرين في ملف main
        # if self.question_number == len(self.question_list):
        #     print("You've completed the quiz!")
        #     print(f"Your final score is: {self.score}/{self.question_number}")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print(" ")


