from pathlib import Path

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    book = ("books/frankenstein.txt")
    book_text = get_book_text(book)
    word_count = len(book_text.split())
    print(f"{word_count} words found in the document")


main()
