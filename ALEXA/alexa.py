from tkinter import *
import random

# Create the main window
root = Tk()
root.title("Simple Joke Bot")
root.geometry("300x200")

# Function to load jokes from file
def load_jokes():
    with open(r"c:\Users\one\Downloads\ALEXA\randomJokes.txt", "r") as file:
        return file.readlines()

# Function to display a random joke
def tell_joke():
    joke = random.choice(jokes).strip()  # Choose a random joke and strip any extra whitespace
    joke_label.config(text=joke.replace("\\n", "\n"))  # Replace placeholder with actual line breaks

# Load jokes
jokes = load_jokes()

# Create and pack a label for the joke
joke_label = Label(root, text="Click the button for a joke!", wraplength=250)
joke_label.pack(pady=20)

# Create and pack a button
joke_button = Button(root, text="Tell me a joke", command=tell_joke)
joke_button.pack()

# Start the GUI event loop
root.mainloop()