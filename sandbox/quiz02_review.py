"""Function Writing Exercises for Quiz 02 Review."""

def odd_and_even(ints: list[int]) -> list[int]:
    result: list[int] = list()
    i: int = 0
    while i < len(ints):
        if i % 2 == 0 and ints[i] % 2 == 1:
            result.append(ints[i])
        i += 1
    return result

def vowels_and_threes(string: str) -> str:
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    is_vowel: bool
    result: str = ""
    i: int = 0
    while i < len(string):
        is_vowel = False
        j: int = 0
        while j < len(vowels):
            if vowels[j] == string[i]:
                is_vowel = True
            j += 1
        if is_vowel and i % 3 == 0:
            result += ""
        elif is_vowel or i % 3 == 0:
            result += string[i]
        i += 1
    return result

def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    result: dict[str, float] = dict()
    for student in grades:
        total: float = 0
        for grade in grades[student]:
            total += grade
        result[student] = total / len(grades[student])
    return result
        
