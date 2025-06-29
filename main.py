import sys
# uses system arguments to get the book file path

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
# this reads the text of a book from a file
    
from stats import count_words, count_characters, sort_characters
# this imports the functions from stats.py

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    characters_dict = count_characters(text)
    sorted_dict = sort_characters(characters_dict)
    print(f"Found {count_words(text)} total words")
    for pair in sorted_dict:
        if pair['char'].isalpha():
            print(f"{pair['char']}: {pair['num']}")
# this prints the number of words and characters in the book and sorts the characters by count (only including letters)

main()