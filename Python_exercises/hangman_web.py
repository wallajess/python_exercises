# Importieren des Moduls für das generieren von Zufallszahlen
import random


# def input_choice ...  # Aufgabenteil (a)


# def shape ...         # Aufgabenteil (b)


# def hangman ...       # Aufgabenteil (c)


if __name__ == '__main__':
    words = ['apple', 'tree', 'python', 'bench', 'float']

    max_fails = int(input("Number of allowed mistakes: "))

    while input_choice("Wanna play a game?", ['yes', 'no']) == 'yes':
        word = random.choice(words)  # Wähle ein zufälliges Wort aus.
        hangman(word, max_fails)
