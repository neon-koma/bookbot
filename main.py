def main():
    # variables
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    wordcount = get_word_number(text)
    chars_sortlist = dict_to_sortlist(get_chars_dict(text))
    
    #print book report
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount} words found in this document\n")

    for i in chars_sortlist:
        print(f"The '{i['char']} character was found {i['num']} times")
    
    print("--- End report ---")



# return book from path
def get_text(path):
    with open(path) as f:
        return f.read()

# count words
def get_word_number(text):
    return len(text.split())

# get amount of each char
def get_chars_dict(text):
    chardict = {}
    text = text.lower()
    for c in text:
        if c.isalpha():
            if c in chardict:
                chardict[c] += 1
            else:
                chardict[c] = 1
    return chardict

# for sorting
def sort_on(d):
    return d["num"]

# char dictionary to sorted list of dictionaries
def dict_to_sortlist(chars_dict):
    list = []
    for c in chars_dict:
        list.append({"char": c, "num": chars_dict[c]})
    
    list.sort(reverse=True, key=sort_on)
    return list

main()