
"""
#List Guide
myList = [1, 2, 3, 4, 5]

myList.append(6) # [1, 2, 3, 4, 5 , 6]
myList.insert(2, 2.5) # [1, 2, 2.5, 3, 4, 5, 6]

myList.remove(2.5)  # [1, 2, 3, 4, 5 ,6]
myList.pop() # [1, 2, 3, 4, 5]
myList.pop(0) # [2, 3, 4, 5]
del myList[1:3:1] # [2, 5]

myListPointer = myList
myListPointer.append(7)
print(myListPointer, '=', myList)

my_other_list = myList.copy()
my_other_list.pop()
print(my_other_list, '!=', myList)

listA = ['a']
listB = ['b']
listAB = listA + listB
listA.extend(listB)
print(listA)

my_list = [1, 0, 1, 0, 1]
print(my_list.count(0))

my_lista = ['a', 'b', 'c', 'd', 'e']
position = my_lista.index('d',1,5)
print(position, my_lista[position])

reverse_list = [1, 2, 3, 4]
alt_rev = reverse_list.copy()
reverse_list.reverse()
print(reverse_list)
print(alt_rev[::-1])

unordered_list = [1,3,5,0,2]
unordered_list.sort()
print('ascending:',unordered_list)
unordered_list.sort(reverse=True)
print('descending:',unordered_list)
no_effect = [1,3,2]
print(no_effect,'sorted:', sorted(no_effect))
"""
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

print('min:', ages[0], 'max:', ages[len(ages) - 1])
ages.append(ages[0])
ages.append(ages[len(ages)-2])
print(ages)
print('median:', (ages[len(ages)//2] + (ages[len(ages)//2])+1)//2)
print('average age:', sum(ages)/len(ages))
ages.sort()
print('range:', ages[len(ages)-1] - ages[0])
print('Comparison:', abs(ages[0] - sum(ages)/len(ages)) == abs(ages[len(ages)-1] - sum(ages)/len(ages)))
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia Colombia',
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
  'Colombi',
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
];
print('middle country:', countries[len(countries)//2])


if len(countries) % 2 == 0:
    country_list_1 = countries[0:(len(countries)//2)]
    country_list_2 = countries[len(countries)//2:]
else:
    country_list_1 = countries[0:(len(countries) // 2)+1]
    country_list_2 = countries[(len(countries) // 2)+1:]
print('First Half:', len(country_list_1), '\nSecond Half', len(country_list_2))

paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

ch, rus, usa, *sc = paises

print(ch, rus, usa, sc)
"""