print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
        bill = 5
    elif age > 30:
        print("Please pay $20")
        bill = 20
    elif age > 18:
        print("Please pay $12")
        bill = 12
    elif age >= 45 and age <= 55:
   #elif 45 <= age <= 55:        اختصار للكود اللي قبله
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Please pay $7")
        bill = 7
    photo = input("Do you want to have a photo? (y/n) ")
    if photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")