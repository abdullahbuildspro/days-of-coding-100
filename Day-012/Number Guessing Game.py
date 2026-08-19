import random
from artg import logo

easy_level = 10
hard_level = 5

def roy(u_user, c_user, total):
    """u_user is the user, and u_user is the computer."""
    if c_user > u_user:     # إذا كان تخمين الكمبيوتر أكبر من تخمين المستخدم
        print("Too Low!")
        return total - 1    # المتغير total سنستخدمه في عدد المحاولات
    elif c_user < u_user:   # إذا كان تخمين الكمبيوتر أصغر من تخمين المستخدم
        print("Too High!")
        return total - 1
    else:
        print(f"You got it! The answer was {c_user}.")


def function():     # هذه الوظيفة بتكون فيها عدد المحاولات على حسب الـlevel
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_level
    elif level == "hard":
        return hard_level


def play():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)       # هنا سيخمن الكمبيوتر رقما بين 1 و100
    print(f"Pssst, the correct answer is {answer}")

    turns = function()  # جعلنا عدد المحاولات التي في الوظيفة function موجودًا في المتغير turns

    guess = 0  # سنضع فيه الرقم الذي سيخمنه المستخدم
    while guess != answer:    # إذا كان التخمين لا يساوي الرقم الذي خمنه الكمبيوتر
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))         # خمن الرقم الصحيح
        turns = roy(u_user=guess, c_user=answer, total=turns)

        if turns == 0:   # إذا انتهى عدد المحاولات
            print("You've run out of guesses, you lose.")
            return     #  ستخرجنا من الدالة while وستخرجنا من الوظيفة أصلا
        elif guess != answer:  # وإن لم ينتهي فأعد المحاولة
            print("Guess again.")

play()