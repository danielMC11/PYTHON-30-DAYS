
def outer_func(a,  b):
    c = a + b

    def inner_func(d):
        print(f'C + D = {c + d}')
    return inner_func


r_in_func = outer_func(2, 3)
r_in_func(5)


def decorator_funct(funct):
    def wrapper(*args):
        print(list(map(lambda x: x**2, list(args))))
        print(funct(*list(args)[:2]))
    return wrapper


@decorator_funct
def bythree(a, b):
    mylist = [a**3, b**3]
    return mylist


bythree(2, 3, 4, 5, 6)
