import random
print('Number Guessing Game')

def Number_Guessing_Game():
    number_to_guess = random.randint(1,10)
    guess = None

    while guess != number_to_guess:
        guess = int(input('Please guess a number between 1 to 10. '))

        if guess < number_to_guess:
            print('Number too low. Please try again!')

        elif guess > number_to_guess:
            print('Number too high. Please try again!')

    else:
        print(f'Nice, you got it right! The number was {number_to_guess}!')

Number_Guessing_Game()
