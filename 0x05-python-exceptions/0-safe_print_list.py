#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    val = 0
    try:
        for elem in range(0, x):
            print(my_list[elem], end='')
            val += 1
            for x in range(0, val):
                print("", end='')
        print('')
        return (val)
    except IndexError:
        print('')
        return (val)
