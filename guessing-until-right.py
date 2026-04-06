
import random # Import the random module to generate a random number

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess number: "))
    
    if guess == secret:
        print("Correct!")
        break