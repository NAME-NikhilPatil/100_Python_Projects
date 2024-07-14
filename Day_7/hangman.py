# Step 1
import random

from Day_7.hangman_art import stages, logo
from Day_7.hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

print(logo)

print(f"Choose word is {chosen_word}")

display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word,You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost!")

    if "_" not in display:
        end_of_game = True
        print("You Won!")

    print(stages[lives])
