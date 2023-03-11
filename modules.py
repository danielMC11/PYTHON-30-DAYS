from random import randint as ran
from string import ascii_lowercase as letterLow, ascii_uppercase as letterUp, digits as dig


def random_user_id():

    number_of_characters = int(input('Number of Characters: '))
    number_of_ids = int(input('Number of IDs: '))

    list_seq = list()
    seq = list()
    for i in range(number_of_ids):
        seq.clear()
        for j in range(number_of_characters):
            if ran(0, 1) == 0: #Number
                seq.append(str(dig[ran(0, len(dig)-1)]))
            elif ran(0, 1) == 0: #Letter
                seq.append(str(letterLow[ran(0, len(letterLow)-1)]))
            else:
                seq.append(str(letterUp[ran(0, len(letterUp)-1)]))
        str_seq = ''.join(seq)
        list_seq.append(str_seq)

    res_seq = '\n'.join(list_seq)
    print(res_seq)

def seven_unique_ran():

    sequence = list()

    while len(sequence) < 7:
        n = ran(0, 9)
        if n not in sequence:
            sequence.append(n)

    print(sequence)

random_user_id()

