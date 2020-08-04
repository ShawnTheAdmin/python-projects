import string
from random import randint
from PyDictionary import PyDictionary


def build_board():
    """
    Builds basic game board.
    """

    board = """
    _______
    |      |
    |      1
    |     234
    |      5
    |     6 7
    |
    |___________
    """

    return board


def append_board(board, num):
    """
    Modifies the hangman board on guesses. Returns modified board to the play game function.
    """
    piece = {1: "O", 2: "/", 3: "|", 4: "\\", 5: "|", 6: "/", 7: "\\"}

    for i in range(8 - num):
        if str(i) in board:
            board = board.replace(str(i), piece[i])

    for i in range(1, 8):
        if str(i) in board:
            board = board.replace(str(i), " ")

    return board


def get_word():
    """
    Obtains and returns random word from the word text list.
    """
    word_list = open("words.txt").read().split()
    random_word = word_list[randint(0, len(word_list))]
    return random_word


def play_round(letters):
    """
    Function to play a round, ensures that the 'guess' is only 1 character and alphabetic.
    """
    alphabet = string.ascii_lowercase
    while True:
        guess = input("Enter a single letter between A and Z: ")
        if len(guess) > 1:
            print(
                "Guess must be ONE alphabetic character between A and Z (not case sensitive). Please try again."
            )
        elif guess not in alphabet:
            print(
                "Guess must be an alphabetic character between A and Z (not case senstivie). Please try again."
            )
        elif guess in letters:
            print("That letter has already been guessed. Please try again.")
        else:
            return guess


def define_word(word):
    """
    Returns definition of the random word if one is available.
    """
    dictionary = PyDictionary()

    try:
        definition = dictionary.meaning(word)
    except IndexError:
        definition = f"Sorry! No definition for {word} is available!"

    return definition


def play_game():
    """
    Main game wrapper. 
    """
    player_name = input("Welcome to hangman! What's your name? ")
    word = get_word().lower()
    blank_word = ["_" for _ in word]
    board = build_board()
    max_guess = 7
    letters_guessed = []
    d = define_word(word)

    print(f"Hello, {player_name}! Word has been generated, take your first guess.")

    while max_guess >= 0 and "_" in blank_word:
        guess = play_round(letters_guessed)
        if guess in word:
            indexes = [i for i in range(len(word)) if word[i] == guess]
            for i in indexes:
                blank_word[i] = guess
            letters_guessed.append(guess)
            print(f"Good job! Guess another letter!")
            print(f"Letters gussed: {letters_guessed}")
            print(*blank_word)
        else:
            letters_guessed.append(guess)
            print(f"Wrong! You have {max_guess} guesses left.")
            print(f"Letters guessed: {letters_guessed}")
            print(*blank_word)
            print(append_board(board, max_guess))
            max_guess -= 1

    if "_" not in blank_word:
        print(f"You won! The word was {word}. The defition is:\n")
        {print(f"{k}: {v[0]}\n") for k, v in d.items()}
    else:
        print(f"You lost! The word was {word}. The defition is:\n")
        {print(f"{k}: {v[0]}\n") for k, v in d.items()}


while True:
    play_game()
    challenge = input("Would you like to play again? ")
    if challenge[0].lower() == "n" or challenge == " ":
        break
