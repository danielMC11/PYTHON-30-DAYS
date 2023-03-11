
"""
#Function as a Parameter

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a -b

def operations(op, f1, f2, a, b):
    if op == 1:
        return f1(a, b)
    elif op == 2:
        return f2(a, b)
    else:
        return None

result = operations(int(input('Opcion 1 (+) / Opcion 2 (-): ')), addition, subtraction, int(input('n1: ')), int(input('n2: ')))
print(result)

"""


"""
#Functions as a Result Value

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def operations(op):
    if op == 1:
        return addition
    elif op == 2:
        return subtraction
    else:
        return None

r_function = operations(int(input('Opcion 1 (+) / Opcion 2 (-): ')))
result = r_function(int(input('n1: ')), int(input('n2: ')))
print(result)
"""
"""
#closures

def operations(op):
    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    if op == 1:
        return addition
    elif op == 2:
        return subtraction
    else:
        return None

r_function = operations(int(input('Operation (+) / Operation (-): ')))
result = r_function(int(input('n1: ')), int(input('n2: ')))
print(result)

"""
"""
#decorators
def article(content):
    print('Decorator executing.. ')

    def wrapper(*args, **kwargs):
        print('Title: ', list(args)[0], end='\n\n')
        content(kwargs)
        print('Author: ', list(args)[1])
    return wrapper

@article
def structured_document(di):
    for i, j in di.items():
        print(i, j, end='\n\n', sep=': ')

@article
def unstructured_document(di):
    for i in di.values():
        print(i, end='\n\n')


structured_document('Python Decorators', 'Daniel Montero', Definition='This is a python pattern design used to add new functionality to functions',
          Explanation='It takes the functions to our decorator function which is also used inside a wrapper function',
          Difficulty='7/10', Related='Functions as Parameter, Functions as return Value'
          )

unstructured_document('Python Decorators', 'Daniel Montero', Definition='This is a python pattern design used to add new functionality to functions',
          Explanation='It takes the functions to our decorator function which is also used inside a wrapper function',
          Difficulty='7/10', Related='Functions as Parameter, Functions as return Value'
          )
"""
#built-in higher order functions

from functools import reduce
from itertools import accumulate


def square(x):
    return x**2


def is_even(x):
    if x % 2 == 0:
        return True
    return False


numbers = [i for i in range(10)]

squared_numbers = map(square, numbers)  #Applies the given function to each value of the sequence and returns it
print(list(squared_numbers), type(squared_numbers))

even_numbers = filter(is_even, numbers) #Applies the given bool function to each value of the sequence and if True: returns
print(list(even_numbers), type(even_numbers))

summation = reduce(lambda a, b: a + b, numbers)
print('Sum of Numbers: ', summation)
process_N_summation = accumulate(numbers, lambda a, b: a + b)
list_process = list(process_N_summation)
print('Process and Result: ', list_process)


for i, j in enumerate(list_process[1:]):
    print('+'.join([str(n) for n in numbers[:i+2] if i+2 <= len(numbers)]), j, sep=' = ')

countries_list = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def land_in(x):
    if 'land' in x:
        return True
    return False


countries_not_land = filter(land_in, countries_list)
print('Countries with Land: ', list(countries_not_land))


def concatenate_red(x, y):
    if y == countries_list[len(countries_list) - 1]:
        return x + ', and ' + y + ' are north European countries'
    return x + ', ' + y


phrase = reduce(concatenate_red, countries_list)
print(phrase)

list_items = [1, 2, '3', 4, 5, '6', 7.1, '9']
print(list(filter(lambda x: type(x) == str, list_items)))


def sequence_in(country, seq):
    if seq in country:
        return True
    return False


def categorize_countries(countries, *seqs):

    list_patterns =[['Pattern: ' + i, [list(filter(lambda country: sequence_in(country, i), countries))]]for i in list(seqs)]
    return list_patterns


countries_list = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for i in categorize_countries(countries_list, 'land', 'ia', 'Island', 'stan'):
    print(i)


from string import ascii_uppercase as letters_up


def starting_letters(countries):
    letters_dict = {i: len([j for j in list(filter(lambda x: x[0] == i, countries))]) for i in letters_up}
    print(letters_dict)


starting_letters(countries_list)


def get_first_ten_countries(country):
    if country in countries_list[:10]:
        return True
    return False


def get_last_ten_countries(country):
    if country in countries_list[-10:]:
        return True
    return False


first_ten = list(filter(get_first_ten_countries, countries_list))
print(first_ten)
last_ten = list(filter(get_last_ten_countries, countries_list))
print(last_ten)

from countriesData import countries_data
