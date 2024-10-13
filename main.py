def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text) 
    new_dict = dict_to_list(num_chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document!\n")
    for w in new_dict:
        print(f"The '{w["name"]}' character was found {w["num"]} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]

def dict_to_list(num_chars):
    list_of_dicts = []
    for key, value in num_chars.items():
        if key.isalpha():
            list_of_dicts.append({"name": key, "num": value})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def get_num_words(text):
    words = text.split()
    return len(words) 

def get_num_chars(text):
    words = text.split()
    char_count = {}
    for word in words:
        lowered_string = word.lower()
        for char in lowered_string:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
