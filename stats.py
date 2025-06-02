
# returns the total number of words in a text file
def get_total_words(text):
    word_lst = text.split()
    word_count = len(word_lst)
    return word_count

# returns a dictionary that contain the number of times each character occurs
def get_character_frequency(text):
    frequency_dict = {}
    lower_text = text.lower() # Normalize the text to avoid duplicates
    for char in lower_text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

# sort key
def sort_on(dict):
    return dict["num"]

# returns a sorted list of dictionaries containing each character and its number of occurrences.
def get_sorted_character_freq(dict):
    sorted_lst_of_char = []
    for key in dict:
        sorted_lst_of_char.append({"char": key, "num": dict[key]})
    
    #sort
    sorted_lst_of_char.sort(reverse=True, key=sort_on)
    return sorted_lst_of_char