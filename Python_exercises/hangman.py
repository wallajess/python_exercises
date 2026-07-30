import random


def input_choice(question: str, poss_answers: list[str]) -> str:
    """This function asks the user a question and prompts them to try again if they enter an invalid answer."""
    print(question + " [" + " | ".join(poss_answers) + "]")
    while True:
        answer = input("> ")
        if answer in poss_answers:
            return answer
        else:
            print("Invalid answer. Try again.")


def shape(word: str, guesses: str) -> str:
    """This function takes the secret word and the users guesses as arguments
    and replaces all of the letters in weather that were not guesses
    with underscores."""
    guessed_letters = ""
    for x in word:
        if x in guesses:
            guessed_letters += x
        else:
            guessed_letters += "_"
    return guessed_letters


def hangman(word=str, max_fails=int):
    """This function plays a game of hangman."""
    wrong_guesses = 0
    guesses = ""
    guessed_word = ""
    while (wrong_guesses < max_fails) or word != guessed_word:
        letter = input("Please guess a letter: ")
        matched = False
        if len(letter) != 1:
            print("Invalid input. Each guess must contain one letter only. Try again.")
            continue
        for x in word:
            if x == letter:
                guesses += letter
                matched = True
                guessed_word = shape(word, guesses)
                print("Yay! Your guess was right!")
                print("Here's what you've got thus far:", guessed_word, ";", "you can still make", max_fails - wrong_guesses, "wrong guess(es). Guess another letter.")
        if word == guessed_word:
            print("Congratulations! You win! The word was", word, "- you're good at this, aren't you?")
            break
        if matched is False:
            wrong_guesses += 1
            print("Unfortunately that letter is not in the word. Try again.")
            print("But be careful: you can only make", max_fails - wrong_guesses, "wrong guess(es) before you hang!")
            if wrong_guesses == max_fails:
                print("You've used up all your guesses. Now you'll hang!")
                break


if __name__ == '__main__':
    words = ['apple', 'tree', 'python', 'bench', 'float']
    while input_choice("Do you want to play a game?", ['yes', 'no']) == 'yes':
        max_fails = int(input("Number of allowed mistakes: "))
        word = random.choice(words)  # Wähle ein zufälliges Wort aus.
        hangman(word, max_fails)