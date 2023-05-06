# Importing the random module to randomly choose a word for the player to guess
import random

# Function to randomly choose a word from a list of words
def get_word():
    # List of words to choose from
    words = ["apple", "banana", "cherry", "orange", "kiwi"]
    # Using the random.choice() function to choose a random word from the list
    chosen_word = random.choice(words)
    return chosen_word

# Function to play the game
def play(word):
    # Initializing variables
    word_completion = "-" * len(word) # A string of dashes equal to the length of the chosen word
    guessed = False # A boolean variable to keep track of whether the player has guessed the word or not
    guessed_letters = [] # An empty list to store the letters that the player has guessed
    tries = 6 # The number of tries the player has to guess the word
    
    # Printing the initial state of the game
    print("Let's play Hangman!")
    print(word_completion)
    print("\n")
    
    # While loop to keep the game going until the player wins or loses
    while not guessed and tries > 0:
        # Getting the player's guess
        guess = input("Please guess a letter or word: ").lower()
        
        # If the guess is a single letter
        if len(guess) == 1:
            # Check if the letter has already been guessed
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            # If the letter has not been guessed and is not in the word
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            # If the letter has not been guessed and is in the word
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                # Replacing the dashes in the word_completion string with the guessed letter
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                # If there are no more dashes in the word_completion string, the player has won
                if "-" not in word_completion:
                    guessed = True
        # If the guess is a word
        elif len(guess) == len(word):
            # Check if the word has already been guessed
            if guess in guessed_words:
                print("You already guessed the word", guess)
            # If the word has not been guessed and is not the chosen word
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            # If the word has not been guessed and is the chosen word
            else:
                guessed = True
                word_completion = word
        # If the guess is not a valid input
        else:
            print("Not a valid guess.")
        
        # Print the current state of the game
        print(word_completion)
        print("\n")
    
    # If the player has guessed the word
    if guessed:
        print("Congratulations, you guessed the word!")
    # If the player has run out of tries
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

# Function to run the game
def game():
    # Getting a word for the player to guess
    word = get_word()
    # Playing the game with the chosen word
    play(word)
    # Asking the player if they want to play again
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

# Running the game
game()
