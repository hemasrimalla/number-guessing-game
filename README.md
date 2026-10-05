# Task 5: Number Guessing Game

A beginner-friendly console-based Number Guessing Game built in Python 3 using only the standard library.

---

## 📌 Project Overview

The computer picks a secret random integer between **1 and 100**. The player attempts to guess the number within a limited number of tries (**7 attempts**). After each guess, the game provides immediate directional hints (**"Too high"** or **"Too low"**). The game handles invalid and out-of-bounds input gracefully without crashing or deducting attempts, and asks if the player wants to play again once a round ends.

---

## ✨ Features

- **Standard Library Only**: Uses Python's built-in `random` module (`random.randint()`) with zero external dependencies.
- **Controlled Game Loop**: Uses a `while` loop that continues until the player guesses correctly or reaches the maximum allowed attempts.
- **Directional Feedback**: Informs the user whether their guess was "Too high" or "Too low".
- **Attempt Tracking & Statistics**: Tracks attempts and reports the exact count upon winning.
- **Robust Input Validation (`try/except`)**:
  - Non-numeric input (e.g. letters, symbols) is caught via `try/except ValueError`.
  - Out-of-range numbers (e.g. `< 1` or `> 100`) are rejected.
  - Invalid inputs **do not count** toward the 7-attempt limit.
- **Bonus Capabilities**:
  - **Attempt Limit**: Capped at 7 attempts.
  - **Answer Reveal**: If attempts run out, reveals the secret number.
  - **Replay Loop**: Prompts `"Play again? (y/n)"` to allow seamless consecutive games.
- **Modular & Clean Architecture**: Logic separated into `get_valid_guess()`, `play_round()`, and `main()`, guarded by `if __name__ == "__main__":`.

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+ installed on your system.

### Execution
Open your terminal/command prompt, navigate to the project directory, and run:

```bash
python number_guessing_game.py
```

---

## 💻 Sample Output

The following is an actual recorded execution showing:
1. **Round 1**: Handling non-numeric input (`python_intern`), handling out-of-range input (`150`), valid guessing with directional hints, and a victory in 6 attempts.
2. **Round 2**: Attempt limit enforcement (7 attempts exhausted), answer reveal, and exit prompt.

```text
**************************************************
       WELCOME TO THE NUMBER GUESSING GAME       
**************************************************

==================================================
I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it. Good luck!
==================================================

[Attempt 1/7] (Remaining: 7)
Enter your guess (1-100): python_intern
Invalid input! Please enter a valid whole number (no letters or symbols).
Enter your guess (1-100): 150
Out of range! Please enter a number between 1 and 100.
Enter your guess (1-100): 50
Too low! Try a higher number.

[Attempt 2/7] (Remaining: 6)
Enter your guess (1-100): 75
Too low! Try a higher number.

[Attempt 3/7] (Remaining: 5)
Enter your guess (1-100): 88
Too low! Try a higher number.

[Attempt 4/7] (Remaining: 4)
Enter your guess (1-100): 94
Too high! Try a lower number.

[Attempt 5/7] (Remaining: 3)
Enter your guess (1-100): 91
Too low! Try a higher number.

[Attempt 6/7] (Remaining: 2)
Enter your guess (1-100): 92

 Congratulations! You guessed the number 92 correctly in 6 attempt(s)!

Play again? (y/n): y

==================================================
I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it. Good luck!
==================================================

[Attempt 1/7] (Remaining: 7)
Enter your guess (1-100): 1
Too low! Try a higher number.

[Attempt 2/7] (Remaining: 6)
Enter your guess (1-100): 2
Too low! Try a higher number.

[Attempt 3/7] (Remaining: 5)
Enter your guess (1-100): 3
Too low! Try a higher number.

[Attempt 4/7] (Remaining: 4)
Enter your guess (1-100): 4
Too low! Try a higher number.

[Attempt 5/7] (Remaining: 3)
Enter your guess (1-100): 5
Too low! Try a higher number.

[Attempt 6/7] (Remaining: 2)
Enter your guess (1-100): 6
Too low! Try a higher number.

[Attempt 7/7] (Remaining: 1)
Enter your guess (1-100): 7
Too low! Try a higher number.

 Game Over! You've run out of attempts.
The secret number was: 32

Play again? (y/n): n

Thank you for playing! Have a great day!
```

---

## 📂 Project Structure

```text
number_guessing_game/
│
├── number_guessing_game.py   # Main executable Python game file
├── sample_output.txt          # Real captured console output
├── interview_answers.md       # Technical interview question answers
└── README.md                  # Project documentation and guide
```
