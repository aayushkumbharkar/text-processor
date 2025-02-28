import argparse
import os

def count_words(file_path: str) -> int:
    """Counts the total number of words in the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return len(text.split())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0

def count_chars(file_path: str) -> int:
    """Counts the total number of characters in the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return len(text)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0

def count_lines(file_path: str) -> int:
    """Counts the total number of lines in the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0

def find_word(file_path: str, word: str) -> int:
    """Finds the occurrences of a specific word in the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text.lower().split().count(word.lower())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0

def replace_word(file_path: str, old_word: str, new_word: str) -> str:
    """Replaces a word in the file and saves a new file."""
    new_file_path = f"updated_{os.path.basename(file_path)}"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        updated_text = text.replace(old_word, new_word)
        
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(updated_text)
        
        return new_file_path
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""

def main():
    parser = argparse.ArgumentParser(description="Command-line tool to process text files.")
    
    parser.add_argument("-f", "--file", required=True, help="Path to the text file")
    parser.add_argument("-wc", "--word-count", action="store_true", help="Count words in the file")
    parser.add_argument("-cc", "--char-count", action="store_true", help="Count characters in the file")
    parser.add_argument("-lc", "--line-count", action="store_true", help="Count lines in the file")
    parser.add_argument("-find", "--find", metavar="WORD", help="Find a word in the file")
    parser.add_argument("-r", "--replace", nargs=2, metavar=("OLD", "NEW"), help="Replace a word in the file")

    args = parser.parse_args()
    file_path = args.file

    if args.word_count:
        print(f"Word Count: {count_words(file_path)}")

    if args.char_count:
        print(f"Character Count: {count_chars(file_path)}")

    if args.line_count:
        print(f"Line Count: {count_lines(file_path)}")

    if args.find:
        word_count = find_word(file_path, args.find)
        print(f'The word "{args.find}" occurs {word_count} times.')

    if args.replace:
        old_word, new_word = args.replace
        new_file = replace_word(file_path, old_word, new_word)
        if new_file:
            print(f'"{old_word}" was replaced with "{new_word}" and saved to {new_file}.')

if __name__ == "__main__":
    main()
