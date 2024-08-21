import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_total(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def blackjack():

    dealer_cards = []
    user_cards = []
    dealer_total = -1
    user_total = -1
    contGame = True

    for num in range(2):
        dealer_cards.append(deal_cards())
        user_cards.append(deal_cards())

    while contGame:
        print(f"dealer card is: {dealer_cards[0]}")
        print(f" your cards are {user_cards}")
        dealer_total = calculate_total(dealer_cards)
        user_total = calculate_total(user_cards)

        if user_total == 0 or dealer_total == 0 or user_total > 21:
            contGame = False
        else:
            another_card = str(input("Do you want to get another card (y/n)")).lower()
            if another_card == "y":
                user_cards.append(deal_cards())
            else:
                contGame = False

    while dealer_total != 0 and dealer_total < 17:
        dealer_cards.append(deal_cards())
        dealer_total = calculate_total(dealer_cards)

        print(f"dealer cards is: {dealer_cards}")
        print(f" your cards are {user_cards}")
        if user_total == dealer_total:
            print("Draw")
        elif dealer_total == 0:
            print("Lose, opponent has Blackjack")
        elif user_total == 0:
            print("Win with a Blackjack")
        elif user_total > 21:
            print("You lose")
        elif dealer_total > 21:
            print("You win")
        elif user_total > dealer_total:
            print("You win")
        else:
            print("You lose")




ans = str(input("Do you want to play blackjack\n"))
if ans == "y":
    blackjack()
