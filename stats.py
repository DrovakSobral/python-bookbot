def get_word_count(book_text: str):
    return len(book_text.split())

def sort_on(items):
    return items["num"]

def get_character_count(book_text: str):
    normalized_lower_case_text = book_text.lower()
    character_count_dict = {}
    for letter in normalized_lower_case_text:
        if letter not in character_count_dict:
            if letter.isalpha():
                character_count_dict[letter] = 1
        else:
            character_count_dict[letter] = character_count_dict[letter] + 1
    
    dict_list_to_sort = []
    temp_dict = {}
    for key, value in character_count_dict.items():
        temp_dict = {"name": key, "num": value}
        dict_list_to_sort.append(temp_dict)
    dict_list_to_sort.sort(reverse=True, key=sort_on)
    temp_dict = {}
    for dict_item in dict_list_to_sort:
        temp_dict[dict_item["name"]] = dict_item["num"]
    character_count_dict = temp_dict
    return character_count_dict