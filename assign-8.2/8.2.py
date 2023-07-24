import random

def words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().splitlines()
    return words

def random_word_generator(words_list):
    return random.choice(words_list)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman_game():
    file_name = "words.txt"
    words_list = words_from_file(file_name)
    word_to_guess = random_word_generator(words_list).upper()
    guessed_letters = set()
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while max_attempts > 0:
        guess = input("Guess your letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            max_attempts -= 1
            print("Incorrect!")
            print("You have", max_attempts, "chance(s) left.")
        else:
            print(display_word(word_to_guess, guessed_letters))

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if max_attempts == 0:
        print("Sorry, you've run out of chances. The word was:", word_to_guess)


hangman_game()
