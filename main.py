from stats import get_num_words,get_letter_dict,get_sorted_letter_list
import sys

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_report(filepath) -> str:
    content = get_book_text(filepath)
    num_words = get_num_words(content)
    letter_dict = get_letter_dict(content)
    letter_list = get_sorted_letter_list(letter_dict)
    result = "============ BOOKBOT ============\n"
    result += f"Analyzing book found at {filepath}...\n"
    result += "----------- Word Count ----------\n"
    result += f"Found {num_words} total words\n"
    result += "--------- Character Count -------\n"
    for pair in letter_list:
        result += f"{pair["char"]}: {pair["num"]}\n"
    result += "============= END ==============="
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    print(get_report(sys.argv[1]))

main()