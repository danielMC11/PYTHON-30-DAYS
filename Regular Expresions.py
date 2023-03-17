import re

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