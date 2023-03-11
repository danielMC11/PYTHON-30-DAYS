
from countriesData import *
"""
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

for i in range(1, 8):
    for j in range(0, i):
        print('#', end="")
    print('\n')
else:
    print('\n\n')

for i in range(8):
    for j in range(8):
        print('#', end="")
    print('\n')
else:
    print('\n\n')

for i in range(0, 11):
    print(i,'x', i, '=', i*i)
else:
    print('\n\n')

for i in range(101):
    if i == 0:
        suma = sumaE = sumaO = i
    else:
        suma = suma + i
        if i % 2 == 0:
            sumaE = sumaE + i
        else:
            sumaO = sumaO + i
else:
    print(f'Sum from 0 to 100 is {suma}, Sum of Even {sumaE}, Sum of Odd {sumaO}')


lands = list()
for country in countries:
    if 'land' in country:
        lands.append(country)
else:
    print('Country Lands: ', lands)

fruit_list = ['banana', 'orange', 'mango', 'lemon']
rev = list()


for i in range(len(fruit_list)):
    rev.insert(0, fruit_list[i])
else:
    print(rev)
"""

world_languages = set()

for dicts in countries_data:
    for lan in dicts['languages']:
        world_languages.add(lan)

list_lan = list(world_languages)
list_lan.sort()
print('Number of Languages: ', len(list_lan))

number_of_countries_lan = dict()

for lan in list_lan:
    n = 0
    for dicts in countries_data:
        if lan in dicts['languages']:
            n += 1
    number_of_countries_lan[lan] = n

valuesList = list(number_of_countries_lan.values())
valuesList.sort(reverse=True)

top_spoken_lan = dict()

for n in valuesList:
    for key, value in number_of_countries_lan.items():
        if n == value:
            top_spoken_lan[key] = value
            break


KeysTop = list(top_spoken_lan.keys())
ValuesTop = list(top_spoken_lan.values())

print('Top 10 Spoken Languages Around The World')
for i in range(10):
    print(i+1,'.',KeysTop[i], ' = ', ValuesTop[i], sep="")

populations = list()

for dicts in countries_data:
    populations.append(dicts['population'])

populations.sort(reverse=True)

top_populated = dict()

for i in populations:
    for dicts in countries_data:
        if dicts['population'] == i:
            top_populated[dicts['name']] = i
            break

keysTopPop = list(top_populated.keys())
valuesTopPop = list(top_populated.values())

print('Top 10 most populated Countries Around The World')
for i in range(10):
    print(i+1,'. ',keysTopPop[i], ' = ', valuesTopPop[i])


