import random

RANDOM_NUMBER = random.randint(1, 100)
EASY_GUESS = 10
HARD_GUESS = 5


def answercheck():
    difficulty = str(input("Choose a difficulty level. Type 'easy' or 'hard': ")).lower()
    guesses = 0
    if difficulty == 'easy':
        guesses = EASY_GUESS
    elif difficulty == 'hard':
        guesses = HARD_GUESS
    print(f"You have {guesses} guesses.")
    while guesses > 0:
        guess = int(input("Guess a number: "))
        if guess > RANDOM_NUMBER:
            print("Too high!")
            guesses -= 1
            print(f"You have {guesses} guesses left.")
        elif guess < RANDOM_NUMBER:
            print("Too low!")
            guesses -= 1
            print(f"You have {guesses} guesses left.")
        elif guess == RANDOM_NUMBER:
            print("You got it!")
            break
    if guesses == 0:
        print("You lose!")




def playGame():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(RANDOM_NUMBER)
    answercheck()



playGame()

