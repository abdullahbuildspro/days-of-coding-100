import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_og_gab):
    for _ in range(int(360 / size_og_gab)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_og_gab)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()