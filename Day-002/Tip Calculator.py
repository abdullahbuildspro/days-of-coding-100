# انشاء اله حاسبة
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
# total_bill = float(total_bill)
give = int(input("How much tip would you like to give? "))
# give = int(give)
peaple = int(input("How many peaple to split the bill? "))
# peaple = int(peaple)
give1 = give / 100
total_bill1 = total_bill * give1 + total_bill
# give1 = give / 100 * total_bill + total_bill     للاختصار
total_bill2 = total_bill1 / peaple
total_bill3 = round(total_bill2, 2)
print(f"Each person should pay: ${total_bill3}")