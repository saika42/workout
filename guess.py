#!/usr/bin/python3

import random

def guessing_game():
    number = random.randint(0,100)
    result = ''
    while result != 'Just right':
        guess = int(input('Guess what number has been chosen (0,100): '))
        if guess == number:
            result = 'Just right'
        elif guess > number:
            result = 'Too high'
        elif guess < number:
            result = 'Too low'
        print(result)
    return

if __name__ == "__main__":
    guessing_game()
