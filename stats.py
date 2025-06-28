def count_words(book):
    word_list = book.split()
    return len(word_list)
# this counts the number of words in a book

def count_characters(book):
    all_lower_case = book.lower()
    characters_dict = {}
    for character in all_lower_case:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict