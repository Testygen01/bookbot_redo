from stats import get_total_words, get_character_frequency, get_sorted_character_freq
import sys

# returns the contents of a text file
def read_file(filepath):
    with open(filepath) as f:
        text_contents = f.read()
    return text_contents

# Main function to execute the code
def main():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py <path_to_file>")
        sys.exit(1)

    # get filepath from the command line
    filepath = sys.argv[1]
    
    file_contents = read_file(filepath)

    print("============ BookBot ============")
    print(f"Analyzing book found at {filepath}...")
    print("------------ Word Count ------------")
    # print total number of words in the text file
    word_count = get_total_words(file_contents)
    print(f"Found {word_count} total words")

    # print the dictionary containing character frequency
    char_freq = get_character_frequency(file_contents)

    # print the sorted list of dictionaries containing character frequency
    lst_of_char_dict = get_sorted_character_freq(char_freq)

    # print the character and frequency nicely
    print("------------ Character Count ------------")
    for dict in lst_of_char_dict:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============ END ============")

main()