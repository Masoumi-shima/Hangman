# using random word generator
# from random_word import RandomWords

# random_words = RandomWords()
# print(random_words.get_random_word())
import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word = word.upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:

        print("You have already used: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in word!")

        elif user_letter in used_letters:
            print("You have already used that letter! Please try again.")

        else:
            print("Invalid character!")
    if lives == 0:
        print("You died!")
    else:
        print("You won! The word is: ", word)


hangman()
