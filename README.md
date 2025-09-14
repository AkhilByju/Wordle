# 🟩🟨 Wordle (Python CLI Version)

A simple **Wordle clone** built in Python for the terminal.
Guess the hidden 5-letter word in **6 tries** or fewer.

Each guess is highlighted with colors:

- 🟩 **Green** — correct letter in the correct spot
- 🟨 **Yellow** — letter is in the word but in the wrong spot
- ⬛ **Gray** — letter is not in the word

---

## ✨ Features

- Random 5-letter word chosen each game from a word list
- Colored feedback for each guess (using ANSI escape codes)
- Keeps track of your guess history
- 6 maximum attempts (like the real Wordle)
- Replay option when the game ends

---

## 🛠️ Requirements

- Python 3.7+
- A terminal that supports ANSI colors (macOS/Linux terminal, VS Code integrated terminal, or Windows Terminal with ANSI enabled)

---

## ▶️ How to Play

1. Clone or download this repo.

2. Make sure you have a `words.py` file with a `WORDS` list of 5-letter words, for example:

   ```python
   WORDS = [
       "apple", "grape", "table", "chair", "spoon", ...
   ]
   ```

3. Run the game:

   ```bash
   python wordle.py
   ```

4. Enter your guesses (must be 5 letters long).

5. Try to guess the word within 6 attempts!

---

## 🔮 Future Improvements

- Word validation (only allow words from the dictionary)
- On-screen colored keyboard (like the original Wordle)
- Daily Word mode
- Win/loss stats and streaks

---

## 📜 License

This project is open-source and free to use for learning and fun.

---
