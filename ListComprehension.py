numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

list_neg_N_zero = [i for i in range(-4,7) if i <= 0]

print(list_neg_N_zero)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [i for outer in list_of_lists for inner in outer for i in inner]
print(flattened_list, end='\n\n')

list_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0, 11)]

for i in list_tuples:
    if i == list_tuples[len(list_tuples)-1]:
        print(i, end='\n\n')
    else:
        print(i)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [list(i) for outer in countries for i in outer]
print(new_countries, end='\n\n')

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [{'country':i.upper()} for outer in countries for inner in outer for i in inner]
print(new_countries, end='\n\n')

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [' '.join(i) for outer in names for i in outer]
print(new_names, end='\n\n')


def slope(delta, y2, y1, x2, x1):
    return delta(y2, y1) / delta(x2, x1)


myslope = slope(lambda a, b: a -b, 8, 4, 4, 2)
print(myslope)