def word_count(book):
    count = len(book.split())
    return count

def count_chars(text):
    text = text.lower()
    char_count_dict = {}

    for char in text:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1

    return char_count_dict

def sorted_dict_list(dictionary):
    sorted_list = []
    for char, count in dictionary.items():
        char_dict = {"char": char, "count": count}
        sorted_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list