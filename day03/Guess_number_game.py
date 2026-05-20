import random

def random_number_generator():
    return random.randint(1,100)

def guess_number(secret,attempts):
    if attempts == 0:
        print("game over")
        return
    user_guess=int(input("Enter your guess"))
    if user_guess == secret:
        print("correct")
    elif user_guess > secret:
        print("too high")   
        guess_number(secret,attempts-1)
    else:
        print("too low")
        guess_number(secret,attempts-1)
    

secret=random_number_generator()
guess_number(secret,10)