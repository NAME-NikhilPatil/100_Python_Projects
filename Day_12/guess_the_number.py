import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of number between 1 to 100")

max_guess = 5
guessed_number = random.randint(1, 100)
print(guessed_number)
guessed = False


def max_guessed(max_guess, guessed):
    if max_guess > 0:
        print(f"You have {max_guess} attempts to guess the number")
        input_guessed = int(input("Make a guess:"))
        if input_guessed == guessed_number:
            print("You won!")
            guessed = True
        elif input_guessed > guessed_number:
            print('Too high!')
            print(("Try again"))
            max_guess -= 1
            guessed = False

        elif input_guessed < guessed_number:
            print('Too low!')
            max_guess -= 1
            guessed = False
        else:
            print('Invalid guess')
            guessed = False


if input("Choose a difficulty lever:Type 'easy' or 'hard':") == 'hard':
    max_guess = 10
    while not guessed:
        max_guessed(max_guess, guessed)
elif input("Choose a difficulty lever:Type 'easy' or 'hard':") == 'easy':
    max_guess = 5
    while not guessed:
        max_guessed(max_guess, guessed)
else:
    print('Invalid guess!')
