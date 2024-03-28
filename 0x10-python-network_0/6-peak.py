#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: A list of integers.

    Returns:
        The peak or None if no peak was found.

    Complexity: O(log n)
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left <= right:
        pivot = (left + right) // 2

        if (list_of_integers[pivot] > list_of_integers[pivot-1]
                and list_of_integers[pivot] > list_of_integers[pivot+1]):
            return list_of_integers[pivot]

        if list_of_integers[pivot-1] < list_of_integers[pivot]:
            left = pivot + 1

        else:
            right = pivot - 1

    return list_of_integers[left]
