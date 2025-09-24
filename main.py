
def get_book_text(file):
    with open(file) as f: 
        file_contents = f.read()
        return file_contents

from stats import word_count
from stats import char_count
from stats import sort

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)
    wc = word_count("books/frankenstein.txt")
    print(f"Found {wc} total words")
    characters = char_count(book)
    print(characters)
    sort_list = sort(characters)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in sort_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
