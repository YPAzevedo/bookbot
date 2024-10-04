def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count_map = get_char_count_map(text)
    char_count_list = get_sorted_book_chars_by_count(char_count_map)

    report_book_stats(book_path, num_words, char_count_list)  


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count_map(book_text):
    char_count_map = {}
    for char in book_text:
        if not char.isalpha():
            continue
        lowered = char.lower()
        if lowered in char_count_map:
            char_count_map[lowered] += 1
        else:
            char_count_map[lowered] = 1
    return char_count_map

def get_sorted_book_chars_by_count(chars_count_map):
    chars_count_list = []
    for char in chars_count_map:
        chars_count_list.append({
            "char": char,
            "count": chars_count_map[char]
        })
    chars_count_list.sort(reverse=True, key=lambda d: d['count'])
    return chars_count_list


def report_book_stats(book_path, num_words, char_count_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n\n")
    
    for entry in char_count_list:
        print(f"The '{entry["char"]}' character was found {entry["count"]} times")
    print(f"\n-- End report --")


main()
