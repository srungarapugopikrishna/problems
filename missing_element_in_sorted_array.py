input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]


def find_element(input, i, j):
    if i < j and j <= len(input):
        mid = (i+j)/2
        if mid+1 == input[mid]:
            return find_element(input, mid+1, j)
        else:
            return find_element(input, i, mid)
    else:
        return i+1


print find_element(input, 0, len(input))
