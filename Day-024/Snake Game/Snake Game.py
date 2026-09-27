# هنا اللعبة كاملة وتجمع أجزائها من الملفات التي سأستدعيها

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")    # لتغيير لون الخلفية
screen.title("My Snake Game")  # لوضع عنوان للشاشة يظهر فوق في الاطار
screen.tracer(0)  # هذه خاصية التتبع توقف عمل البرنامَج حتى تستدعي خاصية التحديث ليكون كل شيء مترابطًا ببعض

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # خاصية التحديث، يتم استدعائها لعمل البرنامَج متتابع بعد أن تحدث كل الأوامر التي قبلها
    time.sleep(0.1)  # تفصل البرنامَج عن العمل مدة ثانية ثم تجعل الذي بعدها يعمل
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:  # إذا لامس رأس الثعبان الطعام فإنه يعيد إنشاء طعام جديد في مكان عشوائي
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: # إذا لامس رأس الثعبان الحائط فإنه يعيد إنشاء طعام جديد في مكان عشوائي
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()