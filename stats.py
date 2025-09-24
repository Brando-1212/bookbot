def get_book_text(file):
    with open(file) as f: 
        file_contents = f.read()
        return file_contents

def word_count(file):
    f = get_book_text(file)    
    word_list = f.split()
    return len(word_list)
def char_count(file):
    tot_count = {}
    char_list = list(file)
    for i in char_list:
        temp = i.lower()
        if temp in tot_count:
            tot_count[temp] += 1
        else:
            tot_count[temp] = 1
    return tot_count 
