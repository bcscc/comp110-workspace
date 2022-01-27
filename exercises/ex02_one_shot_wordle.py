"""EX02 - One Shot Wordle - A bigger step toward Wordle."""

__author__ = "730470219"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
result: str = ""

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)}-letters! Try again: ")

i: int = 0

while i < len(secret_word):
    if guess[i] == secret_word[i]:
        result = f"{result}{GREEN_BOX}"
    else:
        check: bool = False
        j: int = 0
        while (not check) and (j < len(secret_word)):
            if secret_word[j] == guess[i]:
                check = True
            else:
                j = j + 1
        if check:
            result = f"{result}{YELLOW_BOX}"
        else:
            result = f"{result}{WHITE_BOX}"
    i = i + 1

print(result)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")