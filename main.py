"""
# William Escobar
# Simple Python Guessing Game!
Requirements:

1. Generate a random number that the user must guess
2. Accept the users guess
3. Needs to compare the users guess to the generated number	
4. Continue until the user is correct.		
5. Assist the user in finding the right answer.		
6. Count the number of attempts.
7. Ask the user if they want to play again.

"""
import random
import os
import time

def clear():
    _ = os.system('clear')

def mainGame():
    # This creates a random number
    randomNumber = random.randint(1,20)

    # This makes sure that userGuess never equals randomNumber to initiate while loop.
    userGuess = randomNumber + 1
    counter = 0
    print("I've generated a number between 1 and 20!\nTry and guess it!")
    
    #print(randomNumber) # Testing purposes
    while randomNumber != userGuess:
        counter += 1
        print("Attempt #: " + str(counter))
        userGuess = int(input("Enter your guess: "))
        print("\n")
        clear()
        if randomNumber == userGuess:
            print("Correct!")
        elif randomNumber > userGuess:
            print("Go higher!")
        elif randomNumber < userGuess:
            print("Go lower!")

    print("It took you", counter, "attempt(s)!")
    return

# Main program starts here. #
clear()
while True:
    mainGame()
    playAgain = input("Press any key to exit or [1] to play again! ")
    clear()
    if playAgain != "1":
        print("Goodbye!")
        time.sleep(.75)
        clear()
        break