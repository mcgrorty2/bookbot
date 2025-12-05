from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = count_words(book)
    character_count = sort_character_counts(count_characters(book))
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in character_count:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
main()