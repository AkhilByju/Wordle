import os
import random
from words import WORDS

"""
print("\033[92mThis is green\033[0m")
print("\033[93mThis is yellow\033[0m")
print("\033[91mThis is red\033[0m")

"""

word = random.choice(WORDS)
history = []
max_attempts = 6
attempts = 0

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
    global attempts
    global max_attempts
    colored_guess = check(guess)
    history.append(colored_guess)
    os.system("clear")
    print(f"You are on your {attempts} guess, you have {max_attempts - attempts} guesses remaining")
    for row in history:
        print(row)
    return

def check(guess, word):
    result = [""] * len(word)
    word_chars = list(word)

    # First pass: check greens
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result[i] = f"\033[92m{guess[i]}\033[0m"
            word_chars[i] = None  # mark as used

    # Second pass: check yellows
    for i in range(len(guess)):
        if result[i] == "":
            if guess[i] in word_chars:
                result[i] = f"\033[93m{guess[i]}\033[0m"
                word_chars[word_chars.index(guess[i])] = None  # mark as used
            else:
                result[i] = guess[i]  # gray/default

    return "".join(result)


def getUserInput():
    guess = input("Guess: ")
    return guess

def startGame():
    global word, attempts, max_attempts
    solved = False

    gameInstructions()

    while not solved: 
        guess = getUserInput()
        while len(guess) != 5:
            print("\033[91mMake sure your guess contains 5 letters\033[0m")
            guess = getUserInput()

        attempts += 1
        printGuess(guess.lower())
        

        if guess == word:
            solved = True
            gameOver(word)
            break
        else:
            if attempts >= max_attempts:
                print(f"Out of attempts! The word was {word}")
                break

    

if __name__ == "__main__":
    startGame()