

#Dictionary Guide

myDict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

#print('Existent Key (4): ', myDict.get('four'), 'non-existent Key (6): ', myDict.get('six'))

myDict['six'] = 6

myDict.popitem()
myDict.pop('one')

listTupleItems = myDict.items()
listKeys = myDict.keys()
listValues = myDict.values()

print(listTupleItems, listKeys, listValues,'\n', type(listTupleItems), type(listKeys), type(listValues), sep='\n')

"""
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
"""