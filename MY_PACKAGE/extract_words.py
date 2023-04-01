import re
from string import ascii_lowercase as low, ascii_uppercase as up


def unique_words(txt):
    pattern1 = r'[A-Za-z]+[ .;,!-]'
    lst_p1 = re.findall(pattern1, txt)
    pattern2 = r'[. ;,!-][A-Za-z]+[. ;,!-]'
    lst_p2 = re.findall(pattern2, txt)
    pattern3 = r'^[A-Za-z]+$'
    lst_p3 = re.findall(pattern3, txt)
    pattern4 = r'[ .;,!-][A-Za-z]+$'
    lst_p4 = re.findall(pattern4, txt)
    lst_all_p = [lst_p1, lst_p2, lst_p3, lst_p4]
    words_patterns = list()
    for p in lst_all_p:
        words_patterns.extend(p)
    words = clean_words(words_patterns)
    unique_words = list()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


def clean_words(lst_words):
    new_words = list()
    all_letters = low + up
    for word in lst_words:
        if word[0] not in all_letters and word[len(word)-1] not in all_letters:
            new_words.append(word[1:len(word)-1])
        elif word[0] not in all_letters:
            new_words.append((word[1:]))
        elif word[len(word)-1] not in all_letters:
            new_words.append(word[:len(word)-1])
        else:
            new_words.append(word)
    return new_words


#with open('../romeo_and_juliet.txt') as f:
#    words = unique_words(f.read())
#    print(len(words))
