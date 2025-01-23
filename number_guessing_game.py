import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Get the range from the user
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    # Ensure the range is valid
    if lower_bound >= upper_bound:
        print("Invalid range. The upper bound must be greater than the lower bound.")
        return

    # Generate a random number within the range
    target_number = random.randint(lower_bound, upper_bound)

    print(f"I have chosen a number between {lower_bound} and {upper_bound}. Can you guess what it is?")

    attempts = 0

    while True:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < target_number:
                print("Higher!")
            elif guess > target_number:
                print("Lower!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()