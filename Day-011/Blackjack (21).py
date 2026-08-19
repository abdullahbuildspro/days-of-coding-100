

import random
from artb import logo


def deal_card():   # هذه الوظيفة فيها البطاقات وتوزيع البطاقات
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]   # قائمة البطاقات
    card = random.choice(cards)  # توزيع البطاقات بشكل عشوائي
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:    # لو كان عنده بطاقتين ومجموعهم 21 يعني كان عنده 11 و 10
        return 0  # اجعل النتيجة 0

    if 11 in cards and sum(cards) > 21:  # لو كان عنده بطاقة 11 ومجموع بطاقاته فوق 21
        cards.remove(11)   # احذف البطاقة 11 من القائمة
        cards.append(1)    # حط بدلها بطاقة رقم 1

    return sum(cards)     # مجموع بطاقات اللاعب


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:    # إذا كانت بطاقاتهم نفس العدد
        return "Draw 🙃\n"
    elif c_score == 0:        # إذا كان بطاقة الكمبيوتر 0 يعني عنده 11 و 10
        return "\nLose, opponent has Blackjack 😱\n"
    elif u_score == 0:        # اذا كان بطاقة المستخدم 0 يعني 11 و 10
        return "\nWin with a Blackjack 😎\n"
    elif u_score > 21:        # اذا كان مجموع بطاقات المستخدم 21
        return "\nYou went over. You lose 😭\n"
    elif c_score > 21:        # اذا كان مجموع بطاقات الكمبيوتر 21
        return "\nOpponent went over. You win 😁\n"
    elif u_score > c_score:   # اذا كان مجموع بطاقات المستخدم أعلى من الكمبيوتر
        return "\nYou win 😃\n"
    else:
        return "\nYou lose 😤\n"


def play_game():  # هادي وظيفة اللي فيها اللعبة واساس اللعبة
    print(logo)
    user_cards = []       # فيها بطاقات اللاعب
    computer_cards = []   # فيها بطاقات الكمبيوتر
    computer_score = -1   # لا أعلم لماذا -1 هنا توضع مجموع البطاقات الكمبيوتر
    user_score = -1       # لا أعلم لماذا -1 هنا توضع مجموع البطاقات اللاعب
    is_game_over = False  # لأجل الدالة while

    for _ in range(2):  # كرر الاوامر مرتين ( لا يوجد متغير جديد لأن أني ما عندي ما ندير بمتغير حديد، نبيه فقط يكرر الاوامر مرتين )
        user_cards.append(deal_card())       # اعط للاعب بطاقتين
        computer_cards.append(deal_card())   # اعط للكمبيوتر بطاقتين

    while not is_game_over:             # اذا لم يكن المتغير True
        user_score = calculate_score(user_cards)       # user_score مجموع بطاقات اللاعب حطهم في المتغير
        computer_score = calculate_score(computer_cards)  # computer_score بطاقات الكمبيوتر حطهم في المتغير
        print(f"Your cards: {user_cards}, current score: {user_score}")  # بطاقات اللاعب ... ، ومجموعهم ...
        print(f"Computer's first card: {computer_cards[0]}")        # البطاقة الاولى للكمبيوتر هي ...

        if user_score == 0 or computer_score == 0 or user_score > 21:  # اذا كان مجموع بطاقات اللاعب أو المستخدم 0 أو كان اللاعب مجموع بطاقاته فوق 21
            is_game_over = True     # انتهت اللعبة
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")   # اسأله يبي بطاقة تانية والا لا
            if user_should_deal == "y":   # لو قال يبي
                user_cards.append(deal_card())  # اعطيه بطاقة ( الوظيفة deal_card هي المسؤولة على توزيع البطاقات )
            else:
                is_game_over = True   # لو ما يبيش بطاقة خلاص

    while computer_score != 0 and computer_score < 17:  # اذا كانت بطاقات الكمبيوتر لا تساوي 0 وكانت أقل من 17
        computer_cards.append(deal_card())    # اعط الكمبيوتر بطاقة تانية
        computer_score = calculate_score(computer_cards)  # ضيف البطاقة الجديدة للمجموع

    print(f"Your final hand: {user_cards}, final score: {user_score}")  # النتيجة الاخيرة: بطاقات اللاعب هي ... ومجموعهم ...
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")  # بطاقات الكمبيوتر هي ... ومجموعهم ...
    print(compare(user_score, computer_score))  # computer_score استدع وظيفة الرابح والخاسر وحط في المتغير الاول المتغير user_score ، وفي المتغير الثاني المتغير


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":  # اسأله هل يبي يلعب مرة تانية، لو قال نعم:
    print("\n" * 20)
    play_game()  # استدعاء لوظيفة اللعية


