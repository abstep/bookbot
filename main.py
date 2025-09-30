import sys
from sys import argv
from bookbot.stats import count_words
from bookbot.stats import count_characters
from bookbot.stats import sort_characters

def get_path():
    if len(argv) > 1:
        return argv[1]
    else:
        print("Usage: python3 main.py <file_path>")
        sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    path = get_path()
    book_text = get_book_text(path)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path + "...")
    print("----------- Word Count ----------")
    print("Found " + str(num_words) + " total words")
    print("--------- Character Count -------")
    sorted_counts = sort_characters(num_characters)
    for char, count in sorted_counts:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    

main()