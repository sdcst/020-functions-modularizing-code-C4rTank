"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""



def title():
    import random
    
    print("Lets play a number gussing game!")
    print("Guess the number I'm thinking of between 1 to 10!")

    num = random.randint(1, 10)

    guess = int(input("Guess what number I'm thinking of: "))

    if guess == num:
        print("Great job!")
    else:
        print("Wrong!")
        print("The number was",num, end='')
        print('!')

title()
