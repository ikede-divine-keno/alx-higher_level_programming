#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for val in range(0, x):
            print(my_list[val], end='')
        print('')
        return (x)
    except:
        print('')
        return (val)
