from stats import get_num_words, get_char_count, get_char_stats
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    char_stats = get_char_stats(char_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for stat in char_stats:
        if stat["char"].isalpha():
            print(f"{stat["char"]}: {stat["num"]}")
    print(f"============= END ===============")

main()