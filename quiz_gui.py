from tkinter import *
from tkinter import simpledialog, messagebox

# Initialize the main Tkinter window and hide it
main = Tk()
main.withdraw()

# List of questions and their corresponding answers
questions = [
    "What is the capital of Germany?",
    "Who is the president of the US?",
    "What is the capital of France?",
    "What is the capital of Spain?"
]

answers = [
    "Berlin", 
    "Biden",
    "Paris",
    "Madrid"
]

# Initialize the score
score = 0

# Loop through the questions
for i in range(len(questions)):
    # Prompt the user to answer each question
    user_answer = simpledialog.askstring("Question", questions[i]).strip()

    # Check the user's answer (case-insensitive)
    if user_answer.lower() == answers[i].lower():
        messagebox.showinfo("Result", "Correct!")
        score += 1
    else:
        messagebox.showinfo("Result", "Incorrect")

# Show the final score
messagebox.showinfo("Final Score", f"Your score: {score}/{len(questions)}")

# Start the Tkinter main loop
main.mainloop()
