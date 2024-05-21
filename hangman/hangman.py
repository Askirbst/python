import string
import random
import re


def main():

    word_list = []

    wrong_guesses = 0
    wrong_letters = ""

    head = ""
    arms = ""
    legs = ""

    with open('words.txt', "r") as file:
        for line in file:
            word_list.append(line.strip())

    random_word = str.lower(random.choice(word_list))
    word_length = len(random_word)

    letter_list = [""] * word_length

    found = False
    while not found:
        while True:
            user_letter = input("Guess a letter\n")
            if user_letter.isalpha() and len(user_letter) == 1:
                break

        result = checkguess(random_word, user_letter, wrong_guesses, letter_list, wrong_letters)
        letter_list, wrong_guesses, wrong_letters = result

        word_match = "".join(letter_list)

        body_parts = drawman(wrong_guesses, head, arms, legs)
        head, arms, legs = body_parts

        printmatch(word_match)
        print(f"Wrong letters: {wrong_letters}")

        if wrong_guesses == 6:
            print("Sorry, you lose.")
            print(f"The word was {random_word}")
            return

        if random_word == word_match:
            print("You Won!")
            found = True

    return


def checkguess(random_word, user_letter, wrong_guesses, letter_list, wrong_letters):

    index = 0
    correct = 0

    for c in random_word:
        if c == user_letter:
             letter_list[index] = user_letter
             correct += 1
        elif letter_list[index] == "":
              letter_list[index] = " "
        index += 1

    if correct == 0:
        wrong_letters = wrong_letters + user_letter
        wrong_guesses += 1

    return letter_list, wrong_guesses, wrong_letters


def drawman(wrong_guesses, head, arms, legs):

    if wrong_guesses == 1:
        head = "☺"
    if wrong_guesses == 2:
        arms = " |"
    if wrong_guesses == 3:
        arms = "/|"
    if wrong_guesses == 4:
        arms = "/|\\"
    if wrong_guesses == 5:
        legs = "/"
    if wrong_guesses == 6:
        legs = "/ \\"

    drawhanger(head, arms, legs)
    return head, arms, legs


def printmatch(word_match):

    for c in word_match:
        if c.isalpha():
            print(f'\033[42m{c}', end='')
        else:
            print('\x1b[0m_', end='')
    print('\x1b[0m')


def drawhanger(head, arms, legs):

    print("   ___")
    print("  |   |")
    print(f"  |   {head}")
    print(f"  |  {arms}")
    print(f"  |  {legs}")
    print("  |")
    print("__|__")


main()
