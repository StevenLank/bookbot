import sys
from stats import get_count_words
from stats import count_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():

    args = sys.argv
    if len(args) < 2 or len(args) >= 3:
        print("how to use sys.argv Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_loc = args[1]
    
    book = get_book_text(book_loc) 
    count = get_count_words(book)
    lowercase = count_characters(book)
    sort = sort_characters(lowercase) 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for s in sort:
        if s["char"].isalpha():
            print(f"{s["char"]}: {s["num"]}")
    print("============= END ===============")
        
            

main()