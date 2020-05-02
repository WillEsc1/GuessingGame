"""
William Escobar
Scratch file
Testing purposes
"""
#
"""
for b in range (11):
    print (b)
    for x in range(16):
        print (x)
"""
#
"""
a = ["fizz", "buzz", "baz"]
while a:
    print(a.pop(-1))
    b = ["---", "==="]
    while b:
        print(b.pop(-1))
"""
#
"""
import random

play = True

while play:
    number = random.randint(1,5)
    count = 1
    guess = int(input("Enter you guess between 1 and 20: "))
    while guess != number:
        count+=1

        if guess > number + 10:
            print("Too high!")
        elif guess < number - 10:
            print("Too low!")
        elif guess > number:
            print("Getting warm, but still too high!")
        elif guess < number:
            print("Getting warm but still too low!")
        
        guess = int(input("Try again!"))
    
    if guess == number:
        print("Correct! It took you ", count, " tries!")

"""
#
"""
import random
import sys

def guessNumber():
    number=random.randint(1,3)
    count=1
    guess= int(input("Enter your guess between 1 and 1000: "))

    while guess !=number:
        count+=1
        if guess > (number + 10):
            print("Too high!")
        elif guess < (number - 10):
            print("Too low!")
        elif guess > number:
            print("Getting warm but still high!")
        elif guess < number:
            print("Getting warm but still Low!")

        guess = int(input("Try again "))

    if guess == number:
        print("You rock! You guessed the number in ", count, " tries!")
        return

guessNumber()

again = str(input("Do you want to play again (type yes or no): "))
if again == "yes":
    guessNumber()
else:
    sys.exit(0)

"""
#
"""
import random
print("The purpose of this exercise is to enter a number of coin values") 
print("that add up to a displayed target value.\n") 
print("Enter coins values as 1-penny, 5-nickel, 10-dime,and 25-quarter.") 
print("Hit return after the last entered coin value.")
print("--------------------") 
total = 0 
final_coin = random.randint(1, 99)
print("Enter coins that add up to", final_coin, "cents, on per line") 
user_input = int(input("Enter first coin: "))
total = total + user_input

if user_input != 1 and user_input!=5 and user_input!=10 and user_input!=25:
   print("invalid input")

while total != final_coin:
    user_input = int(input("Enter next coin: "))
    total = total + user_input

if total > final_coin:
    print("Sorry - total amount exceeds", (final_coin)) 

if total < final_coin:
    print("Sorry - you only entered",(total))

if total== final_coin: 
    print("correct")
"""
#
"""
# Opt1: Just use the string value entered with one option to go again
while True:
    # your entire program goes here

    try_again = input("Press 1 to try again, any other key to exit. ")
    if try_again != "1":
        break # break out of the outer while loop


# Opt2: if using int(), safeguard against bad user input    
while True:
    # your entire program goes here

    try_again = input("Press 1 to try again, 0 to exit. ")
    try:
        try_again = int(try_again)  # non-numeric input from user could otherwise crash at this point
        if try_again == 0:
            break # break out of this while loop
    except:
        print("Non number entered")


# Opt3: Loop until the user enters one of two valid options
while True:
    # your entire program goes here

    try_again = ""
    # Loop until users opts to go again or quit
    while (try_again != "1") or (try_again != "0"):
        try_again = input("Press 1 to try again, 0 to exit. ")
        if try_again in ["1", "0"]:
            continue  # a valid entry found
        else:
            print("Invalid input- Press 1 to try again, 0 to exit.)
    # at this point, try_again must be "0" or "1"
    if try_again == "0":
        break
"""