def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
# this reads the text of a book from a file
    
from stats import count_words, count_characters
# this imports the functions from stats.py

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    characters_dict = count_characters(text)
    print(f"{count_words(text)} words found in the document")
    print(characters_dict)

main()