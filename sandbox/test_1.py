
a: dict[int, int] = {1: 1, 2: 2}
a.pop(1)

print(len(a))

def grocery_list(a: dict[str, int], b: dict[str, int]) -> list[str]:
    result: list[str] = list()
    for buy in b:
        for inv in a:
            if buy == inv and a[inv] > b[buy]:
                result.append(buy)
    return result

print(grocery_list({"apple": 3, "pear": 2}, {"apple": 1, "pear" : 3, "grapes": 2}))

def filter_last(words: list[str], letter: str) -> list[str]:
    result: list[str] = list()
    i: int = 0
    while i < len(words):
        last_index = len(words[i]) - 1
        if letter == words[i][last_index]:
            result.append(words[i])
        i += 1
    return result

print(filter_last(["pear", "orange", "apple"], "e"))
