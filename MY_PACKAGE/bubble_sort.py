
def sort_ascending(iterable):
    for i in range(len(iterable) - 1):
        for j in range(len(iterable) - i - 1):
            if iterable[j] > iterable[j + 1]:
                temp = iterable[j]
                iterable[j] = iterable[j + 1]
                iterable[j + 1] = temp


def sort_descending(iterable):
    for i in range(len(iterable) - 1):
        for j in range(len(iterable) - i - 1):
            if iterable[j] < iterable[j + 1]:
                temp = iterable[j]
                iterable[j] = iterable[j + 1]
                iterable[j + 1] = temp


