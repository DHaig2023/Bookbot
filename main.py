def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    letters = count_letters(text)
    print(letters)

def count_words(text):
    words = text.split()
    return len(words)



def count_letters(text):
    lower_text = text.lower()
    letters_in_text = {}
    for letter in lower_text:
        if letter in letters_in_text:
            letters_in_text[letter] += 1
        else:
            letters_in_text[letter] = 1
    return letters_in_text

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
