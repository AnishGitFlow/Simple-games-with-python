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
    print(questions[i])
    user_answer = input("Answer: ").strip()  # Use strip() to remove any extra spaces

    # Check the user's answer
    if user_answer.lower() == answers[i].lower():  # Case-insensitive comparison
        print("Correct")
        score += 1  # Increment score if the answer is correct
    else:
        print("Incorrect")

# Print the final score
print(f"Score: {score}/{len(questions)}")
