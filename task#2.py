from random import randint as r

# Set the number range
min_number = 1
max_number = 40

# Generate a random number
secret_number = r(min_number, max_number)

# Initialize the attempt counter
attempts = 0

# Set the maximum number of attempts
max_attempts = 10

# Start the game
while attempts < max_attempts:
    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    # Provide feedback if the guess is incorrect
    else:
        if guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

    # Increment the attempt counter
    attempts += 1

# Check if the user ran out of attempts
if attempts == max_attempts:
    print("You ran out of attempts. The secret number was:", secret_number)
