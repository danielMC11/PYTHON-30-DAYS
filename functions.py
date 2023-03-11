
def is_prime(number):

    if number == 1:
        return  False

    for i in range(1, number+1):
        if number % i == 0 and i != 1 and i != number:
            return False
    return True

for i in range(1, 101):
    print(i, 'is prime', is_prime(i))

