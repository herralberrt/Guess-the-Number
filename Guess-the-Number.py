# Guess the Number -> Powered by Albert-Iulian Romaniuc
"""
This is a fun and interactive number guessing game where the player has to guess a randomly generated number between 1 and 100.
The game provides hints if the guessed number is too high or too low. The objective is to guess the correct number in as few attempts as possible to maximize your score.

Game Rules:
 - The scoring system starts at 100 points and decreases by 5 points for each incorrect guess.
 - If the player guesses the number in 5 attempts or fewer, they receive a 10-point bonus.
 - The score cannot go below 0, ensuring a minimum possible score.
 - The game selects a random number between 1 and 100.
 - The player inputs guesses, receiving hints based on their guess.
 - A score system starts at 100 and decreases with each incorrect guess.
 - Bonus points are awarded if the player guesses correctly within 5 attempts.
 - The game also tracks the time taken to solve the challenge.
 - Players can choose to replay after each game session.

Good luck and have fun!
"""

import random
import time

# Generates a random number between 1 and 100.
def generate_secret_number():
    return random.randint(1, 100)

# Displays the welcome message and game rules.
def display_welcome_message():
    print("Welcome to 'Guess the Number'!")
    print("Rules: You need to guess a number between 1 and 100.")
    print("You will receive hints if the number is too high or too low.")
    print("Your initial score is 100 points, which decreases with each attempt.")
    print("Bonus: If you guess the number in 5 attempts or less, you get extra points!")

# Prompts the user for input and ensures it is a valid integer using isdigit().
def get_user_input():
    guess = input("Guess a number between 1 and 100: ")
    while not guess.isdigit():  # Check if input contains only digits
        print("Please enter a valid number.")
        guess = input("Guess a number between 1 and 100: ")
    return int(guess)

# Calculates the player's score based on the number of attempts.
def calculate_score(attempts):
    score = max(100 - (attempts * 5), 0)
    if attempts <= 5:
        score += 10  # Bonus for quick guessing
    return score

# Generates a random motivational message for the player.
def generate_random_feedback():
    feedback = [
        "You're close! Try again!",
        "Don't give up, you can do it!",
        "Think logically, maybe it's higher or lower...",
        "It's just a game, have fun!",
        "Trust your intuition!",
        "A good strategy is to divide the range in half!",
        "Almost there, keep going!"
    ]
    return random.choice(feedback)

# Main function to run the game logic.
def guess_the_number():
    display_welcome_message()
    secret_number = generate_secret_number()
    attempts = 0
    score = 100  # Initial score
    start_time = time.time()
    
    while True:
        guess = get_user_input()
        attempts += 1
        score = calculate_score(attempts)
        
        if guess < secret_number:
            print("Too low! Try again.")
            print(generate_random_feedback())
        elif guess > secret_number:
            print("Too high! Try again.")
            print(generate_random_feedback())
        else:
            duration = round(time.time() - start_time, 2)
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            print(f"Your final score is: {score}")
            print(f"You solved the game in {duration} seconds.")
            if attempts <= 5:
                print("Amazing! You earned a speed bonus!")
            break

    display_statistics(attempts, score, duration)
    ask_for_replay()

# Displays the player's game statistics after completion.
def display_statistics(attempts, score, duration):
    print("------------------------")
    print(f"Game Statistics: \n - Attempts: {attempts}\n - Final Score: {score}\n - Total Time: {duration} seconds")
    print("------------------------")
    
    if attempts <= 3:
        print("Excellent job! You guessed very quickly!")
    elif attempts <= 7:
        print("Good job! You have decent guessing skills.")
    else:
        print("You got it! Keep practicing to improve your guessing strategy.")

# Asks the player if they want to replay the game.
def ask_for_replay():
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        print("Starting a new game...\n")
        guess_the_number()
    else:
        print("Thank you for playing! Goodbye!")

# Starts the game when the script is run.
if __name__ == "__main__":
    guess_the_number()
