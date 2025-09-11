import os
import random
from words import WORDS

history = []

def gameInstructions():
    # Clear the terminal
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system("clear")

    print("Hello! Welcome to a game of wordle.")
    print("Guess the 5 letter word in under 6 attempts")
    print("Good Luck")

def gameOver(word):
    print(f"Congratulations you guessed {word} correctly")

def printHistory():
    return 

def getUserInput():
    guess = input("Guess: ")
    return guess

def startGame():
    global history
    word = random.choice(WORDS)
    max_attempts = 6
    attempts = 0
    solved = False

    gameInstructions()

    while not solved: 
        guess = getUserInput()
        if guess == word:
            solved = True

    gameOver(word)
    

if __name__ == "__main__":
    startGame()