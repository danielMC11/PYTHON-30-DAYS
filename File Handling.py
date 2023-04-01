"""Reading"""                       # read content and jumps into a new line
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

#file = open('my_data.txt', mode="x")     #create a new file, error if already exists
#file.close()
"""
print('msg')
with open('my_data.txt', mode='r+') as file:       # Read and write existing file
    file.write('DEAD BODIES EVERYWHERE')
    print(file.read())                             # Prints nothing, file pointer at the end
    file.seek(0)
    print(file.read())

with open('my_data_v2.txt', mode='w+') as file:    # Read and write not necessarily existing file
    file.write('SOMETHING TAKES A PART OF ME')
    print(file.read())                             # Prints nothing, file pointer at the end
    file.seek(0)
    print(file.read())

with open('my_data.txt', mode='r+') as file:
    print('A', file.read())                     # Prints and move file pointer at the end
    print('B', file.read())                     # Prints nothing, file pointer at the end

"""


"""
# rewrite and append give the same result always
print('msg')
with open('my_data_v2.txt', mode='w') as file:
    file.write('HEY')

with open('my_data_v2.txt', mode='a+') as file:     # Append and read, file pointer at the end when reading or appending
    file.write('\nShut the Fck Up')
    file.seek(0)
    print(file.read())
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

import json

"""
print('msg')
with open('text_json.json', mode='r+', encoding='utf-8') as file:
    dict_obj = json.loads(file.read())
    dict_obj['name'] = 'Camilo'
    dict_obj['skills'].extend(['Python', 'C++'])
    dict_obj['Languages'] = ['Spanish', 'English']
    file.seek(0)
    json_str = json.dumps(dict_obj, indent=4)           # Two steps, convert dict to json string format
    file.write(json_str)                                # and write in the file with the str
    dict_obj['music-tastes'] = ['nu-metal', 'indie', 'hip-hop']
    file.seek(0)
    json.dump(dict_obj, file, indent=4)                 # One step, send directly dict and file pointer
"""
#file = open('list_dict.json', mode='x')
#file.close()

#with open('list_dict.json', mode='r+') as file:
#    list_dict = [{i: i**2} for i in range(11)]
#    json.dump(list_dict, file, indent=5)
"""
print('msg')
with open('list_dict.json', mode='r+') as file:
    list_dict = json.load(file)
    list_dict[0]["0"] = 10
    file.seek(0)
    json.dump(list_dict, file, indent=4)
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


