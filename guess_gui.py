import random
from tkinter import *
from tkinter import simpledialog, messagebox

# Initialize the main Tkinter window and hide it
main = Tk()
main.withdraw()

# Generate a random number between 0 and 10
random_number = random.randint(0, 10)
print(f"Random number (for debugging): {random_number}")

# Initialize the guess variable
guess = -1

# Loop until the user guesses the correct number
while guess != random_number:
    if guess != -1:
        messagebox.showinfo("Wrong", "Wrong guess")

    # Prompt the user to enter a number
    guess = simpledialog.askstring("Guess", "Enter a number between 0 and 10:")
    
    # Convert the input to an integer
    guess = int(guess)

    if guess == random_number:
        messagebox.showinfo("Right", "You guessed correctly!")
        exit()

# Start the Tkinter main loop
main.mainloop()
