import re
# Regular Expresions
# match
text_no_multiline = 'Daniel Ricardo Montero'                # re.I stands for IGNORECASE lower or uppper
object_match = re.match('Daniel', text_no_multiline, re.I)  # pattern must be at star, else returns None
print(object_match)
print(object_match.span())  # tuple (0, n) range of the substring in string

# search
text_multiline = '''Hello there my name is Daniel Ricardo.
I live in Colombia and SPANISH IS MY FIRST LANGUAGE'''
object_match = re.search('Colombia', text_multiline, re.I)  # pattern can be anywhere, else returns None
print(object_match)
print(object_match.span())  # tuple (a, b) range of the substring in string

# findall
list_matches = re.findall('my', text_multiline, re.I)
print(list_matches)
list_matches = re.findall('my|MY', text_multiline)  # No flag was given, thus | indicates valid uppercase variation
print(list_matches)

# Replace using substring / sub
matches_replaced_string = re.sub('my|MY', 'his', text_multiline)  # replace matches by another substring
print(matches_replaced_string)

list_sep = matches_replaced_string.split(' ')
print(list_sep)
list_sep.clear()
list_sep = re.split(' ', matches_replaced_string)
print(list_sep)


txt = '''Hello1 and hello2'''

#Square Bracket
reg_ex = r'[Hh]ello[0-9]'   # Variation in sequence of characters, also includes character classes 0-9 A-Z
matches_list = re.findall(reg_ex, txt)
print(matches_list)

#Special Characters
reg_ex = r'\Dello\d'   # Other Character classes \D includes Non-digits \d includes digits
print(re.findall(reg_ex, txt))

reg_ex = r'\s'         # Includes whitespace
print(re.findall(reg_ex, txt))
reg_ex = r'\S'          # Includes Non-whitespace
print(re.findall(reg_ex, txt))
reg_ex = r'\w'         # Includes one word character
print(re.findall(reg_ex, txt))
reg_ex = r'\W'         # Includes Non-one word character
print(re.findall(reg_ex, txt))

#Includes all characters except \n

txt = '''Hello1 and hello2
2023'''
reg_ex = r'.'          # .
print(re.findall(reg_ex, txt))

# ^ esto
reg_ex = r'^Hello'      # same as re.match, starts pattern in string txt
print(re.findall(reg_ex, txt))
reg_ex = r'[^and12]'    # Does not include any character in the sequence
print(re.findall(reg_ex, txt))

# $ ends with
reg_ex = r'2023$'   # ends string with pattern
print(re.findall(reg_ex, txt))

# Quantifiers Store in a slot of the list the pattern extended if substring matches
txt = 'Shadow_Spartan777'
reg_ex = r'S*'  # pattern length can be 0 or more
print(re.findall(reg_ex, txt))
reg_ex = r'[A-Za-z]+'  # pattern length can be 1 or more
print(re.findall(reg_ex, txt))
reg_ex = r'[_7]?' # pattern length can be 0 or 1
print(re.findall(reg_ex, txt))
reg_ex = r'[A-Za-z_\d]{3}'  # pattern length is exactly 3
print(re.findall(reg_ex, txt))
reg_ex = r'[A-Za-z_\d]{1,3}' # pattern length is between 1 and 3
print(re.findall(reg_ex, txt))

paragraph = 'I love teaching. If you do not love teaching what else can you love.I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
rx_words = r'[^ .]+'
words = re.findall(rx_words, paragraph)
print(words)

frequent_words = [(len(re.findall(r'[ .]?' + i + r'[ .]', paragraph)), i) for i in set(words)]
print(frequent_words)


def is_valid_variable(var):
    valid = r'[a-z]+_?[a-z]+'
    match = re.match(valid, var)
    if match:
        start, end = match.span()
        print(var == var[start:end])
    else:
        print(False)


is_valid_variable('first_name')
is_valid_variable('first-name')
is_valid_variable('1first_name')
is_valid_variable('firstname')


def extract_numbers(txt):
    pattern = r'-?\d+'
    list_numbers = [int(i) for i in re.findall(pattern, txt)]
    return list_numbers


statement = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
Extract these numbers from this whole text and find the distance between the two furthest particles.'''


numbers = extract_numbers(statement)
numbers.sort()
max_distance = abs(numbers[len(numbers)-1] - numbers[0])
print(max_distance)

def clean_text(txt):
    pattern = r'[^a-zA-z\s.!?]'
    new_str = re.sub(pattern, '', txt)
    return new_str

def get_words_txt(txt):
    pattern = r'[A-Za-z]+'
    list_words = re.findall(pattern, txt)
    return list_words

def unique_words(txt):
    list_uniq = list()
    for i in txt:
        if i not in list_uniq:
            list_uniq.append(i)
    return list_uniq


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

new_sentence = clean_text(sentence)
print(new_sentence)
words = get_words_txt(new_sentence)
u_words = unique_words(words)

re_clean = r'[^a-zA-z ]+'

f_words = [(i, len(re.findall(r' ' + i + r' ', ' ' + re.sub(re_clean, '', new_sentence) + ' '))) for i in u_words]
print(f_words)


list_indexes = list()
list_sorted = list()
var = 0


def bubble_sort_l(list_):
    for i in range(len(list_)):
        for j in range(0, len(list_) - i - 1):
            if list_[j] > list_[j + 1]:
                temp = list_[j]
                list_[j] = list_[j + 1]
                list_[j + 1] = temp


def bubble_sort_lt(list_tup):
    for i in range(len(list_tup)):
        for j in range(0, len(list_tup) - i - 1):
            if list_tup[j][1] < list_tup[j + 1][1]:
                temp = list_tup[j]
                list_tup[j] = list_tup[j + 1]
                list_tup[j + 1] = temp


bubble_sort_lt(f_words)
print(f_words)



