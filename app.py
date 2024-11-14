import random

def coin_toss():
    user_choice = input("Choose Heads or Tails: ").lower()

    if user_choice not in ["heads", "tails"]:
        print("Invalid input! Please choose either 'Heads' or 'Tails'.")
        return

    toss_result = random.choice(["heads", "tails"])

    print(f"The coin landed on: {toss_result.capitalize()}")

    if user_choice == toss_result:
        print("You win!")
    else:
        print("You lose!")

coin_toss()
