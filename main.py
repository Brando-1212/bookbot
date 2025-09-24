import sys

def get_book_text(file):
    with open(file) as f: 
        file_contents = f.read()
        return file_contents

from stats import word_count
from stats import char_count
from stats import sort

def main():
    if not len(sys.argv) == 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    print(book)
    wc = word_count(sys.argv[1])
    print(f"Found {wc} total words")
    characters = char_count(book)
    print(characters)
    sort_list = sort(characters)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in sort_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
