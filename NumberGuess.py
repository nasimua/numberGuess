# import randint function from 'random' module
from random import randint
# Import the sleep function, from the time module
from time import sleep

""" 
Codecademy - Learn Python 2
Number Guess
Nasim Ahmed
"""


def get_user_guess():
    guess = int(input("Guess the sum: "))
    return guess


def roll_dice(number_of_sides):
    # simulate first and second roll
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    # set max possible value to number of sides * 2 as there are to dice
    max_val = number_of_sides * 2
    print("Maximum possible value is: %d" % max_val)
    guess = get_user_guess()
    # check if user guess is more than max possible value
    if guess > max_val:
        print("Invalid Choice! Number is higher than Maximum possible.")
    else:
        print("Rolling...")
        # sleep program for 2 seconds to simulate roll
        sleep(2)
        print("First Roll: %d" % first_roll)
        sleep(1)
        print("Second Roll: %d" % second_roll)
        sleep(1)
        # find sum of rolls
        total_roll = first_roll + second_roll
        print("Total: %d" % total_roll)
        print("Result...")
        sleep(1)
        # check if user guessed correctly
        if (guess == total_roll):
            print("Congratulations! You guessed correct!")
        else:
            print("Well looky here... Looks like we have a LOSER!")


roll_dice(6)
