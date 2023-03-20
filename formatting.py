"""
a = 3
b = 2
print('%s + %s = %s' %(a, b, a+b))
print('{} + {} = {}'.format(a, b, a+b))
print(f'{a} + {b} = {a+b}')
#embeding a str in a str must be interchangeable: f' text {" ".join()}' or f" text {' ',join()}"
"""
"""
#unpacking a sequence into single character
myList = ['Daniel','Montero',19,'Unillanos','Systems Engineering']
name, lastName, age, university, career = myList
print(name, lastName, age, university, career)
print(myList[1::2])
"""
"""
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' space '.join(web_tech)
print(result)
"""

def pack(*arg):
    print('Packing in Tuple')
    print(arg)
    print(type(arg))


def packdoublestar(**arg):
    print('Packing in Dictionary')
    print(arg)
    print(type(arg))


def unpack(a, b, c):
    print('Unpacking')
    print(a, b, c)
    print(type(a), type(b), type(c))


def pack_kw(**kwargs):
    return unpack_kw(*kwargs.keys())


def unpack_kw(a, b):
    print(a, b)
    print(type(a), type(b))


pack_kw(a=1, b=2)

"""
pack(1, 2, 3, 4, 5)
myList = [1, 2, 3]
unpack(*myList)

packdoublestar(uno=1, dos=2, tres=3)
myDict = {'a': 1.9, 'b': 2, 'c': 3}
unpack(**myDict)
"""





"""
a, *b, c, d = 1, 2, 3, 4, 5
print(a, b ,c ,d)
"""