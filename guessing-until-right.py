
import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess number: "))
    
    if guess == secret:
        print("Correct!")
        break