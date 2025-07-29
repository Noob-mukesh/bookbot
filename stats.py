
def get_num_words():
    with open(r"bookbot/books/frankenstein.txt", "r", encoding="utf-8") as f:

        file_contents = f.read()
    
        words=file_contents.split()
    return {len(words)}
    
# get_num_words(get_book_text)
# from main import get_book_text
from string import printable
def count_char():
    with open(r"bookbot/books/frankenstein.txt", "r", encoding="utf-8") as f:
        file_contents = f.read().lower()
    char_dict={}
    for i in file_contents:
        
        if i.isalpha():
            i=i.lower()
            char_dict[i] = char_dict.get(i, 0) + 1
            
    return (char_dict)
        

        
print(count_char())

    