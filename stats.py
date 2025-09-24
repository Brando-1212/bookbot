def get_book_text(file):
    with open(file) as f: 
        file_contents = f.read()
        return file_contents

def word_count(file):
    f = get_book_text(file)    
    word_list = f.split()
    return len(word_list)
