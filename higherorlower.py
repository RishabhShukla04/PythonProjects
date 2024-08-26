import random
from game_data import data



def random_guy(account):
    name = account["name"]
    follower_count = account["follower_count"]
    description = account["description"]
    country = account["country"]
    return f"{name} from {country} who is a {description}"

def compare(a,b):
    if a > b:
        return "a"
    else:
        return "b"

def game():
    print("Welcome to higher or lower!")
    score = 0
    contGame = True
    while contGame:
        accountA = random.choice(data)
        accountB = random.choice(data)
        print(random_guy(accountA))
        print("VS")
        print(random_guy(accountB))

        guess = str(input(f"Who has more followers,A or B? ")).lower()
        comparison = compare(accountA["follower_count"],accountB["follower_count"])
        if comparison == guess:
            score += 1
            print("Correct!")
            print(f"Your current score is {score}")
            print("\n" * 20)
        else:
            print("You lose!")
            print(f"Your final score is {score}")
            contGame = False




game()

