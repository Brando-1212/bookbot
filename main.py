
def get_book_text(file):
    with open(file) as f: 
        file_contents = f.read()
        return file_contents

from stats import word_count
from stats import char_count


def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)
    wc = word_count("books/frankenstein.txt")
    print(f"Found {wc} total words")
    characters = char_count(book)
    print(characters)

main()
