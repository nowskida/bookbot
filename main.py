def count_words(file_contents):
    words = file_contents.split()
    counter = 0
    for w in words:
        counter += 1
    return counter
def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

main()
