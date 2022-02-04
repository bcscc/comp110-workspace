"""EX03 - Wordle - The final step towards Wordle."""

__author__ = "730470219"


def contains_char(word_being_searched: str, searched_letter: str) -> bool:
    """Function that checks for a given letter in a given word."""
    assert len(searched_letter) == 1
    i: int = 0
    while i < len(word_being_searched):
        if word_being_searched[i] == searched_letter:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Function that evaluates the accuracy of the guessed word with the secret word."""
    assert len(guess) == len(secret)
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i += 1
    return result


def input_guess(chosen_length: int) -> str:
    """Function to retrieve a guessed word of a given length."""
    guess: str = input(f"Enter a {chosen_length} character word: ")
    while len(guess) != chosen_length:
        guess = input(f"That wasn't {chosen_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess: str = ""
    playing: bool = True
    turns: int = 1
    while playing and turns < 7:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turns}/6 turns!")
            playing = False
        else:
            turns += 1
    if guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()