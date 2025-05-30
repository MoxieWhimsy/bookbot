def get_num_words(content) -> int:
    words = content.split()
    num_words = len(words)
    return num_words

def get_letter_dict(content) -> dict:
    result = {}
    for letter in content:
        letter = letter.lower()
        if not letter.isalpha():
            continue
        if letter not in result:
            result[letter] = 1
            continue
        result[letter] += 1
    return result

def get_sorted_letter_list(letter_dict: dict) -> list:
    def get_count(e):
        return e["num"]
    letter_list = []
    for letter in letter_dict:
        pair = dict()
        pair["char"] = letter
        pair["num"] = letter_dict[letter]
        letter_list.append(pair)
    letter_list.sort(key=get_count, reverse=True)
    return letter_list