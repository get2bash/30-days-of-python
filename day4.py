# Number guessing game
from random import randint


# Set number of turns for the levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# compare the user guess and the random number
def guess_checker(user_number, actual_number, turn):
    """Checks the guessed number against the actual number and reduces the number of turns"""
    if user_number > actual_number:
        print("Your guess is too high")
        return turn - 1
    elif user_number < actual_number:
        print("Your guess is too low")
        return turn - 1
    else:
        print(f"The correct number is {actual_number}, you WON!!!")


# Set difficulty
def difficulty():
    level = input("What level of difficulty do you want, 'hard' or 'easy'!: ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Greet player
    print("Welcome to the number guessing game!")
    print("A number is selected at random between 1-100, guess the number.")

    # Generate a random number between 1 and 100
    answer = randint(1, 100)

    # Set User_guess
    user_guess = 0

    turns = difficulty()

    while user_guess != answer:
        print(f"You have {turns} attempts remaining")
        # User makes a guess
        user_guess = int(input("Choose a number between 1 and 100: "))
        turns = guess_checker(user_guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return


game()
