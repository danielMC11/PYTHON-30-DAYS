"""
#tuple guide
# functions with tuples, .count() .index and concatenation with +
brothers = ('Andres', 'Daniel')
sisters = ('Isabella', 'Maria')
siblings = brothers + sisters
print('Number of Siblings:', len(siblings))

family_members = list(siblings)
family_members.extend(['Antonio', 'Magda'])
family_members = tuple(family_members)
print('Family members:', family_members)

ElderBro, YoungerBro, ElderSis, YoungerSis, Dad, Mom = family_members

fruit_products = ('banana', 'apple', 'orange')
vegetable_products = ('carrot', 'onion', 'tomato')
animal_products = ('pork chops', 'beef', 'eggs')

food_stuff_tp = fruit_products + vegetable_products + animal_products
food_stuff_list = list(food_stuff_tp)
print('Food Stuff:', food_stuff_list)

middle_item = food_stuff_list[len(food_stuff_list)//2]
print('Middle Item:', middle_item)

first_three = food_stuff_list[:3]
last_three = food_stuff_list[-3:]
print('First Three Items:', first_three, 'Last Three Items:', last_three)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(' Is Estonia a Nordic Country ?', 'Estonia' in nordic_countries, 'Is Iceland a Nordic Country ?', 'Iceland' in nordic_countries)
"""
