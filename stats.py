from itertools import count


def get_count_words(text):
    return len(text.split())

def get_count_characters(character):
    charactersList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "â", "ê", "ë", "ô"]
    count = 0
    charactersCount = []
    for char in charactersList:
        for letter in character.lower():
            if letter == char:
                count+=1
        charactersCount.append(f"{char}: {count}")
        count = 0
    return charactersCount

def sort_on(entry):
    return int(entry.split(": ")[1])
