import re
from string import ascii_lowercase as low, ascii_uppercase as up, punctuation as punc


def clean_word(txt):
    pattern = r'\b\w+\b'
    match = re.search(pattern, txt)
    start, end = match.span() if match is not None else print('no word')
    return txt[start:end]


def get_words(func):
    def wrapper(*args):
        text = list(args)[0]
        pattern = r'\b\w+\b'
        words_patterns = re.findall(pattern, text)
        return func(words_patterns)
    return wrapper


@get_words
def all_words(words):
    return words


@get_words
def unique_words(words):
    unique = list()
    for word in words:
        if word not in unique:
            unique.append(word)
    return unique


