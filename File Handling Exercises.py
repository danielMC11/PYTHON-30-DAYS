# Exercises
"""
import re
def count_lines_and_words(document):
    pattern = r'[A-Za-z]+'
    list_words = list()
    for line in document:
        list_words.extend( re.findall(pattern, line))
    print(f'Number of lines: {len(document)}, Number of words: {len(list_words)}')


with open('obama_speech.txt', mode='r') as file:
    count_lines_and_words(file.readlines())
"""
import re

import re
"""

def extract_list_patterns(funct):
    def wrapper(*args):
        pattern = funct()
        list_of_pattern = list()
        list_of_lines = list(args)[0]
        for line in list_of_lines:
            txt = ''.join(line)
            obj_match = re.search(pattern, txt)
            if obj_match:
                start, end = obj_match.span()
                list_of_pattern.append(txt[start:end])
            else:
                continue

        new_list = list()
        for item in list_of_pattern:
            if item not in new_list:
                new_list.append(item)
        return new_list
    return wrapper

@extract_list_patterns
def pattern_from():
    pattern = r'From [A-Za-z.@]+ '
    return pattern

@extract_list_patterns
def pattern_return_path():
    pattern = r'Return-Path: <[A-Za-z@.]+>'
    return pattern

@extract_list_patterns
def received_from():
    pattern = r'Received: from [A-Za-z@.]+ '
    return pattern

@extract_list_patterns
def pattern_by():
    pattern = r'by [A-Za-z@.]+ '
    return pattern

@extract_list_patterns
def pattern_for():
    pattern = r'for <[A-Za-z@.]+>'
    return pattern

@extract_list_patterns
def pattern_to():
    pattern = r'To: [A-Za-z@.]+\n'
    return pattern

@extract_list_patterns
def pattern_from_colon():
    pattern = r'From: [A-Za-z@.]+\n'
    return pattern

@extract_list_patterns
def pattern_author():
    pattern = r'Author: [A-Za-z@.]+\n'
    return pattern


def all_elements_sliced(list_patterns, start):
    new_list = list()
    for line in list_patterns:
        new_list.append(line[start:len(line)-1])
    return new_list


with open('email_exchanges_big.txt', mode='r') as file:
    lines = file.readlines()
    p_from = all_elements_sliced(pattern_from(lines), 5)
    p_re_path = all_elements_sliced(pattern_return_path(lines), 14)
    p_rec_from = all_elements_sliced(received_from(lines), 15)
    p_by = all_elements_sliced(pattern_by(lines), 3)
    p_for = all_elements_sliced(pattern_for(lines), 5)
    p_to = all_elements_sliced(pattern_to(lines), 4)
    p_from_colon = all_elements_sliced(pattern_from_colon(lines), 6)
    p_author = all_elements_sliced(pattern_author(lines), 8)

    list_of_lists_of_mails = [p_from, p_re_path, p_rec_from, p_by, p_for, p_to, p_from_colon, p_author]

    mails = list()
    for list_of_mails in list_of_lists_of_mails:
        for item in list_of_mails:
            if item not in mails:
                mails.append(item)


with open('mails.txt', mode='w') as f:
    lines_mails = '\n'.join(mails)
    f.write(lines_mails)
"""

"""
import re


def bubble_sort(list_of_tuples):
    for i in range(len(list_of_tuples) - 1):
        for j in range(len(list_of_tuples) - i - 1):
            if list_of_tuples[j][1] < list_of_tuples[j + 1][1]:
                temp = list_of_tuples[j]
                list_of_tuples[j] = list_of_tuples[j + 1]
                list_of_tuples[j + 1] = temp
    return list_of_tuples


with open('romeo_and_juliet.txt', mode='r') as f:
    text = f.read()
    #pattern = r'^[A-Za-z]+[. ;,]|[. ;,][A-Za-z]+[. ;,]|^[A-Za-z]+$|[. ;,][A-Za-z]+$'
    pattern = r'[.; ][A-Za-z]+[.; ]'
    words = re.findall(pattern, text)
    unique_words = list()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    amount_per_word = [(i[1:len(i)-1], len(re.findall(i, text))) for i in unique_words]
    top_words = bubble_sort(amount_per_word)
    for index, item in enumerate(top_words[:10]):
        print(f'{index+1}) {item}')

"""
"""
import csv

with open('hacker_news.csv', mode='r') as f:
    csv_file = csv.reader(f, delimiter=',')
    pattern_py = r'^[Pp]ython[.\s]|[.\s][Pp]ython[.\s]|^[Pp]ython$|[.\s][Pp]ython$'
    lines_python = 0
    python_flag = False

    pattern_js = r'^[Jj]ava[Ss]cript[.\s]|[.\s][Jj]ava[Ss]cript[.\s]|^[Jj]ava[Ss]cript$|[.\s][Jj]ava[Ss]cript$'
    lines_javascript = 0
    javascript_flag = False

    pattern_java = r'^Java[.\s]|[.\s]Java[.\s]|^Java$|[.\s]Java$'
    lines_java = 0
    java_flag = False

    for row in csv_file:
        if python_flag is True:
            lines_python += 1
            python_flag = False
        if javascript_flag is True:
            lines_javascript += 1
            javascript_flag = False
        if java_flag is True:
            lines_java += 1
            javascript_flag = False
        for column in row:
            if re.search(pattern_py, str(column)):
                python_flag = True
            if re.search(pattern_js, str(column)):
                javascript_flag = True
            if re.search(pattern_java, str(column)):
                java_flag = True
    print(f'Number of lines with python: {lines_python}',
          f'Number of lines with javascript: {lines_javascript}',
          f'NUmber of lines with java: {lines_java}',
          sep='\n'
          )
"""



