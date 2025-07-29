from stats import get_num_words,count_char
import sys
def get_book_text():
    with open(r"bookbot/books/frankenstein.txt", "r", encoding="utf-8") as f:

        file_contents = f.read()
        return (file_contents)
    
c=count_char() 
print(type(c))   
char_count_output = "\n".join([f"{char}: {count}" for char, count in  c.items()])
print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {get_num_words} total words
--------- Character Count -------
{char_count_output}
============= END ===============
""")
print(sys.argv)

