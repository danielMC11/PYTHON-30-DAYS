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
txt = ''
reg_ex = r''