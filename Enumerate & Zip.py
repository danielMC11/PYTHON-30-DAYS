
even_numbers = [i for i in range(25) if i % 2 == 0]

for index, item in enumerate(even_numbers, 1): # Second Argument defines start position
    print(f'Pos: {index}, Value: {item}')


from string import ascii_uppercase as letters_up


try:

    mydict = dict()
    for item_l1, item_l2 in zip(letters_up, [i for i in list(filter(lambda x: x % 2 == 0, list(range(0, 25))))]): # traverse two list items simultaneously
        mydict[item_l1] = item_l2

except Exception as e:
    print(e, type(e))
else:
    print(mydict)