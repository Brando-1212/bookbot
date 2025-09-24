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
def sort_on(items):
    return items["num"]

def sort(char_tot):
    sort_list = []
    for key, value in char_tot.items():
        sort_list.append({"char": key , "num": value})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

