from tkinter import *
import random

# Set up the main window
root = Tk()  # Create the main application window
root.title("Simple Math Quiz")  # Set the title of the window
root.geometry("300x300")  # Set the size of the window
root.configure(bg="lightblue")  # Set the background color of the window

score = 0  # Initialize the score variable

# Generate a math question based on difficulty
def generate_question():
    if difficulty == "easy":  # Check if difficulty level is easy
        num1 = random.randint(0, 9)  # Generate first number (0-9)
        num2 = random.randint(0, 9)  # Generate second number (0-9)
        operator = random.choice(['+', '-'])  # Choose an operator (+ or -)
    elif difficulty == "medium":  # Check if difficulty level is medium
        num1 = random.randint(10, 99)  # Generate first number (10-99)
        num2 = random.randint(10, 99)  # Generate second number (10-99)
        operator = random.choice(['+', '-', '*'])  # Choose an operator (+, -, or *)
    else:  # If difficulty level is hard
        num1 = random.randint(1000, 9999)  # Generate first number (1000-9999)
        num2 = random.randint(1000, 9999)  # Generate second number (1000-9999)
        operator = random.choice(['+', '-', '*', '/'])  # Choose an operator (+, -, *, or /)

    question = f"{num1} {operator} {num2}"  # Format the question string
    if operator == '+':  # Calculate answer based on operator
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = num1 // num2  # Use integer division for division operator
    return question, answer  # Return the generated question and its answer

# Check the user's answer
def check_answer():
    global score  # Access the global score variable
    user_answer = answer_entry.get()  # Get user's input from entry field
    if user_answer.isdigit():  # Check if input is a digit
        if int(user_answer) == correct_answer:  # Compare user's answer with correct answer
            result_label.config(text="Correct!", fg="green")  # Update result label for correct answer
            score += 1  # Increment score for correct answer
        else:
            result_label.config(text=f"Wrong. Answer: {correct_answer}", fg="red")  # Show correct answer for wrong input
    else:
        result_label.config(text="Enter a valid number", fg="red")  # Prompt for valid input
    
    score_label.config(text=f"Score: {score}")  # Update score display
    show_next_question()  # Show next question

# Display the next question
def show_next_question():
    global correct_answer  # Access the global correct_answer variable
    question, correct_answer = generate_question()  # Generate a new question and get its answer
    question_label.config(text=question)  # Display the new question in label
    answer_entry.delete(0, 'end')  # Clear the entry field for new input
    result_label.config(text="")  # Clear previous result message

# Start the quiz with selected difficulty level
def start_quiz(level):
    global difficulty, question_label, answer_entry, submit_button, result_label, score_label
    difficulty = level  # Set the selected difficulty level
    
    # Remove difficulty selection widgets from the main window
    for widget in root.winfo_children():
        widget.destroy()
    
    question_label = Label(root, text="", font=("Arial", 16), bg="lightblue")  # Create label for displaying questions
    question_label.pack(pady=10)  # Add label to window

    answer_entry = Entry(root, font=("Arial", 14))  # Create entry field for user answers
    answer_entry.pack()  # Add entry field to window

    submit_button = Button(root, text="Submit", command=check_answer)  # Create submit button to check answers
    submit_button.pack(pady=10)  # Add button to window

    result_label = Label(root, text="", font=("Arial", 12), bg="lightblue")  # Create label for displaying results (correct/wrong)
    result_label.pack()  # Add label to window

    score_label = Label(root, text="Score: 0", font=("Arial", 12), bg="lightblue")  # Create label to display current score
    score_label.pack(pady=10)  # Add label to window

    show_next_question()  # Show the first question

# Create the start screen with title and difficulty selection options
title_label = Label(root, text="Math Quiz", font=("Arial", 18, "bold"), bg="lightblue")  
title_label.pack(pady=20)  

difficulty_label = Label(root, text="Select Difficulty:", font=("Arial", 14), bg="lightblue")  
difficulty_label.pack(pady=10)  

easy_button = Button(root, text="Easy", command=lambda: start_quiz("easy"), font=("Arial", 12))  
easy_button.pack(pady=5)  

medium_button = Button(root, text="Medium", command=lambda: start_quiz("medium"), font=("Arial", 12))  
medium_button.pack(pady=5)  

hard_button = Button(root, text="Hard", command=lambda: start_quiz("hard"), font=("Arial", 12))  
hard_button.pack(pady=5)  

# Start the Tkinter event loop to run the application
root.mainloop()