"""
Hangman

author: Mitchell Thomas

"""
import time

lives = 10
wordStr = "apple"
wordLis = list(wordStr.lower())
guess = ["_"] * len(wordLis)
win = False
incorrectLetters = []

def printScore():
    print("\n\n: " + str(lives))
    print("Incorrect Letters: ", end="")
    for x in range(len(incorrectLetters)):
        if x == len(incorrectLetters) - 1:
            print(incorrectLetters[x], end="")
        else:
            print(incorrectLetters[x], end=",")
    print("")
    for x in range(len(guess)):
        if x == len(guess) - 1:
            print(guess[x], end="")
        else:
            print(guess[x], end=",")
    print("")

def askLetter():
    attempt = input("Please guess a letter: ").lower()
    correct = False
    for x in range(len(wordLis)):
        if attempt == wordLis[x]:
            guess[x] = attempt
            correct = True
    if correct:
        print("You got one!")
    else:
        print("Dang it!  That wasn't in the word.")
        incorrectLetters.append(attempt)
        global lives
        lives -= 1
    time.sleep(1)

def checkWin():
    if "_" not in guess:
        global win
        win = True



while lives > 0 and win == False:
    # Need to print out current scoreboard
    printScore()

    # Prompt a letter
    askLetter()

    # See if they won
    checkWin()



if lives <= 0:
    print("you're a loser!")
else:
    print("you're a winner!  You have " + str(lives) + " left!")
