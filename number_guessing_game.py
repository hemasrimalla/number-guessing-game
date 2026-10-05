"""
Number Guessing Game
====================
A beginner-friendly Python console game where the player tries to guess
a randomly generated number between 1 and 100 within a limited number of attempts.
"""

import random

# Global constants for game configuration
LOWER_BOUND = 1
UPPER_BOUND = 100
MAX_ATTEMPTS = 7


def get_valid_guess(min_val: int, max_val: int) -> int:
    """
    Prompt the user to enter a guess and validate the input.
    
    Uses try/except to catch non-integer inputs without crashing.
    Ensures the number is strictly within [min_val, max_val].
    Invalid inputs do not count toward game attempts.
    """
    while True:
        raw_input_value = input(f"Enter your guess ({min_val}-{max_val}): ").strip()
        
        # 1. Try converting the string input to an integer
        try:
            guess = int(raw_input_value)
        except ValueError:
            print("Invalid input! Please enter a valid whole number (no letters or symbols).")
            continue  # Prompt the user again without penalizing an attempt
            
        # 2. Check if the integer falls within the valid range
        if guess < min_val or guess > max_val:
            print(f"Out of range! Please enter a number between {min_val} and {max_val}.")
            continue  # Prompt the user again without penalizing an attempt
            
        return guess


def play_round() -> bool:
    """
    Play a single round of the Number Guessing Game.
    
    Returns:
        bool: True if the user guessed correctly (won), False if attempts ran out.
    """
    # Generate a secret random number between LOWER_BOUND and UPPER_BOUND
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    attempts = 0
    guessed_correctly = False
    
    print("\n" + "=" * 50)
    print(f"I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it. Good luck!")
    print("=" * 50)
    
    # while loop continues until the player guesses correctly or runs out of attempts
    while attempts < MAX_ATTEMPTS:
        remaining_attempts = MAX_ATTEMPTS - attempts
        print(f"\n[Attempt {attempts + 1}/{MAX_ATTEMPTS}] (Remaining: {remaining_attempts})")
        
        # Get a verified integer guess from the user
        guess = get_valid_guess(LOWER_BOUND, UPPER_BOUND)
        
        # Increment attempt counter only after receiving a valid guess
        attempts += 1
        
        # Conditional checks comparing guess with secret_number
        if guess == secret_number:
            print(f"\n Congratulations! You guessed the number {secret_number} correctly in {attempts} attempt(s)!")
            guessed_correctly = True
            break  # Stop the game after the correct guess
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
            
    # If the loop finished without a correct guess, reveal the answer
    if not guessed_correctly:
        print("\n Game Over! You've run out of attempts.")
        print(f"The secret number was: {secret_number}")
        
    return guessed_correctly


def main():
    """
    Main function to manage game lifecycle and allow replaying.
    """
    print("*" * 50)
    print("       WELCOME TO THE NUMBER GUESSING GAME       ")
    print("*" * 50)
    
    while True:
        play_round()
        
        # Ask the user if they'd like to play another round
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again not in ("y", "yes"):
            print("\nThank you for playing! Have a great day!\n")
            break


if __name__ == "__main__":
    main()
