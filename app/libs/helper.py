
def is_isbn_or_key(word):
    """
    是判断q是isbn还是key
    """

    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('_', '')
    if '_' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key