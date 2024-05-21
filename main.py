def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_wordcount(text)
    letter_count = get_letter_count(text)
    dict_list = sort_letter_count_dict(letter_count)
    #print(text)
    #print(count)
    #print(letter_count)
    #print(dict_list)
    #dict_list.sort(reverse=True, key=sort_on)
    #print(dict_list)
    construct_report(book_path, word_count, dict_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_wordcount(book):
    words = book.split()
    ### can also easily do this  by returning len(words)
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def get_letter_count(book):
    ### don't need to split the string, can iterate over every char of the string as a list, just make lower to remove dupes. 
    book = book.lower()
    counts = {}
    for letter in book:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

def sort_letter_count_dict(letter_count):
    letter_count_list = []
    for key in letter_count:
        if key.isalpha():
            dict = {'char': key, 'count': letter_count[key]}
            letter_count_list.append(dict)
    return letter_count_list

def sort_on(dict_list):
    return dict_list["count"]

def construct_report(book_path, word_count, sorted_list):
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{word_count} words found in the document\n")
    sorted_list.sort(reverse=True, key=sort_on)
    for d in sorted_list:
        print(f"The {d['char']} character was found {d['count']} times\n")
    print(f"--- End report ---")





main()