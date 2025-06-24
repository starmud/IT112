# Imports the random module to generate random numbers
import random

# Generates random number between 1 and 100, stores it in the variable random_number
random_number = random.randint(1, 100)

# Sets value of the guess to 100
guess = 100

# Starts while loop that continues until user guesses correct number
while guess != random_number:
    # Prompts user to enter guess and converts input into integer
    guess = int(input("Guess a number between 1 and 100: "))

    # If the guess is lower than the random number
    if guess < random_number:
        print("Too Low")

    # If the guess is higher than the random number
    elif guess > random_number:
        print("Too High")

    # If the guess is correct (see: random_number) will print success message
    else:
        print("Congrats, you have the right number!")

        
