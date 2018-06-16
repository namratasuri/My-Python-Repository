# This exercise was taken from https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

def call_game(random_number):
    user_input = int(input("Please enter a number from 1-9"))
    count = 1
    while user_input != random_number:
        if user_input < random_number:
            print("The number you entered is lesser than the random number")
        else:
            print("The number you entered is greater than the random number")
        user_input = int(input("Please enter a number from 1-9"))
        count += 1

    print("It took you %d tries to guess the number %d" %(count, random_number))

def main():
    random_number = random.randint(1,9)
    call_game(random_number)

if __name__ == "__main__":
    main()