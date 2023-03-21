"""Reading"""
"""
                                    #  r and t defaulf value
f = open('my_file.txt', mode='rt')# r (read) a (append) w (write) x (create) t (text mode) b (binary mode)
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
# XML
"""
xml_str = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc wealth="rich">141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc wealth="rich">59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc wealth="poor">13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''
root = ET.fromstring(xml_str)
"""

"""
import xml.etree.ElementTree as ET

tree = ET.parse('Countries.xml')
root = tree.getroot()

for country in root.findall('country'):
    name = country.get('name')
    gdp = country.find('gdppc').text
    gdp_type = country.find('gdppc').get('wealth')
    print(f'Country: {name}, Gdp: {gdp} and Type of Wealth: {gdp_type}')

for neighbor_tag in root.iter('neighbor'):
    print(neighbor_tag.attrib)

for year_tag in root.iter('year'):
    print(year_tag.tag, year_tag.text)

for country in root.findall('country'):
    if country.get('name') == 'Liechtenstein':
        country.set('continent', 'europe')
    elif country.get('name') == 'Singapore':
        country.set('continent', 'asia')
    else:
        country.set('continent', 'south-america')


#root.append(ET.SubElement(root, 'Country', {'name': 'Colombia', 'continent': 'south-america'}))

tree.write('Countries.xml')
"""

# Exercises
"""
import re
def count_lines_and_words(document):
    pattern = r'[A-Za-z]+'
    list_words = list()
    for line in document:
        list_words.extend(re.findall(pattern, line))
    print(f'Number of lines: {len(document)}, Number of words: {len(list_words)}')


with open('obama_speech.txt', mode='r') as file:
    count_lines_and_words(file.readlines())
"""

import json

"""
try:
    data = json.load('countries_data.json')
except Exception as e:
    print(type(e), e)
"""



