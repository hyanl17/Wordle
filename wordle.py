import string
from random import random

def get_random(list):
    '''
    this function gets a random word from a list
    '''
    index_length = len(list)
    index = int(index_length*random())
    word = list[index]
    return word

def clear():
    '''
    this function clears the terminal
    '''
    print("\033c", end = '')

def new_line():
    '''
    this function prints a new line
    '''
    print('\n')

word_length = 5

with open('/usr/share/dict/words') as file:
    word_list = []
    words = file.read().split(new_line())
    for word in words:
        if len(word) == word_length and word.islower():
            word_list.append(word.strip())

guess = ''
guessed_word_list = []

random_word = get_random(word_list)
low_alphabet = list(string.ascii_lowercase)

number_of_guesses = 0
total_number_of_guesses = 6
number_of_uses_of_help = 0

clear()
print('Enter "help" for instructions on how to play')

while guess != random_word and number_of_guesses < 6:
    guess = input('Enter your guess: ').lower()
    if guess == 'help':
        clear()
        with open('README.md') as help_file:
            help = help_file.read()
            print(help)
        for guess_word in guessed_word_list:
            for index in range(len(guess_word)):
                if guess_word[index] == random_word[index]:
                        print(f'\033[30;42m {guess_word[index]} \033[0m', end = '')
                elif guess_word[index] in random_word:
                        print(f'\033[30;43m {guess_word[index]} \033[0m', end = '')
                else:
                        print(f'\033[30;100m {guess_word[index]} \033[0m', end = '')
            new_line()
        print(f'Guesses remaining: {total_number_of_guesses}')
    else:
        number_of_letters = 0
        non_letter_character_list = []
        for letter in guess:
            number_of_letters += 1
            if low_alphabet.count(letter) < 1:
                non_letter_character_list.append(letter)
        if len(non_letter_character_list) > 0:
            clear()
            for guess_word in guessed_word_list:
                for index in range(len(guess_word)):
                    if guess_word[index] == random_word[index]:
                        print(f"\033[30;42m {guess_word[index]} \033[0m", end = '')
                    elif guess_word[index] in random_word:
                        print(f"\033[30;43m {guess_word[index]} \033[0m", end = '')
                    else:
                        print(f"\033[30;100m {guess_word[index]} \033[0m", end = '')
                new_line()
            print(f'"{guess}" includes non-letter character(s): {non_letter_character_list}, try again')
            print(f'Guesses remaining: {total_number_of_guesses}')
        elif len(guess) < word_length:
            clear()
            for guess_word in guessed_word_list:
                for index in range(len(guess_word)):
                    if guess_word[index] == random_word[index]:
                        print(f"\033[30;42m {guess_word[index]} \033[0m", end = '')
                    elif guess_word[index] in random_word:
                        print(f"\033[30;43m {guess_word[index]} \033[0m", end = '')
                    else:
                        print(f"\033[30;100m {guess_word[index]} \033[0m", end = '')
                new_line()
            print(f'"{guess}" is less than 5 letters long, try again')
            print(f'Guesses remaining: {total_number_of_guesses}')
        elif len(guess) > word_length:
            clear()
            for guess_word in guessed_word_list:
                for index in range(len(guess_word)):
                    if guess_word[index] == random_word[index]:
                        print(f"\033[30;42m {guess_word[index]} \033[0m", end = '')
                    elif guess_word[index] in random_word:
                        print(f"\033[30;43m {guess_word[index]} \033[0m", end = '')
                    else:
                        print(f"\033[30;100m {guess_word[index]} \033[0m", end = '')
                new_line()
            print(f'"{guess}" is more than 5 letters long, try again')
            print(f'Guesses remaining: {total_number_of_guesses}')
        elif word_list.count(guess) != 1:
            clear()
            for guess_word in guessed_word_list:
                for index in range(len(guess_word)):
                    if guess_word[index] == random_word[index]:
                        print(f"\033[30;42m {guess_word[index]} \033[0m", end = '')
                    elif guess_word[index] in random_word:
                        print(f"\033[30;43m {guess_word[index]} \033[0m", end = '')
                    else:
                        print(f"\033[30;100m {guess_word[index]} \033[0m", end = '')
                new_line()
            print(f'"{guess}" is not a word, try again')
            print(f'Guesses remaining: {total_number_of_guesses}')
        else:
            clear()
            number_of_guesses += 1
            guessed_word_list.append(guess)
            for guess_word in guessed_word_list:
                for index in range(len(guess_word)):
                    if guess_word[index] == random_word[index]:
                        print(f"\033[30;42m {guess_word[index]} \033[0m", end = '')
                    elif guess_word[index] in random_word:
                        print(f"\033[30;43m {guess_word[index]} \033[0m", end = '')
                    else:
                        print(f"\033[30;100m {guess_word[index]} \033[0m", end = '')
                new_line()
            if guess == random_word:
                print(f'You correctly guessed the word: {random_word}')
                print(f'You took number of guesses: {number_of_guesses}')
            else:
                total_number_of_guesses -= 1
                print(f'Guesses remaining: {total_number_of_guesses}')
                if number_of_guesses == 6:
                    print(f'The mystery word is: {random_word}')
