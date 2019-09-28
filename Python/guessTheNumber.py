#Guess the number game.

from random import randint

number=str(randint(1,20))
print("I'm thinking of a number between 1 and 20.")
for guesses in range(0,5):
    print("Guess it.")
    guess=input()
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too hight!")
    else:
        break

if guess == number:
    print("You guessed correctly. The number is " + number)
else:
    print("NOPE! I was thinking of " + number)
