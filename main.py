import art
import random
from game_data import data

score = 0


def pick_account_a():
    account_a = data[random.randint(0, len(data))]
    account_a_followers = account_a.get("follower_count")
    return account_a, account_a_followers


def pick_account_b():
    account_b = data[random.randint(0, len(data))]
    account_b_followers = account_b.get("follower_count")
    return account_b, account_b_followers


print(f"""{art.logo}
\nWelcome to the higher/lower game!
\nGuess which account has more instagram followers:
""")

account_a, account_a_followers = pick_account_a()

while True:

    account_b, account_b_followers = pick_account_b()

    if account_a_followers == account_b_followers:
        continue

    if account_a_followers > account_b_followers:
        right_answer = "A"
    else:
        right_answer = "B"

    print(f"A: {account_a.get("name")}, a {account_a.get("description")}, from {account_a.get("country")}, "
          f"with {account_a.get("follower_count")} million followers")
    print(art.vs)
    print(f"B: {account_b.get("name")}, a {account_b.get("description")}, from {account_b.get("country")}")

    player_answer = input("\nWhich account has more followers? A or B?: ").strip().upper()

    if player_answer == right_answer:
        score += 1
        account_a = account_b
        account_b, account_b_followers = pick_account_b()
        print(art.logo)
        print(f"\nGuess which account has more instagram followers: ")
        continue
    else:
        break

print(f"\nGame over. Your score {score}.")
