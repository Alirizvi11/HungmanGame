import random

# List of words
words = ['python', 'hangman', 'programming', 'developer', 'algorithm']

# Select a random word
word = random.choice(words)

# Initialize game variables
guessed_letters = []
attempts = 6  # Number of incorrect guesses allowed

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Main game loop
while attempts > 0:
    print(f"Word: {display_word(word, guessed_letters)}")
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Good guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Incorrect guess.")

    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        break
else:
    print(f"Game over! The word was: {word}")