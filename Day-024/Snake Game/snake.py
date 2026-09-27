# هنا كل ما يتعلق بأجزاء الثعبات وحركته وكل تفاصيله

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]

    def extend(self):  # إضافة جزء إلى الثعبان.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            ''' هنا الـ range الرقم الأول هو start، ثم الرقم الثاني هو stop، ثم الرقم الثالث هوstep، ولا يسمح بكتابتها كي لا يحدث خطأ'''
            '''هنا يوقف أشياء عن العمل كانت من المفترض أن تعمل هي الأولى فيأخرها، مثلا هنا: الجزء الاول من الثعبان يتوقف، ثم يتقدم الجزء الثالث خطوة ثم الثاني خطوة ثم الأول خطوة وهكذا'''
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # هذا يجعل الثعبان يتحرك للأمام، (أعد مشاهدة فيديو رقم 149 و 148 في اليوم 20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # إذا كنت تريد الاتجاه إلى أحداثيات معينة في الشاشة استخدم هذه الدالة

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

