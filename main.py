import sys
from pathlib import Path
from stats import get_word_count, get_character_count

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Wrong argument format! Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit(2)
    word_count = get_word_count(book_text)
    character_count_dict = get_character_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in character_count_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()