import os
import random
from words import WORDS

"""
print("\033[92mThis is green\033[0m")
print("\033[93mThis is yellow\033[0m")
print("\033[91mThis is red\033[0m")

"""

word = random.choice(WORDS)

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

def printGuess(guess):
    colored_guess = check(guess)
    print(colored_guess)
    return

def check(guess):
    result = []
    chars = set(word)
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result.append(f"\033[92m{guess[i]}\033[0m")
        elif guess[i] in chars:
            result.append(f"\033[93m{guess[i]}\033[0m")
        else:
            result.append(guess[i])
    
    return "".join(result)

def getUserInput():
    guess = input("Guess: ")
    return guess

def startGame():
    global word
    max_attempts = 6
    attempts = 0
    solved = False

    gameInstructions()

    while not solved: 
        guess = ""
        while len(guess) != 5:
            guess = getUserInput()

        printGuess(guess.lower())
        

        if guess == word:
            solved = True

    gameOver(word)
    

if __name__ == "__main__":
    startGame()