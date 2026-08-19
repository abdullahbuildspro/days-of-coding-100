
import artr
print(artr.logo)

def find_highest_bider(bidding_dictionary):
    winner = ""  # فارغ لكي نضع فيه اسم الرابح
    highest_bid = 0  # سنضع فيه أكبر قيمة
    for bidder in bidding_dictionary:  # سنمرر بالمفتاح على المتغير bidder كل مرة مفتاح إلى النهاية
        bid_amount = bidding_dictionary[bidder]  # في هذا المتغير bid_amount ستكون فيه قيمة كل مفتاح بالواحد
        if bid_amount > highest_bid:  # إذا كان هذا الرقم الذي في المتغير bid_amount أكبر من الرقم الذي في المتغير highest_bid
            highest_bid = bid_amount  # bid_amountفاجعل المتغير highest_bid فيه أكبر قيمة وهو الذي في المتغير
            winner = bidder  # ضع اسم أكبر صاحب رقم

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
continue_bedding = True
while continue_bedding:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    bids[name] = price  # يضيف الاسم وهو المفتاح الى القاموس مع قيمته
    should_continue = input("are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue == 'no':
        continue_bedding = False
        find_highest_bider(bids)  # استدعاء للوظيفة ووضع فيها الذي في المتغير bids
    elif should_continue == 'yes':
        print("\n" * 20)  # سيطبع 20 سطر فارغ


