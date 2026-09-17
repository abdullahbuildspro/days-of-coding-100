import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(235, 233, 230), (231, 234, 238), (229, 235, 231), (238, 232, 235), (199, 161, 93), (64, 87, 126), (138, 91, 49), (136, 171, 194), (217, 208, 116), (129, 28, 52), (149, 54, 85), (134, 184, 147), (79, 22, 40), (45, 56, 101), (37, 41, 62), (187, 141, 160), (164, 157, 49), (181, 94, 109), (64, 122, 109), (52, 41, 37), (91, 152, 98), (82, 151, 163), (94, 120, 169), (45, 77, 70), (191, 90, 71), (73, 73, 43), (172, 206, 171), (177, 188, 214), (225, 174, 188), (168, 200, 211)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
