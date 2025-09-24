
def get_book_text(file):
    with open(file) as f: 
        file_contents = f.read()
        return file_contents

from stats import word_count


def main():
    print(get_book_text("books/frankenstein.txt"))
    wc = word_count("books/frankenstein.txt")
    print(f"Found {wc} total words")

main()
