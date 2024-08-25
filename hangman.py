MAX_TRIES = 10
no_guess = 0

# Initialize the word to guess and convert it to lowercase
word = "goodmorning".lower()
print(f"Word to guess (for debugging): {word}")

while True:
    # Prompt the user to guess a letter
    key = input("Guess a letter: ").lower()

    if key in word:
        print(f"The word contains the letter '{key}'.")
        
        # Remove the guessed letter from the word
        word = word.replace(key, "")
        print(f"Remaining letters: {len(word)}")
        
        if len(word) == 0:
            print("You win!")
            break
    else:
        print("Wrong guess.")
        no_guess += 1
        
        if no_guess >= MAX_TRIES:
            print("You lose.")
            break
