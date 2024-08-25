import random

# Generate a random number between 0 and 10
random_number = random.randint(0, 10)
print(f"Random number (for debugging): {random_number}")

# Initialize the guess variable
guess = -1

# Loop until the user guesses the correct number
while guess != random_number:
    if guess != -1:
        print("Wrong guess")

    # Prompt the user to enter a number
    guess = int(input("Enter a number between 0 and 10: "))

print("You guessed correctly!")
