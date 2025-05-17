def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    content = get_book_text("books/frankenstein.txt")
    words = content.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

main()