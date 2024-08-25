from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# Initialize the main window
main = Tk()
main.title("Hangman")
main.geometry("800x600")

# Load images for the hangman stages
imageList = [Image.open(f"images/hangman0{i}.png") for i in range(1, 8)]

# Display the first hangman image
current_image = ImageTk.PhotoImage(imageList[0])
label1 = Label(main, image=current_image)
label1.image = current_image
label1.place(x=0, y=0)

# Game settings
MAX_TRIES = 6
no_guess = 0

# Word to guess
word = "goodmorning".lower()
print(f"Word to guess (for debugging): {word}")

# Main game loop
while True:
    # Prompt the user to guess a letter
    key = simpledialog.askstring("Guess", "Guess a letter: ").lower()

    if key in word:
        messagebox.showinfo("Hangman", f"The word contains the letter '{key}'.")
        
        # Remove the guessed letter from the word
        word = word.replace(key, "")
        
        # Check if the word is completely guessed
        if len(word) == 0:
            messagebox.showinfo("Hangman", "You win!")
            break
    else:
        no_guess += 1
        messagebox.showinfo("Hangman", "Wrong guess.")
        
        # Update the hangman image
        current_image = ImageTk.PhotoImage(imageList[no_guess])
        label1.config(image=current_image)
        label1.image = current_image
        
        # Check if the maximum number of tries has been reached
        if no_guess >= MAX_TRIES:
            messagebox.showinfo("Hangman", "You lose.")
            break

# Start the Tkinter main loop
main.mainloop()
