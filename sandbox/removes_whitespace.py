"""Function that removes whitespaces"""

def remove_ws(word: str) -> str:
    """Removes white space."""
    i: int = 0
    result: str = ""
    while i < len(word):
        if word[i] == " ":
            i += 1
        else:
            result += word[i]
            i += 1
    return result


