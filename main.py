import sys
from stats import get_count_words
from stats import get_count_characters
from stats import sort_on

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text()
    word_count = get_count_words(text)
    characters_count = get_count_characters(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    characters_count.sort(reverse=True, key=sort_on)
    print(characters_count)
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()