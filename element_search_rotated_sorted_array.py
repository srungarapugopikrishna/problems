"""
Given a rotated array which is sorted 
search for an element in it
"""

arr = [13, 15, 19, 20, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12]
search_for = 13


def search_for_element(arr, i, j, element):
    if i < j:
        mid = (i + j) / 2
        if arr[mid] == element:
            return True
        if arr[mid] < element:
            return search_for_element(arr, mid+1, j, element)
        if arr[mid] > element:
            return search_for_element(arr, i, mid, element)
    return False


def find_rotated_point(arr, i, j):
    mid = (i+j)/2
    if arr[mid] > arr[-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    elif arr[mid] < arr[-1] and arr[mid] < arr[mid-1]:
        return arr[mid-1]
    elif arr[mid] < arr[-1]:
        return find_rotated_point(arr, 0, mid)
    else:
        return find_rotated_point(arr, mid, len(arr))


index = arr.index(find_rotated_point(arr, 0, len(arr)))
if search_for >= arr[0]:
    print search_for_element(arr, 0, index, search_for)
else:
    print search_for_element(arr, index+1, len(arr), search_for)
