def get_word_count(book_text: str):
    return len(book_text.split())

def get_character_count(book_text: str):
    normalized_lower_case_text = book_text.lower()
    character_count_dict = {}
    for letter in normalized_lower_case_text:
        if letter not in character_count_dict:
            character_count_dict[letter] = 1
        else:
            character_count_dict[letter] = character_count_dict[letter] + 1
    return character_count_dict