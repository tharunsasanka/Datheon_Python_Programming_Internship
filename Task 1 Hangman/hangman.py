
import random

words = ["python", "computer", "network", "security", "program"]

stages = [
    " +---+\n |   |\n     |\n     |\n     |\n=======",
    " +---+\n |   |\n O   |\n     |\n     |\n=======",
    " +---+\n |   |\n O   |\n |   |\n     |\n=======",
    " +---+\n |   |\n O   |\n/|   |\n     |\n=======",
    " +---+\n |   |\n O   |\n/|\\  |\n     |\n=======",
    " +---+\n |   |\n O   |\n/|\\  |\n/    |\n=======",
    " +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n======="
]

word = random.choice(words)
guessed = set()
mistakes = 0

print("Welcome to Hangman!")
print("Guess the hidden word. You can make 6 mistakes.")

while mistakes < 6:
    print("\n" + stages[mistakes])

    hidden = " ".join(
        letter if letter in guessed else "_"
        for letter in word
    )
    print("Word:", hidden)
    print("Attempts left:", 6 - mistakes)

    if all(letter in guessed for letter in word):
        print("You won! The word was:", word)
        break

    guess = input("Enter a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already tried that letter.")
        continue

    guessed.add(guess)

    if guess not in word:
        mistakes += 1
        print("Wrong guess!")
    else:
        print("Correct guess!")

if mistakes == 6:
    print("\n" + stages[mistakes])
    print("Game over! The word was:", word)
