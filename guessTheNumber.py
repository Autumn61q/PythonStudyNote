print("I am thinking of a number between 1 and 10.")
import random
num=random.randint(1,10)
guess=int(input("Try a guess:"))
while guess!=num:
    if guess>num:
        print("Too high.Try again.")
    else:
        print("Too low.Try again.")
    guess=int(input("Try a guess:"))
print("Congratulations! You guessed it right.")