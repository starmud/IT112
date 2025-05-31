import random

random_number = random.randint(1,100)

guess = 100

while guess !=random_number:
    
    guess = int(input("Guess a number between 1 and 100:"))
    
    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too High")
    else:
        print("congrats, you have the right number")
        