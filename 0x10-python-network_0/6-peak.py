#!/usr/bin/python3
"""  A function that finds a peak
in a list of unsorted integers. """


def find_peak(list_of_integers):
    """Finds a peak in a list of integers."""
    if not list_of_integers:
        return None

    i, j = 0, len(list_of_integers) - 1

    while i < j:
        mid = (i + j) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            i = mid + 1
        else:
            j = mid

    return list_of_integers[i]
