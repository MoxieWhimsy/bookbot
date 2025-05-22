def get_num_words(content) -> int:
    words = content.split()
    num_words = len(words)
    return num_words

def get_letter_dict(content) -> dict:
    result = {}
    for letter in content:
        letter = letter.lower()
        if letter not in result:
            result[letter] = 1
            continue
        result[letter] += 1
    return result