from stats import get_num_words,get_letter_dict

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    content = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(content)
    print(f"{num_words} words found in the document")
    print(get_letter_dict(content))

main()