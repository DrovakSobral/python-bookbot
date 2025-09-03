from pathlib import Path
from stats import get_word_count, get_character_count

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    book = ("books/frankenstein.txt")
    book_text = get_book_text(book)
    word_count = get_word_count(book_text)
    character_count_dict = get_character_count(book_text)
    print(f"{word_count} words found in the document")
    for key, value in character_count_dict.items():
        print(f"\'{key}\': {value}")


main()
