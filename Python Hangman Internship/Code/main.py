import random
import os

# ASCII Gallows art that updates with each incorrect guess (max 6 mistakes)
HANGMAN_PICS = [
    '''
      +---+
          |
          |
          |
         ===''',
    '''
      +---+
      O   |
          |
          |
         ===''',
    '''
      +---+
      O   |
      |   |
          |
         ===''',
    '''
      +---+
      O   |
     /|   |
          |
         ===''',
    '''
      +---+
      O   |
     /|\\  |
          |
         ===''',
    '''
      +---+
      O   |
     /|\\  |
     /    |
         ===''',
    '''
      +---+
      O   |
     /|\\  |
     / \\  |
         ==='''
]

def load_words_from_file(filename="google-10000-english-no-swears.txt"):
    """
    Reads the 10,000 words text file and returns a list of valid English words.
    """
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            # Filter words that are alphabetic and have length greater than 3
            words = [line.strip().lower() for line in f if line.strip().isalpha() and len(line.strip()) > 3]
            if words:
                return words
    
    # Fallback list if the text file is missing
    return ["python", "developer", "programming", "internship", "computer"]

def display_board(missed_letters, correct_letters, secret_word):
    """
    Displays the current ASCII art, missed letters, and the hidden word state.
    """
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    
    print("Missed Letters:", " ".join(missed_letters))
    print()
    
    # Display the secret word with underscores for unguessed letters
    display_list = [letter if letter in correct_letters else '_' for letter in secret_word]
    print("Secret Word: " + " ".join(display_list))
    print()

def get_guess(already_guessed):
    """
    Takes and validates a single letter input from the player.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter only.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose another one.")
        elif not guess.isalpha():
            print("Please enter a valid alphabet letter.")
        else:
            return guess

def play_hangman():
    print("=== Welcome to the Hangman Word Guessing Game! ===")
    
    # Load words from the text file and choose a random secret word
    word_list = load_words_from_file()
    secret_word = random.choice(word_list)
    
    missed_letters = ""
    correct_letters = ""
    game_is_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word)
        
        # Get player's input guess
        guess = get_guess(missed_letters + correct_letters)
        
        if guess in secret_word:
            correct_letters += guess
            
            # Check if the player has guessed all letters
            found_all_letters = True
            for letter in secret_word:
                if letter not in correct_letters:
                    found_all_letters = False
                    break
            
            if found_all_letters:
                display_board(missed_letters, correct_letters, secret_word)
                print(f"\nCongratulations! The secret word was: '{secret_word}'. You have won!")
                game_is_done = True
        else:
            missed_letters += guess
            
            # Check if player has run out of attempts (max 6 wrong guesses)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print(f"\nGame Over! You ran out of guesses.\nThe correct word was: '{secret_word}'.")
                game_is_done = True
                
        if game_is_done:
            if input("\nDo you want to play again? (yes/no): ").lower().startswith('y'):
                missed_letters = ""
                correct_letters = ""
                game_is_done = False
                secret_word = random.choice(word_list)
            else:
                print("Thank you for playing!")
                break

if __name__ == "__main__":
    play_hangman()