
from turtle import Turtle, Screen  # استدعاء لمكتبة السلحفاة

# timmy is Object
# Turtle() is Class
timmy = Turtle()  # الـ Class له سمات تستفيد منها باستدعاء متغيرها
print(timmy)

# الـ shape والـ color والـ forward هنا هي عمليات للـ Class
timmy.shape("turtle")# اسم السلحفاة
timmy.color("coral") # لون السلحفاة
timmy.forward(100)   # تتقدم السلحفاة 100 خطوة

my_screen = Screen()  # الـ Screen() هما هي Class
print(my_screen.canvheight) # الـ canvheight هنا هي اسم سمة في الـ Class

# الـ exitonclick هنا هي عملية للـ Class
my_screen.exitonclick()   # تجعل الشاشة لا تغلق حتى تضغط على اي مكان في الشاشة

