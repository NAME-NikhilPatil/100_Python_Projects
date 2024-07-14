import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


def check_answer(guess, answer, turns):
    """Check answer against guess, returns number of turns ramaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}")


def set_difficulty():
    level = input("Choose a difficulty lever:Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of number between 1 to 100")
    answer = random.randint(1, 100)
    # print(f"The Actual answer is {answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guess, You lose.")
            return
        elif guess != answer:
            print("Guess Again")


game()
