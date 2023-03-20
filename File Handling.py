"""Reading"""
"""
                                    #  r and t defaulf value
f = open('my_file.txt', mode='rt')  # r (read) a (append) w (write) x (create) t (text mode) b (binary mode)
txt = f.read()                      # return str all text
#print(txt)
f.close()

f = open('my_file.txt')
txt_first = f.readline()                  # return str first line
#print(txt_first)
f.close()

f = open('my_file.txt')
txt_list = f.readlines()                 # return list of all the lines
#print(txt_list)
f.close()

# other way of opening a file, close automatically
with open('my_file.txt') as f:
  txt = f.read().splitlines()  # method same as read lines - No \n included
  print(txt)
"""

"""
#with open('my_file.txt', mode='a') as f:           # Appending to the existing text
    f.write('\nI am currently studying system engineering.')

#with open('my_file.txt', mode='w') as f:           # Overwriting to a new text
    f.write('Hello world')
"""

"""Deleting Files"""
"""
import os

if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
else:
    print('The file does not exist')
"""
"""
import json
# JavaScript Object Notation
# Enclosed dictionary in string, str keys or values use double quotes ""
person_json = '''{
    "name": "Daniel",
    "age": 19,
    "Country": "Colombia",
    "skills": []
}'''

person_dct = json.loads(person_json)  # convert json to dict
print(person_dct)

person_json_converted = json.dumps(person_dct, indent=8)  # convert dict to json, indent for indentation of pairs
print(type(person_json_converted))
print(person_json_converted)

with open('text_json.json', mode='w', encoding='utf-8') as f:
    json.dump(person_dct, f, ensure_ascii=False, indent=7)
"""
"""
import csv

with open('text_csv.csv', mode='r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    lines_count = 0

    for row in csv_reader:
        if lines_count == 0:
            print(f"Keys: {', '.join(row)}")
            lines_count += 1
        else:
            print(f"Values: {row[0]}, {row[1]}, {row[2]}")
            lines_count += 1
    print(f'Number of lines: {lines_count}')
"""




