print("Welcome to Python Pizza Deliveries")
bill = 0

size = input("What size Pizza do you want? S, M or L : ")
pepperoni = input("Do you want pepperoni in your pizza? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:           # هادي زايدة ومعناها لو كتب شي غلط يقوله مدخلاتك خاطئة
    print("You typed the wrong inputs")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")