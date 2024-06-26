#Bookbot - Read file

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    report = get_report(letter_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in report:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['num']} times")

    print("--- End report ---")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

#### Count Letters ####

def get_letter_count(text):
    letter_dict = {}
    lower_case = text.lower()
    for letters in lower_case:
        # count = 0
        if letters in letter_dict:
            letter_dict[letters] += 1
        else:
             letter_dict[letters] = 1
    return letter_dict

#### Count words ####

def get_word_count(book):
    words = book.split()
    return f"Word Count: {len(words)}"

#### Print a Report ####
def sort_on(d):
    return d["num"]


def get_report(dict):
    sorter = []
    for char in dict:
        sorter.append({"character" : char, "num": dict[char]})
    sorter.sort(reverse=True, key=sort_on)
    return sorter
main()
