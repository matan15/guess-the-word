import random
import json

# Define the possible words
with open("words_dictionary.json", 'r') as f:
    words_dict = json.load(f)
WORDS = [word for word in words_dict.keys()]

# Choose a random word from the list
word = random.choice(WORDS)

# Initialize the word state
word_state = "_" * len(word)

# Initialize the number of remaining guesses
remaining_guesses = 6

# Initialize the list of guessed letters
guessed_letters = []

# Function to update the word state
def update_word_state(guess):
    global word_state
    new_word_state = ""
    for i in range(len(word)):
        if word[i] == guess:
            new_word_state += guess
        else:
            new_word_state += word_state[i]
    word_state = new_word_state
    print(word_state) # For testing purposes only

# Function to handle user input
def take_guess(guess):
    global remaining_guesses
    global guessed_letters
    global word_state

    # Check if the guess has already been made
    if guess in guessed_letters:
        print("You already guessed that letter.")
        return

    # Check if the guess is in the word
    if guess in word:
        print("Correct!")
        update_word_state(guess)
    else:
        print("Incorrect!")
        remaining_guesses -= 1

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Update the display
    update_display()

# Function to update the display
def update_display():
    global remaining_guesses
    global guessed_letters
    global word_state

    # Clear the screen
    print("\033[H\033[J")

    # Display the remaining guesses
    print("Remaining guesses: ", remaining_guesses)

    # Display the guessed letters
    print("Guessed letters: ", end="")
    for letter in guessed_letters:
        print(letter, end=" ")
    print("")

    # Display the word state
    print(word_state)

    # Check if the game is over
    if remaining_guesses == 0:
        print("Game over. The word was", word)
    elif "_" not in word_state:
        print("You win!")

# Main game loop
while remaining_guesses > 0 and "_" in word_state:
    # Get the user's guess
    guess = input("Guess a letter: ")

    # Handle the user's guess
    take_guess(guess)
