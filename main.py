def get_book_text(file):
    with open(file) as f: 
        file_contents = f.read()
        return file_contents
def main():
    print(get_book_text("books/frankenstein.txt"))
main()
