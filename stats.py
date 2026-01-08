def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    characters = {}

    text = text.lower()

    char_list = list(text)

    for char in char_list:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_on(items):
    return items["num"]

def get_char_stats(char_count):
    char_dict_list = []

    for item in char_count:
        temp_dict = {
            "char":item,
            "num":char_count[item]
        }

        char_dict_list.append(temp_dict)

    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list
