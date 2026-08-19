import random
from artv import logo, vs
from game_data import data

num = 0
ter_a = []
check = True

# يختار عشوائي من القائمة
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

print(logo)

while check:
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare A: {format_data(account_b)}")

    a = account_a["follower_count"]
    b = account_b["follower_count"]

    toi = input("Who has more followers? Type 'A' or 'B: ").lower()

    if a > b:
        if toi == "a":
            num += 1
            print("\n" * 50)
            print(logo)
            print(f"You're right! Current score: {num}.")
        else:
            print("\n " * 50)
            print(f"Sorry, that's wrong. Final score: {num}")
            check = False
    else:
        if toi == "b":
            num += 1
            print("\n" * 50)
            print(logo)
            print(f"You're right! Current score: {num}.")
        else:
            print("\n " * 50)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {num}")
            check = False

