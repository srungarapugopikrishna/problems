
input = 'abcaacd'


def replace_inplace(input):
    aux = list(set(list(input)))
    input = list(input)
    for idx, item in enumerate(input[:]):
        if item in aux:
            aux.remove(item)
        else:
            input[idx] = ''
    return ''.join(input)


print replace_inplace(input)
