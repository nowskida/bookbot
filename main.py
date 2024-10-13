def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text) 
    print(f"{num_words} words found in the document!")
    print(num_chars)

def get_num_words(text):
    words = text.split()
    counter = 0
    for w in words:
        counter += 1
    return counter

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
